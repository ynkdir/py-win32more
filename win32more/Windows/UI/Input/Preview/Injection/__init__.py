from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.Input
import win32more.Windows.UI.Input.Preview.Injection
import win32more.Windows.Win32.System.WinRT
class IInjectedInputGamepadInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo'
    _iid_ = Guid('{20ae9a3f-df11-4572-a9ab-d75b8a5e48ad}')
    @winrt_commethod(6)
    def get_Buttons(self) -> win32more.Windows.Gaming.Input.GamepadButtons: ...
    @winrt_commethod(7)
    def put_Buttons(self, value: win32more.Windows.Gaming.Input.GamepadButtons) -> Void: ...
    @winrt_commethod(8)
    def get_LeftThumbstickX(self) -> Double: ...
    @winrt_commethod(9)
    def put_LeftThumbstickX(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_LeftThumbstickY(self) -> Double: ...
    @winrt_commethod(11)
    def put_LeftThumbstickY(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_LeftTrigger(self) -> Double: ...
    @winrt_commethod(13)
    def put_LeftTrigger(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_RightThumbstickX(self) -> Double: ...
    @winrt_commethod(15)
    def put_RightThumbstickX(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_RightThumbstickY(self) -> Double: ...
    @winrt_commethod(17)
    def put_RightThumbstickY(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_RightTrigger(self) -> Double: ...
    @winrt_commethod(19)
    def put_RightTrigger(self, value: Double) -> Void: ...
    Buttons = property(get_Buttons, put_Buttons)
    LeftThumbstickX = property(get_LeftThumbstickX, put_LeftThumbstickX)
    LeftThumbstickY = property(get_LeftThumbstickY, put_LeftThumbstickY)
    LeftTrigger = property(get_LeftTrigger, put_LeftTrigger)
    RightThumbstickX = property(get_RightThumbstickX, put_RightThumbstickX)
    RightThumbstickY = property(get_RightThumbstickY, put_RightThumbstickY)
    RightTrigger = property(get_RightTrigger, put_RightTrigger)
class IInjectedInputGamepadInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfoFactory'
    _iid_ = Guid('{59596876-6c39-4ec4-8b2a-29ef7de18aca}')
    @winrt_commethod(6)
    def CreateInstanceFromGamepadReading(self, reading: win32more.Windows.Gaming.Input.GamepadReading) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo: ...
class IInjectedInputKeyboardInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo'
    _iid_ = Guid('{4b46d140-2b6a-5ffa-7eae-bd077b052acd}')
    @winrt_commethod(6)
    def get_KeyOptions(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions: ...
    @winrt_commethod(7)
    def put_KeyOptions(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions) -> Void: ...
    @winrt_commethod(8)
    def get_ScanCode(self) -> UInt16: ...
    @winrt_commethod(9)
    def put_ScanCode(self, value: UInt16) -> Void: ...
    @winrt_commethod(10)
    def get_VirtualKey(self) -> UInt16: ...
    @winrt_commethod(11)
    def put_VirtualKey(self, value: UInt16) -> Void: ...
    KeyOptions = property(get_KeyOptions, put_KeyOptions)
    ScanCode = property(get_ScanCode, put_ScanCode)
    VirtualKey = property(get_VirtualKey, put_VirtualKey)
class IInjectedInputMouseInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo'
    _iid_ = Guid('{96f56e6b-e47a-5cf4-418d-8a5fb9670c7d}')
    @winrt_commethod(6)
    def get_MouseOptions(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions: ...
    @winrt_commethod(7)
    def put_MouseOptions(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions) -> Void: ...
    @winrt_commethod(8)
    def get_MouseData(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_MouseData(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_DeltaY(self) -> Int32: ...
    @winrt_commethod(11)
    def put_DeltaY(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_DeltaX(self) -> Int32: ...
    @winrt_commethod(13)
    def put_DeltaX(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_TimeOffsetInMilliseconds(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_TimeOffsetInMilliseconds(self, value: UInt32) -> Void: ...
    DeltaX = property(get_DeltaX, put_DeltaX)
    DeltaY = property(get_DeltaY, put_DeltaY)
    MouseData = property(get_MouseData, put_MouseData)
    MouseOptions = property(get_MouseOptions, put_MouseOptions)
    TimeOffsetInMilliseconds = property(get_TimeOffsetInMilliseconds, put_TimeOffsetInMilliseconds)
class IInjectedInputPenInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo'
    _iid_ = Guid('{6b40ad03-ca1e-5527-7e02-2828540bb1d4}')
    @winrt_commethod(6)
    def get_PointerInfo(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo: ...
    @winrt_commethod(7)
    def put_PointerInfo(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo) -> Void: ...
    @winrt_commethod(8)
    def get_PenButtons(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons: ...
    @winrt_commethod(9)
    def put_PenButtons(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons) -> Void: ...
    @winrt_commethod(10)
    def get_PenParameters(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters: ...
    @winrt_commethod(11)
    def put_PenParameters(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters) -> Void: ...
    @winrt_commethod(12)
    def get_Pressure(self) -> Double: ...
    @winrt_commethod(13)
    def put_Pressure(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_Rotation(self) -> Double: ...
    @winrt_commethod(15)
    def put_Rotation(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_TiltX(self) -> Int32: ...
    @winrt_commethod(17)
    def put_TiltX(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_TiltY(self) -> Int32: ...
    @winrt_commethod(19)
    def put_TiltY(self, value: Int32) -> Void: ...
    PenButtons = property(get_PenButtons, put_PenButtons)
    PenParameters = property(get_PenParameters, put_PenParameters)
    PointerInfo = property(get_PointerInfo, put_PointerInfo)
    Pressure = property(get_Pressure, put_Pressure)
    Rotation = property(get_Rotation, put_Rotation)
    TiltX = property(get_TiltX, put_TiltX)
    TiltY = property(get_TiltY, put_TiltY)
class IInjectedInputTouchInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo'
    _iid_ = Guid('{224fd1df-43e8-5ef5-510a-69ca8c9b4c28}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputRectangle: ...
    @winrt_commethod(7)
    def put_Contact(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputRectangle) -> Void: ...
    @winrt_commethod(8)
    def get_Orientation(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Orientation(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_PointerInfo(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo: ...
    @winrt_commethod(11)
    def put_PointerInfo(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo) -> Void: ...
    @winrt_commethod(12)
    def get_Pressure(self) -> Double: ...
    @winrt_commethod(13)
    def put_Pressure(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_TouchParameters(self) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters: ...
    @winrt_commethod(15)
    def put_TouchParameters(self, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters) -> Void: ...
    Contact = property(get_Contact, put_Contact)
    Orientation = property(get_Orientation, put_Orientation)
    PointerInfo = property(get_PointerInfo, put_PointerInfo)
    Pressure = property(get_Pressure, put_Pressure)
    TouchParameters = property(get_TouchParameters, put_TouchParameters)
class IInputInjector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInputInjector'
    _iid_ = Guid('{8ec26f84-0b02-4bd2-ad7a-3d4658be3e18}')
    @winrt_commethod(6)
    def InjectKeyboardInput(self, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyboardInfo]) -> Void: ...
    @winrt_commethod(7)
    def InjectMouseInput(self, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseInfo]) -> Void: ...
    @winrt_commethod(8)
    def InitializeTouchInjection(self, visualMode: win32more.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode) -> Void: ...
    @winrt_commethod(9)
    def InjectTouchInput(self, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchInfo]) -> Void: ...
    @winrt_commethod(10)
    def UninitializeTouchInjection(self) -> Void: ...
    @winrt_commethod(11)
    def InitializePenInjection(self, visualMode: win32more.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode) -> Void: ...
    @winrt_commethod(12)
    def InjectPenInput(self, input: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenInfo) -> Void: ...
    @winrt_commethod(13)
    def UninitializePenInjection(self) -> Void: ...
    @winrt_commethod(14)
    def InjectShortcut(self, shortcut: win32more.Windows.UI.Input.Preview.Injection.InjectedInputShortcut) -> Void: ...
class IInputInjector2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInputInjector2'
    _iid_ = Guid('{8e7a905d-1453-43a7-9bcb-06d6d7b305f7}')
    @winrt_commethod(6)
    def InitializeGamepadInjection(self) -> Void: ...
    @winrt_commethod(7)
    def InjectGamepadInput(self, input: win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo) -> Void: ...
    @winrt_commethod(8)
    def UninitializeGamepadInjection(self) -> Void: ...
class IInputInjectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInputInjectorStatics'
    _iid_ = Guid('{deae6943-7402-4141-a5c6-0c01aa57b16a}')
    @winrt_commethod(6)
    def TryCreate(self) -> win32more.Windows.UI.Input.Preview.Injection.InputInjector: ...
class IInputInjectorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.Injection.IInputInjectorStatics2'
    _iid_ = Guid('{a4db38fb-dd8c-414f-95ea-f87ef4c0ae6c}')
    @winrt_commethod(6)
    def TryCreateForAppBroadcastOnly(self) -> win32more.Windows.UI.Input.Preview.Injection.InputInjector: ...
class InjectedInputButtonChangeKind(Enum, Int32):
    None_ = 0
    FirstButtonDown = 1
    FirstButtonUp = 2
    SecondButtonDown = 3
    SecondButtonUp = 4
    ThirdButtonDown = 5
    ThirdButtonUp = 6
    FourthButtonDown = 7
    FourthButtonUp = 8
    FifthButtonDown = 9
    FifthButtonUp = 10
class InjectedInputGamepadInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo
    _classid_ = 'Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo.CreateInstanceFromGamepadReading(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo: ...
    @winrt_factorymethod
    def CreateInstanceFromGamepadReading(cls: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfoFactory, reading: win32more.Windows.Gaming.Input.GamepadReading) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo: ...
    @winrt_mixinmethod
    def get_Buttons(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> win32more.Windows.Gaming.Input.GamepadButtons: ...
    @winrt_mixinmethod
    def put_Buttons(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: win32more.Windows.Gaming.Input.GamepadButtons) -> Void: ...
    @winrt_mixinmethod
    def get_LeftThumbstickX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_LeftThumbstickX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LeftThumbstickY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_LeftThumbstickY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LeftTrigger(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_LeftTrigger(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RightThumbstickX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_RightThumbstickX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RightThumbstickY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_RightThumbstickY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RightTrigger(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo) -> Double: ...
    @winrt_mixinmethod
    def put_RightTrigger(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputGamepadInfo, value: Double) -> Void: ...
    Buttons = property(get_Buttons, put_Buttons)
    LeftThumbstickX = property(get_LeftThumbstickX, put_LeftThumbstickX)
    LeftThumbstickY = property(get_LeftThumbstickY, put_LeftThumbstickY)
    LeftTrigger = property(get_LeftTrigger, put_LeftTrigger)
    RightThumbstickX = property(get_RightThumbstickX, put_RightThumbstickX)
    RightThumbstickY = property(get_RightThumbstickY, put_RightThumbstickY)
    RightTrigger = property(get_RightTrigger, put_RightTrigger)
class InjectedInputKeyOptions(Enum, UInt32):
    None_ = 0
    ExtendedKey = 1
    KeyUp = 2
    ScanCode = 8
    Unicode = 4
class InjectedInputKeyboardInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo
    _classid_ = 'Windows.UI.Input.Preview.Injection.InjectedInputKeyboardInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyboardInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyboardInfo: ...
    @winrt_mixinmethod
    def get_KeyOptions(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions: ...
    @winrt_mixinmethod
    def put_KeyOptions(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ScanCode(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo) -> UInt16: ...
    @winrt_mixinmethod
    def put_ScanCode(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo) -> UInt16: ...
    @winrt_mixinmethod
    def put_VirtualKey(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputKeyboardInfo, value: UInt16) -> Void: ...
    KeyOptions = property(get_KeyOptions, put_KeyOptions)
    ScanCode = property(get_ScanCode, put_ScanCode)
    VirtualKey = property(get_VirtualKey, put_VirtualKey)
class InjectedInputMouseInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo
    _classid_ = 'Windows.UI.Input.Preview.Injection.InjectedInputMouseInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseInfo: ...
    @winrt_mixinmethod
    def get_MouseOptions(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions: ...
    @winrt_mixinmethod
    def put_MouseOptions(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions) -> Void: ...
    @winrt_mixinmethod
    def get_MouseData(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_MouseData(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_DeltaY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_DeltaX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TimeOffsetInMilliseconds(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_TimeOffsetInMilliseconds(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputMouseInfo, value: UInt32) -> Void: ...
    DeltaX = property(get_DeltaX, put_DeltaX)
    DeltaY = property(get_DeltaY, put_DeltaY)
    MouseData = property(get_MouseData, put_MouseData)
    MouseOptions = property(get_MouseOptions, put_MouseOptions)
    TimeOffsetInMilliseconds = property(get_TimeOffsetInMilliseconds, put_TimeOffsetInMilliseconds)
class InjectedInputMouseOptions(Enum, UInt32):
    None_ = 0
    Move = 1
    LeftDown = 2
    LeftUp = 4
    RightDown = 8
    RightUp = 16
    MiddleDown = 32
    MiddleUp = 64
    XDown = 128
    XUp = 256
    Wheel = 2048
    HWheel = 4096
    MoveNoCoalesce = 8192
    VirtualDesk = 16384
    Absolute = 32768
class InjectedInputPenButtons(Enum, UInt32):
    None_ = 0
    Barrel = 1
    Inverted = 2
    Eraser = 4
class InjectedInputPenInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo
    _classid_ = 'Windows.UI.Input.Preview.Injection.InjectedInputPenInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenInfo: ...
    @winrt_mixinmethod
    def get_PointerInfo(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo: ...
    @winrt_mixinmethod
    def put_PointerInfo(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo) -> Void: ...
    @winrt_mixinmethod
    def get_PenButtons(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons: ...
    @winrt_mixinmethod
    def put_PenButtons(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons) -> Void: ...
    @winrt_mixinmethod
    def get_PenParameters(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters: ...
    @winrt_mixinmethod
    def put_PenParameters(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters) -> Void: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> Double: ...
    @winrt_mixinmethod
    def put_Pressure(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> Double: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TiltX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_TiltX(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TiltY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_TiltY(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputPenInfo, value: Int32) -> Void: ...
    PenButtons = property(get_PenButtons, put_PenButtons)
    PenParameters = property(get_PenParameters, put_PenParameters)
    PointerInfo = property(get_PointerInfo, put_PointerInfo)
    Pressure = property(get_Pressure, put_Pressure)
    Rotation = property(get_Rotation, put_Rotation)
    TiltX = property(get_TiltX, put_TiltX)
    TiltY = property(get_TiltY, put_TiltY)
class InjectedInputPenParameters(Enum, UInt32):
    None_ = 0
    Pressure = 1
    Rotation = 2
    TiltX = 4
    TiltY = 8
class InjectedInputPoint(Structure):
    PositionX: Int32
    PositionY: Int32
class InjectedInputPointerInfo(Structure):
    PointerId: UInt32
    PointerOptions: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerOptions
    PixelLocation: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPoint
    TimeOffsetInMilliseconds: UInt32
    PerformanceCount: UInt64
class InjectedInputPointerOptions(Enum, UInt32):
    None_ = 0
    New = 1
    InRange = 2
    InContact = 4
    FirstButton = 16
    SecondButton = 32
    Primary = 8192
    Confidence = 16384
    Canceled = 32768
    PointerDown = 65536
    Update = 131072
    PointerUp = 262144
    CaptureChanged = 2097152
class InjectedInputRectangle(Structure):
    Left: Int32
    Top: Int32
    Bottom: Int32
    Right: Int32
class InjectedInputShortcut(Enum, Int32):
    Back = 0
    Start = 1
    Search = 2
class InjectedInputTouchInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo
    _classid_ = 'Windows.UI.Input.Preview.Injection.InjectedInputTouchInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchInfo: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputRectangle: ...
    @winrt_mixinmethod
    def put_Contact(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputRectangle) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_PointerInfo(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo: ...
    @winrt_mixinmethod
    def put_PointerInfo(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo) -> Void: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo) -> Double: ...
    @winrt_mixinmethod
    def put_Pressure(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TouchParameters(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo) -> win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters: ...
    @winrt_mixinmethod
    def put_TouchParameters(self: win32more.Windows.UI.Input.Preview.Injection.IInjectedInputTouchInfo, value: win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters) -> Void: ...
    Contact = property(get_Contact, put_Contact)
    Orientation = property(get_Orientation, put_Orientation)
    PointerInfo = property(get_PointerInfo, put_PointerInfo)
    Pressure = property(get_Pressure, put_Pressure)
    TouchParameters = property(get_TouchParameters, put_TouchParameters)
class InjectedInputTouchParameters(Enum, UInt32):
    None_ = 0
    Contact = 1
    Orientation = 2
    Pressure = 4
class InjectedInputVisualizationMode(Enum, Int32):
    None_ = 0
    Default = 1
    Indirect = 2
class InputInjector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Preview.Injection.IInputInjector
    _classid_ = 'Windows.UI.Input.Preview.Injection.InputInjector'
    @winrt_mixinmethod
    def InjectKeyboardInput(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputKeyboardInfo]) -> Void: ...
    @winrt_mixinmethod
    def InjectMouseInput(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputMouseInfo]) -> Void: ...
    @winrt_mixinmethod
    def InitializeTouchInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, visualMode: win32more.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode) -> Void: ...
    @winrt_mixinmethod
    def InjectTouchInput(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, input: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Preview.Injection.InjectedInputTouchInfo]) -> Void: ...
    @winrt_mixinmethod
    def UninitializeTouchInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector) -> Void: ...
    @winrt_mixinmethod
    def InitializePenInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, visualMode: win32more.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode) -> Void: ...
    @winrt_mixinmethod
    def InjectPenInput(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, input: win32more.Windows.UI.Input.Preview.Injection.InjectedInputPenInfo) -> Void: ...
    @winrt_mixinmethod
    def UninitializePenInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector) -> Void: ...
    @winrt_mixinmethod
    def InjectShortcut(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector, shortcut: win32more.Windows.UI.Input.Preview.Injection.InjectedInputShortcut) -> Void: ...
    @winrt_mixinmethod
    def InitializeGamepadInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector2) -> Void: ...
    @winrt_mixinmethod
    def InjectGamepadInput(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector2, input: win32more.Windows.UI.Input.Preview.Injection.InjectedInputGamepadInfo) -> Void: ...
    @winrt_mixinmethod
    def UninitializeGamepadInjection(self: win32more.Windows.UI.Input.Preview.Injection.IInputInjector2) -> Void: ...
    @winrt_classmethod
    def TryCreateForAppBroadcastOnly(cls: win32more.Windows.UI.Input.Preview.Injection.IInputInjectorStatics2) -> win32more.Windows.UI.Input.Preview.Injection.InputInjector: ...
    @winrt_classmethod
    def TryCreate(cls: win32more.Windows.UI.Input.Preview.Injection.IInputInjectorStatics) -> win32more.Windows.UI.Input.Preview.Injection.InputInjector: ...


make_ready(__name__)
