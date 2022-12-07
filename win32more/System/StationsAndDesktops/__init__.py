from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.StationsAndDesktops
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
def CreateDesktopA(lpszDesktop: win32more.Foundation.PSTR, lpszDevice: win32more.Foundation.PSTR, pDevmode: POINTER(win32more.Graphics.Gdi.DEVMODEA_head), dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopW(lpszDesktop: win32more.Foundation.PWSTR, lpszDevice: win32more.Foundation.PWSTR, pDevmode: POINTER(win32more.Graphics.Gdi.DEVMODEW_head), dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopExA(lpszDesktop: win32more.Foundation.PSTR, lpszDevice: win32more.Foundation.PSTR, pDevmode: POINTER(win32more.Graphics.Gdi.DEVMODEA_head), dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), ulHeapSize: UInt32, pvoid: c_void_p) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopExW(lpszDesktop: win32more.Foundation.PWSTR, lpszDevice: win32more.Foundation.PWSTR, pDevmode: POINTER(win32more.Graphics.Gdi.DEVMODEW_head), dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), ulHeapSize: UInt32, pvoid: c_void_p) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenDesktopA(lpszDesktop: win32more.Foundation.PSTR, dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenDesktopW(lpszDesktop: win32more.Foundation.PWSTR, dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenInputDesktop(dwFlags: win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Foundation.BOOL, dwDesiredAccess: win32more.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def EnumDesktopsA(hwinsta: win32more.System.StationsAndDesktops.HWINSTA, lpEnumFunc: win32more.System.StationsAndDesktops.DESKTOPENUMPROCA, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumDesktopsW(hwinsta: win32more.System.StationsAndDesktops.HWINSTA, lpEnumFunc: win32more.System.StationsAndDesktops.DESKTOPENUMPROCW, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumDesktopWindows(hDesktop: win32more.System.StationsAndDesktops.HDESK, lpfn: win32more.UI.WindowsAndMessaging.WNDENUMPROC, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SwitchDesktop(hDesktop: win32more.System.StationsAndDesktops.HDESK) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDesktop(hDesktop: win32more.System.StationsAndDesktops.HDESK) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseDesktop(hDesktop: win32more.System.StationsAndDesktops.HDESK) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetThreadDesktop(dwThreadId: UInt32) -> win32more.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateWindowStationA(lpwinsta: win32more.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def CreateWindowStationW(lpwinsta: win32more.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def OpenWindowStationA(lpszWinSta: win32more.Foundation.PSTR, fInherit: win32more.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def OpenWindowStationW(lpszWinSta: win32more.Foundation.PWSTR, fInherit: win32more.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def EnumWindowStationsA(lpEnumFunc: win32more.System.StationsAndDesktops.WINSTAENUMPROCA, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumWindowStationsW(lpEnumFunc: win32more.System.StationsAndDesktops.WINSTAENUMPROCW, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseWindowStation(hWinSta: win32more.System.StationsAndDesktops.HWINSTA) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessWindowStation(hWinSta: win32more.System.StationsAndDesktops.HWINSTA) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetProcessWindowStation() -> win32more.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationA(hObj: win32more.Foundation.HANDLE, nIndex: win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: c_void_p, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationW(hObj: win32more.Foundation.HANDLE, nIndex: win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: c_void_p, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetUserObjectInformationA(hObj: win32more.Foundation.HANDLE, nIndex: Int32, pvInfo: c_void_p, nLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetUserObjectInformationW(hObj: win32more.Foundation.HANDLE, nIndex: Int32, pvInfo: c_void_p, nLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageExA(flags: win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pbsmInfo: POINTER(win32more.System.StationsAndDesktops.BSMINFO_head)) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageExW(flags: win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pbsmInfo: POINTER(win32more.System.StationsAndDesktops.BSMINFO_head)) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageA(flags: UInt32, lpInfo: POINTER(UInt32), Msg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageW(flags: win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> Int32: ...
BROADCAST_SYSTEM_MESSAGE_FLAGS = UInt32
BSF_ALLOWSFW: BROADCAST_SYSTEM_MESSAGE_FLAGS = 128
BSF_FLUSHDISK: BROADCAST_SYSTEM_MESSAGE_FLAGS = 4
BSF_FORCEIFHUNG: BROADCAST_SYSTEM_MESSAGE_FLAGS = 32
BSF_IGNORECURRENTTASK: BROADCAST_SYSTEM_MESSAGE_FLAGS = 2
BSF_NOHANG: BROADCAST_SYSTEM_MESSAGE_FLAGS = 8
BSF_NOTIMEOUTIFNOTHUNG: BROADCAST_SYSTEM_MESSAGE_FLAGS = 64
BSF_POSTMESSAGE: BROADCAST_SYSTEM_MESSAGE_FLAGS = 16
BSF_QUERY: BROADCAST_SYSTEM_MESSAGE_FLAGS = 1
BSF_SENDNOTIFYMESSAGE: BROADCAST_SYSTEM_MESSAGE_FLAGS = 256
BSF_LUID: BROADCAST_SYSTEM_MESSAGE_FLAGS = 1024
BSF_RETURNHDESK: BROADCAST_SYSTEM_MESSAGE_FLAGS = 512
BROADCAST_SYSTEM_MESSAGE_INFO = UInt32
BSM_ALLCOMPONENTS: BROADCAST_SYSTEM_MESSAGE_INFO = 0
BSM_ALLDESKTOPS: BROADCAST_SYSTEM_MESSAGE_INFO = 16
BSM_APPLICATIONS: BROADCAST_SYSTEM_MESSAGE_INFO = 8
class BSMINFO(Structure):
    cbSize: UInt32
    hdesk: win32more.System.StationsAndDesktops.HDESK
    hwnd: win32more.Foundation.HWND
    luid: win32more.Foundation.LUID
DESKTOP_ACCESS_FLAGS = UInt32
DESKTOP_DELETE: DESKTOP_ACCESS_FLAGS = 65536
DESKTOP_READ_CONTROL: DESKTOP_ACCESS_FLAGS = 131072
DESKTOP_WRITE_DAC: DESKTOP_ACCESS_FLAGS = 262144
DESKTOP_WRITE_OWNER: DESKTOP_ACCESS_FLAGS = 524288
DESKTOP_SYNCHRONIZE: DESKTOP_ACCESS_FLAGS = 1048576
DESKTOP_READOBJECTS: DESKTOP_ACCESS_FLAGS = 1
DESKTOP_CREATEWINDOW: DESKTOP_ACCESS_FLAGS = 2
DESKTOP_CREATEMENU: DESKTOP_ACCESS_FLAGS = 4
DESKTOP_HOOKCONTROL: DESKTOP_ACCESS_FLAGS = 8
DESKTOP_JOURNALRECORD: DESKTOP_ACCESS_FLAGS = 16
DESKTOP_JOURNALPLAYBACK: DESKTOP_ACCESS_FLAGS = 32
DESKTOP_ENUMERATE: DESKTOP_ACCESS_FLAGS = 64
DESKTOP_WRITEOBJECTS: DESKTOP_ACCESS_FLAGS = 128
DESKTOP_SWITCHDESKTOP: DESKTOP_ACCESS_FLAGS = 256
DESKTOP_CONTROL_FLAGS = UInt32
DF_ALLOWOTHERACCOUNTHOOK: DESKTOP_CONTROL_FLAGS = 1
@winfunctype_pointer
def DESKTOPENUMPROCA(param0: win32more.Foundation.PSTR, param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def DESKTOPENUMPROCW(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
HDESK = IntPtr
HWINSTA = IntPtr
USER_OBJECT_INFORMATION_INDEX = UInt32
UOI_FLAGS: USER_OBJECT_INFORMATION_INDEX = 1
UOI_HEAPSIZE: USER_OBJECT_INFORMATION_INDEX = 5
UOI_IO: USER_OBJECT_INFORMATION_INDEX = 6
UOI_NAME: USER_OBJECT_INFORMATION_INDEX = 2
UOI_TYPE: USER_OBJECT_INFORMATION_INDEX = 3
UOI_USER_SID: USER_OBJECT_INFORMATION_INDEX = 4
class USEROBJECTFLAGS(Structure):
    fInherit: win32more.Foundation.BOOL
    fReserved: win32more.Foundation.BOOL
    dwFlags: UInt32
@winfunctype_pointer
def WINSTAENUMPROCA(param0: win32more.Foundation.PSTR, param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def WINSTAENUMPROCW(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
make_head(_module, 'BSMINFO')
make_head(_module, 'DESKTOPENUMPROCA')
make_head(_module, 'DESKTOPENUMPROCW')
make_head(_module, 'USEROBJECTFLAGS')
make_head(_module, 'WINSTAENUMPROCA')
make_head(_module, 'WINSTAENUMPROCW')
__all__ = [
    "BROADCAST_SYSTEM_MESSAGE_FLAGS",
    "BROADCAST_SYSTEM_MESSAGE_INFO",
    "BSF_ALLOWSFW",
    "BSF_FLUSHDISK",
    "BSF_FORCEIFHUNG",
    "BSF_IGNORECURRENTTASK",
    "BSF_LUID",
    "BSF_NOHANG",
    "BSF_NOTIMEOUTIFNOTHUNG",
    "BSF_POSTMESSAGE",
    "BSF_QUERY",
    "BSF_RETURNHDESK",
    "BSF_SENDNOTIFYMESSAGE",
    "BSMINFO",
    "BSM_ALLCOMPONENTS",
    "BSM_ALLDESKTOPS",
    "BSM_APPLICATIONS",
    "BroadcastSystemMessageA",
    "BroadcastSystemMessageExA",
    "BroadcastSystemMessageExW",
    "BroadcastSystemMessageW",
    "CloseDesktop",
    "CloseWindowStation",
    "CreateDesktopA",
    "CreateDesktopExA",
    "CreateDesktopExW",
    "CreateDesktopW",
    "CreateWindowStationA",
    "CreateWindowStationW",
    "DESKTOPENUMPROCA",
    "DESKTOPENUMPROCW",
    "DESKTOP_ACCESS_FLAGS",
    "DESKTOP_CONTROL_FLAGS",
    "DESKTOP_CREATEMENU",
    "DESKTOP_CREATEWINDOW",
    "DESKTOP_DELETE",
    "DESKTOP_ENUMERATE",
    "DESKTOP_HOOKCONTROL",
    "DESKTOP_JOURNALPLAYBACK",
    "DESKTOP_JOURNALRECORD",
    "DESKTOP_READOBJECTS",
    "DESKTOP_READ_CONTROL",
    "DESKTOP_SWITCHDESKTOP",
    "DESKTOP_SYNCHRONIZE",
    "DESKTOP_WRITEOBJECTS",
    "DESKTOP_WRITE_DAC",
    "DESKTOP_WRITE_OWNER",
    "DF_ALLOWOTHERACCOUNTHOOK",
    "EnumDesktopWindows",
    "EnumDesktopsA",
    "EnumDesktopsW",
    "EnumWindowStationsA",
    "EnumWindowStationsW",
    "GetProcessWindowStation",
    "GetThreadDesktop",
    "GetUserObjectInformationA",
    "GetUserObjectInformationW",
    "HDESK",
    "HWINSTA",
    "OpenDesktopA",
    "OpenDesktopW",
    "OpenInputDesktop",
    "OpenWindowStationA",
    "OpenWindowStationW",
    "SetProcessWindowStation",
    "SetThreadDesktop",
    "SetUserObjectInformationA",
    "SetUserObjectInformationW",
    "SwitchDesktop",
    "UOI_FLAGS",
    "UOI_HEAPSIZE",
    "UOI_IO",
    "UOI_NAME",
    "UOI_TYPE",
    "UOI_USER_SID",
    "USEROBJECTFLAGS",
    "USER_OBJECT_INFORMATION_INDEX",
    "WINSTAENUMPROCA",
    "WINSTAENUMPROCW",
]
