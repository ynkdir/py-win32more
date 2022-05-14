from win32more import *
import win32more.UI.Input.XboxController
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.Input.XboxController, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.Input.XboxController, name)
XINPUT_DEVTYPE_GAMEPAD = 1
XINPUT_DEVSUBTYPE_GAMEPAD = 1
XINPUT_DEVSUBTYPE_UNKNOWN = 0
XINPUT_DEVSUBTYPE_WHEEL = 2
XINPUT_DEVSUBTYPE_ARCADE_STICK = 3
XINPUT_DEVSUBTYPE_FLIGHT_STICK = 4
XINPUT_DEVSUBTYPE_DANCE_PAD = 5
XINPUT_DEVSUBTYPE_GUITAR = 6
XINPUT_DEVSUBTYPE_GUITAR_ALTERNATE = 7
XINPUT_DEVSUBTYPE_DRUM_KIT = 8
XINPUT_DEVSUBTYPE_GUITAR_BASS = 11
XINPUT_DEVSUBTYPE_ARCADE_PAD = 19
XINPUT_CAPS_VOICE_SUPPORTED = 4
XINPUT_CAPS_FFB_SUPPORTED = 1
XINPUT_CAPS_WIRELESS = 2
XINPUT_CAPS_PMD_SUPPORTED = 8
XINPUT_CAPS_NO_NAVIGATION = 16
XINPUT_GAMEPAD_DPAD_UP = 1
XINPUT_GAMEPAD_DPAD_DOWN = 2
XINPUT_GAMEPAD_DPAD_LEFT = 4
XINPUT_GAMEPAD_DPAD_RIGHT = 8
XINPUT_GAMEPAD_START = 16
XINPUT_GAMEPAD_BACK = 32
XINPUT_GAMEPAD_LEFT_THUMB = 64
XINPUT_GAMEPAD_RIGHT_THUMB = 128
XINPUT_GAMEPAD_LEFT_SHOULDER = 256
XINPUT_GAMEPAD_RIGHT_SHOULDER = 512
XINPUT_GAMEPAD_A = 4096
XINPUT_GAMEPAD_B = 8192
XINPUT_GAMEPAD_X = 16384
XINPUT_GAMEPAD_Y = 32768
XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = 7849
XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE = 8689
XINPUT_GAMEPAD_TRIGGER_THRESHOLD = 30
XINPUT_FLAG_GAMEPAD = 1
BATTERY_DEVTYPE_GAMEPAD = 0
BATTERY_DEVTYPE_HEADSET = 1
BATTERY_TYPE_DISCONNECTED = 0
BATTERY_TYPE_WIRED = 1
BATTERY_TYPE_ALKALINE = 2
BATTERY_TYPE_NIMH = 3
BATTERY_TYPE_UNKNOWN = 255
BATTERY_LEVEL_EMPTY = 0
BATTERY_LEVEL_LOW = 1
BATTERY_LEVEL_MEDIUM = 2
BATTERY_LEVEL_FULL = 3
XUSER_MAX_COUNT = 4
XUSER_INDEX_ANY = 255
XINPUT_KEYSTROKE_KEYDOWN = 1
XINPUT_KEYSTROKE_KEYUP = 2
XINPUT_KEYSTROKE_REPEAT = 4
XINPUT_VIRTUAL_KEY = UInt16
VK_PAD_A = 22528
VK_PAD_B = 22529
VK_PAD_X = 22530
VK_PAD_Y = 22531
VK_PAD_RSHOULDER = 22532
VK_PAD_LSHOULDER = 22533
VK_PAD_LTRIGGER = 22534
VK_PAD_RTRIGGER = 22535
VK_PAD_DPAD_UP = 22544
VK_PAD_DPAD_DOWN = 22545
VK_PAD_DPAD_LEFT = 22546
VK_PAD_DPAD_RIGHT = 22547
VK_PAD_START = 22548
VK_PAD_BACK = 22549
VK_PAD_LTHUMB_PRESS = 22550
VK_PAD_RTHUMB_PRESS = 22551
VK_PAD_LTHUMB_UP = 22560
VK_PAD_LTHUMB_DOWN = 22561
VK_PAD_LTHUMB_RIGHT = 22562
VK_PAD_LTHUMB_LEFT = 22563
VK_PAD_LTHUMB_UPLEFT = 22564
VK_PAD_LTHUMB_UPRIGHT = 22565
VK_PAD_LTHUMB_DOWNRIGHT = 22566
VK_PAD_LTHUMB_DOWNLEFT = 22567
VK_PAD_RTHUMB_UP = 22576
VK_PAD_RTHUMB_DOWN = 22577
VK_PAD_RTHUMB_RIGHT = 22578
VK_PAD_RTHUMB_LEFT = 22579
VK_PAD_RTHUMB_UPLEFT = 22580
VK_PAD_RTHUMB_UPRIGHT = 22581
VK_PAD_RTHUMB_DOWNRIGHT = 22582
VK_PAD_RTHUMB_DOWNLEFT = 22583
def _define_XINPUT_GAMEPAD_head():
    class XINPUT_GAMEPAD(Structure):
        pass
    return XINPUT_GAMEPAD
