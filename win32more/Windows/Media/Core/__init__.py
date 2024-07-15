from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Capture.Frames
import win32more.Windows.Media.Core
import win32more.Windows.Media.Devices
import win32more.Windows.Media.Devices.Core
import win32more.Windows.Media.Effects
import win32more.Windows.Media.FaceAnalysis
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Playback
import win32more.Windows.Media.Protection
import win32more.Windows.Media.Streaming.Adaptive
import win32more.Windows.Networking.BackgroundTransfer
import win32more.Windows.Storage
import win32more.Windows.Storage.FileProperties
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class AudioDecoderDegradation(Enum, Int32):
    None_ = 0
    DownmixTo2Channels = 1
    DownmixTo6Channels = 2
    DownmixTo8Channels = 3
class AudioDecoderDegradationReason(Enum, Int32):
    None_ = 0
    LicensingRequirement = 1
    SpatialAudioNotSupported = 2
class AudioStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IAudioStreamDescriptor
    _classid_ = 'Windows.Media.Core.AudioStreamDescriptor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Core.AudioStreamDescriptor.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Core.IAudioStreamDescriptorFactory, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Core.AudioStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Core.IAudioStreamDescriptor) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LeadingEncoderPadding(self: win32more.Windows.Media.Core.IAudioStreamDescriptor2, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_LeadingEncoderPadding(self: win32more.Windows.Media.Core.IAudioStreamDescriptor2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_TrailingEncoderPadding(self: win32more.Windows.Media.Core.IAudioStreamDescriptor2, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_TrailingEncoderPadding(self: win32more.Windows.Media.Core.IAudioStreamDescriptor2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: win32more.Windows.Media.Core.IAudioStreamDescriptor3) -> win32more.Windows.Media.Core.AudioStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
    IsSelected = property(get_IsSelected, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, put_Language)
    LeadingEncoderPadding = property(get_LeadingEncoderPadding, put_LeadingEncoderPadding)
    Name = property(get_Name, put_Name)
    TrailingEncoderPadding = property(get_TrailingEncoderPadding, put_TrailingEncoderPadding)
class AudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaTrack
    _classid_ = 'Windows.Media.Core.AudioTrack'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: win32more.Windows.Media.Core.IMediaTrack) -> win32more.Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: win32more.Windows.Media.Core.IAudioTrack, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.AudioTrack, win32more.Windows.Media.Core.AudioTrackOpenFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: win32more.Windows.Media.Core.IAudioTrack, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetEncodingProperties(self: win32more.Windows.Media.Core.IAudioTrack) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: win32more.Windows.Media.Core.IAudioTrack) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.IAudioTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportInfo(self: win32more.Windows.Media.Core.IAudioTrack) -> win32more.Windows.Media.Core.AudioTrackSupportInfo: ...
    Id = property(get_Id, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, None)
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
    SupportInfo = property(get_SupportInfo, None)
    TrackKind = property(get_TrackKind, None)
    OpenFailed = event()
class AudioTrackOpenFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IAudioTrackOpenFailedEventArgs
    _classid_ = 'Windows.Media.Core.AudioTrackOpenFailedEventArgs'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Core.IAudioTrackOpenFailedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class AudioTrackSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IAudioTrackSupportInfo
    _classid_ = 'Windows.Media.Core.AudioTrackSupportInfo'
    @winrt_mixinmethod
    def get_DecoderStatus(self: win32more.Windows.Media.Core.IAudioTrackSupportInfo) -> win32more.Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_mixinmethod
    def get_Degradation(self: win32more.Windows.Media.Core.IAudioTrackSupportInfo) -> win32more.Windows.Media.Core.AudioDecoderDegradation: ...
    @winrt_mixinmethod
    def get_DegradationReason(self: win32more.Windows.Media.Core.IAudioTrackSupportInfo) -> win32more.Windows.Media.Core.AudioDecoderDegradationReason: ...
    @winrt_mixinmethod
    def get_MediaSourceStatus(self: win32more.Windows.Media.Core.IAudioTrackSupportInfo) -> win32more.Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    Degradation = property(get_Degradation, None)
    DegradationReason = property(get_DegradationReason, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class ChapterCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IChapterCue
    _classid_ = 'Windows.Media.Core.ChapterCue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.ChapterCue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.ChapterCue: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Media.Core.IChapterCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Media.Core.IChapterCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
    StartTime = property(get_StartTime, put_StartTime)
    Title = property(get_Title, put_Title)
class CodecCategory(Enum, Int32):
    Encoder = 0
    Decoder = 1
class CodecInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ICodecInfo
    _classid_ = 'Windows.Media.Core.CodecInfo'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Media.Core.ICodecInfo) -> win32more.Windows.Media.Core.CodecKind: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Media.Core.ICodecInfo) -> win32more.Windows.Media.Core.CodecCategory: ...
    @winrt_mixinmethod
    def get_Subtypes(self: win32more.Windows.Media.Core.ICodecInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Core.ICodecInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsTrusted(self: win32more.Windows.Media.Core.ICodecInfo) -> Boolean: ...
    Category = property(get_Category, None)
    DisplayName = property(get_DisplayName, None)
    IsTrusted = property(get_IsTrusted, None)
    Kind = property(get_Kind, None)
    Subtypes = property(get_Subtypes, None)
class CodecKind(Enum, Int32):
    Audio = 0
    Video = 1
class CodecQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ICodecQuery
    _classid_ = 'Windows.Media.Core.CodecQuery'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.CodecQuery.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.CodecQuery: ...
    @winrt_mixinmethod
    def FindAllAsync(self: win32more.Windows.Media.Core.ICodecQuery, kind: win32more.Windows.Media.Core.CodecKind, category: win32more.Windows.Media.Core.CodecCategory, subType: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.CodecInfo]]: ...
class _CodecSubtypes_Meta_(ComPtr.__class__):
    pass
