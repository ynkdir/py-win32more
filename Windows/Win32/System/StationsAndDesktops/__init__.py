from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security
import Windows.Win32.System.StationsAndDesktops
import Windows.Win32.UI.WindowsAndMessaging
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
def CreateDesktopA(lpszDesktop: Windows.Win32.Foundation.PSTR, lpszDevice: Windows.Win32.Foundation.PSTR, pDevmode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head), dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopW(lpszDesktop: Windows.Win32.Foundation.PWSTR, lpszDevice: Windows.Win32.Foundation.PWSTR, pDevmode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEW_head), dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopExA(lpszDesktop: Windows.Win32.Foundation.PSTR, lpszDevice: Windows.Win32.Foundation.PSTR, pDevmode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head), dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ulHeapSize: UInt32, pvoid: VoidPtr) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopExW(lpszDesktop: Windows.Win32.Foundation.PWSTR, lpszDevice: Windows.Win32.Foundation.PWSTR, pDevmode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEW_head), dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), ulHeapSize: UInt32, pvoid: VoidPtr) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenDesktopA(lpszDesktop: Windows.Win32.Foundation.PSTR, dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenDesktopW(lpszDesktop: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenInputDesktop(dwFlags: Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: Windows.Win32.Foundation.BOOL, dwDesiredAccess: Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def EnumDesktopsA(hwinsta: Windows.Win32.System.StationsAndDesktops.HWINSTA, lpEnumFunc: Windows.Win32.System.StationsAndDesktops.DESKTOPENUMPROCA, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumDesktopsW(hwinsta: Windows.Win32.System.StationsAndDesktops.HWINSTA, lpEnumFunc: Windows.Win32.System.StationsAndDesktops.DESKTOPENUMPROCW, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumDesktopWindows(hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK, lpfn: Windows.Win32.UI.WindowsAndMessaging.WNDENUMPROC, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SwitchDesktop(hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDesktop(hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseDesktop(hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetThreadDesktop(dwThreadId: UInt32) -> Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateWindowStationA(lpwinsta: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def CreateWindowStationW(lpwinsta: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def OpenWindowStationA(lpszWinSta: Windows.Win32.Foundation.PSTR, fInherit: Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def OpenWindowStationW(lpszWinSta: Windows.Win32.Foundation.PWSTR, fInherit: Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def EnumWindowStationsA(lpEnumFunc: Windows.Win32.System.StationsAndDesktops.WINSTAENUMPROCA, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumWindowStationsW(lpEnumFunc: Windows.Win32.System.StationsAndDesktops.WINSTAENUMPROCW, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseWindowStation(hWinSta: Windows.Win32.System.StationsAndDesktops.HWINSTA) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessWindowStation(hWinSta: Windows.Win32.System.StationsAndDesktops.HWINSTA) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetProcessWindowStation() -> Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationA(hObj: Windows.Win32.Foundation.HANDLE, nIndex: Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: VoidPtr, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationW(hObj: Windows.Win32.Foundation.HANDLE, nIndex: Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: VoidPtr, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetUserObjectInformationA(hObj: Windows.Win32.Foundation.HANDLE, nIndex: Int32, pvInfo: VoidPtr, nLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetUserObjectInformationW(hObj: Windows.Win32.Foundation.HANDLE, nIndex: Int32, pvInfo: VoidPtr, nLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageExA(flags: Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pbsmInfo: POINTER(Windows.Win32.System.StationsAndDesktops.BSMINFO_head)) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageExW(flags: Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pbsmInfo: POINTER(Windows.Win32.System.StationsAndDesktops.BSMINFO_head)) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageA(flags: UInt32, lpInfo: POINTER(UInt32), Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageW(flags: Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Int32: ...
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
class BSMINFO(EasyCastStructure):
    cbSize: UInt32
    hdesk: Windows.Win32.System.StationsAndDesktops.HDESK
    hwnd: Windows.Win32.Foundation.HWND
    luid: Windows.Win32.Foundation.LUID
@winfunctype_pointer
def DESKTOPENUMPROCA(param0: Windows.Win32.Foundation.PSTR, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def DESKTOPENUMPROCW(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
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
HDESK = IntPtr
HWINSTA = IntPtr
class USEROBJECTFLAGS(EasyCastStructure):
    fInherit: Windows.Win32.Foundation.BOOL
    fReserved: Windows.Win32.Foundation.BOOL
    dwFlags: UInt32
USER_OBJECT_INFORMATION_INDEX = Int32
UOI_FLAGS: USER_OBJECT_INFORMATION_INDEX = 1
UOI_HEAPSIZE: USER_OBJECT_INFORMATION_INDEX = 5
UOI_IO: USER_OBJECT_INFORMATION_INDEX = 6
UOI_NAME: USER_OBJECT_INFORMATION_INDEX = 2
UOI_TYPE: USER_OBJECT_INFORMATION_INDEX = 3
UOI_USER_SID: USER_OBJECT_INFORMATION_INDEX = 4
@winfunctype_pointer
def WINSTAENUMPROCA(param0: Windows.Win32.Foundation.PSTR, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def WINSTAENUMPROCW(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'BSMINFO')
make_head(_module, 'DESKTOPENUMPROCA')
make_head(_module, 'DESKTOPENUMPROCW')
make_head(_module, 'USEROBJECTFLAGS')
make_head(_module, 'WINSTAENUMPROCA')
make_head(_module, 'WINSTAENUMPROCW')
