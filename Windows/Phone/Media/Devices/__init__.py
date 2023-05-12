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
import Windows.Foundation
import Windows.Phone.Media.Devices
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AudioRoutingEndpoint = Int32
AudioRoutingEndpoint_Default: AudioRoutingEndpoint = 0
AudioRoutingEndpoint_Earpiece: AudioRoutingEndpoint = 1
AudioRoutingEndpoint_Speakerphone: AudioRoutingEndpoint = 2
AudioRoutingEndpoint_Bluetooth: AudioRoutingEndpoint = 3
AudioRoutingEndpoint_WiredHeadset: AudioRoutingEndpoint = 4
AudioRoutingEndpoint_WiredHeadsetSpeakerOnly: AudioRoutingEndpoint = 5
AudioRoutingEndpoint_BluetoothWithNoiseAndEchoCancellation: AudioRoutingEndpoint = 6
AudioRoutingEndpoint_BluetoothPreferred: AudioRoutingEndpoint = 7
class AudioRoutingManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.Media.Devices.IAudioRoutingManager
    _classid_ = 'Windows.Phone.Media.Devices.AudioRoutingManager'
    @winrt_mixinmethod
    def GetAudioEndpoint(self: Windows.Phone.Media.Devices.IAudioRoutingManager) -> Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_mixinmethod
    def SetAudioEndpoint(self: Windows.Phone.Media.Devices.IAudioRoutingManager, endpoint: Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_mixinmethod
    def add_AudioEndpointChanged(self: Windows.Phone.Media.Devices.IAudioRoutingManager, endpointChangeHandler: Windows.Foundation.TypedEventHandler[Windows.Phone.Media.Devices.AudioRoutingManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioEndpointChanged(self: Windows.Phone.Media.Devices.IAudioRoutingManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AvailableAudioEndpoints(self: Windows.Phone.Media.Devices.IAudioRoutingManager) -> Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Phone.Media.Devices.IAudioRoutingManagerStatics) -> Windows.Phone.Media.Devices.AudioRoutingManager: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
AvailableAudioRoutingEndpoints = UInt32
AvailableAudioRoutingEndpoints_None: AvailableAudioRoutingEndpoints = 0
AvailableAudioRoutingEndpoints_Earpiece: AvailableAudioRoutingEndpoints = 1
AvailableAudioRoutingEndpoints_Speakerphone: AvailableAudioRoutingEndpoints = 2
AvailableAudioRoutingEndpoints_Bluetooth: AvailableAudioRoutingEndpoints = 4
class IAudioRoutingManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManager'
    _iid_ = Guid('{79340d20-71cc-4526-9f29-fc8d2486418b}')
    @winrt_commethod(6)
    def GetAudioEndpoint(self) -> Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_commethod(7)
    def SetAudioEndpoint(self, endpoint: Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_commethod(8)
    def add_AudioEndpointChanged(self, endpointChangeHandler: Windows.Foundation.TypedEventHandler[Windows.Phone.Media.Devices.AudioRoutingManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AudioEndpointChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_AvailableAudioEndpoints(self) -> Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
class IAudioRoutingManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManagerStatics'
    _iid_ = Guid('{977fb2a4-5590-4a6f-adde-6a3d0ad58250}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Phone.Media.Devices.AudioRoutingManager: ...
make_head(_module, 'AudioRoutingManager')
make_head(_module, 'IAudioRoutingManager')
make_head(_module, 'IAudioRoutingManagerStatics')
