from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Imaging
import Windows.Media
import Windows.Media.Capture
import Windows.Media.Capture.Core
import Windows.Media.Capture.Frames
import Windows.Media.Core
import Windows.Media.Devices
import Windows.Media.Effects
import Windows.Media.MediaProperties
import Windows.Security.Credentials
import Windows.Storage
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
class AdvancedCapturedPhoto(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.AdvancedCapturedPhoto'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.IAdvancedCapturedPhoto) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Capture.IAdvancedCapturedPhoto) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_mixinmethod
    def get_Context(self: Windows.Media.Capture.IAdvancedCapturedPhoto) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_FrameBoundsRelativeToReferencePhoto(self: Windows.Media.Capture.IAdvancedCapturedPhoto2) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    Frame = property(get_Frame, None)
    Mode = property(get_Mode, None)
    Context = property(get_Context, None)
    FrameBoundsRelativeToReferencePhoto = property(get_FrameBoundsRelativeToReferencePhoto, None)
class AdvancedPhotoCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.AdvancedPhotoCapture'
    @winrt_mixinmethod
    def CaptureAsync(self: Windows.Media.Capture.IAdvancedPhotoCapture) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_mixinmethod
    def CaptureWithContextAsync(self: Windows.Media.Capture.IAdvancedPhotoCapture, context: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_mixinmethod
    def add_OptionalReferencePhotoCaptured(self: Windows.Media.Capture.IAdvancedPhotoCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AdvancedPhotoCapture, Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionalReferencePhotoCaptured(self: Windows.Media.Capture.IAdvancedPhotoCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AllPhotosCaptured(self: Windows.Media.Capture.IAdvancedPhotoCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AdvancedPhotoCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AllPhotosCaptured(self: Windows.Media.Capture.IAdvancedPhotoCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Media.Capture.IAdvancedPhotoCapture) -> Windows.Foundation.IAsyncAction: ...
class AppCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.AppCapture'
    @winrt_mixinmethod
    def get_IsCapturingAudio(self: Windows.Media.Capture.IAppCapture) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCapturingVideo(self: Windows.Media.Capture.IAppCapture) -> Boolean: ...
    @winrt_mixinmethod
    def add_CapturingChanged(self: Windows.Media.Capture.IAppCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AppCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CapturingChanged(self: Windows.Media.Capture.IAppCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def SetAllowedAsync(cls: Windows.Media.Capture.IAppCaptureStatics2, allowed: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Media.Capture.IAppCaptureStatics) -> Windows.Media.Capture.AppCapture: ...
    IsCapturingAudio = property(get_IsCapturingAudio, None)
    IsCapturingVideo = property(get_IsCapturingVideo, None)
class CameraCaptureUI(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CameraCaptureUI'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Capture.CameraCaptureUI: ...
    @winrt_mixinmethod
    def get_PhotoSettings(self: Windows.Media.Capture.ICameraCaptureUI) -> Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_mixinmethod
    def get_VideoSettings(self: Windows.Media.Capture.ICameraCaptureUI) -> Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_mixinmethod
    def CaptureFileAsync(self: Windows.Media.Capture.ICameraCaptureUI, mode: Windows.Media.Capture.CameraCaptureUIMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
CameraCaptureUIMaxPhotoResolution = Int32
CameraCaptureUIMaxPhotoResolution_HighestAvailable: CameraCaptureUIMaxPhotoResolution = 0
CameraCaptureUIMaxPhotoResolution_VerySmallQvga: CameraCaptureUIMaxPhotoResolution = 1
CameraCaptureUIMaxPhotoResolution_SmallVga: CameraCaptureUIMaxPhotoResolution = 2
CameraCaptureUIMaxPhotoResolution_MediumXga: CameraCaptureUIMaxPhotoResolution = 3
CameraCaptureUIMaxPhotoResolution_Large3M: CameraCaptureUIMaxPhotoResolution = 4
CameraCaptureUIMaxPhotoResolution_VeryLarge5M: CameraCaptureUIMaxPhotoResolution = 5
CameraCaptureUIMaxVideoResolution = Int32
CameraCaptureUIMaxVideoResolution_HighestAvailable: CameraCaptureUIMaxVideoResolution = 0
CameraCaptureUIMaxVideoResolution_LowDefinition: CameraCaptureUIMaxVideoResolution = 1
CameraCaptureUIMaxVideoResolution_StandardDefinition: CameraCaptureUIMaxVideoResolution = 2
CameraCaptureUIMaxVideoResolution_HighDefinition: CameraCaptureUIMaxVideoResolution = 3
CameraCaptureUIMode = Int32
CameraCaptureUIMode_PhotoOrVideo: CameraCaptureUIMode = 0
CameraCaptureUIMode_Photo: CameraCaptureUIMode = 1
CameraCaptureUIMode_Video: CameraCaptureUIMode = 2
class CameraCaptureUIPhotoCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings'
    @winrt_mixinmethod
    def get_Format(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedSizeInPixels(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedSizeInPixels(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_CroppedAspectRatio(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_CroppedAspectRatio(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCropping(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCropping(self: Windows.Media.Capture.ICameraCaptureUIPhotoCaptureSettings, value: Boolean) -> Void: ...
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
CameraCaptureUIPhotoFormat = Int32
CameraCaptureUIPhotoFormat_Jpeg: CameraCaptureUIPhotoFormat = 0
CameraCaptureUIPhotoFormat_Png: CameraCaptureUIPhotoFormat = 1
CameraCaptureUIPhotoFormat_JpegXR: CameraCaptureUIPhotoFormat = 2
class CameraCaptureUIVideoCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings'
    @winrt_mixinmethod
    def get_Format(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_mixinmethod
    def put_MaxResolution(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    @winrt_mixinmethod
    def get_MaxDurationInSeconds(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Single: ...
    @winrt_mixinmethod
    def put_MaxDurationInSeconds(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AllowTrimming(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowTrimming(self: Windows.Media.Capture.ICameraCaptureUIVideoCaptureSettings, value: Boolean) -> Void: ...
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
CameraCaptureUIVideoFormat = Int32
CameraCaptureUIVideoFormat_Mp4: CameraCaptureUIVideoFormat = 0
CameraCaptureUIVideoFormat_Wmv: CameraCaptureUIVideoFormat = 1
class CapturedFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CapturedFrame'
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.Capture.ICapturedFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.Capture.ICapturedFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: Windows.Storage.Streams.IInputStream, buffer: Windows.Storage.Streams.IBuffer, count: UInt32, options: Windows.Storage.Streams.InputStreamOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: Windows.Storage.Streams.IOutputStream, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: Windows.Media.Capture.ICapturedFrameWithSoftwareBitmap) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def get_ControlValues(self: Windows.Media.Capture.ICapturedFrame2) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_mixinmethod
    def get_BitmapProperties(self: Windows.Media.Capture.ICapturedFrame2) -> Windows.Graphics.Imaging.BitmapPropertySet: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
    SoftwareBitmap = property(get_SoftwareBitmap, None)
    ControlValues = property(get_ControlValues, None)
    BitmapProperties = property(get_BitmapProperties, None)
class CapturedFrameControlValues(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CapturedFrameControlValues'
    @winrt_mixinmethod
    def get_Exposure(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_ExposureCompensation(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_IsoSpeed(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Focus(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_SceneMode(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_mixinmethod
    def get_Flashed(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_FlashPowerPercent(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_WhiteBalance(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_ZoomFactor(self: Windows.Media.Capture.ICapturedFrameControlValues) -> Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def get_FocusState(self: Windows.Media.Capture.ICapturedFrameControlValues2) -> Windows.Foundation.IReference[Windows.Media.Devices.MediaCaptureFocusState]: ...
    @winrt_mixinmethod
    def get_IsoDigitalGain(self: Windows.Media.Capture.ICapturedFrameControlValues2) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_IsoAnalogGain(self: Windows.Media.Capture.ICapturedFrameControlValues2) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SensorFrameRate(self: Windows.Media.Capture.ICapturedFrameControlValues2) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_WhiteBalanceGain(self: Windows.Media.Capture.ICapturedFrameControlValues2) -> Windows.Foundation.IReference[Windows.Media.Capture.WhiteBalanceGain]: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    IsoSpeed = property(get_IsoSpeed, None)
    Focus = property(get_Focus, None)
    SceneMode = property(get_SceneMode, None)
    Flashed = property(get_Flashed, None)
    FlashPowerPercent = property(get_FlashPowerPercent, None)
    WhiteBalance = property(get_WhiteBalance, None)
    ZoomFactor = property(get_ZoomFactor, None)
    FocusState = property(get_FocusState, None)
    IsoDigitalGain = property(get_IsoDigitalGain, None)
    IsoAnalogGain = property(get_IsoAnalogGain, None)
    SensorFrameRate = property(get_SensorFrameRate, None)
    WhiteBalanceGain = property(get_WhiteBalanceGain, None)
class CapturedPhoto(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.CapturedPhoto'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.ICapturedPhoto) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Capture.ICapturedPhoto) -> Windows.Media.Capture.CapturedFrame: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class IAdvancedCapturedPhoto(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f072728b-b292-4491-9d-41-99-80-7a-55-0b-bf')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Mode(self) -> Windows.Media.Devices.AdvancedPhotoMode: ...
    @winrt_commethod(8)
    def get_Context(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Frame = property(get_Frame, None)
    Mode = property(get_Mode, None)
    Context = property(get_Context, None)
class IAdvancedCapturedPhoto2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('18cf6cd8-cffe-42d8-81-04-01-7b-b3-18-f4-a1')
    @winrt_commethod(6)
    def get_FrameBoundsRelativeToReferencePhoto(self) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    FrameBoundsRelativeToReferencePhoto = property(get_FrameBoundsRelativeToReferencePhoto, None)
class IAdvancedPhotoCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('83ffaafa-6667-44dc-97-3c-a6-bc-e5-96-aa-0f')
    @winrt_commethod(6)
    def CaptureAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_commethod(7)
    def CaptureWithContextAsync(self, context: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedCapturedPhoto]: ...
    @winrt_commethod(8)
    def add_OptionalReferencePhotoCaptured(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AdvancedPhotoCapture, Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OptionalReferencePhotoCaptured(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AllPhotosCaptured(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AdvancedPhotoCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AllPhotosCaptured(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def FinishAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IAppCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9749d453-a29a-45ed-8f-29-22-d0-99-42-cf-f7')
    @winrt_commethod(6)
    def get_IsCapturingAudio(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsCapturingVideo(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_CapturingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.AppCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CapturingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCapturingAudio = property(get_IsCapturingAudio, None)
    IsCapturingVideo = property(get_IsCapturingVideo, None)
class IAppCaptureStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f922dd6c-0a7e-4e74-8b-20-9c-1f-90-2d-08-a1')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Media.Capture.AppCapture: ...
class IAppCaptureStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b2d881d4-836c-4da4-af-d7-fa-cc-04-1e-1c-f3')
    @winrt_commethod(6)
    def SetAllowedAsync(self, allowed: Boolean) -> Windows.Foundation.IAsyncAction: ...
class ICameraCaptureUI(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('48587540-6f93-4bb4-b8-f3-e8-9e-48-94-8c-91')
    @winrt_commethod(6)
    def get_PhotoSettings(self) -> Windows.Media.Capture.CameraCaptureUIPhotoCaptureSettings: ...
    @winrt_commethod(7)
    def get_VideoSettings(self) -> Windows.Media.Capture.CameraCaptureUIVideoCaptureSettings: ...
    @winrt_commethod(8)
    def CaptureFileAsync(self, mode: Windows.Media.Capture.CameraCaptureUIMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    PhotoSettings = property(get_PhotoSettings, None)
    VideoSettings = property(get_VideoSettings, None)
class ICameraCaptureUIPhotoCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b9f5be97-3472-46a8-8a-9e-04-ce-42-cc-c9-7d')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Media.Capture.CameraCaptureUIPhotoFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: Windows.Media.Capture.CameraCaptureUIPhotoFormat) -> Void: ...
    @winrt_commethod(8)
    def get_MaxResolution(self) -> Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution: ...
    @winrt_commethod(9)
    def put_MaxResolution(self, value: Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution) -> Void: ...
    @winrt_commethod(10)
    def get_CroppedSizeInPixels(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def put_CroppedSizeInPixels(self, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(12)
    def get_CroppedAspectRatio(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def put_CroppedAspectRatio(self, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(14)
    def get_AllowCropping(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AllowCropping(self, value: Boolean) -> Void: ...
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
    CroppedSizeInPixels = property(get_CroppedSizeInPixels, put_CroppedSizeInPixels)
    CroppedAspectRatio = property(get_CroppedAspectRatio, put_CroppedAspectRatio)
    AllowCropping = property(get_AllowCropping, put_AllowCropping)
class ICameraCaptureUIVideoCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64e92d1f-a28d-425a-b8-4f-e5-68-33-5f-f2-4e')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Media.Capture.CameraCaptureUIVideoFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: Windows.Media.Capture.CameraCaptureUIVideoFormat) -> Void: ...
    @winrt_commethod(8)
    def get_MaxResolution(self) -> Windows.Media.Capture.CameraCaptureUIMaxVideoResolution: ...
    @winrt_commethod(9)
    def put_MaxResolution(self, value: Windows.Media.Capture.CameraCaptureUIMaxVideoResolution) -> Void: ...
    @winrt_commethod(10)
    def get_MaxDurationInSeconds(self) -> Single: ...
    @winrt_commethod(11)
    def put_MaxDurationInSeconds(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_AllowTrimming(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowTrimming(self, value: Boolean) -> Void: ...
    Format = property(get_Format, put_Format)
    MaxResolution = property(get_MaxResolution, put_MaxResolution)
    MaxDurationInSeconds = property(get_MaxDurationInSeconds, put_MaxDurationInSeconds)
    AllowTrimming = property(get_AllowTrimming, put_AllowTrimming)
class ICapturedFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1dd2de1f-571b-44d8-8e-80-a0-8a-15-78-76-6e')
    @winrt_commethod(6)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Height(self) -> UInt32: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
class ICapturedFrame2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('543fa6d1-bd78-4866-ad-da-24-31-4b-c6-5d-ea')
    @winrt_commethod(6)
    def get_ControlValues(self) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_commethod(7)
    def get_BitmapProperties(self) -> Windows.Graphics.Imaging.BitmapPropertySet: ...
    ControlValues = property(get_ControlValues, None)
    BitmapProperties = property(get_BitmapProperties, None)
class ICapturedFrameControlValues(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('90c65b7f-4e0d-4ca4-88-2d-7a-14-4f-ed-0a-90')
    @winrt_commethod(6)
    def get_Exposure(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_ExposureCompensation(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(8)
    def get_IsoSpeed(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_Focus(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(10)
    def get_SceneMode(self) -> Windows.Foundation.IReference[Windows.Media.Devices.CaptureSceneMode]: ...
    @winrt_commethod(11)
    def get_Flashed(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(12)
    def get_FlashPowerPercent(self) -> Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(13)
    def get_WhiteBalance(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(14)
    def get_ZoomFactor(self) -> Windows.Foundation.IReference[Single]: ...
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    IsoSpeed = property(get_IsoSpeed, None)
    Focus = property(get_Focus, None)
    SceneMode = property(get_SceneMode, None)
    Flashed = property(get_Flashed, None)
    FlashPowerPercent = property(get_FlashPowerPercent, None)
    WhiteBalance = property(get_WhiteBalance, None)
    ZoomFactor = property(get_ZoomFactor, None)
class ICapturedFrameControlValues2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('500b2b88-06d2-4aa7-a7-db-d3-7a-f7-33-21-d8')
    @winrt_commethod(6)
    def get_FocusState(self) -> Windows.Foundation.IReference[Windows.Media.Devices.MediaCaptureFocusState]: ...
    @winrt_commethod(7)
    def get_IsoDigitalGain(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_IsoAnalogGain(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_SensorFrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(10)
    def get_WhiteBalanceGain(self) -> Windows.Foundation.IReference[Windows.Media.Capture.WhiteBalanceGain]: ...
    FocusState = property(get_FocusState, None)
    IsoDigitalGain = property(get_IsoDigitalGain, None)
    IsoAnalogGain = property(get_IsoAnalogGain, None)
    SensorFrameRate = property(get_SensorFrameRate, None)
    WhiteBalanceGain = property(get_WhiteBalanceGain, None)
class ICapturedFrameWithSoftwareBitmap(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b58e8b6e-8503-49b5-9e-86-89-7d-26-a3-ff-3d')
    @winrt_commethod(6)
    def get_SoftwareBitmap(self) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    SoftwareBitmap = property(get_SoftwareBitmap, None)
class ICapturedPhoto(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b0ce7e5a-cfcc-4d6c-8a-d1-08-69-20-8a-ca-16')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> Windows.Media.Capture.CapturedFrame: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
class ILowLagMediaRecording(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('41c8baf7-ff3f-49f0-a4-77-f1-95-e3-ce-51-08')
    @winrt_commethod(6)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> Windows.Foundation.IAsyncAction: ...
class ILowLagMediaRecording2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6369c758-5644-41e2-97-af-8e-f5-6a-25-e2-25')
    @winrt_commethod(6)
    def PauseAsync(self, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ResumeAsync(self) -> Windows.Foundation.IAsyncAction: ...
class ILowLagMediaRecording3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c33ab12-48f7-47da-b4-1e-90-88-0a-5f-e0-ec')
    @winrt_commethod(6)
    def PauseWithResultAsync(self, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_commethod(7)
    def StopWithResultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCaptureStopResult]: ...
class ILowLagPhotoCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a37251b7-6b44-473d-8f-24-f7-03-d6-c0-ec-44')
    @winrt_commethod(6)
    def CaptureAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.CapturedPhoto]: ...
    @winrt_commethod(7)
    def FinishAsync(self) -> Windows.Foundation.IAsyncAction: ...
class ILowLagPhotoSequenceCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cc346bb-b9a9-4c91-8f-fa-28-7e-9c-66-86-69')
    @winrt_commethod(6)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_PhotoCaptured(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.LowLagPhotoSequenceCapture, Windows.Media.Capture.PhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoCaptured(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMediaCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c61afbb4-fb10-4a34-ac-18-ca-80-d9-c8-e7-ee')
    @winrt_commethod(6)
    def InitializeAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def InitializeWithSettingsAsync(self, mediaCaptureInitializationSettings: Windows.Media.Capture.MediaCaptureInitializationSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StartRecordToStorageFileAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StartRecordToStreamAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def StartRecordToCustomSinkAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def StartRecordToCustomSinkIdAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def StopRecordAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def CapturePhotoToStorageFileAsync(self, type: Windows.Media.MediaProperties.ImageEncodingProperties, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def CapturePhotoToStreamAsync(self, type: Windows.Media.MediaProperties.ImageEncodingProperties, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def AddEffectAsync(self, mediaStreamType: Windows.Media.Capture.MediaStreamType, effectActivationID: WinRT_String, effectSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def ClearEffectsAsync(self, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def SetEncoderProperty(self, mediaStreamType: Windows.Media.Capture.MediaStreamType, propertyId: Guid, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(18)
    def GetEncoderProperty(self, mediaStreamType: Windows.Media.Capture.MediaStreamType, propertyId: Guid) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(19)
    def add_Failed(self, errorEventHandler: Windows.Media.Capture.MediaCaptureFailedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_Failed(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_RecordLimitationExceeded(self, recordLimitationExceededEventHandler: Windows.Media.Capture.RecordLimitationExceededEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_RecordLimitationExceeded(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def get_MediaCaptureSettings(self) -> Windows.Media.Capture.MediaCaptureSettings: ...
    @winrt_commethod(24)
    def get_AudioDeviceController(self) -> Windows.Media.Devices.AudioDeviceController: ...
    @winrt_commethod(25)
    def get_VideoDeviceController(self) -> Windows.Media.Devices.VideoDeviceController: ...
    @winrt_commethod(26)
    def SetPreviewMirroring(self, value: Boolean) -> Void: ...
    @winrt_commethod(27)
    def GetPreviewMirroring(self) -> Boolean: ...
    @winrt_commethod(28)
    def SetPreviewRotation(self, value: Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_commethod(29)
    def GetPreviewRotation(self) -> Windows.Media.Capture.VideoRotation: ...
    @winrt_commethod(30)
    def SetRecordRotation(self, value: Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_commethod(31)
    def GetRecordRotation(self) -> Windows.Media.Capture.VideoRotation: ...
    MediaCaptureSettings = property(get_MediaCaptureSettings, None)
    AudioDeviceController = property(get_AudioDeviceController, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
class IMediaCapture2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9cc68260-7da1-4043-b6-52-21-b8-87-8d-af-f9')
    @winrt_commethod(6)
    def PrepareLowLagRecordToStorageFileAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(7)
    def PrepareLowLagRecordToStreamAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(8)
    def PrepareLowLagRecordToCustomSinkAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(9)
    def PrepareLowLagRecordToCustomSinkIdAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_commethod(10)
    def PrepareLowLagPhotoCaptureAsync(self, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagPhotoCapture]: ...
    @winrt_commethod(11)
    def PrepareLowLagPhotoSequenceCaptureAsync(self, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagPhotoSequenceCapture]: ...
    @winrt_commethod(12)
    def SetEncodingPropertiesAsync(self, mediaStreamType: Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: Windows.Media.MediaProperties.IMediaEncodingProperties, encoderProperties: Windows.Media.MediaProperties.MediaPropertySet) -> Windows.Foundation.IAsyncAction: ...
class IMediaCapture3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d4136f30-1564-466e-bc-0a-af-94-e0-2a-b0-16')
    @winrt_commethod(6)
    def PrepareVariablePhotoSequenceCaptureAsync(self, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Core.VariablePhotoSequenceCapture]: ...
    @winrt_commethod(7)
    def add_FocusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.MediaCaptureFocusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_FocusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PhotoConfirmationCaptured(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.PhotoConfirmationCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoConfirmationCaptured(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMediaCapture4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bacd6fd6-fb08-4947-ae-a2-ce-14-ef-f0-ce-13')
    @winrt_commethod(6)
    def AddAudioEffectAsync(self, definition: Windows.Media.Effects.IAudioEffectDefinition) -> Windows.Foundation.IAsyncOperation[Windows.Media.IMediaExtension]: ...
    @winrt_commethod(7)
    def AddVideoEffectAsync(self, definition: Windows.Media.Effects.IVideoEffectDefinition, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.IAsyncOperation[Windows.Media.IMediaExtension]: ...
    @winrt_commethod(8)
    def PauseRecordAsync(self, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ResumeRecordAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def add_CameraStreamStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraStreamStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_CameraStreamState(self) -> Windows.Media.Devices.CameraStreamState: ...
    @winrt_commethod(13)
    def GetPreviewFrameAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.VideoFrame]: ...
    @winrt_commethod(14)
    def GetPreviewFrameCopyAsync(self, destination: Windows.Media.VideoFrame) -> Windows.Foundation.IAsyncOperation[Windows.Media.VideoFrame]: ...
    @winrt_commethod(15)
    def add_ThermalStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ThermalStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def get_ThermalStatus(self) -> Windows.Media.Capture.MediaCaptureThermalStatus: ...
    @winrt_commethod(18)
    def PrepareAdvancedPhotoCaptureAsync(self, encodingProperties: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedPhotoCapture]: ...
    CameraStreamState = property(get_CameraStreamState, None)
    ThermalStatus = property(get_ThermalStatus, None)
class IMediaCapture5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('da787c22-3a9b-4720-a7-1e-97-90-0a-31-6e-5a')
    @winrt_commethod(6)
    def RemoveEffectAsync(self, effect: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def PauseRecordWithResultAsync(self, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_commethod(8)
    def StopRecordWithResultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCaptureStopResult]: ...
    @winrt_commethod(9)
    def get_FrameSources(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Media.Capture.Frames.MediaFrameSource]: ...
    @winrt_commethod(10)
    def CreateFrameReaderAsync(self, inputSource: Windows.Media.Capture.Frames.MediaFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_commethod(11)
    def CreateFrameReaderWithSubtypeAsync(self, inputSource: Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_commethod(12)
    def CreateFrameReaderWithSubtypeAndSizeAsync(self, inputSource: Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String, outputSize: Windows.Graphics.Imaging.BitmapSize) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    FrameSources = property(get_FrameSources, None)
class IMediaCapture6(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('228948bd-4b20-4bb1-9f-d6-a5-83-21-2a-10-12')
    @winrt_commethod(6)
    def add_CaptureDeviceExclusiveControlStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CaptureDeviceExclusiveControlStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CreateMultiSourceFrameReaderAsync(self, inputSources: Windows.Foundation.Collections.IIterable[Windows.Media.Capture.Frames.MediaFrameSource]) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MultiSourceMediaFrameReader]: ...
class IMediaCapture7(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9169f102-8888-541a-95-bc-24-e4-d4-62-54-2a')
    @winrt_commethod(6)
    def CreateRelativePanelWatcher(self, captureMode: Windows.Media.Capture.StreamingCaptureMode, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Windows.Media.Capture.MediaCaptureRelativePanelWatcher: ...
class IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9d2f920d-a588-43c6-89-d6-5a-d3-22-af-00-6a')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatus: ...
    DeviceId = property(get_DeviceId, None)
    Status = property(get_Status, None)
class IMediaCaptureFailedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('80fde3f4-54c4-42c0-8d-19-ce-a1-a8-7c-a1-8b')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Code(self) -> UInt32: ...
    Message = property(get_Message, None)
    Code = property(get_Code, None)
class IMediaCaptureFocusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('81e1bc7f-2277-493e-ab-ee-d3-f4-4f-f9-8c-04')
    @winrt_commethod(6)
    def get_FocusState(self) -> Windows.Media.Devices.MediaCaptureFocusState: ...
    FocusState = property(get_FocusState, None)
class IMediaCaptureInitializationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9782ba70-ea65-4900-93-56-8c-a8-87-72-68-84')
    @winrt_commethod(6)
    def put_AudioDeviceId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_AudioDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_VideoDeviceId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_StreamingCaptureMode(self, value: Windows.Media.Capture.StreamingCaptureMode) -> Void: ...
    @winrt_commethod(11)
    def get_StreamingCaptureMode(self) -> Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_commethod(12)
    def put_PhotoCaptureSource(self, value: Windows.Media.Capture.PhotoCaptureSource) -> Void: ...
    @winrt_commethod(13)
    def get_PhotoCaptureSource(self) -> Windows.Media.Capture.PhotoCaptureSource: ...
    AudioDeviceId = property(get_AudioDeviceId, put_AudioDeviceId)
    VideoDeviceId = property(get_VideoDeviceId, put_VideoDeviceId)
    StreamingCaptureMode = property(get_StreamingCaptureMode, put_StreamingCaptureMode)
    PhotoCaptureSource = property(get_PhotoCaptureSource, put_PhotoCaptureSource)
class IMediaCaptureInitializationSettings2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('404e0626-c9dc-43e9-ae-e4-e6-bf-1b-57-b4-4c')
    @winrt_commethod(6)
    def put_MediaCategory(self, value: Windows.Media.Capture.MediaCategory) -> Void: ...
    @winrt_commethod(7)
    def get_MediaCategory(self) -> Windows.Media.Capture.MediaCategory: ...
    @winrt_commethod(8)
    def put_AudioProcessing(self, value: Windows.Media.AudioProcessing) -> Void: ...
    @winrt_commethod(9)
    def get_AudioProcessing(self) -> Windows.Media.AudioProcessing: ...
    MediaCategory = property(get_MediaCategory, put_MediaCategory)
    AudioProcessing = property(get_AudioProcessing, put_AudioProcessing)
class IMediaCaptureInitializationSettings3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4160519d-be48-4730-81-04-0c-f6-e9-e9-79-48')
    @winrt_commethod(6)
    def put_AudioSource(self, value: Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_commethod(7)
    def get_AudioSource(self) -> Windows.Media.Core.IMediaSource: ...
    @winrt_commethod(8)
    def put_VideoSource(self, value: Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_commethod(9)
    def get_VideoSource(self) -> Windows.Media.Core.IMediaSource: ...
    AudioSource = property(get_AudioSource, put_AudioSource)
    VideoSource = property(get_VideoSource, put_VideoSource)
class IMediaCaptureInitializationSettings4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f502a537-4cb7-4d28-95-ed-4f-9f-01-2e-05-18')
    @winrt_commethod(6)
    def get_VideoProfile(self) -> Windows.Media.Capture.MediaCaptureVideoProfile: ...
    @winrt_commethod(7)
    def put_VideoProfile(self, value: Windows.Media.Capture.MediaCaptureVideoProfile) -> Void: ...
    @winrt_commethod(8)
    def get_PreviewMediaDescription(self) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(9)
    def put_PreviewMediaDescription(self, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_commethod(10)
    def get_RecordMediaDescription(self) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(11)
    def put_RecordMediaDescription(self, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_commethod(12)
    def get_PhotoMediaDescription(self) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_commethod(13)
    def put_PhotoMediaDescription(self, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    VideoProfile = property(get_VideoProfile, put_VideoProfile)
    PreviewMediaDescription = property(get_PreviewMediaDescription, put_PreviewMediaDescription)
    RecordMediaDescription = property(get_RecordMediaDescription, put_RecordMediaDescription)
    PhotoMediaDescription = property(get_PhotoMediaDescription, put_PhotoMediaDescription)
class IMediaCaptureInitializationSettings5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d5a2e3b8-2626-4e94-b7-b3-53-08-a0-f6-4b-1a')
    @winrt_commethod(6)
    def get_SourceGroup(self) -> Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_commethod(7)
    def put_SourceGroup(self, value: Windows.Media.Capture.Frames.MediaFrameSourceGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SharingMode(self) -> Windows.Media.Capture.MediaCaptureSharingMode: ...
    @winrt_commethod(9)
    def put_SharingMode(self, value: Windows.Media.Capture.MediaCaptureSharingMode) -> Void: ...
    @winrt_commethod(10)
    def get_MemoryPreference(self) -> Windows.Media.Capture.MediaCaptureMemoryPreference: ...
    @winrt_commethod(11)
    def put_MemoryPreference(self, value: Windows.Media.Capture.MediaCaptureMemoryPreference) -> Void: ...
    SourceGroup = property(get_SourceGroup, put_SourceGroup)
    SharingMode = property(get_SharingMode, put_SharingMode)
    MemoryPreference = property(get_MemoryPreference, put_MemoryPreference)
class IMediaCaptureInitializationSettings6(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b2e26b47-3db1-4d33-ab-63-0f-fa-09-05-65-85')
    @winrt_commethod(6)
    def get_AlwaysPlaySystemShutterSound(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AlwaysPlaySystemShutterSound(self, value: Boolean) -> Void: ...
    AlwaysPlaySystemShutterSound = property(get_AlwaysPlaySystemShutterSound, put_AlwaysPlaySystemShutterSound)
class IMediaCaptureInitializationSettings7(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('41546967-f58a-5d82-9e-f4-ed-57-2f-b5-e3-4e')
    @winrt_commethod(6)
    def get_DeviceUriPasswordCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def put_DeviceUriPasswordCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_DeviceUri(self, value: Windows.Foundation.Uri) -> Void: ...
    DeviceUriPasswordCredential = property(get_DeviceUriPasswordCredential, put_DeviceUriPasswordCredential)
    DeviceUri = property(get_DeviceUri, put_DeviceUri)
class IMediaCapturePauseResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aec47ca3-4477-4b04-a0-6f-2c-1c-51-82-fe-9d')
    @winrt_commethod(6)
    def get_LastFrame(self) -> Windows.Media.VideoFrame: ...
    @winrt_commethod(7)
    def get_RecordDuration(self) -> Windows.Foundation.TimeSpan: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class IMediaCaptureRelativePanelWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d896566-04be-5b89-b3-0e-bd-34-a9-f1-2d-b0')
    @winrt_commethod(6)
    def get_RelativePanel(self) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCaptureRelativePanelWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    RelativePanel = property(get_RelativePanel, None)
class IMediaCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d83aafe-6d45-4477-8d-c4-ac-5b-c0-1c-40-91')
    @winrt_commethod(6)
    def get_AudioDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_StreamingCaptureMode(self) -> Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_commethod(9)
    def get_PhotoCaptureSource(self) -> Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_commethod(10)
    def get_VideoDeviceCharacteristic(self) -> Windows.Media.Capture.VideoDeviceCharacteristic: ...
    AudioDeviceId = property(get_AudioDeviceId, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    StreamingCaptureMode = property(get_StreamingCaptureMode, None)
    PhotoCaptureSource = property(get_PhotoCaptureSource, None)
    VideoDeviceCharacteristic = property(get_VideoDeviceCharacteristic, None)
class IMediaCaptureSettings2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f9e7cfb-fa9f-4b13-9c-be-5a-b9-4f-1f-34-93')
    @winrt_commethod(6)
    def get_ConcurrentRecordAndPhotoSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ConcurrentRecordAndPhotoSequenceSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CameraSoundRequiredForRegion(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Horizontal35mmEquivalentFocalLength(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(10)
    def get_PitchOffsetDegrees(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def get_Vertical35mmEquivalentFocalLength(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(12)
    def get_MediaCategory(self) -> Windows.Media.Capture.MediaCategory: ...
    @winrt_commethod(13)
    def get_AudioProcessing(self) -> Windows.Media.AudioProcessing: ...
    ConcurrentRecordAndPhotoSupported = property(get_ConcurrentRecordAndPhotoSupported, None)
    ConcurrentRecordAndPhotoSequenceSupported = property(get_ConcurrentRecordAndPhotoSequenceSupported, None)
    CameraSoundRequiredForRegion = property(get_CameraSoundRequiredForRegion, None)
    Horizontal35mmEquivalentFocalLength = property(get_Horizontal35mmEquivalentFocalLength, None)
    PitchOffsetDegrees = property(get_PitchOffsetDegrees, None)
    Vertical35mmEquivalentFocalLength = property(get_Vertical35mmEquivalentFocalLength, None)
    MediaCategory = property(get_MediaCategory, None)
    AudioProcessing = property(get_AudioProcessing, None)
class IMediaCaptureSettings3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('303c67c2-8058-4b1b-b8-77-8c-2e-f3-52-84-40')
    @winrt_commethod(6)
    def get_Direct3D11Device(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    Direct3D11Device = property(get_Direct3D11Device, None)
class IMediaCaptureStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('acef81ff-99ed-4645-96-5e-19-25-cf-c6-38-34')
    @winrt_commethod(6)
    def IsVideoProfileSupported(self, videoDeviceId: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def FindAllVideoProfiles(self, videoDeviceId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_commethod(8)
    def FindConcurrentProfiles(self, videoDeviceId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_commethod(9)
    def FindKnownVideoProfiles(self, videoDeviceId: WinRT_String, name: Windows.Media.Capture.KnownVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
class IMediaCaptureStopResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f9db6a2a-a092-4ad1-97-d4-f2-01-f9-d0-82-db')
    @winrt_commethod(6)
    def get_LastFrame(self) -> Windows.Media.VideoFrame: ...
    @winrt_commethod(7)
    def get_RecordDuration(self) -> Windows.Foundation.TimeSpan: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class IMediaCaptureVideoPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('27727073-549e-447f-a2-0a-4f-03-c4-79-d8-c0')
    @winrt_commethod(6)
    def StartPreviewAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StartPreviewToCustomSinkAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def StartPreviewToCustomSinkIdAsync(self, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def StopPreviewAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IMediaCaptureVideoProfile(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('21a073bf-a3ee-4ecf-9e-f6-50-b0-bc-4e-13-05')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SupportedPreviewMediaDescription(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(9)
    def get_SupportedRecordMediaDescription(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(10)
    def get_SupportedPhotoMediaDescription(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_commethod(11)
    def GetConcurrency(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    Id = property(get_Id, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    SupportedPreviewMediaDescription = property(get_SupportedPreviewMediaDescription, None)
    SupportedRecordMediaDescription = property(get_SupportedRecordMediaDescription, None)
    SupportedPhotoMediaDescription = property(get_SupportedPhotoMediaDescription, None)
class IMediaCaptureVideoProfile2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('97ddc95f-94ce-468f-93-16-fc-5b-c2-63-8f-6b')
    @winrt_commethod(6)
    def get_FrameSourceInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    FrameSourceInfos = property(get_FrameSourceInfos, None)
    Properties = property(get_Properties, None)
class IMediaCaptureVideoProfileMediaDescription(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8012afef-b691-49ff-83-f2-c1-e7-6e-aa-ea-1b')
    @winrt_commethod(6)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_FrameRate(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsVariablePhotoSequenceSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsHdrVideoSupported(self) -> Boolean: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameRate = property(get_FrameRate, None)
    IsVariablePhotoSequenceSupported = property(get_IsVariablePhotoSequenceSupported, None)
    IsHdrVideoSupported = property(get_IsHdrVideoSupported, None)
class IMediaCaptureVideoProfileMediaDescription2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c6a6ef13-322d-413a-b8-5a-68-a8-8e-02-f4-e9')
    @winrt_commethod(6)
    def get_Subtype(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Subtype = property(get_Subtype, None)
    Properties = property(get_Properties, None)
class IOptionalReferencePhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('470f88b3-1e6d-4051-9c-8b-f1-d8-5a-f0-47-b7')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Context(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Frame = property(get_Frame, None)
    Context = property(get_Context, None)
class IPhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('373bfbc1-984e-4ff0-bf-85-1c-00-aa-bc-5a-45')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_Thumbnail(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(8)
    def get_CaptureTimeOffset(self) -> Windows.Foundation.TimeSpan: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
class IPhotoConfirmationCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab473672-c28a-4827-8f-8d-36-36-d3-be-b5-1e')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_CaptureTimeOffset(self) -> Windows.Foundation.TimeSpan: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
class IVideoStreamConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d8770a6f-4390-4b5e-ad-3e-0f-8a-f0-96-34-90')
    @winrt_commethod(6)
    def get_InputProperties(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(7)
    def get_OutputProperties(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    InputProperties = property(get_InputProperties, None)
    OutputProperties = property(get_OutputProperties, None)
KnownVideoProfile = Int32
KnownVideoProfile_VideoRecording: KnownVideoProfile = 0
KnownVideoProfile_HighQualityPhoto: KnownVideoProfile = 1
KnownVideoProfile_BalancedVideoAndPhoto: KnownVideoProfile = 2
KnownVideoProfile_VideoConferencing: KnownVideoProfile = 3
KnownVideoProfile_PhotoSequence: KnownVideoProfile = 4
KnownVideoProfile_HighFrameRate: KnownVideoProfile = 5
KnownVideoProfile_VariablePhotoSequence: KnownVideoProfile = 6
KnownVideoProfile_HdrWithWcgVideo: KnownVideoProfile = 7
KnownVideoProfile_HdrWithWcgPhoto: KnownVideoProfile = 8
KnownVideoProfile_VideoHdr8: KnownVideoProfile = 9
KnownVideoProfile_CompressedCamera: KnownVideoProfile = 10
class LowLagMediaRecording(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.LowLagMediaRecording'
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Capture.ILowLagMediaRecording) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.Capture.ILowLagMediaRecording) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Media.Capture.ILowLagMediaRecording) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseAsync(self: Windows.Media.Capture.ILowLagMediaRecording2, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeAsync(self: Windows.Media.Capture.ILowLagMediaRecording2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseWithResultAsync(self: Windows.Media.Capture.ILowLagMediaRecording3, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_mixinmethod
    def StopWithResultAsync(self: Windows.Media.Capture.ILowLagMediaRecording3) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCaptureStopResult]: ...
class LowLagPhotoCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.LowLagPhotoCapture'
    @winrt_mixinmethod
    def CaptureAsync(self: Windows.Media.Capture.ILowLagPhotoCapture) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.CapturedPhoto]: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Media.Capture.ILowLagPhotoCapture) -> Windows.Foundation.IAsyncAction: ...
class LowLagPhotoSequenceCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.LowLagPhotoSequenceCapture'
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Media.Capture.ILowLagPhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_PhotoCaptured(self: Windows.Media.Capture.ILowLagPhotoSequenceCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.LowLagPhotoSequenceCapture, Windows.Media.Capture.PhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoCaptured(self: Windows.Media.Capture.ILowLagPhotoSequenceCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class MediaCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCapture'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Capture.MediaCapture: ...
    @winrt_mixinmethod
    def InitializeAsync(self: Windows.Media.Capture.IMediaCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def InitializeWithSettingsAsync(self: Windows.Media.Capture.IMediaCapture, mediaCaptureInitializationSettings: Windows.Media.Capture.MediaCaptureInitializationSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToStorageFileAsync(self: Windows.Media.Capture.IMediaCapture, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToStreamAsync(self: Windows.Media.Capture.IMediaCapture, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToCustomSinkAsync(self: Windows.Media.Capture.IMediaCapture, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartRecordToCustomSinkIdAsync(self: Windows.Media.Capture.IMediaCapture, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopRecordAsync(self: Windows.Media.Capture.IMediaCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CapturePhotoToStorageFileAsync(self: Windows.Media.Capture.IMediaCapture, type: Windows.Media.MediaProperties.ImageEncodingProperties, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CapturePhotoToStreamAsync(self: Windows.Media.Capture.IMediaCapture, type: Windows.Media.MediaProperties.ImageEncodingProperties, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AddEffectAsync(self: Windows.Media.Capture.IMediaCapture, mediaStreamType: Windows.Media.Capture.MediaStreamType, effectActivationID: WinRT_String, effectSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearEffectsAsync(self: Windows.Media.Capture.IMediaCapture, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetEncoderProperty(self: Windows.Media.Capture.IMediaCapture, mediaStreamType: Windows.Media.Capture.MediaStreamType, propertyId: Guid, propertyValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def GetEncoderProperty(self: Windows.Media.Capture.IMediaCapture, mediaStreamType: Windows.Media.Capture.MediaStreamType, propertyId: Guid) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def add_Failed(self: Windows.Media.Capture.IMediaCapture, errorEventHandler: Windows.Media.Capture.MediaCaptureFailedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Failed(self: Windows.Media.Capture.IMediaCapture, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RecordLimitationExceeded(self: Windows.Media.Capture.IMediaCapture, recordLimitationExceededEventHandler: Windows.Media.Capture.RecordLimitationExceededEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecordLimitationExceeded(self: Windows.Media.Capture.IMediaCapture, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MediaCaptureSettings(self: Windows.Media.Capture.IMediaCapture) -> Windows.Media.Capture.MediaCaptureSettings: ...
    @winrt_mixinmethod
    def get_AudioDeviceController(self: Windows.Media.Capture.IMediaCapture) -> Windows.Media.Devices.AudioDeviceController: ...
    @winrt_mixinmethod
    def get_VideoDeviceController(self: Windows.Media.Capture.IMediaCapture) -> Windows.Media.Devices.VideoDeviceController: ...
    @winrt_mixinmethod
    def SetPreviewMirroring(self: Windows.Media.Capture.IMediaCapture, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetPreviewMirroring(self: Windows.Media.Capture.IMediaCapture) -> Boolean: ...
    @winrt_mixinmethod
    def SetPreviewRotation(self: Windows.Media.Capture.IMediaCapture, value: Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_mixinmethod
    def GetPreviewRotation(self: Windows.Media.Capture.IMediaCapture) -> Windows.Media.Capture.VideoRotation: ...
    @winrt_mixinmethod
    def SetRecordRotation(self: Windows.Media.Capture.IMediaCapture, value: Windows.Media.Capture.VideoRotation) -> Void: ...
    @winrt_mixinmethod
    def GetRecordRotation(self: Windows.Media.Capture.IMediaCapture) -> Windows.Media.Capture.VideoRotation: ...
    @winrt_mixinmethod
    def StartPreviewAsync(self: Windows.Media.Capture.IMediaCaptureVideoPreview) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartPreviewToCustomSinkAsync(self: Windows.Media.Capture.IMediaCaptureVideoPreview, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartPreviewToCustomSinkIdAsync(self: Windows.Media.Capture.IMediaCaptureVideoPreview, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopPreviewAsync(self: Windows.Media.Capture.IMediaCaptureVideoPreview) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToStorageFileAsync(self: Windows.Media.Capture.IMediaCapture2, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToStreamAsync(self: Windows.Media.Capture.IMediaCapture2, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToCustomSinkAsync(self: Windows.Media.Capture.IMediaCapture2, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customMediaSink: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagRecordToCustomSinkIdAsync(self: Windows.Media.Capture.IMediaCapture2, encodingProfile: Windows.Media.MediaProperties.MediaEncodingProfile, customSinkActivationId: WinRT_String, customSinkSettings: Windows.Foundation.Collections.IPropertySet) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagMediaRecording]: ...
    @winrt_mixinmethod
    def PrepareLowLagPhotoCaptureAsync(self: Windows.Media.Capture.IMediaCapture2, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagPhotoCapture]: ...
    @winrt_mixinmethod
    def PrepareLowLagPhotoSequenceCaptureAsync(self: Windows.Media.Capture.IMediaCapture2, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.LowLagPhotoSequenceCapture]: ...
    @winrt_mixinmethod
    def SetEncodingPropertiesAsync(self: Windows.Media.Capture.IMediaCapture2, mediaStreamType: Windows.Media.Capture.MediaStreamType, mediaEncodingProperties: Windows.Media.MediaProperties.IMediaEncodingProperties, encoderProperties: Windows.Media.MediaProperties.MediaPropertySet) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def PrepareVariablePhotoSequenceCaptureAsync(self: Windows.Media.Capture.IMediaCapture3, type: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Core.VariablePhotoSequenceCapture]: ...
    @winrt_mixinmethod
    def add_FocusChanged(self: Windows.Media.Capture.IMediaCapture3, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.MediaCaptureFocusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FocusChanged(self: Windows.Media.Capture.IMediaCapture3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PhotoConfirmationCaptured(self: Windows.Media.Capture.IMediaCapture3, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.PhotoConfirmationCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoConfirmationCaptured(self: Windows.Media.Capture.IMediaCapture3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddAudioEffectAsync(self: Windows.Media.Capture.IMediaCapture4, definition: Windows.Media.Effects.IAudioEffectDefinition) -> Windows.Foundation.IAsyncOperation[Windows.Media.IMediaExtension]: ...
    @winrt_mixinmethod
    def AddVideoEffectAsync(self: Windows.Media.Capture.IMediaCapture4, definition: Windows.Media.Effects.IVideoEffectDefinition, mediaStreamType: Windows.Media.Capture.MediaStreamType) -> Windows.Foundation.IAsyncOperation[Windows.Media.IMediaExtension]: ...
    @winrt_mixinmethod
    def PauseRecordAsync(self: Windows.Media.Capture.IMediaCapture4, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeRecordAsync(self: Windows.Media.Capture.IMediaCapture4) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_CameraStreamStateChanged(self: Windows.Media.Capture.IMediaCapture4, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraStreamStateChanged(self: Windows.Media.Capture.IMediaCapture4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CameraStreamState(self: Windows.Media.Capture.IMediaCapture4) -> Windows.Media.Devices.CameraStreamState: ...
    @winrt_mixinmethod
    def GetPreviewFrameAsync(self: Windows.Media.Capture.IMediaCapture4) -> Windows.Foundation.IAsyncOperation[Windows.Media.VideoFrame]: ...
    @winrt_mixinmethod
    def GetPreviewFrameCopyAsync(self: Windows.Media.Capture.IMediaCapture4, destination: Windows.Media.VideoFrame) -> Windows.Foundation.IAsyncOperation[Windows.Media.VideoFrame]: ...
    @winrt_mixinmethod
    def add_ThermalStatusChanged(self: Windows.Media.Capture.IMediaCapture4, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ThermalStatusChanged(self: Windows.Media.Capture.IMediaCapture4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ThermalStatus(self: Windows.Media.Capture.IMediaCapture4) -> Windows.Media.Capture.MediaCaptureThermalStatus: ...
    @winrt_mixinmethod
    def PrepareAdvancedPhotoCaptureAsync(self: Windows.Media.Capture.IMediaCapture4, encodingProperties: Windows.Media.MediaProperties.ImageEncodingProperties) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.AdvancedPhotoCapture]: ...
    @winrt_mixinmethod
    def RemoveEffectAsync(self: Windows.Media.Capture.IMediaCapture5, effect: Windows.Media.IMediaExtension) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseRecordWithResultAsync(self: Windows.Media.Capture.IMediaCapture5, behavior: Windows.Media.Devices.MediaCapturePauseBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCapturePauseResult]: ...
    @winrt_mixinmethod
    def StopRecordWithResultAsync(self: Windows.Media.Capture.IMediaCapture5) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.MediaCaptureStopResult]: ...
    @winrt_mixinmethod
    def get_FrameSources(self: Windows.Media.Capture.IMediaCapture5) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Media.Capture.Frames.MediaFrameSource]: ...
    @winrt_mixinmethod
    def CreateFrameReaderAsync(self: Windows.Media.Capture.IMediaCapture5, inputSource: Windows.Media.Capture.Frames.MediaFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithSubtypeAsync(self: Windows.Media.Capture.IMediaCapture5, inputSource: Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithSubtypeAndSizeAsync(self: Windows.Media.Capture.IMediaCapture5, inputSource: Windows.Media.Capture.Frames.MediaFrameSource, outputSubtype: WinRT_String, outputSize: Windows.Graphics.Imaging.BitmapSize) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MediaFrameReader]: ...
    @winrt_mixinmethod
    def add_CaptureDeviceExclusiveControlStatusChanged(self: Windows.Media.Capture.IMediaCapture6, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCapture, Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CaptureDeviceExclusiveControlStatusChanged(self: Windows.Media.Capture.IMediaCapture6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateMultiSourceFrameReaderAsync(self: Windows.Media.Capture.IMediaCapture6, inputSources: Windows.Foundation.Collections.IIterable[Windows.Media.Capture.Frames.MediaFrameSource]) -> Windows.Foundation.IAsyncOperation[Windows.Media.Capture.Frames.MultiSourceMediaFrameReader]: ...
    @winrt_mixinmethod
    def CreateRelativePanelWatcher(self: Windows.Media.Capture.IMediaCapture7, captureMode: Windows.Media.Capture.StreamingCaptureMode, displayRegion: Windows.UI.WindowManagement.DisplayRegion) -> Windows.Media.Capture.MediaCaptureRelativePanelWatcher: ...
    @winrt_classmethod
    def IsVideoProfileSupported(cls: Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def FindAllVideoProfiles(cls: Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_classmethod
    def FindConcurrentProfiles(cls: Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_classmethod
    def FindKnownVideoProfiles(cls: Windows.Media.Capture.IMediaCaptureStatics, videoDeviceId: WinRT_String, name: Windows.Media.Capture.KnownVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    MediaCaptureSettings = property(get_MediaCaptureSettings, None)
    AudioDeviceController = property(get_AudioDeviceController, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
    CameraStreamState = property(get_CameraStreamState, None)
    ThermalStatus = property(get_ThermalStatus, None)
    FrameSources = property(get_FrameSources, None)
MediaCaptureDeviceExclusiveControlReleaseMode = Int32
MediaCaptureDeviceExclusiveControlReleaseMode_OnDispose: MediaCaptureDeviceExclusiveControlReleaseMode = 0
MediaCaptureDeviceExclusiveControlReleaseMode_OnAllStreamsStopped: MediaCaptureDeviceExclusiveControlReleaseMode = 1
MediaCaptureDeviceExclusiveControlStatus = Int32
MediaCaptureDeviceExclusiveControlStatus_ExclusiveControlAvailable: MediaCaptureDeviceExclusiveControlStatus = 0
MediaCaptureDeviceExclusiveControlStatus_SharedReadOnlyAvailable: MediaCaptureDeviceExclusiveControlStatus = 1
class MediaCaptureDeviceExclusiveControlStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Media.Capture.IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs) -> Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatus: ...
    DeviceId = property(get_DeviceId, None)
    Status = property(get_Status, None)
class MediaCaptureFailedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureFailedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: Windows.Media.Capture.IMediaCaptureFailedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Code(self: Windows.Media.Capture.IMediaCaptureFailedEventArgs) -> UInt32: ...
    Message = property(get_Message, None)
    Code = property(get_Code, None)
class MediaCaptureFailedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2014effb-5cd8-4f08-a3-14-0d-36-0d-a5-9f-14')
    ClassId = 'Windows.Media.Capture.MediaCaptureFailedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Media.Capture.MediaCapture, errorEventArgs: Windows.Media.Capture.MediaCaptureFailedEventArgs) -> Void: ...
class MediaCaptureFocusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureFocusChangedEventArgs'
    @winrt_mixinmethod
    def get_FocusState(self: Windows.Media.Capture.IMediaCaptureFocusChangedEventArgs) -> Windows.Media.Devices.MediaCaptureFocusState: ...
    FocusState = property(get_FocusState, None)
class MediaCaptureInitializationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureInitializationSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.Capture.MediaCaptureInitializationSettings: ...
    @winrt_mixinmethod
    def put_AudioDeviceId(self: Windows.Media.Capture.IMediaCaptureInitializationSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AudioDeviceId(self: Windows.Media.Capture.IMediaCaptureInitializationSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VideoDeviceId(self: Windows.Media.Capture.IMediaCaptureInitializationSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: Windows.Media.Capture.IMediaCaptureInitializationSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreamingCaptureMode(self: Windows.Media.Capture.IMediaCaptureInitializationSettings, value: Windows.Media.Capture.StreamingCaptureMode) -> Void: ...
    @winrt_mixinmethod
    def get_StreamingCaptureMode(self: Windows.Media.Capture.IMediaCaptureInitializationSettings) -> Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_mixinmethod
    def put_PhotoCaptureSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings, value: Windows.Media.Capture.PhotoCaptureSource) -> Void: ...
    @winrt_mixinmethod
    def get_PhotoCaptureSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings) -> Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_mixinmethod
    def put_MediaCategory(self: Windows.Media.Capture.IMediaCaptureInitializationSettings2, value: Windows.Media.Capture.MediaCategory) -> Void: ...
    @winrt_mixinmethod
    def get_MediaCategory(self: Windows.Media.Capture.IMediaCaptureInitializationSettings2) -> Windows.Media.Capture.MediaCategory: ...
    @winrt_mixinmethod
    def put_AudioProcessing(self: Windows.Media.Capture.IMediaCaptureInitializationSettings2, value: Windows.Media.AudioProcessing) -> Void: ...
    @winrt_mixinmethod
    def get_AudioProcessing(self: Windows.Media.Capture.IMediaCaptureInitializationSettings2) -> Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def put_AudioSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings3, value: Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_mixinmethod
    def get_AudioSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings3) -> Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def put_VideoSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings3, value: Windows.Media.Core.IMediaSource) -> Void: ...
    @winrt_mixinmethod
    def get_VideoSource(self: Windows.Media.Capture.IMediaCaptureInitializationSettings3) -> Windows.Media.Core.IMediaSource: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> Windows.Media.Capture.MediaCaptureVideoProfile: ...
    @winrt_mixinmethod
    def put_VideoProfile(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: Windows.Media.Capture.MediaCaptureVideoProfile) -> Void: ...
    @winrt_mixinmethod
    def get_PreviewMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_PreviewMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_RecordMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_RecordMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_PhotoMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4) -> Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription: ...
    @winrt_mixinmethod
    def put_PhotoMediaDescription(self: Windows.Media.Capture.IMediaCaptureInitializationSettings4, value: Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription) -> Void: ...
    @winrt_mixinmethod
    def get_SourceGroup(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> Windows.Media.Capture.Frames.MediaFrameSourceGroup: ...
    @winrt_mixinmethod
    def put_SourceGroup(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: Windows.Media.Capture.Frames.MediaFrameSourceGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> Windows.Media.Capture.MediaCaptureSharingMode: ...
    @winrt_mixinmethod
    def put_SharingMode(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: Windows.Media.Capture.MediaCaptureSharingMode) -> Void: ...
    @winrt_mixinmethod
    def get_MemoryPreference(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5) -> Windows.Media.Capture.MediaCaptureMemoryPreference: ...
    @winrt_mixinmethod
    def put_MemoryPreference(self: Windows.Media.Capture.IMediaCaptureInitializationSettings5, value: Windows.Media.Capture.MediaCaptureMemoryPreference) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysPlaySystemShutterSound(self: Windows.Media.Capture.IMediaCaptureInitializationSettings6) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysPlaySystemShutterSound(self: Windows.Media.Capture.IMediaCaptureInitializationSettings6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceUriPasswordCredential(self: Windows.Media.Capture.IMediaCaptureInitializationSettings7) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_DeviceUriPasswordCredential(self: Windows.Media.Capture.IMediaCaptureInitializationSettings7, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceUri(self: Windows.Media.Capture.IMediaCaptureInitializationSettings7) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_DeviceUri(self: Windows.Media.Capture.IMediaCaptureInitializationSettings7, value: Windows.Foundation.Uri) -> Void: ...
    AudioDeviceId = property(get_AudioDeviceId, put_AudioDeviceId)
    VideoDeviceId = property(get_VideoDeviceId, put_VideoDeviceId)
    StreamingCaptureMode = property(get_StreamingCaptureMode, put_StreamingCaptureMode)
    PhotoCaptureSource = property(get_PhotoCaptureSource, put_PhotoCaptureSource)
    MediaCategory = property(get_MediaCategory, put_MediaCategory)
    AudioProcessing = property(get_AudioProcessing, put_AudioProcessing)
    AudioSource = property(get_AudioSource, put_AudioSource)
    VideoSource = property(get_VideoSource, put_VideoSource)
    VideoProfile = property(get_VideoProfile, put_VideoProfile)
    PreviewMediaDescription = property(get_PreviewMediaDescription, put_PreviewMediaDescription)
    RecordMediaDescription = property(get_RecordMediaDescription, put_RecordMediaDescription)
    PhotoMediaDescription = property(get_PhotoMediaDescription, put_PhotoMediaDescription)
    SourceGroup = property(get_SourceGroup, put_SourceGroup)
    SharingMode = property(get_SharingMode, put_SharingMode)
    MemoryPreference = property(get_MemoryPreference, put_MemoryPreference)
    AlwaysPlaySystemShutterSound = property(get_AlwaysPlaySystemShutterSound, put_AlwaysPlaySystemShutterSound)
    DeviceUriPasswordCredential = property(get_DeviceUriPasswordCredential, put_DeviceUriPasswordCredential)
    DeviceUri = property(get_DeviceUri, put_DeviceUri)
MediaCaptureMemoryPreference = Int32
MediaCaptureMemoryPreference_Auto: MediaCaptureMemoryPreference = 0
MediaCaptureMemoryPreference_Cpu: MediaCaptureMemoryPreference = 1
class MediaCapturePauseResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCapturePauseResult'
    @winrt_mixinmethod
    def get_LastFrame(self: Windows.Media.Capture.IMediaCapturePauseResult) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_RecordDuration(self: Windows.Media.Capture.IMediaCapturePauseResult) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
class MediaCaptureRelativePanelWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureRelativePanelWatcher'
    @winrt_mixinmethod
    def get_RelativePanel(self: Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> Windows.Devices.Enumeration.Panel: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.Media.Capture.IMediaCaptureRelativePanelWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.MediaCaptureRelativePanelWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.Media.Capture.IMediaCaptureRelativePanelWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Media.Capture.IMediaCaptureRelativePanelWatcher) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    RelativePanel = property(get_RelativePanel, None)
class MediaCaptureSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureSettings'
    @winrt_mixinmethod
    def get_AudioDeviceId(self: Windows.Media.Capture.IMediaCaptureSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: Windows.Media.Capture.IMediaCaptureSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StreamingCaptureMode(self: Windows.Media.Capture.IMediaCaptureSettings) -> Windows.Media.Capture.StreamingCaptureMode: ...
    @winrt_mixinmethod
    def get_PhotoCaptureSource(self: Windows.Media.Capture.IMediaCaptureSettings) -> Windows.Media.Capture.PhotoCaptureSource: ...
    @winrt_mixinmethod
    def get_VideoDeviceCharacteristic(self: Windows.Media.Capture.IMediaCaptureSettings) -> Windows.Media.Capture.VideoDeviceCharacteristic: ...
    @winrt_mixinmethod
    def get_ConcurrentRecordAndPhotoSupported(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ConcurrentRecordAndPhotoSequenceSupported(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CameraSoundRequiredForRegion(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Horizontal35mmEquivalentFocalLength(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_PitchOffsetDegrees(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Vertical35mmEquivalentFocalLength(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_MediaCategory(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Windows.Media.Capture.MediaCategory: ...
    @winrt_mixinmethod
    def get_AudioProcessing(self: Windows.Media.Capture.IMediaCaptureSettings2) -> Windows.Media.AudioProcessing: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: Windows.Media.Capture.IMediaCaptureSettings3) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    AudioDeviceId = property(get_AudioDeviceId, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    StreamingCaptureMode = property(get_StreamingCaptureMode, None)
    PhotoCaptureSource = property(get_PhotoCaptureSource, None)
    VideoDeviceCharacteristic = property(get_VideoDeviceCharacteristic, None)
    ConcurrentRecordAndPhotoSupported = property(get_ConcurrentRecordAndPhotoSupported, None)
    ConcurrentRecordAndPhotoSequenceSupported = property(get_ConcurrentRecordAndPhotoSequenceSupported, None)
    CameraSoundRequiredForRegion = property(get_CameraSoundRequiredForRegion, None)
    Horizontal35mmEquivalentFocalLength = property(get_Horizontal35mmEquivalentFocalLength, None)
    PitchOffsetDegrees = property(get_PitchOffsetDegrees, None)
    Vertical35mmEquivalentFocalLength = property(get_Vertical35mmEquivalentFocalLength, None)
    MediaCategory = property(get_MediaCategory, None)
    AudioProcessing = property(get_AudioProcessing, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
MediaCaptureSharingMode = Int32
MediaCaptureSharingMode_ExclusiveControl: MediaCaptureSharingMode = 0
MediaCaptureSharingMode_SharedReadOnly: MediaCaptureSharingMode = 1
class MediaCaptureStopResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureStopResult'
    @winrt_mixinmethod
    def get_LastFrame(self: Windows.Media.Capture.IMediaCaptureStopResult) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_RecordDuration(self: Windows.Media.Capture.IMediaCaptureStopResult) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    LastFrame = property(get_LastFrame, None)
    RecordDuration = property(get_RecordDuration, None)
MediaCaptureThermalStatus = Int32
MediaCaptureThermalStatus_Normal: MediaCaptureThermalStatus = 0
MediaCaptureThermalStatus_Overheated: MediaCaptureThermalStatus = 1
class MediaCaptureVideoProfile(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureVideoProfile'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedPreviewMediaDescription(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def get_SupportedRecordMediaDescription(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def get_SupportedPhotoMediaDescription(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription]: ...
    @winrt_mixinmethod
    def GetConcurrency(self: Windows.Media.Capture.IMediaCaptureVideoProfile) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.MediaCaptureVideoProfile]: ...
    @winrt_mixinmethod
    def get_FrameSourceInfos(self: Windows.Media.Capture.IMediaCaptureVideoProfile2) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Capture.Frames.MediaFrameSourceInfo]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Capture.IMediaCaptureVideoProfile2) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Id = property(get_Id, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    SupportedPreviewMediaDescription = property(get_SupportedPreviewMediaDescription, None)
    SupportedRecordMediaDescription = property(get_SupportedRecordMediaDescription, None)
    SupportedPhotoMediaDescription = property(get_SupportedPhotoMediaDescription, None)
    FrameSourceInfos = property(get_FrameSourceInfos, None)
    Properties = property(get_Properties, None)
class MediaCaptureVideoProfileMediaDescription(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription'
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameRate(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Double: ...
    @winrt_mixinmethod
    def get_IsVariablePhotoSequenceSupported(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHdrVideoSupported(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Capture.IMediaCaptureVideoProfileMediaDescription2) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameRate = property(get_FrameRate, None)
    IsVariablePhotoSequenceSupported = property(get_IsVariablePhotoSequenceSupported, None)
    IsHdrVideoSupported = property(get_IsHdrVideoSupported, None)
    Subtype = property(get_Subtype, None)
    Properties = property(get_Properties, None)
MediaCategory = Int32
MediaCategory_Other: MediaCategory = 0
MediaCategory_Communications: MediaCategory = 1
MediaCategory_Media: MediaCategory = 2
MediaCategory_GameChat: MediaCategory = 3
MediaCategory_Speech: MediaCategory = 4
MediaCategory_FarFieldSpeech: MediaCategory = 5
MediaCategory_UniformSpeech: MediaCategory = 6
MediaCategory_VoiceTyping: MediaCategory = 7
MediaStreamType = Int32
MediaStreamType_VideoPreview: MediaStreamType = 0
MediaStreamType_VideoRecord: MediaStreamType = 1
MediaStreamType_Audio: MediaStreamType = 2
MediaStreamType_Photo: MediaStreamType = 3
MediaStreamType_Metadata: MediaStreamType = 4
class OptionalReferencePhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.OptionalReferencePhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Context(self: Windows.Media.Capture.IOptionalReferencePhotoCapturedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Frame = property(get_Frame, None)
    Context = property(get_Context, None)
PhotoCaptureSource = Int32
PhotoCaptureSource_Auto: PhotoCaptureSource = 0
PhotoCaptureSource_VideoPreview: PhotoCaptureSource = 1
PhotoCaptureSource_Photo: PhotoCaptureSource = 2
class PhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.PhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.IPhotoCapturedEventArgs) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Capture.IPhotoCapturedEventArgs) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: Windows.Media.Capture.IPhotoCapturedEventArgs) -> Windows.Foundation.TimeSpan: ...
    Frame = property(get_Frame, None)
    Thumbnail = property(get_Thumbnail, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
class PhotoConfirmationCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.PhotoConfirmationCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: Windows.Media.Capture.IPhotoConfirmationCapturedEventArgs) -> Windows.Foundation.TimeSpan: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
PowerlineFrequency = Int32
PowerlineFrequency_Disabled: PowerlineFrequency = 0
PowerlineFrequency_FiftyHertz: PowerlineFrequency = 1
PowerlineFrequency_SixtyHertz: PowerlineFrequency = 2
PowerlineFrequency_Auto: PowerlineFrequency = 3
class RecordLimitationExceededEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3fae8f2e-4fe1-4ffd-aa-ba-e1-f1-33-7d-4e-53')
    ClassId = 'Windows.Media.Capture.RecordLimitationExceededEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Media.Capture.MediaCapture) -> Void: ...
StreamingCaptureMode = Int32
StreamingCaptureMode_AudioAndVideo: StreamingCaptureMode = 0
StreamingCaptureMode_Audio: StreamingCaptureMode = 1
StreamingCaptureMode_Video: StreamingCaptureMode = 2
VideoDeviceCharacteristic = Int32
VideoDeviceCharacteristic_AllStreamsIndependent: VideoDeviceCharacteristic = 0
VideoDeviceCharacteristic_PreviewRecordStreamsIdentical: VideoDeviceCharacteristic = 1
VideoDeviceCharacteristic_PreviewPhotoStreamsIdentical: VideoDeviceCharacteristic = 2
VideoDeviceCharacteristic_RecordPhotoStreamsIdentical: VideoDeviceCharacteristic = 3
VideoDeviceCharacteristic_AllStreamsIdentical: VideoDeviceCharacteristic = 4
VideoRotation = Int32
VideoRotation_None: VideoRotation = 0
VideoRotation_Clockwise90Degrees: VideoRotation = 1
VideoRotation_Clockwise180Degrees: VideoRotation = 2
VideoRotation_Clockwise270Degrees: VideoRotation = 3
class VideoStreamConfiguration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.VideoStreamConfiguration'
    @winrt_mixinmethod
    def get_InputProperties(self: Windows.Media.Capture.IVideoStreamConfiguration) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_OutputProperties(self: Windows.Media.Capture.IVideoStreamConfiguration) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    InputProperties = property(get_InputProperties, None)
    OutputProperties = property(get_OutputProperties, None)
class WhiteBalanceGain(EasyCastStructure):
    R: Double
    G: Double
    B: Double
make_head(_module, 'AdvancedCapturedPhoto')
make_head(_module, 'AdvancedPhotoCapture')
make_head(_module, 'AppCapture')
make_head(_module, 'CameraCaptureUI')
make_head(_module, 'CameraCaptureUIPhotoCaptureSettings')
make_head(_module, 'CameraCaptureUIVideoCaptureSettings')
make_head(_module, 'CapturedFrame')
make_head(_module, 'CapturedFrameControlValues')
make_head(_module, 'CapturedPhoto')
make_head(_module, 'IAdvancedCapturedPhoto')
make_head(_module, 'IAdvancedCapturedPhoto2')
make_head(_module, 'IAdvancedPhotoCapture')
make_head(_module, 'IAppCapture')
make_head(_module, 'IAppCaptureStatics')
make_head(_module, 'IAppCaptureStatics2')
make_head(_module, 'ICameraCaptureUI')
make_head(_module, 'ICameraCaptureUIPhotoCaptureSettings')
make_head(_module, 'ICameraCaptureUIVideoCaptureSettings')
make_head(_module, 'ICapturedFrame')
make_head(_module, 'ICapturedFrame2')
make_head(_module, 'ICapturedFrameControlValues')
make_head(_module, 'ICapturedFrameControlValues2')
make_head(_module, 'ICapturedFrameWithSoftwareBitmap')
make_head(_module, 'ICapturedPhoto')
make_head(_module, 'ILowLagMediaRecording')
make_head(_module, 'ILowLagMediaRecording2')
make_head(_module, 'ILowLagMediaRecording3')
make_head(_module, 'ILowLagPhotoCapture')
make_head(_module, 'ILowLagPhotoSequenceCapture')
make_head(_module, 'IMediaCapture')
make_head(_module, 'IMediaCapture2')
make_head(_module, 'IMediaCapture3')
make_head(_module, 'IMediaCapture4')
make_head(_module, 'IMediaCapture5')
make_head(_module, 'IMediaCapture6')
make_head(_module, 'IMediaCapture7')
make_head(_module, 'IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs')
make_head(_module, 'IMediaCaptureFailedEventArgs')
make_head(_module, 'IMediaCaptureFocusChangedEventArgs')
make_head(_module, 'IMediaCaptureInitializationSettings')
make_head(_module, 'IMediaCaptureInitializationSettings2')
make_head(_module, 'IMediaCaptureInitializationSettings3')
make_head(_module, 'IMediaCaptureInitializationSettings4')
make_head(_module, 'IMediaCaptureInitializationSettings5')
make_head(_module, 'IMediaCaptureInitializationSettings6')
make_head(_module, 'IMediaCaptureInitializationSettings7')
make_head(_module, 'IMediaCapturePauseResult')
make_head(_module, 'IMediaCaptureRelativePanelWatcher')
make_head(_module, 'IMediaCaptureSettings')
make_head(_module, 'IMediaCaptureSettings2')
make_head(_module, 'IMediaCaptureSettings3')
make_head(_module, 'IMediaCaptureStatics')
make_head(_module, 'IMediaCaptureStopResult')
make_head(_module, 'IMediaCaptureVideoPreview')
make_head(_module, 'IMediaCaptureVideoProfile')
make_head(_module, 'IMediaCaptureVideoProfile2')
make_head(_module, 'IMediaCaptureVideoProfileMediaDescription')
make_head(_module, 'IMediaCaptureVideoProfileMediaDescription2')
make_head(_module, 'IOptionalReferencePhotoCapturedEventArgs')
make_head(_module, 'IPhotoCapturedEventArgs')
make_head(_module, 'IPhotoConfirmationCapturedEventArgs')
make_head(_module, 'IVideoStreamConfiguration')
make_head(_module, 'LowLagMediaRecording')
make_head(_module, 'LowLagPhotoCapture')
make_head(_module, 'LowLagPhotoSequenceCapture')
make_head(_module, 'MediaCapture')
make_head(_module, 'MediaCaptureDeviceExclusiveControlStatusChangedEventArgs')
make_head(_module, 'MediaCaptureFailedEventArgs')
make_head(_module, 'MediaCaptureFailedEventHandler')
make_head(_module, 'MediaCaptureFocusChangedEventArgs')
make_head(_module, 'MediaCaptureInitializationSettings')
make_head(_module, 'MediaCapturePauseResult')
make_head(_module, 'MediaCaptureRelativePanelWatcher')
make_head(_module, 'MediaCaptureSettings')
make_head(_module, 'MediaCaptureStopResult')
make_head(_module, 'MediaCaptureVideoProfile')
make_head(_module, 'MediaCaptureVideoProfileMediaDescription')
make_head(_module, 'OptionalReferencePhotoCapturedEventArgs')
make_head(_module, 'PhotoCapturedEventArgs')
make_head(_module, 'PhotoConfirmationCapturedEventArgs')
make_head(_module, 'RecordLimitationExceededEventHandler')
make_head(_module, 'VideoStreamConfiguration')
make_head(_module, 'WhiteBalanceGain')
