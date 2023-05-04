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
import Windows.Devices.Enumeration
import Windows.Devices.Midi
import Windows.Foundation
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
class IMidiChannelPressureMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{be1fa860-62b4-4d52-a37e-92e54d35b909}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Pressure(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Pressure = property(get_Pressure, None)
class IMidiChannelPressureMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6218ed2f-2284-412a-94cf-10fb04842c6c}')
    @winrt_commethod(6)
    def CreateMidiChannelPressureMessage(self, channel: Byte, pressure: Byte) -> Windows.Devices.Midi.MidiChannelPressureMessage: ...
class IMidiControlChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b7e15f83-780d-405f-b781-3e1598c97f40}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Controller(self) -> Byte: ...
    @winrt_commethod(8)
    def get_ControlValue(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Controller = property(get_Controller, None)
    ControlValue = property(get_ControlValue, None)
class IMidiControlChangeMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2ab14321-956c-46ad-9752-f87f55052fe3}')
    @winrt_commethod(6)
    def CreateMidiControlChangeMessage(self, channel: Byte, controller: Byte, controlValue: Byte) -> Windows.Devices.Midi.MidiControlChangeMessage: ...
class IMidiInPort(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d5c1d9db-971a-4eaf-a23d-ea19fe607ff9}')
    @winrt_commethod(6)
    def add_MessageReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Midi.MidiInPort, Windows.Devices.Midi.MidiMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IMidiInPortStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{44c439dc-67ff-4a6e-8bac-fdb6610cf296}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiInPort]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMidiMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{79767945-1094-4283-9be0-289fc0ee8334}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_RawData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Type(self) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class IMidiMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{76566e56-f328-4b51-907d-b3a8ce96bf80}')
    @winrt_commethod(6)
    def get_Message(self) -> Windows.Devices.Midi.IMidiMessage: ...
    Message = property(get_Message, None)
class IMidiNoteOffMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{16fd8af4-198e-4d8f-a654-d305a293548f}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Note(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Velocity(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Velocity = property(get_Velocity, None)
class IMidiNoteOffMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a6b240e0-a749-425f-8af4-a4d979cc15b5}')
    @winrt_commethod(6)
    def CreateMidiNoteOffMessage(self, channel: Byte, note: Byte, velocity: Byte) -> Windows.Devices.Midi.MidiNoteOffMessage: ...
class IMidiNoteOnMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e0224af5-6181-46dd-afa2-410004c057aa}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Note(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Velocity(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Velocity = property(get_Velocity, None)
class IMidiNoteOnMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9b4280a0-59c1-420e-b517-15a10aa9606b}')
    @winrt_commethod(6)
    def CreateMidiNoteOnMessage(self, channel: Byte, note: Byte, velocity: Byte) -> Windows.Devices.Midi.MidiNoteOnMessage: ...
class IMidiOutPort(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{931d6d9f-57a2-4a3a-adb8-4640886f6693}')
    @winrt_commethod(6)
    def SendMessage(self, midiMessage: Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_commethod(7)
    def SendBuffer(self, midiData: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IMidiOutPortStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{065cc3e9-0f88-448b-9b64-a95826c65b8f}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.IMidiOutPort]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMidiPitchBendChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{29df4cb1-2e9f-4faf-8c2b-9cb82a9079ca}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Bend(self) -> UInt16: ...
    Channel = property(get_Channel, None)
    Bend = property(get_Bend, None)
class IMidiPitchBendChangeMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f5eedf55-cfc8-4926-b30e-a3622393306c}')
    @winrt_commethod(6)
    def CreateMidiPitchBendChangeMessage(self, channel: Byte, bend: UInt16) -> Windows.Devices.Midi.MidiPitchBendChangeMessage: ...
class IMidiPolyphonicKeyPressureMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1f7337fe-ace8-48a0-868e-7cdbf20f04d6}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Note(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Pressure(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Pressure = property(get_Pressure, None)
class IMidiPolyphonicKeyPressureMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e98f483e-c4b3-4dd2-917c-e349815a1b3b}')
    @winrt_commethod(6)
    def CreateMidiPolyphonicKeyPressureMessage(self, channel: Byte, note: Byte, pressure: Byte) -> Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage: ...
class IMidiProgramChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9cbb3c78-7a3e-4327-aa98-20b8e4485af8}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Program(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Program = property(get_Program, None)
class IMidiProgramChangeMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d6b04387-524b-4104-9c99-6572bfd2e261}')
    @winrt_commethod(6)
    def CreateMidiProgramChangeMessage(self, channel: Byte, program: Byte) -> Windows.Devices.Midi.MidiProgramChangeMessage: ...
class IMidiSongPositionPointerMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4ca50c56-ec5e-4ae4-a115-88dc57cc2b79}')
    @winrt_commethod(6)
    def get_Beats(self) -> UInt16: ...
    Beats = property(get_Beats, None)
class IMidiSongPositionPointerMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9c00e996-f10b-4fea-b395-f5d6cf80f64e}')
    @winrt_commethod(6)
    def CreateMidiSongPositionPointerMessage(self, beats: UInt16) -> Windows.Devices.Midi.MidiSongPositionPointerMessage: ...
class IMidiSongSelectMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{49f0f27f-6d83-4741-a5bf-4629f6be974f}')
    @winrt_commethod(6)
    def get_Song(self) -> Byte: ...
    Song = property(get_Song, None)
class IMidiSongSelectMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{848878e4-8748-4129-a66c-a05493f75daa}')
    @winrt_commethod(6)
    def CreateMidiSongSelectMessage(self, song: Byte) -> Windows.Devices.Midi.MidiSongSelectMessage: ...
class IMidiSynthesizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f0da155e-db90-405f-b8ae-21d2e17f2e45}')
    @winrt_commethod(6)
    def get_AudioDevice(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(8)
    def put_Volume(self, value: Double) -> Void: ...
    AudioDevice = property(get_AudioDevice, None)
    Volume = property(get_Volume, put_Volume)
class IMidiSynthesizerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4224eaa8-6629-4d6b-aa8f-d4521a5a31ce}')
    @winrt_commethod(6)
    def CreateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_commethod(7)
    def CreateFromAudioDeviceAsync(self, audioDevice: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_commethod(8)
    def IsSynthesizer(self, midiDevice: Windows.Devices.Enumeration.DeviceInformation) -> Boolean: ...
class IMidiSystemExclusiveMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{083de222-3b74-4320-9b42-0ca8545f8a24}')
    @winrt_commethod(6)
    def CreateMidiSystemExclusiveMessage(self, rawData: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Midi.MidiSystemExclusiveMessage: ...
class IMidiTimeCodeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0bf7087d-fa63-4a1c-8deb-c0e87796a6d7}')
    @winrt_commethod(6)
    def get_FrameType(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Values(self) -> Byte: ...
    FrameType = property(get_FrameType, None)
    Values = property(get_Values, None)
class IMidiTimeCodeMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{eb3099c5-771c-40de-b961-175a7489a85e}')
    @winrt_commethod(6)
    def CreateMidiTimeCodeMessage(self, frameType: Byte, values: Byte) -> Windows.Devices.Midi.MidiTimeCodeMessage: ...
class MidiActiveSensingMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiActiveSensingMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiActiveSensingMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiChannelPressureMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiChannelPressureMessage'
    @winrt_factorymethod
    def CreateMidiChannelPressureMessage(cls: Windows.Devices.Midi.IMidiChannelPressureMessageFactory, channel: Byte, pressure: Byte) -> Windows.Devices.Midi.MidiChannelPressureMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiChannelPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Pressure(self: Windows.Devices.Midi.IMidiChannelPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Pressure = property(get_Pressure, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiContinueMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiContinueMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiContinueMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiControlChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiControlChangeMessage'
    @winrt_factorymethod
    def CreateMidiControlChangeMessage(cls: Windows.Devices.Midi.IMidiControlChangeMessageFactory, channel: Byte, controller: Byte, controlValue: Byte) -> Windows.Devices.Midi.MidiControlChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Controller(self: Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_ControlValue(self: Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Controller = property(get_Controller, None)
    ControlValue = property(get_ControlValue, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiInPort(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiInPort'
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Devices.Midi.IMidiInPort, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Midi.MidiInPort, Windows.Devices.Midi.MidiMessageReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Devices.Midi.IMidiInPort, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Midi.IMidiInPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Midi.IMidiInPortStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiInPort]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Midi.IMidiInPortStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class MidiMessageReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: Windows.Devices.Midi.IMidiMessageReceivedEventArgs) -> Windows.Devices.Midi.IMidiMessage: ...
    Message = property(get_Message, None)
MidiMessageType = Int32
MidiMessageType_None: MidiMessageType = 0
MidiMessageType_NoteOff: MidiMessageType = 128
MidiMessageType_NoteOn: MidiMessageType = 144
MidiMessageType_PolyphonicKeyPressure: MidiMessageType = 160
MidiMessageType_ControlChange: MidiMessageType = 176
MidiMessageType_ProgramChange: MidiMessageType = 192
MidiMessageType_ChannelPressure: MidiMessageType = 208
MidiMessageType_PitchBendChange: MidiMessageType = 224
MidiMessageType_SystemExclusive: MidiMessageType = 240
MidiMessageType_MidiTimeCode: MidiMessageType = 241
MidiMessageType_SongPositionPointer: MidiMessageType = 242
MidiMessageType_SongSelect: MidiMessageType = 243
MidiMessageType_TuneRequest: MidiMessageType = 246
MidiMessageType_EndSystemExclusive: MidiMessageType = 247
MidiMessageType_TimingClock: MidiMessageType = 248
MidiMessageType_Start: MidiMessageType = 250
MidiMessageType_Continue: MidiMessageType = 251
MidiMessageType_Stop: MidiMessageType = 252
MidiMessageType_ActiveSensing: MidiMessageType = 254
MidiMessageType_SystemReset: MidiMessageType = 255
class MidiNoteOffMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiNoteOffMessage'
    @winrt_factorymethod
    def CreateMidiNoteOffMessage(cls: Windows.Devices.Midi.IMidiNoteOffMessageFactory, channel: Byte, note: Byte, velocity: Byte) -> Windows.Devices.Midi.MidiNoteOffMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Velocity(self: Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Velocity = property(get_Velocity, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiNoteOnMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiNoteOnMessage'
    @winrt_factorymethod
    def CreateMidiNoteOnMessage(cls: Windows.Devices.Midi.IMidiNoteOnMessageFactory, channel: Byte, note: Byte, velocity: Byte) -> Windows.Devices.Midi.MidiNoteOnMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Velocity(self: Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Velocity = property(get_Velocity, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiOutPort(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiOutPort'
    @winrt_mixinmethod
    def SendMessage(self: Windows.Devices.Midi.IMidiOutPort, midiMessage: Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_mixinmethod
    def SendBuffer(self: Windows.Devices.Midi.IMidiOutPort, midiData: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Midi.IMidiOutPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Midi.IMidiOutPortStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.IMidiOutPort]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Midi.IMidiOutPortStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class MidiPitchBendChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiPitchBendChangeMessage'
    @winrt_factorymethod
    def CreateMidiPitchBendChangeMessage(cls: Windows.Devices.Midi.IMidiPitchBendChangeMessageFactory, channel: Byte, bend: UInt16) -> Windows.Devices.Midi.MidiPitchBendChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiPitchBendChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Bend(self: Windows.Devices.Midi.IMidiPitchBendChangeMessage) -> UInt16: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Bend = property(get_Bend, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiPolyphonicKeyPressureMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage'
    @winrt_factorymethod
    def CreateMidiPolyphonicKeyPressureMessage(cls: Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessageFactory, channel: Byte, note: Byte, pressure: Byte) -> Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Pressure(self: Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Pressure = property(get_Pressure, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiProgramChangeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiProgramChangeMessage'
    @winrt_factorymethod
    def CreateMidiProgramChangeMessage(cls: Windows.Devices.Midi.IMidiProgramChangeMessageFactory, channel: Byte, program: Byte) -> Windows.Devices.Midi.MidiProgramChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Midi.IMidiProgramChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Program(self: Windows.Devices.Midi.IMidiProgramChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Program = property(get_Program, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiSongPositionPointerMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiSongPositionPointerMessage'
    @winrt_factorymethod
    def CreateMidiSongPositionPointerMessage(cls: Windows.Devices.Midi.IMidiSongPositionPointerMessageFactory, beats: UInt16) -> Windows.Devices.Midi.MidiSongPositionPointerMessage: ...
    @winrt_mixinmethod
    def get_Beats(self: Windows.Devices.Midi.IMidiSongPositionPointerMessage) -> UInt16: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Beats = property(get_Beats, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiSongSelectMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiSongSelectMessage'
    @winrt_factorymethod
    def CreateMidiSongSelectMessage(cls: Windows.Devices.Midi.IMidiSongSelectMessageFactory, song: Byte) -> Windows.Devices.Midi.MidiSongSelectMessage: ...
    @winrt_mixinmethod
    def get_Song(self: Windows.Devices.Midi.IMidiSongSelectMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Song = property(get_Song, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiStartMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiStartMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiStartMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiStopMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiStopMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiStopMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiSynthesizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiSynthesizer'
    @winrt_mixinmethod
    def get_AudioDevice(self: Windows.Devices.Midi.IMidiSynthesizer) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Volume(self: Windows.Devices.Midi.IMidiSynthesizer) -> Double: ...
    @winrt_mixinmethod
    def put_Volume(self: Windows.Devices.Midi.IMidiSynthesizer, value: Double) -> Void: ...
    @winrt_mixinmethod
    def SendMessage(self: Windows.Devices.Midi.IMidiOutPort, midiMessage: Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_mixinmethod
    def SendBuffer(self: Windows.Devices.Midi.IMidiOutPort, midiData: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Midi.IMidiOutPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Devices.Midi.IMidiSynthesizerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_classmethod
    def CreateFromAudioDeviceAsync(cls: Windows.Devices.Midi.IMidiSynthesizerStatics, audioDevice: Windows.Devices.Enumeration.DeviceInformation) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_classmethod
    def IsSynthesizer(cls: Windows.Devices.Midi.IMidiSynthesizerStatics, midiDevice: Windows.Devices.Enumeration.DeviceInformation) -> Boolean: ...
    AudioDevice = property(get_AudioDevice, None)
    Volume = property(get_Volume, put_Volume)
    DeviceId = property(get_DeviceId, None)
class MidiSystemExclusiveMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiSystemExclusiveMessage'
    @winrt_factorymethod
    def CreateMidiSystemExclusiveMessage(cls: Windows.Devices.Midi.IMidiSystemExclusiveMessageFactory, rawData: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Midi.MidiSystemExclusiveMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiSystemResetMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiSystemResetMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiSystemResetMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiTimeCodeMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiTimeCodeMessage'
    @winrt_factorymethod
    def CreateMidiTimeCodeMessage(cls: Windows.Devices.Midi.IMidiTimeCodeMessageFactory, frameType: Byte, values: Byte) -> Windows.Devices.Midi.MidiTimeCodeMessage: ...
    @winrt_mixinmethod
    def get_FrameType(self: Windows.Devices.Midi.IMidiTimeCodeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Values(self: Windows.Devices.Midi.IMidiTimeCodeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    FrameType = property(get_FrameType, None)
    Values = property(get_Values, None)
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiTimingClockMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiTimingClockMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiTimingClockMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
class MidiTuneRequestMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.MidiTuneRequestMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Midi.MidiTuneRequestMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.Midi.IMidiMessage) -> Windows.Devices.Midi.MidiMessageType: ...
    Timestamp = property(get_Timestamp, None)
    RawData = property(get_RawData, None)
    Type = property(get_Type, None)
make_head(_module, 'IMidiChannelPressureMessage')
make_head(_module, 'IMidiChannelPressureMessageFactory')
make_head(_module, 'IMidiControlChangeMessage')
make_head(_module, 'IMidiControlChangeMessageFactory')
make_head(_module, 'IMidiInPort')
make_head(_module, 'IMidiInPortStatics')
make_head(_module, 'IMidiMessage')
make_head(_module, 'IMidiMessageReceivedEventArgs')
make_head(_module, 'IMidiNoteOffMessage')
make_head(_module, 'IMidiNoteOffMessageFactory')
make_head(_module, 'IMidiNoteOnMessage')
make_head(_module, 'IMidiNoteOnMessageFactory')
make_head(_module, 'IMidiOutPort')
make_head(_module, 'IMidiOutPortStatics')
make_head(_module, 'IMidiPitchBendChangeMessage')
make_head(_module, 'IMidiPitchBendChangeMessageFactory')
make_head(_module, 'IMidiPolyphonicKeyPressureMessage')
make_head(_module, 'IMidiPolyphonicKeyPressureMessageFactory')
make_head(_module, 'IMidiProgramChangeMessage')
make_head(_module, 'IMidiProgramChangeMessageFactory')
make_head(_module, 'IMidiSongPositionPointerMessage')
make_head(_module, 'IMidiSongPositionPointerMessageFactory')
make_head(_module, 'IMidiSongSelectMessage')
make_head(_module, 'IMidiSongSelectMessageFactory')
make_head(_module, 'IMidiSynthesizer')
make_head(_module, 'IMidiSynthesizerStatics')
make_head(_module, 'IMidiSystemExclusiveMessageFactory')
make_head(_module, 'IMidiTimeCodeMessage')
make_head(_module, 'IMidiTimeCodeMessageFactory')
make_head(_module, 'MidiActiveSensingMessage')
make_head(_module, 'MidiChannelPressureMessage')
make_head(_module, 'MidiContinueMessage')
make_head(_module, 'MidiControlChangeMessage')
make_head(_module, 'MidiInPort')
make_head(_module, 'MidiMessageReceivedEventArgs')
make_head(_module, 'MidiNoteOffMessage')
make_head(_module, 'MidiNoteOnMessage')
make_head(_module, 'MidiOutPort')
make_head(_module, 'MidiPitchBendChangeMessage')
make_head(_module, 'MidiPolyphonicKeyPressureMessage')
make_head(_module, 'MidiProgramChangeMessage')
make_head(_module, 'MidiSongPositionPointerMessage')
make_head(_module, 'MidiSongSelectMessage')
make_head(_module, 'MidiStartMessage')
make_head(_module, 'MidiStopMessage')
make_head(_module, 'MidiSynthesizer')
make_head(_module, 'MidiSystemExclusiveMessage')
make_head(_module, 'MidiSystemResetMessage')
make_head(_module, 'MidiTimeCodeMessage')
make_head(_module, 'MidiTimingClockMessage')
make_head(_module, 'MidiTuneRequestMessage')
