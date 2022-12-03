from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.StationsAndDesktops
import win32more.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CreateDesktopA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDesktopA', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDesktopW', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopExA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,c_void_p)(('CreateDesktopExA', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),(1, 'ulHeapSize'),(1, 'pvoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopExW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,c_void_p)(('CreateDesktopExW', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),(1, 'ulHeapSize'),(1, 'pvoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenDesktopA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,win32more.Foundation.BOOL,UInt32)(('OpenDesktopA', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenDesktopW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,win32more.Foundation.BOOL,UInt32)(('OpenDesktopW', windll['USER32.dll']), ((1, 'lpszDesktop'),(1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenInputDesktop():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.System.StationsAndDesktops.DESKTOP_CONTROL_FLAGS,win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.DESKTOP_ACCESS_FLAGS)(('OpenInputDesktop', windll['USER32.dll']), ((1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktopsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA,win32more.System.StationsAndDesktops.DESKTOPENUMPROCA,win32more.Foundation.LPARAM)(('EnumDesktopsA', windll['USER32.dll']), ((1, 'hwinsta'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktopsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA,win32more.System.StationsAndDesktops.DESKTOPENUMPROCW,win32more.Foundation.LPARAM)(('EnumDesktopsW', windll['USER32.dll']), ((1, 'hwinsta'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktopWindows():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK,win32more.UI.WindowsAndMessaging.WNDENUMPROC,win32more.Foundation.LPARAM)(('EnumDesktopWindows', windll['USER32.dll']), ((1, 'hDesktop'),(1, 'lpfn'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwitchDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK)(('SwitchDesktop', windll['USER32.dll']), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK)(('SetThreadDesktop', windll['USER32.dll']), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK)(('CloseDesktop', windll['USER32.dll']), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDesktop():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,UInt32)(('GetThreadDesktop', windll['USER32.dll']), ((1, 'dwThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWindowStationA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateWindowStationA', windll['USER32.dll']), ((1, 'lpwinsta'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWindowStationW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateWindowStationW', windll['USER32.dll']), ((1, 'lpwinsta'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWindowStationA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PSTR,win32more.Foundation.BOOL,UInt32)(('OpenWindowStationA', windll['USER32.dll']), ((1, 'lpszWinSta'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWindowStationW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32)(('OpenWindowStationW', windll['USER32.dll']), ((1, 'lpszWinSta'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumWindowStationsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.WINSTAENUMPROCA,win32more.Foundation.LPARAM)(('EnumWindowStationsA', windll['USER32.dll']), ((1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumWindowStationsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.WINSTAENUMPROCW,win32more.Foundation.LPARAM)(('EnumWindowStationsW', windll['USER32.dll']), ((1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseWindowStation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA)(('CloseWindowStation', windll['USER32.dll']), ((1, 'hWinSta'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessWindowStation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA)(('SetProcessWindowStation', windll['USER32.dll']), ((1, 'hWinSta'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessWindowStation():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,)(('GetProcessWindowStation', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX,c_void_p,UInt32,POINTER(UInt32))(('GetUserObjectInformationA', windll['USER32.dll']), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX,c_void_p,UInt32,POINTER(UInt32))(('GetUserObjectInformationW', windll['USER32.dll']), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserObjectInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int32,c_void_p,UInt32)(('SetUserObjectInformationA', windll['USER32.dll']), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserObjectInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int32,c_void_p,UInt32)(('SetUserObjectInformationW', windll['USER32.dll']), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageExA():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.System.StationsAndDesktops.BSMINFO_head))(('BroadcastSystemMessageExA', windll['USER32.dll']), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),(1, 'pbsmInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageExW():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.System.StationsAndDesktops.BSMINFO_head))(('BroadcastSystemMessageExW', windll['USER32.dll']), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),(1, 'pbsmInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageA():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(('BroadcastSystemMessageA', windll['USER32.dll']), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageW():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(('BroadcastSystemMessageW', windll['USER32.dll']), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
BROADCAST_SYSTEM_MESSAGE_FLAGS = UInt32
BSF_ALLOWSFW = 128
BSF_FLUSHDISK = 4
BSF_FORCEIFHUNG = 32
BSF_IGNORECURRENTTASK = 2
BSF_NOHANG = 8
BSF_NOTIMEOUTIFNOTHUNG = 64
BSF_POSTMESSAGE = 16
BSF_QUERY = 1
BSF_SENDNOTIFYMESSAGE = 256
BSF_LUID = 1024
BSF_RETURNHDESK = 512
BROADCAST_SYSTEM_MESSAGE_INFO = UInt32
BSM_ALLCOMPONENTS = 0
BSM_ALLDESKTOPS = 16
BSM_APPLICATIONS = 8
def _define_BSMINFO_head():
    class BSMINFO(Structure):
        pass
    return BSMINFO
def _define_BSMINFO():
    BSMINFO = win32more.System.StationsAndDesktops.BSMINFO_head
    BSMINFO._fields_ = [
        ('cbSize', UInt32),
        ('hdesk', win32more.System.StationsAndDesktops.HDESK),
        ('hwnd', win32more.Foundation.HWND),
        ('luid', win32more.Foundation.LUID),
    ]
    return BSMINFO
DESKTOP_ACCESS_FLAGS = UInt32
DESKTOP_DELETE = 65536
DESKTOP_READ_CONTROL = 131072
DESKTOP_WRITE_DAC = 262144
DESKTOP_WRITE_OWNER = 524288
DESKTOP_SYNCHRONIZE = 1048576
DESKTOP_READOBJECTS = 1
DESKTOP_CREATEWINDOW = 2
DESKTOP_CREATEMENU = 4
DESKTOP_HOOKCONTROL = 8
DESKTOP_JOURNALRECORD = 16
DESKTOP_JOURNALPLAYBACK = 32
DESKTOP_ENUMERATE = 64
DESKTOP_WRITEOBJECTS = 128
DESKTOP_SWITCHDESKTOP = 256
DESKTOP_CONTROL_FLAGS = UInt32
DF_ALLOWOTHERACCOUNTHOOK = 1
def _define_DESKTOPENUMPROCA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.LPARAM)
def _define_DESKTOPENUMPROCW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.LPARAM)
HDESK = IntPtr
HWINSTA = IntPtr
USER_OBJECT_INFORMATION_INDEX = UInt32
UOI_FLAGS = 1
UOI_HEAPSIZE = 5
UOI_IO = 6
UOI_NAME = 2
UOI_TYPE = 3
UOI_USER_SID = 4
def _define_USEROBJECTFLAGS_head():
    class USEROBJECTFLAGS(Structure):
        pass
    return USEROBJECTFLAGS
def _define_USEROBJECTFLAGS():
    USEROBJECTFLAGS = win32more.System.StationsAndDesktops.USEROBJECTFLAGS_head
    USEROBJECTFLAGS._fields_ = [
        ('fInherit', win32more.Foundation.BOOL),
        ('fReserved', win32more.Foundation.BOOL),
        ('dwFlags', UInt32),
    ]
    return USEROBJECTFLAGS
def _define_WINSTAENUMPROCA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.LPARAM)
def _define_WINSTAENUMPROCW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.LPARAM)
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
