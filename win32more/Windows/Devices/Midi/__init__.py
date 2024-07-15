from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Midi
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IMidiChannelPressureMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiChannelPressureMessage'
    _iid_ = Guid('{be1fa860-62b4-4d52-a37e-92e54d35b909}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Pressure(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Pressure = property(get_Pressure, None)
class IMidiChannelPressureMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiChannelPressureMessageFactory'
    _iid_ = Guid('{6218ed2f-2284-412a-94cf-10fb04842c6c}')
    @winrt_commethod(6)
    def CreateMidiChannelPressureMessage(self, channel: Byte, pressure: Byte) -> win32more.Windows.Devices.Midi.MidiChannelPressureMessage: ...
class IMidiControlChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiControlChangeMessage'
    _iid_ = Guid('{b7e15f83-780d-405f-b781-3e1598c97f40}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Controller(self) -> Byte: ...
    @winrt_commethod(8)
    def get_ControlValue(self) -> Byte: ...
    Channel = property(get_Channel, None)
    ControlValue = property(get_ControlValue, None)
    Controller = property(get_Controller, None)
class IMidiControlChangeMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiControlChangeMessageFactory'
    _iid_ = Guid('{2ab14321-956c-46ad-9752-f87f55052fe3}')
    @winrt_commethod(6)
    def CreateMidiControlChangeMessage(self, channel: Byte, controller: Byte, controlValue: Byte) -> win32more.Windows.Devices.Midi.MidiControlChangeMessage: ...
class IMidiInPort(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Midi.IMidiInPort'
    _iid_ = Guid('{d5c1d9db-971a-4eaf-a23d-ea19fe607ff9}')
    @winrt_commethod(6)
    def add_MessageReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Midi.MidiInPort, win32more.Windows.Devices.Midi.MidiMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    MessageReceived = event()
class IMidiInPortStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiInPortStatics'
    _iid_ = Guid('{44c439dc-67ff-4a6e-8bac-fdb6610cf296}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiInPort]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMidiMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiMessage'
    _iid_ = Guid('{79767945-1094-4283-9be0-289fc0ee8334}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_RawData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Type(self) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class IMidiMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiMessageReceivedEventArgs'
    _iid_ = Guid('{76566e56-f328-4b51-907d-b3a8ce96bf80}')
    @winrt_commethod(6)
    def get_Message(self) -> win32more.Windows.Devices.Midi.IMidiMessage: ...
    Message = property(get_Message, None)
class IMidiNoteOffMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiNoteOffMessage'
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiNoteOffMessageFactory'
    _iid_ = Guid('{a6b240e0-a749-425f-8af4-a4d979cc15b5}')
    @winrt_commethod(6)
    def CreateMidiNoteOffMessage(self, channel: Byte, note: Byte, velocity: Byte) -> win32more.Windows.Devices.Midi.MidiNoteOffMessage: ...
class IMidiNoteOnMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiNoteOnMessage'
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiNoteOnMessageFactory'
    _iid_ = Guid('{9b4280a0-59c1-420e-b517-15a10aa9606b}')
    @winrt_commethod(6)
    def CreateMidiNoteOnMessage(self, channel: Byte, note: Byte, velocity: Byte) -> win32more.Windows.Devices.Midi.MidiNoteOnMessage: ...
class IMidiOutPort(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Midi.IMidiOutPort'
    _iid_ = Guid('{931d6d9f-57a2-4a3a-adb8-4640886f6693}')
    @winrt_commethod(6)
    def SendMessage(self, midiMessage: win32more.Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_commethod(7)
    def SendBuffer(self, midiData: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IMidiOutPortStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiOutPortStatics'
    _iid_ = Guid('{065cc3e9-0f88-448b-9b64-a95826c65b8f}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.IMidiOutPort]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMidiPitchBendChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiPitchBendChangeMessage'
    _iid_ = Guid('{29df4cb1-2e9f-4faf-8c2b-9cb82a9079ca}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Bend(self) -> UInt16: ...
    Bend = property(get_Bend, None)
    Channel = property(get_Channel, None)
class IMidiPitchBendChangeMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiPitchBendChangeMessageFactory'
    _iid_ = Guid('{f5eedf55-cfc8-4926-b30e-a3622393306c}')
    @winrt_commethod(6)
    def CreateMidiPitchBendChangeMessage(self, channel: Byte, bend: UInt16) -> win32more.Windows.Devices.Midi.MidiPitchBendChangeMessage: ...
class IMidiPolyphonicKeyPressureMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage'
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessageFactory'
    _iid_ = Guid('{e98f483e-c4b3-4dd2-917c-e349815a1b3b}')
    @winrt_commethod(6)
    def CreateMidiPolyphonicKeyPressureMessage(self, channel: Byte, note: Byte, pressure: Byte) -> win32more.Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage: ...
class IMidiProgramChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiProgramChangeMessage'
    _iid_ = Guid('{9cbb3c78-7a3e-4327-aa98-20b8e4485af8}')
    @winrt_commethod(6)
    def get_Channel(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Program(self) -> Byte: ...
    Channel = property(get_Channel, None)
    Program = property(get_Program, None)
class IMidiProgramChangeMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiProgramChangeMessageFactory'
    _iid_ = Guid('{d6b04387-524b-4104-9c99-6572bfd2e261}')
    @winrt_commethod(6)
    def CreateMidiProgramChangeMessage(self, channel: Byte, program: Byte) -> win32more.Windows.Devices.Midi.MidiProgramChangeMessage: ...
class IMidiSongPositionPointerMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSongPositionPointerMessage'
    _iid_ = Guid('{4ca50c56-ec5e-4ae4-a115-88dc57cc2b79}')
    @winrt_commethod(6)
    def get_Beats(self) -> UInt16: ...
    Beats = property(get_Beats, None)
class IMidiSongPositionPointerMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSongPositionPointerMessageFactory'
    _iid_ = Guid('{9c00e996-f10b-4fea-b395-f5d6cf80f64e}')
    @winrt_commethod(6)
    def CreateMidiSongPositionPointerMessage(self, beats: UInt16) -> win32more.Windows.Devices.Midi.MidiSongPositionPointerMessage: ...
class IMidiSongSelectMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSongSelectMessage'
    _iid_ = Guid('{49f0f27f-6d83-4741-a5bf-4629f6be974f}')
    @winrt_commethod(6)
    def get_Song(self) -> Byte: ...
    Song = property(get_Song, None)
class IMidiSongSelectMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSongSelectMessageFactory'
    _iid_ = Guid('{848878e4-8748-4129-a66c-a05493f75daa}')
    @winrt_commethod(6)
    def CreateMidiSongSelectMessage(self, song: Byte) -> win32more.Windows.Devices.Midi.MidiSongSelectMessage: ...
class IMidiSynthesizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Midi.IMidiSynthesizer'
    _iid_ = Guid('{f0da155e-db90-405f-b8ae-21d2e17f2e45}')
    @winrt_commethod(6)
    def get_AudioDevice(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_Volume(self) -> Double: ...
    @winrt_commethod(8)
    def put_Volume(self, value: Double) -> Void: ...
    AudioDevice = property(get_AudioDevice, None)
    Volume = property(get_Volume, put_Volume)
class IMidiSynthesizerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSynthesizerStatics'
    _iid_ = Guid('{4224eaa8-6629-4d6b-aa8f-d4521a5a31ce}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_commethod(7)
    def CreateFromAudioDeviceAsync(self, audioDevice: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_commethod(8)
    def IsSynthesizer(self, midiDevice: win32more.Windows.Devices.Enumeration.DeviceInformation) -> Boolean: ...
class IMidiSystemExclusiveMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiSystemExclusiveMessageFactory'
    _iid_ = Guid('{083de222-3b74-4320-9b42-0ca8545f8a24}')
    @winrt_commethod(6)
    def CreateMidiSystemExclusiveMessage(self, rawData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Midi.MidiSystemExclusiveMessage: ...
class IMidiTimeCodeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiTimeCodeMessage'
    _iid_ = Guid('{0bf7087d-fa63-4a1c-8deb-c0e87796a6d7}')
    @winrt_commethod(6)
    def get_FrameType(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Values(self) -> Byte: ...
    FrameType = property(get_FrameType, None)
    Values = property(get_Values, None)
class IMidiTimeCodeMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Midi.IMidiTimeCodeMessageFactory'
    _iid_ = Guid('{eb3099c5-771c-40de-b961-175a7489a85e}')
    @winrt_commethod(6)
    def CreateMidiTimeCodeMessage(self, frameType: Byte, values: Byte) -> win32more.Windows.Devices.Midi.MidiTimeCodeMessage: ...
class MidiActiveSensingMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiActiveSensingMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiActiveSensingMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiActiveSensingMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiChannelPressureMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiChannelPressureMessage
    _classid_ = 'Windows.Devices.Midi.MidiChannelPressureMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiChannelPressureMessage.CreateMidiChannelPressureMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiChannelPressureMessage(cls: win32more.Windows.Devices.Midi.IMidiChannelPressureMessageFactory, channel: Byte, pressure: Byte) -> win32more.Windows.Devices.Midi.MidiChannelPressureMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiChannelPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.Devices.Midi.IMidiChannelPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Pressure = property(get_Pressure, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiContinueMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiContinueMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiContinueMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiContinueMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiControlChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiControlChangeMessage
    _classid_ = 'Windows.Devices.Midi.MidiControlChangeMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiControlChangeMessage.CreateMidiControlChangeMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiControlChangeMessage(cls: win32more.Windows.Devices.Midi.IMidiControlChangeMessageFactory, channel: Byte, controller: Byte, controlValue: Byte) -> win32more.Windows.Devices.Midi.MidiControlChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_ControlValue(self: win32more.Windows.Devices.Midi.IMidiControlChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    ControlValue = property(get_ControlValue, None)
    Controller = property(get_Controller, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiInPort(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Midi.IMidiInPort
    _classid_ = 'Windows.Devices.Midi.MidiInPort'
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Devices.Midi.IMidiInPort, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Midi.MidiInPort, win32more.Windows.Devices.Midi.MidiMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Devices.Midi.IMidiInPort, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Midi.IMidiInPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Midi.IMidiInPortStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiInPort]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Midi.IMidiInPortStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    MessageReceived = event()
class MidiMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessageReceivedEventArgs
    _classid_ = 'Windows.Devices.Midi.MidiMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Devices.Midi.IMidiMessageReceivedEventArgs) -> win32more.Windows.Devices.Midi.IMidiMessage: ...
    Message = property(get_Message, None)
class MidiMessageType(Enum, Int32):
    None_ = 0
    NoteOff = 128
    NoteOn = 144
    PolyphonicKeyPressure = 160
    ControlChange = 176
    ProgramChange = 192
    ChannelPressure = 208
    PitchBendChange = 224
    SystemExclusive = 240
    MidiTimeCode = 241
    SongPositionPointer = 242
    SongSelect = 243
    TuneRequest = 246
    EndSystemExclusive = 247
    TimingClock = 248
    Start = 250
    Continue = 251
    Stop = 252
    ActiveSensing = 254
    SystemReset = 255
class MidiNoteOffMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiNoteOffMessage
    _classid_ = 'Windows.Devices.Midi.MidiNoteOffMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiNoteOffMessage.CreateMidiNoteOffMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiNoteOffMessage(cls: win32more.Windows.Devices.Midi.IMidiNoteOffMessageFactory, channel: Byte, note: Byte, velocity: Byte) -> win32more.Windows.Devices.Midi.MidiNoteOffMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: win32more.Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Velocity(self: win32more.Windows.Devices.Midi.IMidiNoteOffMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
    Velocity = property(get_Velocity, None)
class MidiNoteOnMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiNoteOnMessage
    _classid_ = 'Windows.Devices.Midi.MidiNoteOnMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiNoteOnMessage.CreateMidiNoteOnMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiNoteOnMessage(cls: win32more.Windows.Devices.Midi.IMidiNoteOnMessageFactory, channel: Byte, note: Byte, velocity: Byte) -> win32more.Windows.Devices.Midi.MidiNoteOnMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: win32more.Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Velocity(self: win32more.Windows.Devices.Midi.IMidiNoteOnMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
    Velocity = property(get_Velocity, None)
class MidiOutPort(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Midi.IMidiOutPort
    _classid_ = 'Windows.Devices.Midi.MidiOutPort'
    @winrt_mixinmethod
    def SendMessage(self: win32more.Windows.Devices.Midi.IMidiOutPort, midiMessage: win32more.Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_mixinmethod
    def SendBuffer(self: win32more.Windows.Devices.Midi.IMidiOutPort, midiData: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Midi.IMidiOutPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Midi.IMidiOutPortStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.IMidiOutPort]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Midi.IMidiOutPortStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class MidiPitchBendChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiPitchBendChangeMessage
    _classid_ = 'Windows.Devices.Midi.MidiPitchBendChangeMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiPitchBendChangeMessage.CreateMidiPitchBendChangeMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiPitchBendChangeMessage(cls: win32more.Windows.Devices.Midi.IMidiPitchBendChangeMessageFactory, channel: Byte, bend: UInt16) -> win32more.Windows.Devices.Midi.MidiPitchBendChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiPitchBendChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Bend(self: win32more.Windows.Devices.Midi.IMidiPitchBendChangeMessage) -> UInt16: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Bend = property(get_Bend, None)
    Channel = property(get_Channel, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiPolyphonicKeyPressureMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage
    _classid_ = 'Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage.CreateMidiPolyphonicKeyPressureMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiPolyphonicKeyPressureMessage(cls: win32more.Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessageFactory, channel: Byte, note: Byte, pressure: Byte) -> win32more.Windows.Devices.Midi.MidiPolyphonicKeyPressureMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Note(self: win32more.Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.Devices.Midi.IMidiPolyphonicKeyPressureMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Note = property(get_Note, None)
    Pressure = property(get_Pressure, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiProgramChangeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiProgramChangeMessage
    _classid_ = 'Windows.Devices.Midi.MidiProgramChangeMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiProgramChangeMessage.CreateMidiProgramChangeMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiProgramChangeMessage(cls: win32more.Windows.Devices.Midi.IMidiProgramChangeMessageFactory, channel: Byte, program: Byte) -> win32more.Windows.Devices.Midi.MidiProgramChangeMessage: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Midi.IMidiProgramChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Program(self: win32more.Windows.Devices.Midi.IMidiProgramChangeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Channel = property(get_Channel, None)
    Program = property(get_Program, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiSongPositionPointerMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiSongPositionPointerMessage
    _classid_ = 'Windows.Devices.Midi.MidiSongPositionPointerMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiSongPositionPointerMessage.CreateMidiSongPositionPointerMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiSongPositionPointerMessage(cls: win32more.Windows.Devices.Midi.IMidiSongPositionPointerMessageFactory, beats: UInt16) -> win32more.Windows.Devices.Midi.MidiSongPositionPointerMessage: ...
    @winrt_mixinmethod
    def get_Beats(self: win32more.Windows.Devices.Midi.IMidiSongPositionPointerMessage) -> UInt16: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    Beats = property(get_Beats, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiSongSelectMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiSongSelectMessage
    _classid_ = 'Windows.Devices.Midi.MidiSongSelectMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiSongSelectMessage.CreateMidiSongSelectMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiSongSelectMessage(cls: win32more.Windows.Devices.Midi.IMidiSongSelectMessageFactory, song: Byte) -> win32more.Windows.Devices.Midi.MidiSongSelectMessage: ...
    @winrt_mixinmethod
    def get_Song(self: win32more.Windows.Devices.Midi.IMidiSongSelectMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Song = property(get_Song, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiStartMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiStartMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiStartMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiStartMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiStopMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiStopMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiStopMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiStopMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiSynthesizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Midi.IMidiSynthesizer
    _classid_ = 'Windows.Devices.Midi.MidiSynthesizer'
    @winrt_mixinmethod
    def get_AudioDevice(self: win32more.Windows.Devices.Midi.IMidiSynthesizer) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Volume(self: win32more.Windows.Devices.Midi.IMidiSynthesizer) -> Double: ...
    @winrt_mixinmethod
    def put_Volume(self: win32more.Windows.Devices.Midi.IMidiSynthesizer, value: Double) -> Void: ...
    @winrt_mixinmethod
    def SendMessage(self: win32more.Windows.Devices.Midi.IMidiOutPort, midiMessage: win32more.Windows.Devices.Midi.IMidiMessage) -> Void: ...
    @winrt_mixinmethod
    def SendBuffer(self: win32more.Windows.Devices.Midi.IMidiOutPort, midiData: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Midi.IMidiOutPort) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Devices.Midi.IMidiSynthesizerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_classmethod
    def CreateFromAudioDeviceAsync(cls: win32more.Windows.Devices.Midi.IMidiSynthesizerStatics, audioDevice: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Midi.MidiSynthesizer]: ...
    @winrt_classmethod
    def IsSynthesizer(cls: win32more.Windows.Devices.Midi.IMidiSynthesizerStatics, midiDevice: win32more.Windows.Devices.Enumeration.DeviceInformation) -> Boolean: ...
    AudioDevice = property(get_AudioDevice, None)
    DeviceId = property(get_DeviceId, None)
    Volume = property(get_Volume, put_Volume)
class MidiSystemExclusiveMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiSystemExclusiveMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiSystemExclusiveMessage.CreateMidiSystemExclusiveMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiSystemExclusiveMessage(cls: win32more.Windows.Devices.Midi.IMidiSystemExclusiveMessageFactory, rawData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Midi.MidiSystemExclusiveMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiSystemResetMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiSystemResetMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiSystemResetMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiSystemResetMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiTimeCodeMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiTimeCodeMessage
    _classid_ = 'Windows.Devices.Midi.MidiTimeCodeMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiTimeCodeMessage.CreateMidiTimeCodeMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMidiTimeCodeMessage(cls: win32more.Windows.Devices.Midi.IMidiTimeCodeMessageFactory, frameType: Byte, values: Byte) -> win32more.Windows.Devices.Midi.MidiTimeCodeMessage: ...
    @winrt_mixinmethod
    def get_FrameType(self: win32more.Windows.Devices.Midi.IMidiTimeCodeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Values(self: win32more.Windows.Devices.Midi.IMidiTimeCodeMessage) -> Byte: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    FrameType = property(get_FrameType, None)
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
    Values = property(get_Values, None)
class MidiTimingClockMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiTimingClockMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiTimingClockMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiTimingClockMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)
class MidiTuneRequestMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Midi.IMidiMessage
    _classid_ = 'Windows.Devices.Midi.MidiTuneRequestMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Midi.MidiTuneRequestMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Midi.MidiTuneRequestMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RawData(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Devices.Midi.IMidiMessage) -> win32more.Windows.Devices.Midi.MidiMessageType: ...
    RawData = property(get_RawData, None)
    Timestamp = property(get_Timestamp, None)
    Type = property(get_Type, None)


make_ready(__name__)
