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
import Windows.Devices.Haptics
import Windows.Devices.Power
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Gaming.Input
import Windows.Gaming.Input.ForceFeedback
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ArcadeStick(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.ArcadeStick'
    @winrt_mixinmethod
    def GetButtonLabel(self: Windows.Gaming.Input.IArcadeStick, button: Windows.Gaming.Input.ArcadeStickButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IArcadeStick) -> Windows.Gaming.Input.ArcadeStickReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IArcadeStickStatics2, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.ArcadeStick: ...
    @winrt_classmethod
    def add_ArcadeStickAdded(cls: Windows.Gaming.Input.IArcadeStickStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.ArcadeStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ArcadeStickAdded(cls: Windows.Gaming.Input.IArcadeStickStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ArcadeStickRemoved(cls: Windows.Gaming.Input.IArcadeStickStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.ArcadeStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ArcadeStickRemoved(cls: Windows.Gaming.Input.IArcadeStickStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ArcadeSticks(cls: Windows.Gaming.Input.IArcadeStickStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.ArcadeStick]: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    ArcadeSticks = property(get_ArcadeSticks, None)
ArcadeStickButtons = UInt32
ArcadeStickButtons_None: ArcadeStickButtons = 0
ArcadeStickButtons_StickUp: ArcadeStickButtons = 1
ArcadeStickButtons_StickDown: ArcadeStickButtons = 2
ArcadeStickButtons_StickLeft: ArcadeStickButtons = 4
ArcadeStickButtons_StickRight: ArcadeStickButtons = 8
ArcadeStickButtons_Action1: ArcadeStickButtons = 16
ArcadeStickButtons_Action2: ArcadeStickButtons = 32
ArcadeStickButtons_Action3: ArcadeStickButtons = 64
ArcadeStickButtons_Action4: ArcadeStickButtons = 128
ArcadeStickButtons_Action5: ArcadeStickButtons = 256
ArcadeStickButtons_Action6: ArcadeStickButtons = 512
ArcadeStickButtons_Special1: ArcadeStickButtons = 1024
ArcadeStickButtons_Special2: ArcadeStickButtons = 2048
class ArcadeStickReading(EasyCastStructure):
    Timestamp: UInt64
    Buttons: Windows.Gaming.Input.ArcadeStickButtons
class FlightStick(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.FlightStick'
    @winrt_mixinmethod
    def get_HatSwitchKind(self: Windows.Gaming.Input.IFlightStick) -> Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: Windows.Gaming.Input.IFlightStick, button: Windows.Gaming.Input.FlightStickButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IFlightStick) -> Windows.Gaming.Input.FlightStickReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def add_FlightStickAdded(cls: Windows.Gaming.Input.IFlightStickStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.FlightStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_FlightStickAdded(cls: Windows.Gaming.Input.IFlightStickStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_FlightStickRemoved(cls: Windows.Gaming.Input.IFlightStickStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.FlightStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_FlightStickRemoved(cls: Windows.Gaming.Input.IFlightStickStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_FlightSticks(cls: Windows.Gaming.Input.IFlightStickStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.FlightStick]: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IFlightStickStatics, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.FlightStick: ...
    HatSwitchKind = property(get_HatSwitchKind, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    FlightSticks = property(get_FlightSticks, None)
FlightStickButtons = UInt32
FlightStickButtons_None: FlightStickButtons = 0
FlightStickButtons_FirePrimary: FlightStickButtons = 1
FlightStickButtons_FireSecondary: FlightStickButtons = 2
class FlightStickReading(EasyCastStructure):
    Timestamp: UInt64
    Buttons: Windows.Gaming.Input.FlightStickButtons
    HatSwitch: Windows.Gaming.Input.GameControllerSwitchPosition
    Roll: Double
    Pitch: Double
    Yaw: Double
    Throttle: Double
GameControllerButtonLabel = Int32
GameControllerButtonLabel_None: GameControllerButtonLabel = 0
GameControllerButtonLabel_XboxBack: GameControllerButtonLabel = 1
GameControllerButtonLabel_XboxStart: GameControllerButtonLabel = 2
GameControllerButtonLabel_XboxMenu: GameControllerButtonLabel = 3
GameControllerButtonLabel_XboxView: GameControllerButtonLabel = 4
GameControllerButtonLabel_XboxUp: GameControllerButtonLabel = 5
GameControllerButtonLabel_XboxDown: GameControllerButtonLabel = 6
GameControllerButtonLabel_XboxLeft: GameControllerButtonLabel = 7
GameControllerButtonLabel_XboxRight: GameControllerButtonLabel = 8
GameControllerButtonLabel_XboxA: GameControllerButtonLabel = 9
GameControllerButtonLabel_XboxB: GameControllerButtonLabel = 10
GameControllerButtonLabel_XboxX: GameControllerButtonLabel = 11
GameControllerButtonLabel_XboxY: GameControllerButtonLabel = 12
GameControllerButtonLabel_XboxLeftBumper: GameControllerButtonLabel = 13
GameControllerButtonLabel_XboxLeftTrigger: GameControllerButtonLabel = 14
GameControllerButtonLabel_XboxLeftStickButton: GameControllerButtonLabel = 15
GameControllerButtonLabel_XboxRightBumper: GameControllerButtonLabel = 16
GameControllerButtonLabel_XboxRightTrigger: GameControllerButtonLabel = 17
GameControllerButtonLabel_XboxRightStickButton: GameControllerButtonLabel = 18
GameControllerButtonLabel_XboxPaddle1: GameControllerButtonLabel = 19
GameControllerButtonLabel_XboxPaddle2: GameControllerButtonLabel = 20
GameControllerButtonLabel_XboxPaddle3: GameControllerButtonLabel = 21
GameControllerButtonLabel_XboxPaddle4: GameControllerButtonLabel = 22
GameControllerButtonLabel_Mode: GameControllerButtonLabel = 23
GameControllerButtonLabel_Select: GameControllerButtonLabel = 24
GameControllerButtonLabel_Menu: GameControllerButtonLabel = 25
GameControllerButtonLabel_View: GameControllerButtonLabel = 26
GameControllerButtonLabel_Back: GameControllerButtonLabel = 27
GameControllerButtonLabel_Start: GameControllerButtonLabel = 28
GameControllerButtonLabel_Options: GameControllerButtonLabel = 29
GameControllerButtonLabel_Share: GameControllerButtonLabel = 30
GameControllerButtonLabel_Up: GameControllerButtonLabel = 31
GameControllerButtonLabel_Down: GameControllerButtonLabel = 32
GameControllerButtonLabel_Left: GameControllerButtonLabel = 33
GameControllerButtonLabel_Right: GameControllerButtonLabel = 34
GameControllerButtonLabel_LetterA: GameControllerButtonLabel = 35
GameControllerButtonLabel_LetterB: GameControllerButtonLabel = 36
GameControllerButtonLabel_LetterC: GameControllerButtonLabel = 37
GameControllerButtonLabel_LetterL: GameControllerButtonLabel = 38
GameControllerButtonLabel_LetterR: GameControllerButtonLabel = 39
GameControllerButtonLabel_LetterX: GameControllerButtonLabel = 40
GameControllerButtonLabel_LetterY: GameControllerButtonLabel = 41
GameControllerButtonLabel_LetterZ: GameControllerButtonLabel = 42
GameControllerButtonLabel_Cross: GameControllerButtonLabel = 43
GameControllerButtonLabel_Circle: GameControllerButtonLabel = 44
GameControllerButtonLabel_Square: GameControllerButtonLabel = 45
GameControllerButtonLabel_Triangle: GameControllerButtonLabel = 46
GameControllerButtonLabel_LeftBumper: GameControllerButtonLabel = 47
GameControllerButtonLabel_LeftTrigger: GameControllerButtonLabel = 48
GameControllerButtonLabel_LeftStickButton: GameControllerButtonLabel = 49
GameControllerButtonLabel_Left1: GameControllerButtonLabel = 50
GameControllerButtonLabel_Left2: GameControllerButtonLabel = 51
GameControllerButtonLabel_Left3: GameControllerButtonLabel = 52
GameControllerButtonLabel_RightBumper: GameControllerButtonLabel = 53
GameControllerButtonLabel_RightTrigger: GameControllerButtonLabel = 54
GameControllerButtonLabel_RightStickButton: GameControllerButtonLabel = 55
GameControllerButtonLabel_Right1: GameControllerButtonLabel = 56
GameControllerButtonLabel_Right2: GameControllerButtonLabel = 57
GameControllerButtonLabel_Right3: GameControllerButtonLabel = 58
GameControllerButtonLabel_Paddle1: GameControllerButtonLabel = 59
GameControllerButtonLabel_Paddle2: GameControllerButtonLabel = 60
GameControllerButtonLabel_Paddle3: GameControllerButtonLabel = 61
GameControllerButtonLabel_Paddle4: GameControllerButtonLabel = 62
GameControllerButtonLabel_Plus: GameControllerButtonLabel = 63
GameControllerButtonLabel_Minus: GameControllerButtonLabel = 64
GameControllerButtonLabel_DownLeftArrow: GameControllerButtonLabel = 65
GameControllerButtonLabel_DialLeft: GameControllerButtonLabel = 66
GameControllerButtonLabel_DialRight: GameControllerButtonLabel = 67
GameControllerButtonLabel_Suspension: GameControllerButtonLabel = 68
GameControllerSwitchKind = Int32
GameControllerSwitchKind_TwoWay: GameControllerSwitchKind = 0
GameControllerSwitchKind_FourWay: GameControllerSwitchKind = 1
GameControllerSwitchKind_EightWay: GameControllerSwitchKind = 2
GameControllerSwitchPosition = Int32
GameControllerSwitchPosition_Center: GameControllerSwitchPosition = 0
GameControllerSwitchPosition_Up: GameControllerSwitchPosition = 1
GameControllerSwitchPosition_UpRight: GameControllerSwitchPosition = 2
GameControllerSwitchPosition_Right: GameControllerSwitchPosition = 3
GameControllerSwitchPosition_DownRight: GameControllerSwitchPosition = 4
GameControllerSwitchPosition_Down: GameControllerSwitchPosition = 5
GameControllerSwitchPosition_DownLeft: GameControllerSwitchPosition = 6
GameControllerSwitchPosition_Left: GameControllerSwitchPosition = 7
GameControllerSwitchPosition_UpLeft: GameControllerSwitchPosition = 8
class Gamepad(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Gamepad'
    @winrt_mixinmethod
    def get_Vibration(self: Windows.Gaming.Input.IGamepad) -> Windows.Gaming.Input.GamepadVibration: ...
    @winrt_mixinmethod
    def put_Vibration(self: Windows.Gaming.Input.IGamepad, value: Windows.Gaming.Input.GamepadVibration) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IGamepad) -> Windows.Gaming.Input.GamepadReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: Windows.Gaming.Input.IGamepad2, button: Windows.Gaming.Input.GamepadButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IGamepadStatics2, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Gamepad: ...
    @winrt_classmethod
    def add_GamepadAdded(cls: Windows.Gaming.Input.IGamepadStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.Gamepad]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GamepadAdded(cls: Windows.Gaming.Input.IGamepadStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GamepadRemoved(cls: Windows.Gaming.Input.IGamepadStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.Gamepad]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GamepadRemoved(cls: Windows.Gaming.Input.IGamepadStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Gamepads(cls: Windows.Gaming.Input.IGamepadStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.Gamepad]: ...
    Vibration = property(get_Vibration, put_Vibration)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    Gamepads = property(get_Gamepads, None)
GamepadButtons = UInt32
GamepadButtons_None: GamepadButtons = 0
GamepadButtons_Menu: GamepadButtons = 1
GamepadButtons_View: GamepadButtons = 2
GamepadButtons_A: GamepadButtons = 4
GamepadButtons_B: GamepadButtons = 8
GamepadButtons_X: GamepadButtons = 16
GamepadButtons_Y: GamepadButtons = 32
GamepadButtons_DPadUp: GamepadButtons = 64
GamepadButtons_DPadDown: GamepadButtons = 128
GamepadButtons_DPadLeft: GamepadButtons = 256
GamepadButtons_DPadRight: GamepadButtons = 512
GamepadButtons_LeftShoulder: GamepadButtons = 1024
GamepadButtons_RightShoulder: GamepadButtons = 2048
GamepadButtons_LeftThumbstick: GamepadButtons = 4096
GamepadButtons_RightThumbstick: GamepadButtons = 8192
GamepadButtons_Paddle1: GamepadButtons = 16384
GamepadButtons_Paddle2: GamepadButtons = 32768
GamepadButtons_Paddle3: GamepadButtons = 65536
GamepadButtons_Paddle4: GamepadButtons = 131072
class GamepadReading(EasyCastStructure):
    Timestamp: UInt64
    Buttons: Windows.Gaming.Input.GamepadButtons
    LeftTrigger: Double
    RightTrigger: Double
    LeftThumbstickX: Double
    LeftThumbstickY: Double
    RightThumbstickX: Double
    RightThumbstickY: Double
class GamepadVibration(EasyCastStructure):
    LeftMotor: Double
    RightMotor: Double
    LeftTrigger: Double
    RightTrigger: Double
class Headset(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Headset'
    @winrt_mixinmethod
    def get_CaptureDeviceId(self: Windows.Gaming.Input.IHeadset) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RenderDeviceId(self: Windows.Gaming.Input.IHeadset) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    CaptureDeviceId = property(get_CaptureDeviceId, None)
    RenderDeviceId = property(get_RenderDeviceId, None)
class IArcadeStick(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b14a539d-befb-4c81-80-51-15-ec-f3-b1-30-36')
    @winrt_commethod(6)
    def GetButtonLabel(self, button: Windows.Gaming.Input.ArcadeStickButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(7)
    def GetCurrentReading(self) -> Windows.Gaming.Input.ArcadeStickReading: ...
class IArcadeStickStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c37b8c8-37b1-4ad8-94-58-20-0f-1a-30-01-8e')
    @winrt_commethod(6)
    def add_ArcadeStickAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.ArcadeStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ArcadeStickAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ArcadeStickRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.ArcadeStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ArcadeStickRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_ArcadeSticks(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.ArcadeStick]: ...
    ArcadeSticks = property(get_ArcadeSticks, None)
class IArcadeStickStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52b5d744-bb86-445a-b5-9c-59-6f-0e-2a-49-df')
    @winrt_commethod(6)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.ArcadeStick: ...
class IFlightStick(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b4a2c01c-b83b-4459-a1-a9-97-b0-3c-33-da-7c')
    @winrt_commethod(6)
    def get_HatSwitchKind(self) -> Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_commethod(7)
    def GetButtonLabel(self, button: Windows.Gaming.Input.FlightStickButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(8)
    def GetCurrentReading(self) -> Windows.Gaming.Input.FlightStickReading: ...
    HatSwitchKind = property(get_HatSwitchKind, None)
class IFlightStickStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5514924a-fecc-435e-83-dc-5c-ec-8a-18-a5-20')
    @winrt_commethod(6)
    def add_FlightStickAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.FlightStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FlightStickAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_FlightStickRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.FlightStick]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_FlightStickRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_FlightSticks(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.FlightStick]: ...
    @winrt_commethod(11)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.FlightStick: ...
    FlightSticks = property(get_FlightSticks, None)
class IGameController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1baf6522-5f64-42c5-82-67-b9-fe-22-15-bf-bd')
    @winrt_commethod(6)
    def add_HeadsetConnected(self, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_HeadsetConnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_HeadsetDisconnected(self, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HeadsetDisconnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_UserChanged(self, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UserChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Headset(self) -> Windows.Gaming.Input.Headset: ...
    @winrt_commethod(13)
    def get_IsWireless(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_User(self) -> Windows.System.User: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
class IGameControllerBatteryInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dcecc681-3963-4da6-95-5d-55-3f-3b-6f-61-61')
    @winrt_commethod(6)
    def TryGetBatteryReport(self) -> Windows.Devices.Power.BatteryReport: ...
class IGamepad(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bc7bb43c-0a69-3903-9e-9d-a5-0f-86-a4-5d-e5')
    @winrt_commethod(6)
    def get_Vibration(self) -> Windows.Gaming.Input.GamepadVibration: ...
    @winrt_commethod(7)
    def put_Vibration(self, value: Windows.Gaming.Input.GamepadVibration) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentReading(self) -> Windows.Gaming.Input.GamepadReading: ...
    Vibration = property(get_Vibration, put_Vibration)
class IGamepad2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c1689bd-5915-4245-b0-c0-c8-9f-ae-03-08-ff')
    @winrt_commethod(6)
    def GetButtonLabel(self, button: Windows.Gaming.Input.GamepadButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
class IGamepadStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8bbce529-d49c-39e9-95-60-e4-7d-de-96-b7-c8')
    @winrt_commethod(6)
    def add_GamepadAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.Gamepad]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GamepadAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_GamepadRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.Gamepad]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GamepadRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Gamepads(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.Gamepad]: ...
    Gamepads = property(get_Gamepads, None)
class IGamepadStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('42676dc5-0856-47c4-92-13-b3-95-50-4c-3a-3c')
    @winrt_commethod(6)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Gamepad: ...
class IHeadset(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3fd156ef-6925-3fa8-91-81-02-9c-52-23-ae-3b')
    @winrt_commethod(6)
    def get_CaptureDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RenderDeviceId(self) -> WinRT_String: ...
    CaptureDeviceId = property(get_CaptureDeviceId, None)
    RenderDeviceId = property(get_RenderDeviceId, None)
class IRacingWheel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f546656f-e106-4c82-a9-0f-55-40-12-90-4b-85')
    @winrt_commethod(6)
    def get_HasClutch(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasHandbrake(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HasPatternShifter(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_MaxPatternShifterGear(self) -> Int32: ...
    @winrt_commethod(10)
    def get_MaxWheelAngle(self) -> Double: ...
    @winrt_commethod(11)
    def get_WheelMotor(self) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor: ...
    @winrt_commethod(12)
    def GetButtonLabel(self, button: Windows.Gaming.Input.RacingWheelButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(13)
    def GetCurrentReading(self) -> Windows.Gaming.Input.RacingWheelReading: ...
    HasClutch = property(get_HasClutch, None)
    HasHandbrake = property(get_HasHandbrake, None)
    HasPatternShifter = property(get_HasPatternShifter, None)
    MaxPatternShifterGear = property(get_MaxPatternShifterGear, None)
    MaxWheelAngle = property(get_MaxWheelAngle, None)
    WheelMotor = property(get_WheelMotor, None)
class IRacingWheelStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3ac12cd5-581b-4936-9f-94-69-f1-e6-51-4c-7d')
    @winrt_commethod(6)
    def add_RacingWheelAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RacingWheel]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RacingWheelAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RacingWheelRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RacingWheel]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RacingWheelRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_RacingWheels(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.RacingWheel]: ...
    RacingWheels = property(get_RacingWheels, None)
class IRacingWheelStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e666bcaa-edfd-4323-a9-f6-3c-38-40-48-d1-ed')
    @winrt_commethod(6)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.RacingWheel: ...
class IRawGameController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cad6d91-a7e1-4f71-9a-78-33-e9-c5-df-ea-62')
    @winrt_commethod(6)
    def get_AxisCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ButtonCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ForceFeedbackMotors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor]: ...
    @winrt_commethod(9)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_SwitchCount(self) -> Int32: ...
    @winrt_commethod(12)
    def GetButtonLabel(self, buttonIndex: Int32) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(13)
    def GetCurrentReading(self, buttonArray: POINTER(Boolean), switchArray: POINTER(Windows.Gaming.Input.GameControllerSwitchPosition), axisArray: POINTER(Double)) -> UInt64: ...
    @winrt_commethod(14)
    def GetSwitchKind(self, switchIndex: Int32) -> Windows.Gaming.Input.GameControllerSwitchKind: ...
    AxisCount = property(get_AxisCount, None)
    ButtonCount = property(get_ButtonCount, None)
    ForceFeedbackMotors = property(get_ForceFeedbackMotors, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    SwitchCount = property(get_SwitchCount, None)
class IRawGameController2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('43c0c035-bb73-4756-a7-87-3e-d6-be-a6-17-bd')
    @winrt_commethod(6)
    def get_SimpleHapticsControllers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.SimpleHapticsController]: ...
    @winrt_commethod(7)
    def get_NonRoamableId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    SimpleHapticsControllers = property(get_SimpleHapticsControllers, None)
    NonRoamableId = property(get_NonRoamableId, None)
    DisplayName = property(get_DisplayName, None)
class IRawGameControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb8d0792-e95a-4b19-af-c7-0a-59-f8-bf-75-9e')
    @winrt_commethod(6)
    def add_RawGameControllerAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RawGameController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RawGameControllerAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RawGameControllerRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RawGameController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RawGameControllerRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_RawGameControllers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.RawGameController]: ...
    @winrt_commethod(11)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.RawGameController: ...
    RawGameControllers = property(get_RawGameControllers, None)
class IUINavigationController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5aeefdd-f50e-4a55-8c-dc-d3-32-29-54-81-75')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Gaming.Input.UINavigationReading: ...
    @winrt_commethod(7)
    def GetOptionalButtonLabel(self, button: Windows.Gaming.Input.OptionalUINavigationButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(8)
    def GetRequiredButtonLabel(self, button: Windows.Gaming.Input.RequiredUINavigationButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
class IUINavigationControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f14930a-f6f8-4a48-8d-89-94-78-6c-ca-0c-2e')
    @winrt_commethod(6)
    def add_UINavigationControllerAdded(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.UINavigationController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UINavigationControllerAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_UINavigationControllerRemoved(self, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.UINavigationController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_UINavigationControllerRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_UINavigationControllers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.UINavigationController]: ...
    UINavigationControllers = property(get_UINavigationControllers, None)
class IUINavigationControllerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e0cb28e3-b20b-4b0b-9e-d4-f3-d5-3c-ec-0d-e4')
    @winrt_commethod(6)
    def FromGameController(self, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.UINavigationController: ...
OptionalUINavigationButtons = UInt32
OptionalUINavigationButtons_None: OptionalUINavigationButtons = 0
OptionalUINavigationButtons_Context1: OptionalUINavigationButtons = 1
OptionalUINavigationButtons_Context2: OptionalUINavigationButtons = 2
OptionalUINavigationButtons_Context3: OptionalUINavigationButtons = 4
OptionalUINavigationButtons_Context4: OptionalUINavigationButtons = 8
OptionalUINavigationButtons_PageUp: OptionalUINavigationButtons = 16
OptionalUINavigationButtons_PageDown: OptionalUINavigationButtons = 32
OptionalUINavigationButtons_PageLeft: OptionalUINavigationButtons = 64
OptionalUINavigationButtons_PageRight: OptionalUINavigationButtons = 128
OptionalUINavigationButtons_ScrollUp: OptionalUINavigationButtons = 256
OptionalUINavigationButtons_ScrollDown: OptionalUINavigationButtons = 512
OptionalUINavigationButtons_ScrollLeft: OptionalUINavigationButtons = 1024
OptionalUINavigationButtons_ScrollRight: OptionalUINavigationButtons = 2048
class RacingWheel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.RacingWheel'
    @winrt_mixinmethod
    def get_HasClutch(self: Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasHandbrake(self: Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasPatternShifter(self: Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPatternShifterGear(self: Windows.Gaming.Input.IRacingWheel) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxWheelAngle(self: Windows.Gaming.Input.IRacingWheel) -> Double: ...
    @winrt_mixinmethod
    def get_WheelMotor(self: Windows.Gaming.Input.IRacingWheel) -> Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: Windows.Gaming.Input.IRacingWheel, button: Windows.Gaming.Input.RacingWheelButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IRacingWheel) -> Windows.Gaming.Input.RacingWheelReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IRacingWheelStatics2, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.RacingWheel: ...
    @winrt_classmethod
    def add_RacingWheelAdded(cls: Windows.Gaming.Input.IRacingWheelStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RacingWheel]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RacingWheelAdded(cls: Windows.Gaming.Input.IRacingWheelStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RacingWheelRemoved(cls: Windows.Gaming.Input.IRacingWheelStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RacingWheel]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RacingWheelRemoved(cls: Windows.Gaming.Input.IRacingWheelStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RacingWheels(cls: Windows.Gaming.Input.IRacingWheelStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.RacingWheel]: ...
    HasClutch = property(get_HasClutch, None)
    HasHandbrake = property(get_HasHandbrake, None)
    HasPatternShifter = property(get_HasPatternShifter, None)
    MaxPatternShifterGear = property(get_MaxPatternShifterGear, None)
    MaxWheelAngle = property(get_MaxWheelAngle, None)
    WheelMotor = property(get_WheelMotor, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    RacingWheels = property(get_RacingWheels, None)
RacingWheelButtons = UInt32
RacingWheelButtons_None: RacingWheelButtons = 0
RacingWheelButtons_PreviousGear: RacingWheelButtons = 1
RacingWheelButtons_NextGear: RacingWheelButtons = 2
RacingWheelButtons_DPadUp: RacingWheelButtons = 4
RacingWheelButtons_DPadDown: RacingWheelButtons = 8
RacingWheelButtons_DPadLeft: RacingWheelButtons = 16
RacingWheelButtons_DPadRight: RacingWheelButtons = 32
RacingWheelButtons_Button1: RacingWheelButtons = 64
RacingWheelButtons_Button2: RacingWheelButtons = 128
RacingWheelButtons_Button3: RacingWheelButtons = 256
RacingWheelButtons_Button4: RacingWheelButtons = 512
RacingWheelButtons_Button5: RacingWheelButtons = 1024
RacingWheelButtons_Button6: RacingWheelButtons = 2048
RacingWheelButtons_Button7: RacingWheelButtons = 4096
RacingWheelButtons_Button8: RacingWheelButtons = 8192
RacingWheelButtons_Button9: RacingWheelButtons = 16384
RacingWheelButtons_Button10: RacingWheelButtons = 32768
RacingWheelButtons_Button11: RacingWheelButtons = 65536
RacingWheelButtons_Button12: RacingWheelButtons = 131072
RacingWheelButtons_Button13: RacingWheelButtons = 262144
RacingWheelButtons_Button14: RacingWheelButtons = 524288
RacingWheelButtons_Button15: RacingWheelButtons = 1048576
RacingWheelButtons_Button16: RacingWheelButtons = 2097152
class RacingWheelReading(EasyCastStructure):
    Timestamp: UInt64
    Buttons: Windows.Gaming.Input.RacingWheelButtons
    PatternShifterGear: Int32
    Wheel: Double
    Throttle: Double
    Brake: Double
    Clutch: Double
    Handbrake: Double
class RawGameController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.RawGameController'
    @winrt_mixinmethod
    def get_AxisCount(self: Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def get_ButtonCount(self: Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def get_ForceFeedbackMotors(self: Windows.Gaming.Input.IRawGameController) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor]: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: Windows.Gaming.Input.IRawGameController) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: Windows.Gaming.Input.IRawGameController) -> UInt16: ...
    @winrt_mixinmethod
    def get_SwitchCount(self: Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: Windows.Gaming.Input.IRawGameController, buttonIndex: Int32) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IRawGameController, buttonArray: POINTER(Boolean), switchArray: POINTER(Windows.Gaming.Input.GameControllerSwitchPosition), axisArray: POINTER(Double)) -> UInt64: ...
    @winrt_mixinmethod
    def GetSwitchKind(self: Windows.Gaming.Input.IRawGameController, switchIndex: Int32) -> Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_mixinmethod
    def get_SimpleHapticsControllers(self: Windows.Gaming.Input.IRawGameController2) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Haptics.SimpleHapticsController]: ...
    @winrt_mixinmethod
    def get_NonRoamableId(self: Windows.Gaming.Input.IRawGameController2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Gaming.Input.IRawGameController2) -> WinRT_String: ...
    @winrt_classmethod
    def add_RawGameControllerAdded(cls: Windows.Gaming.Input.IRawGameControllerStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RawGameController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RawGameControllerAdded(cls: Windows.Gaming.Input.IRawGameControllerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RawGameControllerRemoved(cls: Windows.Gaming.Input.IRawGameControllerStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.RawGameController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RawGameControllerRemoved(cls: Windows.Gaming.Input.IRawGameControllerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RawGameControllers(cls: Windows.Gaming.Input.IRawGameControllerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.RawGameController]: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IRawGameControllerStatics, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.RawGameController: ...
    AxisCount = property(get_AxisCount, None)
    ButtonCount = property(get_ButtonCount, None)
    ForceFeedbackMotors = property(get_ForceFeedbackMotors, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    SwitchCount = property(get_SwitchCount, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    SimpleHapticsControllers = property(get_SimpleHapticsControllers, None)
    NonRoamableId = property(get_NonRoamableId, None)
    DisplayName = property(get_DisplayName, None)
    RawGameControllers = property(get_RawGameControllers, None)
RequiredUINavigationButtons = UInt32
RequiredUINavigationButtons_None: RequiredUINavigationButtons = 0
RequiredUINavigationButtons_Menu: RequiredUINavigationButtons = 1
RequiredUINavigationButtons_View: RequiredUINavigationButtons = 2
RequiredUINavigationButtons_Accept: RequiredUINavigationButtons = 4
RequiredUINavigationButtons_Cancel: RequiredUINavigationButtons = 8
RequiredUINavigationButtons_Up: RequiredUINavigationButtons = 16
RequiredUINavigationButtons_Down: RequiredUINavigationButtons = 32
RequiredUINavigationButtons_Left: RequiredUINavigationButtons = 64
RequiredUINavigationButtons_Right: RequiredUINavigationButtons = 128
class UINavigationController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.UINavigationController'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Gaming.Input.IUINavigationController) -> Windows.Gaming.Input.UINavigationReading: ...
    @winrt_mixinmethod
    def GetOptionalButtonLabel(self: Windows.Gaming.Input.IUINavigationController, button: Windows.Gaming.Input.OptionalUINavigationButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetRequiredButtonLabel(self: Windows.Gaming.Input.IUINavigationController, button: Windows.Gaming.Input.RequiredUINavigationButtons) -> Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.Gaming.Input.Headset]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: Windows.Gaming.Input.IGameController, value: Windows.Foundation.TypedEventHandler[Windows.Gaming.Input.IGameController, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: Windows.Gaming.Input.IGameController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.Input.IGameController) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.Gaming.Input.IGameControllerBatteryInfo) -> Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: Windows.Gaming.Input.IUINavigationControllerStatics2, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.UINavigationController: ...
    @winrt_classmethod
    def add_UINavigationControllerAdded(cls: Windows.Gaming.Input.IUINavigationControllerStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.UINavigationController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UINavigationControllerAdded(cls: Windows.Gaming.Input.IUINavigationControllerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_UINavigationControllerRemoved(cls: Windows.Gaming.Input.IUINavigationControllerStatics, value: Windows.Foundation.EventHandler[Windows.Gaming.Input.UINavigationController]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UINavigationControllerRemoved(cls: Windows.Gaming.Input.IUINavigationControllerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_UINavigationControllers(cls: Windows.Gaming.Input.IUINavigationControllerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.Input.UINavigationController]: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    UINavigationControllers = property(get_UINavigationControllers, None)
class UINavigationReading(EasyCastStructure):
    Timestamp: UInt64
    RequiredButtons: Windows.Gaming.Input.RequiredUINavigationButtons
    OptionalButtons: Windows.Gaming.Input.OptionalUINavigationButtons
make_head(_module, 'ArcadeStick')
make_head(_module, 'ArcadeStickReading')
make_head(_module, 'FlightStick')
make_head(_module, 'FlightStickReading')
make_head(_module, 'Gamepad')
make_head(_module, 'GamepadReading')
make_head(_module, 'GamepadVibration')
make_head(_module, 'Headset')
make_head(_module, 'IArcadeStick')
make_head(_module, 'IArcadeStickStatics')
make_head(_module, 'IArcadeStickStatics2')
make_head(_module, 'IFlightStick')
make_head(_module, 'IFlightStickStatics')
make_head(_module, 'IGameController')
make_head(_module, 'IGameControllerBatteryInfo')
make_head(_module, 'IGamepad')
make_head(_module, 'IGamepad2')
make_head(_module, 'IGamepadStatics')
make_head(_module, 'IGamepadStatics2')
make_head(_module, 'IHeadset')
make_head(_module, 'IRacingWheel')
make_head(_module, 'IRacingWheelStatics')
make_head(_module, 'IRacingWheelStatics2')
make_head(_module, 'IRawGameController')
make_head(_module, 'IRawGameController2')
make_head(_module, 'IRawGameControllerStatics')
make_head(_module, 'IUINavigationController')
make_head(_module, 'IUINavigationControllerStatics')
make_head(_module, 'IUINavigationControllerStatics2')
make_head(_module, 'RacingWheel')
make_head(_module, 'RacingWheelReading')
make_head(_module, 'RawGameController')
make_head(_module, 'UINavigationController')
make_head(_module, 'UINavigationReading')
