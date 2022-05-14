from win32more import *
import win32more.UI.Input.Pointer
import win32more.Foundation
import win32more.UI.Controls
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.Input.Pointer, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.Input.Pointer, name)
POINTER_FLAGS = UInt32
POINTER_FLAG_NONE = 0
POINTER_FLAG_NEW = 1
POINTER_FLAG_INRANGE = 2
POINTER_FLAG_INCONTACT = 4
POINTER_FLAG_FIRSTBUTTON = 16
POINTER_FLAG_SECONDBUTTON = 32
POINTER_FLAG_THIRDBUTTON = 64
POINTER_FLAG_FOURTHBUTTON = 128
POINTER_FLAG_FIFTHBUTTON = 256
POINTER_FLAG_PRIMARY = 8192
POINTER_FLAG_CONFIDENCE = 16384
POINTER_FLAG_CANCELED = 32768
POINTER_FLAG_DOWN = 65536
POINTER_FLAG_UPDATE = 131072
POINTER_FLAG_UP = 262144
POINTER_FLAG_WHEEL = 524288
POINTER_FLAG_HWHEEL = 1048576
POINTER_FLAG_CAPTURECHANGED = 2097152
POINTER_FLAG_HASTRANSFORM = 4194304
TOUCH_FEEDBACK_MODE = UInt32
TOUCH_FEEDBACK_DEFAULT = 1
TOUCH_FEEDBACK_INDIRECT = 2
TOUCH_FEEDBACK_NONE = 3
POINTER_BUTTON_CHANGE_TYPE = Int32
POINTER_CHANGE_NONE = 0
POINTER_CHANGE_FIRSTBUTTON_DOWN = 1
POINTER_CHANGE_FIRSTBUTTON_UP = 2
POINTER_CHANGE_SECONDBUTTON_DOWN = 3
POINTER_CHANGE_SECONDBUTTON_UP = 4
POINTER_CHANGE_THIRDBUTTON_DOWN = 5
POINTER_CHANGE_THIRDBUTTON_UP = 6
POINTER_CHANGE_FOURTHBUTTON_DOWN = 7
POINTER_CHANGE_FOURTHBUTTON_UP = 8
POINTER_CHANGE_FIFTHBUTTON_DOWN = 9
POINTER_CHANGE_FIFTHBUTTON_UP = 10
def _define_POINTER_INFO_head():
    class POINTER_INFO(Structure):
        pass
    return POINTER_INFO
def _define_POINTER_INFO():
    POINTER_INFO = win32more.UI.Input.Pointer.POINTER_INFO_head
    POINTER_INFO._fields_ = [
        ("pointerType", win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE),
        ("pointerId", UInt32),
        ("frameId", UInt32),
        ("pointerFlags", win32more.UI.Input.Pointer.POINTER_FLAGS),
        ("sourceDevice", win32more.Foundation.HANDLE),
        ("hwndTarget", win32more.Foundation.HWND),
        ("ptPixelLocation", win32more.Foundation.POINT),
        ("ptHimetricLocation", win32more.Foundation.POINT),
        ("ptPixelLocationRaw", win32more.Foundation.POINT),
        ("ptHimetricLocationRaw", win32more.Foundation.POINT),
        ("dwTime", UInt32),
        ("historyCount", UInt32),
        ("InputData", Int32),
        ("dwKeyStates", UInt32),
        ("PerformanceCount", UInt64),
        ("ButtonChangeType", win32more.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE),
    ]
    return POINTER_INFO
def _define_POINTER_TOUCH_INFO_head():
    class POINTER_TOUCH_INFO(Structure):
        pass
    return POINTER_TOUCH_INFO
def _define_POINTER_TOUCH_INFO():
    POINTER_TOUCH_INFO = win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head
    POINTER_TOUCH_INFO._fields_ = [
        ("pointerInfo", win32more.UI.Input.Pointer.POINTER_INFO),
        ("touchFlags", UInt32),
        ("touchMask", UInt32),
        ("rcContact", win32more.Foundation.RECT),
        ("rcContactRaw", win32more.Foundation.RECT),
        ("orientation", UInt32),
        ("pressure", UInt32),
    ]
    return POINTER_TOUCH_INFO
def _define_POINTER_PEN_INFO_head():
    class POINTER_PEN_INFO(Structure):
        pass
    return POINTER_PEN_INFO
def _define_POINTER_PEN_INFO():
    POINTER_PEN_INFO = win32more.UI.Input.Pointer.POINTER_PEN_INFO_head
    POINTER_PEN_INFO._fields_ = [
        ("pointerInfo", win32more.UI.Input.Pointer.POINTER_INFO),
        ("penFlags", UInt32),
        ("penMask", UInt32),
        ("pressure", UInt32),
        ("rotation", UInt32),
        ("tiltX", Int32),
        ("tiltY", Int32),
    ]
    return POINTER_PEN_INFO
