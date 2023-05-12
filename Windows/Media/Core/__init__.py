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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.AppService
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Imaging
import Windows.Media
import Windows.Media.Capture
import Windows.Media.Capture.Frames
import Windows.Media.Core
import Windows.Media.Devices
import Windows.Media.Devices.Core
import Windows.Media.Effects
import Windows.Media.FaceAnalysis
import Windows.Media.MediaProperties
import Windows.Media.Playback
import Windows.Media.Protection
import Windows.Media.Streaming.Adaptive
import Windows.Networking.BackgroundTransfer
import Windows.Storage
import Windows.Storage.FileProperties
import Windows.Storage.Streams
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AudioDecoderDegradation = Int32
AudioDecoderDegradation_None: AudioDecoderDegradation = 0
AudioDecoderDegradation_DownmixTo2Channels: AudioDecoderDegradation = 1
AudioDecoderDegradation_DownmixTo6Channels: AudioDecoderDegradation = 2
AudioDecoderDegradation_DownmixTo8Channels: AudioDecoderDegradation = 3
AudioDecoderDegradationReason = Int32
AudioDecoderDegradationReason_None: AudioDecoderDegradationReason = 0
AudioDecoderDegradationReason_LicensingRequirement: AudioDecoderDegradationReason = 1
AudioDecoderDegradationReason_SpatialAudioNotSupported: AudioDecoderDegradationReason = 2
class AudioStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IAudioStreamDescriptor
    _classid_ = 'Windows.Media.Core.AudioStreamDescriptor'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Core.IAudioStreamDescriptorFactory, encodingProperties: Windows.Media.MediaProperties.AudioEncodingProperties) -> Windows.Media.Core.AudioStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: Windows.Media.Core.IAudioStreamDescriptor) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LeadingEncoderPadding(self: Windows.Media.Core.IAudioStreamDescriptor2, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_LeadingEncoderPadding(self: Windows.Media.Core.IAudioStreamDescriptor2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_TrailingEncoderPadding(self: Windows.Media.Core.IAudioStreamDescriptor2, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_TrailingEncoderPadding(self: Windows.Media.Core.IAudioStreamDescriptor2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.Core.IAudioStreamDescriptor3) -> Windows.Media.Core.AudioStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
    IsSelected = property(get_IsSelected, None)
    Name = property(get_Name, put_Name)
    Language = property(get_Language, put_Language)
    LeadingEncoderPadding = property(get_LeadingEncoderPadding, put_LeadingEncoderPadding)
    TrailingEncoderPadding = property(get_TrailingEncoderPadding, put_TrailingEncoderPadding)
    Label = property(get_Label, put_Label)
class AudioTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaTrack
    _classid_ = 'Windows.Media.Core.AudioTrack'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: Windows.Media.Core.IMediaTrack) -> Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: Windows.Media.Core.IAudioTrack, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.AudioTrack, Windows.Media.Core.AudioTrackOpenFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: Windows.Media.Core.IAudioTrack, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetEncodingProperties(self: Windows.Media.Core.IAudioTrack) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: Windows.Media.Core.IAudioTrack) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.IAudioTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportInfo(self: Windows.Media.Core.IAudioTrack) -> Windows.Media.Core.AudioTrackSupportInfo: ...
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    TrackKind = property(get_TrackKind, None)
    Label = property(get_Label, put_Label)
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
    SupportInfo = property(get_SupportInfo, None)
class AudioTrackOpenFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IAudioTrackOpenFailedEventArgs
    _classid_ = 'Windows.Media.Core.AudioTrackOpenFailedEventArgs'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Core.IAudioTrackOpenFailedEventArgs) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class AudioTrackSupportInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IAudioTrackSupportInfo
    _classid_ = 'Windows.Media.Core.AudioTrackSupportInfo'
    @winrt_mixinmethod
    def get_DecoderStatus(self: Windows.Media.Core.IAudioTrackSupportInfo) -> Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_mixinmethod
    def get_Degradation(self: Windows.Media.Core.IAudioTrackSupportInfo) -> Windows.Media.Core.AudioDecoderDegradation: ...
    @winrt_mixinmethod
    def get_DegradationReason(self: Windows.Media.Core.IAudioTrackSupportInfo) -> Windows.Media.Core.AudioDecoderDegradationReason: ...
    @winrt_mixinmethod
    def get_MediaSourceStatus(self: Windows.Media.Core.IAudioTrackSupportInfo) -> Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    Degradation = property(get_Degradation, None)
    DegradationReason = property(get_DegradationReason, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class ChapterCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IChapterCue
    _classid_ = 'Windows.Media.Core.ChapterCue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.ChapterCue: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Media.Core.IChapterCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Media.Core.IChapterCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StartTime(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Title = property(get_Title, put_Title)
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
CodecCategory = Int32
CodecCategory_Encoder: CodecCategory = 0
CodecCategory_Decoder: CodecCategory = 1
class CodecInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ICodecInfo
    _classid_ = 'Windows.Media.Core.CodecInfo'
    @winrt_mixinmethod
    def get_Kind(self: Windows.Media.Core.ICodecInfo) -> Windows.Media.Core.CodecKind: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Media.Core.ICodecInfo) -> Windows.Media.Core.CodecCategory: ...
    @winrt_mixinmethod
    def get_Subtypes(self: Windows.Media.Core.ICodecInfo) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Media.Core.ICodecInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsTrusted(self: Windows.Media.Core.ICodecInfo) -> Boolean: ...
    Kind = property(get_Kind, None)
    Category = property(get_Category, None)
    Subtypes = property(get_Subtypes, None)
    DisplayName = property(get_DisplayName, None)
    IsTrusted = property(get_IsTrusted, None)
CodecKind = Int32
CodecKind_Audio: CodecKind = 0
CodecKind_Video: CodecKind = 1
class CodecQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ICodecQuery
    _classid_ = 'Windows.Media.Core.CodecQuery'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.CodecQuery: ...
    @winrt_mixinmethod
    def FindAllAsync(self: Windows.Media.Core.ICodecQuery, kind: Windows.Media.Core.CodecKind, category: Windows.Media.Core.CodecCategory, subType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Core.CodecInfo]]: ...
class _CodecSubtypes_Meta_(ComPtr.__class__):
    pass
