from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.UI.Input.XboxController
XINPUT_DLL_A: String = 'xinput1_4.dll'
XINPUT_DLL_W: String = 'xinput1_4.dll'
XINPUT_DLL: String = 'xinput1_4.dll'
XUSER_MAX_COUNT: UInt32 = 4
XUSER_INDEX_ANY: UInt32 = 255
@winfunctype('xinput1_4.dll')
def XInputGetState(dwUserIndex: UInt32, pState: POINTER(win32more.Windows.Win32.UI.Input.XboxController.XINPUT_STATE)) -> UInt32: ...
@winfunctype('xinput1_4.dll')
def XInputSetState(dwUserIndex: UInt32, pVibration: POINTER(win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIBRATION)) -> UInt32: ...
@winfunctype('xinput1_4.dll')
def XInputGetCapabilities(dwUserIndex: UInt32, dwFlags: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_FLAG, pCapabilities: POINTER(win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES)) -> UInt32: ...
@winfunctype('xinput1_4.dll')
def XInputEnable(enable: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('xinput1_4.dll')
def XInputGetAudioDeviceIds(dwUserIndex: UInt32, pRenderDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pRenderCount: POINTER(UInt32), pCaptureDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pCaptureCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('xinput1_4.dll')
def XInputGetBatteryInformation(dwUserIndex: UInt32, devType: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_DEVTYPE, pBatteryInformation: POINTER(win32more.Windows.Win32.UI.Input.XboxController.XINPUT_BATTERY_INFORMATION)) -> UInt32: ...
@winfunctype('xinput1_4.dll')
def XInputGetKeystroke(dwUserIndex: UInt32, dwReserved: UInt32, pKeystroke: POINTER(win32more.Windows.Win32.UI.Input.XboxController.XINPUT_KEYSTROKE)) -> UInt32: ...
BATTERY_DEVTYPE = Byte
BATTERY_DEVTYPE_GAMEPAD: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_DEVTYPE = 0
BATTERY_DEVTYPE_HEADSET: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_DEVTYPE = 1
BATTERY_LEVEL = Byte
BATTERY_LEVEL_EMPTY: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_LEVEL = 0
BATTERY_LEVEL_LOW: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_LEVEL = 1
BATTERY_LEVEL_MEDIUM: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_LEVEL = 2
BATTERY_LEVEL_FULL: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_LEVEL = 3
BATTERY_TYPE = Byte
BATTERY_TYPE_DISCONNECTED: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE = 0
BATTERY_TYPE_WIRED: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE = 1
BATTERY_TYPE_ALKALINE: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE = 2
BATTERY_TYPE_NIMH: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE = 3
BATTERY_TYPE_UNKNOWN: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE = 255
class XINPUT_BATTERY_INFORMATION(Structure):
    BatteryType: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_TYPE
    BatteryLevel: win32more.Windows.Win32.UI.Input.XboxController.BATTERY_LEVEL
class XINPUT_CAPABILITIES(Structure):
    Type: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVTYPE
    SubType: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE
    Flags: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS
    Gamepad: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD
    Vibration: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIBRATION
XINPUT_CAPABILITIES_FLAGS = UInt16
XINPUT_CAPS_VOICE_SUPPORTED: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS = 4
XINPUT_CAPS_FFB_SUPPORTED: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS = 1
XINPUT_CAPS_WIRELESS: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS = 2
XINPUT_CAPS_PMD_SUPPORTED: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS = 8
XINPUT_CAPS_NO_NAVIGATION: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_CAPABILITIES_FLAGS = 16
XINPUT_DEVSUBTYPE = Byte
XINPUT_DEVSUBTYPE_GAMEPAD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 1
XINPUT_DEVSUBTYPE_UNKNOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 0
XINPUT_DEVSUBTYPE_WHEEL: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 2
XINPUT_DEVSUBTYPE_ARCADE_STICK: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 3
XINPUT_DEVSUBTYPE_FLIGHT_STICK: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 4
XINPUT_DEVSUBTYPE_DANCE_PAD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 5
XINPUT_DEVSUBTYPE_GUITAR: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 6
XINPUT_DEVSUBTYPE_GUITAR_ALTERNATE: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 7
XINPUT_DEVSUBTYPE_DRUM_KIT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 8
XINPUT_DEVSUBTYPE_GUITAR_BASS: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 11
XINPUT_DEVSUBTYPE_ARCADE_PAD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVSUBTYPE = 19
XINPUT_DEVTYPE = Byte
XINPUT_DEVTYPE_GAMEPAD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_DEVTYPE = 1
XINPUT_FLAG = UInt32
XINPUT_FLAG_ALL: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_FLAG = 0
XINPUT_FLAG_GAMEPAD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_FLAG = 1
class XINPUT_GAMEPAD(Structure):
    wButtons: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS
    bLeftTrigger: Byte
    bRightTrigger: Byte
    sThumbLX: Int16
    sThumbLY: Int16
    sThumbRX: Int16
    sThumbRY: Int16
XINPUT_GAMEPAD_BUTTON_FLAGS = UInt16
XINPUT_GAMEPAD_DPAD_UP: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 1
XINPUT_GAMEPAD_DPAD_DOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 2
XINPUT_GAMEPAD_DPAD_LEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 4
XINPUT_GAMEPAD_DPAD_RIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 8
XINPUT_GAMEPAD_START: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 16
XINPUT_GAMEPAD_BACK: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 32
XINPUT_GAMEPAD_LEFT_THUMB: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 64
XINPUT_GAMEPAD_RIGHT_THUMB: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 128
XINPUT_GAMEPAD_LEFT_SHOULDER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 256
XINPUT_GAMEPAD_RIGHT_SHOULDER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 512
XINPUT_GAMEPAD_A: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 4096
XINPUT_GAMEPAD_B: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 8192
XINPUT_GAMEPAD_X: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 16384
XINPUT_GAMEPAD_Y: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 32768
XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 7849
XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 8689
XINPUT_GAMEPAD_TRIGGER_THRESHOLD: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD_BUTTON_FLAGS = 30
class XINPUT_KEYSTROKE(Structure):
    VirtualKey: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY
    Unicode: Char
    Flags: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_KEYSTROKE_FLAGS
    UserIndex: Byte
    HidCode: Byte
XINPUT_KEYSTROKE_FLAGS = UInt16
XINPUT_KEYSTROKE_KEYDOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_KEYSTROKE_FLAGS = 1
XINPUT_KEYSTROKE_KEYUP: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_KEYSTROKE_FLAGS = 2
XINPUT_KEYSTROKE_REPEAT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_KEYSTROKE_FLAGS = 4
class XINPUT_STATE(Structure):
    dwPacketNumber: UInt32
    Gamepad: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_GAMEPAD
class XINPUT_VIBRATION(Structure):
    wLeftMotorSpeed: UInt16
    wRightMotorSpeed: UInt16
XINPUT_VIRTUAL_KEY = UInt16
VK_PAD_A: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22528
VK_PAD_B: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22529
VK_PAD_X: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22530
VK_PAD_Y: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22531
VK_PAD_RSHOULDER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22532
VK_PAD_LSHOULDER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22533
VK_PAD_LTRIGGER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22534
VK_PAD_RTRIGGER: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22535
VK_PAD_DPAD_UP: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22544
VK_PAD_DPAD_DOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22545
VK_PAD_DPAD_LEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22546
VK_PAD_DPAD_RIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22547
VK_PAD_START: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22548
VK_PAD_BACK: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22549
VK_PAD_LTHUMB_PRESS: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22550
VK_PAD_RTHUMB_PRESS: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22551
VK_PAD_LTHUMB_UP: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22560
VK_PAD_LTHUMB_DOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22561
VK_PAD_LTHUMB_RIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22562
VK_PAD_LTHUMB_LEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22563
VK_PAD_LTHUMB_UPLEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22564
VK_PAD_LTHUMB_UPRIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22565
VK_PAD_LTHUMB_DOWNRIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22566
VK_PAD_LTHUMB_DOWNLEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22567
VK_PAD_RTHUMB_UP: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22576
VK_PAD_RTHUMB_DOWN: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22577
VK_PAD_RTHUMB_RIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22578
VK_PAD_RTHUMB_LEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22579
VK_PAD_RTHUMB_UPLEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22580
VK_PAD_RTHUMB_UPRIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22581
VK_PAD_RTHUMB_DOWNRIGHT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22582
VK_PAD_RTHUMB_DOWNLEFT: win32more.Windows.Win32.UI.Input.XboxController.XINPUT_VIRTUAL_KEY = 22583


make_ready(__name__)