def _define_INPUT_INJECTION_VALUE_head():
    class INPUT_INJECTION_VALUE(Structure):
        pass
    return INPUT_INJECTION_VALUE
def _define_INPUT_INJECTION_VALUE():
    INPUT_INJECTION_VALUE = win32more.UI.Input.Pointer.INPUT_INJECTION_VALUE_head
    INPUT_INJECTION_VALUE._fields_ = [
        ("page", UInt16),
        ("usage", UInt16),
        ("value", Int32),
        ("index", UInt16),
    ]
    return INPUT_INJECTION_VALUE
def _define_INPUT_TRANSFORM_head():
    class INPUT_TRANSFORM(Structure):
        pass
    return INPUT_TRANSFORM
def _define_INPUT_TRANSFORM():
    INPUT_TRANSFORM = win32more.UI.Input.Pointer.INPUT_TRANSFORM_head
    class INPUT_TRANSFORM__Anonymous_e__Union(Union):
        pass
    class INPUT_TRANSFORM__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    INPUT_TRANSFORM__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_13", Single),
        ("_14", Single),
        ("_21", Single),
        ("_22", Single),
        ("_23", Single),
        ("_24", Single),
        ("_31", Single),
        ("_32", Single),
        ("_33", Single),
        ("_34", Single),
        ("_41", Single),
        ("_42", Single),
        ("_43", Single),
        ("_44", Single),
    ]
    INPUT_TRANSFORM__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    INPUT_TRANSFORM__Anonymous_e__Union._fields_ = [
        ("Anonymous", INPUT_TRANSFORM__Anonymous_e__Union__Anonymous_e__Struct),
        ("m", Single * 16),
    ]
    INPUT_TRANSFORM._anonymous_ = [
        'Anonymous',
    ]
    INPUT_TRANSFORM._fields_ = [
        ("Anonymous", INPUT_TRANSFORM__Anonymous_e__Union),
    ]
    return INPUT_TRANSFORM
