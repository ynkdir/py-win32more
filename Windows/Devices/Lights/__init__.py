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
import Windows.Devices.Lights
import Windows.Foundation
import Windows.Foundation.Numerics
import Windows.Storage.Streams
import Windows.System
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
class ILamp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('047d5b9a-ea45-4b2b-b1-a2-14-df-f0-0b-de-7b')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_BrightnessLevel(self) -> Single: ...
    @winrt_commethod(10)
    def put_BrightnessLevel(self, value: Single) -> Void: ...
    @winrt_commethod(11)
    def get_IsColorSettable(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def add_AvailabilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Lamp, Windows.Devices.Lights.LampAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_AvailabilityChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsColorSettable = property(get_IsColorSettable, None)
    Color = property(get_Color, put_Color)
class ILampArray(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7ace9787-c8a0-4e95-a1-e0-d5-86-76-53-86-49')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_HardwareVersion(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_LampArrayKind(self) -> Windows.Devices.Lights.LampArrayKind: ...
    @winrt_commethod(11)
    def get_LampCount(self) -> Int32: ...
    @winrt_commethod(12)
    def get_MinUpdateInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_BoundingBox(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(14)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_BrightnessLevel(self) -> Double: ...
    @winrt_commethod(17)
    def put_BrightnessLevel(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_IsConnected(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_SupportsVirtualKeys(self) -> Boolean: ...
    @winrt_commethod(20)
    def GetLampInfo(self, lampIndex: Int32) -> Windows.Devices.Lights.LampInfo: ...
    @winrt_commethod(21)
    def GetIndicesForKey(self, key: Windows.System.VirtualKey) -> POINTER(Int32): ...
    @winrt_commethod(22)
    def GetIndicesForPurposes(self, purposes: Windows.Devices.Lights.LampPurposes) -> POINTER(Int32): ...
    @winrt_commethod(23)
    def SetColor(self, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_commethod(24)
    def SetColorForIndex(self, lampIndex: Int32, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_commethod(25)
    def SetSingleColorForIndices(self, desiredColor: Windows.UI.Color, lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_commethod(26)
    def SetColorsForIndices(self, desiredColors: POINTER(Windows.UI.Color_head), lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_commethod(27)
    def SetColorsForKey(self, desiredColor: Windows.UI.Color, key: Windows.System.VirtualKey) -> Void: ...
    @winrt_commethod(28)
    def SetColorsForKeys(self, desiredColors: POINTER(Windows.UI.Color_head), keys: POINTER(Windows.System.VirtualKey)) -> Void: ...
    @winrt_commethod(29)
    def SetColorsForPurposes(self, desiredColor: Windows.UI.Color, purposes: Windows.Devices.Lights.LampPurposes) -> Void: ...
    @winrt_commethod(30)
    def SendMessageAsync(self, messageId: Int32, message: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(31)
    def RequestMessageAsync(self, messageId: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    DeviceId = property(get_DeviceId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    LampArrayKind = property(get_LampArrayKind, None)
    LampCount = property(get_LampCount, None)
    MinUpdateInterval = property(get_MinUpdateInterval, None)
    BoundingBox = property(get_BoundingBox, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsConnected = property(get_IsConnected, None)
    SupportsVirtualKeys = property(get_SupportsVirtualKeys, None)
class ILampArrayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7bb8c98d-5fc1-452d-bb-1f-4a-d4-10-d3-98-ff')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.LampArray]: ...
class ILampAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4f6e3ded-07a2-499d-92-60-67-e3-04-53-2b-a4')
    @winrt_commethod(6)
    def get_IsAvailable(self) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class ILampInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('30bb521c-0acf-49da-8c-10-15-0b-9c-f6-27-13')
    @winrt_commethod(6)
    def get_Index(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Purposes(self) -> Windows.Devices.Lights.LampPurposes: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_RedLevelCount(self) -> Int32: ...
    @winrt_commethod(10)
    def get_GreenLevelCount(self) -> Int32: ...
    @winrt_commethod(11)
    def get_BlueLevelCount(self) -> Int32: ...
    @winrt_commethod(12)
    def get_GainLevelCount(self) -> Int32: ...
    @winrt_commethod(13)
    def get_FixedColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(14)
    def GetNearestSupportedColor(self, desiredColor: Windows.UI.Color) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def get_UpdateLatency(self) -> Windows.Foundation.TimeSpan: ...
    Index = property(get_Index, None)
    Purposes = property(get_Purposes, None)
    Position = property(get_Position, None)
    RedLevelCount = property(get_RedLevelCount, None)
    GreenLevelCount = property(get_GreenLevelCount, None)
    BlueLevelCount = property(get_BlueLevelCount, None)
    GainLevelCount = property(get_GainLevelCount, None)
    FixedColor = property(get_FixedColor, None)
    UpdateLatency = property(get_UpdateLatency, None)
class ILampStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a822416c-8885-401e-b8-21-8e-8b-38-a8-e8-ec')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.Lamp]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.Lamp]: ...
class Lamp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Lamp'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Lights.ILamp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.Lights.ILamp) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Devices.Lights.ILamp, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: Windows.Devices.Lights.ILamp) -> Single: ...
    @winrt_mixinmethod
    def put_BrightnessLevel(self: Windows.Devices.Lights.ILamp, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_IsColorSettable(self: Windows.Devices.Lights.ILamp) -> Boolean: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.Devices.Lights.ILamp) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.Devices.Lights.ILamp, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: Windows.Devices.Lights.ILamp, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Lights.Lamp, Windows.Devices.Lights.LampAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: Windows.Devices.Lights.ILamp, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Lights.ILampStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Lights.ILampStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.Lamp]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Lights.ILampStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.Lamp]: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsColorSettable = property(get_IsColorSettable, None)
    Color = property(get_Color, put_Color)
class LampArray(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.LampArray'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Lights.ILampArray) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersion(self: Windows.Devices.Lights.ILampArray) -> UInt16: ...
    @winrt_mixinmethod
    def get_LampArrayKind(self: Windows.Devices.Lights.ILampArray) -> Windows.Devices.Lights.LampArrayKind: ...
    @winrt_mixinmethod
    def get_LampCount(self: Windows.Devices.Lights.ILampArray) -> Int32: ...
    @winrt_mixinmethod
    def get_MinUpdateInterval(self: Windows.Devices.Lights.ILampArray) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: Windows.Devices.Lights.ILampArray) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Devices.Lights.ILampArray, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: Windows.Devices.Lights.ILampArray) -> Double: ...
    @winrt_mixinmethod
    def put_BrightnessLevel(self: Windows.Devices.Lights.ILampArray, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsVirtualKeys(self: Windows.Devices.Lights.ILampArray) -> Boolean: ...
    @winrt_mixinmethod
    def GetLampInfo(self: Windows.Devices.Lights.ILampArray, lampIndex: Int32) -> Windows.Devices.Lights.LampInfo: ...
    @winrt_mixinmethod
    def GetIndicesForKey(self: Windows.Devices.Lights.ILampArray, key: Windows.System.VirtualKey) -> POINTER(Int32): ...
    @winrt_mixinmethod
    def GetIndicesForPurposes(self: Windows.Devices.Lights.ILampArray, purposes: Windows.Devices.Lights.LampPurposes) -> POINTER(Int32): ...
    @winrt_mixinmethod
    def SetColor(self: Windows.Devices.Lights.ILampArray, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetColorForIndex(self: Windows.Devices.Lights.ILampArray, lampIndex: Int32, desiredColor: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetSingleColorForIndices(self: Windows.Devices.Lights.ILampArray, desiredColor: Windows.UI.Color, lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForIndices(self: Windows.Devices.Lights.ILampArray, desiredColors: POINTER(Windows.UI.Color_head), lampIndexes: POINTER(Int32)) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForKey(self: Windows.Devices.Lights.ILampArray, desiredColor: Windows.UI.Color, key: Windows.System.VirtualKey) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForKeys(self: Windows.Devices.Lights.ILampArray, desiredColors: POINTER(Windows.UI.Color_head), keys: POINTER(Windows.System.VirtualKey)) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForPurposes(self: Windows.Devices.Lights.ILampArray, desiredColor: Windows.UI.Color, purposes: Windows.Devices.Lights.LampPurposes) -> Void: ...
    @winrt_mixinmethod
    def SendMessageAsync(self: Windows.Devices.Lights.ILampArray, messageId: Int32, message: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestMessageAsync(self: Windows.Devices.Lights.ILampArray, messageId: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Lights.ILampArrayStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Lights.ILampArrayStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Lights.LampArray]: ...
    DeviceId = property(get_DeviceId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVersion = property(get_HardwareVersion, None)
    LampArrayKind = property(get_LampArrayKind, None)
    LampCount = property(get_LampCount, None)
    MinUpdateInterval = property(get_MinUpdateInterval, None)
    BoundingBox = property(get_BoundingBox, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    BrightnessLevel = property(get_BrightnessLevel, put_BrightnessLevel)
    IsConnected = property(get_IsConnected, None)
    SupportsVirtualKeys = property(get_SupportsVirtualKeys, None)
LampArrayKind = Int32
LampArrayKind_Undefined: LampArrayKind = 0
LampArrayKind_Keyboard: LampArrayKind = 1
LampArrayKind_Mouse: LampArrayKind = 2
LampArrayKind_GameController: LampArrayKind = 3
LampArrayKind_Peripheral: LampArrayKind = 4
LampArrayKind_Scene: LampArrayKind = 5
LampArrayKind_Notification: LampArrayKind = 6
LampArrayKind_Chassis: LampArrayKind = 7
LampArrayKind_Wearable: LampArrayKind = 8
LampArrayKind_Furniture: LampArrayKind = 9
LampArrayKind_Art: LampArrayKind = 10
class LampAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.LampAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def get_IsAvailable(self: Windows.Devices.Lights.ILampAvailabilityChangedEventArgs) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class LampInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.LampInfo'
    @winrt_mixinmethod
    def get_Index(self: Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_Purposes(self: Windows.Devices.Lights.ILampInfo) -> Windows.Devices.Lights.LampPurposes: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.Lights.ILampInfo) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RedLevelCount(self: Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_GreenLevelCount(self: Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_BlueLevelCount(self: Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_GainLevelCount(self: Windows.Devices.Lights.ILampInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_FixedColor(self: Windows.Devices.Lights.ILampInfo) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def GetNearestSupportedColor(self: Windows.Devices.Lights.ILampInfo, desiredColor: Windows.UI.Color) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_UpdateLatency(self: Windows.Devices.Lights.ILampInfo) -> Windows.Foundation.TimeSpan: ...
    Index = property(get_Index, None)
    Purposes = property(get_Purposes, None)
    Position = property(get_Position, None)
    RedLevelCount = property(get_RedLevelCount, None)
    GreenLevelCount = property(get_GreenLevelCount, None)
    BlueLevelCount = property(get_BlueLevelCount, None)
    GainLevelCount = property(get_GainLevelCount, None)
    FixedColor = property(get_FixedColor, None)
    UpdateLatency = property(get_UpdateLatency, None)
LampPurposes = UInt32
LampPurposes_Undefined: LampPurposes = 0
LampPurposes_Control: LampPurposes = 1
LampPurposes_Accent: LampPurposes = 2
LampPurposes_Branding: LampPurposes = 4
LampPurposes_Status: LampPurposes = 8
LampPurposes_Illumination: LampPurposes = 16
LampPurposes_Presentation: LampPurposes = 32
make_head(_module, 'ILamp')
make_head(_module, 'ILampArray')
make_head(_module, 'ILampArrayStatics')
make_head(_module, 'ILampAvailabilityChangedEventArgs')
make_head(_module, 'ILampInfo')
make_head(_module, 'ILampStatics')
make_head(_module, 'Lamp')
make_head(_module, 'LampArray')
make_head(_module, 'LampAvailabilityChangedEventArgs')
make_head(_module, 'LampInfo')