class CodecSubtypes(ComPtr, metaclass=_CodecSubtypes_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.CodecSubtypes'
    @winrt_classmethod
    def get_VideoFormatDV25(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDV50(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvc(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvh1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvhD(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvsd(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvsl(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH263(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH264(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH265(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH264ES(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatHevc(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatHevcES(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatM4S2(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMjpg(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP43(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP4S(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP4V(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMpeg2(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatVP80(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatVP90(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMpg1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMss1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMss2(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv2(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv3(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWvc1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormat420O(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAac(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAdts(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAlac(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrNB(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrWB(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrWP(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyAC3(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyAC3Spdif(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyDDPlus(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDrm(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDts(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatFlac(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatFloat(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMP3(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMPeg(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMsp1(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatOpus(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatPcm(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWmaSpdif(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioLossless(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioV8(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioV9(cls: Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    _CodecSubtypes_Meta_.VideoFormatDV25 = property(get_VideoFormatDV25.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDV50 = property(get_VideoFormatDV50.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDvc = property(get_VideoFormatDvc.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDvh1 = property(get_VideoFormatDvh1.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDvhD = property(get_VideoFormatDvhD.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDvsd = property(get_VideoFormatDvsd.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatDvsl = property(get_VideoFormatDvsl.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatH263 = property(get_VideoFormatH263.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatH264 = property(get_VideoFormatH264.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatH265 = property(get_VideoFormatH265.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatH264ES = property(get_VideoFormatH264ES.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatHevc = property(get_VideoFormatHevc.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatHevcES = property(get_VideoFormatHevcES.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatM4S2 = property(get_VideoFormatM4S2.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMjpg = property(get_VideoFormatMjpg.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMP43 = property(get_VideoFormatMP43.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMP4S = property(get_VideoFormatMP4S.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMP4V = property(get_VideoFormatMP4V.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMpeg2 = property(get_VideoFormatMpeg2.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatVP80 = property(get_VideoFormatVP80.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatVP90 = property(get_VideoFormatVP90.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMpg1 = property(get_VideoFormatMpg1.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMss1 = property(get_VideoFormatMss1.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatMss2 = property(get_VideoFormatMss2.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatWmv1 = property(get_VideoFormatWmv1.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatWmv2 = property(get_VideoFormatWmv2.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatWmv3 = property(get_VideoFormatWmv3.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormatWvc1 = property(get_VideoFormatWvc1.__wrapped__, None)
    _CodecSubtypes_Meta_.VideoFormat420O = property(get_VideoFormat420O.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAac = property(get_AudioFormatAac.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAdts = property(get_AudioFormatAdts.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAlac = property(get_AudioFormatAlac.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAmrNB = property(get_AudioFormatAmrNB.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAmrWB = property(get_AudioFormatAmrWB.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatAmrWP = property(get_AudioFormatAmrWP.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyAC3 = property(get_AudioFormatDolbyAC3.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyAC3Spdif = property(get_AudioFormatDolbyAC3Spdif.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyDDPlus = property(get_AudioFormatDolbyDDPlus.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatDrm = property(get_AudioFormatDrm.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatDts = property(get_AudioFormatDts.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatFlac = property(get_AudioFormatFlac.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatFloat = property(get_AudioFormatFloat.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatMP3 = property(get_AudioFormatMP3.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatMPeg = property(get_AudioFormatMPeg.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatMsp1 = property(get_AudioFormatMsp1.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatOpus = property(get_AudioFormatOpus.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatPcm = property(get_AudioFormatPcm.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatWmaSpdif = property(get_AudioFormatWmaSpdif.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioLossless = property(get_AudioFormatWMAudioLossless.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioV8 = property(get_AudioFormatWMAudioV8.__wrapped__, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioV9 = property(get_AudioFormatWMAudioV9.__wrapped__, None)
class DataCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IDataCue
    _classid_ = 'Windows.Media.Core.DataCue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.DataCue: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Media.Core.IDataCue, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Media.Core.IDataCue) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_StartTime(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Core.IDataCue2) -> Windows.Foundation.Collections.PropertySet: ...
    Data = property(get_Data, put_Data)
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
    Properties = property(get_Properties, None)
class FaceDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IFaceDetectedEventArgs
    _classid_ = 'Windows.Media.Core.FaceDetectedEventArgs'
    @winrt_mixinmethod
    def get_ResultFrame(self: Windows.Media.Core.IFaceDetectedEventArgs) -> Windows.Media.Core.FaceDetectionEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class FaceDetectionEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IFaceDetectionEffect
    _classid_ = 'Windows.Media.Core.FaceDetectionEffect'
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Core.IFaceDetectionEffect, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Core.IFaceDetectionEffect) -> Boolean: ...
    @winrt_mixinmethod
    def put_DesiredDetectionInterval(self: Windows.Media.Core.IFaceDetectionEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredDetectionInterval(self: Windows.Media.Core.IFaceDetectionEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_FaceDetected(self: Windows.Media.Core.IFaceDetectionEffect, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.FaceDetectionEffect, Windows.Media.Core.FaceDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FaceDetected(self: Windows.Media.Core.IFaceDetectionEffect, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetProperties(self: Windows.Media.IMediaExtension, configuration: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    DesiredDetectionInterval = property(get_DesiredDetectionInterval, put_DesiredDetectionInterval)
class FaceDetectionEffectDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.FaceDetectionEffectDefinition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.FaceDetectionEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Effects.IVideoEffectDefinition) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def put_DetectionMode(self: Windows.Media.Core.IFaceDetectionEffectDefinition, value: Windows.Media.Core.FaceDetectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_DetectionMode(self: Windows.Media.Core.IFaceDetectionEffectDefinition) -> Windows.Media.Core.FaceDetectionMode: ...
    @winrt_mixinmethod
    def put_SynchronousDetectionEnabled(self: Windows.Media.Core.IFaceDetectionEffectDefinition, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SynchronousDetectionEnabled(self: Windows.Media.Core.IFaceDetectionEffectDefinition) -> Boolean: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
    DetectionMode = property(get_DetectionMode, put_DetectionMode)
    SynchronousDetectionEnabled = property(get_SynchronousDetectionEnabled, put_SynchronousDetectionEnabled)
class FaceDetectionEffectFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IFaceDetectionEffectFrame
    _classid_ = 'Windows.Media.Core.FaceDetectionEffectFrame'
    @winrt_mixinmethod
    def get_DetectedFaces(self: Windows.Media.Core.IFaceDetectionEffectFrame) -> Windows.Foundation.Collections.IVectorView[Windows.Media.FaceAnalysis.DetectedFace]: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.IMediaFrame) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SystemRelativeTime(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_IsDiscontinuous(self: Windows.Media.IMediaFrame, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscontinuous(self: Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: Windows.Media.IMediaFrame) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DetectedFaces = property(get_DetectedFaces, None)
    Type = property(get_Type, None)
    IsReadOnly = property(get_IsReadOnly, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    SystemRelativeTime = property(get_SystemRelativeTime, put_SystemRelativeTime)
    Duration = property(get_Duration, put_Duration)
    IsDiscontinuous = property(get_IsDiscontinuous, put_IsDiscontinuous)
    ExtendedProperties = property(get_ExtendedProperties, None)
FaceDetectionMode = Int32
FaceDetectionMode_HighPerformance: FaceDetectionMode = 0
FaceDetectionMode_Balanced: FaceDetectionMode = 1
FaceDetectionMode_HighQuality: FaceDetectionMode = 2
class HighDynamicRangeControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IHighDynamicRangeControl
    _classid_ = 'Windows.Media.Core.HighDynamicRangeControl'
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Core.IHighDynamicRangeControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Core.IHighDynamicRangeControl) -> Boolean: ...
    Enabled = property(get_Enabled, put_Enabled)
class HighDynamicRangeOutput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IHighDynamicRangeOutput
    _classid_ = 'Windows.Media.Core.HighDynamicRangeOutput'
    @winrt_mixinmethod
    def get_Certainty(self: Windows.Media.Core.IHighDynamicRangeOutput) -> Double: ...
    @winrt_mixinmethod
    def get_FrameControllers(self: Windows.Media.Core.IHighDynamicRangeOutput) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.Core.FrameController]: ...
    Certainty = property(get_Certainty, None)
    FrameControllers = property(get_FrameControllers, None)
class IAudioStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor'
    _iid_ = Guid('{1e3692e4-4027-4847-a70b-df1d9a2a7b04}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    EncodingProperties = property(get_EncodingProperties, None)
class IAudioStreamDescriptor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor2'
    _iid_ = Guid('{2e68f1f6-a448-497b-8840-85082665acf9}')
    @winrt_commethod(6)
    def put_LeadingEncoderPadding(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(7)
    def get_LeadingEncoderPadding(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def put_TrailingEncoderPadding(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(9)
    def get_TrailingEncoderPadding(self) -> Windows.Foundation.IReference[UInt32]: ...
    LeadingEncoderPadding = property(get_LeadingEncoderPadding, put_LeadingEncoderPadding)
    TrailingEncoderPadding = property(get_TrailingEncoderPadding, put_TrailingEncoderPadding)
class IAudioStreamDescriptor3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor3'
    _iid_ = Guid('{4d220da1-8e83-44ef-8973-2f63e993f36b}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.Core.AudioStreamDescriptor: ...
class IAudioStreamDescriptorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptorFactory'
    _iid_ = Guid('{4a86ce9e-4cb1-4380-8e0c-83504b7f5bf3}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: Windows.Media.MediaProperties.AudioEncodingProperties) -> Windows.Media.Core.AudioStreamDescriptor: ...
class IAudioTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrack'
    _iid_ = Guid('{f23b6e77-3ef7-40de-b943-068b1321701d}')
    @winrt_commethod(6)
    def add_OpenFailed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.AudioTrack, Windows.Media.Core.AudioTrackOpenFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetEncodingProperties(self) -> Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(9)
    def get_PlaybackItem(self) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SupportInfo(self) -> Windows.Media.Core.AudioTrackSupportInfo: ...
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
    SupportInfo = property(get_SupportInfo, None)
class IAudioTrackOpenFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrackOpenFailedEventArgs'
    _iid_ = Guid('{eeddb9b9-bb7c-4112-bf76-9384676f824b}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAudioTrackSupportInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrackSupportInfo'
    _iid_ = Guid('{178beff7-cc39-44a6-b951-4a5653f073fa}')
    @winrt_commethod(6)
    def get_DecoderStatus(self) -> Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_commethod(7)
    def get_Degradation(self) -> Windows.Media.Core.AudioDecoderDegradation: ...
    @winrt_commethod(8)
    def get_DegradationReason(self) -> Windows.Media.Core.AudioDecoderDegradationReason: ...
    @winrt_commethod(9)
    def get_MediaSourceStatus(self) -> Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    Degradation = property(get_Degradation, None)
    DegradationReason = property(get_DegradationReason, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class IChapterCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IChapterCue'
    _iid_ = Guid('{72a98001-d38a-4c0a-8fa6-75cddaf4664c}')
    @winrt_commethod(6)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    Title = property(get_Title, put_Title)
class ICodecInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ICodecInfo'
    _iid_ = Guid('{51e89f85-ea97-499c-86ac-4ce5e73f3a42}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Media.Core.CodecKind: ...
    @winrt_commethod(7)
    def get_Category(self) -> Windows.Media.Core.CodecCategory: ...
    @winrt_commethod(8)
    def get_Subtypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_IsTrusted(self) -> Boolean: ...
    Kind = property(get_Kind, None)
    Category = property(get_Category, None)
    Subtypes = property(get_Subtypes, None)
    DisplayName = property(get_DisplayName, None)
    IsTrusted = property(get_IsTrusted, None)
class ICodecQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ICodecQuery'
    _iid_ = Guid('{222a953a-af61-4e04-808a-a4634e2f3ac4}')
    @winrt_commethod(6)
    def FindAllAsync(self, kind: Windows.Media.Core.CodecKind, category: Windows.Media.Core.CodecCategory, subType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Core.CodecInfo]]: ...
class ICodecSubtypesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ICodecSubtypesStatics'
    _iid_ = Guid('{a66ac4f2-888b-4224-8cf6-2a8d4eb02382}')
    @winrt_commethod(6)
    def get_VideoFormatDV25(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoFormatDV50(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_VideoFormatDvc(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_VideoFormatDvh1(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_VideoFormatDvhD(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_VideoFormatDvsd(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_VideoFormatDvsl(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_VideoFormatH263(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_VideoFormatH264(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_VideoFormatH265(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_VideoFormatH264ES(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_VideoFormatHevc(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_VideoFormatHevcES(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_VideoFormatM4S2(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_VideoFormatMjpg(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_VideoFormatMP43(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_VideoFormatMP4S(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_VideoFormatMP4V(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_VideoFormatMpeg2(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_VideoFormatVP80(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_VideoFormatVP90(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_VideoFormatMpg1(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_VideoFormatMss1(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_VideoFormatMss2(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_VideoFormatWmv1(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_VideoFormatWmv2(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_VideoFormatWmv3(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_VideoFormatWvc1(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_VideoFormat420O(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_AudioFormatAac(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_AudioFormatAdts(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_AudioFormatAlac(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_AudioFormatAmrNB(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_AudioFormatAmrWB(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_AudioFormatAmrWP(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def get_AudioFormatDolbyAC3(self) -> WinRT_String: ...
    @winrt_commethod(42)
    def get_AudioFormatDolbyAC3Spdif(self) -> WinRT_String: ...
    @winrt_commethod(43)
    def get_AudioFormatDolbyDDPlus(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def get_AudioFormatDrm(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def get_AudioFormatDts(self) -> WinRT_String: ...
    @winrt_commethod(46)
    def get_AudioFormatFlac(self) -> WinRT_String: ...
    @winrt_commethod(47)
    def get_AudioFormatFloat(self) -> WinRT_String: ...
    @winrt_commethod(48)
    def get_AudioFormatMP3(self) -> WinRT_String: ...
    @winrt_commethod(49)
    def get_AudioFormatMPeg(self) -> WinRT_String: ...
    @winrt_commethod(50)
    def get_AudioFormatMsp1(self) -> WinRT_String: ...
    @winrt_commethod(51)
    def get_AudioFormatOpus(self) -> WinRT_String: ...
    @winrt_commethod(52)
    def get_AudioFormatPcm(self) -> WinRT_String: ...
    @winrt_commethod(53)
    def get_AudioFormatWmaSpdif(self) -> WinRT_String: ...
    @winrt_commethod(54)
    def get_AudioFormatWMAudioLossless(self) -> WinRT_String: ...
    @winrt_commethod(55)
    def get_AudioFormatWMAudioV8(self) -> WinRT_String: ...
    @winrt_commethod(56)
    def get_AudioFormatWMAudioV9(self) -> WinRT_String: ...
    VideoFormatDV25 = property(get_VideoFormatDV25, None)
    VideoFormatDV50 = property(get_VideoFormatDV50, None)
    VideoFormatDvc = property(get_VideoFormatDvc, None)
    VideoFormatDvh1 = property(get_VideoFormatDvh1, None)
    VideoFormatDvhD = property(get_VideoFormatDvhD, None)
    VideoFormatDvsd = property(get_VideoFormatDvsd, None)
    VideoFormatDvsl = property(get_VideoFormatDvsl, None)
    VideoFormatH263 = property(get_VideoFormatH263, None)
    VideoFormatH264 = property(get_VideoFormatH264, None)
    VideoFormatH265 = property(get_VideoFormatH265, None)
    VideoFormatH264ES = property(get_VideoFormatH264ES, None)
    VideoFormatHevc = property(get_VideoFormatHevc, None)
    VideoFormatHevcES = property(get_VideoFormatHevcES, None)
    VideoFormatM4S2 = property(get_VideoFormatM4S2, None)
    VideoFormatMjpg = property(get_VideoFormatMjpg, None)
    VideoFormatMP43 = property(get_VideoFormatMP43, None)
    VideoFormatMP4S = property(get_VideoFormatMP4S, None)
    VideoFormatMP4V = property(get_VideoFormatMP4V, None)
    VideoFormatMpeg2 = property(get_VideoFormatMpeg2, None)
    VideoFormatVP80 = property(get_VideoFormatVP80, None)
    VideoFormatVP90 = property(get_VideoFormatVP90, None)
    VideoFormatMpg1 = property(get_VideoFormatMpg1, None)
    VideoFormatMss1 = property(get_VideoFormatMss1, None)
    VideoFormatMss2 = property(get_VideoFormatMss2, None)
    VideoFormatWmv1 = property(get_VideoFormatWmv1, None)
    VideoFormatWmv2 = property(get_VideoFormatWmv2, None)
    VideoFormatWmv3 = property(get_VideoFormatWmv3, None)
    VideoFormatWvc1 = property(get_VideoFormatWvc1, None)
    VideoFormat420O = property(get_VideoFormat420O, None)
    AudioFormatAac = property(get_AudioFormatAac, None)
    AudioFormatAdts = property(get_AudioFormatAdts, None)
    AudioFormatAlac = property(get_AudioFormatAlac, None)
    AudioFormatAmrNB = property(get_AudioFormatAmrNB, None)
    AudioFormatAmrWB = property(get_AudioFormatAmrWB, None)
    AudioFormatAmrWP = property(get_AudioFormatAmrWP, None)
    AudioFormatDolbyAC3 = property(get_AudioFormatDolbyAC3, None)
    AudioFormatDolbyAC3Spdif = property(get_AudioFormatDolbyAC3Spdif, None)
    AudioFormatDolbyDDPlus = property(get_AudioFormatDolbyDDPlus, None)
    AudioFormatDrm = property(get_AudioFormatDrm, None)
    AudioFormatDts = property(get_AudioFormatDts, None)
    AudioFormatFlac = property(get_AudioFormatFlac, None)
    AudioFormatFloat = property(get_AudioFormatFloat, None)
    AudioFormatMP3 = property(get_AudioFormatMP3, None)
    AudioFormatMPeg = property(get_AudioFormatMPeg, None)
    AudioFormatMsp1 = property(get_AudioFormatMsp1, None)
    AudioFormatOpus = property(get_AudioFormatOpus, None)
    AudioFormatPcm = property(get_AudioFormatPcm, None)
    AudioFormatWmaSpdif = property(get_AudioFormatWmaSpdif, None)
    AudioFormatWMAudioLossless = property(get_AudioFormatWMAudioLossless, None)
    AudioFormatWMAudioV8 = property(get_AudioFormatWMAudioV8, None)
    AudioFormatWMAudioV9 = property(get_AudioFormatWMAudioV9, None)
class IDataCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IDataCue'
    _iid_ = Guid('{7c7f676d-1fbc-4e2d-9a87-ee38bd1dc637}')
    @winrt_commethod(6)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, put_Data)
class IDataCue2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IDataCue2'
    _iid_ = Guid('{bc561b15-95f2-49e8-96f1-8dd5dac68d93}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Foundation.Collections.PropertySet: ...
    Properties = property(get_Properties, None)
class IFaceDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectedEventArgs'
    _iid_ = Guid('{19918426-c65b-46ba-85f8-13880576c90a}')
    @winrt_commethod(6)
    def get_ResultFrame(self) -> Windows.Media.Core.FaceDetectionEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class IFaceDetectionEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffect'
    _iid_ = Guid('{ae15ebd2-0542-42a9-bc90-f283a29f46c1}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_DesiredDetectionInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_DesiredDetectionInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def add_FaceDetected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.FaceDetectionEffect, Windows.Media.Core.FaceDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_FaceDetected(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    DesiredDetectionInterval = property(get_DesiredDetectionInterval, put_DesiredDetectionInterval)
class IFaceDetectionEffectDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffectDefinition'
    _iid_ = Guid('{43dca081-b848-4f33-b702-1fd2624fb016}')
    @winrt_commethod(6)
    def put_DetectionMode(self, value: Windows.Media.Core.FaceDetectionMode) -> Void: ...
    @winrt_commethod(7)
    def get_DetectionMode(self) -> Windows.Media.Core.FaceDetectionMode: ...
    @winrt_commethod(8)
    def put_SynchronousDetectionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SynchronousDetectionEnabled(self) -> Boolean: ...
    DetectionMode = property(get_DetectionMode, put_DetectionMode)
    SynchronousDetectionEnabled = property(get_SynchronousDetectionEnabled, put_SynchronousDetectionEnabled)
class IFaceDetectionEffectFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffectFrame'
    _iid_ = Guid('{8ab08993-5dc8-447b-a247-5270bd802ece}')
    @winrt_commethod(6)
    def get_DetectedFaces(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.FaceAnalysis.DetectedFace]: ...
    DetectedFaces = property(get_DetectedFaces, None)
class IHighDynamicRangeControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IHighDynamicRangeControl'
    _iid_ = Guid('{55f1a7ae-d957-4dc9-9d1c-8553a82a7d99}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    Enabled = property(get_Enabled, put_Enabled)
class IHighDynamicRangeOutput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IHighDynamicRangeOutput'
    _iid_ = Guid('{0f57806b-253b-4119-bb40-3a90e51384f7}')
    @winrt_commethod(6)
    def get_Certainty(self) -> Double: ...
    @winrt_commethod(7)
    def get_FrameControllers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Devices.Core.FrameController]: ...
    Certainty = property(get_Certainty, None)
    FrameControllers = property(get_FrameControllers, None)
class IImageCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IImageCue'
    _iid_ = Guid('{52828282-367b-440b-9116-3c84570dd270}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Media.Core.TimedTextPoint: ...
    @winrt_commethod(7)
    def put_Position(self, value: Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_commethod(8)
    def get_Extent(self) -> Windows.Media.Core.TimedTextSize: ...
    @winrt_commethod(9)
    def put_Extent(self, value: Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_commethod(10)
    def put_SoftwareBitmap(self, value: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(11)
    def get_SoftwareBitmap(self) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    Position = property(get_Position, put_Position)
    Extent = property(get_Extent, put_Extent)
    SoftwareBitmap = property(get_SoftwareBitmap, put_SoftwareBitmap)
class IInitializeMediaStreamSourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs'
    _iid_ = Guid('{25bc45e1-9b08-4c2e-a855-4542f1a75deb}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(7)
    def get_RandomAccessStream(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Source = property(get_Source, None)
    RandomAccessStream = property(get_RandomAccessStream, None)
class ILowLightFusionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ILowLightFusionResult'
    _iid_ = Guid('{78edbe35-27a0-42e0-9cd3-738d2089de9c}')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    Frame = property(get_Frame, None)
class ILowLightFusionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ILowLightFusionStatics'
    _iid_ = Guid('{5305016d-c29e-40e2-87a9-9e1fd2f192f5}')
    @winrt_commethod(6)
    def get_SupportedBitmapPixelFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(7)
    def get_MaxSupportedFrameCount(self) -> Int32: ...
    @winrt_commethod(8)
    def FuseAsync(self, frameSet: Windows.Foundation.Collections.IIterable[Windows.Graphics.Imaging.SoftwareBitmap]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Core.LowLightFusionResult, Double]: ...
    SupportedBitmapPixelFormats = property(get_SupportedBitmapPixelFormats, None)
    MaxSupportedFrameCount = property(get_MaxSupportedFrameCount, None)
class IMediaBinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBinder'
    _iid_ = Guid('{2b7e40aa-de07-424f-83f1-f1de46c4fa2e}')
    @winrt_commethod(6)
    def add_Binding(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaBinder, Windows.Media.Core.MediaBindingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Binding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Token(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Token(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> Windows.Media.Core.MediaSource: ...
    Token = property(get_Token, put_Token)
    Source = property(get_Source, None)
class IMediaBindingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs'
    _iid_ = Guid('{b61cb25a-1b6d-4630-a86d-2f0837f712e5}')
    @winrt_commethod(6)
    def add_Canceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaBindingEventArgs, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Canceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_MediaBinder(self) -> Windows.Media.Core.MediaBinder: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    @winrt_commethod(10)
    def SetUri(self, uri: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def SetStream(self, stream: Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetStreamReference(self, stream: Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Void: ...
    MediaBinder = property(get_MediaBinder, None)
class IMediaBindingEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs2'
    _iid_ = Guid('{0464cceb-bb5a-482f-b8ba-f0284c696567}')
    @winrt_commethod(6)
    def SetAdaptiveMediaSource(self, mediaSource: Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Void: ...
    @winrt_commethod(7)
    def SetStorageFile(self, file: Windows.Storage.IStorageFile) -> Void: ...
class IMediaBindingEventArgs3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs3'
    _iid_ = Guid('{f8eb475e-19be-44fc-a5ed-7aba315037f9}')
    @winrt_commethod(6)
    def SetDownloadOperation(self, downloadOperation: Windows.Networking.BackgroundTransfer.DownloadOperation) -> Void: ...
class IMediaCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaCue'
    _iid_ = Guid('{c7d15e5d-59dc-431f-a0ee-27744323b36d}')
    @winrt_commethod(6)
    def put_StartTime(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Id(self) -> WinRT_String: ...
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
class IMediaCueEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaCueEventArgs'
    _iid_ = Guid('{d12f47f7-5fa4-4e68-9fe5-32160dcee57e}')
    @winrt_commethod(6)
    def get_Cue(self) -> Windows.Media.Core.IMediaCue: ...
    Cue = property(get_Cue, None)
class IMediaSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource'
    _iid_ = Guid('{e7bfb599-a09d-4c21-bcdf-20af4f86b3d9}')
class IMediaSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource2'
    _iid_ = Guid('{2eb61048-655f-4c37-b813-b4e45dfa0abe}')
    @winrt_commethod(6)
    def add_OpenOperationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSource, Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenOperationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_CustomProperties(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(9)
    def get_Duration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_ExternalTimedTextSources(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Media.Core.TimedTextSource]: ...
    @winrt_commethod(12)
    def get_ExternalTimedMetadataTracks(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Media.Core.TimedMetadataTrack]: ...
    CustomProperties = property(get_CustomProperties, None)
    Duration = property(get_Duration, None)
    IsOpen = property(get_IsOpen, None)
    ExternalTimedTextSources = property(get_ExternalTimedTextSources, None)
    ExternalTimedMetadataTracks = property(get_ExternalTimedMetadataTracks, None)
class IMediaSource3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource3'
    _iid_ = Guid('{b59f0d9b-4b6e-41ed-bbb4-7c7509a994ad}')
    @winrt_commethod(6)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSource, Windows.Media.Core.MediaSourceStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.Media.Core.MediaSourceState: ...
    @winrt_commethod(9)
    def Reset(self) -> Void: ...
    State = property(get_State, None)
class IMediaSource4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource4'
    _iid_ = Guid('{bdafad57-8eff-4c63-85a6-84de0ae3e4f2}')
    @winrt_commethod(6)
    def get_AdaptiveMediaSource(self) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_commethod(7)
    def get_MediaStreamSource(self) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(8)
    def get_MseStreamSource(self) -> Windows.Media.Core.MseStreamSource: ...
    @winrt_commethod(9)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def OpenAsync(self) -> Windows.Foundation.IAsyncAction: ...
    AdaptiveMediaSource = property(get_AdaptiveMediaSource, None)
    MediaStreamSource = property(get_MediaStreamSource, None)
    MseStreamSource = property(get_MseStreamSource, None)
    Uri = property(get_Uri, None)
class IMediaSource5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource5'
    _iid_ = Guid('{331a22ae-ed2e-4a22-94c8-b743a92b3022}')
    @winrt_commethod(6)
    def get_DownloadOperation(self) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    DownloadOperation = property(get_DownloadOperation, None)
class IMediaSourceAppServiceConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceAppServiceConnection'
    _iid_ = Guid('{61e1ea97-1916-4810-b7f4-b642be829596}')
    @winrt_commethod(6)
    def add_InitializeMediaStreamSourceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSourceAppServiceConnection, Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InitializeMediaStreamSourceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
class IMediaSourceAppServiceConnectionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceAppServiceConnectionFactory'
    _iid_ = Guid('{65b912eb-80b9-44f9-9c1e-e120f6d92838}')
    @winrt_commethod(6)
    def Create(self, appServiceConnection: Windows.ApplicationModel.AppService.AppServiceConnection) -> Windows.Media.Core.MediaSourceAppServiceConnection: ...
class IMediaSourceError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceError'
    _iid_ = Guid('{5c0a8965-37c5-4e9d-8d21-1cdee90cecc6}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IMediaSourceOpenOperationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs'
    _iid_ = Guid('{fc682ceb-e281-477c-a8e0-1acd654114c8}')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Media.Core.MediaSourceError: ...
    Error = property(get_Error, None)
class IMediaSourceStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStateChangedEventArgs'
    _iid_ = Guid('{0a30af82-9071-4bac-bc39-ca2a93b717a9}')
    @winrt_commethod(6)
    def get_OldState(self) -> Windows.Media.Core.MediaSourceState: ...
    @winrt_commethod(7)
    def get_NewState(self) -> Windows.Media.Core.MediaSourceState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
class IMediaSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics'
    _iid_ = Guid('{f77d6fa4-4652-410e-b1d8-e9a5e245a45c}')
    @winrt_commethod(6)
    def CreateFromAdaptiveMediaSource(self, mediaSource: Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(7)
    def CreateFromMediaStreamSource(self, mediaSource: Windows.Media.Core.MediaStreamSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(8)
    def CreateFromMseStreamSource(self, mediaSource: Windows.Media.Core.MseStreamSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(9)
    def CreateFromIMediaSource(self, mediaSource: Windows.Media.Core.IMediaSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(10)
    def CreateFromStorageFile(self, file: Windows.Storage.IStorageFile) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(11)
    def CreateFromStream(self, stream: Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(12)
    def CreateFromStreamReference(self, stream: Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Windows.Media.Core.MediaSource: ...
    @winrt_commethod(13)
    def CreateFromUri(self, uri: Windows.Foundation.Uri) -> Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics2'
    _iid_ = Guid('{eee161a4-7f13-4896-b8cb-df0de5bcb9f1}')
    @winrt_commethod(6)
    def CreateFromMediaBinder(self, binder: Windows.Media.Core.MediaBinder) -> Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics3'
    _iid_ = Guid('{453a30d6-2bea-4122-9f73-eace04526e35}')
    @winrt_commethod(6)
    def CreateFromMediaFrameSource(self, frameSource: Windows.Media.Capture.Frames.MediaFrameSource) -> Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics4'
    _iid_ = Guid('{281b3bfc-e50a-4428-a500-9c4ed918d3f0}')
    @winrt_commethod(6)
    def CreateFromDownloadOperation(self, downloadOperation: Windows.Networking.BackgroundTransfer.DownloadOperation) -> Windows.Media.Core.MediaSource: ...
class IMediaStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamDescriptor'
    _iid_ = Guid('{80f16e6e-92f7-451e-97d2-afd80742da70}')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Language(self) -> WinRT_String: ...
    IsSelected = property(get_IsSelected, None)
    Name = property(get_Name, put_Name)
    Language = property(get_Language, put_Language)
class IMediaStreamDescriptor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamDescriptor2'
    _iid_ = Guid('{5073010f-e8b2-4071-b00b-ebf337a76b58}')
    @winrt_commethod(6)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    Label = property(get_Label, put_Label)
class IMediaStreamSample(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSample'
    _iid_ = Guid('{5c8db627-4b80-4361-9837-6cb7481ad9d6}')
    @winrt_commethod(6)
    def add_Processed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSample, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Processed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Buffer(self) -> Windows.Storage.Streams.Buffer: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_ExtendedProperties(self) -> Windows.Media.Core.MediaStreamSamplePropertySet: ...
    @winrt_commethod(11)
    def get_Protection(self) -> Windows.Media.Core.MediaStreamSampleProtectionProperties: ...
    @winrt_commethod(12)
    def put_DecodeTimestamp(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(13)
    def get_DecodeTimestamp(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(15)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(16)
    def put_KeyFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_KeyFrame(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_Discontinuous(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def get_Discontinuous(self) -> Boolean: ...
    Buffer = property(get_Buffer, None)
    Timestamp = property(get_Timestamp, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
    Protection = property(get_Protection, None)
    DecodeTimestamp = property(get_DecodeTimestamp, put_DecodeTimestamp)
    Duration = property(get_Duration, put_Duration)
    KeyFrame = property(get_KeyFrame, put_KeyFrame)
    Discontinuous = property(get_Discontinuous, put_Discontinuous)
class IMediaStreamSample2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSample2'
    _iid_ = Guid('{45078691-fce8-4746-a1c8-10c25d3d7cd3}')
    @winrt_commethod(6)
    def get_Direct3D11Surface(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    Direct3D11Surface = property(get_Direct3D11Surface, None)
class IMediaStreamSampleProtectionProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleProtectionProperties'
    _iid_ = Guid('{4eb88292-ecdf-493e-841d-dd4add7caca2}')
    @winrt_commethod(6)
    def SetKeyIdentifier(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def GetKeyIdentifier(self, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_commethod(8)
    def SetInitializationVector(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def GetInitializationVector(self, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_commethod(10)
    def SetSubSampleMapping(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(11)
    def GetSubSampleMapping(self, value: POINTER(c_char_p_no)) -> Void: ...
class IMediaStreamSampleStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleStatics'
    _iid_ = Guid('{dfdf218f-a6cf-4579-be41-73dd941ad972}')
    @winrt_commethod(6)
    def CreateFromBuffer(self, buffer: Windows.Storage.Streams.IBuffer, timestamp: Windows.Foundation.TimeSpan) -> Windows.Media.Core.MediaStreamSample: ...
    @winrt_commethod(7)
    def CreateFromStreamAsync(self, stream: Windows.Storage.Streams.IInputStream, count: UInt32, timestamp: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Media.Core.MediaStreamSample]: ...
class IMediaStreamSampleStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleStatics2'
    _iid_ = Guid('{9efe9521-6d46-494c-a2f8-d662922e2dd7}')
    @winrt_commethod(6)
    def CreateFromDirect3D11Surface(self, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, timestamp: Windows.Foundation.TimeSpan) -> Windows.Media.Core.MediaStreamSample: ...
class IMediaStreamSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource'
    _iid_ = Guid('{3712d543-45eb-4138-aa62-c01e26f3843f}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Starting(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Starting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Paused(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Paused(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SampleRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SampleRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SwitchStreamsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SwitchStreamsRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def NotifyError(self, errorStatus: Windows.Media.Core.MediaStreamSourceErrorStatus) -> Void: ...
    @winrt_commethod(17)
    def AddStreamDescriptor(self, descriptor: Windows.Media.Core.IMediaStreamDescriptor) -> Void: ...
    @winrt_commethod(18)
    def put_MediaProtectionManager(self, value: Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_commethod(19)
    def get_MediaProtectionManager(self) -> Windows.Media.Protection.MediaProtectionManager: ...
    @winrt_commethod(20)
    def put_Duration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(21)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(22)
    def put_CanSeek(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_CanSeek(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_BufferTime(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(25)
    def get_BufferTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(26)
    def SetBufferedRange(self, startOffset: Windows.Foundation.TimeSpan, endOffset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(27)
    def get_MusicProperties(self) -> Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_commethod(28)
    def get_VideoProperties(self) -> Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_commethod(29)
    def put_Thumbnail(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(30)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(31)
    def AddProtectionKey(self, streamDescriptor: Windows.Media.Core.IMediaStreamDescriptor, keyIdentifier: c_char_p_no, licenseData: c_char_p_no) -> Void: ...
    MediaProtectionManager = property(get_MediaProtectionManager, put_MediaProtectionManager)
    Duration = property(get_Duration, put_Duration)
    CanSeek = property(get_CanSeek, put_CanSeek)
    BufferTime = property(get_BufferTime, put_BufferTime)
    MusicProperties = property(get_MusicProperties, None)
    VideoProperties = property(get_VideoProperties, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
class IMediaStreamSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource2'
    _iid_ = Guid('{ec55d0ad-2e6a-4f74-adbb-b562d1533849}')
    @winrt_commethod(6)
    def add_SampleRendered(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SampleRendered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMediaStreamSource3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource3'
    _iid_ = Guid('{6a2a2746-3ddd-4ddf-a121-94045ecf9440}')
    @winrt_commethod(6)
    def put_MaxSupportedPlaybackRate(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(7)
    def get_MaxSupportedPlaybackRate(self) -> Windows.Foundation.IReference[Double]: ...
    MaxSupportedPlaybackRate = property(get_MaxSupportedPlaybackRate, put_MaxSupportedPlaybackRate)
class IMediaStreamSource4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource4'
    _iid_ = Guid('{1d0cfcab-830d-417c-a3a9-2454fd6415c7}')
    @winrt_commethod(6)
    def put_IsLive(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsLive(self) -> Boolean: ...
    IsLive = property(get_IsLive, put_IsLive)
class IMediaStreamSourceClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceClosedEventArgs'
    _iid_ = Guid('{cd8c7eb2-4816-4e24-88f0-491ef7386406}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Media.Core.MediaStreamSourceClosedRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceClosedRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceClosedRequest'
    _iid_ = Guid('{907c00e9-18a3-4951-887a-2c1eebd5c69e}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Media.Core.MediaStreamSourceClosedReason: ...
    Reason = property(get_Reason, None)
class IMediaStreamSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceFactory'
    _iid_ = Guid('{ef77e0d9-d158-4b7a-863f-203342fbfd41}')
    @winrt_commethod(6)
    def CreateFromDescriptor(self, descriptor: Windows.Media.Core.IMediaStreamDescriptor) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(7)
    def CreateFromDescriptors(self, descriptor: Windows.Media.Core.IMediaStreamDescriptor, descriptor2: Windows.Media.Core.IMediaStreamDescriptor) -> Windows.Media.Core.MediaStreamSource: ...
class IMediaStreamSourceSampleRenderedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs'
    _iid_ = Guid('{9d697b05-d4f2-4c7a-9dfe-8d6cd0b3ee84}')
    @winrt_commethod(6)
    def get_SampleLag(self) -> Windows.Foundation.TimeSpan: ...
    SampleLag = property(get_SampleLag, None)
class IMediaStreamSourceSampleRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequest'
    _iid_ = Guid('{4db341a9-3501-4d9b-83f9-8f235c822532}')
    @winrt_commethod(6)
    def get_StreamDescriptor(self) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Media.Core.MediaStreamSourceSampleRequestDeferral: ...
    @winrt_commethod(8)
    def put_Sample(self, value: Windows.Media.Core.MediaStreamSample) -> Void: ...
    @winrt_commethod(9)
    def get_Sample(self) -> Windows.Media.Core.MediaStreamSample: ...
    @winrt_commethod(10)
    def ReportSampleProgress(self, progress: UInt32) -> Void: ...
    StreamDescriptor = property(get_StreamDescriptor, None)
    Sample = property(get_Sample, put_Sample)
class IMediaStreamSourceSampleRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral'
    _iid_ = Guid('{7895cc02-f982-43c8-9d16-c62d999319be}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSampleRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs'
    _iid_ = Guid('{10f9bb9e-71c5-492f-847f-0da1f35e81f8}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Media.Core.MediaStreamSourceSampleRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceStartingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingEventArgs'
    _iid_ = Guid('{f41468f2-c274-4940-a5bb-28a572452fa7}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Media.Core.MediaStreamSourceStartingRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceStartingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingRequest'
    _iid_ = Guid('{2a9093e4-35c4-4b1b-a791-0d99db56dd1d}')
    @winrt_commethod(6)
    def get_StartPosition(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Media.Core.MediaStreamSourceStartingRequestDeferral: ...
    @winrt_commethod(8)
    def SetActualStartPosition(self, position: Windows.Foundation.TimeSpan) -> Void: ...
    StartPosition = property(get_StartPosition, None)
class IMediaStreamSourceStartingRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral'
    _iid_ = Guid('{3f1356a5-6340-4dc4-9910-068ed9f598f8}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSwitchStreamsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest'
    _iid_ = Guid('{41b8808e-38a9-4ec3-9ba0-b69b85501e90}')
    @winrt_commethod(6)
    def get_OldStreamDescriptor(self) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(7)
    def get_NewStreamDescriptor(self) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral: ...
    OldStreamDescriptor = property(get_OldStreamDescriptor, None)
    NewStreamDescriptor = property(get_NewStreamDescriptor, None)
class IMediaStreamSourceSwitchStreamsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral'
    _iid_ = Guid('{bee3d835-a505-4f9a-b943-2b8cb1b4bbd9}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSwitchStreamsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs'
    _iid_ = Guid('{42202b72-6ea1-4677-981e-350a0da412aa}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest: ...
    Request = property(get_Request, None)
class IMediaTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaTrack'
    _iid_ = Guid('{03e1fafc-c931-491a-b46b-c10ee8c256b7}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_TrackKind(self) -> Windows.Media.Core.MediaTrackKind: ...
    @winrt_commethod(9)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Label(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    TrackKind = property(get_TrackKind, None)
    Label = property(get_Label, put_Label)
class IMseSourceBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseSourceBuffer'
    _iid_ = Guid('{0c1aa3e3-df8d-4079-a3fe-6849184b4e2f}')
    @winrt_commethod(6)
    def add_UpdateStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UpdateStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_UpdateEnded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UpdateEnded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ErrorOccurred(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ErrorOccurred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Aborted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Aborted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Mode(self) -> Windows.Media.Core.MseAppendMode: ...
    @winrt_commethod(17)
    def put_Mode(self, value: Windows.Media.Core.MseAppendMode) -> Void: ...
    @winrt_commethod(18)
    def get_IsUpdating(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_Buffered(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.MseTimeRange]: ...
    @winrt_commethod(20)
    def get_TimestampOffset(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(21)
    def put_TimestampOffset(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(22)
    def get_AppendWindowStart(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(23)
    def put_AppendWindowStart(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(24)
    def get_AppendWindowEnd(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(25)
    def put_AppendWindowEnd(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(26)
    def AppendBuffer(self, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(27)
    def AppendStream(self, stream: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(28)
    def AppendStreamMaxSize(self, stream: Windows.Storage.Streams.IInputStream, maxSize: UInt64) -> Void: ...
    @winrt_commethod(29)
    def Abort(self) -> Void: ...
    @winrt_commethod(30)
    def Remove(self, start: Windows.Foundation.TimeSpan, end: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    IsUpdating = property(get_IsUpdating, None)
    Buffered = property(get_Buffered, None)
    TimestampOffset = property(get_TimestampOffset, put_TimestampOffset)
    AppendWindowStart = property(get_AppendWindowStart, put_AppendWindowStart)
    AppendWindowEnd = property(get_AppendWindowEnd, put_AppendWindowEnd)
class IMseSourceBufferList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseSourceBufferList'
    _iid_ = Guid('{95fae8e7-a8e7-4ebf-8927-145e940ba511}')
    @winrt_commethod(6)
    def add_SourceBufferAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBufferList, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceBufferAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceBufferRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBufferList, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceBufferRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Buffers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.MseSourceBuffer]: ...
    Buffers = property(get_Buffers, None)
class IMseStreamSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSource'
    _iid_ = Guid('{b0b4198d-02f4-4923-88dd-81bc3f360ffa}')
    @winrt_commethod(6)
    def add_Opened(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Opened(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Ended(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Ended(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_SourceBuffers(self) -> Windows.Media.Core.MseSourceBufferList: ...
    @winrt_commethod(13)
    def get_ActiveSourceBuffers(self) -> Windows.Media.Core.MseSourceBufferList: ...
    @winrt_commethod(14)
    def get_ReadyState(self) -> Windows.Media.Core.MseReadyState: ...
    @winrt_commethod(15)
    def get_Duration(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(16)
    def put_Duration(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(17)
    def AddSourceBuffer(self, mimeType: WinRT_String) -> Windows.Media.Core.MseSourceBuffer: ...
    @winrt_commethod(18)
    def RemoveSourceBuffer(self, buffer: Windows.Media.Core.MseSourceBuffer) -> Void: ...
    @winrt_commethod(19)
    def EndOfStream(self, status: Windows.Media.Core.MseEndOfStreamStatus) -> Void: ...
    SourceBuffers = property(get_SourceBuffers, None)
    ActiveSourceBuffers = property(get_ActiveSourceBuffers, None)
    ReadyState = property(get_ReadyState, None)
    Duration = property(get_Duration, put_Duration)
class IMseStreamSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSource2'
    _iid_ = Guid('{66f57d37-f9e7-418a-9cde-a020e956552b}')
    @winrt_commethod(6)
    def get_LiveSeekableRange(self) -> Windows.Foundation.IReference[Windows.Media.Core.MseTimeRange]: ...
    @winrt_commethod(7)
    def put_LiveSeekableRange(self, value: Windows.Foundation.IReference[Windows.Media.Core.MseTimeRange]) -> Void: ...
    LiveSeekableRange = property(get_LiveSeekableRange, put_LiveSeekableRange)
class IMseStreamSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSourceStatics'
    _iid_ = Guid('{465c679d-d570-43ce-ba21-0bff5f3fbd0a}')
    @winrt_commethod(6)
    def IsContentTypeSupported(self, contentType: WinRT_String) -> Boolean: ...
class ISceneAnalysisEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffect'
    _iid_ = Guid('{c04ba319-ca41-4813-bffd-7b08b0ed2557}')
    @winrt_commethod(6)
    def get_HighDynamicRangeAnalyzer(self) -> Windows.Media.Core.HighDynamicRangeControl: ...
    @winrt_commethod(7)
    def put_DesiredAnalysisInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredAnalysisInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def add_SceneAnalyzed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.SceneAnalysisEffect, Windows.Media.Core.SceneAnalyzedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_SceneAnalyzed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    HighDynamicRangeAnalyzer = property(get_HighDynamicRangeAnalyzer, None)
    DesiredAnalysisInterval = property(get_DesiredAnalysisInterval, put_DesiredAnalysisInterval)
class ISceneAnalysisEffectFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffectFrame'
    _iid_ = Guid('{d8b10e4c-7fd9-42e1-85eb-6572c297c987}')
    @winrt_commethod(6)
    def get_FrameControlValues(self) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_commethod(7)
    def get_HighDynamicRange(self) -> Windows.Media.Core.HighDynamicRangeOutput: ...
    FrameControlValues = property(get_FrameControlValues, None)
    HighDynamicRange = property(get_HighDynamicRange, None)
class ISceneAnalysisEffectFrame2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffectFrame2'
    _iid_ = Guid('{2d4e29be-061f-47ae-9915-02524b5f9a5f}')
    @winrt_commethod(6)
    def get_AnalysisRecommendation(self) -> Windows.Media.Core.SceneAnalysisRecommendation: ...
    AnalysisRecommendation = property(get_AnalysisRecommendation, None)
class ISceneAnalyzedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalyzedEventArgs'
    _iid_ = Guid('{146b9588-2851-45e4-ad55-44cf8df8db4d}')
    @winrt_commethod(6)
    def get_ResultFrame(self) -> Windows.Media.Core.SceneAnalysisEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class ISingleSelectMediaTrackList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISingleSelectMediaTrackList'
    _iid_ = Guid('{77206f1f-c34f-494f-8077-2bad9ff4ecf1}')
    @winrt_commethod(6)
    def add_SelectedIndexChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.ISingleSelectMediaTrackList, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SelectedIndexChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def put_SelectedIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_SelectedIndex(self) -> Int32: ...
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
class ISpeechCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISpeechCue'
    _iid_ = Guid('{aee254dc-1725-4bad-8043-a98499b017a2}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_StartPositionInInput(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_StartPositionInInput(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_EndPositionInInput(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_EndPositionInInput(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    Text = property(get_Text, put_Text)
    StartPositionInInput = property(get_StartPositionInInput, put_StartPositionInInput)
    EndPositionInInput = property(get_EndPositionInInput, put_EndPositionInInput)
class ITimedMetadataStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataStreamDescriptor'
    _iid_ = Guid('{133336bf-296a-463e-9ff9-01cd25691408}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_commethod(7)
    def Copy(self) -> Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
class ITimedMetadataStreamDescriptorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataStreamDescriptorFactory'
    _iid_ = Guid('{c027de30-7362-4ff9-98b1-2dfd0b8d1cae}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: Windows.Media.MediaProperties.TimedMetadataEncodingProperties) -> Windows.Media.Core.TimedMetadataStreamDescriptor: ...
class ITimedMetadataTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrack'
    _iid_ = Guid('{9e6aed9e-f67a-49a9-b330-cf03b0e9cf07}')
    @winrt_commethod(6)
    def add_CueEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.MediaCueEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CueEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_CueExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.MediaCueEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CueExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_TrackFailed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.TimedMetadataTrackFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_TrackFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Cues(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.IMediaCue]: ...
    @winrt_commethod(13)
    def get_ActiveCues(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.IMediaCue]: ...
    @winrt_commethod(14)
    def get_TimedMetadataKind(self) -> Windows.Media.Core.TimedMetadataKind: ...
    @winrt_commethod(15)
    def get_DispatchType(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def AddCue(self, cue: Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_commethod(17)
    def RemoveCue(self, cue: Windows.Media.Core.IMediaCue) -> Void: ...
    Cues = property(get_Cues, None)
    ActiveCues = property(get_ActiveCues, None)
    TimedMetadataKind = property(get_TimedMetadataKind, None)
    DispatchType = property(get_DispatchType, None)
class ITimedMetadataTrack2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrack2'
    _iid_ = Guid('{21b4b648-9f9d-40ba-a8f3-1a92753aef0b}')
    @winrt_commethod(6)
    def get_PlaybackItem(self) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
class ITimedMetadataTrackError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackError'
    _iid_ = Guid('{b3767915-4114-4819-b9d9-dd76089e72f8}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> Windows.Media.Core.TimedMetadataTrackErrorCode: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedError = property(get_ExtendedError, None)
class ITimedMetadataTrackFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackFactory'
    _iid_ = Guid('{8dd57611-97b3-4e1f-852c-0f482c81ad26}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, language: WinRT_String, kind: Windows.Media.Core.TimedMetadataKind) -> Windows.Media.Core.TimedMetadataTrack: ...
class ITimedMetadataTrackFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackFailedEventArgs'
    _iid_ = Guid('{a57fc9d1-6789-4d4d-b07f-84b4f31acb70}')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Media.Core.TimedMetadataTrackError: ...
    Error = property(get_Error, None)
class ITimedMetadataTrackProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackProvider'
    _iid_ = Guid('{3b7f2024-f74e-4ade-93c5-219da05b6856}')
    @winrt_commethod(6)
    def get_TimedMetadataTracks(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.TimedMetadataTrack]: ...
    TimedMetadataTracks = property(get_TimedMetadataTracks, None)
class ITimedTextBouten(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextBouten'
    _iid_ = Guid('{d9062783-5597-5092-820c-8f738e0f774a}')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Media.Core.TimedTextBoutenType: ...
    @winrt_commethod(7)
    def put_Type(self, value: Windows.Media.Core.TimedTextBoutenType) -> Void: ...
    @winrt_commethod(8)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Position(self) -> Windows.Media.Core.TimedTextBoutenPosition: ...
    @winrt_commethod(11)
    def put_Position(self, value: Windows.Media.Core.TimedTextBoutenPosition) -> Void: ...
    Type = property(get_Type, put_Type)
    Color = property(get_Color, put_Color)
    Position = property(get_Position, put_Position)
class ITimedTextCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextCue'
    _iid_ = Guid('{51c79e51-3b86-494d-b359-bb2ea7aca9a9}')
    @winrt_commethod(6)
    def get_CueRegion(self) -> Windows.Media.Core.TimedTextRegion: ...
    @winrt_commethod(7)
    def put_CueRegion(self, value: Windows.Media.Core.TimedTextRegion) -> Void: ...
    @winrt_commethod(8)
    def get_CueStyle(self) -> Windows.Media.Core.TimedTextStyle: ...
    @winrt_commethod(9)
    def put_CueStyle(self, value: Windows.Media.Core.TimedTextStyle) -> Void: ...
    @winrt_commethod(10)
    def get_Lines(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedTextLine]: ...
    CueRegion = property(get_CueRegion, put_CueRegion)
    CueStyle = property(get_CueStyle, put_CueStyle)
    Lines = property(get_Lines, None)
class ITimedTextLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextLine'
    _iid_ = Guid('{978d7ce2-7308-4c66-be50-65777289f5df}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Subformats(self) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedTextSubformat]: ...
    Text = property(get_Text, put_Text)
    Subformats = property(get_Subformats, None)
class ITimedTextRegion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextRegion'
    _iid_ = Guid('{1ed0881f-8a06-4222-9f59-b21bf40124b4}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Media.Core.TimedTextPoint: ...
    @winrt_commethod(9)
    def put_Position(self, value: Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_commethod(10)
    def get_Extent(self) -> Windows.Media.Core.TimedTextSize: ...
    @winrt_commethod(11)
    def put_Extent(self, value: Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_commethod(12)
    def get_Background(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_Background(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_WritingMode(self) -> Windows.Media.Core.TimedTextWritingMode: ...
    @winrt_commethod(15)
    def put_WritingMode(self, value: Windows.Media.Core.TimedTextWritingMode) -> Void: ...
    @winrt_commethod(16)
    def get_DisplayAlignment(self) -> Windows.Media.Core.TimedTextDisplayAlignment: ...
    @winrt_commethod(17)
    def put_DisplayAlignment(self, value: Windows.Media.Core.TimedTextDisplayAlignment) -> Void: ...
    @winrt_commethod(18)
    def get_LineHeight(self) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(19)
    def put_LineHeight(self, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(20)
    def get_IsOverflowClipped(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsOverflowClipped(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_Padding(self) -> Windows.Media.Core.TimedTextPadding: ...
    @winrt_commethod(23)
    def put_Padding(self, value: Windows.Media.Core.TimedTextPadding) -> Void: ...
    @winrt_commethod(24)
    def get_TextWrapping(self) -> Windows.Media.Core.TimedTextWrapping: ...
    @winrt_commethod(25)
    def put_TextWrapping(self, value: Windows.Media.Core.TimedTextWrapping) -> Void: ...
    @winrt_commethod(26)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(27)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(28)
    def get_ScrollMode(self) -> Windows.Media.Core.TimedTextScrollMode: ...
    @winrt_commethod(29)
    def put_ScrollMode(self, value: Windows.Media.Core.TimedTextScrollMode) -> Void: ...
    Name = property(get_Name, put_Name)
    Position = property(get_Position, put_Position)
    Extent = property(get_Extent, put_Extent)
    Background = property(get_Background, put_Background)
    WritingMode = property(get_WritingMode, put_WritingMode)
    DisplayAlignment = property(get_DisplayAlignment, put_DisplayAlignment)
    LineHeight = property(get_LineHeight, put_LineHeight)
    IsOverflowClipped = property(get_IsOverflowClipped, put_IsOverflowClipped)
    Padding = property(get_Padding, put_Padding)
    TextWrapping = property(get_TextWrapping, put_TextWrapping)
    ZIndex = property(get_ZIndex, put_ZIndex)
    ScrollMode = property(get_ScrollMode, put_ScrollMode)
class ITimedTextRuby(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextRuby'
    _iid_ = Guid('{10335c29-5b3c-5693-9959-d05a0bd24628}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Media.Core.TimedTextRubyPosition: ...
    @winrt_commethod(9)
    def put_Position(self, value: Windows.Media.Core.TimedTextRubyPosition) -> Void: ...
    @winrt_commethod(10)
    def get_Align(self) -> Windows.Media.Core.TimedTextRubyAlign: ...
    @winrt_commethod(11)
    def put_Align(self, value: Windows.Media.Core.TimedTextRubyAlign) -> Void: ...
    @winrt_commethod(12)
    def get_Reserve(self) -> Windows.Media.Core.TimedTextRubyReserve: ...
    @winrt_commethod(13)
    def put_Reserve(self, value: Windows.Media.Core.TimedTextRubyReserve) -> Void: ...
    Text = property(get_Text, put_Text)
    Position = property(get_Position, put_Position)
    Align = property(get_Align, put_Align)
    Reserve = property(get_Reserve, put_Reserve)
class ITimedTextSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSource'
    _iid_ = Guid('{c4ed9ba6-101f-404d-a949-82f33fcd93b7}')
    @winrt_commethod(6)
    def add_Resolved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedTextSource, Windows.Media.Core.TimedTextSourceResolveResultEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Resolved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ITimedTextSourceResolveResultEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceResolveResultEventArgs'
    _iid_ = Guid('{48907c9c-dcd8-4c33-9ad3-6cdce7b1c566}')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Media.Core.TimedMetadataTrackError: ...
    @winrt_commethod(7)
    def get_Tracks(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.TimedMetadataTrack]: ...
    Error = property(get_Error, None)
    Tracks = property(get_Tracks, None)
class ITimedTextSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceStatics'
    _iid_ = Guid('{7e311853-9aba-4ac4-bb98-2fb176c3bfdd}')
    @winrt_commethod(6)
    def CreateFromStream(self, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(7)
    def CreateFromUri(self, uri: Windows.Foundation.Uri) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(8)
    def CreateFromStreamWithLanguage(self, stream: Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(9)
    def CreateFromUriWithLanguage(self, uri: Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
class ITimedTextSourceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceStatics2'
    _iid_ = Guid('{b66b7602-923e-43fa-9633-587075812db5}')
    @winrt_commethod(6)
    def CreateFromStreamWithIndex(self, stream: Windows.Storage.Streams.IRandomAccessStream, indexStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(7)
    def CreateFromUriWithIndex(self, uri: Windows.Foundation.Uri, indexUri: Windows.Foundation.Uri) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(8)
    def CreateFromStreamWithIndexAndLanguage(self, stream: Windows.Storage.Streams.IRandomAccessStream, indexStream: Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(9)
    def CreateFromUriWithIndexAndLanguage(self, uri: Windows.Foundation.Uri, indexUri: Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
class ITimedTextStyle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextStyle'
    _iid_ = Guid('{1bb2384d-a825-40c2-a7f5-281eaedf3b55}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_FontFamily(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_FontFamily(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_FontSize(self) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(11)
    def put_FontSize(self, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(12)
    def get_FontWeight(self) -> Windows.Media.Core.TimedTextWeight: ...
    @winrt_commethod(13)
    def put_FontWeight(self, value: Windows.Media.Core.TimedTextWeight) -> Void: ...
    @winrt_commethod(14)
    def get_Foreground(self) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_Foreground(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(16)
    def get_Background(self) -> Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_Background(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_IsBackgroundAlwaysShown(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsBackgroundAlwaysShown(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_FlowDirection(self) -> Windows.Media.Core.TimedTextFlowDirection: ...
    @winrt_commethod(21)
    def put_FlowDirection(self, value: Windows.Media.Core.TimedTextFlowDirection) -> Void: ...
    @winrt_commethod(22)
    def get_LineAlignment(self) -> Windows.Media.Core.TimedTextLineAlignment: ...
    @winrt_commethod(23)
    def put_LineAlignment(self, value: Windows.Media.Core.TimedTextLineAlignment) -> Void: ...
    @winrt_commethod(24)
    def get_OutlineColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(25)
    def put_OutlineColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(26)
    def get_OutlineThickness(self) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(27)
    def put_OutlineThickness(self, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(28)
    def get_OutlineRadius(self) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(29)
    def put_OutlineRadius(self, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    Name = property(get_Name, put_Name)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontWeight = property(get_FontWeight, put_FontWeight)
    Foreground = property(get_Foreground, put_Foreground)
    Background = property(get_Background, put_Background)
    IsBackgroundAlwaysShown = property(get_IsBackgroundAlwaysShown, put_IsBackgroundAlwaysShown)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    LineAlignment = property(get_LineAlignment, put_LineAlignment)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    OutlineThickness = property(get_OutlineThickness, put_OutlineThickness)
    OutlineRadius = property(get_OutlineRadius, put_OutlineRadius)
class ITimedTextStyle2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextStyle2'
    _iid_ = Guid('{655f492d-6111-4787-89cc-686fece57e14}')
    @winrt_commethod(6)
    def get_FontStyle(self) -> Windows.Media.Core.TimedTextFontStyle: ...
    @winrt_commethod(7)
    def put_FontStyle(self, value: Windows.Media.Core.TimedTextFontStyle) -> Void: ...
    @winrt_commethod(8)
    def get_IsUnderlineEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsUnderlineEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsLineThroughEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsLineThroughEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsOverlineEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsOverlineEnabled(self, value: Boolean) -> Void: ...
    FontStyle = property(get_FontStyle, put_FontStyle)
    IsUnderlineEnabled = property(get_IsUnderlineEnabled, put_IsUnderlineEnabled)
    IsLineThroughEnabled = property(get_IsLineThroughEnabled, put_IsLineThroughEnabled)
    IsOverlineEnabled = property(get_IsOverlineEnabled, put_IsOverlineEnabled)
class ITimedTextStyle3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextStyle3'
    _iid_ = Guid('{f803f93b-3e99-595e-bbb7-78a2fa13c270}')
    @winrt_commethod(6)
    def get_Ruby(self) -> Windows.Media.Core.TimedTextRuby: ...
    @winrt_commethod(7)
    def get_Bouten(self) -> Windows.Media.Core.TimedTextBouten: ...
    @winrt_commethod(8)
    def get_IsTextCombined(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsTextCombined(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_FontAngleInDegrees(self) -> Double: ...
    @winrt_commethod(11)
    def put_FontAngleInDegrees(self, value: Double) -> Void: ...
    Ruby = property(get_Ruby, None)
    Bouten = property(get_Bouten, None)
    IsTextCombined = property(get_IsTextCombined, put_IsTextCombined)
    FontAngleInDegrees = property(get_FontAngleInDegrees, put_FontAngleInDegrees)
class ITimedTextSubformat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSubformat'
    _iid_ = Guid('{d713502f-3261-4722-a0c2-b937b2390f14}')
    @winrt_commethod(6)
    def get_StartIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_StartIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Length(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Length(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_SubformatStyle(self) -> Windows.Media.Core.TimedTextStyle: ...
    @winrt_commethod(11)
    def put_SubformatStyle(self, value: Windows.Media.Core.TimedTextStyle) -> Void: ...
    StartIndex = property(get_StartIndex, put_StartIndex)
    Length = property(get_Length, put_Length)
    SubformatStyle = property(get_SubformatStyle, put_SubformatStyle)
class IVideoStabilizationEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStabilizationEffect'
    _iid_ = Guid('{0808a650-9698-4e57-877b-bd7cb2ee0f8a}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_EnabledChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.VideoStabilizationEffect, Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnabledChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetRecommendedStreamConfiguration(self, controller: Windows.Media.Devices.VideoDeviceController, desiredProperties: Windows.Media.MediaProperties.VideoEncodingProperties) -> Windows.Media.Capture.VideoStreamConfiguration: ...
    Enabled = property(get_Enabled, put_Enabled)
class IVideoStabilizationEffectEnabledChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs'
    _iid_ = Guid('{187eff28-67bb-4713-b900-4168da164529}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Media.Core.VideoStabilizationEffectEnabledChangedReason: ...
    Reason = property(get_Reason, None)
class IVideoStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptor'
    _iid_ = Guid('{12ee0d55-9c2b-4440-8057-2c7a90f0cbec}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    EncodingProperties = property(get_EncodingProperties, None)
class IVideoStreamDescriptor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptor2'
    _iid_ = Guid('{8b306e10-453e-4088-832d-c36fa4f94af3}')
    @winrt_commethod(6)
    def Copy(self) -> Windows.Media.Core.VideoStreamDescriptor: ...
class IVideoStreamDescriptorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptorFactory'
    _iid_ = Guid('{494ef6d1-bb75-43d2-9e5e-7b79a3afced4}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: Windows.Media.MediaProperties.VideoEncodingProperties) -> Windows.Media.Core.VideoStreamDescriptor: ...
class IVideoTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrack'
    _iid_ = Guid('{99f3b7f3-e298-4396-bb6a-a51be6a2a20a}')
    @winrt_commethod(6)
    def add_OpenFailed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.VideoTrack, Windows.Media.Core.VideoTrackOpenFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetEncodingProperties(self) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(9)
    def get_PlaybackItem(self) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SupportInfo(self) -> Windows.Media.Core.VideoTrackSupportInfo: ...
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
    SupportInfo = property(get_SupportInfo, None)
class IVideoTrackOpenFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrackOpenFailedEventArgs'
    _iid_ = Guid('{7679e231-04f9-4c82-a4ee-8602c8bb4754}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IVideoTrackSupportInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrackSupportInfo'
    _iid_ = Guid('{4bb534a0-fc5f-450d-8ff0-778d590486de}')
    @winrt_commethod(6)
    def get_DecoderStatus(self) -> Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_commethod(7)
    def get_MediaSourceStatus(self) -> Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class ImageCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IImageCue
    _classid_ = 'Windows.Media.Core.ImageCue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.ImageCue: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Core.IImageCue) -> Windows.Media.Core.TimedTextPoint: ...
    @winrt_mixinmethod
    def put_Position(self: Windows.Media.Core.IImageCue, value: Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_mixinmethod
    def get_Extent(self: Windows.Media.Core.IImageCue) -> Windows.Media.Core.TimedTextSize: ...
    @winrt_mixinmethod
    def put_Extent(self: Windows.Media.Core.IImageCue, value: Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_mixinmethod
    def put_SoftwareBitmap(self: Windows.Media.Core.IImageCue, value: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: Windows.Media.Core.IImageCue) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def put_StartTime(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Position = property(get_Position, put_Position)
    Extent = property(get_Extent, put_Extent)
    SoftwareBitmap = property(get_SoftwareBitmap, put_SoftwareBitmap)
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
class InitializeMediaStreamSourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs
    _classid_ = 'Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs'
    @winrt_mixinmethod
    def get_Source(self: Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def get_RandomAccessStream(self: Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Source = property(get_Source, None)
    RandomAccessStream = property(get_RandomAccessStream, None)
class _LowLightFusion_Meta_(ComPtr.__class__):
    pass
class LowLightFusion(ComPtr, metaclass=_LowLightFusion_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.LowLightFusion'
    @winrt_classmethod
    def get_SupportedBitmapPixelFormats(cls: Windows.Media.Core.ILowLightFusionStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def get_MaxSupportedFrameCount(cls: Windows.Media.Core.ILowLightFusionStatics) -> Int32: ...
    @winrt_classmethod
    def FuseAsync(cls: Windows.Media.Core.ILowLightFusionStatics, frameSet: Windows.Foundation.Collections.IIterable[Windows.Graphics.Imaging.SoftwareBitmap]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Core.LowLightFusionResult, Double]: ...
    _LowLightFusion_Meta_.SupportedBitmapPixelFormats = property(get_SupportedBitmapPixelFormats.__wrapped__, None)
    _LowLightFusion_Meta_.MaxSupportedFrameCount = property(get_MaxSupportedFrameCount.__wrapped__, None)
class LowLightFusionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ILowLightFusionResult
    _classid_ = 'Windows.Media.Core.LowLightFusionResult'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Core.ILowLightFusionResult) -> Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Frame = property(get_Frame, None)
class MediaBinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaBinder
    _classid_ = 'Windows.Media.Core.MediaBinder'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.MediaBinder: ...
    @winrt_mixinmethod
    def add_Binding(self: Windows.Media.Core.IMediaBinder, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaBinder, Windows.Media.Core.MediaBindingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Binding(self: Windows.Media.Core.IMediaBinder, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Token(self: Windows.Media.Core.IMediaBinder) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Token(self: Windows.Media.Core.IMediaBinder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Media.Core.IMediaBinder) -> Windows.Media.Core.MediaSource: ...
    Token = property(get_Token, put_Token)
    Source = property(get_Source, None)
class MediaBindingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaBindingEventArgs
    _classid_ = 'Windows.Media.Core.MediaBindingEventArgs'
    @winrt_mixinmethod
    def add_Canceled(self: Windows.Media.Core.IMediaBindingEventArgs, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaBindingEventArgs, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: Windows.Media.Core.IMediaBindingEventArgs, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MediaBinder(self: Windows.Media.Core.IMediaBindingEventArgs) -> Windows.Media.Core.MediaBinder: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Core.IMediaBindingEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def SetUri(self: Windows.Media.Core.IMediaBindingEventArgs, uri: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetStream(self: Windows.Media.Core.IMediaBindingEventArgs, stream: Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetStreamReference(self: Windows.Media.Core.IMediaBindingEventArgs, stream: Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetAdaptiveMediaSource(self: Windows.Media.Core.IMediaBindingEventArgs2, mediaSource: Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Void: ...
    @winrt_mixinmethod
    def SetStorageFile(self: Windows.Media.Core.IMediaBindingEventArgs2, file: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def SetDownloadOperation(self: Windows.Media.Core.IMediaBindingEventArgs3, downloadOperation: Windows.Networking.BackgroundTransfer.DownloadOperation) -> Void: ...
    MediaBinder = property(get_MediaBinder, None)
class MediaCueEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaCueEventArgs
    _classid_ = 'Windows.Media.Core.MediaCueEventArgs'
    @winrt_mixinmethod
    def get_Cue(self: Windows.Media.Core.IMediaCueEventArgs) -> Windows.Media.Core.IMediaCue: ...
    Cue = property(get_Cue, None)
MediaDecoderStatus = Int32
MediaDecoderStatus_FullySupported: MediaDecoderStatus = 0
MediaDecoderStatus_UnsupportedSubtype: MediaDecoderStatus = 1
MediaDecoderStatus_UnsupportedEncoderProperties: MediaDecoderStatus = 2
MediaDecoderStatus_Degraded: MediaDecoderStatus = 3
class MediaSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaSource2
    _classid_ = 'Windows.Media.Core.MediaSource'
    @winrt_mixinmethod
    def add_OpenOperationCompleted(self: Windows.Media.Core.IMediaSource2, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSource, Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenOperationCompleted(self: Windows.Media.Core.IMediaSource2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CustomProperties(self: Windows.Media.Core.IMediaSource2) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaSource2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_IsOpen(self: Windows.Media.Core.IMediaSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExternalTimedTextSources(self: Windows.Media.Core.IMediaSource2) -> Windows.Foundation.Collections.IObservableVector[Windows.Media.Core.TimedTextSource]: ...
    @winrt_mixinmethod
    def get_ExternalTimedMetadataTracks(self: Windows.Media.Core.IMediaSource2) -> Windows.Foundation.Collections.IObservableVector[Windows.Media.Core.TimedMetadataTrack]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Media.Core.IMediaSource3, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSource, Windows.Media.Core.MediaSourceStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Media.Core.IMediaSource3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Media.Core.IMediaSource3) -> Windows.Media.Core.MediaSourceState: ...
    @winrt_mixinmethod
    def Reset(self: Windows.Media.Core.IMediaSource3) -> Void: ...
    @winrt_mixinmethod
    def get_AdaptiveMediaSource(self: Windows.Media.Core.IMediaSource4) -> Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_mixinmethod
    def get_MediaStreamSource(self: Windows.Media.Core.IMediaSource4) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def get_MseStreamSource(self: Windows.Media.Core.IMediaSource4) -> Windows.Media.Core.MseStreamSource: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Media.Core.IMediaSource4) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def OpenAsync(self: Windows.Media.Core.IMediaSource4) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DownloadOperation(self: Windows.Media.Core.IMediaSource5) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_classmethod
    def CreateFromDownloadOperation(cls: Windows.Media.Core.IMediaSourceStatics4, downloadOperation: Windows.Networking.BackgroundTransfer.DownloadOperation) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaFrameSource(cls: Windows.Media.Core.IMediaSourceStatics3, frameSource: Windows.Media.Capture.Frames.MediaFrameSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaBinder(cls: Windows.Media.Core.IMediaSourceStatics2, binder: Windows.Media.Core.MediaBinder) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromAdaptiveMediaSource(cls: Windows.Media.Core.IMediaSourceStatics, mediaSource: Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaStreamSource(cls: Windows.Media.Core.IMediaSourceStatics, mediaSource: Windows.Media.Core.MediaStreamSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMseStreamSource(cls: Windows.Media.Core.IMediaSourceStatics, mediaSource: Windows.Media.Core.MseStreamSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromIMediaSource(cls: Windows.Media.Core.IMediaSourceStatics, mediaSource: Windows.Media.Core.IMediaSource) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStorageFile(cls: Windows.Media.Core.IMediaSourceStatics, file: Windows.Storage.IStorageFile) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStream(cls: Windows.Media.Core.IMediaSourceStatics, stream: Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStreamReference(cls: Windows.Media.Core.IMediaSourceStatics, stream: Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromUri(cls: Windows.Media.Core.IMediaSourceStatics, uri: Windows.Foundation.Uri) -> Windows.Media.Core.MediaSource: ...
    CustomProperties = property(get_CustomProperties, None)
    Duration = property(get_Duration, None)
    IsOpen = property(get_IsOpen, None)
    ExternalTimedTextSources = property(get_ExternalTimedTextSources, None)
    ExternalTimedMetadataTracks = property(get_ExternalTimedMetadataTracks, None)
    State = property(get_State, None)
    AdaptiveMediaSource = property(get_AdaptiveMediaSource, None)
    MediaStreamSource = property(get_MediaStreamSource, None)
    MseStreamSource = property(get_MseStreamSource, None)
    Uri = property(get_Uri, None)
    DownloadOperation = property(get_DownloadOperation, None)
class MediaSourceAppServiceConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaSourceAppServiceConnection
    _classid_ = 'Windows.Media.Core.MediaSourceAppServiceConnection'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Core.IMediaSourceAppServiceConnectionFactory, appServiceConnection: Windows.ApplicationModel.AppService.AppServiceConnection) -> Windows.Media.Core.MediaSourceAppServiceConnection: ...
    @winrt_mixinmethod
    def add_InitializeMediaStreamSourceRequested(self: Windows.Media.Core.IMediaSourceAppServiceConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaSourceAppServiceConnection, Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InitializeMediaStreamSourceRequested(self: Windows.Media.Core.IMediaSourceAppServiceConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Media.Core.IMediaSourceAppServiceConnection) -> Void: ...
class MediaSourceError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaSourceError
    _classid_ = 'Windows.Media.Core.MediaSourceError'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Core.IMediaSourceError) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class MediaSourceOpenOperationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs
    _classid_ = 'Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs) -> Windows.Media.Core.MediaSourceError: ...
    Error = property(get_Error, None)
MediaSourceState = Int32
MediaSourceState_Initial: MediaSourceState = 0
MediaSourceState_Opening: MediaSourceState = 1
MediaSourceState_Opened: MediaSourceState = 2
MediaSourceState_Failed: MediaSourceState = 3
MediaSourceState_Closed: MediaSourceState = 4
class MediaSourceStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaSourceStateChangedEventArgs
    _classid_ = 'Windows.Media.Core.MediaSourceStateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldState(self: Windows.Media.Core.IMediaSourceStateChangedEventArgs) -> Windows.Media.Core.MediaSourceState: ...
    @winrt_mixinmethod
    def get_NewState(self: Windows.Media.Core.IMediaSourceStateChangedEventArgs) -> Windows.Media.Core.MediaSourceState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
MediaSourceStatus = Int32
MediaSourceStatus_FullySupported: MediaSourceStatus = 0
MediaSourceStatus_Unknown: MediaSourceStatus = 1
class MediaStreamSample(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSample
    _classid_ = 'Windows.Media.Core.MediaStreamSample'
    @winrt_mixinmethod
    def add_Processed(self: Windows.Media.Core.IMediaStreamSample, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSample, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Processed(self: Windows.Media.Core.IMediaStreamSample, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Buffer(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Storage.Streams.Buffer: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Media.Core.MediaStreamSamplePropertySet: ...
    @winrt_mixinmethod
    def get_Protection(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Media.Core.MediaStreamSampleProtectionProperties: ...
    @winrt_mixinmethod
    def put_DecodeTimestamp(self: Windows.Media.Core.IMediaStreamSample, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DecodeTimestamp(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaStreamSample, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaStreamSample) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_KeyFrame(self: Windows.Media.Core.IMediaStreamSample, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyFrame(self: Windows.Media.Core.IMediaStreamSample) -> Boolean: ...
    @winrt_mixinmethod
    def put_Discontinuous(self: Windows.Media.Core.IMediaStreamSample, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Discontinuous(self: Windows.Media.Core.IMediaStreamSample) -> Boolean: ...
    @winrt_mixinmethod
    def get_Direct3D11Surface(self: Windows.Media.Core.IMediaStreamSample2) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_classmethod
    def CreateFromDirect3D11Surface(cls: Windows.Media.Core.IMediaStreamSampleStatics2, surface: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, timestamp: Windows.Foundation.TimeSpan) -> Windows.Media.Core.MediaStreamSample: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.Media.Core.IMediaStreamSampleStatics, buffer: Windows.Storage.Streams.IBuffer, timestamp: Windows.Foundation.TimeSpan) -> Windows.Media.Core.MediaStreamSample: ...
    @winrt_classmethod
    def CreateFromStreamAsync(cls: Windows.Media.Core.IMediaStreamSampleStatics, stream: Windows.Storage.Streams.IInputStream, count: UInt32, timestamp: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Media.Core.MediaStreamSample]: ...
    Buffer = property(get_Buffer, None)
    Timestamp = property(get_Timestamp, None)
    ExtendedProperties = property(get_ExtendedProperties, None)
    Protection = property(get_Protection, None)
    DecodeTimestamp = property(get_DecodeTimestamp, put_DecodeTimestamp)
    Duration = property(get_Duration, put_Duration)
    KeyFrame = property(get_KeyFrame, put_KeyFrame)
    Discontinuous = property(get_Discontinuous, put_Discontinuous)
    Direct3D11Surface = property(get_Direct3D11Surface, None)
class MediaStreamSamplePropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]
    _classid_ = 'Windows.Media.Core.MediaStreamSamplePropertySet'
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
class MediaStreamSampleProtectionProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSampleProtectionProperties
    _classid_ = 'Windows.Media.Core.MediaStreamSampleProtectionProperties'
    @winrt_mixinmethod
    def SetKeyIdentifier(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetKeyIdentifier(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_mixinmethod
    def SetInitializationVector(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetInitializationVector(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_mixinmethod
    def SetSubSampleMapping(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def GetSubSampleMapping(self: Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: POINTER(c_char_p_no)) -> Void: ...
class MediaStreamSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSource
    _classid_ = 'Windows.Media.Core.MediaStreamSource'
    @winrt_factorymethod
    def CreateFromDescriptor(cls: Windows.Media.Core.IMediaStreamSourceFactory, descriptor: Windows.Media.Core.IMediaStreamDescriptor) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_factorymethod
    def CreateFromDescriptors(cls: Windows.Media.Core.IMediaStreamSourceFactory, descriptor: Windows.Media.Core.IMediaStreamDescriptor, descriptor2: Windows.Media.Core.IMediaStreamDescriptor) -> Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Media.Core.IMediaStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Media.Core.IMediaStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Starting(self: Windows.Media.Core.IMediaStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Starting(self: Windows.Media.Core.IMediaStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Paused(self: Windows.Media.Core.IMediaStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Paused(self: Windows.Media.Core.IMediaStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SampleRequested(self: Windows.Media.Core.IMediaStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SampleRequested(self: Windows.Media.Core.IMediaStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SwitchStreamsRequested(self: Windows.Media.Core.IMediaStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SwitchStreamsRequested(self: Windows.Media.Core.IMediaStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyError(self: Windows.Media.Core.IMediaStreamSource, errorStatus: Windows.Media.Core.MediaStreamSourceErrorStatus) -> Void: ...
    @winrt_mixinmethod
    def AddStreamDescriptor(self: Windows.Media.Core.IMediaStreamSource, descriptor: Windows.Media.Core.IMediaStreamDescriptor) -> Void: ...
    @winrt_mixinmethod
    def put_MediaProtectionManager(self: Windows.Media.Core.IMediaStreamSource, value: Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_mixinmethod
    def get_MediaProtectionManager(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Media.Protection.MediaProtectionManager: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaStreamSource, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_CanSeek(self: Windows.Media.Core.IMediaStreamSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanSeek(self: Windows.Media.Core.IMediaStreamSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_BufferTime(self: Windows.Media.Core.IMediaStreamSource, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BufferTime(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetBufferedRange(self: Windows.Media.Core.IMediaStreamSource, startOffset: Windows.Foundation.TimeSpan, endOffset: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_MusicProperties(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_mixinmethod
    def get_VideoProperties(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.Media.Core.IMediaStreamSource, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Core.IMediaStreamSource) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def AddProtectionKey(self: Windows.Media.Core.IMediaStreamSource, streamDescriptor: Windows.Media.Core.IMediaStreamDescriptor, keyIdentifier: c_char_p_no, licenseData: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def add_SampleRendered(self: Windows.Media.Core.IMediaStreamSource2, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MediaStreamSource, Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SampleRendered(self: Windows.Media.Core.IMediaStreamSource2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_MaxSupportedPlaybackRate(self: Windows.Media.Core.IMediaStreamSource3, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSupportedPlaybackRate(self: Windows.Media.Core.IMediaStreamSource3) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_IsLive(self: Windows.Media.Core.IMediaStreamSource4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLive(self: Windows.Media.Core.IMediaStreamSource4) -> Boolean: ...
    MediaProtectionManager = property(get_MediaProtectionManager, put_MediaProtectionManager)
    Duration = property(get_Duration, put_Duration)
    CanSeek = property(get_CanSeek, put_CanSeek)
    BufferTime = property(get_BufferTime, put_BufferTime)
    MusicProperties = property(get_MusicProperties, None)
    VideoProperties = property(get_VideoProperties, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    MaxSupportedPlaybackRate = property(get_MaxSupportedPlaybackRate, put_MaxSupportedPlaybackRate)
    IsLive = property(get_IsLive, put_IsLive)
class MediaStreamSourceClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceClosedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceClosedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Media.Core.IMediaStreamSourceClosedEventArgs) -> Windows.Media.Core.MediaStreamSourceClosedRequest: ...
    Request = property(get_Request, None)
MediaStreamSourceClosedReason = Int32
MediaStreamSourceClosedReason_Done: MediaStreamSourceClosedReason = 0
MediaStreamSourceClosedReason_UnknownError: MediaStreamSourceClosedReason = 1
MediaStreamSourceClosedReason_AppReportedError: MediaStreamSourceClosedReason = 2
MediaStreamSourceClosedReason_UnsupportedProtectionSystem: MediaStreamSourceClosedReason = 3
MediaStreamSourceClosedReason_ProtectionSystemFailure: MediaStreamSourceClosedReason = 4
MediaStreamSourceClosedReason_UnsupportedEncodingFormat: MediaStreamSourceClosedReason = 5
MediaStreamSourceClosedReason_MissingSampleRequestedEventHandler: MediaStreamSourceClosedReason = 6
class MediaStreamSourceClosedRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceClosedRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceClosedRequest'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Media.Core.IMediaStreamSourceClosedRequest) -> Windows.Media.Core.MediaStreamSourceClosedReason: ...
    Reason = property(get_Reason, None)
MediaStreamSourceErrorStatus = Int32
MediaStreamSourceErrorStatus_Other: MediaStreamSourceErrorStatus = 0
MediaStreamSourceErrorStatus_OutOfMemory: MediaStreamSourceErrorStatus = 1
MediaStreamSourceErrorStatus_FailedToOpenFile: MediaStreamSourceErrorStatus = 2
MediaStreamSourceErrorStatus_FailedToConnectToServer: MediaStreamSourceErrorStatus = 3
MediaStreamSourceErrorStatus_ConnectionToServerLost: MediaStreamSourceErrorStatus = 4
MediaStreamSourceErrorStatus_UnspecifiedNetworkError: MediaStreamSourceErrorStatus = 5
MediaStreamSourceErrorStatus_DecodeError: MediaStreamSourceErrorStatus = 6
MediaStreamSourceErrorStatus_UnsupportedMediaFormat: MediaStreamSourceErrorStatus = 7
class MediaStreamSourceSampleRenderedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs'
    @winrt_mixinmethod
    def get_SampleLag(self: Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs) -> Windows.Foundation.TimeSpan: ...
    SampleLag = property(get_SampleLag, None)
class MediaStreamSourceSampleRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSampleRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequest'
    @winrt_mixinmethod
    def get_StreamDescriptor(self: Windows.Media.Core.IMediaStreamSourceSampleRequest) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Core.IMediaStreamSourceSampleRequest) -> Windows.Media.Core.MediaStreamSourceSampleRequestDeferral: ...
    @winrt_mixinmethod
    def put_Sample(self: Windows.Media.Core.IMediaStreamSourceSampleRequest, value: Windows.Media.Core.MediaStreamSample) -> Void: ...
    @winrt_mixinmethod
    def get_Sample(self: Windows.Media.Core.IMediaStreamSourceSampleRequest) -> Windows.Media.Core.MediaStreamSample: ...
    @winrt_mixinmethod
    def ReportSampleProgress(self: Windows.Media.Core.IMediaStreamSourceSampleRequest, progress: UInt32) -> Void: ...
    StreamDescriptor = property(get_StreamDescriptor, None)
    Sample = property(get_Sample, put_Sample)
class MediaStreamSourceSampleRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral) -> Void: ...
class MediaStreamSourceSampleRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs) -> Windows.Media.Core.MediaStreamSourceSampleRequest: ...
    Request = property(get_Request, None)
class MediaStreamSourceStartingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceStartingEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Media.Core.IMediaStreamSourceStartingEventArgs) -> Windows.Media.Core.MediaStreamSourceStartingRequest: ...
    Request = property(get_Request, None)
class MediaStreamSourceStartingRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceStartingRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingRequest'
    @winrt_mixinmethod
    def get_StartPosition(self: Windows.Media.Core.IMediaStreamSourceStartingRequest) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Core.IMediaStreamSourceStartingRequest) -> Windows.Media.Core.MediaStreamSourceStartingRequestDeferral: ...
    @winrt_mixinmethod
    def SetActualStartPosition(self: Windows.Media.Core.IMediaStreamSourceStartingRequest, position: Windows.Foundation.TimeSpan) -> Void: ...
    StartPosition = property(get_StartPosition, None)
class MediaStreamSourceStartingRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral) -> Void: ...
class MediaStreamSourceSwitchStreamsRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest'
    @winrt_mixinmethod
    def get_OldStreamDescriptor(self: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def get_NewStreamDescriptor(self: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral: ...
    OldStreamDescriptor = property(get_OldStreamDescriptor, None)
    NewStreamDescriptor = property(get_NewStreamDescriptor, None)
class MediaStreamSourceSwitchStreamsRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral) -> Void: ...
class MediaStreamSourceSwitchStreamsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs) -> Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest: ...
    Request = property(get_Request, None)
MediaTrackKind = Int32
MediaTrackKind_Audio: MediaTrackKind = 0
MediaTrackKind_Video: MediaTrackKind = 1
MediaTrackKind_TimedMetadata: MediaTrackKind = 2
MseAppendMode = Int32
MseAppendMode_Segments: MseAppendMode = 0
MseAppendMode_Sequence: MseAppendMode = 1
MseEndOfStreamStatus = Int32
MseEndOfStreamStatus_Success: MseEndOfStreamStatus = 0
MseEndOfStreamStatus_NetworkError: MseEndOfStreamStatus = 1
MseEndOfStreamStatus_DecodeError: MseEndOfStreamStatus = 2
MseEndOfStreamStatus_UnknownError: MseEndOfStreamStatus = 3
MseReadyState = Int32
MseReadyState_Closed: MseReadyState = 0
MseReadyState_Open: MseReadyState = 1
MseReadyState_Ended: MseReadyState = 2
class MseSourceBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMseSourceBuffer
    _classid_ = 'Windows.Media.Core.MseSourceBuffer'
    @winrt_mixinmethod
    def add_UpdateStarting(self: Windows.Media.Core.IMseSourceBuffer, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateStarting(self: Windows.Media.Core.IMseSourceBuffer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Media.Core.IMseSourceBuffer, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Media.Core.IMseSourceBuffer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateEnded(self: Windows.Media.Core.IMseSourceBuffer, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateEnded(self: Windows.Media.Core.IMseSourceBuffer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: Windows.Media.Core.IMseSourceBuffer, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: Windows.Media.Core.IMseSourceBuffer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Aborted(self: Windows.Media.Core.IMseSourceBuffer, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBuffer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Aborted(self: Windows.Media.Core.IMseSourceBuffer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.Media.Core.IMseSourceBuffer) -> Windows.Media.Core.MseAppendMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.Media.Core.IMseSourceBuffer, value: Windows.Media.Core.MseAppendMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsUpdating(self: Windows.Media.Core.IMseSourceBuffer) -> Boolean: ...
    @winrt_mixinmethod
    def get_Buffered(self: Windows.Media.Core.IMseSourceBuffer) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.MseTimeRange]: ...
    @winrt_mixinmethod
    def get_TimestampOffset(self: Windows.Media.Core.IMseSourceBuffer) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TimestampOffset(self: Windows.Media.Core.IMseSourceBuffer, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AppendWindowStart(self: Windows.Media.Core.IMseSourceBuffer) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AppendWindowStart(self: Windows.Media.Core.IMseSourceBuffer, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AppendWindowEnd(self: Windows.Media.Core.IMseSourceBuffer) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_AppendWindowEnd(self: Windows.Media.Core.IMseSourceBuffer, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def AppendBuffer(self: Windows.Media.Core.IMseSourceBuffer, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def AppendStream(self: Windows.Media.Core.IMseSourceBuffer, stream: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def AppendStreamMaxSize(self: Windows.Media.Core.IMseSourceBuffer, stream: Windows.Storage.Streams.IInputStream, maxSize: UInt64) -> Void: ...
    @winrt_mixinmethod
    def Abort(self: Windows.Media.Core.IMseSourceBuffer) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Media.Core.IMseSourceBuffer, start: Windows.Foundation.TimeSpan, end: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    IsUpdating = property(get_IsUpdating, None)
    Buffered = property(get_Buffered, None)
    TimestampOffset = property(get_TimestampOffset, put_TimestampOffset)
    AppendWindowStart = property(get_AppendWindowStart, put_AppendWindowStart)
    AppendWindowEnd = property(get_AppendWindowEnd, put_AppendWindowEnd)
class MseSourceBufferList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMseSourceBufferList
    _classid_ = 'Windows.Media.Core.MseSourceBufferList'
    @winrt_mixinmethod
    def add_SourceBufferAdded(self: Windows.Media.Core.IMseSourceBufferList, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBufferList, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceBufferAdded(self: Windows.Media.Core.IMseSourceBufferList, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceBufferRemoved(self: Windows.Media.Core.IMseSourceBufferList, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseSourceBufferList, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceBufferRemoved(self: Windows.Media.Core.IMseSourceBufferList, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Buffers(self: Windows.Media.Core.IMseSourceBufferList) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.MseSourceBuffer]: ...
    Buffers = property(get_Buffers, None)
class MseStreamSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMseStreamSource
    _classid_ = 'Windows.Media.Core.MseStreamSource'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.MseStreamSource: ...
    @winrt_mixinmethod
    def add_Opened(self: Windows.Media.Core.IMseStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: Windows.Media.Core.IMseStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Ended(self: Windows.Media.Core.IMseStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Ended(self: Windows.Media.Core.IMseStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Media.Core.IMseStreamSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.MseStreamSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Media.Core.IMseStreamSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SourceBuffers(self: Windows.Media.Core.IMseStreamSource) -> Windows.Media.Core.MseSourceBufferList: ...
    @winrt_mixinmethod
    def get_ActiveSourceBuffers(self: Windows.Media.Core.IMseStreamSource) -> Windows.Media.Core.MseSourceBufferList: ...
    @winrt_mixinmethod
    def get_ReadyState(self: Windows.Media.Core.IMseStreamSource) -> Windows.Media.Core.MseReadyState: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMseStreamSource) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMseStreamSource, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def AddSourceBuffer(self: Windows.Media.Core.IMseStreamSource, mimeType: WinRT_String) -> Windows.Media.Core.MseSourceBuffer: ...
    @winrt_mixinmethod
    def RemoveSourceBuffer(self: Windows.Media.Core.IMseStreamSource, buffer: Windows.Media.Core.MseSourceBuffer) -> Void: ...
    @winrt_mixinmethod
    def EndOfStream(self: Windows.Media.Core.IMseStreamSource, status: Windows.Media.Core.MseEndOfStreamStatus) -> Void: ...
    @winrt_mixinmethod
    def get_LiveSeekableRange(self: Windows.Media.Core.IMseStreamSource2) -> Windows.Foundation.IReference[Windows.Media.Core.MseTimeRange]: ...
    @winrt_mixinmethod
    def put_LiveSeekableRange(self: Windows.Media.Core.IMseStreamSource2, value: Windows.Foundation.IReference[Windows.Media.Core.MseTimeRange]) -> Void: ...
    @winrt_classmethod
    def IsContentTypeSupported(cls: Windows.Media.Core.IMseStreamSourceStatics, contentType: WinRT_String) -> Boolean: ...
    SourceBuffers = property(get_SourceBuffers, None)
    ActiveSourceBuffers = property(get_ActiveSourceBuffers, None)
    ReadyState = property(get_ReadyState, None)
    Duration = property(get_Duration, put_Duration)
    LiveSeekableRange = property(get_LiveSeekableRange, put_LiveSeekableRange)
class MseTimeRange(EasyCastStructure):
    Start: Windows.Foundation.TimeSpan
    End: Windows.Foundation.TimeSpan
class SceneAnalysisEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ISceneAnalysisEffect
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffect'
    @winrt_mixinmethod
    def get_HighDynamicRangeAnalyzer(self: Windows.Media.Core.ISceneAnalysisEffect) -> Windows.Media.Core.HighDynamicRangeControl: ...
    @winrt_mixinmethod
    def put_DesiredAnalysisInterval(self: Windows.Media.Core.ISceneAnalysisEffect, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredAnalysisInterval(self: Windows.Media.Core.ISceneAnalysisEffect) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_SceneAnalyzed(self: Windows.Media.Core.ISceneAnalysisEffect, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.SceneAnalysisEffect, Windows.Media.Core.SceneAnalyzedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SceneAnalyzed(self: Windows.Media.Core.ISceneAnalysisEffect, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetProperties(self: Windows.Media.IMediaExtension, configuration: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    HighDynamicRangeAnalyzer = property(get_HighDynamicRangeAnalyzer, None)
    DesiredAnalysisInterval = property(get_DesiredAnalysisInterval, put_DesiredAnalysisInterval)
class SceneAnalysisEffectDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffectDefinition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.SceneAnalysisEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Effects.IVideoEffectDefinition) -> Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class SceneAnalysisEffectFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ISceneAnalysisEffectFrame
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffectFrame'
    @winrt_mixinmethod
    def get_FrameControlValues(self: Windows.Media.Core.ISceneAnalysisEffectFrame) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_mixinmethod
    def get_HighDynamicRange(self: Windows.Media.Core.ISceneAnalysisEffectFrame) -> Windows.Media.Core.HighDynamicRangeOutput: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.IMediaFrame) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SystemRelativeTime(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.IMediaFrame, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.IMediaFrame) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_IsDiscontinuous(self: Windows.Media.IMediaFrame, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscontinuous(self: Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: Windows.Media.IMediaFrame) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_AnalysisRecommendation(self: Windows.Media.Core.ISceneAnalysisEffectFrame2) -> Windows.Media.Core.SceneAnalysisRecommendation: ...
    FrameControlValues = property(get_FrameControlValues, None)
    HighDynamicRange = property(get_HighDynamicRange, None)
    Type = property(get_Type, None)
    IsReadOnly = property(get_IsReadOnly, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    SystemRelativeTime = property(get_SystemRelativeTime, put_SystemRelativeTime)
    Duration = property(get_Duration, put_Duration)
    IsDiscontinuous = property(get_IsDiscontinuous, put_IsDiscontinuous)
    ExtendedProperties = property(get_ExtendedProperties, None)
    AnalysisRecommendation = property(get_AnalysisRecommendation, None)
SceneAnalysisRecommendation = Int32
SceneAnalysisRecommendation_Standard: SceneAnalysisRecommendation = 0
SceneAnalysisRecommendation_Hdr: SceneAnalysisRecommendation = 1
SceneAnalysisRecommendation_LowLight: SceneAnalysisRecommendation = 2
class SceneAnalyzedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ISceneAnalyzedEventArgs
    _classid_ = 'Windows.Media.Core.SceneAnalyzedEventArgs'
    @winrt_mixinmethod
    def get_ResultFrame(self: Windows.Media.Core.ISceneAnalyzedEventArgs) -> Windows.Media.Core.SceneAnalysisEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class SpeechCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ISpeechCue
    _classid_ = 'Windows.Media.Core.SpeechCue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.SpeechCue: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Core.ISpeechCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.Media.Core.ISpeechCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartPositionInInput(self: Windows.Media.Core.ISpeechCue) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_StartPositionInInput(self: Windows.Media.Core.ISpeechCue, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_EndPositionInInput(self: Windows.Media.Core.ISpeechCue) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_EndPositionInInput(self: Windows.Media.Core.ISpeechCue, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def put_StartTime(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Text = property(get_Text, put_Text)
    StartPositionInInput = property(get_StartPositionInInput, put_StartPositionInInput)
    EndPositionInInput = property(get_EndPositionInInput, put_EndPositionInInput)
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
TimedMetadataKind = Int32
TimedMetadataKind_Caption: TimedMetadataKind = 0
TimedMetadataKind_Chapter: TimedMetadataKind = 1
TimedMetadataKind_Custom: TimedMetadataKind = 2
TimedMetadataKind_Data: TimedMetadataKind = 3
TimedMetadataKind_Description: TimedMetadataKind = 4
TimedMetadataKind_Subtitle: TimedMetadataKind = 5
TimedMetadataKind_ImageSubtitle: TimedMetadataKind = 6
TimedMetadataKind_Speech: TimedMetadataKind = 7
class TimedMetadataStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaStreamDescriptor
    _classid_ = 'Windows.Media.Core.TimedMetadataStreamDescriptor'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Core.ITimedMetadataStreamDescriptorFactory, encodingProperties: Windows.Media.MediaProperties.TimedMetadataEncodingProperties) -> Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: Windows.Media.Core.ITimedMetadataStreamDescriptor) -> Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.Core.ITimedMetadataStreamDescriptor) -> Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    EncodingProperties = property(get_EncodingProperties, None)
    Label = property(get_Label, put_Label)
    IsSelected = property(get_IsSelected, None)
    Name = property(get_Name, put_Name)
    Language = property(get_Language, put_Language)
class TimedMetadataTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedMetadataTrack
    _classid_ = 'Windows.Media.Core.TimedMetadataTrack'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Core.ITimedMetadataTrackFactory, id: WinRT_String, language: WinRT_String, kind: Windows.Media.Core.TimedMetadataKind) -> Windows.Media.Core.TimedMetadataTrack: ...
    @winrt_mixinmethod
    def add_CueEntered(self: Windows.Media.Core.ITimedMetadataTrack, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.MediaCueEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CueEntered(self: Windows.Media.Core.ITimedMetadataTrack, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CueExited(self: Windows.Media.Core.ITimedMetadataTrack, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.MediaCueEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CueExited(self: Windows.Media.Core.ITimedMetadataTrack, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TrackFailed(self: Windows.Media.Core.ITimedMetadataTrack, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedMetadataTrack, Windows.Media.Core.TimedMetadataTrackFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TrackFailed(self: Windows.Media.Core.ITimedMetadataTrack, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Cues(self: Windows.Media.Core.ITimedMetadataTrack) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.IMediaCue]: ...
    @winrt_mixinmethod
    def get_ActiveCues(self: Windows.Media.Core.ITimedMetadataTrack) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.IMediaCue]: ...
    @winrt_mixinmethod
    def get_TimedMetadataKind(self: Windows.Media.Core.ITimedMetadataTrack) -> Windows.Media.Core.TimedMetadataKind: ...
    @winrt_mixinmethod
    def get_DispatchType(self: Windows.Media.Core.ITimedMetadataTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddCue(self: Windows.Media.Core.ITimedMetadataTrack, cue: Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_mixinmethod
    def RemoveCue(self: Windows.Media.Core.ITimedMetadataTrack, cue: Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: Windows.Media.Core.IMediaTrack) -> Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: Windows.Media.Core.ITimedMetadataTrack2) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.ITimedMetadataTrack2) -> WinRT_String: ...
    Cues = property(get_Cues, None)
    ActiveCues = property(get_ActiveCues, None)
    TimedMetadataKind = property(get_TimedMetadataKind, None)
    DispatchType = property(get_DispatchType, None)
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    TrackKind = property(get_TrackKind, None)
    Label = property(get_Label, put_Label)
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
class TimedMetadataTrackError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedMetadataTrackError
    _classid_ = 'Windows.Media.Core.TimedMetadataTrackError'
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Media.Core.ITimedMetadataTrackError) -> Windows.Media.Core.TimedMetadataTrackErrorCode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Core.ITimedMetadataTrackError) -> Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedError = property(get_ExtendedError, None)
TimedMetadataTrackErrorCode = Int32
TimedMetadataTrackErrorCode_None: TimedMetadataTrackErrorCode = 0
TimedMetadataTrackErrorCode_DataFormatError: TimedMetadataTrackErrorCode = 1
TimedMetadataTrackErrorCode_NetworkError: TimedMetadataTrackErrorCode = 2
TimedMetadataTrackErrorCode_InternalError: TimedMetadataTrackErrorCode = 3
class TimedMetadataTrackFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedMetadataTrackFailedEventArgs
    _classid_ = 'Windows.Media.Core.TimedMetadataTrackFailedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Media.Core.ITimedMetadataTrackFailedEventArgs) -> Windows.Media.Core.TimedMetadataTrackError: ...
    Error = property(get_Error, None)
class TimedTextBouten(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextBouten
    _classid_ = 'Windows.Media.Core.TimedTextBouten'
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Core.ITimedTextBouten) -> Windows.Media.Core.TimedTextBoutenType: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.Media.Core.ITimedTextBouten, value: Windows.Media.Core.TimedTextBoutenType) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.Media.Core.ITimedTextBouten) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.Media.Core.ITimedTextBouten, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Core.ITimedTextBouten) -> Windows.Media.Core.TimedTextBoutenPosition: ...
    @winrt_mixinmethod
    def put_Position(self: Windows.Media.Core.ITimedTextBouten, value: Windows.Media.Core.TimedTextBoutenPosition) -> Void: ...
    Type = property(get_Type, put_Type)
    Color = property(get_Color, put_Color)
    Position = property(get_Position, put_Position)
TimedTextBoutenPosition = Int32
TimedTextBoutenPosition_Before: TimedTextBoutenPosition = 0
TimedTextBoutenPosition_After: TimedTextBoutenPosition = 1
TimedTextBoutenPosition_Outside: TimedTextBoutenPosition = 2
TimedTextBoutenType = Int32
TimedTextBoutenType_None: TimedTextBoutenType = 0
TimedTextBoutenType_Auto: TimedTextBoutenType = 1
TimedTextBoutenType_FilledCircle: TimedTextBoutenType = 2
TimedTextBoutenType_OpenCircle: TimedTextBoutenType = 3
TimedTextBoutenType_FilledDot: TimedTextBoutenType = 4
TimedTextBoutenType_OpenDot: TimedTextBoutenType = 5
TimedTextBoutenType_FilledSesame: TimedTextBoutenType = 6
TimedTextBoutenType_OpenSesame: TimedTextBoutenType = 7
class TimedTextCue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextCue
    _classid_ = 'Windows.Media.Core.TimedTextCue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.TimedTextCue: ...
    @winrt_mixinmethod
    def get_CueRegion(self: Windows.Media.Core.ITimedTextCue) -> Windows.Media.Core.TimedTextRegion: ...
    @winrt_mixinmethod
    def put_CueRegion(self: Windows.Media.Core.ITimedTextCue, value: Windows.Media.Core.TimedTextRegion) -> Void: ...
    @winrt_mixinmethod
    def get_CueStyle(self: Windows.Media.Core.ITimedTextCue) -> Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def put_CueStyle(self: Windows.Media.Core.ITimedTextCue, value: Windows.Media.Core.TimedTextStyle) -> Void: ...
    @winrt_mixinmethod
    def get_Lines(self: Windows.Media.Core.ITimedTextCue) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedTextLine]: ...
    @winrt_mixinmethod
    def put_StartTime(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: Windows.Media.Core.IMediaCue, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.Core.IMediaCue) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    CueRegion = property(get_CueRegion, put_CueRegion)
    CueStyle = property(get_CueStyle, put_CueStyle)
    Lines = property(get_Lines, None)
    StartTime = property(get_StartTime, put_StartTime)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
TimedTextDisplayAlignment = Int32
TimedTextDisplayAlignment_Before: TimedTextDisplayAlignment = 0
TimedTextDisplayAlignment_After: TimedTextDisplayAlignment = 1
TimedTextDisplayAlignment_Center: TimedTextDisplayAlignment = 2
class TimedTextDouble(EasyCastStructure):
    Value: Double
    Unit: Windows.Media.Core.TimedTextUnit
TimedTextFlowDirection = Int32
TimedTextFlowDirection_LeftToRight: TimedTextFlowDirection = 0
TimedTextFlowDirection_RightToLeft: TimedTextFlowDirection = 1
TimedTextFontStyle = Int32
TimedTextFontStyle_Normal: TimedTextFontStyle = 0
TimedTextFontStyle_Oblique: TimedTextFontStyle = 1
TimedTextFontStyle_Italic: TimedTextFontStyle = 2
class TimedTextLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextLine
    _classid_ = 'Windows.Media.Core.TimedTextLine'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.TimedTextLine: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Core.ITimedTextLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.Media.Core.ITimedTextLine, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subformats(self: Windows.Media.Core.ITimedTextLine) -> Windows.Foundation.Collections.IVector[Windows.Media.Core.TimedTextSubformat]: ...
    Text = property(get_Text, put_Text)
    Subformats = property(get_Subformats, None)
TimedTextLineAlignment = Int32
TimedTextLineAlignment_Start: TimedTextLineAlignment = 0
TimedTextLineAlignment_End: TimedTextLineAlignment = 1
TimedTextLineAlignment_Center: TimedTextLineAlignment = 2
class TimedTextPadding(EasyCastStructure):
    Before: Double
    After: Double
    Start: Double
    End: Double
    Unit: Windows.Media.Core.TimedTextUnit
class TimedTextPoint(EasyCastStructure):
    X: Double
    Y: Double
    Unit: Windows.Media.Core.TimedTextUnit
class TimedTextRegion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextRegion
    _classid_ = 'Windows.Media.Core.TimedTextRegion'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.TimedTextRegion: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.ITimedTextRegion) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Core.ITimedTextRegion, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextPoint: ...
    @winrt_mixinmethod
    def put_Position(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_mixinmethod
    def get_Extent(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextSize: ...
    @winrt_mixinmethod
    def put_Extent(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_mixinmethod
    def get_Background(self: Windows.Media.Core.ITimedTextRegion) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Background(self: Windows.Media.Core.ITimedTextRegion, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_WritingMode(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextWritingMode: ...
    @winrt_mixinmethod
    def put_WritingMode(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextWritingMode) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayAlignment(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextDisplayAlignment: ...
    @winrt_mixinmethod
    def put_DisplayAlignment(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextDisplayAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_LineHeight(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_LineHeight(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverflowClipped(self: Windows.Media.Core.ITimedTextRegion) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverflowClipped(self: Windows.Media.Core.ITimedTextRegion, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Padding(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextPadding: ...
    @winrt_mixinmethod
    def put_Padding(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextPadding) -> Void: ...
    @winrt_mixinmethod
    def get_TextWrapping(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextWrapping: ...
    @winrt_mixinmethod
    def put_TextWrapping(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextWrapping) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: Windows.Media.Core.ITimedTextRegion) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: Windows.Media.Core.ITimedTextRegion, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ScrollMode(self: Windows.Media.Core.ITimedTextRegion) -> Windows.Media.Core.TimedTextScrollMode: ...
    @winrt_mixinmethod
    def put_ScrollMode(self: Windows.Media.Core.ITimedTextRegion, value: Windows.Media.Core.TimedTextScrollMode) -> Void: ...
    Name = property(get_Name, put_Name)
    Position = property(get_Position, put_Position)
    Extent = property(get_Extent, put_Extent)
    Background = property(get_Background, put_Background)
    WritingMode = property(get_WritingMode, put_WritingMode)
    DisplayAlignment = property(get_DisplayAlignment, put_DisplayAlignment)
    LineHeight = property(get_LineHeight, put_LineHeight)
    IsOverflowClipped = property(get_IsOverflowClipped, put_IsOverflowClipped)
    Padding = property(get_Padding, put_Padding)
    TextWrapping = property(get_TextWrapping, put_TextWrapping)
    ZIndex = property(get_ZIndex, put_ZIndex)
    ScrollMode = property(get_ScrollMode, put_ScrollMode)
class TimedTextRuby(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextRuby
    _classid_ = 'Windows.Media.Core.TimedTextRuby'
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Core.ITimedTextRuby) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.Media.Core.ITimedTextRuby, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Media.Core.ITimedTextRuby) -> Windows.Media.Core.TimedTextRubyPosition: ...
    @winrt_mixinmethod
    def put_Position(self: Windows.Media.Core.ITimedTextRuby, value: Windows.Media.Core.TimedTextRubyPosition) -> Void: ...
    @winrt_mixinmethod
    def get_Align(self: Windows.Media.Core.ITimedTextRuby) -> Windows.Media.Core.TimedTextRubyAlign: ...
    @winrt_mixinmethod
    def put_Align(self: Windows.Media.Core.ITimedTextRuby, value: Windows.Media.Core.TimedTextRubyAlign) -> Void: ...
    @winrt_mixinmethod
    def get_Reserve(self: Windows.Media.Core.ITimedTextRuby) -> Windows.Media.Core.TimedTextRubyReserve: ...
    @winrt_mixinmethod
    def put_Reserve(self: Windows.Media.Core.ITimedTextRuby, value: Windows.Media.Core.TimedTextRubyReserve) -> Void: ...
    Text = property(get_Text, put_Text)
    Position = property(get_Position, put_Position)
    Align = property(get_Align, put_Align)
    Reserve = property(get_Reserve, put_Reserve)
TimedTextRubyAlign = Int32
TimedTextRubyAlign_Center: TimedTextRubyAlign = 0
TimedTextRubyAlign_Start: TimedTextRubyAlign = 1
TimedTextRubyAlign_End: TimedTextRubyAlign = 2
TimedTextRubyAlign_SpaceAround: TimedTextRubyAlign = 3
TimedTextRubyAlign_SpaceBetween: TimedTextRubyAlign = 4
TimedTextRubyAlign_WithBase: TimedTextRubyAlign = 5
TimedTextRubyPosition = Int32
TimedTextRubyPosition_Before: TimedTextRubyPosition = 0
TimedTextRubyPosition_After: TimedTextRubyPosition = 1
TimedTextRubyPosition_Outside: TimedTextRubyPosition = 2
TimedTextRubyReserve = Int32
TimedTextRubyReserve_None: TimedTextRubyReserve = 0
TimedTextRubyReserve_Before: TimedTextRubyReserve = 1
TimedTextRubyReserve_After: TimedTextRubyReserve = 2
TimedTextRubyReserve_Both: TimedTextRubyReserve = 3
TimedTextRubyReserve_Outside: TimedTextRubyReserve = 4
TimedTextScrollMode = Int32
TimedTextScrollMode_Popon: TimedTextScrollMode = 0
TimedTextScrollMode_Rollup: TimedTextScrollMode = 1
class TimedTextSize(EasyCastStructure):
    Height: Double
    Width: Double
    Unit: Windows.Media.Core.TimedTextUnit
class TimedTextSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextSource
    _classid_ = 'Windows.Media.Core.TimedTextSource'
    @winrt_mixinmethod
    def add_Resolved(self: Windows.Media.Core.ITimedTextSource, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.TimedTextSource, Windows.Media.Core.TimedTextSourceResolveResultEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Resolved(self: Windows.Media.Core.ITimedTextSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromStreamWithIndex(cls: Windows.Media.Core.ITimedTextSourceStatics2, stream: Windows.Storage.Streams.IRandomAccessStream, indexStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithIndex(cls: Windows.Media.Core.ITimedTextSourceStatics2, uri: Windows.Foundation.Uri, indexUri: Windows.Foundation.Uri) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStreamWithIndexAndLanguage(cls: Windows.Media.Core.ITimedTextSourceStatics2, stream: Windows.Storage.Streams.IRandomAccessStream, indexStream: Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithIndexAndLanguage(cls: Windows.Media.Core.ITimedTextSourceStatics2, uri: Windows.Foundation.Uri, indexUri: Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStream(cls: Windows.Media.Core.ITimedTextSourceStatics, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUri(cls: Windows.Media.Core.ITimedTextSourceStatics, uri: Windows.Foundation.Uri) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStreamWithLanguage(cls: Windows.Media.Core.ITimedTextSourceStatics, stream: Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithLanguage(cls: Windows.Media.Core.ITimedTextSourceStatics, uri: Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> Windows.Media.Core.TimedTextSource: ...
class TimedTextSourceResolveResultEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextSourceResolveResultEventArgs
    _classid_ = 'Windows.Media.Core.TimedTextSourceResolveResultEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Media.Core.ITimedTextSourceResolveResultEventArgs) -> Windows.Media.Core.TimedMetadataTrackError: ...
    @winrt_mixinmethod
    def get_Tracks(self: Windows.Media.Core.ITimedTextSourceResolveResultEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.TimedMetadataTrack]: ...
    Error = property(get_Error, None)
    Tracks = property(get_Tracks, None)
class TimedTextStyle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextStyle
    _classid_ = 'Windows.Media.Core.TimedTextStyle'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.ITimedTextStyle) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Core.ITimedTextStyle, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FontFamily(self: Windows.Media.Core.ITimedTextStyle) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FontFamily(self: Windows.Media.Core.ITimedTextStyle, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FontSize(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_FontSize(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_FontWeight(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextWeight: ...
    @winrt_mixinmethod
    def put_FontWeight(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextWeight) -> Void: ...
    @winrt_mixinmethod
    def get_Foreground(self: Windows.Media.Core.ITimedTextStyle) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Foreground(self: Windows.Media.Core.ITimedTextStyle, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Background(self: Windows.Media.Core.ITimedTextStyle) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Background(self: Windows.Media.Core.ITimedTextStyle, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_IsBackgroundAlwaysShown(self: Windows.Media.Core.ITimedTextStyle) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBackgroundAlwaysShown(self: Windows.Media.Core.ITimedTextStyle, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FlowDirection(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextFlowDirection: ...
    @winrt_mixinmethod
    def put_FlowDirection(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextFlowDirection) -> Void: ...
    @winrt_mixinmethod
    def get_LineAlignment(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextLineAlignment: ...
    @winrt_mixinmethod
    def put_LineAlignment(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextLineAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineColor(self: Windows.Media.Core.ITimedTextStyle) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_OutlineColor(self: Windows.Media.Core.ITimedTextStyle, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineThickness(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_OutlineThickness(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineRadius(self: Windows.Media.Core.ITimedTextStyle) -> Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_OutlineRadius(self: Windows.Media.Core.ITimedTextStyle, value: Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_FontStyle(self: Windows.Media.Core.ITimedTextStyle2) -> Windows.Media.Core.TimedTextFontStyle: ...
    @winrt_mixinmethod
    def put_FontStyle(self: Windows.Media.Core.ITimedTextStyle2, value: Windows.Media.Core.TimedTextFontStyle) -> Void: ...
    @winrt_mixinmethod
    def get_IsUnderlineEnabled(self: Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsUnderlineEnabled(self: Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLineThroughEnabled(self: Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLineThroughEnabled(self: Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverlineEnabled(self: Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverlineEnabled(self: Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ruby(self: Windows.Media.Core.ITimedTextStyle3) -> Windows.Media.Core.TimedTextRuby: ...
    @winrt_mixinmethod
    def get_Bouten(self: Windows.Media.Core.ITimedTextStyle3) -> Windows.Media.Core.TimedTextBouten: ...
    @winrt_mixinmethod
    def get_IsTextCombined(self: Windows.Media.Core.ITimedTextStyle3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTextCombined(self: Windows.Media.Core.ITimedTextStyle3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FontAngleInDegrees(self: Windows.Media.Core.ITimedTextStyle3) -> Double: ...
    @winrt_mixinmethod
    def put_FontAngleInDegrees(self: Windows.Media.Core.ITimedTextStyle3, value: Double) -> Void: ...
    Name = property(get_Name, put_Name)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontWeight = property(get_FontWeight, put_FontWeight)
    Foreground = property(get_Foreground, put_Foreground)
    Background = property(get_Background, put_Background)
    IsBackgroundAlwaysShown = property(get_IsBackgroundAlwaysShown, put_IsBackgroundAlwaysShown)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    LineAlignment = property(get_LineAlignment, put_LineAlignment)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    OutlineThickness = property(get_OutlineThickness, put_OutlineThickness)
    OutlineRadius = property(get_OutlineRadius, put_OutlineRadius)
    FontStyle = property(get_FontStyle, put_FontStyle)
    IsUnderlineEnabled = property(get_IsUnderlineEnabled, put_IsUnderlineEnabled)
    IsLineThroughEnabled = property(get_IsLineThroughEnabled, put_IsLineThroughEnabled)
    IsOverlineEnabled = property(get_IsOverlineEnabled, put_IsOverlineEnabled)
    Ruby = property(get_Ruby, None)
    Bouten = property(get_Bouten, None)
    IsTextCombined = property(get_IsTextCombined, put_IsTextCombined)
    FontAngleInDegrees = property(get_FontAngleInDegrees, put_FontAngleInDegrees)
class TimedTextSubformat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.ITimedTextSubformat
    _classid_ = 'Windows.Media.Core.TimedTextSubformat'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.TimedTextSubformat: ...
    @winrt_mixinmethod
    def get_StartIndex(self: Windows.Media.Core.ITimedTextSubformat) -> Int32: ...
    @winrt_mixinmethod
    def put_StartIndex(self: Windows.Media.Core.ITimedTextSubformat, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.Media.Core.ITimedTextSubformat) -> Int32: ...
    @winrt_mixinmethod
    def put_Length(self: Windows.Media.Core.ITimedTextSubformat, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SubformatStyle(self: Windows.Media.Core.ITimedTextSubformat) -> Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def put_SubformatStyle(self: Windows.Media.Core.ITimedTextSubformat, value: Windows.Media.Core.TimedTextStyle) -> Void: ...
    StartIndex = property(get_StartIndex, put_StartIndex)
    Length = property(get_Length, put_Length)
    SubformatStyle = property(get_SubformatStyle, put_SubformatStyle)
TimedTextUnit = Int32
TimedTextUnit_Pixels: TimedTextUnit = 0
TimedTextUnit_Percentage: TimedTextUnit = 1
TimedTextWeight = Int32
TimedTextWeight_Normal: TimedTextWeight = 400
TimedTextWeight_Bold: TimedTextWeight = 700
TimedTextWrapping = Int32
TimedTextWrapping_NoWrap: TimedTextWrapping = 0
TimedTextWrapping_Wrap: TimedTextWrapping = 1
TimedTextWritingMode = Int32
TimedTextWritingMode_LeftRightTopBottom: TimedTextWritingMode = 0
TimedTextWritingMode_RightLeftTopBottom: TimedTextWritingMode = 1
TimedTextWritingMode_TopBottomRightLeft: TimedTextWritingMode = 2
TimedTextWritingMode_TopBottomLeftRight: TimedTextWritingMode = 3
TimedTextWritingMode_LeftRight: TimedTextWritingMode = 4
TimedTextWritingMode_RightLeft: TimedTextWritingMode = 5
TimedTextWritingMode_TopBottom: TimedTextWritingMode = 6
class VideoStabilizationEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IVideoStabilizationEffect
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffect'
    @winrt_mixinmethod
    def put_Enabled(self: Windows.Media.Core.IVideoStabilizationEffect, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Media.Core.IVideoStabilizationEffect) -> Boolean: ...
    @winrt_mixinmethod
    def add_EnabledChanged(self: Windows.Media.Core.IVideoStabilizationEffect, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.VideoStabilizationEffect, Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnabledChanged(self: Windows.Media.Core.IVideoStabilizationEffect, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetRecommendedStreamConfiguration(self: Windows.Media.Core.IVideoStabilizationEffect, controller: Windows.Media.Devices.VideoDeviceController, desiredProperties: Windows.Media.MediaProperties.VideoEncodingProperties) -> Windows.Media.Capture.VideoStreamConfiguration: ...
    @winrt_mixinmethod
    def SetProperties(self: Windows.Media.IMediaExtension, configuration: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
class VideoStabilizationEffectDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffectDefinition'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Core.VideoStabilizationEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.Effects.IVideoEffectDefinition) -> Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class VideoStabilizationEffectEnabledChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs) -> Windows.Media.Core.VideoStabilizationEffectEnabledChangedReason: ...
    Reason = property(get_Reason, None)
VideoStabilizationEffectEnabledChangedReason = Int32
VideoStabilizationEffectEnabledChangedReason_Programmatic: VideoStabilizationEffectEnabledChangedReason = 0
VideoStabilizationEffectEnabledChangedReason_PixelRateTooHigh: VideoStabilizationEffectEnabledChangedReason = 1
VideoStabilizationEffectEnabledChangedReason_RunningSlowly: VideoStabilizationEffectEnabledChangedReason = 2
class VideoStreamDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IVideoStreamDescriptor
    _classid_ = 'Windows.Media.Core.VideoStreamDescriptor'
    @winrt_factorymethod
    def Create(cls: Windows.Media.Core.IVideoStreamDescriptorFactory, encodingProperties: Windows.Media.MediaProperties.VideoEncodingProperties) -> Windows.Media.Core.VideoStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: Windows.Media.Core.IVideoStreamDescriptor) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: Windows.Media.Core.IVideoStreamDescriptor2) -> Windows.Media.Core.VideoStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
    IsSelected = property(get_IsSelected, None)
    Name = property(get_Name, put_Name)
    Language = property(get_Language, put_Language)
    Label = property(get_Label, put_Label)
class VideoTrack(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IMediaTrack
    _classid_ = 'Windows.Media.Core.VideoTrack'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: Windows.Media.Core.IMediaTrack) -> Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: Windows.Media.Core.IVideoTrack, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Core.VideoTrack, Windows.Media.Core.VideoTrackOpenFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: Windows.Media.Core.IVideoTrack, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetEncodingProperties(self: Windows.Media.Core.IVideoTrack) -> Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: Windows.Media.Core.IVideoTrack) -> Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Core.IVideoTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportInfo(self: Windows.Media.Core.IVideoTrack) -> Windows.Media.Core.VideoTrackSupportInfo: ...
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    TrackKind = property(get_TrackKind, None)
    Label = property(get_Label, put_Label)
    PlaybackItem = property(get_PlaybackItem, None)
    Name = property(get_Name, None)
    SupportInfo = property(get_SupportInfo, None)
class VideoTrackOpenFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IVideoTrackOpenFailedEventArgs
    _classid_ = 'Windows.Media.Core.VideoTrackOpenFailedEventArgs'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.Core.IVideoTrackOpenFailedEventArgs) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class VideoTrackSupportInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Core.IVideoTrackSupportInfo
    _classid_ = 'Windows.Media.Core.VideoTrackSupportInfo'
    @winrt_mixinmethod
    def get_DecoderStatus(self: Windows.Media.Core.IVideoTrackSupportInfo) -> Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_mixinmethod
    def get_MediaSourceStatus(self: Windows.Media.Core.IVideoTrackSupportInfo) -> Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
make_head(_module, 'AudioStreamDescriptor')
make_head(_module, 'AudioTrack')
make_head(_module, 'AudioTrackOpenFailedEventArgs')
make_head(_module, 'AudioTrackSupportInfo')
make_head(_module, 'ChapterCue')
make_head(_module, 'CodecInfo')
make_head(_module, 'CodecQuery')
make_head(_module, 'CodecSubtypes')
make_head(_module, 'DataCue')
make_head(_module, 'FaceDetectedEventArgs')
make_head(_module, 'FaceDetectionEffect')
make_head(_module, 'FaceDetectionEffectDefinition')
make_head(_module, 'FaceDetectionEffectFrame')
make_head(_module, 'HighDynamicRangeControl')
make_head(_module, 'HighDynamicRangeOutput')
make_head(_module, 'IAudioStreamDescriptor')
make_head(_module, 'IAudioStreamDescriptor2')
make_head(_module, 'IAudioStreamDescriptor3')
make_head(_module, 'IAudioStreamDescriptorFactory')
make_head(_module, 'IAudioTrack')
make_head(_module, 'IAudioTrackOpenFailedEventArgs')
make_head(_module, 'IAudioTrackSupportInfo')
make_head(_module, 'IChapterCue')
make_head(_module, 'ICodecInfo')
make_head(_module, 'ICodecQuery')
make_head(_module, 'ICodecSubtypesStatics')
make_head(_module, 'IDataCue')
make_head(_module, 'IDataCue2')
make_head(_module, 'IFaceDetectedEventArgs')
make_head(_module, 'IFaceDetectionEffect')
make_head(_module, 'IFaceDetectionEffectDefinition')
make_head(_module, 'IFaceDetectionEffectFrame')
make_head(_module, 'IHighDynamicRangeControl')
make_head(_module, 'IHighDynamicRangeOutput')
make_head(_module, 'IImageCue')
make_head(_module, 'IInitializeMediaStreamSourceRequestedEventArgs')
make_head(_module, 'ILowLightFusionResult')
make_head(_module, 'ILowLightFusionStatics')
make_head(_module, 'IMediaBinder')
make_head(_module, 'IMediaBindingEventArgs')
make_head(_module, 'IMediaBindingEventArgs2')
make_head(_module, 'IMediaBindingEventArgs3')
make_head(_module, 'IMediaCue')
make_head(_module, 'IMediaCueEventArgs')
make_head(_module, 'IMediaSource')
make_head(_module, 'IMediaSource2')
make_head(_module, 'IMediaSource3')
make_head(_module, 'IMediaSource4')
make_head(_module, 'IMediaSource5')
make_head(_module, 'IMediaSourceAppServiceConnection')
make_head(_module, 'IMediaSourceAppServiceConnectionFactory')
make_head(_module, 'IMediaSourceError')
make_head(_module, 'IMediaSourceOpenOperationCompletedEventArgs')
make_head(_module, 'IMediaSourceStateChangedEventArgs')
make_head(_module, 'IMediaSourceStatics')
make_head(_module, 'IMediaSourceStatics2')
make_head(_module, 'IMediaSourceStatics3')
make_head(_module, 'IMediaSourceStatics4')
make_head(_module, 'IMediaStreamDescriptor')
make_head(_module, 'IMediaStreamDescriptor2')
make_head(_module, 'IMediaStreamSample')
make_head(_module, 'IMediaStreamSample2')
make_head(_module, 'IMediaStreamSampleProtectionProperties')
make_head(_module, 'IMediaStreamSampleStatics')
make_head(_module, 'IMediaStreamSampleStatics2')
make_head(_module, 'IMediaStreamSource')
make_head(_module, 'IMediaStreamSource2')
make_head(_module, 'IMediaStreamSource3')
make_head(_module, 'IMediaStreamSource4')
make_head(_module, 'IMediaStreamSourceClosedEventArgs')
make_head(_module, 'IMediaStreamSourceClosedRequest')
make_head(_module, 'IMediaStreamSourceFactory')
make_head(_module, 'IMediaStreamSourceSampleRenderedEventArgs')
make_head(_module, 'IMediaStreamSourceSampleRequest')
make_head(_module, 'IMediaStreamSourceSampleRequestDeferral')
make_head(_module, 'IMediaStreamSourceSampleRequestedEventArgs')
make_head(_module, 'IMediaStreamSourceStartingEventArgs')
make_head(_module, 'IMediaStreamSourceStartingRequest')
make_head(_module, 'IMediaStreamSourceStartingRequestDeferral')
make_head(_module, 'IMediaStreamSourceSwitchStreamsRequest')
make_head(_module, 'IMediaStreamSourceSwitchStreamsRequestDeferral')
make_head(_module, 'IMediaStreamSourceSwitchStreamsRequestedEventArgs')
make_head(_module, 'IMediaTrack')
make_head(_module, 'IMseSourceBuffer')
make_head(_module, 'IMseSourceBufferList')
make_head(_module, 'IMseStreamSource')
make_head(_module, 'IMseStreamSource2')
make_head(_module, 'IMseStreamSourceStatics')
make_head(_module, 'ISceneAnalysisEffect')
make_head(_module, 'ISceneAnalysisEffectFrame')
make_head(_module, 'ISceneAnalysisEffectFrame2')
make_head(_module, 'ISceneAnalyzedEventArgs')
make_head(_module, 'ISingleSelectMediaTrackList')
make_head(_module, 'ISpeechCue')
make_head(_module, 'ITimedMetadataStreamDescriptor')
make_head(_module, 'ITimedMetadataStreamDescriptorFactory')
make_head(_module, 'ITimedMetadataTrack')
make_head(_module, 'ITimedMetadataTrack2')
make_head(_module, 'ITimedMetadataTrackError')
make_head(_module, 'ITimedMetadataTrackFactory')
make_head(_module, 'ITimedMetadataTrackFailedEventArgs')
make_head(_module, 'ITimedMetadataTrackProvider')
make_head(_module, 'ITimedTextBouten')
make_head(_module, 'ITimedTextCue')
make_head(_module, 'ITimedTextLine')
make_head(_module, 'ITimedTextRegion')
make_head(_module, 'ITimedTextRuby')
make_head(_module, 'ITimedTextSource')
make_head(_module, 'ITimedTextSourceResolveResultEventArgs')
make_head(_module, 'ITimedTextSourceStatics')
make_head(_module, 'ITimedTextSourceStatics2')
make_head(_module, 'ITimedTextStyle')
make_head(_module, 'ITimedTextStyle2')
make_head(_module, 'ITimedTextStyle3')
make_head(_module, 'ITimedTextSubformat')
make_head(_module, 'IVideoStabilizationEffect')
make_head(_module, 'IVideoStabilizationEffectEnabledChangedEventArgs')
make_head(_module, 'IVideoStreamDescriptor')
make_head(_module, 'IVideoStreamDescriptor2')
make_head(_module, 'IVideoStreamDescriptorFactory')
make_head(_module, 'IVideoTrack')
make_head(_module, 'IVideoTrackOpenFailedEventArgs')
make_head(_module, 'IVideoTrackSupportInfo')
make_head(_module, 'ImageCue')
make_head(_module, 'InitializeMediaStreamSourceRequestedEventArgs')
make_head(_module, 'LowLightFusion')
make_head(_module, 'LowLightFusionResult')
make_head(_module, 'MediaBinder')
make_head(_module, 'MediaBindingEventArgs')
make_head(_module, 'MediaCueEventArgs')
make_head(_module, 'MediaSource')
make_head(_module, 'MediaSourceAppServiceConnection')
make_head(_module, 'MediaSourceError')
make_head(_module, 'MediaSourceOpenOperationCompletedEventArgs')
make_head(_module, 'MediaSourceStateChangedEventArgs')
make_head(_module, 'MediaStreamSample')
make_head(_module, 'MediaStreamSamplePropertySet')
make_head(_module, 'MediaStreamSampleProtectionProperties')
make_head(_module, 'MediaStreamSource')
make_head(_module, 'MediaStreamSourceClosedEventArgs')
make_head(_module, 'MediaStreamSourceClosedRequest')
make_head(_module, 'MediaStreamSourceSampleRenderedEventArgs')
make_head(_module, 'MediaStreamSourceSampleRequest')
make_head(_module, 'MediaStreamSourceSampleRequestDeferral')
make_head(_module, 'MediaStreamSourceSampleRequestedEventArgs')
make_head(_module, 'MediaStreamSourceStartingEventArgs')
make_head(_module, 'MediaStreamSourceStartingRequest')
make_head(_module, 'MediaStreamSourceStartingRequestDeferral')
make_head(_module, 'MediaStreamSourceSwitchStreamsRequest')
make_head(_module, 'MediaStreamSourceSwitchStreamsRequestDeferral')
make_head(_module, 'MediaStreamSourceSwitchStreamsRequestedEventArgs')
make_head(_module, 'MseSourceBuffer')
make_head(_module, 'MseSourceBufferList')
make_head(_module, 'MseStreamSource')
make_head(_module, 'MseTimeRange')
make_head(_module, 'SceneAnalysisEffect')
make_head(_module, 'SceneAnalysisEffectDefinition')
make_head(_module, 'SceneAnalysisEffectFrame')
make_head(_module, 'SceneAnalyzedEventArgs')
make_head(_module, 'SpeechCue')
make_head(_module, 'TimedMetadataStreamDescriptor')
make_head(_module, 'TimedMetadataTrack')
make_head(_module, 'TimedMetadataTrackError')
make_head(_module, 'TimedMetadataTrackFailedEventArgs')
make_head(_module, 'TimedTextBouten')
make_head(_module, 'TimedTextCue')
make_head(_module, 'TimedTextDouble')
make_head(_module, 'TimedTextLine')
make_head(_module, 'TimedTextPadding')
make_head(_module, 'TimedTextPoint')
make_head(_module, 'TimedTextRegion')
make_head(_module, 'TimedTextRuby')
make_head(_module, 'TimedTextSize')
make_head(_module, 'TimedTextSource')
make_head(_module, 'TimedTextSourceResolveResultEventArgs')
make_head(_module, 'TimedTextStyle')
make_head(_module, 'TimedTextSubformat')
make_head(_module, 'VideoStabilizationEffect')
make_head(_module, 'VideoStabilizationEffectDefinition')
make_head(_module, 'VideoStabilizationEffectEnabledChangedEventArgs')
make_head(_module, 'VideoStreamDescriptor')
make_head(_module, 'VideoTrack')
make_head(_module, 'VideoTrackOpenFailedEventArgs')
make_head(_module, 'VideoTrackSupportInfo')
