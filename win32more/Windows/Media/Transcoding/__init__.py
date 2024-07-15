from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Core
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Transcoding
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IMediaTranscoder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Transcoding.IMediaTranscoder'
    _iid_ = Guid('{190c99d2-a0aa-4d34-86bc-eed1b12c2f5b}')
    @winrt_commethod(6)
    def put_TrimStartTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def get_TrimStartTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_TrimStopTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_TrimStopTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def put_AlwaysReencode(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_AlwaysReencode(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_HardwareAccelerationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_HardwareAccelerationEnabled(self) -> Boolean: ...
    @winrt_commethod(14)
    def AddAudioEffect(self, activatableClassId: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def AddAudioEffectWithSettings(self, activatableClassId: WinRT_String, effectRequired: Boolean, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(16)
    def AddVideoEffect(self, activatableClassId: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def AddVideoEffectWithSettings(self, activatableClassId: WinRT_String, effectRequired: Boolean, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(18)
    def ClearEffects(self) -> Void: ...
    @winrt_commethod(19)
    def PrepareFileTranscodeAsync(self, source: win32more.Windows.Storage.IStorageFile, destination: win32more.Windows.Storage.IStorageFile, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    @winrt_commethod(20)
    def PrepareStreamTranscodeAsync(self, source: win32more.Windows.Storage.Streams.IRandomAccessStream, destination: win32more.Windows.Storage.Streams.IRandomAccessStream, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    AlwaysReencode = property(get_AlwaysReencode, put_AlwaysReencode)
    HardwareAccelerationEnabled = property(get_HardwareAccelerationEnabled, put_HardwareAccelerationEnabled)
    TrimStartTime = property(get_TrimStartTime, put_TrimStartTime)
    TrimStopTime = property(get_TrimStopTime, put_TrimStopTime)
class IMediaTranscoder2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Transcoding.IMediaTranscoder2'
    _iid_ = Guid('{40531d74-35e0-4f04-8574-ca8bc4e5a082}')
    @winrt_commethod(6)
    def PrepareMediaStreamSourceTranscodeAsync(self, source: win32more.Windows.Media.Core.IMediaSource, destination: win32more.Windows.Storage.Streams.IRandomAccessStream, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    @winrt_commethod(7)
    def put_VideoProcessingAlgorithm(self, value: win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm) -> Void: ...
    @winrt_commethod(8)
    def get_VideoProcessingAlgorithm(self) -> win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm: ...
    VideoProcessingAlgorithm = property(get_VideoProcessingAlgorithm, put_VideoProcessingAlgorithm)
class IPrepareTranscodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Transcoding.IPrepareTranscodeResult'
    _iid_ = Guid('{05f25dce-994f-4a34-9d68-97ccce1730d6}')
    @winrt_commethod(6)
    def get_CanTranscode(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_FailureReason(self) -> win32more.Windows.Media.Transcoding.TranscodeFailureReason: ...
    @winrt_commethod(8)
    def TranscodeAsync(self) -> win32more.Windows.Foundation.IAsyncActionWithProgress[Double]: ...
    CanTranscode = property(get_CanTranscode, None)
    FailureReason = property(get_FailureReason, None)
class MediaTranscoder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Transcoding.IMediaTranscoder
    _classid_ = 'Windows.Media.Transcoding.MediaTranscoder'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Transcoding.MediaTranscoder.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Transcoding.MediaTranscoder: ...
    @winrt_mixinmethod
    def put_TrimStartTime(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TrimStartTime(self: win32more.Windows.Media.Transcoding.IMediaTranscoder) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TrimStopTime(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TrimStopTime(self: win32more.Windows.Media.Transcoding.IMediaTranscoder) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AlwaysReencode(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysReencode(self: win32more.Windows.Media.Transcoding.IMediaTranscoder) -> Boolean: ...
    @winrt_mixinmethod
    def put_HardwareAccelerationEnabled(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HardwareAccelerationEnabled(self: win32more.Windows.Media.Transcoding.IMediaTranscoder) -> Boolean: ...
    @winrt_mixinmethod
    def AddAudioEffect(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, activatableClassId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddAudioEffectWithSettings(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, activatableClassId: WinRT_String, effectRequired: Boolean, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def AddVideoEffect(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, activatableClassId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddVideoEffectWithSettings(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, activatableClassId: WinRT_String, effectRequired: Boolean, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def ClearEffects(self: win32more.Windows.Media.Transcoding.IMediaTranscoder) -> Void: ...
    @winrt_mixinmethod
    def PrepareFileTranscodeAsync(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, source: win32more.Windows.Storage.IStorageFile, destination: win32more.Windows.Storage.IStorageFile, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    @winrt_mixinmethod
    def PrepareStreamTranscodeAsync(self: win32more.Windows.Media.Transcoding.IMediaTranscoder, source: win32more.Windows.Storage.Streams.IRandomAccessStream, destination: win32more.Windows.Storage.Streams.IRandomAccessStream, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    @winrt_mixinmethod
    def PrepareMediaStreamSourceTranscodeAsync(self: win32more.Windows.Media.Transcoding.IMediaTranscoder2, source: win32more.Windows.Media.Core.IMediaSource, destination: win32more.Windows.Storage.Streams.IRandomAccessStream, profile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Transcoding.PrepareTranscodeResult]: ...
    @winrt_mixinmethod
    def put_VideoProcessingAlgorithm(self: win32more.Windows.Media.Transcoding.IMediaTranscoder2, value: win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_VideoProcessingAlgorithm(self: win32more.Windows.Media.Transcoding.IMediaTranscoder2) -> win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm: ...
    AlwaysReencode = property(get_AlwaysReencode, put_AlwaysReencode)
    HardwareAccelerationEnabled = property(get_HardwareAccelerationEnabled, put_HardwareAccelerationEnabled)
    TrimStartTime = property(get_TrimStartTime, put_TrimStartTime)
    TrimStopTime = property(get_TrimStopTime, put_TrimStopTime)
    VideoProcessingAlgorithm = property(get_VideoProcessingAlgorithm, put_VideoProcessingAlgorithm)
class MediaVideoProcessingAlgorithm(Enum, Int32):
    Default = 0
    MrfCrf444 = 1
class PrepareTranscodeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Transcoding.IPrepareTranscodeResult
    _classid_ = 'Windows.Media.Transcoding.PrepareTranscodeResult'
    @winrt_mixinmethod
    def get_CanTranscode(self: win32more.Windows.Media.Transcoding.IPrepareTranscodeResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_FailureReason(self: win32more.Windows.Media.Transcoding.IPrepareTranscodeResult) -> win32more.Windows.Media.Transcoding.TranscodeFailureReason: ...
    @winrt_mixinmethod
    def TranscodeAsync(self: win32more.Windows.Media.Transcoding.IPrepareTranscodeResult) -> win32more.Windows.Foundation.IAsyncActionWithProgress[Double]: ...
    CanTranscode = property(get_CanTranscode, None)
    FailureReason = property(get_FailureReason, None)
class TranscodeFailureReason(Enum, Int32):
    None_ = 0
    Unknown = 1
    InvalidProfile = 2
    CodecNotFound = 3


make_ready(__name__)