def _define_GetUnpredictedMessagePos():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetUnpredictedMessagePos", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeTouchInjection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.UI.Input.Pointer.TOUCH_FEEDBACK_MODE, use_last_error=True)(("InitializeTouchInjection", windll["USER32"]), ((1, 'maxCount'),(1, 'dwMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InjectTouchInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO), use_last_error=True)(("InjectTouchInput", windll["USER32"]), ((1, 'count'),(1, 'contacts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerType():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE), use_last_error=True)(("GetPointerType", windll["USER32"]), ((1, 'pointerId'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerCursorId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32), use_last_error=True)(("GetPointerCursorId", windll["USER32"]), ((1, 'pointerId'),(1, 'cursorId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head), use_last_error=True)(("GetPointerInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_INFO), use_last_error=True)(("GetPointerInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFrameInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_INFO), use_last_error=True)(("GetPointerFrameInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'pointerCount'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFrameInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head), use_last_error=True)(("GetPointerFrameInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'pointerCount'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerTouchInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head), use_last_error=True)(("GetPointerTouchInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'touchInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerTouchInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO), use_last_error=True)(("GetPointerTouchInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'touchInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFrameTouchInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO), use_last_error=True)(("GetPointerFrameTouchInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'pointerCount'),(1, 'touchInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFrameTouchInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head), use_last_error=True)(("GetPointerFrameTouchInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'pointerCount'),(1, 'touchInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerPenInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head), use_last_error=True)(("GetPointerPenInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'penInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerPenInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO), use_last_error=True)(("GetPointerPenInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'penInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFramePenInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO), use_last_error=True)(("GetPointerFramePenInfo", windll["USER32"]), ((1, 'pointerId'),(1, 'pointerCount'),(1, 'penInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerFramePenInfoHistory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head), use_last_error=True)(("GetPointerFramePenInfoHistory", windll["USER32"]), ((1, 'pointerId'),(1, 'entriesCount'),(1, 'pointerCount'),(1, 'penInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SkipPointerFrameMessages():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=True)(("SkipPointerFrameMessages", windll["USER32"]), ((1, 'pointerId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InjectSyntheticPointerInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Controls.HSYNTHETICPOINTERDEVICE,POINTER(win32more.UI.Controls.POINTER_TYPE_INFO),UInt32, use_last_error=True)(("InjectSyntheticPointerInput", windll["USER32"]), ((1, 'device'),(1, 'pointerInfo'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableMouseInPointer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("EnableMouseInPointer", windll["USER32"]), ((1, 'fEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsMouseInPointerEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("IsMouseInPointerEnabled", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerInputTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,POINTER(win32more.UI.Input.Pointer.INPUT_TRANSFORM), use_last_error=True)(("GetPointerInputTransform", windll["USER32"]), ((1, 'pointerId'),(1, 'historyCount'),(1, 'inputTransform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerDevices():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),POINTER(win32more.UI.Controls.POINTER_DEVICE_INFO), use_last_error=True)(("GetPointerDevices", windll["USER32"]), ((1, 'deviceCount'),(1, 'pointerDevices'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.UI.Controls.POINTER_DEVICE_INFO_head), use_last_error=True)(("GetPointerDevice", windll["USER32"]), ((1, 'device'),(1, 'pointerDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerDeviceProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.UI.Controls.POINTER_DEVICE_PROPERTY), use_last_error=True)(("GetPointerDeviceProperties", windll["USER32"]), ((1, 'device'),(1, 'propertyCount'),(1, 'pointerProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerDeviceRects():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head), use_last_error=True)(("GetPointerDeviceRects", windll["USER32"]), ((1, 'device'),(1, 'pointerDeviceRect'),(1, 'displayRect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPointerDeviceCursors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.UI.Controls.POINTER_DEVICE_CURSOR_INFO), use_last_error=True)(("GetPointerDeviceCursors", windll["USER32"]), ((1, 'device'),(1, 'cursorCount'),(1, 'deviceCursors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRawPointerDeviceData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,UInt32,POINTER(win32more.UI.Controls.POINTER_DEVICE_PROPERTY),POINTER(Int32), use_last_error=True)(("GetRawPointerDeviceData", windll["USER32"]), ((1, 'pointerId'),(1, 'historyCount'),(1, 'propertiesCount'),(1, 'pProperties'),(1, 'pValues'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "POINTER_FLAGS",
    "POINTER_FLAG_NONE",
    "POINTER_FLAG_NEW",
    "POINTER_FLAG_INRANGE",
    "POINTER_FLAG_INCONTACT",
    "POINTER_FLAG_FIRSTBUTTON",
    "POINTER_FLAG_SECONDBUTTON",
    "POINTER_FLAG_THIRDBUTTON",
    "POINTER_FLAG_FOURTHBUTTON",
    "POINTER_FLAG_FIFTHBUTTON",
    "POINTER_FLAG_PRIMARY",
    "POINTER_FLAG_CONFIDENCE",
    "POINTER_FLAG_CANCELED",
    "POINTER_FLAG_DOWN",
    "POINTER_FLAG_UPDATE",
    "POINTER_FLAG_UP",
    "POINTER_FLAG_WHEEL",
    "POINTER_FLAG_HWHEEL",
    "POINTER_FLAG_CAPTURECHANGED",
    "POINTER_FLAG_HASTRANSFORM",
    "TOUCH_FEEDBACK_MODE",
    "TOUCH_FEEDBACK_DEFAULT",
    "TOUCH_FEEDBACK_INDIRECT",
    "TOUCH_FEEDBACK_NONE",
    "POINTER_BUTTON_CHANGE_TYPE",
    "POINTER_CHANGE_NONE",
    "POINTER_CHANGE_FIRSTBUTTON_DOWN",
    "POINTER_CHANGE_FIRSTBUTTON_UP",
    "POINTER_CHANGE_SECONDBUTTON_DOWN",
    "POINTER_CHANGE_SECONDBUTTON_UP",
    "POINTER_CHANGE_THIRDBUTTON_DOWN",
    "POINTER_CHANGE_THIRDBUTTON_UP",
    "POINTER_CHANGE_FOURTHBUTTON_DOWN",
    "POINTER_CHANGE_FOURTHBUTTON_UP",
    "POINTER_CHANGE_FIFTHBUTTON_DOWN",
    "POINTER_CHANGE_FIFTHBUTTON_UP",
    "POINTER_INFO",
    "POINTER_TOUCH_INFO",
    "POINTER_PEN_INFO",
    "INPUT_INJECTION_VALUE",
    "INPUT_TRANSFORM",
    "GetUnpredictedMessagePos",
    "InitializeTouchInjection",
    "InjectTouchInput",
    "GetPointerType",
    "GetPointerCursorId",
    "GetPointerInfo",
    "GetPointerInfoHistory",
    "GetPointerFrameInfo",
    "GetPointerFrameInfoHistory",
    "GetPointerTouchInfo",
    "GetPointerTouchInfoHistory",
    "GetPointerFrameTouchInfo",
    "GetPointerFrameTouchInfoHistory",
    "GetPointerPenInfo",
    "GetPointerPenInfoHistory",
    "GetPointerFramePenInfo",
    "GetPointerFramePenInfoHistory",
    "SkipPointerFrameMessages",
    "InjectSyntheticPointerInput",
    "EnableMouseInPointer",
    "IsMouseInPointerEnabled",
    "GetPointerInputTransform",
    "GetPointerDevices",
    "GetPointerDevice",
    "GetPointerDeviceProperties",
    "GetPointerDeviceRects",
    "GetPointerDeviceCursors",
    "GetRawPointerDeviceData",
]
