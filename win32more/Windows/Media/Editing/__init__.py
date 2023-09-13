from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
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
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media.Core
import win32more.Windows.Media.Editing
import win32more.Windows.Media.Effects
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Transcoding
import win32more.Windows.Storage
import win32more.Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BackgroundAudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IBackgroundAudioTrack
    _classid_ = 'Windows.Media.Editing.BackgroundAudioTrack'
    @winrt_mixinmethod
    def get_TrimTimeFromStart(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TrimTimeFromStart(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TrimTimeFromEnd(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TrimTimeFromEnd(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalDuration(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrimmedDuration(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UserData(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def put_Delay(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Volume(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Volume(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> Double: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Media.Editing.BackgroundAudioTrack: ...
    @winrt_mixinmethod
    def GetAudioEncodingProperties(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_AudioEffectDefinitions(self: win32more.Windows.Media.Editing.IBackgroundAudioTrack) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_classmethod
    def CreateFromEmbeddedAudioTrack(cls: win32more.Windows.Media.Editing.IBackgroundAudioTrackStatics, embeddedAudioTrack: win32more.Windows.Media.Editing.EmbeddedAudioTrack) -> win32more.Windows.Media.Editing.BackgroundAudioTrack: ...
    @winrt_classmethod
    def CreateFromFileAsync(cls: win32more.Windows.Media.Editing.IBackgroundAudioTrackStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.BackgroundAudioTrack]: ...
    TrimTimeFromStart = property(get_TrimTimeFromStart, put_TrimTimeFromStart)
    TrimTimeFromEnd = property(get_TrimTimeFromEnd, put_TrimTimeFromEnd)
    OriginalDuration = property(get_OriginalDuration, None)
    TrimmedDuration = property(get_TrimmedDuration, None)
    UserData = property(get_UserData, None)
    Delay = property(get_Delay, put_Delay)
    Volume = property(get_Volume, put_Volume)
    AudioEffectDefinitions = property(get_AudioEffectDefinitions, None)
class EmbeddedAudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IEmbeddedAudioTrack
    _classid_ = 'Windows.Media.Editing.EmbeddedAudioTrack'
    @winrt_mixinmethod
    def GetAudioEncodingProperties(self: win32more.Windows.Media.Editing.IEmbeddedAudioTrack) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
class IBackgroundAudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IBackgroundAudioTrack'
    _iid_ = Guid('{4b91b3bd-9e21-4266-a9c2-67dd011a2357}')
    @winrt_commethod(6)
    def get_TrimTimeFromStart(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_TrimTimeFromStart(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_TrimTimeFromEnd(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_TrimTimeFromEnd(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_TrimmedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_UserData(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(13)
    def put_Delay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_Delay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_Volume(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(17)
    def Clone(self) -> win32more.Windows.Media.Editing.BackgroundAudioTrack: ...
    @winrt_commethod(18)
    def GetAudioEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(19)
    def get_AudioEffectDefinitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    TrimTimeFromStart = property(get_TrimTimeFromStart, put_TrimTimeFromStart)
    TrimTimeFromEnd = property(get_TrimTimeFromEnd, put_TrimTimeFromEnd)
    OriginalDuration = property(get_OriginalDuration, None)
    TrimmedDuration = property(get_TrimmedDuration, None)
    UserData = property(get_UserData, None)
    Delay = property(get_Delay, put_Delay)
    Volume = property(get_Volume, put_Volume)
    AudioEffectDefinitions = property(get_AudioEffectDefinitions, None)
class IBackgroundAudioTrackStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IBackgroundAudioTrackStatics'
    _iid_ = Guid('{d9b1c0d7-d018-42a8-a559-cb4d9e97e664}')
    @winrt_commethod(6)
    def CreateFromEmbeddedAudioTrack(self, embeddedAudioTrack: win32more.Windows.Media.Editing.EmbeddedAudioTrack) -> win32more.Windows.Media.Editing.BackgroundAudioTrack: ...
    @winrt_commethod(7)
    def CreateFromFileAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.BackgroundAudioTrack]: ...
class IEmbeddedAudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IEmbeddedAudioTrack'
    _iid_ = Guid('{55ee5a7a-2d30-3fba-a190-4f1a6454f88f}')
    @winrt_commethod(6)
    def GetAudioEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
class IMediaClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaClip'
    _iid_ = Guid('{53f25366-5fba-3ea4-8693-24761811140a}')
    @winrt_commethod(6)
    def get_TrimTimeFromStart(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_TrimTimeFromStart(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_TrimTimeFromEnd(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_TrimTimeFromEnd(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_TrimmedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_UserData(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(13)
    def Clone(self) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_commethod(14)
    def get_StartTimeInComposition(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def get_EndTimeInComposition(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(16)
    def get_EmbeddedAudioTracks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Editing.EmbeddedAudioTrack]: ...
    @winrt_commethod(17)
    def get_SelectedEmbeddedAudioTrackIndex(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_SelectedEmbeddedAudioTrackIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def put_Volume(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(21)
    def GetVideoEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(22)
    def get_AudioEffectDefinitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_commethod(23)
    def get_VideoEffectDefinitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IVideoEffectDefinition]: ...
    TrimTimeFromStart = property(get_TrimTimeFromStart, put_TrimTimeFromStart)
    TrimTimeFromEnd = property(get_TrimTimeFromEnd, put_TrimTimeFromEnd)
    OriginalDuration = property(get_OriginalDuration, None)
    TrimmedDuration = property(get_TrimmedDuration, None)
    UserData = property(get_UserData, None)
    StartTimeInComposition = property(get_StartTimeInComposition, None)
    EndTimeInComposition = property(get_EndTimeInComposition, None)
    EmbeddedAudioTracks = property(get_EmbeddedAudioTracks, None)
    SelectedEmbeddedAudioTrackIndex = property(get_SelectedEmbeddedAudioTrackIndex, put_SelectedEmbeddedAudioTrackIndex)
    Volume = property(get_Volume, put_Volume)
    AudioEffectDefinitions = property(get_AudioEffectDefinitions, None)
    VideoEffectDefinitions = property(get_VideoEffectDefinitions, None)
class IMediaClipStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaClipStatics'
    _iid_ = Guid('{fa402b68-928f-43c4-bc6e-783a1a359656}')
    @winrt_commethod(6)
    def CreateFromColor(self, color: win32more.Windows.UI.Color, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_commethod(7)
    def CreateFromFileAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaClip]: ...
    @winrt_commethod(8)
    def CreateFromImageFileAsync(self, file: win32more.Windows.Storage.IStorageFile, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaClip]: ...
class IMediaClipStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaClipStatics2'
    _iid_ = Guid('{5b1dd7b3-854e-4d9b-877d-4774a556cd12}')
    @winrt_commethod(6)
    def CreateFromSurface(self, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Editing.MediaClip: ...
class IMediaComposition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaComposition'
    _iid_ = Guid('{2e06e605-dc71-41d6-b837-2d2bc14a2947}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_Clips(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaClip]: ...
    @winrt_commethod(8)
    def get_BackgroundAudioTracks(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.BackgroundAudioTrack]: ...
    @winrt_commethod(9)
    def get_UserData(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(10)
    def Clone(self) -> win32more.Windows.Media.Editing.MediaComposition: ...
    @winrt_commethod(11)
    def SaveAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def GetThumbnailAsync(self, timeFromStart: win32more.Windows.Foundation.TimeSpan, scaledWidth: Int32, scaledHeight: Int32, framePrecision: win32more.Windows.Media.Editing.VideoFramePrecision) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_commethod(13)
    def GetThumbnailsAsync(self, timesFromStart: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.TimeSpan], scaledWidth: Int32, scaledHeight: Int32, framePrecision: win32more.Windows.Media.Editing.VideoFramePrecision) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.ImageStream]]: ...
    @winrt_commethod(14)
    def RenderToFileAsync(self, destination: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_commethod(15)
    def RenderToFileWithTrimmingPreferenceAsync(self, destination: win32more.Windows.Storage.IStorageFile, trimmingPreference: win32more.Windows.Media.Editing.MediaTrimmingPreference) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_commethod(16)
    def RenderToFileWithProfileAsync(self, destination: win32more.Windows.Storage.IStorageFile, trimmingPreference: win32more.Windows.Media.Editing.MediaTrimmingPreference, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_commethod(17)
    def CreateDefaultEncodingProfile(self) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_commethod(18)
    def GenerateMediaStreamSource(self) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(19)
    def GenerateMediaStreamSourceWithProfile(self, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(20)
    def GeneratePreviewMediaStreamSource(self, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    Duration = property(get_Duration, None)
    Clips = property(get_Clips, None)
    BackgroundAudioTracks = property(get_BackgroundAudioTracks, None)
    UserData = property(get_UserData, None)
class IMediaComposition2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaComposition2'
    _iid_ = Guid('{a59e5372-2366-492c-bec8-e6dfba6d0281}')
    @winrt_commethod(6)
    def get_OverlayLayers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaOverlayLayer]: ...
    OverlayLayers = property(get_OverlayLayers, None)
class IMediaCompositionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaCompositionStatics'
    _iid_ = Guid('{87a08f04-e32a-45ce-8f66-a30df0766224}')
    @winrt_commethod(6)
    def LoadAsync(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaComposition]: ...
class IMediaOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaOverlay'
    _iid_ = Guid('{a902ae5d-7869-4830-8ab1-94dc01c05fa4}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def put_Delay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_Delay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(11)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def Clone(self) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    @winrt_commethod(13)
    def get_Clip(self) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_commethod(14)
    def get_AudioEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AudioEnabled(self, value: Boolean) -> Void: ...
    Position = property(get_Position, put_Position)
    Delay = property(get_Delay, put_Delay)
    Opacity = property(get_Opacity, put_Opacity)
    Clip = property(get_Clip, None)
    AudioEnabled = property(get_AudioEnabled, put_AudioEnabled)
class IMediaOverlayFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaOverlayFactory'
    _iid_ = Guid('{b584828a-6188-4f8f-a2e0-aa552d598e18}')
    @winrt_commethod(6)
    def Create(self, clip: win32more.Windows.Media.Editing.MediaClip) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    @winrt_commethod(7)
    def CreateWithPositionAndOpacity(self, clip: win32more.Windows.Media.Editing.MediaClip, position: win32more.Windows.Foundation.Rect, opacity: Double) -> win32more.Windows.Media.Editing.MediaOverlay: ...
class IMediaOverlayLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaOverlayLayer'
    _iid_ = Guid('{a6d9ba57-eeda-46c6-bbe5-e398c84168ac}')
    @winrt_commethod(6)
    def Clone(self) -> win32more.Windows.Media.Editing.MediaOverlayLayer: ...
    @winrt_commethod(7)
    def get_Overlays(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaOverlay]: ...
    @winrt_commethod(8)
    def get_CustomCompositorDefinition(self) -> win32more.Windows.Media.Effects.IVideoCompositorDefinition: ...
    Overlays = property(get_Overlays, None)
    CustomCompositorDefinition = property(get_CustomCompositorDefinition, None)
class IMediaOverlayLayerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Editing.IMediaOverlayLayerFactory'
    _iid_ = Guid('{947cb473-a39e-4362-abbf-9f8b5070a062}')
    @winrt_commethod(6)
    def CreateWithCompositorDefinition(self, compositorDefinition: win32more.Windows.Media.Effects.IVideoCompositorDefinition) -> win32more.Windows.Media.Editing.MediaOverlayLayer: ...
class MediaClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IMediaClip
    _classid_ = 'Windows.Media.Editing.MediaClip'
    @winrt_mixinmethod
    def get_TrimTimeFromStart(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TrimTimeFromStart(self: win32more.Windows.Media.Editing.IMediaClip, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_TrimTimeFromEnd(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TrimTimeFromEnd(self: win32more.Windows.Media.Editing.IMediaClip, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalDuration(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrimmedDuration(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UserData(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_mixinmethod
    def get_StartTimeInComposition(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_EndTimeInComposition(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_EmbeddedAudioTracks(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Editing.EmbeddedAudioTrack]: ...
    @winrt_mixinmethod
    def get_SelectedEmbeddedAudioTrackIndex(self: win32more.Windows.Media.Editing.IMediaClip) -> UInt32: ...
    @winrt_mixinmethod
    def put_SelectedEmbeddedAudioTrackIndex(self: win32more.Windows.Media.Editing.IMediaClip, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def put_Volume(self: win32more.Windows.Media.Editing.IMediaClip, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Volume(self: win32more.Windows.Media.Editing.IMediaClip) -> Double: ...
    @winrt_mixinmethod
    def GetVideoEncodingProperties(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_AudioEffectDefinitions(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IAudioEffectDefinition]: ...
    @winrt_mixinmethod
    def get_VideoEffectDefinitions(self: win32more.Windows.Media.Editing.IMediaClip) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Effects.IVideoEffectDefinition]: ...
    @winrt_classmethod
    def CreateFromSurface(cls: win32more.Windows.Media.Editing.IMediaClipStatics2, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_classmethod
    def CreateFromColor(cls: win32more.Windows.Media.Editing.IMediaClipStatics, color: win32more.Windows.UI.Color, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_classmethod
    def CreateFromFileAsync(cls: win32more.Windows.Media.Editing.IMediaClipStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaClip]: ...
    @winrt_classmethod
    def CreateFromImageFileAsync(cls: win32more.Windows.Media.Editing.IMediaClipStatics, file: win32more.Windows.Storage.IStorageFile, originalDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaClip]: ...
    TrimTimeFromStart = property(get_TrimTimeFromStart, put_TrimTimeFromStart)
    TrimTimeFromEnd = property(get_TrimTimeFromEnd, put_TrimTimeFromEnd)
    OriginalDuration = property(get_OriginalDuration, None)
    TrimmedDuration = property(get_TrimmedDuration, None)
    UserData = property(get_UserData, None)
    StartTimeInComposition = property(get_StartTimeInComposition, None)
    EndTimeInComposition = property(get_EndTimeInComposition, None)
    EmbeddedAudioTracks = property(get_EmbeddedAudioTracks, None)
    SelectedEmbeddedAudioTrackIndex = property(get_SelectedEmbeddedAudioTrackIndex, put_SelectedEmbeddedAudioTrackIndex)
    Volume = property(get_Volume, put_Volume)
    AudioEffectDefinitions = property(get_AudioEffectDefinitions, None)
    VideoEffectDefinitions = property(get_VideoEffectDefinitions, None)
class MediaComposition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IMediaComposition
    _classid_ = 'Windows.Media.Editing.MediaComposition'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Editing.MediaComposition: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Clips(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaClip]: ...
    @winrt_mixinmethod
    def get_BackgroundAudioTracks(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.BackgroundAudioTrack]: ...
    @winrt_mixinmethod
    def get_UserData(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Media.Editing.MediaComposition: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Media.Editing.IMediaComposition, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Media.Editing.IMediaComposition, timeFromStart: win32more.Windows.Foundation.TimeSpan, scaledWidth: Int32, scaledHeight: Int32, framePrecision: win32more.Windows.Media.Editing.VideoFramePrecision) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Imaging.ImageStream]: ...
    @winrt_mixinmethod
    def GetThumbnailsAsync(self: win32more.Windows.Media.Editing.IMediaComposition, timesFromStart: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.TimeSpan], scaledWidth: Int32, scaledHeight: Int32, framePrecision: win32more.Windows.Media.Editing.VideoFramePrecision) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.ImageStream]]: ...
    @winrt_mixinmethod
    def RenderToFileAsync(self: win32more.Windows.Media.Editing.IMediaComposition, destination: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_mixinmethod
    def RenderToFileWithTrimmingPreferenceAsync(self: win32more.Windows.Media.Editing.IMediaComposition, destination: win32more.Windows.Storage.IStorageFile, trimmingPreference: win32more.Windows.Media.Editing.MediaTrimmingPreference) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_mixinmethod
    def RenderToFileWithProfileAsync(self: win32more.Windows.Media.Editing.IMediaComposition, destination: win32more.Windows.Storage.IStorageFile, trimmingPreference: win32more.Windows.Media.Editing.MediaTrimmingPreference, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Transcoding.TranscodeFailureReason, Double]: ...
    @winrt_mixinmethod
    def CreateDefaultEncodingProfile(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Media.MediaProperties.MediaEncodingProfile: ...
    @winrt_mixinmethod
    def GenerateMediaStreamSource(self: win32more.Windows.Media.Editing.IMediaComposition) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def GenerateMediaStreamSourceWithProfile(self: win32more.Windows.Media.Editing.IMediaComposition, encodingProfile: win32more.Windows.Media.MediaProperties.MediaEncodingProfile) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def GeneratePreviewMediaStreamSource(self: win32more.Windows.Media.Editing.IMediaComposition, scaledWidth: Int32, scaledHeight: Int32) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def get_OverlayLayers(self: win32more.Windows.Media.Editing.IMediaComposition2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaOverlayLayer]: ...
    @winrt_classmethod
    def LoadAsync(cls: win32more.Windows.Media.Editing.IMediaCompositionStatics, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Editing.MediaComposition]: ...
    Duration = property(get_Duration, None)
    Clips = property(get_Clips, None)
    BackgroundAudioTracks = property(get_BackgroundAudioTracks, None)
    UserData = property(get_UserData, None)
    OverlayLayers = property(get_OverlayLayers, None)
class MediaOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IMediaOverlay
    _classid_ = 'Windows.Media.Editing.MediaOverlay'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Editing.IMediaOverlayFactory, clip: win32more.Windows.Media.Editing.MediaClip) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    @winrt_factorymethod
    def CreateWithPositionAndOpacity(cls: win32more.Windows.Media.Editing.IMediaOverlayFactory, clip: win32more.Windows.Media.Editing.MediaClip, position: win32more.Windows.Foundation.Rect, opacity: Double) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Editing.IMediaOverlay) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Editing.IMediaOverlay, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def put_Delay(self: win32more.Windows.Media.Editing.IMediaOverlay, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.Media.Editing.IMediaOverlay) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.Media.Editing.IMediaOverlay) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.Media.Editing.IMediaOverlay, value: Double) -> Void: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Media.Editing.IMediaOverlay) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    @winrt_mixinmethod
    def get_Clip(self: win32more.Windows.Media.Editing.IMediaOverlay) -> win32more.Windows.Media.Editing.MediaClip: ...
    @winrt_mixinmethod
    def get_AudioEnabled(self: win32more.Windows.Media.Editing.IMediaOverlay) -> Boolean: ...
    @winrt_mixinmethod
    def put_AudioEnabled(self: win32more.Windows.Media.Editing.IMediaOverlay, value: Boolean) -> Void: ...
    Position = property(get_Position, put_Position)
    Delay = property(get_Delay, put_Delay)
    Opacity = property(get_Opacity, put_Opacity)
    Clip = property(get_Clip, None)
    AudioEnabled = property(get_AudioEnabled, put_AudioEnabled)
class MediaOverlayLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Editing.IMediaOverlayLayer
    _classid_ = 'Windows.Media.Editing.MediaOverlayLayer'
    @winrt_factorymethod
    def CreateWithCompositorDefinition(cls: win32more.Windows.Media.Editing.IMediaOverlayLayerFactory, compositorDefinition: win32more.Windows.Media.Effects.IVideoCompositorDefinition) -> win32more.Windows.Media.Editing.MediaOverlayLayer: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Editing.MediaOverlayLayer: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Media.Editing.IMediaOverlayLayer) -> win32more.Windows.Media.Editing.MediaOverlayLayer: ...
    @winrt_mixinmethod
    def get_Overlays(self: win32more.Windows.Media.Editing.IMediaOverlayLayer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Editing.MediaOverlay]: ...
    @winrt_mixinmethod
    def get_CustomCompositorDefinition(self: win32more.Windows.Media.Editing.IMediaOverlayLayer) -> win32more.Windows.Media.Effects.IVideoCompositorDefinition: ...
    Overlays = property(get_Overlays, None)
    CustomCompositorDefinition = property(get_CustomCompositorDefinition, None)
MediaTrimmingPreference = Int32
MediaTrimmingPreference_Fast: MediaTrimmingPreference = 0
MediaTrimmingPreference_Precise: MediaTrimmingPreference = 1
VideoFramePrecision = Int32
VideoFramePrecision_NearestFrame: VideoFramePrecision = 0
VideoFramePrecision_NearestKeyFrame: VideoFramePrecision = 1
make_head(_module, 'BackgroundAudioTrack')
make_head(_module, 'EmbeddedAudioTrack')
make_head(_module, 'IBackgroundAudioTrack')
make_head(_module, 'IBackgroundAudioTrackStatics')
make_head(_module, 'IEmbeddedAudioTrack')
make_head(_module, 'IMediaClip')
make_head(_module, 'IMediaClipStatics')
make_head(_module, 'IMediaClipStatics2')
make_head(_module, 'IMediaComposition')
make_head(_module, 'IMediaComposition2')
make_head(_module, 'IMediaCompositionStatics')
make_head(_module, 'IMediaOverlay')
make_head(_module, 'IMediaOverlayFactory')
make_head(_module, 'IMediaOverlayLayer')
make_head(_module, 'IMediaOverlayLayerFactory')
make_head(_module, 'MediaClip')
make_head(_module, 'MediaComposition')
make_head(_module, 'MediaOverlay')
make_head(_module, 'MediaOverlayLayer')
