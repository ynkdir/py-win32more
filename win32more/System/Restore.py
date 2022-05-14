from win32more import *
import win32more.System.Restore
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Restore, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Restore, name)
MIN_EVENT = 100
BEGIN_NESTED_SYSTEM_CHANGE_NORP = 104
MAX_EVENT = 104
MIN_RPT = 0
DESKTOP_SETTING = 2
ACCESSIBILITY_SETTING = 3
OE_SETTING = 4
APPLICATION_RUN = 5
RESTORE = 6
CHECKPOINT = 7
WINDOWS_SHUTDOWN = 8
WINDOWS_BOOT = 9
FIRSTRUN = 11
BACKUP_RECOVERY = 14
BACKUP = 15
MANUAL_CHECKPOINT = 16
WINDOWS_UPDATE = 17
CRITICAL_UPDATE = 18
MAX_RPT = 18
MAX_DESC = 64
MAX_DESC_W = 256
RESTOREPOINTINFO_TYPE = UInt32
APPLICATION_INSTALL = 0
APPLICATION_UNINSTALL = 1
DEVICE_DRIVER_INSTALL = 10
MODIFY_SETTINGS = 12
CANCELLED_OPERATION = 13
RESTOREPOINTINFO_EVENT_TYPE = UInt32
BEGIN_NESTED_SYSTEM_CHANGE = 102
BEGIN_SYSTEM_CHANGE = 100
END_NESTED_SYSTEM_CHANGE = 103
END_SYSTEM_CHANGE = 101
def _define_RESTOREPOINTINFOA_head():
    class RESTOREPOINTINFOA(Structure):
        pass
    return RESTOREPOINTINFOA
def _define_RESTOREPOINTINFOA():
    RESTOREPOINTINFOA = win32more.System.Restore.RESTOREPOINTINFOA_head
    RESTOREPOINTINFOA._pack_ = 1
    RESTOREPOINTINFOA._fields_ = [
        ("dwEventType", win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE),
        ("dwRestorePtType", win32more.System.Restore.RESTOREPOINTINFO_TYPE),
        ("llSequenceNumber", Int64),
        ("szDescription", win32more.Foundation.CHAR * 64),
    ]
    return RESTOREPOINTINFOA
def _define_RESTOREPOINTINFOW_head():
    class RESTOREPOINTINFOW(Structure):
        pass
    return RESTOREPOINTINFOW
def _define_RESTOREPOINTINFOW():
    RESTOREPOINTINFOW = win32more.System.Restore.RESTOREPOINTINFOW_head
    RESTOREPOINTINFOW._pack_ = 1
    RESTOREPOINTINFOW._fields_ = [
        ("dwEventType", win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE),
        ("dwRestorePtType", win32more.System.Restore.RESTOREPOINTINFO_TYPE),
        ("llSequenceNumber", Int64),
        ("szDescription", Char * 256),
    ]
    return RESTOREPOINTINFOW
def _define__RESTOREPTINFOEX_head():
    class _RESTOREPTINFOEX(Structure):
        pass
    return _RESTOREPTINFOEX
def _define__RESTOREPTINFOEX():
    _RESTOREPTINFOEX = win32more.System.Restore._RESTOREPTINFOEX_head
    _RESTOREPTINFOEX._pack_ = 1
    _RESTOREPTINFOEX._fields_ = [
        ("ftCreation", win32more.Foundation.FILETIME),
        ("dwEventType", UInt32),
        ("dwRestorePtType", UInt32),
        ("dwRPNum", UInt32),
        ("szDescription", Char * 256),
    ]
    return _RESTOREPTINFOEX
def _define_STATEMGRSTATUS_head():
    class STATEMGRSTATUS(Structure):
        pass
    return STATEMGRSTATUS
def _define_STATEMGRSTATUS():
    STATEMGRSTATUS = win32more.System.Restore.STATEMGRSTATUS_head
    STATEMGRSTATUS._pack_ = 1
    STATEMGRSTATUS._fields_ = [
        ("nStatus", UInt32),
        ("llSequenceNumber", Int64),
    ]
    return STATEMGRSTATUS
def _define_SRSetRestorePointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Restore.RESTOREPOINTINFOA_head),POINTER(win32more.System.Restore.STATEMGRSTATUS_head), use_last_error=False)(("SRSetRestorePointA", windll["sfc"]), ((1, 'pRestorePtSpec'),(1, 'pSMgrStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SRSetRestorePointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Restore.RESTOREPOINTINFOW_head),POINTER(win32more.System.Restore.STATEMGRSTATUS_head), use_last_error=False)(("SRSetRestorePointW", windll["sfc"]), ((1, 'pRestorePtSpec'),(1, 'pSMgrStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SRSetRestorePoint():
    return win32more.System.Restore.SRSetRestorePointW
__all__ = [
    "MIN_EVENT",
    "BEGIN_NESTED_SYSTEM_CHANGE_NORP",
    "MAX_EVENT",
    "MIN_RPT",
    "DESKTOP_SETTING",
    "ACCESSIBILITY_SETTING",
    "OE_SETTING",
    "APPLICATION_RUN",
    "RESTORE",
    "CHECKPOINT",
    "WINDOWS_SHUTDOWN",
    "WINDOWS_BOOT",
    "FIRSTRUN",
    "BACKUP_RECOVERY",
    "BACKUP",
    "MANUAL_CHECKPOINT",
    "WINDOWS_UPDATE",
    "CRITICAL_UPDATE",
    "MAX_RPT",
    "MAX_DESC",
    "MAX_DESC_W",
    "RESTOREPOINTINFO_TYPE",
    "APPLICATION_INSTALL",
    "APPLICATION_UNINSTALL",
    "DEVICE_DRIVER_INSTALL",
    "MODIFY_SETTINGS",
    "CANCELLED_OPERATION",
    "RESTOREPOINTINFO_EVENT_TYPE",
    "BEGIN_NESTED_SYSTEM_CHANGE",
    "BEGIN_SYSTEM_CHANGE",
    "END_NESTED_SYSTEM_CHANGE",
    "END_SYSTEM_CHANGE",
    "RESTOREPOINTINFOA",
    "RESTOREPOINTINFOW",
    "_RESTOREPTINFOEX",
    "STATEMGRSTATUS",
    "SRSetRestorePointA",
    "SRSetRestorePointW",
    "SRSetRestorePoint",
]
