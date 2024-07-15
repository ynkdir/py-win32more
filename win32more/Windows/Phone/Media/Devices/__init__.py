from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Phone.Media.Devices
import win32more.Windows.Win32.System.WinRT
class AudioRoutingEndpoint(Enum, Int32):
    Default = 0
    Earpiece = 1
    Speakerphone = 2
    Bluetooth = 3
    WiredHeadset = 4
    WiredHeadsetSpeakerOnly = 5
    BluetoothWithNoiseAndEchoCancellation = 6
    BluetoothPreferred = 7
class AudioRoutingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager
    _classid_ = 'Windows.Phone.Media.Devices.AudioRoutingManager'
    @winrt_mixinmethod
    def GetAudioEndpoint(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager) -> win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_mixinmethod
    def SetAudioEndpoint(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, endpoint: win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_mixinmethod
    def add_AudioEndpointChanged(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, endpointChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Phone.Media.Devices.AudioRoutingManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioEndpointChanged(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AvailableAudioEndpoints(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager) -> win32more.Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Phone.Media.Devices.IAudioRoutingManagerStatics) -> win32more.Windows.Phone.Media.Devices.AudioRoutingManager: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
    AudioEndpointChanged = event()
class AvailableAudioRoutingEndpoints(Enum, UInt32):
    None_ = 0
    Earpiece = 1
    Speakerphone = 2
    Bluetooth = 4
class IAudioRoutingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManager'
    _iid_ = Guid('{79340d20-71cc-4526-9f29-fc8d2486418b}')
    @winrt_commethod(6)
    def GetAudioEndpoint(self) -> win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_commethod(7)
    def SetAudioEndpoint(self, endpoint: win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_commethod(8)
    def add_AudioEndpointChanged(self, endpointChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Phone.Media.Devices.AudioRoutingManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AudioEndpointChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_AvailableAudioEndpoints(self) -> win32more.Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
    AudioEndpointChanged = event()
class IAudioRoutingManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManagerStatics'
    _iid_ = Guid('{977fb2a4-5590-4a6f-adde-6a3d0ad58250}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Phone.Media.Devices.AudioRoutingManager: ...


make_ready(__name__)
