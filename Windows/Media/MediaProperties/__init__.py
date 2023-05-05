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
import Windows.Media.Core
import Windows.Media.MediaProperties
import Windows.Storage
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
class AudioEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IAudioEncodingProperties
    _classid_ = 'Windows.Media.MediaProperties.AudioEncodingProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def put_Bitrate(self: Windows.Media.MediaProperties.IAudioEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bitrate(self: Windows.Media.MediaProperties.IAudioEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_ChannelCount(self: Windows.Media.MediaProperties.IAudioEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ChannelCount(self: Windows.Media.MediaProperties.IAudioEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_SampleRate(self: Windows.Media.MediaProperties.IAudioEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_SampleRate(self: Windows.Media.MediaProperties.IAudioEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_BitsPerSample(self: Windows.Media.MediaProperties.IAudioEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BitsPerSample(self: Windows.Media.MediaProperties.IAudioEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetFormatUserData(self: Windows.Media.MediaProperties.IAudioEncodingPropertiesWithFormatUserData, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetFormatUserData(self: Windows.Media.MediaProperties.IAudioEncodingPropertiesWithFormatUserData, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_mixinmethod
    def get_IsSpatial(self: Windows.Media.MediaProperties.IAudioEncodingProperties2) -> Boolean: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.MediaProperties.IAudioEncodingProperties3) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateAlac(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics2, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateFlac(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics2, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateAac(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateAacAdts(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateMp3(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreatePcm(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_classmethod
    def CreateWma(cls: Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    Bitrate = property(get_Bitrate, put_Bitrate)
    ChannelCount = property(get_ChannelCount, put_ChannelCount)
    SampleRate = property(get_SampleRate, put_SampleRate)
    BitsPerSample = property(get_BitsPerSample, put_BitsPerSample)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
    IsSpatial = property(get_IsSpatial, None)
AudioEncodingQuality = Int32
AudioEncodingQuality_Auto: AudioEncodingQuality = 0
AudioEncodingQuality_High: AudioEncodingQuality = 1
AudioEncodingQuality_Medium: AudioEncodingQuality = 2
AudioEncodingQuality_Low: AudioEncodingQuality = 3
class ContainerEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IContainerEncodingProperties
    _classid_ = 'Windows.Media.MediaProperties.ContainerEncodingProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.ContainerEncodingProperties: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.MediaProperties.IContainerEncodingProperties2) -> Windows.Media.MediaProperties.ContainerEncodingProperties: ...
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
class H264ProfileIds(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.H264ProfileIds'
    @winrt_classmethod
    def get_ConstrainedBaseline(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_Baseline(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_Extended(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_Main(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_High(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_High10(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_High422(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_High444(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_StereoHigh(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_MultiviewHigh(cls: Windows.Media.MediaProperties.IH264ProfileIdsStatics) -> Int32: ...
    ConstrainedBaseline = property(get_ConstrainedBaseline, None)
    Baseline = property(get_Baseline, None)
    Extended = property(get_Extended, None)
    Main = property(get_Main, None)
    High = property(get_High, None)
    High10 = property(get_High10, None)
    High422 = property(get_High422, None)
    High444 = property(get_High444, None)
    StereoHigh = property(get_StereoHigh, None)
    MultiviewHigh = property(get_MultiviewHigh, None)
class IAudioEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingProperties'
    _iid_ = Guid('{62bc7a16-005c-4b3b-8a0b-0a090e9687f3}')
    @winrt_commethod(6)
    def put_Bitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_Bitrate(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ChannelCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ChannelCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_SampleRate(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_SampleRate(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_BitsPerSample(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_BitsPerSample(self) -> UInt32: ...
    Bitrate = property(get_Bitrate, put_Bitrate)
    ChannelCount = property(get_ChannelCount, put_ChannelCount)
    SampleRate = property(get_SampleRate, put_SampleRate)
    BitsPerSample = property(get_BitsPerSample, put_BitsPerSample)
class IAudioEncodingProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingProperties2'
    _iid_ = Guid('{c45d54da-80bd-4c23-80d5-72d4a181e894}')
    @winrt_commethod(6)
    def get_IsSpatial(self) -> Boolean: ...
    IsSpatial = property(get_IsSpatial, None)
class IAudioEncodingProperties3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingProperties3'
    _iid_ = Guid('{87600341-748c-4f8d-b0fd-10caf08ff087}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
class IAudioEncodingPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics'
    _iid_ = Guid('{0cad332c-ebe9-4527-b36d-e42a13cf38db}')
    @winrt_commethod(6)
    def CreateAac(self, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(7)
    def CreateAacAdts(self, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(8)
    def CreateMp3(self, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(9)
    def CreatePcm(self, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(10)
    def CreateWma(self, sampleRate: UInt32, channelCount: UInt32, bitrate: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
class IAudioEncodingPropertiesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingPropertiesStatics2'
    _iid_ = Guid('{7489316f-77a0-433d-8ed5-4040280e8665}')
    @winrt_commethod(6)
    def CreateAlac(self, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(7)
    def CreateFlac(self, sampleRate: UInt32, channelCount: UInt32, bitsPerSample: UInt32) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
class IAudioEncodingPropertiesWithFormatUserData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IAudioEncodingPropertiesWithFormatUserData'
    _iid_ = Guid('{98f10d79-13ea-49ff-be70-2673db69702c}')
    @winrt_commethod(6)
    def SetFormatUserData(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def GetFormatUserData(self, value: POINTER(c_char_p_no)) -> Void: ...
class IContainerEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IContainerEncodingProperties'
    _iid_ = Guid('{59ac2a57-b32a-479e-8a61-4b7f2e9e7ea0}')
class IContainerEncodingProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IContainerEncodingProperties2'
    _iid_ = Guid('{b272c029-ae26-4819-baad-ad7a49b0a876}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.MediaProperties.ContainerEncodingProperties: ...
class IH264ProfileIdsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IH264ProfileIdsStatics'
    _iid_ = Guid('{38654ca7-846a-4f97-a2e5-c3a15bbf70fd}')
    @winrt_commethod(6)
    def get_ConstrainedBaseline(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Baseline(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Extended(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Main(self) -> Int32: ...
    @winrt_commethod(10)
    def get_High(self) -> Int32: ...
    @winrt_commethod(11)
    def get_High10(self) -> Int32: ...
    @winrt_commethod(12)
    def get_High422(self) -> Int32: ...
    @winrt_commethod(13)
    def get_High444(self) -> Int32: ...
    @winrt_commethod(14)
    def get_StereoHigh(self) -> Int32: ...
    @winrt_commethod(15)
    def get_MultiviewHigh(self) -> Int32: ...
    ConstrainedBaseline = property(get_ConstrainedBaseline, None)
    Baseline = property(get_Baseline, None)
    Extended = property(get_Extended, None)
    Main = property(get_Main, None)
    High = property(get_High, None)
    High10 = property(get_High10, None)
    High422 = property(get_High422, None)
    High444 = property(get_High444, None)
    StereoHigh = property(get_StereoHigh, None)
    MultiviewHigh = property(get_MultiviewHigh, None)
class IImageEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IImageEncodingProperties'
    _iid_ = Guid('{78625635-f331-4189-b1c3-b48d5ae034f1}')
    @winrt_commethod(6)
    def put_Width(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_Height(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
class IImageEncodingProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IImageEncodingProperties2'
    _iid_ = Guid('{c854a2df-c923-469b-ac8e-6a9f3c1cd9e3}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
class IImageEncodingPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IImageEncodingPropertiesStatics'
    _iid_ = Guid('{257c68dc-8b99-439e-aa59-913a36161297}')
    @winrt_commethod(6)
    def CreateJpeg(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_commethod(7)
    def CreatePng(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_commethod(8)
    def CreateJpegXR(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
class IImageEncodingPropertiesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IImageEncodingPropertiesStatics2'
    _iid_ = Guid('{f6c25b29-3824-46b0-956e-501329e1be3c}')
    @winrt_commethod(6)
    def CreateUncompressed(self, format: Windows.Media.MediaProperties.MediaPixelFormat) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_commethod(7)
    def CreateBmp(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
class IImageEncodingPropertiesStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IImageEncodingPropertiesStatics3'
    _iid_ = Guid('{48f4814d-a2ff-48dc-8ea0-e90680663656}')
    @winrt_commethod(6)
    def CreateHeif(self) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
class IMediaEncodingProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfile'
    _iid_ = Guid('{e7dbf5a8-1db9-4783-876b-3dfe12acfdb3}')
    @winrt_commethod(6)
    def put_Audio(self, value: Windows.Media.MediaProperties.AudioEncodingProperties) -> Void: ...
    @winrt_commethod(7)
    def get_Audio(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(8)
    def put_Video(self, value: Windows.Media.MediaProperties.VideoEncodingProperties) -> Void: ...
    @winrt_commethod(9)
    def get_Video(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(10)
    def put_Container(self, value: Windows.Media.MediaProperties.ContainerEncodingProperties) -> Void: ...
    @winrt_commethod(11)
    def get_Container(self) -> Windows.Media.MediaProperties.ContainerEncodingProperties: ...
    Audio = property(get_Audio, put_Audio)
    Video = property(get_Video, put_Video)
    Container = property(get_Container, put_Container)
class IMediaEncodingProfile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfile2'
    _iid_ = Guid('{349b3e0a-4035-488e-9877-85632865ed10}')
    @winrt_commethod(6)
    def SetAudioTracks(self, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.AudioStreamDescriptor]) -> Void: ...
    @winrt_commethod(7)
    def GetAudioTracks(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.AudioStreamDescriptor]: ...
    @winrt_commethod(8)
    def SetVideoTracks(self, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_commethod(9)
    def GetVideoTracks(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.VideoStreamDescriptor]: ...
class IMediaEncodingProfile3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfile3'
    _iid_ = Guid('{ba6ebe88-7570-4e69-accf-5611ad015f88}')
    @winrt_commethod(6)
    def SetTimedMetadataTracks(self, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.TimedMetadataStreamDescriptor]) -> Void: ...
    @winrt_commethod(7)
    def GetTimedMetadataTracks(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedMetadataStreamDescriptor]: ...
class IMediaEncodingProfileStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfileStatics'
    _iid_ = Guid('{197f352c-2ede-4a45-a896-817a4854f8fe}')
    @winrt_commethod(6)
    def CreateM4a(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(7)
    def CreateMp3(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(8)
    def CreateWma(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(9)
    def CreateMp4(self, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(10)
    def CreateWmv(self, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(11)
    def CreateFromFileAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.MediaProperties.MediaEncodingProfile]: ...
    @winrt_commethod(12)
    def CreateFromStreamAsync(self, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Media.MediaProperties.MediaEncodingProfile]: ...
class IMediaEncodingProfileStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfileStatics2'
    _iid_ = Guid('{ce8de74f-6af4-4288-8fe2-79adf1f79a43}')
    @winrt_commethod(6)
    def CreateWav(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(7)
    def CreateAvi(self, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
class IMediaEncodingProfileStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProfileStatics3'
    _iid_ = Guid('{90dac5aa-cf76-4294-a9ed-1a1420f51f6b}')
    @winrt_commethod(6)
    def CreateAlac(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(7)
    def CreateFlac(self, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(8)
    def CreateHevc(self, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
class IMediaEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingProperties'
    _iid_ = Guid('{b4002af6-acd4-4e5a-a24b-5d7498a8b8c4}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_commethod(7)
    def get_Type(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Subtype(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Subtype(self) -> WinRT_String: ...
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
class IMediaEncodingSubtypesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics'
    _iid_ = Guid('{37b6580e-a171-4464-ba5a-53189e48c1c8}')
    @winrt_commethod(6)
    def get_Aac(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AacAdts(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Ac3(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AmrNb(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AmrWb(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Argb32(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Asf(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Avi(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Bgra8(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Bmp(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Eac3(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Float(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Gif(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_H263(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_H264(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_H264Es(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Hevc(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_HevcEs(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_Iyuv(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_Jpeg(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_JpegXr(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_Mjpg(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_Mpeg(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_Mpeg1(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_Mpeg2(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_Mp3(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_Mpeg4(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_Nv12(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_Pcm(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_Png(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_Rgb24(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_Rgb32(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_Tiff(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_Wave(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_Wma8(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def get_Wma9(self) -> WinRT_String: ...
    @winrt_commethod(42)
    def get_Wmv3(self) -> WinRT_String: ...
    @winrt_commethod(43)
    def get_Wvc1(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def get_Yuy2(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def get_Yv12(self) -> WinRT_String: ...
    Aac = property(get_Aac, None)
    AacAdts = property(get_AacAdts, None)
    Ac3 = property(get_Ac3, None)
    AmrNb = property(get_AmrNb, None)
    AmrWb = property(get_AmrWb, None)
    Argb32 = property(get_Argb32, None)
    Asf = property(get_Asf, None)
    Avi = property(get_Avi, None)
    Bgra8 = property(get_Bgra8, None)
    Bmp = property(get_Bmp, None)
    Eac3 = property(get_Eac3, None)
    Float = property(get_Float, None)
    Gif = property(get_Gif, None)
    H263 = property(get_H263, None)
    H264 = property(get_H264, None)
    H264Es = property(get_H264Es, None)
    Hevc = property(get_Hevc, None)
    HevcEs = property(get_HevcEs, None)
    Iyuv = property(get_Iyuv, None)
    Jpeg = property(get_Jpeg, None)
    JpegXr = property(get_JpegXr, None)
    Mjpg = property(get_Mjpg, None)
    Mpeg = property(get_Mpeg, None)
    Mpeg1 = property(get_Mpeg1, None)
    Mpeg2 = property(get_Mpeg2, None)
    Mp3 = property(get_Mp3, None)
    Mpeg4 = property(get_Mpeg4, None)
    Nv12 = property(get_Nv12, None)
    Pcm = property(get_Pcm, None)
    Png = property(get_Png, None)
    Rgb24 = property(get_Rgb24, None)
    Rgb32 = property(get_Rgb32, None)
    Tiff = property(get_Tiff, None)
    Wave = property(get_Wave, None)
    Wma8 = property(get_Wma8, None)
    Wma9 = property(get_Wma9, None)
    Wmv3 = property(get_Wmv3, None)
    Wvc1 = property(get_Wvc1, None)
    Yuy2 = property(get_Yuy2, None)
    Yv12 = property(get_Yv12, None)
class IMediaEncodingSubtypesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics2'
    _iid_ = Guid('{4b7cd23d-42ff-4d33-8531-0626bee4b52d}')
    @winrt_commethod(6)
    def get_Vp9(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_L8(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_L16(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_D16(self) -> WinRT_String: ...
    Vp9 = property(get_Vp9, None)
    L8 = property(get_L8, None)
    L16 = property(get_L16, None)
    D16 = property(get_D16, None)
class IMediaEncodingSubtypesStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics3'
    _iid_ = Guid('{ba2414e4-883d-464e-a44f-097da08ef7ff}')
    @winrt_commethod(6)
    def get_Alac(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Flac(self) -> WinRT_String: ...
    Alac = property(get_Alac, None)
    Flac = property(get_Flac, None)
class IMediaEncodingSubtypesStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics4'
    _iid_ = Guid('{ddece58a-3949-4644-8a2c-59ef02c642fa}')
    @winrt_commethod(6)
    def get_P010(self) -> WinRT_String: ...
    P010 = property(get_P010, None)
class IMediaEncodingSubtypesStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics5'
    _iid_ = Guid('{5ad4a007-ffce-4760-9828-5d0c99637e6a}')
    @winrt_commethod(6)
    def get_Heif(self) -> WinRT_String: ...
    Heif = property(get_Heif, None)
class IMediaEncodingSubtypesStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics6'
    _iid_ = Guid('{a1252973-a984-5912-93bb-54e7e569e053}')
    @winrt_commethod(6)
    def get_Pgs(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Srt(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Ssa(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_VobSub(self) -> WinRT_String: ...
    Pgs = property(get_Pgs, None)
    Srt = property(get_Srt, None)
    Ssa = property(get_Ssa, None)
    VobSub = property(get_VobSub, None)
class IMediaRatio(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMediaRatio'
    _iid_ = Guid('{d2d0fee5-8929-401d-ac78-7d357e378163}')
    @winrt_commethod(6)
    def put_Numerator(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_Numerator(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_Denominator(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_Denominator(self) -> UInt32: ...
    Numerator = property(get_Numerator, put_Numerator)
    Denominator = property(get_Denominator, put_Denominator)
class IMpeg2ProfileIdsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics'
    _iid_ = Guid('{a461ff85-e57a-4128-9b21-d5331b04235c}')
    @winrt_commethod(6)
    def get_Simple(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Main(self) -> Int32: ...
    @winrt_commethod(8)
    def get_SignalNoiseRatioScalable(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SpatiallyScalable(self) -> Int32: ...
    @winrt_commethod(10)
    def get_High(self) -> Int32: ...
    Simple = property(get_Simple, None)
    Main = property(get_Main, None)
    SignalNoiseRatioScalable = property(get_SignalNoiseRatioScalable, None)
    SpatiallyScalable = property(get_SpatiallyScalable, None)
    High = property(get_High, None)
class ITimedMetadataEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.ITimedMetadataEncodingProperties'
    _iid_ = Guid('{51cd30d3-d690-4cfa-97f4-4a398e9db420}')
    @winrt_commethod(6)
    def SetFormatUserData(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def GetFormatUserData(self, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_commethod(8)
    def Copy(self) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
class ITimedMetadataEncodingPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.ITimedMetadataEncodingPropertiesStatics'
    _iid_ = Guid('{6629bb67-6e55-5643-89a0-7a7e8d85b52c}')
    @winrt_commethod(6)
    def CreatePgs(self) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_commethod(7)
    def CreateSrt(self) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_commethod(8)
    def CreateSsa(self, formatUserData: c_char_p_no) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_commethod(9)
    def CreateVobSub(self, formatUserData: c_char_p_no) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
class IVideoEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingProperties'
    _iid_ = Guid('{76ee6c9a-37c2-4f2a-880a-1282bbb4373d}')
    @winrt_commethod(6)
    def put_Bitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_Bitrate(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_Width(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_Height(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_FrameRate(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_commethod(13)
    def get_PixelAspectRatio(self) -> Windows.Media.MediaProperties.MediaRatio: ...
    Bitrate = property(get_Bitrate, put_Bitrate)
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
    FrameRate = property(get_FrameRate, None)
    PixelAspectRatio = property(get_PixelAspectRatio, None)
class IVideoEncodingProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingProperties2'
    _iid_ = Guid('{f743a1ef-d465-4290-a94b-ef0f1528f8e3}')
    @winrt_commethod(6)
    def SetFormatUserData(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def GetFormatUserData(self, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_commethod(8)
    def put_ProfileId(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_ProfileId(self) -> Int32: ...
    ProfileId = property(get_ProfileId, put_ProfileId)
class IVideoEncodingProperties3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingProperties3'
    _iid_ = Guid('{386bcdc4-873a-479f-b3eb-56c1fcbec6d7}')
    @winrt_commethod(6)
    def get_StereoscopicVideoPackingMode(self) -> Windows.Media.MediaProperties.StereoscopicVideoPackingMode: ...
    StereoscopicVideoPackingMode = property(get_StereoscopicVideoPackingMode, None)
class IVideoEncodingProperties4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingProperties4'
    _iid_ = Guid('{724ef014-c10c-40f2-9d72-3ee13b45fa8e}')
    @winrt_commethod(6)
    def get_SphericalVideoFrameFormat(self) -> Windows.Media.MediaProperties.SphericalVideoFrameFormat: ...
    SphericalVideoFrameFormat = property(get_SphericalVideoFrameFormat, None)
class IVideoEncodingProperties5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingProperties5'
    _iid_ = Guid('{4959080f-272f-4ece-a4df-c0ccdb33d840}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
class IVideoEncodingPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics'
    _iid_ = Guid('{3ce14d44-1dc5-43db-9f38-ebebf90152cb}')
    @winrt_commethod(6)
    def CreateH264(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(7)
    def CreateMpeg2(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(8)
    def CreateUncompressed(self, subtype: WinRT_String, width: UInt32, height: UInt32) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
class IVideoEncodingPropertiesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics2'
    _iid_ = Guid('{cf1ebd5d-49fe-4d00-b59a-cfa4dfc51944}')
    @winrt_commethod(6)
    def CreateHevc(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
class ImageEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IImageEncodingProperties
    _classid_ = 'Windows.Media.MediaProperties.ImageEncodingProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_mixinmethod
    def put_Width(self: Windows.Media.MediaProperties.IImageEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.MediaProperties.IImageEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Height(self: Windows.Media.MediaProperties.IImageEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.MediaProperties.IImageEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.MediaProperties.IImageEncodingProperties2) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreateHeif(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics3) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreateUncompressed(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics2, format: Windows.Media.MediaProperties.MediaPixelFormat) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreateBmp(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics2) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreateJpeg(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreatePng(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    @winrt_classmethod
    def CreateJpegXR(cls: Windows.Media.MediaProperties.IImageEncodingPropertiesStatics) -> Windows.Media.MediaProperties.ImageEncodingProperties: ...
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
class MediaEncodingProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IMediaEncodingProfile
    _classid_ = 'Windows.Media.MediaProperties.MediaEncodingProfile'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_mixinmethod
    def put_Audio(self: Windows.Media.MediaProperties.IMediaEncodingProfile, value: Windows.Media.MediaProperties.AudioEncodingProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Audio(self: Windows.Media.MediaProperties.IMediaEncodingProfile) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def put_Video(self: Windows.Media.MediaProperties.IMediaEncodingProfile, value: Windows.Media.MediaProperties.VideoEncodingProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Video(self: Windows.Media.MediaProperties.IMediaEncodingProfile) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def put_Container(self: Windows.Media.MediaProperties.IMediaEncodingProfile, value: Windows.Media.MediaProperties.ContainerEncodingProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Container(self: Windows.Media.MediaProperties.IMediaEncodingProfile) -> Windows.Media.MediaProperties.ContainerEncodingProperties: ...
    @winrt_mixinmethod
    def SetAudioTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile2, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.AudioStreamDescriptor]) -> Void: ...
    @winrt_mixinmethod
    def GetAudioTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile2) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.AudioStreamDescriptor]: ...
    @winrt_mixinmethod
    def SetVideoTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile2, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.VideoStreamDescriptor]) -> Void: ...
    @winrt_mixinmethod
    def GetVideoTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile2) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.VideoStreamDescriptor]: ...
    @winrt_mixinmethod
    def SetTimedMetadataTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile3, value: Windows.Foundation.Collections.IIterable[Windows.Media.Core.TimedMetadataStreamDescriptor]) -> Void: ...
    @winrt_mixinmethod
    def GetTimedMetadataTracks(self: Windows.Media.MediaProperties.IMediaEncodingProfile3) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedMetadataStreamDescriptor]: ...
    @winrt_classmethod
    def CreateAlac(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics3, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateFlac(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics3, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateHevc(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics3, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateWav(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics2, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateAvi(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics2, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateM4a(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateMp3(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateWma(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, quality: Windows.Media.MediaProperties.AudioEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateMp4(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateWmv(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, quality: Windows.Media.MediaProperties.VideoEncodingQuality) -> Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_classmethod
    def CreateFromFileAsync(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.MediaProperties.MediaEncodingProfile]: ...
    @winrt_classmethod
    def CreateFromStreamAsync(cls: Windows.Media.MediaProperties.IMediaEncodingProfileStatics, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Media.MediaProperties.MediaEncodingProfile]: ...
    Audio = property(get_Audio, put_Audio)
    Video = property(get_Video, put_Video)
    Container = property(get_Container, put_Container)
class MediaEncodingSubtypes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.MediaEncodingSubtypes'
    @winrt_classmethod
    def get_Pgs(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics6) -> WinRT_String: ...
    @winrt_classmethod
    def get_Srt(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics6) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ssa(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics6) -> WinRT_String: ...
    @winrt_classmethod
    def get_VobSub(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics6) -> WinRT_String: ...
    @winrt_classmethod
    def get_Heif(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics5) -> WinRT_String: ...
    @winrt_classmethod
    def get_P010(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def get_Alac(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_Flac(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_Vp9(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_L8(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_L16(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_D16(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Aac(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AacAdts(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ac3(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AmrNb(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AmrWb(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Argb32(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Asf(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Avi(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bgra8(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bmp(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Eac3(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Float(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Gif(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_H263(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_H264(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_H264Es(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hevc(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HevcEs(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Iyuv(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Jpeg(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_JpegXr(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mjpg(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mpeg(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mpeg1(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mpeg2(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mp3(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Mpeg4(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Nv12(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pcm(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Png(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rgb24(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rgb32(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Tiff(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wave(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wma8(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wma9(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wmv3(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wvc1(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Yuy2(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Yv12(cls: Windows.Media.MediaProperties.IMediaEncodingSubtypesStatics) -> WinRT_String: ...
    Pgs = property(get_Pgs, None)
    Srt = property(get_Srt, None)
    Ssa = property(get_Ssa, None)
    VobSub = property(get_VobSub, None)
    Heif = property(get_Heif, None)
    P010 = property(get_P010, None)
    Alac = property(get_Alac, None)
    Flac = property(get_Flac, None)
    Vp9 = property(get_Vp9, None)
    L8 = property(get_L8, None)
    L16 = property(get_L16, None)
    D16 = property(get_D16, None)
    Aac = property(get_Aac, None)
    AacAdts = property(get_AacAdts, None)
    Ac3 = property(get_Ac3, None)
    AmrNb = property(get_AmrNb, None)
    AmrWb = property(get_AmrWb, None)
    Argb32 = property(get_Argb32, None)
    Asf = property(get_Asf, None)
    Avi = property(get_Avi, None)
    Bgra8 = property(get_Bgra8, None)
    Bmp = property(get_Bmp, None)
    Eac3 = property(get_Eac3, None)
    Float = property(get_Float, None)
    Gif = property(get_Gif, None)
    H263 = property(get_H263, None)
    H264 = property(get_H264, None)
    H264Es = property(get_H264Es, None)
    Hevc = property(get_Hevc, None)
    HevcEs = property(get_HevcEs, None)
    Iyuv = property(get_Iyuv, None)
    Jpeg = property(get_Jpeg, None)
    JpegXr = property(get_JpegXr, None)
    Mjpg = property(get_Mjpg, None)
    Mpeg = property(get_Mpeg, None)
    Mpeg1 = property(get_Mpeg1, None)
    Mpeg2 = property(get_Mpeg2, None)
    Mp3 = property(get_Mp3, None)
    Mpeg4 = property(get_Mpeg4, None)
    Nv12 = property(get_Nv12, None)
    Pcm = property(get_Pcm, None)
    Png = property(get_Png, None)
    Rgb24 = property(get_Rgb24, None)
    Rgb32 = property(get_Rgb32, None)
    Tiff = property(get_Tiff, None)
    Wave = property(get_Wave, None)
    Wma8 = property(get_Wma8, None)
    Wma9 = property(get_Wma9, None)
    Wmv3 = property(get_Wmv3, None)
    Wvc1 = property(get_Wvc1, None)
    Yuy2 = property(get_Yuy2, None)
    Yv12 = property(get_Yv12, None)
MediaMirroringOptions = UInt32
MediaMirroringOptions_None: MediaMirroringOptions = 0
MediaMirroringOptions_Horizontal: MediaMirroringOptions = 1
MediaMirroringOptions_Vertical: MediaMirroringOptions = 2
MediaPixelFormat = Int32
MediaPixelFormat_Nv12: MediaPixelFormat = 0
MediaPixelFormat_Bgra8: MediaPixelFormat = 1
MediaPixelFormat_P010: MediaPixelFormat = 2
class MediaPropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]
    _classid_ = 'Windows.Media.MediaProperties.MediaPropertySet'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head], key: Guid) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head], key: Guid) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head], key: Guid, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head], key: Guid) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class MediaRatio(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IMediaRatio
    _classid_ = 'Windows.Media.MediaProperties.MediaRatio'
    @winrt_mixinmethod
    def put_Numerator(self: Windows.Media.MediaProperties.IMediaRatio, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Numerator(self: Windows.Media.MediaProperties.IMediaRatio) -> UInt32: ...
    @winrt_mixinmethod
    def put_Denominator(self: Windows.Media.MediaProperties.IMediaRatio, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Denominator(self: Windows.Media.MediaProperties.IMediaRatio) -> UInt32: ...
    Numerator = property(get_Numerator, put_Numerator)
    Denominator = property(get_Denominator, put_Denominator)
MediaRotation = Int32
MediaRotation_None: MediaRotation = 0
MediaRotation_Clockwise90Degrees: MediaRotation = 1
MediaRotation_Clockwise180Degrees: MediaRotation = 2
MediaRotation_Clockwise270Degrees: MediaRotation = 3
MediaThumbnailFormat = Int32
MediaThumbnailFormat_Bmp: MediaThumbnailFormat = 0
MediaThumbnailFormat_Bgra8: MediaThumbnailFormat = 1
class Mpeg2ProfileIds(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.MediaProperties.Mpeg2ProfileIds'
    @winrt_classmethod
    def get_Simple(cls: Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_Main(cls: Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_SignalNoiseRatioScalable(cls: Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_SpatiallyScalable(cls: Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics) -> Int32: ...
    @winrt_classmethod
    def get_High(cls: Windows.Media.MediaProperties.IMpeg2ProfileIdsStatics) -> Int32: ...
    Simple = property(get_Simple, None)
    Main = property(get_Main, None)
    SignalNoiseRatioScalable = property(get_SignalNoiseRatioScalable, None)
    SpatiallyScalable = property(get_SpatiallyScalable, None)
    High = property(get_High, None)
SphericalVideoFrameFormat = Int32
SphericalVideoFrameFormat_None: SphericalVideoFrameFormat = 0
SphericalVideoFrameFormat_Unsupported: SphericalVideoFrameFormat = 1
SphericalVideoFrameFormat_Equirectangular: SphericalVideoFrameFormat = 2
StereoscopicVideoPackingMode = Int32
StereoscopicVideoPackingMode_None: StereoscopicVideoPackingMode = 0
StereoscopicVideoPackingMode_SideBySide: StereoscopicVideoPackingMode = 1
StereoscopicVideoPackingMode_TopBottom: StereoscopicVideoPackingMode = 2
class TimedMetadataEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IMediaEncodingProperties
    _classid_ = 'Windows.Media.MediaProperties.TimedMetadataEncodingProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_mixinmethod
    def SetFormatUserData(self: Windows.Media.MediaProperties.ITimedMetadataEncodingProperties, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetFormatUserData(self: Windows.Media.MediaProperties.ITimedMetadataEncodingProperties, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.MediaProperties.ITimedMetadataEncodingProperties) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_classmethod
    def CreatePgs(cls: Windows.Media.MediaProperties.ITimedMetadataEncodingPropertiesStatics) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_classmethod
    def CreateSrt(cls: Windows.Media.MediaProperties.ITimedMetadataEncodingPropertiesStatics) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_classmethod
    def CreateSsa(cls: Windows.Media.MediaProperties.ITimedMetadataEncodingPropertiesStatics, formatUserData: c_char_p_no) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_classmethod
    def CreateVobSub(cls: Windows.Media.MediaProperties.ITimedMetadataEncodingPropertiesStatics, formatUserData: c_char_p_no) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
class VideoEncodingProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.MediaProperties.IVideoEncodingProperties
    _classid_ = 'Windows.Media.MediaProperties.VideoEncodingProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def put_Bitrate(self: Windows.Media.MediaProperties.IVideoEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bitrate(self: Windows.Media.MediaProperties.IVideoEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Width(self: Windows.Media.MediaProperties.IVideoEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Media.MediaProperties.IVideoEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Height(self: Windows.Media.MediaProperties.IVideoEncodingProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Media.MediaProperties.IVideoEncodingProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameRate(self: Windows.Media.MediaProperties.IVideoEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_PixelAspectRatio(self: Windows.Media.MediaProperties.IVideoEncodingProperties) -> Windows.Media.MediaProperties.MediaRatio: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> Windows.Media.MediaProperties.MediaPropertySet: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtype(self: Windows.Media.MediaProperties.IMediaEncodingProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetFormatUserData(self: Windows.Media.MediaProperties.IVideoEncodingProperties2, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetFormatUserData(self: Windows.Media.MediaProperties.IVideoEncodingProperties2, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_mixinmethod
    def put_ProfileId(self: Windows.Media.MediaProperties.IVideoEncodingProperties2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileId(self: Windows.Media.MediaProperties.IVideoEncodingProperties2) -> Int32: ...
    @winrt_mixinmethod
    def get_StereoscopicVideoPackingMode(self: Windows.Media.MediaProperties.IVideoEncodingProperties3) -> Windows.Media.MediaProperties.StereoscopicVideoPackingMode: ...
    @winrt_mixinmethod
    def get_SphericalVideoFrameFormat(self: Windows.Media.MediaProperties.IVideoEncodingProperties4) -> Windows.Media.MediaProperties.SphericalVideoFrameFormat: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.MediaProperties.IVideoEncodingProperties5) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_classmethod
    def CreateHevc(cls: Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics2) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_classmethod
    def CreateH264(cls: Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_classmethod
    def CreateMpeg2(cls: Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_classmethod
    def CreateUncompressed(cls: Windows.Media.MediaProperties.IVideoEncodingPropertiesStatics, subtype: WinRT_String, width: UInt32, height: UInt32) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    Bitrate = property(get_Bitrate, put_Bitrate)
    Width = property(get_Width, put_Width)
    Height = property(get_Height, put_Height)
    FrameRate = property(get_FrameRate, None)
    PixelAspectRatio = property(get_PixelAspectRatio, None)
    Properties = property(get_Properties, None)
    Type = property(get_Type, None)
    Subtype = property(get_Subtype, put_Subtype)
    ProfileId = property(get_ProfileId, put_ProfileId)
    StereoscopicVideoPackingMode = property(get_StereoscopicVideoPackingMode, None)
    SphericalVideoFrameFormat = property(get_SphericalVideoFrameFormat, None)
VideoEncodingQuality = Int32
VideoEncodingQuality_Auto: VideoEncodingQuality = 0
VideoEncodingQuality_HD1080p: VideoEncodingQuality = 1
VideoEncodingQuality_HD720p: VideoEncodingQuality = 2
VideoEncodingQuality_Wvga: VideoEncodingQuality = 3
VideoEncodingQuality_Ntsc: VideoEncodingQuality = 4
VideoEncodingQuality_Pal: VideoEncodingQuality = 5
VideoEncodingQuality_Vga: VideoEncodingQuality = 6
VideoEncodingQuality_Qvga: VideoEncodingQuality = 7
VideoEncodingQuality_Uhd2160p: VideoEncodingQuality = 8
VideoEncodingQuality_Uhd4320p: VideoEncodingQuality = 9
make_head(_module, 'AudioEncodingProperties')
make_head(_module, 'ContainerEncodingProperties')
make_head(_module, 'H264ProfileIds')
make_head(_module, 'IAudioEncodingProperties')
make_head(_module, 'IAudioEncodingProperties2')
make_head(_module, 'IAudioEncodingProperties3')
make_head(_module, 'IAudioEncodingPropertiesStatics')
make_head(_module, 'IAudioEncodingPropertiesStatics2')
make_head(_module, 'IAudioEncodingPropertiesWithFormatUserData')
make_head(_module, 'IContainerEncodingProperties')
make_head(_module, 'IContainerEncodingProperties2')
make_head(_module, 'IH264ProfileIdsStatics')
make_head(_module, 'IImageEncodingProperties')
make_head(_module, 'IImageEncodingProperties2')
make_head(_module, 'IImageEncodingPropertiesStatics')
make_head(_module, 'IImageEncodingPropertiesStatics2')
make_head(_module, 'IImageEncodingPropertiesStatics3')
make_head(_module, 'IMediaEncodingProfile')
make_head(_module, 'IMediaEncodingProfile2')
make_head(_module, 'IMediaEncodingProfile3')
make_head(_module, 'IMediaEncodingProfileStatics')
make_head(_module, 'IMediaEncodingProfileStatics2')
make_head(_module, 'IMediaEncodingProfileStatics3')
make_head(_module, 'IMediaEncodingProperties')
make_head(_module, 'IMediaEncodingSubtypesStatics')
make_head(_module, 'IMediaEncodingSubtypesStatics2')
make_head(_module, 'IMediaEncodingSubtypesStatics3')
make_head(_module, 'IMediaEncodingSubtypesStatics4')
make_head(_module, 'IMediaEncodingSubtypesStatics5')
make_head(_module, 'IMediaEncodingSubtypesStatics6')
make_head(_module, 'IMediaRatio')
make_head(_module, 'IMpeg2ProfileIdsStatics')
make_head(_module, 'ITimedMetadataEncodingProperties')
make_head(_module, 'ITimedMetadataEncodingPropertiesStatics')
make_head(_module, 'IVideoEncodingProperties')
make_head(_module, 'IVideoEncodingProperties2')
make_head(_module, 'IVideoEncodingProperties3')
make_head(_module, 'IVideoEncodingProperties4')
make_head(_module, 'IVideoEncodingProperties5')
make_head(_module, 'IVideoEncodingPropertiesStatics')
make_head(_module, 'IVideoEncodingPropertiesStatics2')
make_head(_module, 'ImageEncodingProperties')
make_head(_module, 'MediaEncodingProfile')
make_head(_module, 'MediaEncodingSubtypes')
make_head(_module, 'MediaPropertySet')
make_head(_module, 'MediaRatio')
make_head(_module, 'Mpeg2ProfileIds')
make_head(_module, 'TimedMetadataEncodingProperties')
make_head(_module, 'VideoEncodingProperties')
