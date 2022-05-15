from win32more import *
import win32more.UI.Input
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.UI.Input, name, globals()[f"_define_{name}"]())
    return getattr(win32more.UI.Input, name)
def __dir__():
    return __all__
RAW_INPUT_DATA_COMMAND_FLAGS = UInt32
RID_HEADER = 268435461
RID_INPUT = 268435459
RAW_INPUT_DEVICE_INFO_COMMAND = UInt32
RIDI_PREPARSEDDATA = 536870917
RIDI_DEVICENAME = 536870919
RIDI_DEVICEINFO = 536870923
RID_DEVICE_INFO_TYPE = UInt32
RIM_TYPEMOUSE = 0
RIM_TYPEKEYBOARD = 1
RIM_TYPEHID = 2
RAWINPUTDEVICE_FLAGS = UInt32
RIDEV_REMOVE = 1
RIDEV_EXCLUDE = 16
RIDEV_PAGEONLY = 32
RIDEV_NOLEGACY = 48
RIDEV_INPUTSINK = 256
RIDEV_CAPTUREMOUSE = 512
RIDEV_NOHOTKEYS = 512
RIDEV_APPKEYS = 1024
RIDEV_EXINPUTSINK = 4096
RIDEV_DEVNOTIFY = 8192
HRAWINPUT = IntPtr
def _define_RAWINPUTHEADER_head():
    class RAWINPUTHEADER(Structure):
        pass
    return RAWINPUTHEADER
def _define_RAWINPUTHEADER():
    RAWINPUTHEADER = win32more.UI.Input.RAWINPUTHEADER_head
    RAWINPUTHEADER._fields_ = [
        ("dwType", UInt32),
        ("dwSize", UInt32),
        ("hDevice", win32more.Foundation.HANDLE),
        ("wParam", win32more.Foundation.WPARAM),
    ]
    return RAWINPUTHEADER
def _define_RAWMOUSE_head():
    class RAWMOUSE(Structure):
        pass
    return RAWMOUSE
