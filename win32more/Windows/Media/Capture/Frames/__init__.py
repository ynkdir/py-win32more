from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Capture.Frames
import win32more.Windows.Media.Devices
import win32more.Windows.Media.Devices.Core
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Perception.Spatial
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.WindowManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AudioMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IAudioMediaFrame
    _classid_ = 'Windows.Media.Capture.Frames.AudioMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: win32more.Windows.Media.Capture.Frames.IAudioMediaFrame) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_AudioEncodingProperties(self: win32more.Windows.Media.Capture.Frames.IAudioMediaFrame) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def GetAudioFrame(self: win32more.Windows.Media.Capture.Frames.IAudioMediaFrame) -> win32more.Windows.Media.AudioFrame: ...
    FrameReference = property(get_FrameReference, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class BufferMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IBufferMediaFrame
    _classid_ = 'Windows.Media.Capture.Frames.BufferMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: win32more.Windows.Media.Capture.Frames.IBufferMediaFrame) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Windows.Media.Capture.Frames.IBufferMediaFrame) -> win32more.Windows.Storage.Streams.IBuffer: ...
    FrameReference = property(get_FrameReference, None)
    Buffer = property(get_Buffer, None)
class DepthMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame
    _classid_ = 'Windows.Media.Capture.Frames.DepthMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_DepthFormat(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_mixinmethod
    def TryCreateCoordinateMapper(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame, cameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper: ...
    @winrt_mixinmethod
    def get_MaxReliableDepth(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinReliableDepth(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrame2) -> UInt32: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    DepthFormat = property(get_DepthFormat, None)
    MaxReliableDepth = property(get_MaxReliableDepth, None)
    MinReliableDepth = property(get_MinReliableDepth, None)
class DepthMediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IDepthMediaFrameFormat
    _classid_ = 'Windows.Media.Capture.Frames.DepthMediaFrameFormat'
    @winrt_mixinmethod
    def get_VideoFormat(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrameFormat) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_DepthScaleInMeters(self: win32more.Windows.Media.Capture.Frames.IDepthMediaFrameFormat) -> Double: ...
    VideoFormat = property(get_VideoFormat, None)
    DepthScaleInMeters = property(get_DepthScaleInMeters, None)
class IAudioMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IAudioMediaFrame'
    _iid_ = Guid('{a3a9feff-8021-441b-9a46-e7f0137b7981}')
    @winrt_commethod(6)
    def get_FrameReference(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_AudioEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(8)
    def GetAudioFrame(self) -> win32more.Windows.Media.AudioFrame: ...
    FrameReference = property(get_FrameReference, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class IBufferMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IBufferMediaFrame'
    _iid_ = Guid('{b5b153c7-9b84-4062-b79c-a365b2596854}')
    @winrt_commethod(6)
    def get_FrameReference(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_Buffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    FrameReference = property(get_FrameReference, None)
    Buffer = property(get_Buffer, None)
class IDepthMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IDepthMediaFrame'
    _iid_ = Guid('{47135e4f-8549-45c0-925b-80d35efdb10a}')
    @winrt_commethod(6)
    def get_FrameReference(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(8)
    def get_DepthFormat(self) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_commethod(9)
    def TryCreateCoordinateMapper(self, cameraIntrinsics: win32more.Windows.Media.Devices.Core.CameraIntrinsics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Media.Devices.Core.DepthCorrelatedCoordinateMapper: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    DepthFormat = property(get_DepthFormat, None)
class IDepthMediaFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IDepthMediaFrame2'
    _iid_ = Guid('{6cca473d-c4a4-4176-b0cd-33eae3b35aa3}')
    @winrt_commethod(6)
    def get_MaxReliableDepth(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MinReliableDepth(self) -> UInt32: ...
    MaxReliableDepth = property(get_MaxReliableDepth, None)
    MinReliableDepth = property(get_MinReliableDepth, None)
class IDepthMediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IDepthMediaFrameFormat'
    _iid_ = Guid('{c312cf40-d729-453e-8780-2e04f140d28e}')
    @winrt_commethod(6)
    def get_VideoFormat(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_commethod(7)
    def get_DepthScaleInMeters(self) -> Double: ...
    VideoFormat = property(get_VideoFormat, None)
    DepthScaleInMeters = property(get_DepthScaleInMeters, None)
class IInfraredMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IInfraredMediaFrame'
    _iid_ = Guid('{3fd13503-004b-4f0e-91ac-465299b41658}')
    @winrt_commethod(6)
    def get_FrameReference(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(8)
    def get_IsIlluminated(self) -> Boolean: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    IsIlluminated = property(get_IsIlluminated, None)
class IMediaFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameArrivedEventArgs'
    _iid_ = Guid('{0b430add-a490-4435-ada1-9affd55239f7}')
class IMediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameFormat'
    _iid_ = Guid('{71902b4e-b279-4a97-a9db-bd5a2fb78f39}')
    @winrt_commethod(6)
    def get_MajorType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Subtype(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FrameRate(self) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(9)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(10)
    def get_VideoFormat(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    MajorType = property(get_MajorType, None)
    Subtype = property(get_Subtype, None)
    FrameRate = property(get_FrameRate, None)
    Properties = property(get_Properties, None)
    VideoFormat = property(get_VideoFormat, None)
class IMediaFrameFormat2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameFormat2'
    _iid_ = Guid('{63856340-5e87-4c10-86d1-6df097a6c6a8}')
    @winrt_commethod(6)
    def get_AudioEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class IMediaFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameReader'
    _iid_ = Guid('{e4c94395-2028-48ed-90b0-d1c1b162e24c}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MediaFrameReader, win32more.Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrame(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(9)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReaderStartStatus]: ...
    @winrt_commethod(10)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMediaFrameReader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameReader2'
    _iid_ = Guid('{871127b3-8531-4050-87cc-a13733cf3e9b}')
    @winrt_commethod(6)
    def put_AcquisitionMode(self, value: win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_commethod(7)
    def get_AcquisitionMode(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
class IMediaFrameReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameReference'
    _iid_ = Guid('{f6b88641-f0dc-4044-8dc9-961cedd05bad}')
    @winrt_commethod(6)
    def get_SourceKind(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_commethod(7)
    def get_Format(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(8)
    def get_SystemRelativeTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(11)
    def get_BufferMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.BufferMediaFrame: ...
    @winrt_commethod(12)
    def get_VideoMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_commethod(13)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    SourceKind = property(get_SourceKind, None)
    Format = property(get_Format, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    Duration = property(get_Duration, None)
    Properties = property(get_Properties, None)
    BufferMediaFrame = property(get_BufferMediaFrame, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
class IMediaFrameReference2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameReference2'
    _iid_ = Guid('{ddbc3ecc-d5b2-49ef-836a-947d989b80c1}')
    @winrt_commethod(6)
    def get_AudioMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.AudioMediaFrame: ...
    AudioMediaFrame = property(get_AudioMediaFrame, None)
class IMediaFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSource'
    _iid_ = Guid('{d6782953-90db-46a8-8add-2aa884a8d253}')
    @winrt_commethod(6)
    def get_Info(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo: ...
    @winrt_commethod(7)
    def get_Controller(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceController: ...
    @winrt_commethod(8)
    def get_SupportedFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameFormat]: ...
    @winrt_commethod(9)
    def get_CurrentFormat(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(10)
    def SetFormatAsync(self, format: win32more.Windows.Media.Capture.Frames.MediaFrameFormat) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def add_FormatChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MediaFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_FormatChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def TryGetCameraIntrinsics(self, format: win32more.Windows.Media.Capture.Frames.MediaFrameFormat) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    Info = property(get_Info, None)
    Controller = property(get_Controller, None)
    SupportedFormats = property(get_SupportedFormats, None)
    CurrentFormat = property(get_CurrentFormat, None)
class IMediaFrameSourceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceController'
    _iid_ = Guid('{6d076635-316d-4b8f-b7b6-eeb04a8c6525}')
    @winrt_commethod(6)
    def GetPropertyAsync(self, propertyId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_commethod(7)
    def SetPropertyAsync(self, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_commethod(8)
    def get_VideoDeviceController(self) -> win32more.Windows.Media.Devices.VideoDeviceController: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
class IMediaFrameSourceController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceController2'
    _iid_ = Guid('{efc49fd4-fcf2-4a03-b4e4-ac9628739bee}')
    @winrt_commethod(6)
    def GetPropertyByExtendedIdAsync(self, extendedPropertyId: Annotated[SZArray[Byte], 'In'], maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_commethod(7)
    def SetPropertyByExtendedIdAsync(self, extendedPropertyId: Annotated[SZArray[Byte], 'In'], propertyValue: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
class IMediaFrameSourceController3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceController3'
    _iid_ = Guid('{1f0cf815-2464-4651-b1e8-4a82dbdb54de}')
    @winrt_commethod(6)
    def get_AudioDeviceController(self) -> win32more.Windows.Media.Devices.AudioDeviceController: ...
    AudioDeviceController = property(get_AudioDeviceController, None)
class IMediaFrameSourceGetPropertyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult'
    _iid_ = Guid('{088616c2-3a64-4bd5-bd2b-e7c898d2f37a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IMediaFrameSourceGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceGroup'
    _iid_ = Guid('{7f605b87-4832-4b5f-ae3d-412faab37d34}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SourceInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    SourceInfos = property(get_SourceInfos, None)
class IMediaFrameSourceGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics'
    _iid_ = Guid('{1c48bfc5-436f-4508-94cf-d5d8b7326445}')
    @winrt_commethod(6)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup]]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMediaFrameSourceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceInfo'
    _iid_ = Guid('{87bdc9cd-4601-408f-91cf-038318cd0af3}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MediaStreamType(self) -> win32more.Windows.Media.Capture.MediaStreamType: ...
    @winrt_commethod(8)
    def get_SourceKind(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_commethod(9)
    def get_SourceGroup(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_commethod(10)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(11)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    Id = property(get_Id, None)
    MediaStreamType = property(get_MediaStreamType, None)
    SourceKind = property(get_SourceKind, None)
    SourceGroup = property(get_SourceGroup, None)
    DeviceInformation = property(get_DeviceInformation, None)
    Properties = property(get_Properties, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
class IMediaFrameSourceInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceInfo2'
    _iid_ = Guid('{195a7855-6457-42c6-a769-19b65bd32e6e}')
    @winrt_commethod(6)
    def get_ProfileId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoProfileMediaDescription(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    ProfileId = property(get_ProfileId, None)
    VideoProfileMediaDescription = property(get_VideoProfileMediaDescription, None)
class IMediaFrameSourceInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceInfo3'
    _iid_ = Guid('{ca824ab6-66ea-5885-a2b6-26c0eeec3c7b}')
    @winrt_commethod(6)
    def GetRelativePanel(self, displayRegion: win32more.Windows.UI.WindowManagement.DisplayRegion) -> win32more.Windows.Devices.Enumeration.Panel: ...
class IMediaFrameSourceInfo4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMediaFrameSourceInfo4'
    _iid_ = Guid('{4817d721-85eb-470c-8f37-43ca5498e41d}')
    @winrt_commethod(6)
    def get_IsShareable(self) -> Boolean: ...
    IsShareable = property(get_IsShareable, None)
class IMultiSourceMediaFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMultiSourceMediaFrameArrivedEventArgs'
    _iid_ = Guid('{63115e01-cf51-48fd-aab0-6d693eb48127}')
class IMultiSourceMediaFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader'
    _iid_ = Guid('{8d144402-f763-488d-98f2-b437bcf075e7}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReader, win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrame(self) -> win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReference: ...
    @winrt_commethod(9)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReaderStartStatus]: ...
    @winrt_commethod(10)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMultiSourceMediaFrameReader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader2'
    _iid_ = Guid('{ef5c8abd-fc5c-4c6b-9d81-3cb9cc637c26}')
    @winrt_commethod(6)
    def put_AcquisitionMode(self, value: win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_commethod(7)
    def get_AcquisitionMode(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
class IMultiSourceMediaFrameReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IMultiSourceMediaFrameReference'
    _iid_ = Guid('{21964b1a-7fe2-44d6-92e5-298e6d2810e9}')
    @winrt_commethod(6)
    def TryGetFrameReferenceBySourceId(self, sourceId: WinRT_String) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
class IVideoMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IVideoMediaFrame'
    _iid_ = Guid('{00dd4ccb-32bd-4fe1-a013-7cc13cf5dbcf}')
    @winrt_commethod(6)
    def get_FrameReference(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_commethod(7)
    def get_VideoFormat(self) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_commethod(8)
    def get_SoftwareBitmap(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(9)
    def get_Direct3DSurface(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(10)
    def get_CameraIntrinsics(self) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(11)
    def get_InfraredMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.InfraredMediaFrame: ...
    @winrt_commethod(12)
    def get_DepthMediaFrame(self) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrame: ...
    @winrt_commethod(13)
    def GetVideoFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    FrameReference = property(get_FrameReference, None)
    VideoFormat = property(get_VideoFormat, None)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    Direct3DSurface = property(get_Direct3DSurface, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    InfraredMediaFrame = property(get_InfraredMediaFrame, None)
    DepthMediaFrame = property(get_DepthMediaFrame, None)
class IVideoMediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Frames.IVideoMediaFrameFormat'
    _iid_ = Guid('{46027fc0-d71b-45c7-8f14-6d9a0ae604e4}')
    @winrt_commethod(6)
    def get_MediaFrameFormat(self) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_commethod(7)
    def get_DepthFormat(self) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    MediaFrameFormat = property(get_MediaFrameFormat, None)
    DepthFormat = property(get_DepthFormat, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
class InfraredMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IInfraredMediaFrame
    _classid_ = 'Windows.Media.Capture.Frames.InfraredMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: win32more.Windows.Media.Capture.Frames.IInfraredMediaFrame) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: win32more.Windows.Media.Capture.Frames.IInfraredMediaFrame) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_IsIlluminated(self: win32more.Windows.Media.Capture.Frames.IInfraredMediaFrame) -> Boolean: ...
    FrameReference = property(get_FrameReference, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    IsIlluminated = property(get_IsIlluminated, None)
class MediaFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameArrivedEventArgs
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs'
class MediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameFormat'
    @winrt_mixinmethod
    def get_MajorType(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subtype(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameRate(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat) -> win32more.Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_VideoFormat(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_AudioEncodingProperties(self: win32more.Windows.Media.Capture.Frames.IMediaFrameFormat2) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    MajorType = property(get_MajorType, None)
    Subtype = property(get_Subtype, None)
    FrameRate = property(get_FrameRate, None)
    Properties = property(get_Properties, None)
    VideoFormat = property(get_VideoFormat, None)
    AudioEncodingProperties = property(get_AudioEncodingProperties, None)
class MediaFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameReader
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MediaFrameReader, win32more.Windows.Media.Capture.Frames.MediaFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrame(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameReaderStartStatus]: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_AcquisitionMode(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader2, value: win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AcquisitionMode(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReader2) -> win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
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
class MediaFrameReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameReference
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameReference'
    @winrt_mixinmethod
    def get_SourceKind(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_BufferMediaFrame(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Media.Capture.Frames.BufferMediaFrame: ...
    @winrt_mixinmethod
    def get_VideoMediaFrame(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrame: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_AudioMediaFrame(self: win32more.Windows.Media.Capture.Frames.IMediaFrameReference2) -> win32more.Windows.Media.Capture.Frames.AudioMediaFrame: ...
    SourceKind = property(get_SourceKind, None)
    Format = property(get_Format, None)
    SystemRelativeTime = property(get_SystemRelativeTime, None)
    Duration = property(get_Duration, None)
    Properties = property(get_Properties, None)
    BufferMediaFrame = property(get_BufferMediaFrame, None)
    VideoMediaFrame = property(get_VideoMediaFrame, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    AudioMediaFrame = property(get_AudioMediaFrame, None)
class MediaFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameSource
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameSource'
    @winrt_mixinmethod
    def get_Info(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo: ...
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceController: ...
    @winrt_mixinmethod
    def get_SupportedFormats(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameFormat]: ...
    @winrt_mixinmethod
    def get_CurrentFormat(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def SetFormatAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource, format: win32more.Windows.Media.Capture.Frames.MediaFrameFormat) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_FormatChanged(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MediaFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FormatChanged(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryGetCameraIntrinsics(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSource, format: win32more.Windows.Media.Capture.Frames.MediaFrameFormat) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    Info = property(get_Info, None)
    Controller = property(get_Controller, None)
    SupportedFormats = property(get_SupportedFormats, None)
    CurrentFormat = property(get_CurrentFormat, None)
class MediaFrameSourceController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameSourceController'
    @winrt_mixinmethod
    def GetPropertyAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController, propertyId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_mixinmethod
    def SetPropertyAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController, propertyId: WinRT_String, propertyValue: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_mixinmethod
    def get_VideoDeviceController(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController) -> win32more.Windows.Media.Devices.VideoDeviceController: ...
    @winrt_mixinmethod
    def GetPropertyByExtendedIdAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController2, extendedPropertyId: Annotated[SZArray[Byte], 'In'], maxPropertyValueSize: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult]: ...
    @winrt_mixinmethod
    def SetPropertyByExtendedIdAsync(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController2, extendedPropertyId: Annotated[SZArray[Byte], 'In'], propertyValue: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceSetPropertyStatus]: ...
    @winrt_mixinmethod
    def get_AudioDeviceController(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceController3) -> win32more.Windows.Media.Devices.AudioDeviceController: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    AudioDeviceController = property(get_AudioDeviceController, None)
class MediaFrameSourceGetPropertyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGetPropertyStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGetPropertyResult) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
MediaFrameSourceGetPropertyStatus = Int32
MediaFrameSourceGetPropertyStatus_Success: MediaFrameSourceGetPropertyStatus = 0
MediaFrameSourceGetPropertyStatus_UnknownFailure: MediaFrameSourceGetPropertyStatus = 1
MediaFrameSourceGetPropertyStatus_NotSupported: MediaFrameSourceGetPropertyStatus = 2
MediaFrameSourceGetPropertyStatus_DeviceNotAvailable: MediaFrameSourceGetPropertyStatus = 3
MediaFrameSourceGetPropertyStatus_MaxPropertyValueSizeTooSmall: MediaFrameSourceGetPropertyStatus = 4
MediaFrameSourceGetPropertyStatus_MaxPropertyValueSizeRequired: MediaFrameSourceGetPropertyStatus = 5
class MediaFrameSourceGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroup
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameSourceGroup'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceInfos(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroup) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceGroupStatics) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    SourceInfos = property(get_SourceInfos, None)
class MediaFrameSourceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo
    _classid_ = 'Windows.Media.Capture.Frames.MediaFrameSourceInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MediaStreamType(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Media.Capture.MediaStreamType: ...
    @winrt_mixinmethod
    def get_SourceKind(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceKind: ...
    @winrt_mixinmethod
    def get_SourceGroup(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_ProfileId(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoProfileMediaDescription(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def GetRelativePanel(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo3, displayRegion: win32more.Windows.UI.WindowManagement.DisplayRegion) -> win32more.Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def get_IsShareable(self: win32more.Windows.Media.Capture.Frames.IMediaFrameSourceInfo4) -> Boolean: ...
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
class MultiSourceMediaFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameArrivedEventArgs
    _classid_ = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs'
class MultiSourceMediaFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader
    _classid_ = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReader, win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrame(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReference: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Capture.Frames.MultiSourceMediaFrameReaderStartStatus]: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_AcquisitionMode(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader2, value: win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AcquisitionMode(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReader2) -> win32more.Windows.Media.Capture.Frames.MediaFrameReaderAcquisitionMode: ...
    AcquisitionMode = property(get_AcquisitionMode, put_AcquisitionMode)
MultiSourceMediaFrameReaderStartStatus = Int32
MultiSourceMediaFrameReaderStartStatus_Success: MultiSourceMediaFrameReaderStartStatus = 0
MultiSourceMediaFrameReaderStartStatus_NotSupported: MultiSourceMediaFrameReaderStartStatus = 1
MultiSourceMediaFrameReaderStartStatus_InsufficientResources: MultiSourceMediaFrameReaderStartStatus = 2
MultiSourceMediaFrameReaderStartStatus_DeviceNotAvailable: MultiSourceMediaFrameReaderStartStatus = 3
MultiSourceMediaFrameReaderStartStatus_UnknownFailure: MultiSourceMediaFrameReaderStartStatus = 4
class MultiSourceMediaFrameReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReference
    _classid_ = 'Windows.Media.Capture.Frames.MultiSourceMediaFrameReference'
    @winrt_mixinmethod
    def TryGetFrameReferenceBySourceId(self: win32more.Windows.Media.Capture.Frames.IMultiSourceMediaFrameReference, sourceId: WinRT_String) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class VideoMediaFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame
    _classid_ = 'Windows.Media.Capture.Frames.VideoMediaFrame'
    @winrt_mixinmethod
    def get_FrameReference(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.Capture.Frames.MediaFrameReference: ...
    @winrt_mixinmethod
    def get_VideoFormat(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.Capture.Frames.VideoMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_Direct3DSurface(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def get_InfraredMediaFrame(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.Capture.Frames.InfraredMediaFrame: ...
    @winrt_mixinmethod
    def get_DepthMediaFrame(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrame: ...
    @winrt_mixinmethod
    def GetVideoFrame(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrame) -> win32more.Windows.Media.VideoFrame: ...
    FrameReference = property(get_FrameReference, None)
    VideoFormat = property(get_VideoFormat, None)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    Direct3DSurface = property(get_Direct3DSurface, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    InfraredMediaFrame = property(get_InfraredMediaFrame, None)
    DepthMediaFrame = property(get_DepthMediaFrame, None)
class VideoMediaFrameFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Frames.IVideoMediaFrameFormat
    _classid_ = 'Windows.Media.Capture.Frames.VideoMediaFrameFormat'
    @winrt_mixinmethod
    def get_MediaFrameFormat(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> win32more.Windows.Media.Capture.Frames.MediaFrameFormat: ...
    @winrt_mixinmethod
    def get_DepthFormat(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> win32more.Windows.Media.Capture.Frames.DepthMediaFrameFormat: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Media.Capture.Frames.IVideoMediaFrameFormat) -> UInt32: ...
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