def _define_XINPUT_GAMEPAD():
    XINPUT_GAMEPAD = win32more.UI.Input.XboxController.XINPUT_GAMEPAD_head
    XINPUT_GAMEPAD._fields_ = [
        ("wButtons", UInt16),
        ("bLeftTrigger", Byte),
        ("bRightTrigger", Byte),
        ("sThumbLX", Int16),
        ("sThumbLY", Int16),
        ("sThumbRX", Int16),
        ("sThumbRY", Int16),
    ]
    return XINPUT_GAMEPAD
def _define_XINPUT_STATE_head():
    class XINPUT_STATE(Structure):
        pass
    return XINPUT_STATE
def _define_XINPUT_STATE():
    XINPUT_STATE = win32more.UI.Input.XboxController.XINPUT_STATE_head
    XINPUT_STATE._fields_ = [
        ("dwPacketNumber", UInt32),
        ("Gamepad", win32more.UI.Input.XboxController.XINPUT_GAMEPAD),
    ]
    return XINPUT_STATE
def _define_XINPUT_VIBRATION_head():
    class XINPUT_VIBRATION(Structure):
        pass
    return XINPUT_VIBRATION
def _define_XINPUT_VIBRATION():
    XINPUT_VIBRATION = win32more.UI.Input.XboxController.XINPUT_VIBRATION_head
    XINPUT_VIBRATION._fields_ = [
        ("wLeftMotorSpeed", UInt16),
        ("wRightMotorSpeed", UInt16),
    ]
    return XINPUT_VIBRATION
def _define_XINPUT_CAPABILITIES_head():
    class XINPUT_CAPABILITIES(Structure):
        pass
    return XINPUT_CAPABILITIES
def _define_XINPUT_CAPABILITIES():
    XINPUT_CAPABILITIES = win32more.UI.Input.XboxController.XINPUT_CAPABILITIES_head
    XINPUT_CAPABILITIES._fields_ = [
        ("Type", Byte),
        ("SubType", Byte),
        ("Flags", UInt16),
        ("Gamepad", win32more.UI.Input.XboxController.XINPUT_GAMEPAD),
        ("Vibration", win32more.UI.Input.XboxController.XINPUT_VIBRATION),
    ]
    return XINPUT_CAPABILITIES
def _define_XINPUT_BATTERY_INFORMATION_head():
    class XINPUT_BATTERY_INFORMATION(Structure):
        pass
    return XINPUT_BATTERY_INFORMATION
def _define_XINPUT_BATTERY_INFORMATION():
    XINPUT_BATTERY_INFORMATION = win32more.UI.Input.XboxController.XINPUT_BATTERY_INFORMATION_head
    XINPUT_BATTERY_INFORMATION._fields_ = [
        ("BatteryType", Byte),
        ("BatteryLevel", Byte),
    ]
    return XINPUT_BATTERY_INFORMATION
def _define_XINPUT_KEYSTROKE_head():
    class XINPUT_KEYSTROKE(Structure):
        pass
    return XINPUT_KEYSTROKE
def _define_XINPUT_KEYSTROKE():
    XINPUT_KEYSTROKE = win32more.UI.Input.XboxController.XINPUT_KEYSTROKE_head
    XINPUT_KEYSTROKE._fields_ = [
        ("VirtualKey", win32more.UI.Input.XboxController.XINPUT_VIRTUAL_KEY),
        ("Unicode", Char),
        ("Flags", UInt16),
        ("UserIndex", Byte),
        ("HidCode", Byte),
    ]
    return XINPUT_KEYSTROKE
