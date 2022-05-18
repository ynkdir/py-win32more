from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Mailslots

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_CreateMailslotA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateMailslotA", windll["KERNEL32"]), ((1, 'lpName'),(1, 'nMaxMessageSize'),(1, 'lReadTimeout'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMailslotW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=True)(("CreateMailslotW", windll["KERNEL32"]), ((1, 'lpName'),(1, 'nMaxMessageSize'),(1, 'lReadTimeout'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMailslot():
    return win32more.System.Mailslots.CreateMailslotW
def _define_GetMailslotInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("GetMailslotInfo", windll["KERNEL32"]), ((1, 'hMailslot'),(1, 'lpMaxMessageSize'),(1, 'lpNextSize'),(1, 'lpMessageCount'),(1, 'lpReadTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMailslotInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("SetMailslotInfo", windll["KERNEL32"]), ((1, 'hMailslot'),(1, 'lReadTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CreateMailslotA",
    "CreateMailslotW",
    "CreateMailslot",
    "GetMailslotInfo",
    "SetMailslotInfo",
]