def _define_RAWMOUSE():
    RAWMOUSE = win32more.UI.Input.RAWMOUSE_head
    class RAWMOUSE__Anonymous_e__Union(Union):
        pass
    class RAWMOUSE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    RAWMOUSE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("usButtonFlags", UInt16),
        ("usButtonData", UInt16),
    ]
    RAWMOUSE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    RAWMOUSE__Anonymous_e__Union._fields_ = [
        ("ulButtons", UInt32),
        ("Anonymous", RAWMOUSE__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    RAWMOUSE._anonymous_ = [
        'Anonymous',
    ]
    RAWMOUSE._fields_ = [
        ("usFlags", UInt16),
        ("Anonymous", RAWMOUSE__Anonymous_e__Union),
        ("ulRawButtons", UInt32),
        ("lLastX", Int32),
        ("lLastY", Int32),
        ("ulExtraInformation", UInt32),
    ]
    return RAWMOUSE
def _define_RAWKEYBOARD_head():
    class RAWKEYBOARD(Structure):
        pass
    return RAWKEYBOARD
def _define_RAWKEYBOARD():
    RAWKEYBOARD = win32more.UI.Input.RAWKEYBOARD_head
    RAWKEYBOARD._fields_ = [
        ("MakeCode", UInt16),
        ("Flags", UInt16),
        ("Reserved", UInt16),
        ("VKey", UInt16),
        ("Message", UInt32),
        ("ExtraInformation", UInt32),
    ]
    return RAWKEYBOARD
def _define_RAWHID_head():
    class RAWHID(Structure):
        pass
    return RAWHID
def _define_RAWHID():
    RAWHID = win32more.UI.Input.RAWHID_head
    RAWHID._fields_ = [
        ("dwSizeHid", UInt32),
        ("dwCount", UInt32),
        ("bRawData", Byte * 0),
    ]
    return RAWHID
def _define_RAWINPUT_head():
    class RAWINPUT(Structure):
        pass
    return RAWINPUT
def _define_RAWINPUT():
    RAWINPUT = win32more.UI.Input.RAWINPUT_head
    class RAWINPUT__data_e__Union(Union):
        pass
    RAWINPUT__data_e__Union._fields_ = [
        ("mouse", win32more.UI.Input.RAWMOUSE),
        ("keyboard", win32more.UI.Input.RAWKEYBOARD),
        ("hid", win32more.UI.Input.RAWHID),
    ]
    RAWINPUT._fields_ = [
        ("header", win32more.UI.Input.RAWINPUTHEADER),
        ("data", RAWINPUT__data_e__Union),
    ]
    return RAWINPUT
def _define_RID_DEVICE_INFO_MOUSE_head():
    class RID_DEVICE_INFO_MOUSE(Structure):
        pass
    return RID_DEVICE_INFO_MOUSE
def _define_RID_DEVICE_INFO_MOUSE():
    RID_DEVICE_INFO_MOUSE = win32more.UI.Input.RID_DEVICE_INFO_MOUSE_head
    RID_DEVICE_INFO_MOUSE._fields_ = [
        ("dwId", UInt32),
        ("dwNumberOfButtons", UInt32),
        ("dwSampleRate", UInt32),
        ("fHasHorizontalWheel", win32more.Foundation.BOOL),
    ]
    return RID_DEVICE_INFO_MOUSE
def _define_RID_DEVICE_INFO_KEYBOARD_head():
    class RID_DEVICE_INFO_KEYBOARD(Structure):
        pass
    return RID_DEVICE_INFO_KEYBOARD
def _define_RID_DEVICE_INFO_KEYBOARD():
    RID_DEVICE_INFO_KEYBOARD = win32more.UI.Input.RID_DEVICE_INFO_KEYBOARD_head
    RID_DEVICE_INFO_KEYBOARD._fields_ = [
        ("dwType", UInt32),
        ("dwSubType", UInt32),
        ("dwKeyboardMode", UInt32),
        ("dwNumberOfFunctionKeys", UInt32),
        ("dwNumberOfIndicators", UInt32),
        ("dwNumberOfKeysTotal", UInt32),
    ]
    return RID_DEVICE_INFO_KEYBOARD
def _define_RID_DEVICE_INFO_HID_head():
    class RID_DEVICE_INFO_HID(Structure):
        pass
    return RID_DEVICE_INFO_HID
def _define_RID_DEVICE_INFO_HID():
    RID_DEVICE_INFO_HID = win32more.UI.Input.RID_DEVICE_INFO_HID_head
    RID_DEVICE_INFO_HID._fields_ = [
        ("dwVendorId", UInt32),
        ("dwProductId", UInt32),
        ("dwVersionNumber", UInt32),
        ("usUsagePage", UInt16),
        ("usUsage", UInt16),
    ]
    return RID_DEVICE_INFO_HID
def _define_RID_DEVICE_INFO_head():
    class RID_DEVICE_INFO(Structure):
        pass
    return RID_DEVICE_INFO
def _define_RID_DEVICE_INFO():
    RID_DEVICE_INFO = win32more.UI.Input.RID_DEVICE_INFO_head
    class RID_DEVICE_INFO__Anonymous_e__Union(Union):
        pass
    RID_DEVICE_INFO__Anonymous_e__Union._fields_ = [
        ("mouse", win32more.UI.Input.RID_DEVICE_INFO_MOUSE),
        ("keyboard", win32more.UI.Input.RID_DEVICE_INFO_KEYBOARD),
        ("hid", win32more.UI.Input.RID_DEVICE_INFO_HID),
    ]
    RID_DEVICE_INFO._anonymous_ = [
        'Anonymous',
    ]
    RID_DEVICE_INFO._fields_ = [
        ("cbSize", UInt32),
        ("dwType", win32more.UI.Input.RID_DEVICE_INFO_TYPE),
        ("Anonymous", RID_DEVICE_INFO__Anonymous_e__Union),
    ]
    return RID_DEVICE_INFO
def _define_RAWINPUTDEVICE_head():
    class RAWINPUTDEVICE(Structure):
        pass
    return RAWINPUTDEVICE
def _define_RAWINPUTDEVICE():
    RAWINPUTDEVICE = win32more.UI.Input.RAWINPUTDEVICE_head
    RAWINPUTDEVICE._fields_ = [
        ("usUsagePage", UInt16),
        ("usUsage", UInt16),
        ("dwFlags", win32more.UI.Input.RAWINPUTDEVICE_FLAGS),
        ("hwndTarget", win32more.Foundation.HWND),
    ]
    return RAWINPUTDEVICE
def _define_RAWINPUTDEVICELIST_head():
    class RAWINPUTDEVICELIST(Structure):
        pass
    return RAWINPUTDEVICELIST
def _define_RAWINPUTDEVICELIST():
    RAWINPUTDEVICELIST = win32more.UI.Input.RAWINPUTDEVICELIST_head
    RAWINPUTDEVICELIST._fields_ = [
        ("hDevice", win32more.Foundation.HANDLE),
        ("dwType", win32more.UI.Input.RID_DEVICE_INFO_TYPE),
    ]
    return RAWINPUTDEVICELIST
INPUT_MESSAGE_DEVICE_TYPE = Int32
IMDT_UNAVAILABLE = 0
IMDT_KEYBOARD = 1
IMDT_MOUSE = 2
IMDT_TOUCH = 4
IMDT_PEN = 8
IMDT_TOUCHPAD = 16
INPUT_MESSAGE_ORIGIN_ID = Int32
IMO_UNAVAILABLE = 0
IMO_HARDWARE = 1
IMO_INJECTED = 2
IMO_SYSTEM = 4
def _define_INPUT_MESSAGE_SOURCE_head():
    class INPUT_MESSAGE_SOURCE(Structure):
        pass
    return INPUT_MESSAGE_SOURCE
def _define_INPUT_MESSAGE_SOURCE():
    INPUT_MESSAGE_SOURCE = win32more.UI.Input.INPUT_MESSAGE_SOURCE_head
    INPUT_MESSAGE_SOURCE._fields_ = [
        ("deviceType", win32more.UI.Input.INPUT_MESSAGE_DEVICE_TYPE),
        ("originId", win32more.UI.Input.INPUT_MESSAGE_ORIGIN_ID),
    ]
    return INPUT_MESSAGE_SOURCE
def _define_GetRawInputData():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.Input.HRAWINPUT,win32more.UI.Input.RAW_INPUT_DATA_COMMAND_FLAGS,c_void_p,POINTER(UInt32),UInt32, use_last_error=False)(("GetRawInputData", windll["USER32"]), ((1, 'hRawInput'),(1, 'uiCommand'),(1, 'pData'),(1, 'pcbSize'),(1, 'cbSizeHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRawInputDeviceInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND,c_void_p,POINTER(UInt32), use_last_error=True)(("GetRawInputDeviceInfoA", windll["USER32"]), ((1, 'hDevice'),(1, 'uiCommand'),(1, 'pData'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRawInputDeviceInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND,c_void_p,POINTER(UInt32), use_last_error=True)(("GetRawInputDeviceInfoW", windll["USER32"]), ((1, 'hDevice'),(1, 'uiCommand'),(1, 'pData'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRawInputDeviceInfo():
    return win32more.UI.Input.GetRawInputDeviceInfoW
def _define_GetRawInputBuffer():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.UI.Input.RAWINPUT_head),POINTER(UInt32),UInt32, use_last_error=True)(("GetRawInputBuffer", windll["USER32"]), ((1, 'pData'),(1, 'pcbSize'),(1, 'cbSizeHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterRawInputDevices():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.RAWINPUTDEVICE),UInt32,UInt32, use_last_error=True)(("RegisterRawInputDevices", windll["USER32"]), ((1, 'pRawInputDevices'),(1, 'uiNumDevices'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRegisteredRawInputDevices():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.UI.Input.RAWINPUTDEVICE),POINTER(UInt32),UInt32, use_last_error=True)(("GetRegisteredRawInputDevices", windll["USER32"]), ((1, 'pRawInputDevices'),(1, 'puiNumDevices'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRawInputDeviceList():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.UI.Input.RAWINPUTDEVICELIST),POINTER(UInt32),UInt32, use_last_error=True)(("GetRawInputDeviceList", windll["USER32"]), ((1, 'pRawInputDeviceList'),(1, 'puiNumDevices'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DefRawInputProc():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,POINTER(POINTER(win32more.UI.Input.RAWINPUT_head)),Int32,UInt32, use_last_error=False)(("DefRawInputProc", windll["USER32"]), ((1, 'paRawInput'),(1, 'nInput'),(1, 'cbSizeHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentInputMessageSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.INPUT_MESSAGE_SOURCE_head), use_last_error=True)(("GetCurrentInputMessageSource", windll["USER32"]), ((1, 'inputMessageSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCIMSSM():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.INPUT_MESSAGE_SOURCE_head), use_last_error=False)(("GetCIMSSM", windll["USER32"]), ((1, 'inputMessageSource'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "RAW_INPUT_DATA_COMMAND_FLAGS",
    "RID_HEADER",
    "RID_INPUT",
    "RAW_INPUT_DEVICE_INFO_COMMAND",
    "RIDI_PREPARSEDDATA",
    "RIDI_DEVICENAME",
    "RIDI_DEVICEINFO",
    "RID_DEVICE_INFO_TYPE",
    "RIM_TYPEMOUSE",
    "RIM_TYPEKEYBOARD",
    "RIM_TYPEHID",
    "RAWINPUTDEVICE_FLAGS",
    "RIDEV_REMOVE",
    "RIDEV_EXCLUDE",
    "RIDEV_PAGEONLY",
    "RIDEV_NOLEGACY",
    "RIDEV_INPUTSINK",
    "RIDEV_CAPTUREMOUSE",
    "RIDEV_NOHOTKEYS",
    "RIDEV_APPKEYS",
    "RIDEV_EXINPUTSINK",
    "RIDEV_DEVNOTIFY",
    "HRAWINPUT",
    "RAWINPUTHEADER",
    "RAWMOUSE",
    "RAWKEYBOARD",
    "RAWHID",
    "RAWINPUT",
    "RID_DEVICE_INFO_MOUSE",
    "RID_DEVICE_INFO_KEYBOARD",
    "RID_DEVICE_INFO_HID",
    "RID_DEVICE_INFO",
    "RAWINPUTDEVICE",
    "RAWINPUTDEVICELIST",
    "INPUT_MESSAGE_DEVICE_TYPE",
    "IMDT_UNAVAILABLE",
    "IMDT_KEYBOARD",
    "IMDT_MOUSE",
    "IMDT_TOUCH",
    "IMDT_PEN",
    "IMDT_TOUCHPAD",
    "INPUT_MESSAGE_ORIGIN_ID",
    "IMO_UNAVAILABLE",
    "IMO_HARDWARE",
    "IMO_INJECTED",
    "IMO_SYSTEM",
    "INPUT_MESSAGE_SOURCE",
    "GetRawInputData",
    "GetRawInputDeviceInfoA",
    "GetRawInputDeviceInfoW",
    "GetRawInputDeviceInfo",
    "GetRawInputBuffer",
    "RegisterRawInputDevices",
    "GetRegisteredRawInputDevices",
    "GetRawInputDeviceList",
    "DefRawInputProc",
    "GetCurrentInputMessageSource",
    "GetCIMSSM",
]
