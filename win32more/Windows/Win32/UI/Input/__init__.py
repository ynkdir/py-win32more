from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.UI.Input
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('USER32.dll')
def GetRawInputData(hRawInput: win32more.Windows.Win32.UI.Input.HRAWINPUT, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DATA_COMMAND_FLAGS, pData: VoidPtr, pcbSize: POINTER(UInt32), cbSizeHeader: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceInfoA(hDevice: win32more.Windows.Win32.Foundation.HANDLE, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND, pData: VoidPtr, pcbSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceInfoW(hDevice: win32more.Windows.Win32.Foundation.HANDLE, uiCommand: win32more.Windows.Win32.UI.Input.RAW_INPUT_DEVICE_INFO_COMMAND, pData: VoidPtr, pcbSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputBuffer(pData: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUT_head), pcbSize: POINTER(UInt32), cbSizeHeader: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def RegisterRawInputDevices(pRawInputDevices: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_head), uiNumDevices: UInt32, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetRegisteredRawInputDevices(pRawInputDevices: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICE_head), puiNumDevices: POINTER(UInt32), cbSize: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetRawInputDeviceList(pRawInputDeviceList: POINTER(win32more.Windows.Win32.UI.Input.RAWINPUTDEVICELIST_head), puiNumDevices: POINTER(UInt32), cbSize: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DefRawInputProc(paRawInput: POINTER(POINTER(win32more.Windows.Win32.UI.Input.RAWINPUT_head)), nInput: Int32, cbSizeHeader: UInt32) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def GetCurrentInputMessageSource(inputMessageSource: POINTER(win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_SOURCE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetCIMSSM(inputMessageSource: POINTER(win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_SOURCE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
HRAWINPUT = IntPtr
INPUT_MESSAGE_DEVICE_TYPE = Int32
IMDT_UNAVAILABLE: INPUT_MESSAGE_DEVICE_TYPE = 0
IMDT_KEYBOARD: INPUT_MESSAGE_DEVICE_TYPE = 1
IMDT_MOUSE: INPUT_MESSAGE_DEVICE_TYPE = 2
IMDT_TOUCH: INPUT_MESSAGE_DEVICE_TYPE = 4
IMDT_PEN: INPUT_MESSAGE_DEVICE_TYPE = 8
IMDT_TOUCHPAD: INPUT_MESSAGE_DEVICE_TYPE = 16
INPUT_MESSAGE_ORIGIN_ID = Int32
IMO_UNAVAILABLE: INPUT_MESSAGE_ORIGIN_ID = 0
IMO_HARDWARE: INPUT_MESSAGE_ORIGIN_ID = 1
IMO_INJECTED: INPUT_MESSAGE_ORIGIN_ID = 2
IMO_SYSTEM: INPUT_MESSAGE_ORIGIN_ID = 4
class INPUT_MESSAGE_SOURCE(EasyCastStructure):
    deviceType: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_DEVICE_TYPE
    originId: win32more.Windows.Win32.UI.Input.INPUT_MESSAGE_ORIGIN_ID
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
RIDEV_REMOVE: RAWINPUTDEVICE_FLAGS = 1
RIDEV_EXCLUDE: RAWINPUTDEVICE_FLAGS = 16
RIDEV_PAGEONLY: RAWINPUTDEVICE_FLAGS = 32
RIDEV_NOLEGACY: RAWINPUTDEVICE_FLAGS = 48
RIDEV_INPUTSINK: RAWINPUTDEVICE_FLAGS = 256
RIDEV_CAPTUREMOUSE: RAWINPUTDEVICE_FLAGS = 512
RIDEV_NOHOTKEYS: RAWINPUTDEVICE_FLAGS = 512
RIDEV_APPKEYS: RAWINPUTDEVICE_FLAGS = 1024
RIDEV_EXINPUTSINK: RAWINPUTDEVICE_FLAGS = 4096
RIDEV_DEVNOTIFY: RAWINPUTDEVICE_FLAGS = 8192
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
    usFlags: UInt16
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
RID_HEADER: RAW_INPUT_DATA_COMMAND_FLAGS = 268435461
RID_INPUT: RAW_INPUT_DATA_COMMAND_FLAGS = 268435459
RAW_INPUT_DEVICE_INFO_COMMAND = UInt32
RIDI_PREPARSEDDATA: RAW_INPUT_DEVICE_INFO_COMMAND = 536870917
RIDI_DEVICENAME: RAW_INPUT_DEVICE_INFO_COMMAND = 536870919
RIDI_DEVICEINFO: RAW_INPUT_DEVICE_INFO_COMMAND = 536870923
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
RIM_TYPEMOUSE: RID_DEVICE_INFO_TYPE = 0
RIM_TYPEKEYBOARD: RID_DEVICE_INFO_TYPE = 1
RIM_TYPEHID: RID_DEVICE_INFO_TYPE = 2
make_head(_module, 'INPUT_MESSAGE_SOURCE')
make_head(_module, 'RAWHID')
make_head(_module, 'RAWINPUT')
make_head(_module, 'RAWINPUTDEVICE')
make_head(_module, 'RAWINPUTDEVICELIST')
make_head(_module, 'RAWINPUTHEADER')
make_head(_module, 'RAWKEYBOARD')
make_head(_module, 'RAWMOUSE')
make_head(_module, 'RID_DEVICE_INFO')
make_head(_module, 'RID_DEVICE_INFO_HID')
make_head(_module, 'RID_DEVICE_INFO_KEYBOARD')
make_head(_module, 'RID_DEVICE_INFO_MOUSE')
