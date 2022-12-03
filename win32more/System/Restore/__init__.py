from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Restore
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
def _define_SRSetRestorePointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Restore.RESTOREPOINTINFOA_head),POINTER(win32more.System.Restore.STATEMGRSTATUS_head))(('SRSetRestorePointA', windll['sfc.dll']), ((1, 'pRestorePtSpec'),(1, 'pSMgrStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SRSetRestorePointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Restore.RESTOREPOINTINFOW_head),POINTER(win32more.System.Restore.STATEMGRSTATUS_head))(('SRSetRestorePointW', windll['sfc.dll']), ((1, 'pRestorePtSpec'),(1, 'pSMgrStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
RESTOREPOINTINFO_EVENT_TYPE = UInt32
BEGIN_NESTED_SYSTEM_CHANGE = 102
BEGIN_SYSTEM_CHANGE = 100
END_NESTED_SYSTEM_CHANGE = 103
END_SYSTEM_CHANGE = 101
RESTOREPOINTINFO_TYPE = UInt32
APPLICATION_INSTALL = 0
APPLICATION_UNINSTALL = 1
DEVICE_DRIVER_INSTALL = 10
MODIFY_SETTINGS = 12
CANCELLED_OPERATION = 13
def _define_RESTOREPOINTINFOA_head():
    class RESTOREPOINTINFOA(Structure):
        pass
    return RESTOREPOINTINFOA
def _define_RESTOREPOINTINFOA():
    RESTOREPOINTINFOA = win32more.System.Restore.RESTOREPOINTINFOA_head
    RESTOREPOINTINFOA._pack_ = 1
    RESTOREPOINTINFOA._fields_ = [
        ('dwEventType', win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE),
        ('dwRestorePtType', win32more.System.Restore.RESTOREPOINTINFO_TYPE),
        ('llSequenceNumber', Int64),
        ('szDescription', win32more.Foundation.CHAR * 64),
    ]
    return RESTOREPOINTINFOA
def _define_RESTOREPOINTINFOEX_head():
    class RESTOREPOINTINFOEX(Structure):
        pass
    return RESTOREPOINTINFOEX
def _define_RESTOREPOINTINFOEX():
    RESTOREPOINTINFOEX = win32more.System.Restore.RESTOREPOINTINFOEX_head
    RESTOREPOINTINFOEX._pack_ = 1
    RESTOREPOINTINFOEX._fields_ = [
        ('ftCreation', win32more.Foundation.FILETIME),
        ('dwEventType', UInt32),
        ('dwRestorePtType', UInt32),
        ('dwRPNum', UInt32),
        ('szDescription', Char * 256),
    ]
    return RESTOREPOINTINFOEX
def _define_RESTOREPOINTINFOW_head():
    class RESTOREPOINTINFOW(Structure):
        pass
    return RESTOREPOINTINFOW
def _define_RESTOREPOINTINFOW():
    RESTOREPOINTINFOW = win32more.System.Restore.RESTOREPOINTINFOW_head
    RESTOREPOINTINFOW._pack_ = 1
    RESTOREPOINTINFOW._fields_ = [
        ('dwEventType', win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE),
        ('dwRestorePtType', win32more.System.Restore.RESTOREPOINTINFO_TYPE),
        ('llSequenceNumber', Int64),
        ('szDescription', Char * 256),
    ]
    return RESTOREPOINTINFOW
def _define_STATEMGRSTATUS_head():
    class STATEMGRSTATUS(Structure):
        pass
    return STATEMGRSTATUS
def _define_STATEMGRSTATUS():
    STATEMGRSTATUS = win32more.System.Restore.STATEMGRSTATUS_head
    STATEMGRSTATUS._pack_ = 1
    STATEMGRSTATUS._fields_ = [
        ('nStatus', UInt32),
        ('llSequenceNumber', Int64),
    ]
    return STATEMGRSTATUS
__all__ = [
    "ACCESSIBILITY_SETTING",
    "APPLICATION_INSTALL",
    "APPLICATION_RUN",
    "APPLICATION_UNINSTALL",
    "BACKUP",
    "BACKUP_RECOVERY",
    "BEGIN_NESTED_SYSTEM_CHANGE",
    "BEGIN_NESTED_SYSTEM_CHANGE_NORP",
    "BEGIN_SYSTEM_CHANGE",
    "CANCELLED_OPERATION",
    "CHECKPOINT",
    "CRITICAL_UPDATE",
    "DESKTOP_SETTING",
    "DEVICE_DRIVER_INSTALL",
    "END_NESTED_SYSTEM_CHANGE",
    "END_SYSTEM_CHANGE",
    "FIRSTRUN",
    "MANUAL_CHECKPOINT",
    "MAX_DESC",
    "MAX_DESC_W",
    "MAX_EVENT",
    "MAX_RPT",
    "MIN_EVENT",
    "MIN_RPT",
    "MODIFY_SETTINGS",
    "OE_SETTING",
    "RESTORE",
    "RESTOREPOINTINFOA",
    "RESTOREPOINTINFOEX",
    "RESTOREPOINTINFOW",
    "RESTOREPOINTINFO_EVENT_TYPE",
    "RESTOREPOINTINFO_TYPE",
    "SRSetRestorePointA",
    "SRSetRestorePointW",
    "STATEMGRSTATUS",
    "WINDOWS_BOOT",
    "WINDOWS_SHUTDOWN",
    "WINDOWS_UPDATE",
]
