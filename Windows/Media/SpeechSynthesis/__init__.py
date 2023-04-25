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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media
import Windows.Media.Core
import Windows.Media.SpeechSynthesis
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
class IInstalledVoicesStatic(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d526ecc-7533-4c3f-85-be-88-8c-2b-ae-eb-dc')
    @winrt_commethod(6)
    def get_AllVoices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.SpeechSynthesis.VoiceInformation]: ...
    @winrt_commethod(7)
    def get_DefaultVoice(self) -> Windows.Media.SpeechSynthesis.VoiceInformation: ...
    AllVoices = property(get_AllVoices, None)
    DefaultVoice = property(get_DefaultVoice, None)
class IInstalledVoicesStatic2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64255f2e-358d-4058-be-9a-fd-3f-cb-42-35-30')
    @winrt_commethod(6)
    def TrySetDefaultVoiceAsync(self, voice: Windows.Media.SpeechSynthesis.VoiceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISpeechSynthesisStream(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('83e46e93-244c-4622-ba-0b-62-29-c4-d0-d6-5d')
    @winrt_commethod(6)
    def get_Markers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.IMediaMarker]: ...
    Markers = property(get_Markers, None)
class ISpeechSynthesizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce9f7c76-97f4-4ced-ad-68-d5-1c-45-8e-45-c6')
    @winrt_commethod(6)
    def SynthesizeTextToStreamAsync(self, text: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_commethod(7)
    def SynthesizeSsmlToStreamAsync(self, Ssml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_commethod(8)
    def put_Voice(self, value: Windows.Media.SpeechSynthesis.VoiceInformation) -> Void: ...
    @winrt_commethod(9)
    def get_Voice(self) -> Windows.Media.SpeechSynthesis.VoiceInformation: ...
    Voice = property(get_Voice, put_Voice)
class ISpeechSynthesizer2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a7c5ecb2-4339-4d6a-bb-f8-c7-a4-f1-54-4c-2e')
    @winrt_commethod(6)
    def get_Options(self) -> Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions: ...
    Options = property(get_Options, None)
class ISpeechSynthesizerOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a0e23871-cc3d-43c9-91-b1-ee-18-53-24-d8-3d')
    @winrt_commethod(6)
    def get_IncludeWordBoundaryMetadata(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IncludeWordBoundaryMetadata(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IncludeSentenceBoundaryMetadata(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeSentenceBoundaryMetadata(self, value: Boolean) -> Void: ...
    IncludeWordBoundaryMetadata = property(get_IncludeWordBoundaryMetadata, put_IncludeWordBoundaryMetadata)
    IncludeSentenceBoundaryMetadata = property(get_IncludeSentenceBoundaryMetadata, put_IncludeSentenceBoundaryMetadata)
class ISpeechSynthesizerOptions2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1cbef60e-119c-4bed-b1-18-d2-50-c3-a2-57-93')
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
    AudioVolume = property(get_AudioVolume, put_AudioVolume)
    SpeakingRate = property(get_SpeakingRate, put_SpeakingRate)
    AudioPitch = property(get_AudioPitch, put_AudioPitch)
class ISpeechSynthesizerOptions3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('401ed877-902c-4814-a5-82-a5-d0-c0-76-9f-a8')
    @winrt_commethod(6)
    def get_AppendedSilence(self) -> Windows.Media.SpeechSynthesis.SpeechAppendedSilence: ...
    @winrt_commethod(7)
    def put_AppendedSilence(self, value: Windows.Media.SpeechSynthesis.SpeechAppendedSilence) -> Void: ...
    @winrt_commethod(8)
    def get_PunctuationSilence(self) -> Windows.Media.SpeechSynthesis.SpeechPunctuationSilence: ...
    @winrt_commethod(9)
    def put_PunctuationSilence(self, value: Windows.Media.SpeechSynthesis.SpeechPunctuationSilence) -> Void: ...
    AppendedSilence = property(get_AppendedSilence, put_AppendedSilence)
    PunctuationSilence = property(get_PunctuationSilence, put_PunctuationSilence)
class IVoiceInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b127d6a4-1291-4604-aa-9c-83-13-40-83-35-2c')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Gender(self) -> Windows.Media.SpeechSynthesis.VoiceGender: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    Description = property(get_Description, None)
    Gender = property(get_Gender, None)
SpeechAppendedSilence = Int32
SpeechAppendedSilence_Default: SpeechAppendedSilence = 0
SpeechAppendedSilence_Min: SpeechAppendedSilence = 1
SpeechPunctuationSilence = Int32
SpeechPunctuationSilence_Default: SpeechPunctuationSilence = 0
SpeechPunctuationSilence_Min: SpeechPunctuationSilence = 1
class SpeechSynthesisStream(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.SpeechSynthesis.SpeechSynthesisStream'
    @winrt_mixinmethod
    def get_Markers(self: Windows.Media.SpeechSynthesis.ISpeechSynthesisStream) -> Windows.Foundation.Collections.IVectorView[Windows.Media.IMediaMarker]: ...
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
    def get_TimedMetadataTracks(self: Windows.Media.Core.ITimedMetadataTrackProvider) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Core.TimedMetadataTrack]: ...
    Markers = property(get_Markers, None)
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
    TimedMetadataTracks = property(get_TimedMetadataTracks, None)
class SpeechSynthesizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.SpeechSynthesis.SpeechSynthesizer'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.SpeechSynthesis.SpeechSynthesizer: ...
    @winrt_mixinmethod
    def SynthesizeTextToStreamAsync(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizer, text: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_mixinmethod
    def SynthesizeSsmlToStreamAsync(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizer, Ssml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.SpeechSynthesis.SpeechSynthesisStream]: ...
    @winrt_mixinmethod
    def put_Voice(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizer, value: Windows.Media.SpeechSynthesis.VoiceInformation) -> Void: ...
    @winrt_mixinmethod
    def get_Voice(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizer) -> Windows.Media.SpeechSynthesis.VoiceInformation: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizer2) -> Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions: ...
    @winrt_classmethod
    def TrySetDefaultVoiceAsync(cls: Windows.Media.SpeechSynthesis.IInstalledVoicesStatic2, voice: Windows.Media.SpeechSynthesis.VoiceInformation) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_AllVoices(cls: Windows.Media.SpeechSynthesis.IInstalledVoicesStatic) -> Windows.Foundation.Collections.IVectorView[Windows.Media.SpeechSynthesis.VoiceInformation]: ...
    @winrt_classmethod
    def get_DefaultVoice(cls: Windows.Media.SpeechSynthesis.IInstalledVoicesStatic) -> Windows.Media.SpeechSynthesis.VoiceInformation: ...
    Voice = property(get_Voice, put_Voice)
    Options = property(get_Options, None)
    AllVoices = property(get_AllVoices, None)
    DefaultVoice = property(get_DefaultVoice, None)
class SpeechSynthesizerOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.SpeechSynthesis.SpeechSynthesizerOptions'
    @winrt_mixinmethod
    def get_IncludeWordBoundaryMetadata(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeWordBoundaryMetadata(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeSentenceBoundaryMetadata(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeSentenceBoundaryMetadata(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AudioVolume(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_AudioVolume(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SpeakingRate(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_SpeakingRate(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AudioPitch(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2) -> Double: ...
    @winrt_mixinmethod
    def put_AudioPitch(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions2, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AppendedSilence(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3) -> Windows.Media.SpeechSynthesis.SpeechAppendedSilence: ...
    @winrt_mixinmethod
    def put_AppendedSilence(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3, value: Windows.Media.SpeechSynthesis.SpeechAppendedSilence) -> Void: ...
    @winrt_mixinmethod
    def get_PunctuationSilence(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3) -> Windows.Media.SpeechSynthesis.SpeechPunctuationSilence: ...
    @winrt_mixinmethod
    def put_PunctuationSilence(self: Windows.Media.SpeechSynthesis.ISpeechSynthesizerOptions3, value: Windows.Media.SpeechSynthesis.SpeechPunctuationSilence) -> Void: ...
    IncludeWordBoundaryMetadata = property(get_IncludeWordBoundaryMetadata, put_IncludeWordBoundaryMetadata)
    IncludeSentenceBoundaryMetadata = property(get_IncludeSentenceBoundaryMetadata, put_IncludeSentenceBoundaryMetadata)
    AudioVolume = property(get_AudioVolume, put_AudioVolume)
    SpeakingRate = property(get_SpeakingRate, put_SpeakingRate)
    AudioPitch = property(get_AudioPitch, put_AudioPitch)
    AppendedSilence = property(get_AppendedSilence, put_AppendedSilence)
    PunctuationSilence = property(get_PunctuationSilence, put_PunctuationSilence)
VoiceGender = Int32
VoiceGender_Male: VoiceGender = 0
VoiceGender_Female: VoiceGender = 1
class VoiceInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.SpeechSynthesis.VoiceInformation'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Media.SpeechSynthesis.IVoiceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Gender(self: Windows.Media.SpeechSynthesis.IVoiceInformation) -> Windows.Media.SpeechSynthesis.VoiceGender: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Language = property(get_Language, None)
    Description = property(get_Description, None)
    Gender = property(get_Gender, None)
make_head(_module, 'IInstalledVoicesStatic')
make_head(_module, 'IInstalledVoicesStatic2')
make_head(_module, 'ISpeechSynthesisStream')
make_head(_module, 'ISpeechSynthesizer')
make_head(_module, 'ISpeechSynthesizer2')
make_head(_module, 'ISpeechSynthesizerOptions')
make_head(_module, 'ISpeechSynthesizerOptions2')
make_head(_module, 'ISpeechSynthesizerOptions3')
make_head(_module, 'IVoiceInformation')
make_head(_module, 'SpeechSynthesisStream')
make_head(_module, 'SpeechSynthesizer')
make_head(_module, 'SpeechSynthesizerOptions')
make_head(_module, 'VoiceInformation')
