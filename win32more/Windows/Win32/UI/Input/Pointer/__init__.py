from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Input.Pointer
import win32more.Windows.Win32.UI.WindowsAndMessaging
@winfunctype('USER32.dll')
def GetUnpredictedMessagePos() -> UInt32: ...
@winfunctype('USER32.dll')
def InitializeTouchInjection(maxCount: UInt32, dwMode: win32more.Windows.Win32.UI.Input.Pointer.TOUCH_FEEDBACK_MODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def InjectTouchInput(count: UInt32, contacts: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_TOUCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerType(pointerId: UInt32, pointerType: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerCursorId(pointerId: UInt32, cursorId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInfo(pointerId: UInt32, pointerInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), pointerInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), pointerInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerTouchInfo(pointerId: UInt32, touchInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_TOUCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerTouchInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), touchInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_TOUCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameTouchInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), touchInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_TOUCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFrameTouchInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), touchInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_TOUCH_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerPenInfo(pointerId: UInt32, penInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_PEN_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerPenInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), penInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_PEN_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFramePenInfo(pointerId: UInt32, pointerCount: POINTER(UInt32), penInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_PEN_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerFramePenInfoHistory(pointerId: UInt32, entriesCount: POINTER(UInt32), pointerCount: POINTER(UInt32), penInfo: POINTER(win32more.Windows.Win32.UI.Input.Pointer.POINTER_PEN_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SkipPointerFrameMessages(pointerId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def InjectSyntheticPointerInput(device: win32more.Windows.Win32.UI.Controls.HSYNTHETICPOINTERDEVICE, pointerInfo: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_TYPE_INFO), count: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnableMouseInPointer(fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsMouseInPointerEnabled() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerInputTransform(pointerId: UInt32, historyCount: UInt32, inputTransform: POINTER(win32more.Windows.Win32.UI.Input.Pointer.INPUT_TRANSFORM)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDevices(deviceCount: POINTER(UInt32), pointerDevices: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_DEVICE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDevice(device: win32more.Windows.Win32.Foundation.HANDLE, pointerDevice: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_DEVICE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceProperties(device: win32more.Windows.Win32.Foundation.HANDLE, propertyCount: POINTER(UInt32), pointerProperties: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_DEVICE_PROPERTY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceRects(device: win32more.Windows.Win32.Foundation.HANDLE, pointerDeviceRect: POINTER(win32more.Windows.Win32.Foundation.RECT), displayRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPointerDeviceCursors(device: win32more.Windows.Win32.Foundation.HANDLE, cursorCount: POINTER(UInt32), deviceCursors: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_DEVICE_CURSOR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetRawPointerDeviceData(pointerId: UInt32, historyCount: UInt32, propertiesCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.UI.Controls.POINTER_DEVICE_PROPERTY), pValues: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
POINTER_CHANGE_NONE: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 0
POINTER_CHANGE_FIRSTBUTTON_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 1
POINTER_CHANGE_FIRSTBUTTON_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 2
POINTER_CHANGE_SECONDBUTTON_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 3
POINTER_CHANGE_SECONDBUTTON_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 4
POINTER_CHANGE_THIRDBUTTON_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 5
POINTER_CHANGE_THIRDBUTTON_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 6
POINTER_CHANGE_FOURTHBUTTON_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 7
POINTER_CHANGE_FOURTHBUTTON_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 8
POINTER_CHANGE_FIFTHBUTTON_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 9
POINTER_CHANGE_FIFTHBUTTON_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE = 10
POINTER_FLAGS = UInt32
POINTER_FLAG_NONE: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 0
POINTER_FLAG_NEW: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 1
POINTER_FLAG_INRANGE: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 2
POINTER_FLAG_INCONTACT: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 4
POINTER_FLAG_FIRSTBUTTON: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 16
POINTER_FLAG_SECONDBUTTON: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 32
POINTER_FLAG_THIRDBUTTON: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 64
POINTER_FLAG_FOURTHBUTTON: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 128
POINTER_FLAG_FIFTHBUTTON: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 256
POINTER_FLAG_PRIMARY: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 8192
POINTER_FLAG_CONFIDENCE: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 16384
POINTER_FLAG_CANCELED: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 32768
POINTER_FLAG_DOWN: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 65536
POINTER_FLAG_UPDATE: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 131072
POINTER_FLAG_UP: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 262144
POINTER_FLAG_WHEEL: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 524288
POINTER_FLAG_HWHEEL: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 1048576
POINTER_FLAG_CAPTURECHANGED: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 2097152
POINTER_FLAG_HASTRANSFORM: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS = 4194304
class POINTER_INFO(Structure):
    pointerType: win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE
    pointerId: UInt32
    frameId: UInt32
    pointerFlags: win32more.Windows.Win32.UI.Input.Pointer.POINTER_FLAGS
    sourceDevice: win32more.Windows.Win32.Foundation.HANDLE
    hwndTarget: win32more.Windows.Win32.Foundation.HWND
    ptPixelLocation: win32more.Windows.Win32.Foundation.POINT
    ptHimetricLocation: win32more.Windows.Win32.Foundation.POINT
    ptPixelLocationRaw: win32more.Windows.Win32.Foundation.POINT
    ptHimetricLocationRaw: win32more.Windows.Win32.Foundation.POINT
    dwTime: UInt32
    historyCount: UInt32
    InputData: Int32
    dwKeyStates: UInt32
    PerformanceCount: UInt64
    ButtonChangeType: win32more.Windows.Win32.UI.Input.Pointer.POINTER_BUTTON_CHANGE_TYPE
class POINTER_PEN_INFO(Structure):
    pointerInfo: win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO
    penFlags: UInt32
    penMask: UInt32
    pressure: UInt32
    rotation: UInt32
    tiltX: Int32
    tiltY: Int32
class POINTER_TOUCH_INFO(Structure):
    pointerInfo: win32more.Windows.Win32.UI.Input.Pointer.POINTER_INFO
    touchFlags: UInt32
    touchMask: UInt32
    rcContact: win32more.Windows.Win32.Foundation.RECT
    rcContactRaw: win32more.Windows.Win32.Foundation.RECT
    orientation: UInt32
    pressure: UInt32
TOUCH_FEEDBACK_MODE = UInt32
TOUCH_FEEDBACK_DEFAULT: win32more.Windows.Win32.UI.Input.Pointer.TOUCH_FEEDBACK_MODE = 1
TOUCH_FEEDBACK_INDIRECT: win32more.Windows.Win32.UI.Input.Pointer.TOUCH_FEEDBACK_MODE = 2
TOUCH_FEEDBACK_NONE: win32more.Windows.Win32.UI.Input.Pointer.TOUCH_FEEDBACK_MODE = 3


make_ready(__name__)
