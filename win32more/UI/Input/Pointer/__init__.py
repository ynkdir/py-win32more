from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.UI.Controls
import win32more.UI.Input.Pointer
import win32more.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('USER32.dll')
def GetUnpredictedMessagePos() -> UInt32: ...
@winfunctype('USER32.dll')
def InitializeTouchInjection(maxCount: UInt32, dwMode: win32more.UI.Input.Pointer.TOUCH_FEEDBACK_MODE) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def InjectTouchInput(count: UInt32, contacts: POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerType(pointerId: UInt32, pointerType: POINTER(win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerCursorId(pointerId: UInt32, cursorId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInfo(pointerId: UInt32, pointerInfo: POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerInfo: POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), pointerInfo: POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), pointerInfo: POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerTouchInfo(pointerId: UInt32, touchInfo: POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerTouchInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), touchInfo: POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameTouchInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), touchInfo: POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameTouchInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), touchInfo: POINTER(win32more.UI.Input.Pointer.POINTER_TOUCH_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerPenInfo(pointerId: UInt32, penInfo: POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerPenInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), penInfo: POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFramePenInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), penInfo: POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFramePenInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), penInfo: POINTER(win32more.UI.Input.Pointer.POINTER_PEN_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SkipPointerFrameMessages(pointerId: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def InjectSyntheticPointerInput(device: win32more.UI.Controls.HSYNTHETICPOINTERDEVICE, pointerInfo: POINTER(win32more.UI.Controls.POINTER_TYPE_INFO_head), count: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnableMouseInPointer(fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsMouseInPointerEnabled() -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInputTransform(pointerId: UInt32, historyCount: UInt32, inputTransform: POINTER(win32more.UI.Input.Pointer.INPUT_TRANSFORM_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDevices(deviceCount: POINTER(UInt32), pointerDevices: POINTER(win32more.UI.Controls.POINTER_DEVICE_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDevice(device: win32more.Foundation.HANDLE, pointerDevice: POINTER(win32more.UI.Controls.POINTER_DEVICE_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceProperties(device: win32more.Foundation.HANDLE, propertyCount: POINTER(UInt32), pointerProperties: POINTER(win32more.UI.Controls.POINTER_DEVICE_PROPERTY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceRects(device: win32more.Foundation.HANDLE, pointerDeviceRect: POINTER(win32more.Foundation.RECT_head), displayRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceCursors(device: win32more.Foundation.HANDLE, cursorCount: POINTER(UInt32), deviceCursors: POINTER(win32more.UI.Controls.POINTER_DEVICE_CURSOR_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetRawPointerDeviceData(pointerId: UInt32, historyCount: UInt32, propertiesCount: UInt32, pProperties: POINTER(win32more.UI.Controls.POINTER_DEVICE_PROPERTY_head), pValues: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
class INPUT_INJECTION_VALUE(Structure):
    page: UInt16
    usage: UInt16
    value: Int32
    index: UInt16
class INPUT_TRANSFORM(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        m: Single * 16
        class _Anonymous_e__Struct(Structure):
            _11: Single
            _12: Single
            _13: Single
            _14: Single
            _21: Single
            _22: Single
            _23: Single
            _24: Single
            _31: Single
            _32: Single
            _33: Single
            _34: Single
            _41: Single
            _42: Single
            _43: Single
            _44: Single
POINTER_BUTTON_CHANGE_TYPE = Int32
POINTER_CHANGE_NONE: POINTER_BUTTON_CHANGE_TYPE = 0
POINTER_CHANGE_FIRSTBUTTON_DOWN: POINTER_BUTTON_CHANGE_TYPE = 1
POINTER_CHANGE_FIRSTBUTTON_UP: POINTER_BUTTON_CHANGE_TYPE = 2
POINTER_CHANGE_SECONDBUTTON_DOWN: POINTER_BUTTON_CHANGE_TYPE = 3
POINTER_CHANGE_SECONDBUTTON_UP: POINTER_BUTTON_CHANGE_TYPE = 4
POINTER_CHANGE_THIRDBUTTON_DOWN: POINTER_BUTTON_CHANGE_TYPE = 5
POINTER_CHANGE_THIRDBUTTON_UP: POINTER_BUTTON_CHANGE_TYPE = 6
POINTER_CHANGE_FOURTHBUTTON_DOWN: POINTER_BUTTON_CHANGE_TYPE = 7
POINTER_CHANGE_FOURTHBUTTON_UP: POINTER_BUTTON_CHANGE_TYPE = 8
POINTER_CHANGE_FIFTHBUTTON_DOWN: POINTER_BUTTON_CHANGE_TYPE = 9
POINTER_CHANGE_FIFTHBUTTON_UP: POINTER_BUTTON_CHANGE_TYPE = 10
POINTER_FLAGS = UInt32
POINTER_FLAG_NONE: POINTER_FLAGS = 0
POINTER_FLAG_NEW: POINTER_FLAGS = 1
POINTER_FLAG_INRANGE: POINTER_FLAGS = 2
POINTER_FLAG_INCONTACT: POINTER_FLAGS = 4
POINTER_FLAG_FIRSTBUTTON: POINTER_FLAGS = 16
POINTER_FLAG_SECONDBUTTON: POINTER_FLAGS = 32
POINTER_FLAG_THIRDBUTTON: POINTER_FLAGS = 64
POINTER_FLAG_FOURTHBUTTON: POINTER_FLAGS = 128
POINTER_FLAG_FIFTHBUTTON: POINTER_FLAGS = 256
POINTER_FLAG_PRIMARY: POINTER_FLAGS = 8192
POINTER_FLAG_CONFIDENCE: POINTER_FLAGS = 16384
POINTER_FLAG_CANCELED: POINTER_FLAGS = 32768
POINTER_FLAG_DOWN: POINTER_FLAGS = 65536
POINTER_FLAG_UPDATE: POINTER_FLAGS = 131072
POINTER_FLAG_UP: POINTER_FLAGS = 262144
POINTER_FLAG_WHEEL: POINTER_FLAGS = 524288
POINTER_FLAG_HWHEEL: POINTER_FLAGS = 1048576
POINTER_FLAG_CAPTURECHANGED: POINTER_FLAGS = 2097152
POINTER_FLAG_HASTRANSFORM: POINTER_FLAGS = 4194304
class POINTER_INFO(Structure):
    pointerType: win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE
    pointerId: UInt32
    frameId: UInt32
    pointerFlags: win32more.UI.Input.Pointer.POINTER_FLAGS
    sourceDevice: win32more.Foundation.HANDLE
    hwndTarget: win32more.Foundation.HWND
    ptPixelLocation: win32more.Foundation.POINT
    ptHimetricLocation: win32more.Foundation.POINT
    ptPixelLocationRaw: win32more.Foundation.POINT
    ptHimetricLocationRaw: win32more.Foundation.POINT
    dwTime: UInt32
    historyCount: UInt32
    InputData: Int32
    dwKeyStates: UInt32
    PerformanceCount: UInt64
    ButtonChangeType: win32more.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE
class POINTER_PEN_INFO(Structure):
    pointerInfo: win32more.UI.Input.Pointer.POINTER_INFO
    penFlags: UInt32
    penMask: UInt32
    pressure: UInt32
    rotation: UInt32
    tiltX: Int32
    tiltY: Int32
class POINTER_TOUCH_INFO(Structure):
    pointerInfo: win32more.UI.Input.Pointer.POINTER_INFO
    touchFlags: UInt32
    touchMask: UInt32
    rcContact: win32more.Foundation.RECT
    rcContactRaw: win32more.Foundation.RECT
    orientation: UInt32
    pressure: UInt32
TOUCH_FEEDBACK_MODE = UInt32
TOUCH_FEEDBACK_DEFAULT: TOUCH_FEEDBACK_MODE = 1
TOUCH_FEEDBACK_INDIRECT: TOUCH_FEEDBACK_MODE = 2
TOUCH_FEEDBACK_NONE: TOUCH_FEEDBACK_MODE = 3
make_head(_module, 'INPUT_INJECTION_VALUE')
make_head(_module, 'INPUT_TRANSFORM')
make_head(_module, 'POINTER_INFO')
make_head(_module, 'POINTER_PEN_INFO')
make_head(_module, 'POINTER_TOUCH_INFO')
__all__ = [
    "EnableMouseInPointer",
    "GetPointerCursorId",
    "GetPointerDevice",
    "GetPointerDeviceCursors",
    "GetPointerDeviceProperties",
    "GetPointerDeviceRects",
    "GetPointerDevices",
    "GetPointerFrameInfo",
    "GetPointerFrameInfoHistory",
    "GetPointerFramePenInfo",
    "GetPointerFramePenInfoHistory",
    "GetPointerFrameTouchInfo",
    "GetPointerFrameTouchInfoHistory",
    "GetPointerInfo",
    "GetPointerInfoHistory",
    "GetPointerInputTransform",
    "GetPointerPenInfo",
    "GetPointerPenInfoHistory",
    "GetPointerTouchInfo",
    "GetPointerTouchInfoHistory",
    "GetPointerType",
    "GetRawPointerDeviceData",
    "GetUnpredictedMessagePos",
    "INPUT_INJECTION_VALUE",
    "INPUT_TRANSFORM",
    "InitializeTouchInjection",
    "InjectSyntheticPointerInput",
    "InjectTouchInput",
    "IsMouseInPointerEnabled",
    "POINTER_BUTTON_CHANGE_TYPE",
    "POINTER_CHANGE_FIFTHBUTTON_DOWN",
    "POINTER_CHANGE_FIFTHBUTTON_UP",
    "POINTER_CHANGE_FIRSTBUTTON_DOWN",
    "POINTER_CHANGE_FIRSTBUTTON_UP",
    "POINTER_CHANGE_FOURTHBUTTON_DOWN",
    "POINTER_CHANGE_FOURTHBUTTON_UP",
    "POINTER_CHANGE_NONE",
    "POINTER_CHANGE_SECONDBUTTON_DOWN",
    "POINTER_CHANGE_SECONDBUTTON_UP",
    "POINTER_CHANGE_THIRDBUTTON_DOWN",
    "POINTER_CHANGE_THIRDBUTTON_UP",
    "POINTER_FLAGS",
    "POINTER_FLAG_CANCELED",
    "POINTER_FLAG_CAPTURECHANGED",
    "POINTER_FLAG_CONFIDENCE",
    "POINTER_FLAG_DOWN",
    "POINTER_FLAG_FIFTHBUTTON",
    "POINTER_FLAG_FIRSTBUTTON",
    "POINTER_FLAG_FOURTHBUTTON",
    "POINTER_FLAG_HASTRANSFORM",
    "POINTER_FLAG_HWHEEL",
    "POINTER_FLAG_INCONTACT",
    "POINTER_FLAG_INRANGE",
    "POINTER_FLAG_NEW",
    "POINTER_FLAG_NONE",
    "POINTER_FLAG_PRIMARY",
    "POINTER_FLAG_SECONDBUTTON",
    "POINTER_FLAG_THIRDBUTTON",
    "POINTER_FLAG_UP",
    "POINTER_FLAG_UPDATE",
    "POINTER_FLAG_WHEEL",
    "POINTER_INFO",
    "POINTER_PEN_INFO",
    "POINTER_TOUCH_INFO",
    "SkipPointerFrameMessages",
    "TOUCH_FEEDBACK_DEFAULT",
    "TOUCH_FEEDBACK_INDIRECT",
    "TOUCH_FEEDBACK_MODE",
    "TOUCH_FEEDBACK_NONE",
]