def _define_XInputGetState():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.UI.Input.XboxController.XINPUT_STATE_head), use_last_error=False)(("XInputGetState", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'pState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputSetState():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.UI.Input.XboxController.XINPUT_VIBRATION_head), use_last_error=False)(("XInputSetState", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'pVibration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputGetCapabilities():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,POINTER(win32more.UI.Input.XboxController.XINPUT_CAPABILITIES_head), use_last_error=False)(("XInputGetCapabilities", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'dwFlags'),(1, 'pCapabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputEnable():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(("XInputEnable", windll["XINPUTUAP"]), ((1, 'enable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputGetAudioDeviceIds():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)(("XInputGetAudioDeviceIds", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'pRenderDeviceId'),(1, 'pRenderCount'),(1, 'pCaptureDeviceId'),(1, 'pCaptureCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputGetBatteryInformation():
    try:
        return WINFUNCTYPE(UInt32,UInt32,Byte,POINTER(win32more.UI.Input.XboxController.XINPUT_BATTERY_INFORMATION_head), use_last_error=False)(("XInputGetBatteryInformation", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'devType'),(1, 'pBatteryInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XInputGetKeystroke():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,POINTER(win32more.UI.Input.XboxController.XINPUT_KEYSTROKE_head), use_last_error=False)(("XInputGetKeystroke", windll["XINPUTUAP"]), ((1, 'dwUserIndex'),(1, 'dwReserved'),(1, 'pKeystroke'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "XINPUT_DEVTYPE_GAMEPAD",
    "XINPUT_DEVSUBTYPE_GAMEPAD",
    "XINPUT_DEVSUBTYPE_UNKNOWN",
    "XINPUT_DEVSUBTYPE_WHEEL",
    "XINPUT_DEVSUBTYPE_ARCADE_STICK",
    "XINPUT_DEVSUBTYPE_FLIGHT_STICK",
    "XINPUT_DEVSUBTYPE_DANCE_PAD",
    "XINPUT_DEVSUBTYPE_GUITAR",
    "XINPUT_DEVSUBTYPE_GUITAR_ALTERNATE",
    "XINPUT_DEVSUBTYPE_DRUM_KIT",
    "XINPUT_DEVSUBTYPE_GUITAR_BASS",
    "XINPUT_DEVSUBTYPE_ARCADE_PAD",
    "XINPUT_CAPS_VOICE_SUPPORTED",
    "XINPUT_CAPS_FFB_SUPPORTED",
    "XINPUT_CAPS_WIRELESS",
    "XINPUT_CAPS_PMD_SUPPORTED",
    "XINPUT_CAPS_NO_NAVIGATION",
    "XINPUT_GAMEPAD_DPAD_UP",
    "XINPUT_GAMEPAD_DPAD_DOWN",
    "XINPUT_GAMEPAD_DPAD_LEFT",
    "XINPUT_GAMEPAD_DPAD_RIGHT",
    "XINPUT_GAMEPAD_START",
    "XINPUT_GAMEPAD_BACK",
    "XINPUT_GAMEPAD_LEFT_THUMB",
    "XINPUT_GAMEPAD_RIGHT_THUMB",
    "XINPUT_GAMEPAD_LEFT_SHOULDER",
    "XINPUT_GAMEPAD_RIGHT_SHOULDER",
    "XINPUT_GAMEPAD_A",
    "XINPUT_GAMEPAD_B",
    "XINPUT_GAMEPAD_X",
    "XINPUT_GAMEPAD_Y",
    "XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE",
    "XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE",
    "XINPUT_GAMEPAD_TRIGGER_THRESHOLD",
    "XINPUT_FLAG_GAMEPAD",
    "BATTERY_DEVTYPE_GAMEPAD",
    "BATTERY_DEVTYPE_HEADSET",
    "BATTERY_TYPE_DISCONNECTED",
    "BATTERY_TYPE_WIRED",
    "BATTERY_TYPE_ALKALINE",
    "BATTERY_TYPE_NIMH",
    "BATTERY_TYPE_UNKNOWN",
    "BATTERY_LEVEL_EMPTY",
    "BATTERY_LEVEL_LOW",
    "BATTERY_LEVEL_MEDIUM",
    "BATTERY_LEVEL_FULL",
    "XUSER_MAX_COUNT",
    "XUSER_INDEX_ANY",
    "XINPUT_KEYSTROKE_KEYDOWN",
    "XINPUT_KEYSTROKE_KEYUP",
    "XINPUT_KEYSTROKE_REPEAT",
    "XINPUT_VIRTUAL_KEY",
    "VK_PAD_A",
    "VK_PAD_B",
    "VK_PAD_X",
    "VK_PAD_Y",
    "VK_PAD_RSHOULDER",
    "VK_PAD_LSHOULDER",
    "VK_PAD_LTRIGGER",
    "VK_PAD_RTRIGGER",
    "VK_PAD_DPAD_UP",
    "VK_PAD_DPAD_DOWN",
    "VK_PAD_DPAD_LEFT",
    "VK_PAD_DPAD_RIGHT",
    "VK_PAD_START",
    "VK_PAD_BACK",
    "VK_PAD_LTHUMB_PRESS",
    "VK_PAD_RTHUMB_PRESS",
    "VK_PAD_LTHUMB_UP",
    "VK_PAD_LTHUMB_DOWN",
    "VK_PAD_LTHUMB_RIGHT",
    "VK_PAD_LTHUMB_LEFT",
    "VK_PAD_LTHUMB_UPLEFT",
    "VK_PAD_LTHUMB_UPRIGHT",
    "VK_PAD_LTHUMB_DOWNRIGHT",
    "VK_PAD_LTHUMB_DOWNLEFT",
    "VK_PAD_RTHUMB_UP",
    "VK_PAD_RTHUMB_DOWN",
    "VK_PAD_RTHUMB_RIGHT",
    "VK_PAD_RTHUMB_LEFT",
    "VK_PAD_RTHUMB_UPLEFT",
    "VK_PAD_RTHUMB_UPRIGHT",
    "VK_PAD_RTHUMB_DOWNRIGHT",
    "VK_PAD_RTHUMB_DOWNLEFT",
    "XINPUT_GAMEPAD",
    "XINPUT_STATE",
    "XINPUT_VIBRATION",
    "XINPUT_CAPABILITIES",
    "XINPUT_BATTERY_INFORMATION",
    "XINPUT_KEYSTROKE",
    "XInputGetState",
    "XInputSetState",
    "XInputGetCapabilities",
    "XInputEnable",
    "XInputGetAudioDeviceIds",
    "XInputGetBatteryInformation",
    "XInputGetKeystroke",
]
