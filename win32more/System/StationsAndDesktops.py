from win32more import *
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.StationsAndDesktops
import win32more.UI.WindowsAndMessaging

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
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
USER_OBJECT_INFORMATION_INDEX = UInt32
UOI_FLAGS = 1
UOI_HEAPSIZE = 5
UOI_IO = 6
UOI_NAME = 2
UOI_TYPE = 3
UOI_USER_SID = 4
def _define_WINSTAENUMPROCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.LPARAM, use_last_error=False)
def _define_WINSTAENUMPROCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.LPARAM, use_last_error=False)
def _define_DESKTOPENUMPROCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.LPARAM, use_last_error=False)
def _define_DESKTOPENUMPROCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.LPARAM, use_last_error=False)
HWINSTA = IntPtr
HDESK = IntPtr
def _define_USEROBJECTFLAGS_head():
    class USEROBJECTFLAGS(Structure):
        pass
    return USEROBJECTFLAGS
def _define_USEROBJECTFLAGS():
    USEROBJECTFLAGS = win32more.System.StationsAndDesktops.USEROBJECTFLAGS_head
    USEROBJECTFLAGS._fields_ = [
        ("fInherit", win32more.Foundation.BOOL),
        ("fReserved", win32more.Foundation.BOOL),
        ("dwFlags", UInt32),
    ]
    return USEROBJECTFLAGS
def _define_BSMINFO_head():
    class BSMINFO(Structure):
        pass
    return BSMINFO
def _define_BSMINFO():
    BSMINFO = win32more.System.StationsAndDesktops.BSMINFO_head
    BSMINFO._fields_ = [
        ("cbSize", UInt32),
        ("hdesk", win32more.System.StationsAndDesktops.HDESK),
        ("hwnd", win32more.Foundation.HWND),
        ("luid", win32more.Foundation.LUID),
    ]
    return BSMINFO
def _define_CreateDesktopA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateDesktopA", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateDesktopW", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktop():
    return win32more.System.StationsAndDesktops.CreateDesktopW
