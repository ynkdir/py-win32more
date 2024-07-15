from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media
import win32more.Windows.Media.Core
import win32more.Windows.Media.SpeechSynthesis
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IInstalledVoicesStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.IInstalledVoicesStatic'
    _iid_ = Guid('{7d526ecc-7533-4c3f-85be-888c2baeebdc}')
    @winrt_commethod(6)
    def get_AllVoices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.SpeechSynthesis.VoiceInformation]: ...
    @winrt_commethod(7)
    def get_DefaultVoice(self) -> win32more.Windows.Media.SpeechSynthesis.VoiceInformation: ...
    AllVoices = property(get_AllVoices, None)
    DefaultVoice = property(get_DefaultVoice, None)
class IInstalledVoicesStatic2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.IInstalledVoicesStatic2'
    _iid_ = Guid('{64255f2e-358d-4058-be9a-fd3fcb423530}')
    @winrt_commethod(6)
    def TrySetDefaultVoiceAsync(self, voice: win32more.Windows.Media.SpeechSynthesis.VoiceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpeechSynthesisStream(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesisStream'
    _iid_ = Guid('{83e46e93-244c-4622-ba0b-6229c4d0d65d}')
    @winrt_commethod(6)
    def get_Markers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.IMediaMarker]: ...
    Markers = property(get_Markers, None)
class ISpeechSynthesizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesizer'
    _iid_ = Guid('{ce9f7c76-97f4-4ced-ad68-d51c458e45c6}')
    @winrt_commethod(6)
    def SynthesizeTextToStreamAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_commethod(7)
    def SynthesizeSsmlToStreamAsync(self, Ssml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_commethod(8)
    def put_Voice(self, value: win32more.Windows.Media.SpeechSynthesis.VoiceInformation) -> Void: ...
    @winrt_commethod(9)
    def get_Voice(self) -> win32more.Windows.Media.SpeechSynthesis.VoiceInformation: ...
    Voice = property(get_Voice, put_Voice)
class ISpeechSynthesizer2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesizer2'
    _iid_ = Guid('{a7c5ecb2-4339-4d6a-bbf8-c7a4f1544c2e}')
    @winrt_commethod(6)
    def get_Options(self) -> win32more.Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions: ...
    Options = property(get_Options, None)
class ISpeechSynthesizerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions'
    _iid_ = Guid('{a0e23871-cc3d-43c9-91b1-ee185324d83d}')
    @winrt_commethod(6)
    def get_IncludeWordBoundaryMetadata(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IncludeWordBoundaryMetadata(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IncludeSentenceBoundaryMetadata(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeSentenceBoundaryMetadata(self, value: Boolean) -> Void: ...
    IncludeSentenceBoundaryMetadata = property(get_IncludeSentenceBoundaryMetadata, put_IncludeSentenceBoundaryMetadata)
    IncludeWordBoundaryMetadata = property(get_IncludeWordBoundaryMetadata, put_IncludeWordBoundaryMetadata)
class ISpeechSynthesizerOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2'
    _iid_ = Guid('{1cbef60e-119c-4bed-b118-d250c3a25793}')
    @winrt_commethod(6)
    def get_AudioVolume(self) -> Double: ...
    @winrt_commethod(7)
    def put_AudioVolume(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_SpeakingRate(self) -> Double: ...
    @winrt_commethod(9)
    def put_SpeakingRate(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_AudioPitch(self) -> Double: ...
    @winrt_commethod(11)
    def put_AudioPitch(self, value: Double) -> Void: ...
    AudioPitch = property(get_AudioPitch, put_AudioPitch)
    AudioVolume = property(get_AudioVolume, put_AudioVolume)
    SpeakingRate = property(get_SpeakingRate, put_SpeakingRate)
class ISpeechSynthesizerOptions3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3'
    _iid_ = Guid('{401ed877-902c-4814-a582-a5d0c0769fa8}')
    @winrt_commethod(6)
    def get_AppendedSilence(self) -> win32more.Windows.Media.SpeechSynthesis.SpeechAppendedSilence: ...
    @winrt_commethod(7)
    def put_AppendedSilence(self, value: win32more.Windows.Media.SpeechSynthesis.SpeechAppendedSilence) -> Void: ...
    @winrt_commethod(8)
    def get_PunctuationSilence(self) -> win32more.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence: ...
    @winrt_commethod(9)
    def put_PunctuationSilence(self, value: win32more.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence) -> Void: ...
    AppendedSilence = property(get_AppendedSilence, put_AppendedSilence)
    PunctuationSilence = property(get_PunctuationSilence, put_PunctuationSilence)
class IVoiceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.SpeechSynthesis.IVoiceInformation'
    _iid_ = Guid('{b127d6a4-1291-4604-aa9c-83134083352c}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Gender(self) -> win32more.Windows.Media.SpeechSynthesis.VoiceGender: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Gender = property(get_Gender, None)
    Id = property(get_Id, None)
    Language = property(get_Language, None)
class SpeechAppendedSilence(Enum, Int32):
    Default = 0
    Min = 1
class SpeechPunctuationSilence(Enum, Int32):
    Default = 0
    Min = 1
class SpeechSynthesisStream(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesisStream
    _classid_ = 'Windows.Media.SpeechSynthesis.SpeechSynthesisStream'
    @winrt_mixinmethod
    def get_Markers(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesisStream) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.IMediaMarker]: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TimedMetadataTracks(self: win32more.Windows.Media.Core.ITimedMetadataTrackProvider) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Core.TimedMetadataTrack]: ...
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
    Markers = property(get_Markers, None)
    Position = property(get_Position, None)
    Size = property(get_Size, put_Size)
    TimedMetadataTracks = property(get_TimedMetadataTracks, None)
class _SpeechSynthesizer_Meta_(ComPtr.__class__):
    pass
class SpeechSynthesizer(ComPtr, metaclass=_SpeechSynthesizer_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer
    _classid_ = 'Windows.Media.SpeechSynthesis.SpeechSynthesizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.SpeechSynthesis.SpeechSynthesizer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.SpeechSynthesis.SpeechSynthesizer: ...
    @winrt_mixinmethod
    def SynthesizeTextToStreamAsync(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_mixinmethod
    def SynthesizeSsmlToStreamAsync(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer, Ssml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_mixinmethod
    def put_Voice(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer, value: win32more.Windows.Media.SpeechSynthesis.VoiceInformation) -> Void: ...
    @winrt_mixinmethod
    def get_Voice(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer) -> win32more.Windows.Media.SpeechSynthesis.VoiceInformation: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizer2) -> win32more.Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions: ...
    @winrt_classmethod
    def TrySetDefaultVoiceAsync(cls: win32more.Windows.Media.SpeechSynthesis.IInstalledVoicesStatic2, voice: win32more.Windows.Media.SpeechSynthesis.VoiceInformation) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_AllVoices(cls: win32more.Windows.Media.SpeechSynthesis.IInstalledVoicesStatic) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.SpeechSynthesis.VoiceInformation]: ...
    @winrt_classmethod
    def get_DefaultVoice(cls: win32more.Windows.Media.SpeechSynthesis.IInstalledVoicesStatic) -> win32more.Windows.Media.SpeechSynthesis.VoiceInformation: ...
    Options = property(get_Options, None)
    Voice = property(get_Voice, put_Voice)
    _SpeechSynthesizer_Meta_.AllVoices = property(get_AllVoices, None)
    _SpeechSynthesizer_Meta_.DefaultVoice = property(get_DefaultVoice, None)
class SpeechSynthesizerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions
    _classid_ = 'Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions'
    @winrt_mixinmethod
    def get_IncludeWordBoundaryMetadata(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeWordBoundaryMetadata(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeSentenceBoundaryMetadata(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeSentenceBoundaryMetadata(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AudioVolume(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_AudioVolume(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SpeakingRate(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_SpeakingRate(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AudioPitch(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_AudioPitch(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AppendedSilence(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3) -> win32more.Windows.Media.SpeechSynthesis.SpeechAppendedSilence: ...
    @winrt_mixinmethod
    def put_AppendedSilence(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3, value: win32more.Windows.Media.SpeechSynthesis.SpeechAppendedSilence) -> Void: ...
    @winrt_mixinmethod
    def get_PunctuationSilence(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3) -> win32more.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence: ...
    @winrt_mixinmethod
    def put_PunctuationSilence(self: win32more.Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3, value: win32more.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence) -> Void: ...
    AppendedSilence = property(get_AppendedSilence, put_AppendedSilence)
    AudioPitch = property(get_AudioPitch, put_AudioPitch)
    AudioVolume = property(get_AudioVolume, put_AudioVolume)
    IncludeSentenceBoundaryMetadata = property(get_IncludeSentenceBoundaryMetadata, put_IncludeSentenceBoundaryMetadata)
    IncludeWordBoundaryMetadata = property(get_IncludeWordBoundaryMetadata, put_IncludeWordBoundaryMetadata)
    PunctuationSilence = property(get_PunctuationSilence, put_PunctuationSilence)
    SpeakingRate = property(get_SpeakingRate, put_SpeakingRate)
class VoiceGender(Enum, Int32):
    Male = 0
    Female = 1
class VoiceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation
    _classid_ = 'Windows.Media.SpeechSynthesis.VoiceInformation'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Gender(self: win32more.Windows.Media.SpeechSynthesis.IVoiceInformation) -> win32more.Windows.Media.SpeechSynthesis.VoiceGender: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Gender = property(get_Gender, None)
    Id = property(get_Id, None)
    Language = property(get_Language, None)


make_ready(__name__)
