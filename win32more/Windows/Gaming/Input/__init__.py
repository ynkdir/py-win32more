from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Haptics
import win32more.Windows.Devices.Power
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.Input
import win32more.Windows.Gaming.Input.ForceFeedback
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class _ArcadeStick_Meta_(ComPtr.__class__):
    pass
class ArcadeStick(ComPtr, metaclass=_ArcadeStick_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IArcadeStick
    _classid_ = 'Windows.Gaming.Input.ArcadeStick'
    @winrt_mixinmethod
    def GetButtonLabel(self: win32more.Windows.Gaming.Input.IArcadeStick, button: win32more.Windows.Gaming.Input.ArcadeStickButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IArcadeStick) -> win32more.Windows.Gaming.Input.ArcadeStickReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics2, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.ArcadeStick: ...
    @winrt_classmethod
    def add_ArcadeStickAdded(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.ArcadeStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ArcadeStickAdded(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ArcadeStickRemoved(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.ArcadeStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ArcadeStickRemoved(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ArcadeSticks(cls: win32more.Windows.Gaming.Input.IArcadeStickStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.ArcadeStick]: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    _ArcadeStick_Meta_.ArcadeSticks = property(get_ArcadeSticks, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class ArcadeStickButtons(Enum, UInt32):
    None_ = 0
    StickUp = 1
    StickDown = 2
    StickLeft = 4
    StickRight = 8
    Action1 = 16
    Action2 = 32
    Action3 = 64
    Action4 = 128
    Action5 = 256
    Action6 = 512
    Special1 = 1024
    Special2 = 2048
class ArcadeStickReading(Structure):
    Timestamp: UInt64
    Buttons: win32more.Windows.Gaming.Input.ArcadeStickButtons
class _FlightStick_Meta_(ComPtr.__class__):
    pass
class FlightStick(ComPtr, metaclass=_FlightStick_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IFlightStick
    _classid_ = 'Windows.Gaming.Input.FlightStick'
    @winrt_mixinmethod
    def get_HatSwitchKind(self: win32more.Windows.Gaming.Input.IFlightStick) -> win32more.Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: win32more.Windows.Gaming.Input.IFlightStick, button: win32more.Windows.Gaming.Input.FlightStickButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IFlightStick) -> win32more.Windows.Gaming.Input.FlightStickReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def add_FlightStickAdded(cls: win32more.Windows.Gaming.Input.IFlightStickStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.FlightStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_FlightStickAdded(cls: win32more.Windows.Gaming.Input.IFlightStickStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_FlightStickRemoved(cls: win32more.Windows.Gaming.Input.IFlightStickStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.FlightStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_FlightStickRemoved(cls: win32more.Windows.Gaming.Input.IFlightStickStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_FlightSticks(cls: win32more.Windows.Gaming.Input.IFlightStickStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.FlightStick]: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IFlightStickStatics, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.FlightStick: ...
    HatSwitchKind = property(get_HatSwitchKind, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    _FlightStick_Meta_.FlightSticks = property(get_FlightSticks, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class FlightStickButtons(Enum, UInt32):
    None_ = 0
    FirePrimary = 1
    FireSecondary = 2
class FlightStickReading(Structure):
    Timestamp: UInt64
    Buttons: win32more.Windows.Gaming.Input.FlightStickButtons
    HatSwitch: win32more.Windows.Gaming.Input.GameControllerSwitchPosition
    Roll: Double
    Pitch: Double
    Yaw: Double
    Throttle: Double
class GameControllerButtonLabel(Enum, Int32):
    None_ = 0
    XboxBack = 1
    XboxStart = 2
    XboxMenu = 3
    XboxView = 4
    XboxUp = 5
    XboxDown = 6
    XboxLeft = 7
    XboxRight = 8
    XboxA = 9
    XboxB = 10
    XboxX = 11
    XboxY = 12
    XboxLeftBumper = 13
    XboxLeftTrigger = 14
    XboxLeftStickButton = 15
    XboxRightBumper = 16
    XboxRightTrigger = 17
    XboxRightStickButton = 18
    XboxPaddle1 = 19
    XboxPaddle2 = 20
    XboxPaddle3 = 21
    XboxPaddle4 = 22
    Mode = 23
    Select = 24
    Menu = 25
    View = 26
    Back = 27
    Start = 28
    Options = 29
    Share = 30
    Up = 31
    Down = 32
    Left = 33
    Right = 34
    LetterA = 35
    LetterB = 36
    LetterC = 37
    LetterL = 38
    LetterR = 39
    LetterX = 40
    LetterY = 41
    LetterZ = 42
    Cross = 43
    Circle = 44
    Square = 45
    Triangle = 46
    LeftBumper = 47
    LeftTrigger = 48
    LeftStickButton = 49
    Left1 = 50
    Left2 = 51
    Left3 = 52
    RightBumper = 53
    RightTrigger = 54
    RightStickButton = 55
    Right1 = 56
    Right2 = 57
    Right3 = 58
    Paddle1 = 59
    Paddle2 = 60
    Paddle3 = 61
    Paddle4 = 62
    Plus = 63
    Minus = 64
    DownLeftArrow = 65
    DialLeft = 66
    DialRight = 67
    Suspension = 68
class GameControllerSwitchKind(Enum, Int32):
    TwoWay = 0
    FourWay = 1
    EightWay = 2
class GameControllerSwitchPosition(Enum, Int32):
    Center = 0
    Up = 1
    UpRight = 2
    Right = 3
    DownRight = 4
    Down = 5
    DownLeft = 6
    Left = 7
    UpLeft = 8
class _Gamepad_Meta_(ComPtr.__class__):
    pass
class Gamepad(ComPtr, metaclass=_Gamepad_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IGamepad
    _classid_ = 'Windows.Gaming.Input.Gamepad'
    @winrt_mixinmethod
    def get_Vibration(self: win32more.Windows.Gaming.Input.IGamepad) -> win32more.Windows.Gaming.Input.GamepadVibration: ...
    @winrt_mixinmethod
    def put_Vibration(self: win32more.Windows.Gaming.Input.IGamepad, value: win32more.Windows.Gaming.Input.GamepadVibration) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IGamepad) -> win32more.Windows.Gaming.Input.GamepadReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: win32more.Windows.Gaming.Input.IGamepad2, button: win32more.Windows.Gaming.Input.GamepadButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IGamepadStatics2, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Gamepad: ...
    @winrt_classmethod
    def add_GamepadAdded(cls: win32more.Windows.Gaming.Input.IGamepadStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.Gamepad]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GamepadAdded(cls: win32more.Windows.Gaming.Input.IGamepadStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GamepadRemoved(cls: win32more.Windows.Gaming.Input.IGamepadStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.Gamepad]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GamepadRemoved(cls: win32more.Windows.Gaming.Input.IGamepadStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Gamepads(cls: win32more.Windows.Gaming.Input.IGamepadStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.Gamepad]: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    Vibration = property(get_Vibration, put_Vibration)
    _Gamepad_Meta_.Gamepads = property(get_Gamepads, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class GamepadButtons(Enum, UInt32):
    None_ = 0
    Menu = 1
    View = 2
    A = 4
    B = 8
    X = 16
    Y = 32
    DPadUp = 64
    DPadDown = 128
    DPadLeft = 256
    DPadRight = 512
    LeftShoulder = 1024
    RightShoulder = 2048
    LeftThumbstick = 4096
    RightThumbstick = 8192
    Paddle1 = 16384
    Paddle2 = 32768
    Paddle3 = 65536
    Paddle4 = 131072
class GamepadReading(Structure):
    Timestamp: UInt64
    Buttons: win32more.Windows.Gaming.Input.GamepadButtons
    LeftTrigger: Double
    RightTrigger: Double
    LeftThumbstickX: Double
    LeftThumbstickY: Double
    RightThumbstickX: Double
    RightThumbstickY: Double
class GamepadVibration(Structure):
    LeftMotor: Double
    RightMotor: Double
    LeftTrigger: Double
    RightTrigger: Double
GamingInputPreviewContract: UInt32 = 131072
class Headset(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IHeadset
    _classid_ = 'Windows.Gaming.Input.Headset'
    @winrt_mixinmethod
    def get_CaptureDeviceId(self: win32more.Windows.Gaming.Input.IHeadset) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RenderDeviceId(self: win32more.Windows.Gaming.Input.IHeadset) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    CaptureDeviceId = property(get_CaptureDeviceId, None)
    RenderDeviceId = property(get_RenderDeviceId, None)
class IArcadeStick(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IArcadeStick'
    _iid_ = Guid('{b14a539d-befb-4c81-8051-15ecf3b13036}')
    @winrt_commethod(6)
    def GetButtonLabel(self, button: win32more.Windows.Gaming.Input.ArcadeStickButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(7)
    def GetCurrentReading(self) -> win32more.Windows.Gaming.Input.ArcadeStickReading: ...
class IArcadeStickStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IArcadeStickStatics'
    _iid_ = Guid('{5c37b8c8-37b1-4ad8-9458-200f1a30018e}')
    @winrt_commethod(6)
    def add_ArcadeStickAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.ArcadeStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ArcadeStickAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ArcadeStickRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.ArcadeStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ArcadeStickRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_ArcadeSticks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.ArcadeStick]: ...
    ArcadeSticks = property(get_ArcadeSticks, None)
    ArcadeStickAdded = event()
    ArcadeStickRemoved = event()
class IArcadeStickStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IArcadeStickStatics2'
    _iid_ = Guid('{52b5d744-bb86-445a-b59c-596f0e2a49df}')
    @winrt_commethod(6)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.ArcadeStick: ...
class IFlightStick(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IFlightStick'
    _iid_ = Guid('{b4a2c01c-b83b-4459-a1a9-97b03c33da7c}')
    @winrt_commethod(6)
    def get_HatSwitchKind(self) -> win32more.Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_commethod(7)
    def GetButtonLabel(self, button: win32more.Windows.Gaming.Input.FlightStickButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(8)
    def GetCurrentReading(self) -> win32more.Windows.Gaming.Input.FlightStickReading: ...
    HatSwitchKind = property(get_HatSwitchKind, None)
class IFlightStickStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IFlightStickStatics'
    _iid_ = Guid('{5514924a-fecc-435e-83dc-5cec8a18a520}')
    @winrt_commethod(6)
    def add_FlightStickAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.FlightStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FlightStickAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_FlightStickRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.FlightStick]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_FlightStickRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_FlightSticks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.FlightStick]: ...
    @winrt_commethod(11)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.FlightStick: ...
    FlightSticks = property(get_FlightSticks, None)
    FlightStickAdded = event()
    FlightStickRemoved = event()
class IGameController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGameController'
    _iid_ = Guid('{1baf6522-5f64-42c5-8267-b9fe2215bfbd}')
    @winrt_commethod(6)
    def add_HeadsetConnected(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_HeadsetConnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_HeadsetDisconnected(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HeadsetDisconnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_UserChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UserChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Headset(self) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_commethod(13)
    def get_IsWireless(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_User(self) -> win32more.Windows.System.User: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class IGameControllerBatteryInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGameControllerBatteryInfo'
    _iid_ = Guid('{dcecc681-3963-4da6-955d-553f3b6f6161}')
    @winrt_commethod(6)
    def TryGetBatteryReport(self) -> win32more.Windows.Devices.Power.BatteryReport: ...
class IGamepad(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGamepad'
    _iid_ = Guid('{bc7bb43c-0a69-3903-9e9d-a50f86a45de5}')
    @winrt_commethod(6)
    def get_Vibration(self) -> win32more.Windows.Gaming.Input.GamepadVibration: ...
    @winrt_commethod(7)
    def put_Vibration(self, value: win32more.Windows.Gaming.Input.GamepadVibration) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentReading(self) -> win32more.Windows.Gaming.Input.GamepadReading: ...
    Vibration = property(get_Vibration, put_Vibration)
class IGamepad2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGamepad2'
    _iid_ = Guid('{3c1689bd-5915-4245-b0c0-c89fae0308ff}')
    @winrt_commethod(6)
    def GetButtonLabel(self, button: win32more.Windows.Gaming.Input.GamepadButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
class IGamepadStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGamepadStatics'
    _iid_ = Guid('{8bbce529-d49c-39e9-9560-e47dde96b7c8}')
    @winrt_commethod(6)
    def add_GamepadAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.Gamepad]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GamepadAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_GamepadRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.Gamepad]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GamepadRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Gamepads(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.Gamepad]: ...
    Gamepads = property(get_Gamepads, None)
    GamepadAdded = event()
    GamepadRemoved = event()
class IGamepadStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IGamepadStatics2'
    _iid_ = Guid('{42676dc5-0856-47c4-9213-b395504c3a3c}')
    @winrt_commethod(6)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Gamepad: ...
class IHeadset(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IHeadset'
    _iid_ = Guid('{3fd156ef-6925-3fa8-9181-029c5223ae3b}')
    @winrt_commethod(6)
    def get_CaptureDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RenderDeviceId(self) -> WinRT_String: ...
    CaptureDeviceId = property(get_CaptureDeviceId, None)
    RenderDeviceId = property(get_RenderDeviceId, None)
class IRacingWheel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRacingWheel'
    _iid_ = Guid('{f546656f-e106-4c82-a90f-554012904b85}')
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
    def get_WheelMotor(self) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor: ...
    @winrt_commethod(12)
    def GetButtonLabel(self, button: win32more.Windows.Gaming.Input.RacingWheelButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(13)
    def GetCurrentReading(self) -> win32more.Windows.Gaming.Input.RacingWheelReading: ...
    HasClutch = property(get_HasClutch, None)
    HasHandbrake = property(get_HasHandbrake, None)
    HasPatternShifter = property(get_HasPatternShifter, None)
    MaxPatternShifterGear = property(get_MaxPatternShifterGear, None)
    MaxWheelAngle = property(get_MaxWheelAngle, None)
    WheelMotor = property(get_WheelMotor, None)
class IRacingWheelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRacingWheelStatics'
    _iid_ = Guid('{3ac12cd5-581b-4936-9f94-69f1e6514c7d}')
    @winrt_commethod(6)
    def add_RacingWheelAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RacingWheel]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RacingWheelAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RacingWheelRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RacingWheel]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RacingWheelRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_RacingWheels(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.RacingWheel]: ...
    RacingWheels = property(get_RacingWheels, None)
    RacingWheelAdded = event()
    RacingWheelRemoved = event()
class IRacingWheelStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRacingWheelStatics2'
    _iid_ = Guid('{e666bcaa-edfd-4323-a9f6-3c384048d1ed}')
    @winrt_commethod(6)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.RacingWheel: ...
class IRawGameController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRawGameController'
    _iid_ = Guid('{7cad6d91-a7e1-4f71-9a78-33e9c5dfea62}')
    @winrt_commethod(6)
    def get_AxisCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ButtonCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ForceFeedbackMotors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor]: ...
    @winrt_commethod(9)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_SwitchCount(self) -> Int32: ...
    @winrt_commethod(12)
    def GetButtonLabel(self, buttonIndex: Int32) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(13)
    def GetCurrentReading(self, buttonArray: FillArray[Boolean], switchArray: FillArray[win32more.Windows.Gaming.Input.GameControllerSwitchPosition], axisArray: FillArray[Double]) -> UInt64: ...
    @winrt_commethod(14)
    def GetSwitchKind(self, switchIndex: Int32) -> win32more.Windows.Gaming.Input.GameControllerSwitchKind: ...
    AxisCount = property(get_AxisCount, None)
    ButtonCount = property(get_ButtonCount, None)
    ForceFeedbackMotors = property(get_ForceFeedbackMotors, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    SwitchCount = property(get_SwitchCount, None)
class IRawGameController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRawGameController2'
    _iid_ = Guid('{43c0c035-bb73-4756-a787-3ed6bea617bd}')
    @winrt_commethod(6)
    def get_SimpleHapticsControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.SimpleHapticsController]: ...
    @winrt_commethod(7)
    def get_NonRoamableId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    NonRoamableId = property(get_NonRoamableId, None)
    SimpleHapticsControllers = property(get_SimpleHapticsControllers, None)
class IRawGameControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IRawGameControllerStatics'
    _iid_ = Guid('{eb8d0792-e95a-4b19-afc7-0a59f8bf759e}')
    @winrt_commethod(6)
    def add_RawGameControllerAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RawGameController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RawGameControllerAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RawGameControllerRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RawGameController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RawGameControllerRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_RawGameControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.RawGameController]: ...
    @winrt_commethod(11)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.RawGameController: ...
    RawGameControllers = property(get_RawGameControllers, None)
    RawGameControllerAdded = event()
    RawGameControllerRemoved = event()
class IUINavigationController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IUINavigationController'
    _iid_ = Guid('{e5aeefdd-f50e-4a55-8cdc-d33229548175}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> win32more.Windows.Gaming.Input.UINavigationReading: ...
    @winrt_commethod(7)
    def GetOptionalButtonLabel(self, button: win32more.Windows.Gaming.Input.OptionalUINavigationButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_commethod(8)
    def GetRequiredButtonLabel(self, button: win32more.Windows.Gaming.Input.RequiredUINavigationButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
class IUINavigationControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IUINavigationControllerStatics'
    _iid_ = Guid('{2f14930a-f6f8-4a48-8d89-94786cca0c2e}')
    @winrt_commethod(6)
    def add_UINavigationControllerAdded(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.UINavigationController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UINavigationControllerAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_UINavigationControllerRemoved(self, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.UINavigationController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_UINavigationControllerRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_UINavigationControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.UINavigationController]: ...
    UINavigationControllers = property(get_UINavigationControllers, None)
    UINavigationControllerAdded = event()
    UINavigationControllerRemoved = event()
class IUINavigationControllerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.IUINavigationControllerStatics2'
    _iid_ = Guid('{e0cb28e3-b20b-4b0b-9ed4-f3d53cec0de4}')
    @winrt_commethod(6)
    def FromGameController(self, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.UINavigationController: ...
class OptionalUINavigationButtons(Enum, UInt32):
    None_ = 0
    Context1 = 1
    Context2 = 2
    Context3 = 4
    Context4 = 8
    PageUp = 16
    PageDown = 32
    PageLeft = 64
    PageRight = 128
    ScrollUp = 256
    ScrollDown = 512
    ScrollLeft = 1024
    ScrollRight = 2048
class _RacingWheel_Meta_(ComPtr.__class__):
    pass
class RacingWheel(ComPtr, metaclass=_RacingWheel_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IRacingWheel
    _classid_ = 'Windows.Gaming.Input.RacingWheel'
    @winrt_mixinmethod
    def get_HasClutch(self: win32more.Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasHandbrake(self: win32more.Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasPatternShifter(self: win32more.Windows.Gaming.Input.IRacingWheel) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPatternShifterGear(self: win32more.Windows.Gaming.Input.IRacingWheel) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxWheelAngle(self: win32more.Windows.Gaming.Input.IRacingWheel) -> Double: ...
    @winrt_mixinmethod
    def get_WheelMotor(self: win32more.Windows.Gaming.Input.IRacingWheel) -> win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: win32more.Windows.Gaming.Input.IRacingWheel, button: win32more.Windows.Gaming.Input.RacingWheelButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IRacingWheel) -> win32more.Windows.Gaming.Input.RacingWheelReading: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics2, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.RacingWheel: ...
    @winrt_classmethod
    def add_RacingWheelAdded(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RacingWheel]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RacingWheelAdded(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RacingWheelRemoved(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RacingWheel]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RacingWheelRemoved(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RacingWheels(cls: win32more.Windows.Gaming.Input.IRacingWheelStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.RacingWheel]: ...
    HasClutch = property(get_HasClutch, None)
    HasHandbrake = property(get_HasHandbrake, None)
    HasPatternShifter = property(get_HasPatternShifter, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    MaxPatternShifterGear = property(get_MaxPatternShifterGear, None)
    MaxWheelAngle = property(get_MaxWheelAngle, None)
    User = property(get_User, None)
    WheelMotor = property(get_WheelMotor, None)
    _RacingWheel_Meta_.RacingWheels = property(get_RacingWheels, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class RacingWheelButtons(Enum, UInt32):
    None_ = 0
    PreviousGear = 1
    NextGear = 2
    DPadUp = 4
    DPadDown = 8
    DPadLeft = 16
    DPadRight = 32
    Button1 = 64
    Button2 = 128
    Button3 = 256
    Button4 = 512
    Button5 = 1024
    Button6 = 2048
    Button7 = 4096
    Button8 = 8192
    Button9 = 16384
    Button10 = 32768
    Button11 = 65536
    Button12 = 131072
    Button13 = 262144
    Button14 = 524288
    Button15 = 1048576
    Button16 = 2097152
class RacingWheelReading(Structure):
    Timestamp: UInt64
    Buttons: win32more.Windows.Gaming.Input.RacingWheelButtons
    PatternShifterGear: Int32
    Wheel: Double
    Throttle: Double
    Brake: Double
    Clutch: Double
    Handbrake: Double
class _RawGameController_Meta_(ComPtr.__class__):
    pass
class RawGameController(ComPtr, metaclass=_RawGameController_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IRawGameController
    _classid_ = 'Windows.Gaming.Input.RawGameController'
    @winrt_mixinmethod
    def get_AxisCount(self: win32more.Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def get_ButtonCount(self: win32more.Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def get_ForceFeedbackMotors(self: win32more.Windows.Gaming.Input.IRawGameController) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.ForceFeedback.ForceFeedbackMotor]: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: win32more.Windows.Gaming.Input.IRawGameController) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: win32more.Windows.Gaming.Input.IRawGameController) -> UInt16: ...
    @winrt_mixinmethod
    def get_SwitchCount(self: win32more.Windows.Gaming.Input.IRawGameController) -> Int32: ...
    @winrt_mixinmethod
    def GetButtonLabel(self: win32more.Windows.Gaming.Input.IRawGameController, buttonIndex: Int32) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IRawGameController, buttonArray: FillArray[Boolean], switchArray: FillArray[win32more.Windows.Gaming.Input.GameControllerSwitchPosition], axisArray: FillArray[Double]) -> UInt64: ...
    @winrt_mixinmethod
    def GetSwitchKind(self: win32more.Windows.Gaming.Input.IRawGameController, switchIndex: Int32) -> win32more.Windows.Gaming.Input.GameControllerSwitchKind: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_mixinmethod
    def get_SimpleHapticsControllers(self: win32more.Windows.Gaming.Input.IRawGameController2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Haptics.SimpleHapticsController]: ...
    @winrt_mixinmethod
    def get_NonRoamableId(self: win32more.Windows.Gaming.Input.IRawGameController2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Gaming.Input.IRawGameController2) -> WinRT_String: ...
    @winrt_classmethod
    def add_RawGameControllerAdded(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RawGameController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RawGameControllerAdded(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RawGameControllerRemoved(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.RawGameController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RawGameControllerRemoved(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RawGameControllers(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.RawGameController]: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IRawGameControllerStatics, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.RawGameController: ...
    AxisCount = property(get_AxisCount, None)
    ButtonCount = property(get_ButtonCount, None)
    DisplayName = property(get_DisplayName, None)
    ForceFeedbackMotors = property(get_ForceFeedbackMotors, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    NonRoamableId = property(get_NonRoamableId, None)
    SimpleHapticsControllers = property(get_SimpleHapticsControllers, None)
    SwitchCount = property(get_SwitchCount, None)
    User = property(get_User, None)
    _RawGameController_Meta_.RawGameControllers = property(get_RawGameControllers, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class RequiredUINavigationButtons(Enum, UInt32):
    None_ = 0
    Menu = 1
    View = 2
    Accept = 4
    Cancel = 8
    Up = 16
    Down = 32
    Left = 64
    Right = 128
class _UINavigationController_Meta_(ComPtr.__class__):
    pass
class UINavigationController(ComPtr, metaclass=_UINavigationController_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.IUINavigationController
    _classid_ = 'Windows.Gaming.Input.UINavigationController'
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Gaming.Input.IUINavigationController) -> win32more.Windows.Gaming.Input.UINavigationReading: ...
    @winrt_mixinmethod
    def GetOptionalButtonLabel(self: win32more.Windows.Gaming.Input.IUINavigationController, button: win32more.Windows.Gaming.Input.OptionalUINavigationButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def GetRequiredButtonLabel(self: win32more.Windows.Gaming.Input.IUINavigationController, button: win32more.Windows.Gaming.Input.RequiredUINavigationButtons) -> win32more.Windows.Gaming.Input.GameControllerButtonLabel: ...
    @winrt_mixinmethod
    def add_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetConnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.Gaming.Input.Headset]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadsetDisconnected(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.Input.IGameController, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserChanged(self: win32more.Windows.Gaming.Input.IGameController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Headset(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.Headset: ...
    @winrt_mixinmethod
    def get_IsWireless(self: win32more.Windows.Gaming.Input.IGameController) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.Gaming.Input.IGameControllerBatteryInfo) -> win32more.Windows.Devices.Power.BatteryReport: ...
    @winrt_classmethod
    def FromGameController(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics2, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.UINavigationController: ...
    @winrt_classmethod
    def add_UINavigationControllerAdded(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.UINavigationController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UINavigationControllerAdded(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_UINavigationControllerRemoved(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics, value: win32more.Windows.Foundation.EventHandler[win32more.Windows.Gaming.Input.UINavigationController]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UINavigationControllerRemoved(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_UINavigationControllers(cls: win32more.Windows.Gaming.Input.IUINavigationControllerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Input.UINavigationController]: ...
    Headset = property(get_Headset, None)
    IsWireless = property(get_IsWireless, None)
    User = property(get_User, None)
    _UINavigationController_Meta_.UINavigationControllers = property(get_UINavigationControllers, None)
    HeadsetConnected = event()
    HeadsetDisconnected = event()
    UserChanged = event()
class UINavigationReading(Structure):
    Timestamp: UInt64
    RequiredButtons: win32more.Windows.Gaming.Input.RequiredUINavigationButtons
    OptionalButtons: win32more.Windows.Gaming.Input.OptionalUINavigationButtons


make_ready(__name__)
