from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
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
import win32more.Windows.Media.Core
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Transcoding
import win32more.Windows.Storage
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
    TrimStartTime = property(get_TrimStartTime, put_TrimStartTime)
    TrimStopTime = property(get_TrimStopTime, put_TrimStopTime)
    AlwaysReencode = property(get_AlwaysReencode, put_AlwaysReencode)
    HardwareAccelerationEnabled = property(get_HardwareAccelerationEnabled, put_HardwareAccelerationEnabled)
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
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Transcoding.MediaTranscoder: ...
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
    TrimStartTime = property(get_TrimStartTime, put_TrimStartTime)
    TrimStopTime = property(get_TrimStopTime, put_TrimStopTime)
    AlwaysReencode = property(get_AlwaysReencode, put_AlwaysReencode)
    HardwareAccelerationEnabled = property(get_HardwareAccelerationEnabled, put_HardwareAccelerationEnabled)
    VideoProcessingAlgorithm = property(get_VideoProcessingAlgorithm, put_VideoProcessingAlgorithm)
MediaVideoProcessingAlgorithm = Int32
MediaVideoProcessingAlgorithm_Default: MediaVideoProcessingAlgorithm = 0
MediaVideoProcessingAlgorithm_MrfCrf444: MediaVideoProcessingAlgorithm = 1
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
TranscodeFailureReason = Int32
TranscodeFailureReason_None: TranscodeFailureReason = 0
TranscodeFailureReason_Unknown: TranscodeFailureReason = 1
TranscodeFailureReason_InvalidProfile: TranscodeFailureReason = 2
TranscodeFailureReason_CodecNotFound: TranscodeFailureReason = 3
make_head(_module, 'IMediaTranscoder')
make_head(_module, 'IMediaTranscoder2')
make_head(_module, 'IPrepareTranscodeResult')
make_head(_module, 'MediaTranscoder')
make_head(_module, 'PrepareTranscodeResult')
