from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.RestartManager
CCH_RM_SESSION_KEY: UInt32 = 32
CCH_RM_MAX_APP_NAME: UInt32 = 255
CCH_RM_MAX_SVC_NAME: UInt32 = 63
RM_INVALID_TS_SESSION: Int32 = -1
RM_INVALID_PROCESS: Int32 = -1
@winfunctype('rstrtmgr.dll')
def RmStartSession(pSessionHandle: POINTER(UInt32), dwSessionFlags: UInt32, strSessionKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('RstrtMgr.dll')
def RmJoinSession(pSessionHandle: POINTER(UInt32), strSessionKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('rstrtmgr.dll')
def RmEndSession(dwSessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('rstrtmgr.dll')
def RmRegisterResources(dwSessionHandle: UInt32, nFiles: UInt32, rgsFileNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), nApplications: UInt32, rgApplications: POINTER(win32more.Windows.Win32.System.RestartManager.RM_UNIQUE_PROCESS), nServices: UInt32, rgsServiceNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('rstrtmgr.dll')
def RmGetList(dwSessionHandle: UInt32, pnProcInfoNeeded: POINTER(UInt32), pnProcInfo: POINTER(UInt32), rgAffectedApps: POINTER(win32more.Windows.Win32.System.RestartManager.RM_PROCESS_INFO), lpdwRebootReasons: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('rstrtmgr.dll')
def RmShutdown(dwSessionHandle: UInt32, lActionFlags: UInt32, fnStatus: win32more.Windows.Win32.System.RestartManager.RM_WRITE_STATUS_CALLBACK) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('rstrtmgr.dll')
def RmRestart(dwSessionHandle: UInt32, dwRestartFlags: UInt32, fnStatus: win32more.Windows.Win32.System.RestartManager.RM_WRITE_STATUS_CALLBACK) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('RstrtMgr.dll')
def RmCancelCurrentTask(dwSessionHandle: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('RstrtMgr.dll')
def RmAddFilter(dwSessionHandle: UInt32, strModuleName: win32more.Windows.Win32.Foundation.PWSTR, pProcess: POINTER(win32more.Windows.Win32.System.RestartManager.RM_UNIQUE_PROCESS), strServiceShortName: win32more.Windows.Win32.Foundation.PWSTR, FilterAction: win32more.Windows.Win32.System.RestartManager.RM_FILTER_ACTION) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('RstrtMgr.dll')
def RmRemoveFilter(dwSessionHandle: UInt32, strModuleName: win32more.Windows.Win32.Foundation.PWSTR, pProcess: POINTER(win32more.Windows.Win32.System.RestartManager.RM_UNIQUE_PROCESS), strServiceShortName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('RstrtMgr.dll')
def RmGetFilterList(dwSessionHandle: UInt32, pbFilterBuf: POINTER(Byte), cbFilterBuf: UInt32, cbFilterBufNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RM_APP_STATUS = Int32
RM_APP_STATUS_RmStatusUnknown: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 0
RM_APP_STATUS_RmStatusRunning: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 1
RM_APP_STATUS_RmStatusStopped: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 2
RM_APP_STATUS_RmStatusStoppedOther: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 4
RM_APP_STATUS_RmStatusRestarted: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 8
RM_APP_STATUS_RmStatusErrorOnStop: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 16
RM_APP_STATUS_RmStatusErrorOnRestart: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 32
RM_APP_STATUS_RmStatusShutdownMasked: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 64
RM_APP_STATUS_RmStatusRestartMasked: win32more.Windows.Win32.System.RestartManager.RM_APP_STATUS = 128
RM_APP_TYPE = Int32
RM_APP_TYPE_RmUnknownApp: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 0
RM_APP_TYPE_RmMainWindow: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 1
RM_APP_TYPE_RmOtherWindow: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 2
RM_APP_TYPE_RmService: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 3
RM_APP_TYPE_RmExplorer: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 4
RM_APP_TYPE_RmConsole: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 5
RM_APP_TYPE_RmCritical: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE = 1000
RM_FILTER_ACTION = Int32
RM_FILTER_ACTION_RmInvalidFilterAction: win32more.Windows.Win32.System.RestartManager.RM_FILTER_ACTION = 0
RM_FILTER_ACTION_RmNoRestart: win32more.Windows.Win32.System.RestartManager.RM_FILTER_ACTION = 1
RM_FILTER_ACTION_RmNoShutdown: win32more.Windows.Win32.System.RestartManager.RM_FILTER_ACTION = 2
class RM_FILTER_INFO(EasyCastStructure):
    FilterAction: win32more.Windows.Win32.System.RestartManager.RM_FILTER_ACTION
    FilterTrigger: win32more.Windows.Win32.System.RestartManager.RM_FILTER_TRIGGER
    cbNextOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        strFilename: win32more.Windows.Win32.Foundation.PWSTR
        Process: win32more.Windows.Win32.System.RestartManager.RM_UNIQUE_PROCESS
        strServiceShortName: win32more.Windows.Win32.Foundation.PWSTR
RM_FILTER_TRIGGER = Int32
RM_FILTER_TRIGGER_RmFilterTriggerInvalid: win32more.Windows.Win32.System.RestartManager.RM_FILTER_TRIGGER = 0
RM_FILTER_TRIGGER_RmFilterTriggerFile: win32more.Windows.Win32.System.RestartManager.RM_FILTER_TRIGGER = 1
RM_FILTER_TRIGGER_RmFilterTriggerProcess: win32more.Windows.Win32.System.RestartManager.RM_FILTER_TRIGGER = 2
RM_FILTER_TRIGGER_RmFilterTriggerService: win32more.Windows.Win32.System.RestartManager.RM_FILTER_TRIGGER = 3
class RM_PROCESS_INFO(EasyCastStructure):
    Process: win32more.Windows.Win32.System.RestartManager.RM_UNIQUE_PROCESS
    strAppName: Char * 256
    strServiceShortName: Char * 64
    ApplicationType: win32more.Windows.Win32.System.RestartManager.RM_APP_TYPE
    AppStatus: UInt32
    TSSessionId: UInt32
    bRestartable: win32more.Windows.Win32.Foundation.BOOL
RM_REBOOT_REASON = Int32
RM_REBOOT_REASON_RmRebootReasonNone: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 0
RM_REBOOT_REASON_RmRebootReasonPermissionDenied: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 1
RM_REBOOT_REASON_RmRebootReasonSessionMismatch: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 2
RM_REBOOT_REASON_RmRebootReasonCriticalProcess: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 4
RM_REBOOT_REASON_RmRebootReasonCriticalService: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 8
RM_REBOOT_REASON_RmRebootReasonDetectedSelf: win32more.Windows.Win32.System.RestartManager.RM_REBOOT_REASON = 16
RM_SHUTDOWN_TYPE = Int32
RM_SHUTDOWN_TYPE_RmForceShutdown: win32more.Windows.Win32.System.RestartManager.RM_SHUTDOWN_TYPE = 1
RM_SHUTDOWN_TYPE_RmShutdownOnlyRegistered: win32more.Windows.Win32.System.RestartManager.RM_SHUTDOWN_TYPE = 16
class RM_UNIQUE_PROCESS(EasyCastStructure):
    dwProcessId: UInt32
    ProcessStartTime: win32more.Windows.Win32.Foundation.FILETIME
@winfunctype_pointer
def RM_WRITE_STATUS_CALLBACK(nPercentComplete: UInt32) -> Void: ...


make_ready(__name__)