def _define_CreateDesktopExA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,c_void_p, use_last_error=True)(("CreateDesktopExA", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),(1, 'ulHeapSize'),(1, 'pvoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopExW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,c_void_p, use_last_error=True)(("CreateDesktopExW", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'lpszDevice'),(1, 'pDevmode'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),(1, 'ulHeapSize'),(1, 'pvoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDesktopEx():
    return win32more.System.StationsAndDesktops.CreateDesktopExW
def _define_OpenDesktopA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PSTR,UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=True)(("OpenDesktopA", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenDesktopW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=True)(("OpenDesktopW", windll["USER32"]), ((1, 'lpszDesktop'),(1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenDesktop():
    return win32more.System.StationsAndDesktops.OpenDesktopW
def _define_OpenInputDesktop():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=True)(("OpenInputDesktop", windll["USER32"]), ((1, 'dwFlags'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktopsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA,win32more.System.StationsAndDesktops.DESKTOPENUMPROCA,win32more.Foundation.LPARAM, use_last_error=True)(("EnumDesktopsA", windll["USER32"]), ((1, 'hwinsta'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktopsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA,win32more.System.StationsAndDesktops.DESKTOPENUMPROCW,win32more.Foundation.LPARAM, use_last_error=True)(("EnumDesktopsW", windll["USER32"]), ((1, 'hwinsta'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDesktops():
    return win32more.System.StationsAndDesktops.EnumDesktopsW
def _define_EnumDesktopWindows():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK,win32more.UI.WindowsAndMessaging.WNDENUMPROC,win32more.Foundation.LPARAM, use_last_error=True)(("EnumDesktopWindows", windll["USER32"]), ((1, 'hDesktop'),(1, 'lpfn'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwitchDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK, use_last_error=True)(("SwitchDesktop", windll["USER32"]), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK, use_last_error=True)(("SetThreadDesktop", windll["USER32"]), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HDESK, use_last_error=True)(("CloseDesktop", windll["USER32"]), ((1, 'hDesktop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDesktop():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HDESK,UInt32, use_last_error=True)(("GetThreadDesktop", windll["USER32"]), ((1, 'dwThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWindowStationA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateWindowStationA", windll["USER32"]), ((1, 'lpwinsta'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWindowStationW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateWindowStationW", windll["USER32"]), ((1, 'lpwinsta'),(1, 'dwFlags'),(1, 'dwDesiredAccess'),(1, 'lpsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWindowStation():
    return win32more.System.StationsAndDesktops.CreateWindowStationW
def _define_OpenWindowStationA():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PSTR,win32more.Foundation.BOOL,UInt32, use_last_error=True)(("OpenWindowStationA", windll["USER32"]), ((1, 'lpszWinSta'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWindowStationW():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32, use_last_error=True)(("OpenWindowStationW", windll["USER32"]), ((1, 'lpszWinSta'),(1, 'fInherit'),(1, 'dwDesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenWindowStation():
    return win32more.System.StationsAndDesktops.OpenWindowStationW
def _define_EnumWindowStationsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.WINSTAENUMPROCA,win32more.Foundation.LPARAM, use_last_error=True)(("EnumWindowStationsA", windll["USER32"]), ((1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumWindowStationsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.WINSTAENUMPROCW,win32more.Foundation.LPARAM, use_last_error=True)(("EnumWindowStationsW", windll["USER32"]), ((1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumWindowStations():
    return win32more.System.StationsAndDesktops.EnumWindowStationsW
def _define_CloseWindowStation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA, use_last_error=True)(("CloseWindowStation", windll["USER32"]), ((1, 'hWinSta'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessWindowStation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.StationsAndDesktops.HWINSTA, use_last_error=True)(("SetProcessWindowStation", windll["USER32"]), ((1, 'hWinSta'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessWindowStation():
    try:
        return WINFUNCTYPE(win32more.System.StationsAndDesktops.HWINSTA, use_last_error=True)(("GetProcessWindowStation", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("GetUserObjectInformationA", windll["USER32"]), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.StationsAndDesktops.USER_OBJECT_INFORMATION_INDEX,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("GetUserObjectInformationW", windll["USER32"]), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectInformation():
    return win32more.System.StationsAndDesktops.GetUserObjectInformationW
def _define_SetUserObjectInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int32,c_void_p,UInt32, use_last_error=True)(("SetUserObjectInformationA", windll["USER32"]), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserObjectInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int32,c_void_p,UInt32, use_last_error=True)(("SetUserObjectInformationW", windll["USER32"]), ((1, 'hObj'),(1, 'nIndex'),(1, 'pvInfo'),(1, 'nLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserObjectInformation():
    return win32more.System.StationsAndDesktops.SetUserObjectInformationW
def _define_BroadcastSystemMessageExA():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.System.StationsAndDesktops.BSMINFO_head), use_last_error=True)(("BroadcastSystemMessageExA", windll["USER32"]), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),(1, 'pbsmInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageExW():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.System.StationsAndDesktops.BSMINFO_head), use_last_error=True)(("BroadcastSystemMessageExW", windll["USER32"]), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),(1, 'pbsmInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageEx():
    return win32more.System.StationsAndDesktops.BroadcastSystemMessageExW
def _define_BroadcastSystemMessageA():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(("BroadcastSystemMessageA", windll["USER32"]), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessageW():
    try:
        return WINFUNCTYPE(Int32,win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_FLAGS,POINTER(win32more.System.StationsAndDesktops.BROADCAST_SYSTEM_MESSAGE_INFO),UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=True)(("BroadcastSystemMessageW", windll["USER32"]), ((1, 'flags'),(1, 'lpInfo'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BroadcastSystemMessage():
    return win32more.System.StationsAndDesktops.BroadcastSystemMessageW
__all__ = [
    "BROADCAST_SYSTEM_MESSAGE_FLAGS",
    "BSF_ALLOWSFW",
    "BSF_FLUSHDISK",
    "BSF_FORCEIFHUNG",
    "BSF_IGNORECURRENTTASK",
    "BSF_NOHANG",
    "BSF_NOTIMEOUTIFNOTHUNG",
    "BSF_POSTMESSAGE",
    "BSF_QUERY",
    "BSF_SENDNOTIFYMESSAGE",
    "BSF_LUID",
    "BSF_RETURNHDESK",
    "BROADCAST_SYSTEM_MESSAGE_INFO",
    "BSM_ALLCOMPONENTS",
    "BSM_ALLDESKTOPS",
    "BSM_APPLICATIONS",
    "USER_OBJECT_INFORMATION_INDEX",
    "UOI_FLAGS",
    "UOI_HEAPSIZE",
    "UOI_IO",
    "UOI_NAME",
    "UOI_TYPE",
    "UOI_USER_SID",
    "WINSTAENUMPROCA",
    "WINSTAENUMPROCW",
    "DESKTOPENUMPROCA",
    "DESKTOPENUMPROCW",
    "HWINSTA",
    "HDESK",
    "USEROBJECTFLAGS",
    "BSMINFO",
    "CreateDesktopA",
    "CreateDesktopW",
    "CreateDesktop",
    "CreateDesktopExA",
    "CreateDesktopExW",
    "CreateDesktopEx",
    "OpenDesktopA",
    "OpenDesktopW",
    "OpenDesktop",
    "OpenInputDesktop",
    "EnumDesktopsA",
    "EnumDesktopsW",
    "EnumDesktops",
    "EnumDesktopWindows",
    "SwitchDesktop",
    "SetThreadDesktop",
    "CloseDesktop",
    "GetThreadDesktop",
    "CreateWindowStationA",
    "CreateWindowStationW",
    "CreateWindowStation",
    "OpenWindowStationA",
    "OpenWindowStationW",
    "OpenWindowStation",
    "EnumWindowStationsA",
    "EnumWindowStationsW",
    "EnumWindowStations",
    "CloseWindowStation",
    "SetProcessWindowStation",
    "GetProcessWindowStation",
    "GetUserObjectInformationA",
    "GetUserObjectInformationW",
    "GetUserObjectInformation",
    "SetUserObjectInformationA",
    "SetUserObjectInformationW",
    "SetUserObjectInformation",
    "BroadcastSystemMessageExA",
    "BroadcastSystemMessageExW",
    "BroadcastSystemMessageEx",
    "BroadcastSystemMessageA",
    "BroadcastSystemMessageW",
    "BroadcastSystemMessage",
]
