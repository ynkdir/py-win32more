from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Imaging
import Windows.Media
import Windows.Media.Capture
import Windows.Media.Capture.Frames
import Windows.Media.Devices
import Windows.Media.Devices.Core
import Windows.Media.MediaProperties
import Windows.Perception.Spatial
import Windows.Storage.Streams
import Windows.UI.WindowManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AudioMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.AudioMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: Windows.Media.Capture.Frames.IAudioMediaFrame) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_AudioEncodingProperties(self: Windows.Media.Capture.Frames.IAudioMediaFrame) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def GetAudioFrame(self: Windows.Media.Capture.Frames.IAudioMediaFrame) -> Windows.Media.AudioFrame: ...
    FrameReference = property(get_FrameReference, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class BufferMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.BufferMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: Windows.Media.Capture.Frames.IBufferMediaFrame) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_Buffer(self: Windows.Media.Capture.Frames.IBufferMediaFrame) -> Windows.Storage.Streams.IBuffer: ...
    FrameReference = property(get_FrameReference, None)
    Buffer = property(get_Buffer, None)
class DepthMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.DepthMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: Windows.Media.Capture.Frames.IDepthMediaFrame) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: Windows.Media.Capture.Frames.IDepthMediaFrame) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_DepthFormat(self: Windows.Media.Capture.Frames.IDepthMediaFrame) -> Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_mixinmethod
    def TryCreateCoordinateMapper(self: Windows.Media.Capture.Frames.IDepthMediaFrame, cameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper: ...
    @winrt_mixinmethod
    def get_MaxReliableDepth(self: Windows.Media.Capture.Frames.IDepthMediaFrame2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinReliableDepth(self: Windows.Media.Capture.Frames.IDepthMediaFrame2) -> UInt32: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    DepthFormat = property(get_DepthFormat, None)
    MaxReliableDepth = property(get_MaxReliableDepth, None)
    MinReliableDepth = property(get_MinReliableDepth, None)
class DepthMediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.DepthMediaFrameFormat'
    @winrt_mixinmethod
    def get_VideoFormat(self: Windows.Media.Capture.Frames.IDepthMediaFrameFormat) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_DepthScaleInMeters(self: Windows.Media.Capture.Frames.IDepthMediaFrameFormat) -> Double: ...
    VideoFormat = property(get_VideoFormat, None)
    DepthScaleInMeters = property(get_DepthScaleInMeters, None)
class IAudioMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a3a9feff-8021-441b-9a-46-e7-f0-13-7b-79-81')
    @winrt_commethod(6)
    def get_FrameReference(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_AudioEncodingProperties(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(8)
    def GetAudioFrame(self) -> Windows.Media.AudioFrame: ...
    FrameReference = property(get_FrameReference, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class IBufferMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b5b153c7-9b84-4062-b7-9c-a3-65-b2-59-68-54')
    @winrt_commethod(6)
    def get_FrameReference(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_Buffer(self) -> Windows.Storage.Streams.IBuffer: ...
    FrameReference = property(get_FrameReference, None)
    Buffer = property(get_Buffer, None)
class IDepthMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47135e4f-8549-45c0-92-5b-80-d3-5e-fd-b1-0a')
    @winrt_commethod(6)
    def get_FrameReference(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoMediaFrame(self) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(8)
    def get_DepthFormat(self) -> Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_commethod(9)
    def TryCreateCoordinateMapper(self, cameraIntrinsics: Windows.Media.Devices.Core.CameraIntrinsics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    DepthFormat = property(get_DepthFormat, None)
class IDepthMediaFrame2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6cca473d-c4a4-4176-b0-cd-33-ea-e3-b3-5a-a3')
    @winrt_commethod(6)
    def get_MaxReliableDepth(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MinReliableDepth(self) -> UInt32: ...
    MaxReliableDepth = property(get_MaxReliableDepth, None)
    MinReliableDepth = property(get_MinReliableDepth, None)
class IDepthMediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c312cf40-d729-453e-87-80-2e-04-f1-40-d2-8e')
    @winrt_commethod(6)
    def get_VideoFormat(self) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_commethod(7)
    def get_DepthScaleInMeters(self) -> Double: ...
    VideoFormat = property(get_VideoFormat, None)
    DepthScaleInMeters = property(get_DepthScaleInMeters, None)
class IInfraredMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3fd13503-004b-4f0e-91-ac-46-52-99-b4-16-58')
    @winrt_commethod(6)
    def get_FrameReference(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoMediaFrame(self) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(8)
    def get_IsIlluminated(self) -> Boolean: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    IsIlluminated = property(get_IsIlluminated, None)
class IMediaFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0b430add-a490-4435-ad-a1-9a-ff-d5-52-39-f7')
class IMediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71902b4e-b279-4a97-a9-db-bd-5a-2f-b7-8f-39')
    @winrt_commethod(6)
    def get_MajorType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Subtype(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(9)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(10)
    def get_VideoFormat(self) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    MajorType = property(get_MajorType, None)
    Subtype = property(get_Subtype, None)
    FrameRate = property(get_FrameRate, None)
    Properties = property(get_Properties, None)
    VideoFormat = property(get_VideoFormat, None)
class IMediaFrameFormat2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63856340-5e87-4c10-86-d1-6d-f0-97-a6-c6-a8')
    @winrt_commethod(6)
    def get_AudioEncodingProperties(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class IMediaFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e4c94395-2028-48ed-90-b0-d1-c1-b1-62-e2-4c')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MediaFrameReader, Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrame(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(9)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReaderStartStatus]: ...
    @winrt_commethod(10)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IMediaFrameReader2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('871127b3-8531-4050-87-cc-a1-37-33-cf-3e-9b')
    @winrt_commethod(6)
    def put_AcquisitionMode(self, value: Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_commethod(7)
    def get_AcquisitionMode(self) -> Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
class IMediaFrameReference(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6b88641-f0dc-4044-8d-c9-96-1c-ed-d0-5b-ad')
    @winrt_commethod(6)
    def get_SourceKind(self) -> Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_commethod(7)
    def get_Format(self) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(8)
    def get_SystemRelativeTime(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(11)
    def get_BufferMediaFrame(self) -> Windows.Media.Capture.Frames.BufferMediaFrame: ...
    @winrt_commethod(12)
    def get_VideoMediaFrame(self) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(13)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    SourceKind = property(get_SourceKind, None)
    Format = property(get_Format, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    Duration = property(get_Duration, None)
    Properties = property(get_Properties, None)
    BufferMediaFrame = property(get_BufferMediaFrame, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
class IMediaFrameReference2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ddbc3ecc-d5b2-49ef-83-6a-94-7d-98-9b-80-c1')
    @winrt_commethod(6)
    def get_AudioMediaFrame(self) -> Windows.Media.Capture.Frames.AudioMediaFrame: ...
    AudioMediaFrame = property(get_AudioMediaFrame, None)
class IMediaFrameSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d6782953-90db-46a8-8a-dd-2a-a8-84-a8-d2-53')
    @winrt_commethod(6)
    def get_Info(self) -> Windows.Media.Capture.Frames.MediaFrameSourceInfo: ...
    @winrt_commethod(7)
    def get_Controller(self) -> Windows.Media.Capture.Frames.MediaFrameSourceController: ...
    @winrt_commethod(8)
    def get_SupportedFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameFormat]: ...
    @winrt_commethod(9)
    def get_CurrentFormat(self) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(10)
    def SetFormatAsync(self, format: Windows.Media.Capture.Frames.MediaFrameFormat) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def add_FormatChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MediaFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_FormatChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def TryGetCameraIntrinsics(self, format: Windows.Media.Capture.Frames.MediaFrameFormat) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    Info = property(get_Info, None)
    Controller = property(get_Controller, None)
    SupportedFormats = property(get_SupportedFormats, None)
    CurrentFormat = property(get_CurrentFormat, None)
class IMediaFrameSourceController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6d076635-316d-4b8f-b7-b6-ee-b0-4a-8c-65-25')
    @winrt_commethod(6)
    def GetPropertyAsync(self, propertyId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_commethod(7)
    def SetPropertyAsync(self, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_commethod(8)
    def get_VideoDeviceController(self) -> Windows.Media.Devices.VideoDeviceController: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
class IMediaFrameSourceController2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('efc49fd4-fcf2-4a03-b4-e4-ac-96-28-73-9b-ee')
    @winrt_commethod(6)
    def GetPropertyByExtendedIdAsync(self, extendedPropertyId: c_char_p_no, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_commethod(7)
    def SetPropertyByExtendedIdAsync(self, extendedPropertyId: c_char_p_no, propertyValue: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
class IMediaFrameSourceController3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1f0cf815-2464-4651-b1-e8-4a-82-db-db-54-de')
    @winrt_commethod(6)
    def get_AudioDeviceController(self) -> Windows.Media.Devices.AudioDeviceController: ...
    AudioDeviceController = property(get_AudioDeviceController, None)
class IMediaFrameSourceGetPropertyResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('088616c2-3a64-4bd5-bd-2b-e7-c8-98-d2-f3-7a')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IMediaFrameSourceGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7f605b87-4832-4b5f-ae-3d-41-2f-aa-b3-7d-34')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SourceInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    SourceInfos = property(get_SourceInfos, None)
class IMediaFrameSourceGroupStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c48bfc5-436f-4508-94-cf-d5-d8-b7-32-64-45')
    @winrt_commethod(6)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceGroup]]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGroup]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMediaFrameSourceInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('87bdc9cd-4601-408f-91-cf-03-83-18-cd-0a-f3')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MediaStreamType(self) -> Windows.Media.Capture.MediaStreamType: ...
    @winrt_commethod(8)
    def get_SourceKind(self) -> Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_commethod(9)
    def get_SourceGroup(self) -> Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_commethod(10)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    Id = property(get_Id, None)
    MediaStreamType = property(get_MediaStreamType, None)
    SourceKind = property(get_SourceKind, None)
    SourceGroup = property(get_SourceGroup, None)
    DeviceInformation = property(get_DeviceInformation, None)
    Properties = property(get_Properties, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
class IMediaFrameSourceInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('195a7855-6457-42c6-a7-69-19-b6-5b-d3-2e-6e')
    @winrt_commethod(6)
    def get_ProfileId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoProfileMediaDescription(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    ProfileId = property(get_ProfileId, None)
    VideoProfileMediaDescription = property(get_VideoProfileMediaDescription, None)
class IMediaFrameSourceInfo3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca824ab6-66ea-5885-a2-b6-26-c0-ee-ec-3c-7b')
    @winrt_commethod(6)
    def GetRelativePanel(self, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Windows.Devices.Enumeration.Panel: ...
class IMediaFrameSourceInfo4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4817d721-85eb-470c-8f-37-43-ca-54-98-e4-1d')
    @winrt_commethod(6)
    def get_IsShareable(self) -> Boolean: ...
    IsShareable = property(get_IsShareable, None)
class IMultiSourceMediaFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63115e01-cf51-48fd-aa-b0-6d-69-3e-b4-81-27')
class IMultiSourceMediaFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d144402-f763-488d-98-f2-b4-37-bc-f0-75-e7')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MultiSourceMediaFrameReader, Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrame(self) -> Windows.Media.Capture.Frames.MultiSourceMediaFrameReference: ...
    @winrt_commethod(9)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MultiSourceMediaFrameReaderStartStatus]: ...
    @winrt_commethod(10)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IMultiSourceMediaFrameReader2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef5c8abd-fc5c-4c6b-9d-81-3c-b9-cc-63-7c-26')
    @winrt_commethod(6)
    def put_AcquisitionMode(self, value: Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_commethod(7)
    def get_AcquisitionMode(self) -> Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
class IMultiSourceMediaFrameReference(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('21964b1a-7fe2-44d6-92-e5-29-8e-6d-28-10-e9')
    @winrt_commethod(6)
    def TryGetFrameReferenceBySourceId(self, sourceId: WinRT_String) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
class IVideoMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00dd4ccb-32bd-4fe1-a0-13-7c-c1-3c-f5-db-cf')
    @winrt_commethod(6)
    def get_FrameReference(self) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoFormat(self) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_commethod(8)
    def get_SoftwareBitmap(self) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(9)
    def get_Direct3DSurface(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(10)
    def get_CameraIntrinsics(self) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(11)
    def get_InfraredMediaFrame(self) -> Windows.Media.Capture.Frames.InfraredMediaFrame: ...
    @winrt_commethod(12)
    def get_DepthMediaFrame(self) -> Windows.Media.Capture.Frames.DepthMediaFrame: ...
    @winrt_commethod(13)
    def GetVideoFrame(self) -> Windows.Media.VideoFrame: ...
    FrameReference = property(get_FrameReference, None)
    VideoFormat = property(get_VideoFormat, None)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    Direct3DSurface = property(get_Direct3DSurface, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    InfraredMediaFrame = property(get_InfraredMediaFrame, None)
    DepthMediaFrame = property(get_DepthMediaFrame, None)
class IVideoMediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('46027fc0-d71b-45c7-8f-14-6d-9a-0a-e6-04-e4')
    @winrt_commethod(6)
    def get_MediaFrameFormat(self) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(7)
    def get_DepthFormat(self) -> Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    MediaFrameFormat = property(get_MediaFrameFormat, None)
    DepthFormat = property(get_DepthFormat, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
class InfraredMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.InfraredMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: Windows.Media.Capture.Frames.IInfraredMediaFrame) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: Windows.Media.Capture.Frames.IInfraredMediaFrame) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_IsIlluminated(self: Windows.Media.Capture.Frames.IInfraredMediaFrame) -> Boolean: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    IsIlluminated = property(get_IsIlluminated, None)
class MediaFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs'
class MediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameFormat'
    @winrt_mixinmethod
    def get_MajorType(self: Windows.Media.Capture.Frames.IMediaFrameFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.Capture.Frames.IMediaFrameFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameRate(self: Windows.Media.Capture.Frames.IMediaFrameFormat) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Capture.Frames.IMediaFrameFormat) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_VideoFormat(self: Windows.Media.Capture.Frames.IMediaFrameFormat) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_AudioEncodingProperties(self: Windows.Media.Capture.Frames.IMediaFrameFormat2) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    MajorType = property(get_MajorType, None)
    Subtype = property(get_Subtype, None)
    FrameRate = property(get_FrameRate, None)
    Properties = property(get_Properties, None)
    VideoFormat = property(get_VideoFormat, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class MediaFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Media.Capture.Frames.IMediaFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MediaFrameReader, Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Media.Capture.Frames.IMediaFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrame(self: Windows.Media.Capture.Frames.IMediaFrameReader) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Capture.Frames.IMediaFrameReader) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReaderStartStatus]: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.Capture.Frames.IMediaFrameReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_AcquisitionMode(self: Windows.Media.Capture.Frames.IMediaFrameReader2, value: Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AcquisitionMode(self: Windows.Media.Capture.Frames.IMediaFrameReader2) -> Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
MediaFrameReaderAcquisitionMode = Int32
MediaFrameReaderAcquisitionMode_Realtime: MediaFrameReaderAcquisitionMode = 0
MediaFrameReaderAcquisitionMode_Buffered: MediaFrameReaderAcquisitionMode = 1
MediaFrameReaderStartStatus = Int32
MediaFrameReaderStartStatus_Success: MediaFrameReaderStartStatus = 0
MediaFrameReaderStartStatus_UnknownFailure: MediaFrameReaderStartStatus = 1
MediaFrameReaderStartStatus_DeviceNotAvailable: MediaFrameReaderStartStatus = 2
MediaFrameReaderStartStatus_OutputFormatNotSupported: MediaFrameReaderStartStatus = 3
MediaFrameReaderStartStatus_ExclusiveControlNotAvailable: MediaFrameReaderStartStatus = 4
class MediaFrameReference(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameReference'
    @winrt_mixinmethod
    def get_SourceKind(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_BufferMediaFrame(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Media.Capture.Frames.BufferMediaFrame: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Media.Capture.Frames.IMediaFrameReference) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_AudioMediaFrame(self: Windows.Media.Capture.Frames.IMediaFrameReference2) -> Windows.Media.Capture.Frames.AudioMediaFrame: ...
    SourceKind = property(get_SourceKind, None)
    Format = property(get_Format, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    Duration = property(get_Duration, None)
    Properties = property(get_Properties, None)
    BufferMediaFrame = property(get_BufferMediaFrame, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    AudioMediaFrame = property(get_AudioMediaFrame, None)
class MediaFrameSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameSource'
    @winrt_mixinmethod
    def get_Info(self: Windows.Media.Capture.Frames.IMediaFrameSource) -> Windows.Media.Capture.Frames.MediaFrameSourceInfo: ...
    @winrt_mixinmethod
    def get_Controller(self: Windows.Media.Capture.Frames.IMediaFrameSource) -> Windows.Media.Capture.Frames.MediaFrameSourceController: ...
    @winrt_mixinmethod
    def get_SupportedFormats(self: Windows.Media.Capture.Frames.IMediaFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameFormat]: ...
    @winrt_mixinmethod
    def get_CurrentFormat(self: Windows.Media.Capture.Frames.IMediaFrameSource) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def SetFormatAsync(self: Windows.Media.Capture.Frames.IMediaFrameSource, format: Windows.Media.Capture.Frames.MediaFrameFormat) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_FormatChanged(self: Windows.Media.Capture.Frames.IMediaFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MediaFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FormatChanged(self: Windows.Media.Capture.Frames.IMediaFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryGetCameraIntrinsics(self: Windows.Media.Capture.Frames.IMediaFrameSource, format: Windows.Media.Capture.Frames.MediaFrameFormat) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    Info = property(get_Info, None)
    Controller = property(get_Controller, None)
    SupportedFormats = property(get_SupportedFormats, None)
    CurrentFormat = property(get_CurrentFormat, None)
class MediaFrameSourceController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameSourceController'
    @winrt_mixinmethod
    def GetPropertyAsync(self: Windows.Media.Capture.Frames.IMediaFrameSourceController, propertyId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_mixinmethod
    def SetPropertyAsync(self: Windows.Media.Capture.Frames.IMediaFrameSourceController, propertyId: WinRT_String, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_mixinmethod
    def get_VideoDeviceController(self: Windows.Media.Capture.Frames.IMediaFrameSourceController) -> Windows.Media.Devices.VideoDeviceController: ...
    @winrt_mixinmethod
    def GetPropertyByExtendedIdAsync(self: Windows.Media.Capture.Frames.IMediaFrameSourceController2, extendedPropertyId: c_char_p_no, maxPropertyValueSize: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_mixinmethod
    def SetPropertyByExtendedIdAsync(self: Windows.Media.Capture.Frames.IMediaFrameSourceController2, extendedPropertyId: c_char_p_no, propertyValue: c_char_p_no) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_mixinmethod
    def get_AudioDeviceController(self: Windows.Media.Capture.Frames.IMediaFrameSourceController3) -> Windows.Media.Devices.AudioDeviceController: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    AudioDeviceController = property(get_AudioDeviceController, None)
class MediaFrameSourceGetPropertyResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult) -> Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
MediaFrameSourceGetPropertyStatus = Int32
MediaFrameSourceGetPropertyStatus_Success: MediaFrameSourceGetPropertyStatus = 0
MediaFrameSourceGetPropertyStatus_UnknownFailure: MediaFrameSourceGetPropertyStatus = 1
MediaFrameSourceGetPropertyStatus_NotSupported: MediaFrameSourceGetPropertyStatus = 2
MediaFrameSourceGetPropertyStatus_DeviceNotAvailable: MediaFrameSourceGetPropertyStatus = 3
MediaFrameSourceGetPropertyStatus_MaxPropertyValueSizeTooSmall: MediaFrameSourceGetPropertyStatus = 4
MediaFrameSourceGetPropertyStatus_MaxPropertyValueSizeRequired: MediaFrameSourceGetPropertyStatus = 5
class MediaFrameSourceGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameSourceGroup'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceInfos(self: Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceGroup]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameSourceGroup]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    SourceInfos = property(get_SourceInfos, None)
class MediaFrameSourceInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MediaFrameSourceInfo'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MediaStreamType(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Media.Capture.MediaStreamType: ...
    @winrt_mixinmethod
    def get_SourceKind(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_mixinmethod
    def get_SourceGroup(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_ProfileId(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoProfileMediaDescription(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def GetRelativePanel(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo3, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def get_IsShareable(self: Windows.Media.Capture.Frames.IMediaFrameSourceInfo4) -> Boolean: ...
    Id = property(get_Id, None)
    MediaStreamType = property(get_MediaStreamType, None)
    SourceKind = property(get_SourceKind, None)
    SourceGroup = property(get_SourceGroup, None)
    DeviceInformation = property(get_DeviceInformation, None)
    Properties = property(get_Properties, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    ProfileId = property(get_ProfileId, None)
    VideoProfileMediaDescription = property(get_VideoProfileMediaDescription, None)
    IsShareable = property(get_IsShareable, None)
MediaFrameSourceKind = Int32
MediaFrameSourceKind_Custom: MediaFrameSourceKind = 0
MediaFrameSourceKind_Color: MediaFrameSourceKind = 1
MediaFrameSourceKind_Infrared: MediaFrameSourceKind = 2
MediaFrameSourceKind_Depth: MediaFrameSourceKind = 3
MediaFrameSourceKind_Audio: MediaFrameSourceKind = 4
MediaFrameSourceKind_Image: MediaFrameSourceKind = 5
MediaFrameSourceKind_Metadata: MediaFrameSourceKind = 6
MediaFrameSourceSetPropertyStatus = Int32
MediaFrameSourceSetPropertyStatus_Success: MediaFrameSourceSetPropertyStatus = 0
MediaFrameSourceSetPropertyStatus_UnknownFailure: MediaFrameSourceSetPropertyStatus = 1
MediaFrameSourceSetPropertyStatus_NotSupported: MediaFrameSourceSetPropertyStatus = 2
MediaFrameSourceSetPropertyStatus_InvalidValue: MediaFrameSourceSetPropertyStatus = 3
MediaFrameSourceSetPropertyStatus_DeviceNotAvailable: MediaFrameSourceSetPropertyStatus = 4
MediaFrameSourceSetPropertyStatus_NotInControl: MediaFrameSourceSetPropertyStatus = 5
class MultiSourceMediaFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs'
class MultiSourceMediaFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Frames.MultiSourceMediaFrameReader, Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrame(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> Windows.Media.Capture.Frames.MultiSourceMediaFrameReference: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MultiSourceMediaFrameReaderStartStatus]: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_AcquisitionMode(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader2, value: Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AcquisitionMode(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader2) -> Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
MultiSourceMediaFrameReaderStartStatus = Int32
MultiSourceMediaFrameReaderStartStatus_Success: MultiSourceMediaFrameReaderStartStatus = 0
MultiSourceMediaFrameReaderStartStatus_NotSupported: MultiSourceMediaFrameReaderStartStatus = 1
MultiSourceMediaFrameReaderStartStatus_InsufficientResources: MultiSourceMediaFrameReaderStartStatus = 2
MultiSourceMediaFrameReaderStartStatus_DeviceNotAvailable: MultiSourceMediaFrameReaderStartStatus = 3
MultiSourceMediaFrameReaderStartStatus_UnknownFailure: MultiSourceMediaFrameReaderStartStatus = 4
class MultiSourceMediaFrameReference(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameReference'
    @winrt_mixinmethod
    def TryGetFrameReferenceBySourceId(self: Windows.Media.Capture.Frames.IMultiSourceMediaFrameReference, sourceId: WinRT_String) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class VideoMediaFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.VideoMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoFormat(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_Direct3DSurface(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def get_InfraredMediaFrame(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.Capture.Frames.InfraredMediaFrame: ...
    @winrt_mixinmethod
    def get_DepthMediaFrame(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.Capture.Frames.DepthMediaFrame: ...
    @winrt_mixinmethod
    def GetVideoFrame(self: Windows.Media.Capture.Frames.IVideoMediaFrame) -> Windows.Media.VideoFrame: ...
    FrameReference = property(get_FrameReference, None)
    VideoFormat = property(get_VideoFormat, None)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    Direct3DSurface = property(get_Direct3DSurface, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    InfraredMediaFrame = property(get_InfraredMediaFrame, None)
    DepthMediaFrame = property(get_DepthMediaFrame, None)
class VideoMediaFrameFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Frames.VideoMediaFrameFormat'
    @winrt_mixinmethod
    def get_MediaFrameFormat(self: Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def get_DepthFormat(self: Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> UInt32: ...
    MediaFrameFormat = property(get_MediaFrameFormat, None)
    DepthFormat = property(get_DepthFormat, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
make_head(_module, 'AudioMediaFrame')
make_head(_module, 'BufferMediaFrame')
make_head(_module, 'DepthMediaFrame')
make_head(_module, 'DepthMediaFrameFormat')
make_head(_module, 'IAudioMediaFrame')
make_head(_module, 'IBufferMediaFrame')
make_head(_module, 'IDepthMediaFrame')
make_head(_module, 'IDepthMediaFrame2')
make_head(_module, 'IDepthMediaFrameFormat')
make_head(_module, 'IInfraredMediaFrame')
make_head(_module, 'IMediaFrameArrivedEventArgs')
make_head(_module, 'IMediaFrameFormat')
make_head(_module, 'IMediaFrameFormat2')
make_head(_module, 'IMediaFrameReader')
make_head(_module, 'IMediaFrameReader2')
make_head(_module, 'IMediaFrameReference')
make_head(_module, 'IMediaFrameReference2')
make_head(_module, 'IMediaFrameSource')
make_head(_module, 'IMediaFrameSourceController')
make_head(_module, 'IMediaFrameSourceController2')
make_head(_module, 'IMediaFrameSourceController3')
make_head(_module, 'IMediaFrameSourceGetPropertyResult')
make_head(_module, 'IMediaFrameSourceGroup')
make_head(_module, 'IMediaFrameSourceGroupStatics')
make_head(_module, 'IMediaFrameSourceInfo')
make_head(_module, 'IMediaFrameSourceInfo2')
make_head(_module, 'IMediaFrameSourceInfo3')
make_head(_module, 'IMediaFrameSourceInfo4')
make_head(_module, 'IMultiSourceMediaFrameArrivedEventArgs')
make_head(_module, 'IMultiSourceMediaFrameReader')
make_head(_module, 'IMultiSourceMediaFrameReader2')
make_head(_module, 'IMultiSourceMediaFrameReference')
make_head(_module, 'IVideoMediaFrame')
make_head(_module, 'IVideoMediaFrameFormat')
make_head(_module, 'InfraredMediaFrame')
make_head(_module, 'MediaFrameArrivedEventArgs')
make_head(_module, 'MediaFrameFormat')
make_head(_module, 'MediaFrameReader')
make_head(_module, 'MediaFrameReference')
make_head(_module, 'MediaFrameSource')
make_head(_module, 'MediaFrameSourceController')
make_head(_module, 'MediaFrameSourceGetPropertyResult')
make_head(_module, 'MediaFrameSourceGroup')
make_head(_module, 'MediaFrameSourceInfo')
make_head(_module, 'MultiSourceMediaFrameArrivedEventArgs')
make_head(_module, 'MultiSourceMediaFrameReader')
make_head(_module, 'MultiSourceMediaFrameReference')
make_head(_module, 'VideoMediaFrame')
make_head(_module, 'VideoMediaFrameFormat')
