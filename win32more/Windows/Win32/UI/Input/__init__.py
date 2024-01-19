from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.UI.Input
@winfunctype('USER32.dll')
def GetRawInputData(hRawInput: win32more.Windows.Win32.UI.Input.HRAWINPUT, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DATA_COMMAND_FLAGS, pData: VoidPtr, pcbSize: POINTER(UInt32), cbSizeHeader: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceInfoA(hDevice: win32more.Windows.Win32.Foundation.HANDLE, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND, pData: VoidPtr, pcbSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceInfoW(hDevice: win32more.Windows.Win32.Foundation.HANDLE, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND, pData: VoidPtr, pcbSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputBuffer(pData: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUT), pcbSize: POINTER(UInt32), cbSizeHeader: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def RegisterRawInputDevices(pRawInputDevices: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE), uiNumDevices: UInt32, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetRegisteredRawInputDevices(pRawInputDevices: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE), puiNumDevices: POINTER(UInt32), cbSize: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceList(pRawInputDeviceList: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICELIST), puiNumDevices: POINTER(UInt32), cbSize: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DefRawInputProc(paRawInput: POINTER(POINTER(win32more.Windows.Win32.UI.Input.RAWINPUT)), nInput: Int32, cbSizeHeader: UInt32) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def GetCurrentInputMessageSource(inputMessageSource: POINTER(win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_SOURCE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetCIMSSM(inputMessageSource: POINTER(win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_SOURCE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
HRAWINPUT = IntPtr
INPUT_MESSAGE_DEVICE_TYPE = Int32
IMDT_UNAVAILABLE: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 0
IMDT_KEYBOARD: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 1
IMDT_MOUSE: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 2
IMDT_TOUCH: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 4
IMDT_PEN: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 8
IMDT_TOUCHPAD: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE = 16
INPUT_MESSAGE_ORIGIN_ID = Int32
IMO_UNAVAILABLE: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID = 0
IMO_HARDWARE: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID = 1
IMO_INJECTED: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID = 2
IMO_SYSTEM: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID = 4
class INPUT_MESSAGE_SOURCE(EasyCastStructure):
    deviceType: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE
    originId: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID
MOUSE_STATE = UInt16
MOUSE_MOVE_RELATIVE: win32more.Windows.Win32.UI.Input.MOUSE_STATE = 0
MOUSE_MOVE_ABSOLUTE: win32more.Windows.Win32.UI.Input.MOUSE_STATE = 1
MOUSE_VIRTUAL_DESKTOP: win32more.Windows.Win32.UI.Input.MOUSE_STATE = 2
MOUSE_ATTRIBUTES_CHANGED: win32more.Windows.Win32.UI.Input.MOUSE_STATE = 4
MOUSE_MOVE_NOCOALESCE: win32more.Windows.Win32.UI.Input.MOUSE_STATE = 8
class RAWHID(EasyCastStructure):
    dwSizeHid: UInt32
    dwCount: UInt32
    bRawData: Byte * 1
class RAWINPUT(EasyCastStructure):
    header: win32more.Windows.Win32.UI.Input.RAWINPUTHEADER
    data: _data_e__Union
    class _data_e__Union(EasyCastUnion):
        mouse: win32more.Windows.Win32.UI.Input.RAWMOUSE
        keyboard: win32more.Windows.Win32.UI.Input.RAWKEYBOARD
        hid: win32more.Windows.Win32.UI.Input.RAWHID
class RAWINPUTDEVICE(EasyCastStructure):
    usUsagePage: UInt16
    usUsage: UInt16
    dwFlags: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS
    hwndTarget: win32more.Windows.Win32.Foundation.HWND
class RAWINPUTDEVICELIST(EasyCastStructure):
    hDevice: win32more.Windows.Win32.Foundation.HANDLE
    dwType: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_TYPE
RAWINPUTDEVICE_FLAGS = UInt32
RIDEV_REMOVE: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 1
RIDEV_EXCLUDE: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 16
RIDEV_PAGEONLY: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 32
RIDEV_NOLEGACY: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 48
RIDEV_INPUTSINK: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 256
RIDEV_CAPTUREMOUSE: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 512
RIDEV_NOHOTKEYS: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 512
RIDEV_APPKEYS: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 1024
RIDEV_EXINPUTSINK: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 4096
RIDEV_DEVNOTIFY: win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_FLAGS = 8192
class RAWINPUTHEADER(EasyCastStructure):
    dwType: UInt32
    dwSize: UInt32
    hDevice: win32more.Windows.Win32.Foundation.HANDLE
    wParam: win32more.Windows.Win32.Foundation.WPARAM
class RAWKEYBOARD(EasyCastStructure):
    MakeCode: UInt16
    Flags: UInt16
    Reserved: UInt16
    VKey: UInt16
    Message: UInt32
    ExtraInformation: UInt32
class RAWMOUSE(EasyCastStructure):
    usFlags: win32more.Windows.Win32.UI.Input.MOUSE_STATE
    Anonymous: _Anonymous_e__Union
    ulRawButtons: UInt32
    lLastX: Int32
    lLastY: Int32
    ulExtraInformation: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
        ulButtons: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            usButtonFlags: UInt16
            usButtonData: UInt16
RAW_INPUT_DATA_COMMAND_FLAGS = UInt32
RID_HEADER: win32more.Windows.Win32.UI.Input.RAW_INPUT_DATA_COMMAND_FLAGS = 268435461
RID_INPUT: win32more.Windows.Win32.UI.Input.RAW_INPUT_DATA_COMMAND_FLAGS = 268435459
RAW_INPUT_DEVICE_INFO_COMMAND = UInt32
RIDI_PREPARSEDDATA: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND = 536870917
RIDI_DEVICENAME: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND = 536870919
RIDI_DEVICEINFO: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND = 536870923
class RID_DEVICE_INFO(EasyCastStructure):
    cbSize: UInt32
    dwType: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        mouse: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_MOUSE
        keyboard: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_KEYBOARD
        hid: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_HID
class RID_DEVICE_INFO_HID(EasyCastStructure):
    dwVendorId: UInt32
    dwProductId: UInt32
    dwVersionNumber: UInt32
    usUsagePage: UInt16
    usUsage: UInt16
class RID_DEVICE_INFO_KEYBOARD(EasyCastStructure):
    dwType: UInt32
    dwSubType: UInt32
    dwKeyboardMode: UInt32
    dwNumberOfFunctionKeys: UInt32
    dwNumberOfIndicators: UInt32
    dwNumberOfKeysTotal: UInt32
class RID_DEVICE_INFO_MOUSE(EasyCastStructure):
    dwId: UInt32
    dwNumberOfButtons: UInt32
    dwSampleRate: UInt32
    fHasHorizontalWheel: win32more.Windows.Win32.Foundation.BOOL
RID_DEVICE_INFO_TYPE = UInt32
RIM_TYPEMOUSE: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_TYPE = 0
RIM_TYPEKEYBOARD: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_TYPE = 1
RIM_TYPEHID: win32more.Windows.Win32.UI.Input.RID_DEVICE_INFO_TYPE = 2


make_ready(__name__)
