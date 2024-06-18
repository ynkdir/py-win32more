from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Restore
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
def SRSetRestorePointA(pRestorePtSpec: POINTER(win32more.Windows.Win32.System.Restore.RESTOREPOINTINFOA), pSMgrStatus: POINTER(win32more.Windows.Win32.System.Restore.STATEMGRSTATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('sfc.dll')
def SRSetRestorePointW(pRestorePtSpec: POINTER(win32more.Windows.Win32.System.Restore.RESTOREPOINTINFOW), pSMgrStatus: POINTER(win32more.Windows.Win32.System.Restore.STATEMGRSTATUS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SRSetRestorePoint = UnicodeAlias('SRSetRestorePointW')
@winfunctype('SrClient.dll')
def SRRemoveRestorePoint(dwRPNum: UInt32) -> UInt32: ...
class RESTOREPOINTINFOA(Structure):
    dwEventType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 64
    _pack_ = 1
class RESTOREPOINTINFOEX(Structure):
    ftCreation: win32more.Windows.Win32.Foundation.FILETIME
    dwEventType: UInt32
    dwRestorePtType: UInt32
    dwRPNum: UInt32
    szDescription: Char * 256
    _pack_ = 1
class RESTOREPOINTINFOW(Structure):
    dwEventType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE
    dwRestorePtType: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE
    llSequenceNumber: Int64
    szDescription: Char * 256
    _pack_ = 1
RESTOREPOINTINFO = UnicodeAlias('RESTOREPOINTINFOW')
RESTOREPOINTINFO_EVENT_TYPE = UInt32
BEGIN_NESTED_SYSTEM_CHANGE: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE = 102
BEGIN_SYSTEM_CHANGE: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE = 100
END_NESTED_SYSTEM_CHANGE: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE = 103
END_SYSTEM_CHANGE: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_EVENT_TYPE = 101
RESTOREPOINTINFO_TYPE = UInt32
APPLICATION_INSTALL: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE = 0
APPLICATION_UNINSTALL: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE = 1
DEVICE_DRIVER_INSTALL: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE = 10
MODIFY_SETTINGS: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE = 12
CANCELLED_OPERATION: win32more.Windows.Win32.System.Restore.RESTOREPOINTINFO_TYPE = 13
class STATEMGRSTATUS(Structure):
    nStatus: win32more.Windows.Win32.Foundation.WIN32_ERROR
    llSequenceNumber: Int64
    _pack_ = 1


make_ready(__name__)
