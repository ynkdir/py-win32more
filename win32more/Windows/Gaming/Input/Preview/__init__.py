from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.Input
import win32more.Windows.Gaming.Input.Custom
import win32more.Windows.Gaming.Input.Preview
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class DeviceCommand(Enum, Int32):
    Reset = 0
class GameControllerBatteryChargingState(Enum, Int32):
    Unknown = 0
    Inactive = 1
    Active = 2
    Error = 3
class GameControllerBatteryKind(Enum, Int32):
    Unknown = 0
    None_ = 1
    Standard = 2
    Rechargeable = 3
class GameControllerBatteryLevel(Enum, Int32):
    Unknown = 0
    Critical = 1
    Low = 2
    Medium = 3
    Full = 4
class GameControllerFirmwareCorruptReason(Enum, Int32):
    Unknown = 0
    NotCorrupt = 1
    TwoUpCorrupt = 2
    AppCorrupt = 3
    RadioCorrupt = 4
    EepromCorrupt = 5
    SafeToUpdate = 6
class GameControllerProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.GameControllerProviderInfo'
    @winrt_classmethod
    def GetParentProviderId(cls: win32more.Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_classmethod
    def GetProviderId(cls: win32more.Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
class HeadsetGeqGains(Structure):
    band1Gain: Int32
    band2Gain: Int32
    band3Gain: Int32
    band4Gain: Int32
    band5Gain: Int32
class HeadsetLevel(Enum, Int32):
    Off = 0
    Low = 1
    Medium = 2
    High = 3
class HeadsetOperation(Enum, Int32):
    Geq = 0
    BassBoostGain = 1
    SmartMute = 2
    SideTone = 3
    MuteLedBrightness = 4
    SwapMixAndVolumeDials = 5
class IGameControllerProviderInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.IGameControllerProviderInfoStatics'
    _iid_ = Guid('{0be1e6c5-d9bd-44ee-8362-488b2e464bfb}')
    @winrt_commethod(6)
    def GetParentProviderId(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetProviderId(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> WinRT_String: ...
class ILegacyGipGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider'
    _iid_ = Guid('{2da3ed52-ffd9-43e2-825c-1d2790e04d14}')
    @winrt_commethod(6)
    def get_BatteryChargingState(self) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryChargingState: ...
    @winrt_commethod(7)
    def get_BatteryKind(self) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryKind: ...
    @winrt_commethod(8)
    def get_BatteryLevel(self) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryLevel: ...
    @winrt_commethod(9)
    def GetDeviceFirmwareCorruptionState(self) -> win32more.Windows.Gaming.Input.Preview.GameControllerFirmwareCorruptReason: ...
    @winrt_commethod(10)
    def get_IsFirmwareCorrupted(self) -> Boolean: ...
    @winrt_commethod(11)
    def IsInterfaceSupported(self, interfaceId: Guid) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsSyntheticDevice(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_PreferredTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(14)
    def ExecuteCommand(self, command: win32more.Windows.Gaming.Input.Preview.DeviceCommand) -> Void: ...
    @winrt_commethod(15)
    def SetHomeLedIntensity(self, intensity: Byte) -> Void: ...
    @winrt_commethod(16)
    def GetExtendedDeviceInfo(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(17)
    def SetHeadsetOperation(self, operation: win32more.Windows.Gaming.Input.Preview.HeadsetOperation, buffer: PassArray[Byte]) -> Void: ...
    @winrt_commethod(18)
    def GetHeadsetOperation(self, operation: win32more.Windows.Gaming.Input.Preview.HeadsetOperation) -> ReceiveArray[Byte]: ...
    @winrt_commethod(19)
    def get_AppCompatVersion(self) -> UInt32: ...
    @winrt_commethod(20)
    def SetStandardControllerButtonRemapping(self, user: win32more.Windows.System.User, previous: Boolean, remapping: win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.Gaming.Input.Preview.RemappingButtonCategory, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_commethod(21)
    def GetStandardControllerButtonRemapping(self, user: win32more.Windows.System.User, previous: Boolean) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.Gaming.Input.Preview.RemappingButtonCategory, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    AppCompatVersion = property(get_AppCompatVersion, None)
    BatteryChargingState = property(get_BatteryChargingState, None)
    BatteryKind = property(get_BatteryKind, None)
    BatteryLevel = property(get_BatteryLevel, None)
    IsFirmwareCorrupted = property(get_IsFirmwareCorrupted, None)
    IsSyntheticDevice = property(get_IsSyntheticDevice, None)
    PreferredTypes = property(get_PreferredTypes, None)
class ILegacyGipGameControllerProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics'
    _iid_ = Guid('{d40dda17-b1f4-499a-874c-7095aac15291}')
    @winrt_commethod(6)
    def FromGameController(self, controller: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Preview.LegacyGipGameControllerProvider: ...
    @winrt_commethod(7)
    def FromGameControllerProvider(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.LegacyGipGameControllerProvider: ...
    @winrt_commethod(8)
    def PairPilotToCopilot(self, user: win32more.Windows.System.User, pilotControllerProviderId: WinRT_String, copilotControllerProviderId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def ClearPairing(self, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def IsPilot(self, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(11)
    def IsCopilot(self, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> WinRT_String: ...
class LegacyGipGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider
    _classid_ = 'Windows.Gaming.Input.Preview.LegacyGipGameControllerProvider'
    @winrt_mixinmethod
    def get_BatteryChargingState(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryChargingState: ...
    @winrt_mixinmethod
    def get_BatteryKind(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryKind: ...
    @winrt_mixinmethod
    def get_BatteryLevel(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.GameControllerBatteryLevel: ...
    @winrt_mixinmethod
    def GetDeviceFirmwareCorruptionState(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.GameControllerFirmwareCorruptReason: ...
    @winrt_mixinmethod
    def get_IsFirmwareCorrupted(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> Boolean: ...
    @winrt_mixinmethod
    def IsInterfaceSupported(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, interfaceId: Guid) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSyntheticDevice(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_PreferredTypes(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def ExecuteCommand(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, command: win32more.Windows.Gaming.Input.Preview.DeviceCommand) -> Void: ...
    @winrt_mixinmethod
    def SetHomeLedIntensity(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, intensity: Byte) -> Void: ...
    @winrt_mixinmethod
    def GetExtendedDeviceInfo(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def SetHeadsetOperation(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, operation: win32more.Windows.Gaming.Input.Preview.HeadsetOperation, buffer: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def GetHeadsetOperation(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, operation: win32more.Windows.Gaming.Input.Preview.HeadsetOperation) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_AppCompatVersion(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider) -> UInt32: ...
    @winrt_mixinmethod
    def SetStandardControllerButtonRemapping(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, user: win32more.Windows.System.User, previous: Boolean, remapping: win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.Gaming.Input.Preview.RemappingButtonCategory, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def GetStandardControllerButtonRemapping(self: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProvider, user: win32more.Windows.System.User, previous: Boolean) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.Gaming.Input.Preview.RemappingButtonCategory, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, controller: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Preview.LegacyGipGameControllerProvider: ...
    @winrt_classmethod
    def FromGameControllerProvider(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Preview.LegacyGipGameControllerProvider: ...
    @winrt_classmethod
    def PairPilotToCopilot(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, user: win32more.Windows.System.User, pilotControllerProviderId: WinRT_String, copilotControllerProviderId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def ClearPairing(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsPilot(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def IsCopilot(cls: win32more.Windows.Gaming.Input.Preview.ILegacyGipGameControllerProviderStatics, user: win32more.Windows.System.User, controllerProviderId: WinRT_String) -> WinRT_String: ...
    AppCompatVersion = property(get_AppCompatVersion, None)
    BatteryChargingState = property(get_BatteryChargingState, None)
    BatteryKind = property(get_BatteryKind, None)
    BatteryLevel = property(get_BatteryLevel, None)
    IsFirmwareCorrupted = property(get_IsFirmwareCorrupted, None)
    IsSyntheticDevice = property(get_IsSyntheticDevice, None)
    PreferredTypes = property(get_PreferredTypes, None)
class RemappingButtonCategory(Enum, Int32):
    ButtonSettings = 0
    AnalogSettings = 1
    VibrationSettings = 2
    ShareShortPress = 3
    ShareShortPressMetaData = 4
    ShareShortPressMetaDataDisplay = 5
    ShareLongPress = 6
    ShareLongPressMetaData = 7
    ShareLongPressMetaDataDisplay = 8
    ShareDoublePress = 9
    ShareDoublePressMetaData = 10
    ShareDoublePressMetaDataDisplay = 11


make_ready(__name__)
