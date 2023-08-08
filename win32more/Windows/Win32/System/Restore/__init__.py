from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Restore
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def SRSetRestorePointA(pRestorePtSpec: POINTER(win32more.Windows.Win32.System.Restore.RESTOREPOINTINFOA_head), pSMgrStatus: POINTER(win32more.Windows.Win32.System.Restore.STATEMGRSTATUS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('sfc.dll')
def SRSetRestorePointW(pRestorePtSpec: POINTER(win32more.Windows.Win32.System.Restore.RESTOREPOINTINFOW_head), pSMgrStatus: POINTER(win32more.Windows.Win32.System.Restore.STATEMGRSTATUS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SrClient.dll')
def SRRemoveRestorePoint(dwRPNum: UInt32) -> UInt32: ...
class RESTOREPOINTINFOA(EasyCastStructure):
    dwEventType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 64
    _pack_ = 1
class RESTOREPOINTINFOEX(EasyCastStructure):
    ftCreation: win32more.Windows.Win32.Foundation.FILETIME
    dwEventType: UInt32
    dwRestorePtType: UInt32
    dwRPNum: UInt32
    szDescription: Char * 256
    _pack_ = 1
class RESTOREPOINTINFOW(EasyCastStructure):
    dwEventType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: Char * 256
    _pack_ = 1
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
class STATEMGRSTATUS(EasyCastStructure):
    nStatus: win32more.Windows.Win32.Foundation.WIN32_ERROR
    llSequenceNumber: Int64
    _pack_ = 1
make_head(_module, 'RESTOREPOINTINFOA')
make_head(_module, 'RESTOREPOINTINFOEX')
make_head(_module, 'RESTOREPOINTINFOW')
make_head(_module, 'STATEMGRSTATUS')