class CodecSubtypes(ComPtr, metaclass=_CodecSubtypes_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.CodecSubtypes'
    @winrt_classmethod
    def get_VideoFormatDV25(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDV50(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvc(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvh1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvhD(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvsd(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatDvsl(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH263(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH264(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH265(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatH264ES(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatHevc(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatHevcES(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatM4S2(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMjpg(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP43(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP4S(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMP4V(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMpeg2(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatVP80(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatVP90(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMpg1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMss1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatMss2(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv2(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWmv3(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormatWvc1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VideoFormat420O(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAac(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAdts(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAlac(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrNB(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrWB(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatAmrWP(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyAC3(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyAC3Spdif(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDolbyDDPlus(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDrm(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatDts(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatFlac(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatFloat(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMP3(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMPeg(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatMsp1(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatOpus(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatPcm(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWmaSpdif(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioLossless(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioV8(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AudioFormatWMAudioV9(cls: win32more.Windows.Media.Core.ICodecSubtypesStatics) -> WinRT_String: ...
    _CodecSubtypes_Meta_.AudioFormatAac = property(get_AudioFormatAac, None)
    _CodecSubtypes_Meta_.AudioFormatAdts = property(get_AudioFormatAdts, None)
    _CodecSubtypes_Meta_.AudioFormatAlac = property(get_AudioFormatAlac, None)
    _CodecSubtypes_Meta_.AudioFormatAmrNB = property(get_AudioFormatAmrNB, None)
    _CodecSubtypes_Meta_.AudioFormatAmrWB = property(get_AudioFormatAmrWB, None)
    _CodecSubtypes_Meta_.AudioFormatAmrWP = property(get_AudioFormatAmrWP, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyAC3 = property(get_AudioFormatDolbyAC3, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyAC3Spdif = property(get_AudioFormatDolbyAC3Spdif, None)
    _CodecSubtypes_Meta_.AudioFormatDolbyDDPlus = property(get_AudioFormatDolbyDDPlus, None)
    _CodecSubtypes_Meta_.AudioFormatDrm = property(get_AudioFormatDrm, None)
    _CodecSubtypes_Meta_.AudioFormatDts = property(get_AudioFormatDts, None)
    _CodecSubtypes_Meta_.AudioFormatFlac = property(get_AudioFormatFlac, None)
    _CodecSubtypes_Meta_.AudioFormatFloat = property(get_AudioFormatFloat, None)
    _CodecSubtypes_Meta_.AudioFormatMP3 = property(get_AudioFormatMP3, None)
    _CodecSubtypes_Meta_.AudioFormatMPeg = property(get_AudioFormatMPeg, None)
    _CodecSubtypes_Meta_.AudioFormatMsp1 = property(get_AudioFormatMsp1, None)
    _CodecSubtypes_Meta_.AudioFormatOpus = property(get_AudioFormatOpus, None)
    _CodecSubtypes_Meta_.AudioFormatPcm = property(get_AudioFormatPcm, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioLossless = property(get_AudioFormatWMAudioLossless, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioV8 = property(get_AudioFormatWMAudioV8, None)
    _CodecSubtypes_Meta_.AudioFormatWMAudioV9 = property(get_AudioFormatWMAudioV9, None)
    _CodecSubtypes_Meta_.AudioFormatWmaSpdif = property(get_AudioFormatWmaSpdif, None)
    _CodecSubtypes_Meta_.VideoFormat420O = property(get_VideoFormat420O, None)
    _CodecSubtypes_Meta_.VideoFormatDV25 = property(get_VideoFormatDV25, None)
    _CodecSubtypes_Meta_.VideoFormatDV50 = property(get_VideoFormatDV50, None)
    _CodecSubtypes_Meta_.VideoFormatDvc = property(get_VideoFormatDvc, None)
    _CodecSubtypes_Meta_.VideoFormatDvh1 = property(get_VideoFormatDvh1, None)
    _CodecSubtypes_Meta_.VideoFormatDvhD = property(get_VideoFormatDvhD, None)
    _CodecSubtypes_Meta_.VideoFormatDvsd = property(get_VideoFormatDvsd, None)
    _CodecSubtypes_Meta_.VideoFormatDvsl = property(get_VideoFormatDvsl, None)
    _CodecSubtypes_Meta_.VideoFormatH263 = property(get_VideoFormatH263, None)
    _CodecSubtypes_Meta_.VideoFormatH264 = property(get_VideoFormatH264, None)
    _CodecSubtypes_Meta_.VideoFormatH264ES = property(get_VideoFormatH264ES, None)
    _CodecSubtypes_Meta_.VideoFormatH265 = property(get_VideoFormatH265, None)
    _CodecSubtypes_Meta_.VideoFormatHevc = property(get_VideoFormatHevc, None)
    _CodecSubtypes_Meta_.VideoFormatHevcES = property(get_VideoFormatHevcES, None)
    _CodecSubtypes_Meta_.VideoFormatM4S2 = property(get_VideoFormatM4S2, None)
    _CodecSubtypes_Meta_.VideoFormatMP43 = property(get_VideoFormatMP43, None)
    _CodecSubtypes_Meta_.VideoFormatMP4S = property(get_VideoFormatMP4S, None)
    _CodecSubtypes_Meta_.VideoFormatMP4V = property(get_VideoFormatMP4V, None)
    _CodecSubtypes_Meta_.VideoFormatMjpg = property(get_VideoFormatMjpg, None)
    _CodecSubtypes_Meta_.VideoFormatMpeg2 = property(get_VideoFormatMpeg2, None)
    _CodecSubtypes_Meta_.VideoFormatMpg1 = property(get_VideoFormatMpg1, None)
    _CodecSubtypes_Meta_.VideoFormatMss1 = property(get_VideoFormatMss1, None)
    _CodecSubtypes_Meta_.VideoFormatMss2 = property(get_VideoFormatMss2, None)
    _CodecSubtypes_Meta_.VideoFormatVP80 = property(get_VideoFormatVP80, None)
    _CodecSubtypes_Meta_.VideoFormatVP90 = property(get_VideoFormatVP90, None)
    _CodecSubtypes_Meta_.VideoFormatWmv1 = property(get_VideoFormatWmv1, None)
    _CodecSubtypes_Meta_.VideoFormatWmv2 = property(get_VideoFormatWmv2, None)
    _CodecSubtypes_Meta_.VideoFormatWmv3 = property(get_VideoFormatWmv3, None)
    _CodecSubtypes_Meta_.VideoFormatWvc1 = property(get_VideoFormatWvc1, None)
class DataCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IDataCue
    _classid_ = 'Windows.Media.Core.DataCue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.DataCue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.DataCue: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Media.Core.IDataCue, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Media.Core.IDataCue) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Core.IDataCue2) -> win32more.Windows.Foundation.Collections.PropertySet: ...
    Data = property(get_Data, put_Data)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
    Properties = property(get_Properties, None)
    StartTime = property(get_StartTime, put_StartTime)
class FaceDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IFaceDetectedEventArgs
    _classid_ = 'Windows.Media.Core.FaceDetectedEventArgs'
    @winrt_mixinmethod
    def get_ResultFrame(self: win32more.Windows.Media.Core.IFaceDetectedEventArgs) -> win32more.Windows.Media.Core.FaceDetectionEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class FaceDetectionEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IFaceDetectionEffect
    _classid_ = 'Windows.Media.Core.FaceDetectionEffect'
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Core.IFaceDetectionEffect, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Core.IFaceDetectionEffect) -> Boolean: ...
    @winrt_mixinmethod
    def put_DesiredDetectionInterval(self: win32more.Windows.Media.Core.IFaceDetectionEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredDetectionInterval(self: win32more.Windows.Media.Core.IFaceDetectionEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_FaceDetected(self: win32more.Windows.Media.Core.IFaceDetectionEffect, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.FaceDetectionEffect, win32more.Windows.Media.Core.FaceDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FaceDetected(self: win32more.Windows.Media.Core.IFaceDetectionEffect, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetProperties(self: win32more.Windows.Media.IMediaExtension, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    DesiredDetectionInterval = property(get_DesiredDetectionInterval, put_DesiredDetectionInterval)
    Enabled = property(get_Enabled, put_Enabled)
    FaceDetected = event()
class FaceDetectionEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.FaceDetectionEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.FaceDetectionEffectDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.FaceDetectionEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def put_DetectionMode(self: win32more.Windows.Media.Core.IFaceDetectionEffectDefinition, value: win32more.Windows.Media.Core.FaceDetectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_DetectionMode(self: win32more.Windows.Media.Core.IFaceDetectionEffectDefinition) -> win32more.Windows.Media.Core.FaceDetectionMode: ...
    @winrt_mixinmethod
    def put_SynchronousDetectionEnabled(self: win32more.Windows.Media.Core.IFaceDetectionEffectDefinition, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SynchronousDetectionEnabled(self: win32more.Windows.Media.Core.IFaceDetectionEffectDefinition) -> Boolean: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    DetectionMode = property(get_DetectionMode, put_DetectionMode)
    Properties = property(get_Properties, None)
    SynchronousDetectionEnabled = property(get_SynchronousDetectionEnabled, put_SynchronousDetectionEnabled)
class FaceDetectionEffectFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Core.IFaceDetectionEffectFrame
    _classid_ = 'Windows.Media.Core.FaceDetectionEffectFrame'
    @winrt_mixinmethod
    def get_DetectedFaces(self: win32more.Windows.Media.Core.IFaceDetectionEffectFrame) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.FaceAnalysis.DetectedFace]: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.IMediaFrame) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SystemRelativeTime(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_IsDiscontinuous(self: win32more.Windows.Media.IMediaFrame, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscontinuous(self: win32more.Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DetectedFaces = property(get_DetectedFaces, None)
    Duration = property(get_Duration, put_Duration)
    ExtendedProperties = property(get_ExtendedProperties, None)
    IsDiscontinuous = property(get_IsDiscontinuous, put_IsDiscontinuous)
    IsReadOnly = property(get_IsReadOnly, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    SystemRelativeTime = property(get_SystemRelativeTime, put_SystemRelativeTime)
    Type = property(get_Type, None)
class FaceDetectionMode(Enum, Int32):
    HighPerformance = 0
    Balanced = 1
    HighQuality = 2
class HighDynamicRangeControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IHighDynamicRangeControl
    _classid_ = 'Windows.Media.Core.HighDynamicRangeControl'
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Core.IHighDynamicRangeControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Core.IHighDynamicRangeControl) -> Boolean: ...
    Enabled = property(get_Enabled, put_Enabled)
class HighDynamicRangeOutput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IHighDynamicRangeOutput
    _classid_ = 'Windows.Media.Core.HighDynamicRangeOutput'
    @winrt_mixinmethod
    def get_Certainty(self: win32more.Windows.Media.Core.IHighDynamicRangeOutput) -> Double: ...
    @winrt_mixinmethod
    def get_FrameControllers(self: win32more.Windows.Media.Core.IHighDynamicRangeOutput) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.Core.FrameController]: ...
    Certainty = property(get_Certainty, None)
    FrameControllers = property(get_FrameControllers, None)
class IAudioStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor'
    _iid_ = Guid('{1e3692e4-4027-4847-a70b-df1d9a2a7b04}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    EncodingProperties = property(get_EncodingProperties, None)
class IAudioStreamDescriptor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor2'
    _iid_ = Guid('{2e68f1f6-a448-497b-8840-85082665acf9}')
    @winrt_commethod(6)
    def put_LeadingEncoderPadding(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(7)
    def get_LeadingEncoderPadding(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def put_TrailingEncoderPadding(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(9)
    def get_TrailingEncoderPadding(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    LeadingEncoderPadding = property(get_LeadingEncoderPadding, put_LeadingEncoderPadding)
    TrailingEncoderPadding = property(get_TrailingEncoderPadding, put_TrailingEncoderPadding)
class IAudioStreamDescriptor3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptor3'
    _iid_ = Guid('{4d220da1-8e83-44ef-8973-2f63e993f36b}')
    @winrt_commethod(6)
    def Copy(self) -> win32more.Windows.Media.Core.AudioStreamDescriptor: ...
class IAudioStreamDescriptorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioStreamDescriptorFactory'
    _iid_ = Guid('{4a86ce9e-4cb1-4380-8e0c-83504b7f5bf3}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> win32more.Windows.Media.Core.AudioStreamDescriptor: ...
class IAudioTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrack'
    _iid_ = Guid('{f23b6e77-3ef7-40de-b943-068b1321701d}')
    @winrt_commethod(6)
    def add_OpenFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.AudioTrack, win32more.Windows.Media.Core.AudioTrackOpenFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.AudioEncodingProperties: ...
    @winrt_commethod(9)
    def get_PlaybackItem(self) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SupportInfo(self) -> win32more.Windows.Media.Core.AudioTrackSupportInfo: ...
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
    SupportInfo = property(get_SupportInfo, None)
    OpenFailed = event()
class IAudioTrackOpenFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrackOpenFailedEventArgs'
    _iid_ = Guid('{eeddb9b9-bb7c-4112-bf76-9384676f824b}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAudioTrackSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IAudioTrackSupportInfo'
    _iid_ = Guid('{178beff7-cc39-44a6-b951-4a5653f073fa}')
    @winrt_commethod(6)
    def get_DecoderStatus(self) -> win32more.Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_commethod(7)
    def get_Degradation(self) -> win32more.Windows.Media.Core.AudioDecoderDegradation: ...
    @winrt_commethod(8)
    def get_DegradationReason(self) -> win32more.Windows.Media.Core.AudioDecoderDegradationReason: ...
    @winrt_commethod(9)
    def get_MediaSourceStatus(self) -> win32more.Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    Degradation = property(get_Degradation, None)
    DegradationReason = property(get_DegradationReason, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class IChapterCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IChapterCue'
    _iid_ = Guid('{72a98001-d38a-4c0a-8fa6-75cddaf4664c}')
    @winrt_commethod(6)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    Title = property(get_Title, put_Title)
class ICodecInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ICodecInfo'
    _iid_ = Guid('{51e89f85-ea97-499c-86ac-4ce5e73f3a42}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Media.Core.CodecKind: ...
    @winrt_commethod(7)
    def get_Category(self) -> win32more.Windows.Media.Core.CodecCategory: ...
    @winrt_commethod(8)
    def get_Subtypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_IsTrusted(self) -> Boolean: ...
    Category = property(get_Category, None)
    DisplayName = property(get_DisplayName, None)
    IsTrusted = property(get_IsTrusted, None)
    Kind = property(get_Kind, None)
    Subtypes = property(get_Subtypes, None)
class ICodecQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ICodecQuery'
    _iid_ = Guid('{222a953a-af61-4e04-808a-a4634e2f3ac4}')
    @winrt_commethod(6)
    def FindAllAsync(self, kind: win32more.Windows.Media.Core.CodecKind, category: win32more.Windows.Media.Core.CodecCategory, subType: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.CodecInfo]]: ...
class ICodecSubtypesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    AudioFormatWMAudioLossless = property(get_AudioFormatWMAudioLossless, None)
    AudioFormatWMAudioV8 = property(get_AudioFormatWMAudioV8, None)
    AudioFormatWMAudioV9 = property(get_AudioFormatWMAudioV9, None)
    AudioFormatWmaSpdif = property(get_AudioFormatWmaSpdif, None)
    VideoFormat420O = property(get_VideoFormat420O, None)
    VideoFormatDV25 = property(get_VideoFormatDV25, None)
    VideoFormatDV50 = property(get_VideoFormatDV50, None)
    VideoFormatDvc = property(get_VideoFormatDvc, None)
    VideoFormatDvh1 = property(get_VideoFormatDvh1, None)
    VideoFormatDvhD = property(get_VideoFormatDvhD, None)
    VideoFormatDvsd = property(get_VideoFormatDvsd, None)
    VideoFormatDvsl = property(get_VideoFormatDvsl, None)
    VideoFormatH263 = property(get_VideoFormatH263, None)
    VideoFormatH264 = property(get_VideoFormatH264, None)
    VideoFormatH264ES = property(get_VideoFormatH264ES, None)
    VideoFormatH265 = property(get_VideoFormatH265, None)
    VideoFormatHevc = property(get_VideoFormatHevc, None)
    VideoFormatHevcES = property(get_VideoFormatHevcES, None)
    VideoFormatM4S2 = property(get_VideoFormatM4S2, None)
    VideoFormatMP43 = property(get_VideoFormatMP43, None)
    VideoFormatMP4S = property(get_VideoFormatMP4S, None)
    VideoFormatMP4V = property(get_VideoFormatMP4V, None)
    VideoFormatMjpg = property(get_VideoFormatMjpg, None)
    VideoFormatMpeg2 = property(get_VideoFormatMpeg2, None)
    VideoFormatMpg1 = property(get_VideoFormatMpg1, None)
    VideoFormatMss1 = property(get_VideoFormatMss1, None)
    VideoFormatMss2 = property(get_VideoFormatMss2, None)
    VideoFormatVP80 = property(get_VideoFormatVP80, None)
    VideoFormatVP90 = property(get_VideoFormatVP90, None)
    VideoFormatWmv1 = property(get_VideoFormatWmv1, None)
    VideoFormatWmv2 = property(get_VideoFormatWmv2, None)
    VideoFormatWmv3 = property(get_VideoFormatWmv3, None)
    VideoFormatWvc1 = property(get_VideoFormatWvc1, None)
class IDataCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IDataCue'
    _iid_ = Guid('{7c7f676d-1fbc-4e2d-9a87-ee38bd1dc637}')
    @winrt_commethod(6)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, put_Data)
class IDataCue2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IDataCue2'
    _iid_ = Guid('{bc561b15-95f2-49e8-96f1-8dd5dac68d93}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.PropertySet: ...
    Properties = property(get_Properties, None)
class IFaceDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectedEventArgs'
    _iid_ = Guid('{19918426-c65b-46ba-85f8-13880576c90a}')
    @winrt_commethod(6)
    def get_ResultFrame(self) -> win32more.Windows.Media.Core.FaceDetectionEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class IFaceDetectionEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffect'
    _iid_ = Guid('{ae15ebd2-0542-42a9-bc90-f283a29f46c1}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_DesiredDetectionInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_DesiredDetectionInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def add_FaceDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.FaceDetectionEffect, win32more.Windows.Media.Core.FaceDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_FaceDetected(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredDetectionInterval = property(get_DesiredDetectionInterval, put_DesiredDetectionInterval)
    Enabled = property(get_Enabled, put_Enabled)
    FaceDetected = event()
class IFaceDetectionEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffectDefinition'
    _iid_ = Guid('{43dca081-b848-4f33-b702-1fd2624fb016}')
    @winrt_commethod(6)
    def put_DetectionMode(self, value: win32more.Windows.Media.Core.FaceDetectionMode) -> Void: ...
    @winrt_commethod(7)
    def get_DetectionMode(self) -> win32more.Windows.Media.Core.FaceDetectionMode: ...
    @winrt_commethod(8)
    def put_SynchronousDetectionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SynchronousDetectionEnabled(self) -> Boolean: ...
    DetectionMode = property(get_DetectionMode, put_DetectionMode)
    SynchronousDetectionEnabled = property(get_SynchronousDetectionEnabled, put_SynchronousDetectionEnabled)
class IFaceDetectionEffectFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.IFaceDetectionEffectFrame'
    _iid_ = Guid('{8ab08993-5dc8-447b-a247-5270bd802ece}')
    @winrt_commethod(6)
    def get_DetectedFaces(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.FaceAnalysis.DetectedFace]: ...
    DetectedFaces = property(get_DetectedFaces, None)
class IHighDynamicRangeControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IHighDynamicRangeControl'
    _iid_ = Guid('{55f1a7ae-d957-4dc9-9d1c-8553a82a7d99}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    Enabled = property(get_Enabled, put_Enabled)
class IHighDynamicRangeOutput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IHighDynamicRangeOutput'
    _iid_ = Guid('{0f57806b-253b-4119-bb40-3a90e51384f7}')
    @winrt_commethod(6)
    def get_Certainty(self) -> Double: ...
    @winrt_commethod(7)
    def get_FrameControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Devices.Core.FrameController]: ...
    Certainty = property(get_Certainty, None)
    FrameControllers = property(get_FrameControllers, None)
class IImageCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IImageCue'
    _iid_ = Guid('{52828282-367b-440b-9116-3c84570dd270}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Media.Core.TimedTextPoint: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_commethod(8)
    def get_Extent(self) -> win32more.Windows.Media.Core.TimedTextSize: ...
    @winrt_commethod(9)
    def put_Extent(self, value: win32more.Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_commethod(10)
    def put_SoftwareBitmap(self, value: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(11)
    def get_SoftwareBitmap(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    Extent = property(get_Extent, put_Extent)
    Position = property(get_Position, put_Position)
    SoftwareBitmap = property(get_SoftwareBitmap, put_SoftwareBitmap)
class IInitializeMediaStreamSourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs'
    _iid_ = Guid('{25bc45e1-9b08-4c2e-a855-4542f1a75deb}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(7)
    def get_RandomAccessStream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    RandomAccessStream = property(get_RandomAccessStream, None)
    Source = property(get_Source, None)
class ILowLightFusionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ILowLightFusionResult'
    _iid_ = Guid('{78edbe35-27a0-42e0-9cd3-738d2089de9c}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    Frame = property(get_Frame, None)
class ILowLightFusionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ILowLightFusionStatics'
    _iid_ = Guid('{5305016d-c29e-40e2-87a9-9e1fd2f192f5}')
    @winrt_commethod(6)
    def get_SupportedBitmapPixelFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_commethod(7)
    def get_MaxSupportedFrameCount(self) -> Int32: ...
    @winrt_commethod(8)
    def FuseAsync(self, frameSet: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Imaging.SoftwareBitmap]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Core.LowLightFusionResult, Double]: ...
    MaxSupportedFrameCount = property(get_MaxSupportedFrameCount, None)
    SupportedBitmapPixelFormats = property(get_SupportedBitmapPixelFormats, None)
class IMediaBinder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBinder'
    _iid_ = Guid('{2b7e40aa-de07-424f-83f1-f1de46c4fa2e}')
    @winrt_commethod(6)
    def add_Binding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaBinder, win32more.Windows.Media.Core.MediaBindingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Binding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Token(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Token(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Source(self) -> win32more.Windows.Media.Core.MediaSource: ...
    Source = property(get_Source, None)
    Token = property(get_Token, put_Token)
    Binding = event()
class IMediaBindingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs'
    _iid_ = Guid('{b61cb25a-1b6d-4630-a86d-2f0837f712e5}')
    @winrt_commethod(6)
    def add_Canceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaBindingEventArgs, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Canceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_MediaBinder(self) -> win32more.Windows.Media.Core.MediaBinder: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(10)
    def SetUri(self, uri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def SetStream(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def SetStreamReference(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Void: ...
    MediaBinder = property(get_MediaBinder, None)
    Canceled = event()
class IMediaBindingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs2'
    _iid_ = Guid('{0464cceb-bb5a-482f-b8ba-f0284c696567}')
    @winrt_commethod(6)
    def SetAdaptiveMediaSource(self, mediaSource: win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Void: ...
    @winrt_commethod(7)
    def SetStorageFile(self, file: win32more.Windows.Storage.IStorageFile) -> Void: ...
class IMediaBindingEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaBindingEventArgs3'
    _iid_ = Guid('{f8eb475e-19be-44fc-a5ed-7aba315037f9}')
    @winrt_commethod(6)
    def SetDownloadOperation(self, downloadOperation: win32more.Windows.Networking.BackgroundTransfer.DownloadOperation) -> Void: ...
class IMediaCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaCue'
    _iid_ = Guid('{c7d15e5d-59dc-431f-a0ee-27744323b36d}')
    @winrt_commethod(6)
    def put_StartTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Id(self) -> WinRT_String: ...
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
    StartTime = property(get_StartTime, put_StartTime)
class IMediaCueEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaCueEventArgs'
    _iid_ = Guid('{d12f47f7-5fa4-4e68-9fe5-32160dcee57e}')
    @winrt_commethod(6)
    def get_Cue(self) -> win32more.Windows.Media.Core.IMediaCue: ...
    Cue = property(get_Cue, None)
class IMediaSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource'
    _iid_ = Guid('{e7bfb599-a09d-4c21-bcdf-20af4f86b3d9}')
class IMediaSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.IMediaSource2'
    _iid_ = Guid('{2eb61048-655f-4c37-b813-b4e45dfa0abe}')
    @winrt_commethod(6)
    def add_OpenOperationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSource, win32more.Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenOperationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_CustomProperties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_ExternalTimedTextSources(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Media.Core.TimedTextSource]: ...
    @winrt_commethod(12)
    def get_ExternalTimedMetadataTracks(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    CustomProperties = property(get_CustomProperties, None)
    Duration = property(get_Duration, None)
    ExternalTimedMetadataTracks = property(get_ExternalTimedMetadataTracks, None)
    ExternalTimedTextSources = property(get_ExternalTimedTextSources, None)
    IsOpen = property(get_IsOpen, None)
    OpenOperationCompleted = event()
class IMediaSource3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.IMediaSource3'
    _iid_ = Guid('{b59f0d9b-4b6e-41ed-bbb4-7c7509a994ad}')
    @winrt_commethod(6)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSource, win32more.Windows.Media.Core.MediaSourceStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Media.Core.MediaSourceState: ...
    @winrt_commethod(9)
    def Reset(self) -> Void: ...
    State = property(get_State, None)
    StateChanged = event()
class IMediaSource4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.IMediaSource4'
    _iid_ = Guid('{bdafad57-8eff-4c63-85a6-84de0ae3e4f2}')
    @winrt_commethod(6)
    def get_AdaptiveMediaSource(self) -> win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_commethod(7)
    def get_MediaStreamSource(self) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(8)
    def get_MseStreamSource(self) -> win32more.Windows.Media.Core.MseStreamSource: ...
    @winrt_commethod(9)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def OpenAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AdaptiveMediaSource = property(get_AdaptiveMediaSource, None)
    MediaStreamSource = property(get_MediaStreamSource, None)
    MseStreamSource = property(get_MseStreamSource, None)
    Uri = property(get_Uri, None)
class IMediaSource5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSource5'
    _iid_ = Guid('{331a22ae-ed2e-4a22-94c8-b743a92b3022}')
    @winrt_commethod(6)
    def get_DownloadOperation(self) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    DownloadOperation = property(get_DownloadOperation, None)
class IMediaSourceAppServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceAppServiceConnection'
    _iid_ = Guid('{61e1ea97-1916-4810-b7f4-b642be829596}')
    @winrt_commethod(6)
    def add_InitializeMediaStreamSourceRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSourceAppServiceConnection, win32more.Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InitializeMediaStreamSourceRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    InitializeMediaStreamSourceRequested = event()
class IMediaSourceAppServiceConnectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceAppServiceConnectionFactory'
    _iid_ = Guid('{65b912eb-80b9-44f9-9c1e-e120f6d92838}')
    @winrt_commethod(6)
    def Create(self, appServiceConnection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.Media.Core.MediaSourceAppServiceConnection: ...
class IMediaSourceError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceError'
    _iid_ = Guid('{5c0a8965-37c5-4e9d-8d21-1cdee90cecc6}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IMediaSourceOpenOperationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs'
    _iid_ = Guid('{fc682ceb-e281-477c-a8e0-1acd654114c8}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Media.Core.MediaSourceError: ...
    Error = property(get_Error, None)
class IMediaSourceStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStateChangedEventArgs'
    _iid_ = Guid('{0a30af82-9071-4bac-bc39-ca2a93b717a9}')
    @winrt_commethod(6)
    def get_OldState(self) -> win32more.Windows.Media.Core.MediaSourceState: ...
    @winrt_commethod(7)
    def get_NewState(self) -> win32more.Windows.Media.Core.MediaSourceState: ...
    NewState = property(get_NewState, None)
    OldState = property(get_OldState, None)
class IMediaSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics'
    _iid_ = Guid('{f77d6fa4-4652-410e-b1d8-e9a5e245a45c}')
    @winrt_commethod(6)
    def CreateFromAdaptiveMediaSource(self, mediaSource: win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(7)
    def CreateFromMediaStreamSource(self, mediaSource: win32more.Windows.Media.Core.MediaStreamSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(8)
    def CreateFromMseStreamSource(self, mediaSource: win32more.Windows.Media.Core.MseStreamSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(9)
    def CreateFromIMediaSource(self, mediaSource: win32more.Windows.Media.Core.IMediaSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(10)
    def CreateFromStorageFile(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(11)
    def CreateFromStream(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(12)
    def CreateFromStreamReference(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_commethod(13)
    def CreateFromUri(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics2'
    _iid_ = Guid('{eee161a4-7f13-4896-b8cb-df0de5bcb9f1}')
    @winrt_commethod(6)
    def CreateFromMediaBinder(self, binder: win32more.Windows.Media.Core.MediaBinder) -> win32more.Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics3'
    _iid_ = Guid('{453a30d6-2bea-4122-9f73-eace04526e35}')
    @winrt_commethod(6)
    def CreateFromMediaFrameSource(self, frameSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource) -> win32more.Windows.Media.Core.MediaSource: ...
class IMediaSourceStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaSourceStatics4'
    _iid_ = Guid('{281b3bfc-e50a-4428-a500-9c4ed918d3f0}')
    @winrt_commethod(6)
    def CreateFromDownloadOperation(self, downloadOperation: win32more.Windows.Networking.BackgroundTransfer.DownloadOperation) -> win32more.Windows.Media.Core.MediaSource: ...
class IMediaStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    Language = property(get_Language, put_Language)
    Name = property(get_Name, put_Name)
class IMediaStreamDescriptor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamDescriptor2'
    _iid_ = Guid('{5073010f-e8b2-4071-b00b-ebf337a76b58}')
    @winrt_commethod(6)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    Label = property(get_Label, put_Label)
class IMediaStreamSample(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSample'
    _iid_ = Guid('{5c8db627-4b80-4361-9837-6cb7481ad9d6}')
    @winrt_commethod(6)
    def add_Processed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSample, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Processed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Buffer(self) -> win32more.Windows.Storage.Streams.Buffer: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_ExtendedProperties(self) -> win32more.Windows.Media.Core.MediaStreamSamplePropertySet: ...
    @winrt_commethod(11)
    def get_Protection(self) -> win32more.Windows.Media.Core.MediaStreamSampleProtectionProperties: ...
    @winrt_commethod(12)
    def put_DecodeTimestamp(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(13)
    def get_DecodeTimestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(15)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(16)
    def put_KeyFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_KeyFrame(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_Discontinuous(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def get_Discontinuous(self) -> Boolean: ...
    Buffer = property(get_Buffer, None)
    DecodeTimestamp = property(get_DecodeTimestamp, put_DecodeTimestamp)
    Discontinuous = property(get_Discontinuous, put_Discontinuous)
    Duration = property(get_Duration, put_Duration)
    ExtendedProperties = property(get_ExtendedProperties, None)
    KeyFrame = property(get_KeyFrame, put_KeyFrame)
    Protection = property(get_Protection, None)
    Timestamp = property(get_Timestamp, None)
    Processed = event()
class IMediaStreamSample2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSample2'
    _iid_ = Guid('{45078691-fce8-4746-a1c8-10c25d3d7cd3}')
    @winrt_commethod(6)
    def get_Direct3D11Surface(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    Direct3D11Surface = property(get_Direct3D11Surface, None)
class IMediaStreamSampleProtectionProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleProtectionProperties'
    _iid_ = Guid('{4eb88292-ecdf-493e-841d-dd4add7caca2}')
    @winrt_commethod(6)
    def SetKeyIdentifier(self, value: PassArray[Byte]) -> Void: ...
    @winrt_commethod(7)
    def GetKeyIdentifier(self, value: ReceiveArray[Byte]) -> Void: ...
    @winrt_commethod(8)
    def SetInitializationVector(self, value: PassArray[Byte]) -> Void: ...
    @winrt_commethod(9)
    def GetInitializationVector(self, value: ReceiveArray[Byte]) -> Void: ...
    @winrt_commethod(10)
    def SetSubSampleMapping(self, value: PassArray[Byte]) -> Void: ...
    @winrt_commethod(11)
    def GetSubSampleMapping(self, value: ReceiveArray[Byte]) -> Void: ...
class IMediaStreamSampleStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleStatics'
    _iid_ = Guid('{dfdf218f-a6cf-4579-be41-73dd941ad972}')
    @winrt_commethod(6)
    def CreateFromBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Core.MediaStreamSample: ...
    @winrt_commethod(7)
    def CreateFromStreamAsync(self, stream: win32more.Windows.Storage.Streams.IInputStream, count: UInt32, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Core.MediaStreamSample]: ...
class IMediaStreamSampleStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSampleStatics2'
    _iid_ = Guid('{9efe9521-6d46-494c-a2f8-d662922e2dd7}')
    @winrt_commethod(6)
    def CreateFromDirect3D11Surface(self, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Core.MediaStreamSample: ...
class IMediaStreamSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource'
    _iid_ = Guid('{3712d543-45eb-4138-aa62-c01e26f3843f}')
    @winrt_commethod(6)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Starting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Starting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Paused(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Paused(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SampleRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SampleRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SwitchStreamsRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SwitchStreamsRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def NotifyError(self, errorStatus: win32more.Windows.Media.Core.MediaStreamSourceErrorStatus) -> Void: ...
    @winrt_commethod(17)
    def AddStreamDescriptor(self, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> Void: ...
    @winrt_commethod(18)
    def put_MediaProtectionManager(self, value: win32more.Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_commethod(19)
    def get_MediaProtectionManager(self) -> win32more.Windows.Media.Protection.MediaProtectionManager: ...
    @winrt_commethod(20)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(21)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(22)
    def put_CanSeek(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def get_CanSeek(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_BufferTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(25)
    def get_BufferTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(26)
    def SetBufferedRange(self, startOffset: win32more.Windows.Foundation.TimeSpan, endOffset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(27)
    def get_MusicProperties(self) -> win32more.Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_commethod(28)
    def get_VideoProperties(self) -> win32more.Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_commethod(29)
    def put_Thumbnail(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(30)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(31)
    def AddProtectionKey(self, streamDescriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, keyIdentifier: PassArray[Byte], licenseData: PassArray[Byte]) -> Void: ...
    BufferTime = property(get_BufferTime, put_BufferTime)
    CanSeek = property(get_CanSeek, put_CanSeek)
    Duration = property(get_Duration, put_Duration)
    MediaProtectionManager = property(get_MediaProtectionManager, put_MediaProtectionManager)
    MusicProperties = property(get_MusicProperties, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    VideoProperties = property(get_VideoProperties, None)
    Closed = event()
    Starting = event()
    Paused = event()
    SampleRequested = event()
    SwitchStreamsRequested = event()
class IMediaStreamSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource2'
    _iid_ = Guid('{ec55d0ad-2e6a-4f74-adbb-b562d1533849}')
    @winrt_commethod(6)
    def add_SampleRendered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SampleRendered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SampleRendered = event()
class IMediaStreamSource3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource3'
    _iid_ = Guid('{6a2a2746-3ddd-4ddf-a121-94045ecf9440}')
    @winrt_commethod(6)
    def put_MaxSupportedPlaybackRate(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(7)
    def get_MaxSupportedPlaybackRate(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    MaxSupportedPlaybackRate = property(get_MaxSupportedPlaybackRate, put_MaxSupportedPlaybackRate)
class IMediaStreamSource4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSource4'
    _iid_ = Guid('{1d0cfcab-830d-417c-a3a9-2454fd6415c7}')
    @winrt_commethod(6)
    def put_IsLive(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsLive(self) -> Boolean: ...
    IsLive = property(get_IsLive, put_IsLive)
class IMediaStreamSourceClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceClosedEventArgs'
    _iid_ = Guid('{cd8c7eb2-4816-4e24-88f0-491ef7386406}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Media.Core.MediaStreamSourceClosedRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceClosedRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceClosedRequest'
    _iid_ = Guid('{907c00e9-18a3-4951-887a-2c1eebd5c69e}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Media.Core.MediaStreamSourceClosedReason: ...
    Reason = property(get_Reason, None)
class IMediaStreamSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceFactory'
    _iid_ = Guid('{ef77e0d9-d158-4b7a-863f-203342fbfd41}')
    @winrt_commethod(6)
    def CreateFromDescriptor(self, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_commethod(7)
    def CreateFromDescriptors(self, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, descriptor2: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> win32more.Windows.Media.Core.MediaStreamSource: ...
class IMediaStreamSourceSampleRenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs'
    _iid_ = Guid('{9d697b05-d4f2-4c7a-9dfe-8d6cd0b3ee84}')
    @winrt_commethod(6)
    def get_SampleLag(self) -> win32more.Windows.Foundation.TimeSpan: ...
    SampleLag = property(get_SampleLag, None)
class IMediaStreamSourceSampleRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequest'
    _iid_ = Guid('{4db341a9-3501-4d9b-83f9-8f235c822532}')
    @winrt_commethod(6)
    def get_StreamDescriptor(self) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Media.Core.MediaStreamSourceSampleRequestDeferral: ...
    @winrt_commethod(8)
    def put_Sample(self, value: win32more.Windows.Media.Core.MediaStreamSample) -> Void: ...
    @winrt_commethod(9)
    def get_Sample(self) -> win32more.Windows.Media.Core.MediaStreamSample: ...
    @winrt_commethod(10)
    def ReportSampleProgress(self, progress: UInt32) -> Void: ...
    Sample = property(get_Sample, put_Sample)
    StreamDescriptor = property(get_StreamDescriptor, None)
class IMediaStreamSourceSampleRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral'
    _iid_ = Guid('{7895cc02-f982-43c8-9d16-c62d999319be}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSampleRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs'
    _iid_ = Guid('{10f9bb9e-71c5-492f-847f-0da1f35e81f8}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Media.Core.MediaStreamSourceSampleRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingEventArgs'
    _iid_ = Guid('{f41468f2-c274-4940-a5bb-28a572452fa7}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Media.Core.MediaStreamSourceStartingRequest: ...
    Request = property(get_Request, None)
class IMediaStreamSourceStartingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingRequest'
    _iid_ = Guid('{2a9093e4-35c4-4b1b-a791-0d99db56dd1d}')
    @winrt_commethod(6)
    def get_StartPosition(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Media.Core.MediaStreamSourceStartingRequestDeferral: ...
    @winrt_commethod(8)
    def SetActualStartPosition(self, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    StartPosition = property(get_StartPosition, None)
class IMediaStreamSourceStartingRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral'
    _iid_ = Guid('{3f1356a5-6340-4dc4-9910-068ed9f598f8}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSwitchStreamsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest'
    _iid_ = Guid('{41b8808e-38a9-4ec3-9ba0-b69b85501e90}')
    @winrt_commethod(6)
    def get_OldStreamDescriptor(self) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(7)
    def get_NewStreamDescriptor(self) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral: ...
    NewStreamDescriptor = property(get_NewStreamDescriptor, None)
    OldStreamDescriptor = property(get_OldStreamDescriptor, None)
class IMediaStreamSourceSwitchStreamsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral'
    _iid_ = Guid('{bee3d835-a505-4f9a-b943-2b8cb1b4bbd9}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMediaStreamSourceSwitchStreamsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs'
    _iid_ = Guid('{42202b72-6ea1-4677-981e-350a0da412aa}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest: ...
    Request = property(get_Request, None)
class IMediaTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMediaTrack'
    _iid_ = Guid('{03e1fafc-c931-491a-b46b-c10ee8c256b7}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_TrackKind(self) -> win32more.Windows.Media.Core.MediaTrackKind: ...
    @winrt_commethod(9)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Label(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, None)
    TrackKind = property(get_TrackKind, None)
class IMseSourceBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseSourceBuffer'
    _iid_ = Guid('{0c1aa3e3-df8d-4079-a3fe-6849184b4e2f}')
    @winrt_commethod(6)
    def add_UpdateStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UpdateStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_UpdateEnded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UpdateEnded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ErrorOccurred(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ErrorOccurred(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Aborted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Aborted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Mode(self) -> win32more.Windows.Media.Core.MseAppendMode: ...
    @winrt_commethod(17)
    def put_Mode(self, value: win32more.Windows.Media.Core.MseAppendMode) -> Void: ...
    @winrt_commethod(18)
    def get_IsUpdating(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_Buffered(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.MseTimeRange]: ...
    @winrt_commethod(20)
    def get_TimestampOffset(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(21)
    def put_TimestampOffset(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(22)
    def get_AppendWindowStart(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(23)
    def put_AppendWindowStart(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(24)
    def get_AppendWindowEnd(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(25)
    def put_AppendWindowEnd(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(26)
    def AppendBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(27)
    def AppendStream(self, stream: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(28)
    def AppendStreamMaxSize(self, stream: win32more.Windows.Storage.Streams.IInputStream, maxSize: UInt64) -> Void: ...
    @winrt_commethod(29)
    def Abort(self) -> Void: ...
    @winrt_commethod(30)
    def Remove(self, start: win32more.Windows.Foundation.TimeSpan, end: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    AppendWindowEnd = property(get_AppendWindowEnd, put_AppendWindowEnd)
    AppendWindowStart = property(get_AppendWindowStart, put_AppendWindowStart)
    Buffered = property(get_Buffered, None)
    IsUpdating = property(get_IsUpdating, None)
    Mode = property(get_Mode, put_Mode)
    TimestampOffset = property(get_TimestampOffset, put_TimestampOffset)
    UpdateStarting = event()
    Updated = event()
    UpdateEnded = event()
    ErrorOccurred = event()
    Aborted = event()
class IMseSourceBufferList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseSourceBufferList'
    _iid_ = Guid('{95fae8e7-a8e7-4ebf-8927-145e940ba511}')
    @winrt_commethod(6)
    def add_SourceBufferAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBufferList, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceBufferAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceBufferRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBufferList, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceBufferRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Buffers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.MseSourceBuffer]: ...
    Buffers = property(get_Buffers, None)
    SourceBufferAdded = event()
    SourceBufferRemoved = event()
class IMseStreamSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSource'
    _iid_ = Guid('{b0b4198d-02f4-4923-88dd-81bc3f360ffa}')
    @winrt_commethod(6)
    def add_Opened(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Opened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Ended(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Ended(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_SourceBuffers(self) -> win32more.Windows.Media.Core.MseSourceBufferList: ...
    @winrt_commethod(13)
    def get_ActiveSourceBuffers(self) -> win32more.Windows.Media.Core.MseSourceBufferList: ...
    @winrt_commethod(14)
    def get_ReadyState(self) -> win32more.Windows.Media.Core.MseReadyState: ...
    @winrt_commethod(15)
    def get_Duration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(16)
    def put_Duration(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(17)
    def AddSourceBuffer(self, mimeType: WinRT_String) -> win32more.Windows.Media.Core.MseSourceBuffer: ...
    @winrt_commethod(18)
    def RemoveSourceBuffer(self, buffer: win32more.Windows.Media.Core.MseSourceBuffer) -> Void: ...
    @winrt_commethod(19)
    def EndOfStream(self, status: win32more.Windows.Media.Core.MseEndOfStreamStatus) -> Void: ...
    ActiveSourceBuffers = property(get_ActiveSourceBuffers, None)
    Duration = property(get_Duration, put_Duration)
    ReadyState = property(get_ReadyState, None)
    SourceBuffers = property(get_SourceBuffers, None)
    Opened = event()
    Ended = event()
    Closed = event()
class IMseStreamSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSource2'
    _iid_ = Guid('{66f57d37-f9e7-418a-9cde-a020e956552b}')
    @winrt_commethod(6)
    def get_LiveSeekableRange(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Core.MseTimeRange]: ...
    @winrt_commethod(7)
    def put_LiveSeekableRange(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Media.Core.MseTimeRange]) -> Void: ...
    LiveSeekableRange = property(get_LiveSeekableRange, put_LiveSeekableRange)
class IMseStreamSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IMseStreamSourceStatics'
    _iid_ = Guid('{465c679d-d570-43ce-ba21-0bff5f3fbd0a}')
    @winrt_commethod(6)
    def IsContentTypeSupported(self, contentType: WinRT_String) -> Boolean: ...
class ISceneAnalysisEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffect'
    _iid_ = Guid('{c04ba319-ca41-4813-bffd-7b08b0ed2557}')
    @winrt_commethod(6)
    def get_HighDynamicRangeAnalyzer(self) -> win32more.Windows.Media.Core.HighDynamicRangeControl: ...
    @winrt_commethod(7)
    def put_DesiredAnalysisInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_DesiredAnalysisInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def add_SceneAnalyzed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.SceneAnalysisEffect, win32more.Windows.Media.Core.SceneAnalyzedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_SceneAnalyzed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredAnalysisInterval = property(get_DesiredAnalysisInterval, put_DesiredAnalysisInterval)
    HighDynamicRangeAnalyzer = property(get_HighDynamicRangeAnalyzer, None)
    SceneAnalyzed = event()
class ISceneAnalysisEffectFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffectFrame'
    _iid_ = Guid('{d8b10e4c-7fd9-42e1-85eb-6572c297c987}')
    @winrt_commethod(6)
    def get_FrameControlValues(self) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_commethod(7)
    def get_HighDynamicRange(self) -> win32more.Windows.Media.Core.HighDynamicRangeOutput: ...
    FrameControlValues = property(get_FrameControlValues, None)
    HighDynamicRange = property(get_HighDynamicRange, None)
class ISceneAnalysisEffectFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Core.ISceneAnalysisEffectFrame2'
    _iid_ = Guid('{2d4e29be-061f-47ae-9915-02524b5f9a5f}')
    @winrt_commethod(6)
    def get_AnalysisRecommendation(self) -> win32more.Windows.Media.Core.SceneAnalysisRecommendation: ...
    AnalysisRecommendation = property(get_AnalysisRecommendation, None)
class ISceneAnalyzedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISceneAnalyzedEventArgs'
    _iid_ = Guid('{146b9588-2851-45e4-ad55-44cf8df8db4d}')
    @winrt_commethod(6)
    def get_ResultFrame(self) -> win32more.Windows.Media.Core.SceneAnalysisEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class ISingleSelectMediaTrackList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISingleSelectMediaTrackList'
    _iid_ = Guid('{77206f1f-c34f-494f-8077-2bad9ff4ecf1}')
    @winrt_commethod(6)
    def add_SelectedIndexChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.ISingleSelectMediaTrackList, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SelectedIndexChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def put_SelectedIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_SelectedIndex(self) -> Int32: ...
    SelectedIndex = property(get_SelectedIndex, put_SelectedIndex)
    SelectedIndexChanged = event()
class ISpeechCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ISpeechCue'
    _iid_ = Guid('{aee254dc-1725-4bad-8043-a98499b017a2}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_StartPositionInInput(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_StartPositionInInput(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_EndPositionInInput(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_EndPositionInInput(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    EndPositionInInput = property(get_EndPositionInInput, put_EndPositionInInput)
    StartPositionInInput = property(get_StartPositionInInput, put_StartPositionInInput)
    Text = property(get_Text, put_Text)
class ITimedMetadataStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataStreamDescriptor'
    _iid_ = Guid('{133336bf-296a-463e-9ff9-01cd25691408}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_commethod(7)
    def Copy(self) -> win32more.Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
class ITimedMetadataStreamDescriptorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataStreamDescriptorFactory'
    _iid_ = Guid('{c027de30-7362-4ff9-98b1-2dfd0b8d1cae}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: win32more.Windows.Media.MediaProperties.TimedMetadataEncodingProperties) -> win32more.Windows.Media.Core.TimedMetadataStreamDescriptor: ...
class ITimedMetadataTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrack'
    _iid_ = Guid('{9e6aed9e-f67a-49a9-b330-cf03b0e9cf07}')
    @winrt_commethod(6)
    def add_CueEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.MediaCueEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CueEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_CueExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.MediaCueEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CueExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_TrackFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.TimedMetadataTrackFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_TrackFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Cues(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.IMediaCue]: ...
    @winrt_commethod(13)
    def get_ActiveCues(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.IMediaCue]: ...
    @winrt_commethod(14)
    def get_TimedMetadataKind(self) -> win32more.Windows.Media.Core.TimedMetadataKind: ...
    @winrt_commethod(15)
    def get_DispatchType(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def AddCue(self, cue: win32more.Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_commethod(17)
    def RemoveCue(self, cue: win32more.Windows.Media.Core.IMediaCue) -> Void: ...
    ActiveCues = property(get_ActiveCues, None)
    Cues = property(get_Cues, None)
    DispatchType = property(get_DispatchType, None)
    TimedMetadataKind = property(get_TimedMetadataKind, None)
    CueEntered = event()
    CueExited = event()
    TrackFailed = event()
class ITimedMetadataTrack2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrack2'
    _iid_ = Guid('{21b4b648-9f9d-40ba-a8f3-1a92753aef0b}')
    @winrt_commethod(6)
    def get_PlaybackItem(self) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
class ITimedMetadataTrackError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackError'
    _iid_ = Guid('{b3767915-4114-4819-b9d9-dd76089e72f8}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> win32more.Windows.Media.Core.TimedMetadataTrackErrorCode: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedError = property(get_ExtendedError, None)
class ITimedMetadataTrackFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackFactory'
    _iid_ = Guid('{8dd57611-97b3-4e1f-852c-0f482c81ad26}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, language: WinRT_String, kind: win32more.Windows.Media.Core.TimedMetadataKind) -> win32more.Windows.Media.Core.TimedMetadataTrack: ...
class ITimedMetadataTrackFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackFailedEventArgs'
    _iid_ = Guid('{a57fc9d1-6789-4d4d-b07f-84b4f31acb70}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Media.Core.TimedMetadataTrackError: ...
    Error = property(get_Error, None)
class ITimedMetadataTrackProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedMetadataTrackProvider'
    _iid_ = Guid('{3b7f2024-f74e-4ade-93c5-219da05b6856}')
    @winrt_commethod(6)
    def get_TimedMetadataTracks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    TimedMetadataTracks = property(get_TimedMetadataTracks, None)
class ITimedTextBouten(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextBouten'
    _iid_ = Guid('{d9062783-5597-5092-820c-8f738e0f774a}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Media.Core.TimedTextBoutenType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Windows.Media.Core.TimedTextBoutenType) -> Void: ...
    @winrt_commethod(8)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Position(self) -> win32more.Windows.Media.Core.TimedTextBoutenPosition: ...
    @winrt_commethod(11)
    def put_Position(self, value: win32more.Windows.Media.Core.TimedTextBoutenPosition) -> Void: ...
    Color = property(get_Color, put_Color)
    Position = property(get_Position, put_Position)
    Type = property(get_Type, put_Type)
class ITimedTextCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextCue'
    _iid_ = Guid('{51c79e51-3b86-494d-b359-bb2ea7aca9a9}')
    @winrt_commethod(6)
    def get_CueRegion(self) -> win32more.Windows.Media.Core.TimedTextRegion: ...
    @winrt_commethod(7)
    def put_CueRegion(self, value: win32more.Windows.Media.Core.TimedTextRegion) -> Void: ...
    @winrt_commethod(8)
    def get_CueStyle(self) -> win32more.Windows.Media.Core.TimedTextStyle: ...
    @winrt_commethod(9)
    def put_CueStyle(self, value: win32more.Windows.Media.Core.TimedTextStyle) -> Void: ...
    @winrt_commethod(10)
    def get_Lines(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.TimedTextLine]: ...
    CueRegion = property(get_CueRegion, put_CueRegion)
    CueStyle = property(get_CueStyle, put_CueStyle)
    Lines = property(get_Lines, None)
class ITimedTextLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextLine'
    _iid_ = Guid('{978d7ce2-7308-4c66-be50-65777289f5df}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Subformats(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.TimedTextSubformat]: ...
    Subformats = property(get_Subformats, None)
    Text = property(get_Text, put_Text)
class ITimedTextRegion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextRegion'
    _iid_ = Guid('{1ed0881f-8a06-4222-9f59-b21bf40124b4}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Media.Core.TimedTextPoint: ...
    @winrt_commethod(9)
    def put_Position(self, value: win32more.Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_commethod(10)
    def get_Extent(self) -> win32more.Windows.Media.Core.TimedTextSize: ...
    @winrt_commethod(11)
    def put_Extent(self, value: win32more.Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_commethod(12)
    def get_Background(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_Background(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_WritingMode(self) -> win32more.Windows.Media.Core.TimedTextWritingMode: ...
    @winrt_commethod(15)
    def put_WritingMode(self, value: win32more.Windows.Media.Core.TimedTextWritingMode) -> Void: ...
    @winrt_commethod(16)
    def get_DisplayAlignment(self) -> win32more.Windows.Media.Core.TimedTextDisplayAlignment: ...
    @winrt_commethod(17)
    def put_DisplayAlignment(self, value: win32more.Windows.Media.Core.TimedTextDisplayAlignment) -> Void: ...
    @winrt_commethod(18)
    def get_LineHeight(self) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(19)
    def put_LineHeight(self, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(20)
    def get_IsOverflowClipped(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsOverflowClipped(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_Padding(self) -> win32more.Windows.Media.Core.TimedTextPadding: ...
    @winrt_commethod(23)
    def put_Padding(self, value: win32more.Windows.Media.Core.TimedTextPadding) -> Void: ...
    @winrt_commethod(24)
    def get_TextWrapping(self) -> win32more.Windows.Media.Core.TimedTextWrapping: ...
    @winrt_commethod(25)
    def put_TextWrapping(self, value: win32more.Windows.Media.Core.TimedTextWrapping) -> Void: ...
    @winrt_commethod(26)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(27)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(28)
    def get_ScrollMode(self) -> win32more.Windows.Media.Core.TimedTextScrollMode: ...
    @winrt_commethod(29)
    def put_ScrollMode(self, value: win32more.Windows.Media.Core.TimedTextScrollMode) -> Void: ...
    Background = property(get_Background, put_Background)
    DisplayAlignment = property(get_DisplayAlignment, put_DisplayAlignment)
    Extent = property(get_Extent, put_Extent)
    IsOverflowClipped = property(get_IsOverflowClipped, put_IsOverflowClipped)
    LineHeight = property(get_LineHeight, put_LineHeight)
    Name = property(get_Name, put_Name)
    Padding = property(get_Padding, put_Padding)
    Position = property(get_Position, put_Position)
    ScrollMode = property(get_ScrollMode, put_ScrollMode)
    TextWrapping = property(get_TextWrapping, put_TextWrapping)
    WritingMode = property(get_WritingMode, put_WritingMode)
    ZIndex = property(get_ZIndex, put_ZIndex)
class ITimedTextRuby(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextRuby'
    _iid_ = Guid('{10335c29-5b3c-5693-9959-d05a0bd24628}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Media.Core.TimedTextRubyPosition: ...
    @winrt_commethod(9)
    def put_Position(self, value: win32more.Windows.Media.Core.TimedTextRubyPosition) -> Void: ...
    @winrt_commethod(10)
    def get_Align(self) -> win32more.Windows.Media.Core.TimedTextRubyAlign: ...
    @winrt_commethod(11)
    def put_Align(self, value: win32more.Windows.Media.Core.TimedTextRubyAlign) -> Void: ...
    @winrt_commethod(12)
    def get_Reserve(self) -> win32more.Windows.Media.Core.TimedTextRubyReserve: ...
    @winrt_commethod(13)
    def put_Reserve(self, value: win32more.Windows.Media.Core.TimedTextRubyReserve) -> Void: ...
    Align = property(get_Align, put_Align)
    Position = property(get_Position, put_Position)
    Reserve = property(get_Reserve, put_Reserve)
    Text = property(get_Text, put_Text)
class ITimedTextSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSource'
    _iid_ = Guid('{c4ed9ba6-101f-404d-a949-82f33fcd93b7}')
    @winrt_commethod(6)
    def add_Resolved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedTextSource, win32more.Windows.Media.Core.TimedTextSourceResolveResultEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Resolved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Resolved = event()
class ITimedTextSourceResolveResultEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceResolveResultEventArgs'
    _iid_ = Guid('{48907c9c-dcd8-4c33-9ad3-6cdce7b1c566}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Media.Core.TimedMetadataTrackError: ...
    @winrt_commethod(7)
    def get_Tracks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    Error = property(get_Error, None)
    Tracks = property(get_Tracks, None)
class ITimedTextSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceStatics'
    _iid_ = Guid('{7e311853-9aba-4ac4-bb98-2fb176c3bfdd}')
    @winrt_commethod(6)
    def CreateFromStream(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(7)
    def CreateFromUri(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(8)
    def CreateFromStreamWithLanguage(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(9)
    def CreateFromUriWithLanguage(self, uri: win32more.Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
class ITimedTextSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextSourceStatics2'
    _iid_ = Guid('{b66b7602-923e-43fa-9633-587075812db5}')
    @winrt_commethod(6)
    def CreateFromStreamWithIndex(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, indexStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(7)
    def CreateFromUriWithIndex(self, uri: win32more.Windows.Foundation.Uri, indexUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(8)
    def CreateFromStreamWithIndexAndLanguage(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, indexStream: win32more.Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_commethod(9)
    def CreateFromUriWithIndexAndLanguage(self, uri: win32more.Windows.Foundation.Uri, indexUri: win32more.Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
class ITimedTextStyle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_FontSize(self) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(11)
    def put_FontSize(self, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(12)
    def get_FontWeight(self) -> win32more.Windows.Media.Core.TimedTextWeight: ...
    @winrt_commethod(13)
    def put_FontWeight(self, value: win32more.Windows.Media.Core.TimedTextWeight) -> Void: ...
    @winrt_commethod(14)
    def get_Foreground(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_Foreground(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(16)
    def get_Background(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_Background(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_IsBackgroundAlwaysShown(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsBackgroundAlwaysShown(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_FlowDirection(self) -> win32more.Windows.Media.Core.TimedTextFlowDirection: ...
    @winrt_commethod(21)
    def put_FlowDirection(self, value: win32more.Windows.Media.Core.TimedTextFlowDirection) -> Void: ...
    @winrt_commethod(22)
    def get_LineAlignment(self) -> win32more.Windows.Media.Core.TimedTextLineAlignment: ...
    @winrt_commethod(23)
    def put_LineAlignment(self, value: win32more.Windows.Media.Core.TimedTextLineAlignment) -> Void: ...
    @winrt_commethod(24)
    def get_OutlineColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(25)
    def put_OutlineColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(26)
    def get_OutlineThickness(self) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(27)
    def put_OutlineThickness(self, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_commethod(28)
    def get_OutlineRadius(self) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_commethod(29)
    def put_OutlineRadius(self, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    Background = property(get_Background, put_Background)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontWeight = property(get_FontWeight, put_FontWeight)
    Foreground = property(get_Foreground, put_Foreground)
    IsBackgroundAlwaysShown = property(get_IsBackgroundAlwaysShown, put_IsBackgroundAlwaysShown)
    LineAlignment = property(get_LineAlignment, put_LineAlignment)
    Name = property(get_Name, put_Name)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    OutlineRadius = property(get_OutlineRadius, put_OutlineRadius)
    OutlineThickness = property(get_OutlineThickness, put_OutlineThickness)
class ITimedTextStyle2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextStyle2'
    _iid_ = Guid('{655f492d-6111-4787-89cc-686fece57e14}')
    @winrt_commethod(6)
    def get_FontStyle(self) -> win32more.Windows.Media.Core.TimedTextFontStyle: ...
    @winrt_commethod(7)
    def put_FontStyle(self, value: win32more.Windows.Media.Core.TimedTextFontStyle) -> Void: ...
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
    IsLineThroughEnabled = property(get_IsLineThroughEnabled, put_IsLineThroughEnabled)
    IsOverlineEnabled = property(get_IsOverlineEnabled, put_IsOverlineEnabled)
    IsUnderlineEnabled = property(get_IsUnderlineEnabled, put_IsUnderlineEnabled)
class ITimedTextStyle3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.ITimedTextStyle3'
    _iid_ = Guid('{f803f93b-3e99-595e-bbb7-78a2fa13c270}')
    @winrt_commethod(6)
    def get_Ruby(self) -> win32more.Windows.Media.Core.TimedTextRuby: ...
    @winrt_commethod(7)
    def get_Bouten(self) -> win32more.Windows.Media.Core.TimedTextBouten: ...
    @winrt_commethod(8)
    def get_IsTextCombined(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsTextCombined(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_FontAngleInDegrees(self) -> Double: ...
    @winrt_commethod(11)
    def put_FontAngleInDegrees(self, value: Double) -> Void: ...
    Bouten = property(get_Bouten, None)
    FontAngleInDegrees = property(get_FontAngleInDegrees, put_FontAngleInDegrees)
    IsTextCombined = property(get_IsTextCombined, put_IsTextCombined)
    Ruby = property(get_Ruby, None)
class ITimedTextSubformat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_SubformatStyle(self) -> win32more.Windows.Media.Core.TimedTextStyle: ...
    @winrt_commethod(11)
    def put_SubformatStyle(self, value: win32more.Windows.Media.Core.TimedTextStyle) -> Void: ...
    Length = property(get_Length, put_Length)
    StartIndex = property(get_StartIndex, put_StartIndex)
    SubformatStyle = property(get_SubformatStyle, put_SubformatStyle)
class IVideoStabilizationEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStabilizationEffect'
    _iid_ = Guid('{0808a650-9698-4e57-877b-bd7cb2ee0f8a}')
    @winrt_commethod(6)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_EnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.VideoStabilizationEffect, win32more.Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnabledChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetRecommendedStreamConfiguration(self, controller: win32more.Windows.Media.Devices.VideoDeviceController, desiredProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties) -> win32more.Windows.Media.Capture.VideoStreamConfiguration: ...
    Enabled = property(get_Enabled, put_Enabled)
    EnabledChanged = event()
class IVideoStabilizationEffectEnabledChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs'
    _iid_ = Guid('{187eff28-67bb-4713-b900-4168da164529}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Media.Core.VideoStabilizationEffectEnabledChangedReason: ...
    Reason = property(get_Reason, None)
class IVideoStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptor'
    _iid_ = Guid('{12ee0d55-9c2b-4440-8057-2c7a90f0cbec}')
    @winrt_commethod(6)
    def get_EncodingProperties(self) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    EncodingProperties = property(get_EncodingProperties, None)
class IVideoStreamDescriptor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptor2'
    _iid_ = Guid('{8b306e10-453e-4088-832d-c36fa4f94af3}')
    @winrt_commethod(6)
    def Copy(self) -> win32more.Windows.Media.Core.VideoStreamDescriptor: ...
class IVideoStreamDescriptorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoStreamDescriptorFactory'
    _iid_ = Guid('{494ef6d1-bb75-43d2-9e5e-7b79a3afced4}')
    @winrt_commethod(6)
    def Create(self, encodingProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties) -> win32more.Windows.Media.Core.VideoStreamDescriptor: ...
class IVideoTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrack'
    _iid_ = Guid('{99f3b7f3-e298-4396-bb6a-a51be6a2a20a}')
    @winrt_commethod(6)
    def add_OpenFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.VideoTrack, win32more.Windows.Media.Core.VideoTrackOpenFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OpenFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetEncodingProperties(self) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_commethod(9)
    def get_PlaybackItem(self) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SupportInfo(self) -> win32more.Windows.Media.Core.VideoTrackSupportInfo: ...
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
    SupportInfo = property(get_SupportInfo, None)
    OpenFailed = event()
class IVideoTrackOpenFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrackOpenFailedEventArgs'
    _iid_ = Guid('{7679e231-04f9-4c82-a4ee-8602c8bb4754}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IVideoTrackSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.IVideoTrackSupportInfo'
    _iid_ = Guid('{4bb534a0-fc5f-450d-8ff0-778d590486de}')
    @winrt_commethod(6)
    def get_DecoderStatus(self) -> win32more.Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_commethod(7)
    def get_MediaSourceStatus(self) -> win32more.Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)
class ImageCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IImageCue
    _classid_ = 'Windows.Media.Core.ImageCue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.ImageCue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.ImageCue: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Core.IImageCue) -> win32more.Windows.Media.Core.TimedTextPoint: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Core.IImageCue, value: win32more.Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_mixinmethod
    def get_Extent(self: win32more.Windows.Media.Core.IImageCue) -> win32more.Windows.Media.Core.TimedTextSize: ...
    @winrt_mixinmethod
    def put_Extent(self: win32more.Windows.Media.Core.IImageCue, value: win32more.Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_mixinmethod
    def put_SoftwareBitmap(self: win32more.Windows.Media.Core.IImageCue, value: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def get_SoftwareBitmap(self: win32more.Windows.Media.Core.IImageCue) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Duration = property(get_Duration, put_Duration)
    Extent = property(get_Extent, put_Extent)
    Id = property(get_Id, put_Id)
    Position = property(get_Position, put_Position)
    SoftwareBitmap = property(get_SoftwareBitmap, put_SoftwareBitmap)
    StartTime = property(get_StartTime, put_StartTime)
class InitializeMediaStreamSourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs
    _classid_ = 'Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def get_RandomAccessStream(self: win32more.Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Core.IInitializeMediaStreamSourceRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    RandomAccessStream = property(get_RandomAccessStream, None)
    Source = property(get_Source, None)
class _LowLightFusion_Meta_(ComPtr.__class__):
    pass
class LowLightFusion(ComPtr, metaclass=_LowLightFusion_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.LowLightFusion'
    @winrt_classmethod
    def get_SupportedBitmapPixelFormats(cls: win32more.Windows.Media.Core.ILowLightFusionStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Imaging.BitmapPixelFormat]: ...
    @winrt_classmethod
    def get_MaxSupportedFrameCount(cls: win32more.Windows.Media.Core.ILowLightFusionStatics) -> Int32: ...
    @winrt_classmethod
    def FuseAsync(cls: win32more.Windows.Media.Core.ILowLightFusionStatics, frameSet: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Imaging.SoftwareBitmap]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Core.LowLightFusionResult, Double]: ...
    _LowLightFusion_Meta_.MaxSupportedFrameCount = property(get_MaxSupportedFrameCount, None)
    _LowLightFusion_Meta_.SupportedBitmapPixelFormats = property(get_SupportedBitmapPixelFormats, None)
class LowLightFusionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Core.ILowLightFusionResult
    _classid_ = 'Windows.Media.Core.LowLightFusionResult'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Core.ILowLightFusionResult) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Frame = property(get_Frame, None)
class MediaBinder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaBinder
    _classid_ = 'Windows.Media.Core.MediaBinder'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.MediaBinder.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.MediaBinder: ...
    @winrt_mixinmethod
    def add_Binding(self: win32more.Windows.Media.Core.IMediaBinder, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaBinder, win32more.Windows.Media.Core.MediaBindingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Binding(self: win32more.Windows.Media.Core.IMediaBinder, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Token(self: win32more.Windows.Media.Core.IMediaBinder) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Token(self: win32more.Windows.Media.Core.IMediaBinder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Media.Core.IMediaBinder) -> win32more.Windows.Media.Core.MediaSource: ...
    Source = property(get_Source, None)
    Token = property(get_Token, put_Token)
    Binding = event()
class MediaBindingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaBindingEventArgs
    _classid_ = 'Windows.Media.Core.MediaBindingEventArgs'
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Windows.Media.Core.IMediaBindingEventArgs, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaBindingEventArgs, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Windows.Media.Core.IMediaBindingEventArgs, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MediaBinder(self: win32more.Windows.Media.Core.IMediaBindingEventArgs) -> win32more.Windows.Media.Core.MediaBinder: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Core.IMediaBindingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def SetUri(self: win32more.Windows.Media.Core.IMediaBindingEventArgs, uri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetStream(self: win32more.Windows.Media.Core.IMediaBindingEventArgs, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetStreamReference(self: win32more.Windows.Media.Core.IMediaBindingEventArgs, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetAdaptiveMediaSource(self: win32more.Windows.Media.Core.IMediaBindingEventArgs2, mediaSource: win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> Void: ...
    @winrt_mixinmethod
    def SetStorageFile(self: win32more.Windows.Media.Core.IMediaBindingEventArgs2, file: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def SetDownloadOperation(self: win32more.Windows.Media.Core.IMediaBindingEventArgs3, downloadOperation: win32more.Windows.Networking.BackgroundTransfer.DownloadOperation) -> Void: ...
    MediaBinder = property(get_MediaBinder, None)
    Canceled = event()
class MediaCueEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaCueEventArgs
    _classid_ = 'Windows.Media.Core.MediaCueEventArgs'
    @winrt_mixinmethod
    def get_Cue(self: win32more.Windows.Media.Core.IMediaCueEventArgs) -> win32more.Windows.Media.Core.IMediaCue: ...
    Cue = property(get_Cue, None)
class MediaDecoderStatus(Enum, Int32):
    FullySupported = 0
    UnsupportedSubtype = 1
    UnsupportedEncoderProperties = 2
    Degraded = 3
class MediaSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Core.IMediaSource2
    _classid_ = 'Windows.Media.Core.MediaSource'
    @winrt_mixinmethod
    def add_OpenOperationCompleted(self: win32more.Windows.Media.Core.IMediaSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSource, win32more.Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenOperationCompleted(self: win32more.Windows.Media.Core.IMediaSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_CustomProperties(self: win32more.Windows.Media.Core.IMediaSource2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaSource2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Windows.Media.Core.IMediaSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExternalTimedTextSources(self: win32more.Windows.Media.Core.IMediaSource2) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Media.Core.TimedTextSource]: ...
    @winrt_mixinmethod
    def get_ExternalTimedMetadataTracks(self: win32more.Windows.Media.Core.IMediaSource2) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Media.Core.IMediaSource3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSource, win32more.Windows.Media.Core.MediaSourceStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Media.Core.IMediaSource3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Core.IMediaSource3) -> win32more.Windows.Media.Core.MediaSourceState: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Media.Core.IMediaSource3) -> Void: ...
    @winrt_mixinmethod
    def get_AdaptiveMediaSource(self: win32more.Windows.Media.Core.IMediaSource4) -> win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource: ...
    @winrt_mixinmethod
    def get_MediaStreamSource(self: win32more.Windows.Media.Core.IMediaSource4) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def get_MseStreamSource(self: win32more.Windows.Media.Core.IMediaSource4) -> win32more.Windows.Media.Core.MseStreamSource: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Media.Core.IMediaSource4) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.Media.Core.IMediaSource4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DownloadOperation(self: win32more.Windows.Media.Core.IMediaSource5) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_classmethod
    def CreateFromDownloadOperation(cls: win32more.Windows.Media.Core.IMediaSourceStatics4, downloadOperation: win32more.Windows.Networking.BackgroundTransfer.DownloadOperation) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaFrameSource(cls: win32more.Windows.Media.Core.IMediaSourceStatics3, frameSource: win32more.Windows.Media.Capture.Frames.MediaFrameSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaBinder(cls: win32more.Windows.Media.Core.IMediaSourceStatics2, binder: win32more.Windows.Media.Core.MediaBinder) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromAdaptiveMediaSource(cls: win32more.Windows.Media.Core.IMediaSourceStatics, mediaSource: win32more.Windows.Media.Streaming.Adaptive.AdaptiveMediaSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMediaStreamSource(cls: win32more.Windows.Media.Core.IMediaSourceStatics, mediaSource: win32more.Windows.Media.Core.MediaStreamSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromMseStreamSource(cls: win32more.Windows.Media.Core.IMediaSourceStatics, mediaSource: win32more.Windows.Media.Core.MseStreamSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromIMediaSource(cls: win32more.Windows.Media.Core.IMediaSourceStatics, mediaSource: win32more.Windows.Media.Core.IMediaSource) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStorageFile(cls: win32more.Windows.Media.Core.IMediaSourceStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStream(cls: win32more.Windows.Media.Core.IMediaSourceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, contentType: WinRT_String) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromStreamReference(cls: win32more.Windows.Media.Core.IMediaSourceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, contentType: WinRT_String) -> win32more.Windows.Media.Core.MediaSource: ...
    @winrt_classmethod
    def CreateFromUri(cls: win32more.Windows.Media.Core.IMediaSourceStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.MediaSource: ...
    AdaptiveMediaSource = property(get_AdaptiveMediaSource, None)
    CustomProperties = property(get_CustomProperties, None)
    DownloadOperation = property(get_DownloadOperation, None)
    Duration = property(get_Duration, None)
    ExternalTimedMetadataTracks = property(get_ExternalTimedMetadataTracks, None)
    ExternalTimedTextSources = property(get_ExternalTimedTextSources, None)
    IsOpen = property(get_IsOpen, None)
    MediaStreamSource = property(get_MediaStreamSource, None)
    MseStreamSource = property(get_MseStreamSource, None)
    State = property(get_State, None)
    Uri = property(get_Uri, None)
    OpenOperationCompleted = event()
    StateChanged = event()
class MediaSourceAppServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaSourceAppServiceConnection
    _classid_ = 'Windows.Media.Core.MediaSourceAppServiceConnection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Core.MediaSourceAppServiceConnection.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Core.IMediaSourceAppServiceConnectionFactory, appServiceConnection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.Media.Core.MediaSourceAppServiceConnection: ...
    @winrt_mixinmethod
    def add_InitializeMediaStreamSourceRequested(self: win32more.Windows.Media.Core.IMediaSourceAppServiceConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaSourceAppServiceConnection, win32more.Windows.Media.Core.InitializeMediaStreamSourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InitializeMediaStreamSourceRequested(self: win32more.Windows.Media.Core.IMediaSourceAppServiceConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Media.Core.IMediaSourceAppServiceConnection) -> Void: ...
    InitializeMediaStreamSourceRequested = event()
class MediaSourceError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaSourceError
    _classid_ = 'Windows.Media.Core.MediaSourceError'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Core.IMediaSourceError) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class MediaSourceOpenOperationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs
    _classid_ = 'Windows.Media.Core.MediaSourceOpenOperationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Media.Core.IMediaSourceOpenOperationCompletedEventArgs) -> win32more.Windows.Media.Core.MediaSourceError: ...
    Error = property(get_Error, None)
class MediaSourceState(Enum, Int32):
    Initial = 0
    Opening = 1
    Opened = 2
    Failed = 3
    Closed = 4
class MediaSourceStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaSourceStateChangedEventArgs
    _classid_ = 'Windows.Media.Core.MediaSourceStateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldState(self: win32more.Windows.Media.Core.IMediaSourceStateChangedEventArgs) -> win32more.Windows.Media.Core.MediaSourceState: ...
    @winrt_mixinmethod
    def get_NewState(self: win32more.Windows.Media.Core.IMediaSourceStateChangedEventArgs) -> win32more.Windows.Media.Core.MediaSourceState: ...
    NewState = property(get_NewState, None)
    OldState = property(get_OldState, None)
class MediaSourceStatus(Enum, Int32):
    FullySupported = 0
    Unknown = 1
class MediaStreamSample(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSample
    _classid_ = 'Windows.Media.Core.MediaStreamSample'
    @winrt_mixinmethod
    def add_Processed(self: win32more.Windows.Media.Core.IMediaStreamSample, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSample, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Processed(self: win32more.Windows.Media.Core.IMediaStreamSample, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Storage.Streams.Buffer: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Media.Core.MediaStreamSamplePropertySet: ...
    @winrt_mixinmethod
    def get_Protection(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Media.Core.MediaStreamSampleProtectionProperties: ...
    @winrt_mixinmethod
    def put_DecodeTimestamp(self: win32more.Windows.Media.Core.IMediaStreamSample, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DecodeTimestamp(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaStreamSample, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaStreamSample) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_KeyFrame(self: win32more.Windows.Media.Core.IMediaStreamSample, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyFrame(self: win32more.Windows.Media.Core.IMediaStreamSample) -> Boolean: ...
    @winrt_mixinmethod
    def put_Discontinuous(self: win32more.Windows.Media.Core.IMediaStreamSample, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Discontinuous(self: win32more.Windows.Media.Core.IMediaStreamSample) -> Boolean: ...
    @winrt_mixinmethod
    def get_Direct3D11Surface(self: win32more.Windows.Media.Core.IMediaStreamSample2) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_classmethod
    def CreateFromDirect3D11Surface(cls: win32more.Windows.Media.Core.IMediaStreamSampleStatics2, surface: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Core.MediaStreamSample: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.Media.Core.IMediaStreamSampleStatics, buffer: win32more.Windows.Storage.Streams.IBuffer, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Media.Core.MediaStreamSample: ...
    @winrt_classmethod
    def CreateFromStreamAsync(cls: win32more.Windows.Media.Core.IMediaStreamSampleStatics, stream: win32more.Windows.Storage.Streams.IInputStream, count: UInt32, timestamp: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Core.MediaStreamSample]: ...
    Buffer = property(get_Buffer, None)
    DecodeTimestamp = property(get_DecodeTimestamp, put_DecodeTimestamp)
    Direct3D11Surface = property(get_Direct3D11Surface, None)
    Discontinuous = property(get_Discontinuous, put_Discontinuous)
    Duration = property(get_Duration, put_Duration)
    ExtendedProperties = property(get_ExtendedProperties, None)
    KeyFrame = property(get_KeyFrame, put_KeyFrame)
    Protection = property(get_Protection, None)
    Timestamp = property(get_Timestamp, None)
    Processed = event()
class MediaStreamSamplePropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]
    _classid_ = 'Windows.Media.Core.MediaStreamSamplePropertySet'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable], key: Guid) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable], key: Guid) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable], key: Guid, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable], key: Guid) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[Guid, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
class MediaStreamSampleProtectionProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties
    _classid_ = 'Windows.Media.Core.MediaStreamSampleProtectionProperties'
    @winrt_mixinmethod
    def SetKeyIdentifier(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def GetKeyIdentifier(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: ReceiveArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def SetInitializationVector(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def GetInitializationVector(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: ReceiveArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def SetSubSampleMapping(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def GetSubSampleMapping(self: win32more.Windows.Media.Core.IMediaStreamSampleProtectionProperties, value: ReceiveArray[Byte]) -> Void: ...
class MediaStreamSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSource
    _classid_ = 'Windows.Media.Core.MediaStreamSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Core.MediaStreamSource.CreateFromDescriptor(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Core.MediaStreamSource.CreateFromDescriptors(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromDescriptor(cls: win32more.Windows.Media.Core.IMediaStreamSourceFactory, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_factorymethod
    def CreateFromDescriptors(cls: win32more.Windows.Media.Core.IMediaStreamSourceFactory, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, descriptor2: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> win32more.Windows.Media.Core.MediaStreamSource: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Media.Core.IMediaStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Media.Core.IMediaStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Starting(self: win32more.Windows.Media.Core.IMediaStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Starting(self: win32more.Windows.Media.Core.IMediaStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Paused(self: win32more.Windows.Media.Core.IMediaStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Paused(self: win32more.Windows.Media.Core.IMediaStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SampleRequested(self: win32more.Windows.Media.Core.IMediaStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SampleRequested(self: win32more.Windows.Media.Core.IMediaStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SwitchStreamsRequested(self: win32more.Windows.Media.Core.IMediaStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SwitchStreamsRequested(self: win32more.Windows.Media.Core.IMediaStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyError(self: win32more.Windows.Media.Core.IMediaStreamSource, errorStatus: win32more.Windows.Media.Core.MediaStreamSourceErrorStatus) -> Void: ...
    @winrt_mixinmethod
    def AddStreamDescriptor(self: win32more.Windows.Media.Core.IMediaStreamSource, descriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> Void: ...
    @winrt_mixinmethod
    def put_MediaProtectionManager(self: win32more.Windows.Media.Core.IMediaStreamSource, value: win32more.Windows.Media.Protection.MediaProtectionManager) -> Void: ...
    @winrt_mixinmethod
    def get_MediaProtectionManager(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Media.Protection.MediaProtectionManager: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaStreamSource, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_CanSeek(self: win32more.Windows.Media.Core.IMediaStreamSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanSeek(self: win32more.Windows.Media.Core.IMediaStreamSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_BufferTime(self: win32more.Windows.Media.Core.IMediaStreamSource, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BufferTime(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetBufferedRange(self: win32more.Windows.Media.Core.IMediaStreamSource, startOffset: win32more.Windows.Foundation.TimeSpan, endOffset: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_MusicProperties(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Storage.FileProperties.MusicProperties: ...
    @winrt_mixinmethod
    def get_VideoProperties(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Storage.FileProperties.VideoProperties: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.Media.Core.IMediaStreamSource, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Core.IMediaStreamSource) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def AddProtectionKey(self: win32more.Windows.Media.Core.IMediaStreamSource, streamDescriptor: win32more.Windows.Media.Core.IMediaStreamDescriptor, keyIdentifier: PassArray[Byte], licenseData: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def add_SampleRendered(self: win32more.Windows.Media.Core.IMediaStreamSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MediaStreamSource, win32more.Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SampleRendered(self: win32more.Windows.Media.Core.IMediaStreamSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_MaxSupportedPlaybackRate(self: win32more.Windows.Media.Core.IMediaStreamSource3, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxSupportedPlaybackRate(self: win32more.Windows.Media.Core.IMediaStreamSource3) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_IsLive(self: win32more.Windows.Media.Core.IMediaStreamSource4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLive(self: win32more.Windows.Media.Core.IMediaStreamSource4) -> Boolean: ...
    BufferTime = property(get_BufferTime, put_BufferTime)
    CanSeek = property(get_CanSeek, put_CanSeek)
    Duration = property(get_Duration, put_Duration)
    IsLive = property(get_IsLive, put_IsLive)
    MaxSupportedPlaybackRate = property(get_MaxSupportedPlaybackRate, put_MaxSupportedPlaybackRate)
    MediaProtectionManager = property(get_MediaProtectionManager, put_MediaProtectionManager)
    MusicProperties = property(get_MusicProperties, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    VideoProperties = property(get_VideoProperties, None)
    Closed = event()
    Starting = event()
    Paused = event()
    SampleRequested = event()
    SwitchStreamsRequested = event()
    SampleRendered = event()
class MediaStreamSourceClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceClosedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceClosedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Media.Core.IMediaStreamSourceClosedEventArgs) -> win32more.Windows.Media.Core.MediaStreamSourceClosedRequest: ...
    Request = property(get_Request, None)
class MediaStreamSourceClosedReason(Enum, Int32):
    Done = 0
    UnknownError = 1
    AppReportedError = 2
    UnsupportedProtectionSystem = 3
    ProtectionSystemFailure = 4
    UnsupportedEncodingFormat = 5
    MissingSampleRequestedEventHandler = 6
class MediaStreamSourceClosedRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceClosedRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceClosedRequest'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Media.Core.IMediaStreamSourceClosedRequest) -> win32more.Windows.Media.Core.MediaStreamSourceClosedReason: ...
    Reason = property(get_Reason, None)
class MediaStreamSourceErrorStatus(Enum, Int32):
    Other = 0
    OutOfMemory = 1
    FailedToOpenFile = 2
    FailedToConnectToServer = 3
    ConnectionToServerLost = 4
    UnspecifiedNetworkError = 5
    DecodeError = 6
    UnsupportedMediaFormat = 7
class MediaStreamSourceSampleRenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRenderedEventArgs'
    @winrt_mixinmethod
    def get_SampleLag(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRenderedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    SampleLag = property(get_SampleLag, None)
class MediaStreamSourceSampleRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequest'
    @winrt_mixinmethod
    def get_StreamDescriptor(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest) -> win32more.Windows.Media.Core.MediaStreamSourceSampleRequestDeferral: ...
    @winrt_mixinmethod
    def put_Sample(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest, value: win32more.Windows.Media.Core.MediaStreamSample) -> Void: ...
    @winrt_mixinmethod
    def get_Sample(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest) -> win32more.Windows.Media.Core.MediaStreamSample: ...
    @winrt_mixinmethod
    def ReportSampleProgress(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequest, progress: UInt32) -> Void: ...
    Sample = property(get_Sample, put_Sample)
    StreamDescriptor = property(get_StreamDescriptor, None)
class MediaStreamSourceSampleRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequestDeferral) -> Void: ...
class MediaStreamSourceSampleRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSampleRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Media.Core.IMediaStreamSourceSampleRequestedEventArgs) -> win32more.Windows.Media.Core.MediaStreamSourceSampleRequest: ...
    Request = property(get_Request, None)
class MediaStreamSourceStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceStartingEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Media.Core.IMediaStreamSourceStartingEventArgs) -> win32more.Windows.Media.Core.MediaStreamSourceStartingRequest: ...
    Request = property(get_Request, None)
class MediaStreamSourceStartingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingRequest'
    @winrt_mixinmethod
    def get_StartPosition(self: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequest) -> win32more.Windows.Media.Core.MediaStreamSourceStartingRequestDeferral: ...
    @winrt_mixinmethod
    def SetActualStartPosition(self: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequest, position: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    StartPosition = property(get_StartPosition, None)
class MediaStreamSourceStartingRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceStartingRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Media.Core.IMediaStreamSourceStartingRequestDeferral) -> Void: ...
class MediaStreamSourceSwitchStreamsRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest'
    @winrt_mixinmethod
    def get_OldStreamDescriptor(self: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def get_NewStreamDescriptor(self: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> win32more.Windows.Media.Core.IMediaStreamDescriptor: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequest) -> win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral: ...
    NewStreamDescriptor = property(get_NewStreamDescriptor, None)
    OldStreamDescriptor = property(get_OldStreamDescriptor, None)
class MediaStreamSourceSwitchStreamsRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestDeferral) -> Void: ...
class MediaStreamSourceSwitchStreamsRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs
    _classid_ = 'Windows.Media.Core.MediaStreamSourceSwitchStreamsRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Media.Core.IMediaStreamSourceSwitchStreamsRequestedEventArgs) -> win32more.Windows.Media.Core.MediaStreamSourceSwitchStreamsRequest: ...
    Request = property(get_Request, None)
class MediaTrackKind(Enum, Int32):
    Audio = 0
    Video = 1
    TimedMetadata = 2
class MseAppendMode(Enum, Int32):
    Segments = 0
    Sequence = 1
class MseEndOfStreamStatus(Enum, Int32):
    Success = 0
    NetworkError = 1
    DecodeError = 2
    UnknownError = 3
class MseReadyState(Enum, Int32):
    Closed = 0
    Open = 1
    Ended = 2
class MseSourceBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMseSourceBuffer
    _classid_ = 'Windows.Media.Core.MseSourceBuffer'
    @winrt_mixinmethod
    def add_UpdateStarting(self: win32more.Windows.Media.Core.IMseSourceBuffer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateStarting(self: win32more.Windows.Media.Core.IMseSourceBuffer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Media.Core.IMseSourceBuffer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Media.Core.IMseSourceBuffer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateEnded(self: win32more.Windows.Media.Core.IMseSourceBuffer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateEnded(self: win32more.Windows.Media.Core.IMseSourceBuffer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: win32more.Windows.Media.Core.IMseSourceBuffer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: win32more.Windows.Media.Core.IMseSourceBuffer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Aborted(self: win32more.Windows.Media.Core.IMseSourceBuffer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBuffer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Aborted(self: win32more.Windows.Media.Core.IMseSourceBuffer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> win32more.Windows.Media.Core.MseAppendMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.Media.Core.IMseSourceBuffer, value: win32more.Windows.Media.Core.MseAppendMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsUpdating(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> Boolean: ...
    @winrt_mixinmethod
    def get_Buffered(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.MseTimeRange]: ...
    @winrt_mixinmethod
    def get_TimestampOffset(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TimestampOffset(self: win32more.Windows.Media.Core.IMseSourceBuffer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AppendWindowStart(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AppendWindowStart(self: win32more.Windows.Media.Core.IMseSourceBuffer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AppendWindowEnd(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_AppendWindowEnd(self: win32more.Windows.Media.Core.IMseSourceBuffer, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def AppendBuffer(self: win32more.Windows.Media.Core.IMseSourceBuffer, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def AppendStream(self: win32more.Windows.Media.Core.IMseSourceBuffer, stream: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def AppendStreamMaxSize(self: win32more.Windows.Media.Core.IMseSourceBuffer, stream: win32more.Windows.Storage.Streams.IInputStream, maxSize: UInt64) -> Void: ...
    @winrt_mixinmethod
    def Abort(self: win32more.Windows.Media.Core.IMseSourceBuffer) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Media.Core.IMseSourceBuffer, start: win32more.Windows.Foundation.TimeSpan, end: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    AppendWindowEnd = property(get_AppendWindowEnd, put_AppendWindowEnd)
    AppendWindowStart = property(get_AppendWindowStart, put_AppendWindowStart)
    Buffered = property(get_Buffered, None)
    IsUpdating = property(get_IsUpdating, None)
    Mode = property(get_Mode, put_Mode)
    TimestampOffset = property(get_TimestampOffset, put_TimestampOffset)
    UpdateStarting = event()
    Updated = event()
    UpdateEnded = event()
    ErrorOccurred = event()
    Aborted = event()
class MseSourceBufferList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMseSourceBufferList
    _classid_ = 'Windows.Media.Core.MseSourceBufferList'
    @winrt_mixinmethod
    def add_SourceBufferAdded(self: win32more.Windows.Media.Core.IMseSourceBufferList, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBufferList, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceBufferAdded(self: win32more.Windows.Media.Core.IMseSourceBufferList, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceBufferRemoved(self: win32more.Windows.Media.Core.IMseSourceBufferList, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseSourceBufferList, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceBufferRemoved(self: win32more.Windows.Media.Core.IMseSourceBufferList, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Buffers(self: win32more.Windows.Media.Core.IMseSourceBufferList) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.MseSourceBuffer]: ...
    Buffers = property(get_Buffers, None)
    SourceBufferAdded = event()
    SourceBufferRemoved = event()
class MseStreamSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMseStreamSource
    _classid_ = 'Windows.Media.Core.MseStreamSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.MseStreamSource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.MseStreamSource: ...
    @winrt_mixinmethod
    def add_Opened(self: win32more.Windows.Media.Core.IMseStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Opened(self: win32more.Windows.Media.Core.IMseStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Ended(self: win32more.Windows.Media.Core.IMseStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Ended(self: win32more.Windows.Media.Core.IMseStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.Media.Core.IMseStreamSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.MseStreamSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.Media.Core.IMseStreamSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SourceBuffers(self: win32more.Windows.Media.Core.IMseStreamSource) -> win32more.Windows.Media.Core.MseSourceBufferList: ...
    @winrt_mixinmethod
    def get_ActiveSourceBuffers(self: win32more.Windows.Media.Core.IMseStreamSource) -> win32more.Windows.Media.Core.MseSourceBufferList: ...
    @winrt_mixinmethod
    def get_ReadyState(self: win32more.Windows.Media.Core.IMseStreamSource) -> win32more.Windows.Media.Core.MseReadyState: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMseStreamSource) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMseStreamSource, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def AddSourceBuffer(self: win32more.Windows.Media.Core.IMseStreamSource, mimeType: WinRT_String) -> win32more.Windows.Media.Core.MseSourceBuffer: ...
    @winrt_mixinmethod
    def RemoveSourceBuffer(self: win32more.Windows.Media.Core.IMseStreamSource, buffer: win32more.Windows.Media.Core.MseSourceBuffer) -> Void: ...
    @winrt_mixinmethod
    def EndOfStream(self: win32more.Windows.Media.Core.IMseStreamSource, status: win32more.Windows.Media.Core.MseEndOfStreamStatus) -> Void: ...
    @winrt_mixinmethod
    def get_LiveSeekableRange(self: win32more.Windows.Media.Core.IMseStreamSource2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Core.MseTimeRange]: ...
    @winrt_mixinmethod
    def put_LiveSeekableRange(self: win32more.Windows.Media.Core.IMseStreamSource2, value: win32more.Windows.Foundation.IReference[win32more.Windows.Media.Core.MseTimeRange]) -> Void: ...
    @winrt_classmethod
    def IsContentTypeSupported(cls: win32more.Windows.Media.Core.IMseStreamSourceStatics, contentType: WinRT_String) -> Boolean: ...
    ActiveSourceBuffers = property(get_ActiveSourceBuffers, None)
    Duration = property(get_Duration, put_Duration)
    LiveSeekableRange = property(get_LiveSeekableRange, put_LiveSeekableRange)
    ReadyState = property(get_ReadyState, None)
    SourceBuffers = property(get_SourceBuffers, None)
    Opened = event()
    Ended = event()
    Closed = event()
class MseTimeRange(Structure):
    Start: win32more.Windows.Foundation.TimeSpan
    End: win32more.Windows.Foundation.TimeSpan
class SceneAnalysisEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ISceneAnalysisEffect
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffect'
    @winrt_mixinmethod
    def get_HighDynamicRangeAnalyzer(self: win32more.Windows.Media.Core.ISceneAnalysisEffect) -> win32more.Windows.Media.Core.HighDynamicRangeControl: ...
    @winrt_mixinmethod
    def put_DesiredAnalysisInterval(self: win32more.Windows.Media.Core.ISceneAnalysisEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredAnalysisInterval(self: win32more.Windows.Media.Core.ISceneAnalysisEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_SceneAnalyzed(self: win32more.Windows.Media.Core.ISceneAnalysisEffect, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.SceneAnalysisEffect, win32more.Windows.Media.Core.SceneAnalyzedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SceneAnalyzed(self: win32more.Windows.Media.Core.ISceneAnalysisEffect, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetProperties(self: win32more.Windows.Media.IMediaExtension, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    DesiredAnalysisInterval = property(get_DesiredAnalysisInterval, put_DesiredAnalysisInterval)
    HighDynamicRangeAnalyzer = property(get_HighDynamicRangeAnalyzer, None)
    SceneAnalyzed = event()
class SceneAnalysisEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.SceneAnalysisEffectDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.SceneAnalysisEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class SceneAnalysisEffectFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Core.ISceneAnalysisEffectFrame
    _classid_ = 'Windows.Media.Core.SceneAnalysisEffectFrame'
    @winrt_mixinmethod
    def get_FrameControlValues(self: win32more.Windows.Media.Core.ISceneAnalysisEffectFrame) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    @winrt_mixinmethod
    def get_HighDynamicRange(self: win32more.Windows.Media.Core.ISceneAnalysisEffectFrame) -> win32more.Windows.Media.Core.HighDynamicRangeOutput: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.IMediaFrame) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SystemRelativeTime(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SystemRelativeTime(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.IMediaFrame, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_IsDiscontinuous(self: win32more.Windows.Media.IMediaFrame, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscontinuous(self: win32more.Windows.Media.IMediaFrame) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedProperties(self: win32more.Windows.Media.IMediaFrame) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_AnalysisRecommendation(self: win32more.Windows.Media.Core.ISceneAnalysisEffectFrame2) -> win32more.Windows.Media.Core.SceneAnalysisRecommendation: ...
    AnalysisRecommendation = property(get_AnalysisRecommendation, None)
    Duration = property(get_Duration, put_Duration)
    ExtendedProperties = property(get_ExtendedProperties, None)
    FrameControlValues = property(get_FrameControlValues, None)
    HighDynamicRange = property(get_HighDynamicRange, None)
    IsDiscontinuous = property(get_IsDiscontinuous, put_IsDiscontinuous)
    IsReadOnly = property(get_IsReadOnly, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    SystemRelativeTime = property(get_SystemRelativeTime, put_SystemRelativeTime)
    Type = property(get_Type, None)
class SceneAnalysisRecommendation(Enum, Int32):
    Standard = 0
    Hdr = 1
    LowLight = 2
class SceneAnalyzedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ISceneAnalyzedEventArgs
    _classid_ = 'Windows.Media.Core.SceneAnalyzedEventArgs'
    @winrt_mixinmethod
    def get_ResultFrame(self: win32more.Windows.Media.Core.ISceneAnalyzedEventArgs) -> win32more.Windows.Media.Core.SceneAnalysisEffectFrame: ...
    ResultFrame = property(get_ResultFrame, None)
class SpeechCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ISpeechCue
    _classid_ = 'Windows.Media.Core.SpeechCue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.SpeechCue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.SpeechCue: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Core.ISpeechCue) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.Media.Core.ISpeechCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartPositionInInput(self: win32more.Windows.Media.Core.ISpeechCue) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_StartPositionInInput(self: win32more.Windows.Media.Core.ISpeechCue, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_EndPositionInInput(self: win32more.Windows.Media.Core.ISpeechCue) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_EndPositionInInput(self: win32more.Windows.Media.Core.ISpeechCue, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    Duration = property(get_Duration, put_Duration)
    EndPositionInInput = property(get_EndPositionInInput, put_EndPositionInInput)
    Id = property(get_Id, put_Id)
    StartPositionInInput = property(get_StartPositionInInput, put_StartPositionInInput)
    StartTime = property(get_StartTime, put_StartTime)
    Text = property(get_Text, put_Text)
class TimedMetadataKind(Enum, Int32):
    Caption = 0
    Chapter = 1
    Custom = 2
    Data = 3
    Description = 4
    Subtitle = 5
    ImageSubtitle = 6
    Speech = 7
class TimedMetadataStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaStreamDescriptor
    _classid_ = 'Windows.Media.Core.TimedMetadataStreamDescriptor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Core.TimedMetadataStreamDescriptor.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Core.ITimedMetadataStreamDescriptorFactory, encodingProperties: win32more.Windows.Media.MediaProperties.TimedMetadataEncodingProperties) -> win32more.Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Core.ITimedMetadataStreamDescriptor) -> win32more.Windows.Media.MediaProperties.TimedMetadataEncodingProperties: ...
    @winrt_mixinmethod
    def Copy(self: win32more.Windows.Media.Core.ITimedMetadataStreamDescriptor) -> win32more.Windows.Media.Core.TimedMetadataStreamDescriptor: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    EncodingProperties = property(get_EncodingProperties, None)
    IsSelected = property(get_IsSelected, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, put_Language)
    Name = property(get_Name, put_Name)
class TimedMetadataTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedMetadataTrack
    _classid_ = 'Windows.Media.Core.TimedMetadataTrack'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Media.Core.TimedMetadataTrack.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Core.ITimedMetadataTrackFactory, id: WinRT_String, language: WinRT_String, kind: win32more.Windows.Media.Core.TimedMetadataKind) -> win32more.Windows.Media.Core.TimedMetadataTrack: ...
    @winrt_mixinmethod
    def add_CueEntered(self: win32more.Windows.Media.Core.ITimedMetadataTrack, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.MediaCueEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CueEntered(self: win32more.Windows.Media.Core.ITimedMetadataTrack, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CueExited(self: win32more.Windows.Media.Core.ITimedMetadataTrack, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.MediaCueEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CueExited(self: win32more.Windows.Media.Core.ITimedMetadataTrack, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TrackFailed(self: win32more.Windows.Media.Core.ITimedMetadataTrack, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedMetadataTrack, win32more.Windows.Media.Core.TimedMetadataTrackFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TrackFailed(self: win32more.Windows.Media.Core.ITimedMetadataTrack, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Cues(self: win32more.Windows.Media.Core.ITimedMetadataTrack) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.IMediaCue]: ...
    @winrt_mixinmethod
    def get_ActiveCues(self: win32more.Windows.Media.Core.ITimedMetadataTrack) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.IMediaCue]: ...
    @winrt_mixinmethod
    def get_TimedMetadataKind(self: win32more.Windows.Media.Core.ITimedMetadataTrack) -> win32more.Windows.Media.Core.TimedMetadataKind: ...
    @winrt_mixinmethod
    def get_DispatchType(self: win32more.Windows.Media.Core.ITimedMetadataTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddCue(self: win32more.Windows.Media.Core.ITimedMetadataTrack, cue: win32more.Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_mixinmethod
    def RemoveCue(self: win32more.Windows.Media.Core.ITimedMetadataTrack, cue: win32more.Windows.Media.Core.IMediaCue) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: win32more.Windows.Media.Core.IMediaTrack) -> win32more.Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: win32more.Windows.Media.Core.ITimedMetadataTrack2) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.ITimedMetadataTrack2) -> WinRT_String: ...
    ActiveCues = property(get_ActiveCues, None)
    Cues = property(get_Cues, None)
    DispatchType = property(get_DispatchType, None)
    Id = property(get_Id, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, None)
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
    TimedMetadataKind = property(get_TimedMetadataKind, None)
    TrackKind = property(get_TrackKind, None)
    CueEntered = event()
    CueExited = event()
    TrackFailed = event()
class TimedMetadataTrackError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedMetadataTrackError
    _classid_ = 'Windows.Media.Core.TimedMetadataTrackError'
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Media.Core.ITimedMetadataTrackError) -> win32more.Windows.Media.Core.TimedMetadataTrackErrorCode: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Core.ITimedMetadataTrackError) -> win32more.Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedError = property(get_ExtendedError, None)
class TimedMetadataTrackErrorCode(Enum, Int32):
    None_ = 0
    DataFormatError = 1
    NetworkError = 2
    InternalError = 3
class TimedMetadataTrackFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedMetadataTrackFailedEventArgs
    _classid_ = 'Windows.Media.Core.TimedMetadataTrackFailedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Media.Core.ITimedMetadataTrackFailedEventArgs) -> win32more.Windows.Media.Core.TimedMetadataTrackError: ...
    Error = property(get_Error, None)
class TimedTextBouten(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextBouten
    _classid_ = 'Windows.Media.Core.TimedTextBouten'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Core.ITimedTextBouten) -> win32more.Windows.Media.Core.TimedTextBoutenType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.Media.Core.ITimedTextBouten, value: win32more.Windows.Media.Core.TimedTextBoutenType) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Media.Core.ITimedTextBouten) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Media.Core.ITimedTextBouten, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Core.ITimedTextBouten) -> win32more.Windows.Media.Core.TimedTextBoutenPosition: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Core.ITimedTextBouten, value: win32more.Windows.Media.Core.TimedTextBoutenPosition) -> Void: ...
    Color = property(get_Color, put_Color)
    Position = property(get_Position, put_Position)
    Type = property(get_Type, put_Type)
class TimedTextBoutenPosition(Enum, Int32):
    Before = 0
    After = 1
    Outside = 2
class TimedTextBoutenType(Enum, Int32):
    None_ = 0
    Auto = 1
    FilledCircle = 2
    OpenCircle = 3
    FilledDot = 4
    OpenDot = 5
    FilledSesame = 6
    OpenSesame = 7
class TimedTextCue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextCue
    _classid_ = 'Windows.Media.Core.TimedTextCue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.TimedTextCue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.TimedTextCue: ...
    @winrt_mixinmethod
    def get_CueRegion(self: win32more.Windows.Media.Core.ITimedTextCue) -> win32more.Windows.Media.Core.TimedTextRegion: ...
    @winrt_mixinmethod
    def put_CueRegion(self: win32more.Windows.Media.Core.ITimedTextCue, value: win32more.Windows.Media.Core.TimedTextRegion) -> Void: ...
    @winrt_mixinmethod
    def get_CueStyle(self: win32more.Windows.Media.Core.ITimedTextCue) -> win32more.Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def put_CueStyle(self: win32more.Windows.Media.Core.ITimedTextCue, value: win32more.Windows.Media.Core.TimedTextStyle) -> Void: ...
    @winrt_mixinmethod
    def get_Lines(self: win32more.Windows.Media.Core.ITimedTextCue) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.TimedTextLine]: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Media.Core.IMediaCue, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.Core.IMediaCue) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Media.Core.IMediaCue, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaCue) -> WinRT_String: ...
    CueRegion = property(get_CueRegion, put_CueRegion)
    CueStyle = property(get_CueStyle, put_CueStyle)
    Duration = property(get_Duration, put_Duration)
    Id = property(get_Id, put_Id)
    Lines = property(get_Lines, None)
    StartTime = property(get_StartTime, put_StartTime)
class TimedTextDisplayAlignment(Enum, Int32):
    Before = 0
    After = 1
    Center = 2
class TimedTextDouble(Structure):
    Value: Double
    Unit: win32more.Windows.Media.Core.TimedTextUnit
class TimedTextFlowDirection(Enum, Int32):
    LeftToRight = 0
    RightToLeft = 1
class TimedTextFontStyle(Enum, Int32):
    Normal = 0
    Oblique = 1
    Italic = 2
class TimedTextLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextLine
    _classid_ = 'Windows.Media.Core.TimedTextLine'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.TimedTextLine.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.TimedTextLine: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Core.ITimedTextLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.Media.Core.ITimedTextLine, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subformats(self: win32more.Windows.Media.Core.ITimedTextLine) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Core.TimedTextSubformat]: ...
    Subformats = property(get_Subformats, None)
    Text = property(get_Text, put_Text)
class TimedTextLineAlignment(Enum, Int32):
    Start = 0
    End = 1
    Center = 2
class TimedTextPadding(Structure):
    Before: Double
    After: Double
    Start: Double
    End: Double
    Unit: win32more.Windows.Media.Core.TimedTextUnit
class TimedTextPoint(Structure):
    X: Double
    Y: Double
    Unit: win32more.Windows.Media.Core.TimedTextUnit
class TimedTextRegion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextRegion
    _classid_ = 'Windows.Media.Core.TimedTextRegion'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.TimedTextRegion.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.TimedTextRegion: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.ITimedTextRegion) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Core.ITimedTextRegion, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextPoint: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextPoint) -> Void: ...
    @winrt_mixinmethod
    def get_Extent(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextSize: ...
    @winrt_mixinmethod
    def put_Extent(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextSize) -> Void: ...
    @winrt_mixinmethod
    def get_Background(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Background(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_WritingMode(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextWritingMode: ...
    @winrt_mixinmethod
    def put_WritingMode(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextWritingMode) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayAlignment(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextDisplayAlignment: ...
    @winrt_mixinmethod
    def put_DisplayAlignment(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextDisplayAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_LineHeight(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_LineHeight(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverflowClipped(self: win32more.Windows.Media.Core.ITimedTextRegion) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverflowClipped(self: win32more.Windows.Media.Core.ITimedTextRegion, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Padding(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextPadding: ...
    @winrt_mixinmethod
    def put_Padding(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextPadding) -> Void: ...
    @winrt_mixinmethod
    def get_TextWrapping(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextWrapping: ...
    @winrt_mixinmethod
    def put_TextWrapping(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextWrapping) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Media.Core.ITimedTextRegion) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Media.Core.ITimedTextRegion, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ScrollMode(self: win32more.Windows.Media.Core.ITimedTextRegion) -> win32more.Windows.Media.Core.TimedTextScrollMode: ...
    @winrt_mixinmethod
    def put_ScrollMode(self: win32more.Windows.Media.Core.ITimedTextRegion, value: win32more.Windows.Media.Core.TimedTextScrollMode) -> Void: ...
    Background = property(get_Background, put_Background)
    DisplayAlignment = property(get_DisplayAlignment, put_DisplayAlignment)
    Extent = property(get_Extent, put_Extent)
    IsOverflowClipped = property(get_IsOverflowClipped, put_IsOverflowClipped)
    LineHeight = property(get_LineHeight, put_LineHeight)
    Name = property(get_Name, put_Name)
    Padding = property(get_Padding, put_Padding)
    Position = property(get_Position, put_Position)
    ScrollMode = property(get_ScrollMode, put_ScrollMode)
    TextWrapping = property(get_TextWrapping, put_TextWrapping)
    WritingMode = property(get_WritingMode, put_WritingMode)
    ZIndex = property(get_ZIndex, put_ZIndex)
class TimedTextRuby(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextRuby
    _classid_ = 'Windows.Media.Core.TimedTextRuby'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Core.ITimedTextRuby) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.Media.Core.ITimedTextRuby, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Media.Core.ITimedTextRuby) -> win32more.Windows.Media.Core.TimedTextRubyPosition: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.Media.Core.ITimedTextRuby, value: win32more.Windows.Media.Core.TimedTextRubyPosition) -> Void: ...
    @winrt_mixinmethod
    def get_Align(self: win32more.Windows.Media.Core.ITimedTextRuby) -> win32more.Windows.Media.Core.TimedTextRubyAlign: ...
    @winrt_mixinmethod
    def put_Align(self: win32more.Windows.Media.Core.ITimedTextRuby, value: win32more.Windows.Media.Core.TimedTextRubyAlign) -> Void: ...
    @winrt_mixinmethod
    def get_Reserve(self: win32more.Windows.Media.Core.ITimedTextRuby) -> win32more.Windows.Media.Core.TimedTextRubyReserve: ...
    @winrt_mixinmethod
    def put_Reserve(self: win32more.Windows.Media.Core.ITimedTextRuby, value: win32more.Windows.Media.Core.TimedTextRubyReserve) -> Void: ...
    Align = property(get_Align, put_Align)
    Position = property(get_Position, put_Position)
    Reserve = property(get_Reserve, put_Reserve)
    Text = property(get_Text, put_Text)
class TimedTextRubyAlign(Enum, Int32):
    Center = 0
    Start = 1
    End = 2
    SpaceAround = 3
    SpaceBetween = 4
    WithBase = 5
class TimedTextRubyPosition(Enum, Int32):
    Before = 0
    After = 1
    Outside = 2
class TimedTextRubyReserve(Enum, Int32):
    None_ = 0
    Before = 1
    After = 2
    Both = 3
    Outside = 4
class TimedTextScrollMode(Enum, Int32):
    Popon = 0
    Rollup = 1
class TimedTextSize(Structure):
    Height: Double
    Width: Double
    Unit: win32more.Windows.Media.Core.TimedTextUnit
class TimedTextSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextSource
    _classid_ = 'Windows.Media.Core.TimedTextSource'
    @winrt_mixinmethod
    def add_Resolved(self: win32more.Windows.Media.Core.ITimedTextSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.TimedTextSource, win32more.Windows.Media.Core.TimedTextSourceResolveResultEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Resolved(self: win32more.Windows.Media.Core.ITimedTextSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromStreamWithIndex(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics2, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, indexStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithIndex(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics2, uri: win32more.Windows.Foundation.Uri, indexUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStreamWithIndexAndLanguage(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics2, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, indexStream: win32more.Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithIndexAndLanguage(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics2, uri: win32more.Windows.Foundation.Uri, indexUri: win32more.Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStream(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUri(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromStreamWithLanguage(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    @winrt_classmethod
    def CreateFromUriWithLanguage(cls: win32more.Windows.Media.Core.ITimedTextSourceStatics, uri: win32more.Windows.Foundation.Uri, defaultLanguage: WinRT_String) -> win32more.Windows.Media.Core.TimedTextSource: ...
    Resolved = event()
class TimedTextSourceResolveResultEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextSourceResolveResultEventArgs
    _classid_ = 'Windows.Media.Core.TimedTextSourceResolveResultEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Media.Core.ITimedTextSourceResolveResultEventArgs) -> win32more.Windows.Media.Core.TimedMetadataTrackError: ...
    @winrt_mixinmethod
    def get_Tracks(self: win32more.Windows.Media.Core.ITimedTextSourceResolveResultEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    Error = property(get_Error, None)
    Tracks = property(get_Tracks, None)
class TimedTextStyle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextStyle
    _classid_ = 'Windows.Media.Core.TimedTextStyle'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.TimedTextStyle.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.ITimedTextStyle) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Core.ITimedTextStyle, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FontFamily(self: win32more.Windows.Media.Core.ITimedTextStyle) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FontFamily(self: win32more.Windows.Media.Core.ITimedTextStyle, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FontSize(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_FontSize(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_FontWeight(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextWeight: ...
    @winrt_mixinmethod
    def put_FontWeight(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextWeight) -> Void: ...
    @winrt_mixinmethod
    def get_Foreground(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Foreground(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Background(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Background(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_IsBackgroundAlwaysShown(self: win32more.Windows.Media.Core.ITimedTextStyle) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBackgroundAlwaysShown(self: win32more.Windows.Media.Core.ITimedTextStyle, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FlowDirection(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextFlowDirection: ...
    @winrt_mixinmethod
    def put_FlowDirection(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextFlowDirection) -> Void: ...
    @winrt_mixinmethod
    def get_LineAlignment(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextLineAlignment: ...
    @winrt_mixinmethod
    def put_LineAlignment(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextLineAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineColor(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_OutlineColor(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineThickness(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_OutlineThickness(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineRadius(self: win32more.Windows.Media.Core.ITimedTextStyle) -> win32more.Windows.Media.Core.TimedTextDouble: ...
    @winrt_mixinmethod
    def put_OutlineRadius(self: win32more.Windows.Media.Core.ITimedTextStyle, value: win32more.Windows.Media.Core.TimedTextDouble) -> Void: ...
    @winrt_mixinmethod
    def get_FontStyle(self: win32more.Windows.Media.Core.ITimedTextStyle2) -> win32more.Windows.Media.Core.TimedTextFontStyle: ...
    @winrt_mixinmethod
    def put_FontStyle(self: win32more.Windows.Media.Core.ITimedTextStyle2, value: win32more.Windows.Media.Core.TimedTextFontStyle) -> Void: ...
    @winrt_mixinmethod
    def get_IsUnderlineEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsUnderlineEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLineThroughEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLineThroughEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsOverlineEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOverlineEnabled(self: win32more.Windows.Media.Core.ITimedTextStyle2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ruby(self: win32more.Windows.Media.Core.ITimedTextStyle3) -> win32more.Windows.Media.Core.TimedTextRuby: ...
    @winrt_mixinmethod
    def get_Bouten(self: win32more.Windows.Media.Core.ITimedTextStyle3) -> win32more.Windows.Media.Core.TimedTextBouten: ...
    @winrt_mixinmethod
    def get_IsTextCombined(self: win32more.Windows.Media.Core.ITimedTextStyle3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTextCombined(self: win32more.Windows.Media.Core.ITimedTextStyle3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FontAngleInDegrees(self: win32more.Windows.Media.Core.ITimedTextStyle3) -> Double: ...
    @winrt_mixinmethod
    def put_FontAngleInDegrees(self: win32more.Windows.Media.Core.ITimedTextStyle3, value: Double) -> Void: ...
    Background = property(get_Background, put_Background)
    Bouten = property(get_Bouten, None)
    FlowDirection = property(get_FlowDirection, put_FlowDirection)
    FontAngleInDegrees = property(get_FontAngleInDegrees, put_FontAngleInDegrees)
    FontFamily = property(get_FontFamily, put_FontFamily)
    FontSize = property(get_FontSize, put_FontSize)
    FontStyle = property(get_FontStyle, put_FontStyle)
    FontWeight = property(get_FontWeight, put_FontWeight)
    Foreground = property(get_Foreground, put_Foreground)
    IsBackgroundAlwaysShown = property(get_IsBackgroundAlwaysShown, put_IsBackgroundAlwaysShown)
    IsLineThroughEnabled = property(get_IsLineThroughEnabled, put_IsLineThroughEnabled)
    IsOverlineEnabled = property(get_IsOverlineEnabled, put_IsOverlineEnabled)
    IsTextCombined = property(get_IsTextCombined, put_IsTextCombined)
    IsUnderlineEnabled = property(get_IsUnderlineEnabled, put_IsUnderlineEnabled)
    LineAlignment = property(get_LineAlignment, put_LineAlignment)
    Name = property(get_Name, put_Name)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    OutlineRadius = property(get_OutlineRadius, put_OutlineRadius)
    OutlineThickness = property(get_OutlineThickness, put_OutlineThickness)
    Ruby = property(get_Ruby, None)
class TimedTextSubformat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.ITimedTextSubformat
    _classid_ = 'Windows.Media.Core.TimedTextSubformat'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.TimedTextSubformat.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.TimedTextSubformat: ...
    @winrt_mixinmethod
    def get_StartIndex(self: win32more.Windows.Media.Core.ITimedTextSubformat) -> Int32: ...
    @winrt_mixinmethod
    def put_StartIndex(self: win32more.Windows.Media.Core.ITimedTextSubformat, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Media.Core.ITimedTextSubformat) -> Int32: ...
    @winrt_mixinmethod
    def put_Length(self: win32more.Windows.Media.Core.ITimedTextSubformat, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SubformatStyle(self: win32more.Windows.Media.Core.ITimedTextSubformat) -> win32more.Windows.Media.Core.TimedTextStyle: ...
    @winrt_mixinmethod
    def put_SubformatStyle(self: win32more.Windows.Media.Core.ITimedTextSubformat, value: win32more.Windows.Media.Core.TimedTextStyle) -> Void: ...
    Length = property(get_Length, put_Length)
    StartIndex = property(get_StartIndex, put_StartIndex)
    SubformatStyle = property(get_SubformatStyle, put_SubformatStyle)
class TimedTextUnit(Enum, Int32):
    Pixels = 0
    Percentage = 1
class TimedTextWeight(Enum, Int32):
    Normal = 400
    Bold = 700
class TimedTextWrapping(Enum, Int32):
    NoWrap = 0
    Wrap = 1
class TimedTextWritingMode(Enum, Int32):
    LeftRightTopBottom = 0
    RightLeftTopBottom = 1
    TopBottomRightLeft = 2
    TopBottomLeftRight = 3
    LeftRight = 4
    RightLeft = 5
    TopBottom = 6
class VideoStabilizationEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IVideoStabilizationEffect
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffect'
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Media.Core.IVideoStabilizationEffect, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Media.Core.IVideoStabilizationEffect) -> Boolean: ...
    @winrt_mixinmethod
    def add_EnabledChanged(self: win32more.Windows.Media.Core.IVideoStabilizationEffect, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.VideoStabilizationEffect, win32more.Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnabledChanged(self: win32more.Windows.Media.Core.IVideoStabilizationEffect, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetRecommendedStreamConfiguration(self: win32more.Windows.Media.Core.IVideoStabilizationEffect, controller: win32more.Windows.Media.Devices.VideoDeviceController, desiredProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties) -> win32more.Windows.Media.Capture.VideoStreamConfiguration: ...
    @winrt_mixinmethod
    def SetProperties(self: win32more.Windows.Media.IMediaExtension, configuration: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    EnabledChanged = event()
class VideoStabilizationEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Core.VideoStabilizationEffectDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Core.VideoStabilizationEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class VideoStabilizationEffectEnabledChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs
    _classid_ = 'Windows.Media.Core.VideoStabilizationEffectEnabledChangedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Media.Core.IVideoStabilizationEffectEnabledChangedEventArgs) -> win32more.Windows.Media.Core.VideoStabilizationEffectEnabledChangedReason: ...
    Reason = property(get_Reason, None)
class VideoStabilizationEffectEnabledChangedReason(Enum, Int32):
    Programmatic = 0
    PixelRateTooHigh = 1
    RunningSlowly = 2
class VideoStreamDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IVideoStreamDescriptor
    _classid_ = 'Windows.Media.Core.VideoStreamDescriptor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Core.VideoStreamDescriptor.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Core.IVideoStreamDescriptorFactory, encodingProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties) -> win32more.Windows.Media.Core.VideoStreamDescriptor: ...
    @winrt_mixinmethod
    def get_EncodingProperties(self: win32more.Windows.Media.Core.IVideoStreamDescriptor) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaStreamDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaStreamDescriptor2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Copy(self: win32more.Windows.Media.Core.IVideoStreamDescriptor2) -> win32more.Windows.Media.Core.VideoStreamDescriptor: ...
    EncodingProperties = property(get_EncodingProperties, None)
    IsSelected = property(get_IsSelected, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, put_Language)
    Name = property(get_Name, put_Name)
class VideoTrack(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IMediaTrack
    _classid_ = 'Windows.Media.Core.VideoTrack'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackKind(self: win32more.Windows.Media.Core.IMediaTrack) -> win32more.Windows.Media.Core.MediaTrackKind: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Media.Core.IMediaTrack, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Media.Core.IMediaTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_OpenFailed(self: win32more.Windows.Media.Core.IVideoTrack, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Core.VideoTrack, win32more.Windows.Media.Core.VideoTrackOpenFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OpenFailed(self: win32more.Windows.Media.Core.IVideoTrack, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetEncodingProperties(self: win32more.Windows.Media.Core.IVideoTrack) -> win32more.Windows.Media.MediaProperties.VideoEncodingProperties: ...
    @winrt_mixinmethod
    def get_PlaybackItem(self: win32more.Windows.Media.Core.IVideoTrack) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Core.IVideoTrack) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportInfo(self: win32more.Windows.Media.Core.IVideoTrack) -> win32more.Windows.Media.Core.VideoTrackSupportInfo: ...
    Id = property(get_Id, None)
    Label = property(get_Label, put_Label)
    Language = property(get_Language, None)
    Name = property(get_Name, None)
    PlaybackItem = property(get_PlaybackItem, None)
    SupportInfo = property(get_SupportInfo, None)
    TrackKind = property(get_TrackKind, None)
    OpenFailed = event()
class VideoTrackOpenFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IVideoTrackOpenFailedEventArgs
    _classid_ = 'Windows.Media.Core.VideoTrackOpenFailedEventArgs'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.Core.IVideoTrackOpenFailedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class VideoTrackSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Core.IVideoTrackSupportInfo
    _classid_ = 'Windows.Media.Core.VideoTrackSupportInfo'
    @winrt_mixinmethod
    def get_DecoderStatus(self: win32more.Windows.Media.Core.IVideoTrackSupportInfo) -> win32more.Windows.Media.Core.MediaDecoderStatus: ...
    @winrt_mixinmethod
    def get_MediaSourceStatus(self: win32more.Windows.Media.Core.IVideoTrackSupportInfo) -> win32more.Windows.Media.Core.MediaSourceStatus: ...
    DecoderStatus = property(get_DecoderStatus, None)
    MediaSourceStatus = property(get_MediaSourceStatus, None)


make_ready(__name__)
