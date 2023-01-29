from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Restore
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MIN_EVENT: UInt32 = 100
BEGIN_NESTED_SYSTEM_CHANGE_NORP: UInt32 = 104
MAX_EVENT: UInt32 = 104
MIN_RPT: UInt32 = 0
DESKTOP_SETTING: UInt32 = 2
ACCESSIBILITY_SETTING: UInt32 = 3
OE_SETTING: UInt32 = 4
APPLICATION_RUN: UInt32 = 5
RESTORE: UInt32 = 6
CHECKPOINT: UInt32 = 7
WINDOWS_SHUTDOWN: UInt32 = 8
WINDOWS_BOOT: UInt32 = 9
FIRSTRUN: UInt32 = 11
BACKUP_RECOVERY: UInt32 = 14
BACKUP: UInt32 = 15
MANUAL_CHECKPOINT: UInt32 = 16
WINDOWS_UPDATE: UInt32 = 17
CRITICAL_UPDATE: UInt32 = 18
MAX_RPT: UInt32 = 18
MAX_DESC: UInt32 = 64
MAX_DESC_W: UInt32 = 256
@winfunctype('sfc.dll')
def SRSetRestorePointA(pRestorePtSpec: POINTER(win32more.System.Restore.RESTOREPOINTINFOA_head), pSMgrStatus: POINTER(win32more.System.Restore.STATEMGRSTATUS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('sfc.dll')
def SRSetRestorePointW(pRestorePtSpec: POINTER(win32more.System.Restore.RESTOREPOINTINFOW_head), pSMgrStatus: POINTER(win32more.System.Restore.STATEMGRSTATUS_head)) -> win32more.Foundation.BOOL: ...
RESTOREPOINTINFO_EVENT_TYPE = UInt32
BEGIN_NESTED_SYSTEM_CHANGE: RESTOREPOINTINFO_EVENT_TYPE = 102
BEGIN_SYSTEM_CHANGE: RESTOREPOINTINFO_EVENT_TYPE = 100
END_NESTED_SYSTEM_CHANGE: RESTOREPOINTINFO_EVENT_TYPE = 103
END_SYSTEM_CHANGE: RESTOREPOINTINFO_EVENT_TYPE = 101
RESTOREPOINTINFO_TYPE = UInt32
APPLICATION_INSTALL: RESTOREPOINTINFO_TYPE = 0
APPLICATION_UNINSTALL: RESTOREPOINTINFO_TYPE = 1
DEVICE_DRIVER_INSTALL: RESTOREPOINTINFO_TYPE = 10
MODIFY_SETTINGS: RESTOREPOINTINFO_TYPE = 12
CANCELLED_OPERATION: RESTOREPOINTINFO_TYPE = 13
class RESTOREPOINTINFOA(Structure):
    dwEventType: win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: win32more.Foundation.CHAR * 64
    _pack_ = 1
class RESTOREPOINTINFOEX(Structure):
    ftCreation: win32more.Foundation.FILETIME
    dwEventType: UInt32
    dwRestorePtType: UInt32
    dwRPNum: UInt32
    szDescription: Char * 256
    _pack_ = 1
class RESTOREPOINTINFOW(Structure):
    dwEventType: win32more.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: Char * 256
    _pack_ = 1
class STATEMGRSTATUS(Structure):
    nStatus: UInt32
    llSequenceNumber: Int64
    _pack_ = 1
make_head(_module, 'RESTOREPOINTINFOA')
make_head(_module, 'RESTOREPOINTINFOEX')
make_head(_module, 'RESTOREPOINTINFOW')
make_head(_module, 'STATEMGRSTATUS')
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
_arch_optional = [
]
