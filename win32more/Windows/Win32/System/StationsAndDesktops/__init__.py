from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.StationsAndDesktops
import win32more.Windows.Win32.UI.WindowsAndMessaging
@winfunctype('USER32.dll')
def CreateDesktopA(lpszDesktop: win32more.Windows.Win32.Foundation.PSTR, lpszDevice: win32more.Windows.Win32.Foundation.PSTR, pDevmode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEA), dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopW(lpszDesktop: win32more.Windows.Win32.Foundation.PWSTR, lpszDevice: win32more.Windows.Win32.Foundation.PWSTR, pDevmode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEW), dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
CreateDesktop = UnicodeAlias('CreateDesktopW')
@winfunctype('USER32.dll')
def CreateDesktopExA(lpszDesktop: win32more.Windows.Win32.Foundation.PSTR, lpszDevice: win32more.Windows.Win32.Foundation.PSTR, pDevmode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEA), dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), ulHeapSize: UInt32, pvoid: VoidPtr) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateDesktopExW(lpszDesktop: win32more.Windows.Win32.Foundation.PWSTR, lpszDevice: win32more.Windows.Win32.Foundation.PWSTR, pDevmode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEW), dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), ulHeapSize: UInt32, pvoid: VoidPtr) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
CreateDesktopEx = UnicodeAlias('CreateDesktopExW')
@winfunctype('USER32.dll')
def OpenDesktopA(lpszDesktop: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def OpenDesktopW(lpszDesktop: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
OpenDesktop = UnicodeAlias('OpenDesktopW')
@winfunctype('USER32.dll')
def OpenInputDesktop(dwFlags: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS, fInherit: win32more.Windows.Win32.Foundation.BOOL, dwDesiredAccess: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def EnumDesktopsA(hwinsta: win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA, lpEnumFunc: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOPENUMPROCA, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumDesktopsW(hwinsta: win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA, lpEnumFunc: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOPENUMPROCW, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumDesktops = UnicodeAlias('EnumDesktopsW')
@winfunctype('USER32.dll')
def EnumDesktopWindows(hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK, lpfn: win32more.Windows.Win32.UI.WindowsAndMessaging.WNDENUMPROC, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SwitchDesktop(hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDesktop(hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseDesktop(hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetThreadDesktop(dwThreadId: UInt32) -> win32more.Windows.Win32.System.StationsAndDesktops.HDESK: ...
@winfunctype('USER32.dll')
def CreateWindowStationA(lpwinsta: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def CreateWindowStationW(lpwinsta: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwDesiredAccess: UInt32, lpsa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
CreateWindowStation = UnicodeAlias('CreateWindowStationW')
@winfunctype('USER32.dll')
def OpenWindowStationA(lpszWinSta: win32more.Windows.Win32.Foundation.PSTR, fInherit: win32more.Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def OpenWindowStationW(lpszWinSta: win32more.Windows.Win32.Foundation.PWSTR, fInherit: win32more.Windows.Win32.Foundation.BOOL, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
OpenWindowStation = UnicodeAlias('OpenWindowStationW')
@winfunctype('USER32.dll')
def EnumWindowStationsA(lpEnumFunc: win32more.Windows.Win32.System.StationsAndDesktops.WINSTAENUMPROCA, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnumWindowStationsW(lpEnumFunc: win32more.Windows.Win32.System.StationsAndDesktops.WINSTAENUMPROCW, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumWindowStations = UnicodeAlias('EnumWindowStationsW')
@winfunctype('USER32.dll')
def CloseWindowStation(hWinSta: win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessWindowStation(hWinSta: win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetProcessWindowStation() -> win32more.Windows.Win32.System.StationsAndDesktops.HWINSTA: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationA(hObj: win32more.Windows.Win32.Foundation.HANDLE, nIndex: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: VoidPtr, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUserObjectInformationW(hObj: win32more.Windows.Win32.Foundation.HANDLE, nIndex: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX, pvInfo: VoidPtr, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetUserObjectInformation = UnicodeAlias('GetUserObjectInformationW')
@winfunctype('USER32.dll')
def SetUserObjectInformationA(hObj: win32more.Windows.Win32.Foundation.HANDLE, nIndex: Int32, pvInfo: VoidPtr, nLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetUserObjectInformationW(hObj: win32more.Windows.Win32.Foundation.HANDLE, nIndex: Int32, pvInfo: VoidPtr, nLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetUserObjectInformation = UnicodeAlias('SetUserObjectInformationW')
@winfunctype('USER32.dll')
def BroadcastSystemMessageExA(flags: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pbsmInfo: POINTER(win32more.Windows.Win32.System.StationsAndDesktops.BSMINFO)) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageExW(flags: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pbsmInfo: POINTER(win32more.Windows.Win32.System.StationsAndDesktops.BSMINFO)) -> Int32: ...
BroadcastSystemMessageEx = UnicodeAlias('BroadcastSystemMessageExW')
@winfunctype('USER32.dll')
def BroadcastSystemMessageA(flags: UInt32, lpInfo: POINTER(UInt32), Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype('USER32.dll')
def BroadcastSystemMessageW(flags: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS, lpInfo: POINTER(win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO), Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
BroadcastSystemMessage = UnicodeAlias('BroadcastSystemMessageW')
BROADCAST_SYSTEM_MESSAGE_FLAGS = UInt32
BSF_ALLOWSFW: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 128
BSF_FLUSHDISK: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 4
BSF_FORCEIFHUNG: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 32
BSF_IGNORECURRENTTASK: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 2
BSF_NOHANG: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 8
BSF_NOTIMEOUTIFNOTHUNG: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 64
BSF_POSTMESSAGE: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 16
BSF_QUERY: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 1
BSF_SENDNOTIFYMESSAGE: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 256
BSF_LUID: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 1024
BSF_RETURNHDESK: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS = 512
BROADCAST_SYSTEM_MESSAGE_INFO = UInt32
BSM_ALLCOMPONENTS: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO = 0
BSM_ALLDESKTOPS: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO = 16
BSM_APPLICATIONS: win32more.Windows.Win32.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO = 8
class BSMINFO(Structure):
    cbSize: UInt32
    hdesk: win32more.Windows.Win32.System.StationsAndDesktops.HDESK
    hwnd: win32more.Windows.Win32.Foundation.HWND
    luid: win32more.Windows.Win32.Foundation.LUID
@winfunctype_pointer
def DESKTOPENUMPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def DESKTOPENUMPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
DESKTOPENUMPROC = UnicodeAlias('DESKTOPENUMPROCW')
DESKTOP_ACCESS_FLAGS = UInt32
DESKTOP_DELETE: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 65536
DESKTOP_READ_CONTROL: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 131072
DESKTOP_WRITE_DAC: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 262144
DESKTOP_WRITE_OWNER: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 524288
DESKTOP_SYNCHRONIZE: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 1048576
DESKTOP_READOBJECTS: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 1
DESKTOP_CREATEWINDOW: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 2
DESKTOP_CREATEMENU: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 4
DESKTOP_HOOKCONTROL: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 8
DESKTOP_JOURNALRECORD: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 16
DESKTOP_JOURNALPLAYBACK: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 32
DESKTOP_ENUMERATE: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 64
DESKTOP_WRITEOBJECTS: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 128
DESKTOP_SWITCHDESKTOP: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS = 256
DESKTOP_CONTROL_FLAGS = UInt32
DF_ALLOWOTHERACCOUNTHOOK: win32more.Windows.Win32.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS = 1
HDESK = VoidPtr
HWINSTA = VoidPtr
class USEROBJECTFLAGS(Structure):
    fInherit: win32more.Windows.Win32.Foundation.BOOL
    fReserved: win32more.Windows.Win32.Foundation.BOOL
    dwFlags: UInt32
USER_OBJECT_INFORMATION_INDEX = Int32
UOI_FLAGS: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 1
UOI_HEAPSIZE: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 5
UOI_IO: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 6
UOI_NAME: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 2
UOI_TYPE: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 3
UOI_USER_SID: win32more.Windows.Win32.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX = 4
@winfunctype_pointer
def WINSTAENUMPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def WINSTAENUMPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
WINSTAENUMPROC = UnicodeAlias('WINSTAENUMPROCW')


make_ready(__name__)
