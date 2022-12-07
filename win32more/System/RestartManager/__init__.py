from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.RestartManager
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CCH_RM_SESSION_KEY: UInt32 = 32
CCH_RM_MAX_APP_NAME: UInt32 = 255
CCH_RM_MAX_SVC_NAME: UInt32 = 63
RM_INVALID_TS_SESSION: Int32 = -1
RM_INVALID_PROCESS: Int32 = -1
@winfunctype('rstrtmgr.dll')
def RmStartSession(pSessionHandle: POINTER(UInt32), dwSessionFlags: UInt32, strSessionKey: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('RstrtMgr.dll')
def RmJoinSession(pSessionHandle: POINTER(UInt32), strSessionKey: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('rstrtmgr.dll')
def RmEndSession(dwSessionHandle: UInt32) -> UInt32: ...
@winfunctype('rstrtmgr.dll')
def RmRegisterResources(dwSessionHandle: UInt32, nFiles: UInt32, rgsFileNames: POINTER(win32more.Foundation.PWSTR), nApplications: UInt32, rgApplications: POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS_head), nServices: UInt32, rgsServiceNames: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('rstrtmgr.dll')
def RmGetList(dwSessionHandle: UInt32, pnProcInfoNeeded: POINTER(UInt32), pnProcInfo: POINTER(UInt32), rgAffectedApps: POINTER(win32more.System.RestartManager.RM_PROCESS_INFO_head), lpdwRebootReasons: POINTER(UInt32)) -> UInt32: ...
@winfunctype('rstrtmgr.dll')
def RmShutdown(dwSessionHandle: UInt32, lActionFlags: UInt32, fnStatus: win32more.System.RestartManager.RM_WRITE_STATUS_CALLBACK) -> UInt32: ...
@winfunctype('rstrtmgr.dll')
def RmRestart(dwSessionHandle: UInt32, dwRestartFlags: UInt32, fnStatus: win32more.System.RestartManager.RM_WRITE_STATUS_CALLBACK) -> UInt32: ...
@winfunctype('RstrtMgr.dll')
def RmCancelCurrentTask(dwSessionHandle: UInt32) -> UInt32: ...
@winfunctype('RstrtMgr.dll')
def RmAddFilter(dwSessionHandle: UInt32, strModuleName: win32more.Foundation.PWSTR, pProcess: POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS_head), strServiceShortName: win32more.Foundation.PWSTR, FilterAction: win32more.System.RestartManager.RM_FILTER_ACTION) -> UInt32: ...
@winfunctype('RstrtMgr.dll')
def RmRemoveFilter(dwSessionHandle: UInt32, strModuleName: win32more.Foundation.PWSTR, pProcess: POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS_head), strServiceShortName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('RstrtMgr.dll')
def RmGetFilterList(dwSessionHandle: UInt32, pbFilterBuf: c_char_p_no, cbFilterBuf: UInt32, cbFilterBufNeeded: POINTER(UInt32)) -> UInt32: ...
RM_APP_STATUS = Int32
RM_APP_STATUS_RmStatusUnknown: RM_APP_STATUS = 0
RM_APP_STATUS_RmStatusRunning: RM_APP_STATUS = 1
RM_APP_STATUS_RmStatusStopped: RM_APP_STATUS = 2
RM_APP_STATUS_RmStatusStoppedOther: RM_APP_STATUS = 4
RM_APP_STATUS_RmStatusRestarted: RM_APP_STATUS = 8
RM_APP_STATUS_RmStatusErrorOnStop: RM_APP_STATUS = 16
RM_APP_STATUS_RmStatusErrorOnRestart: RM_APP_STATUS = 32
RM_APP_STATUS_RmStatusShutdownMasked: RM_APP_STATUS = 64
RM_APP_STATUS_RmStatusRestartMasked: RM_APP_STATUS = 128
RM_APP_TYPE = Int32
RM_APP_TYPE_RmUnknownApp: RM_APP_TYPE = 0
RM_APP_TYPE_RmMainWindow: RM_APP_TYPE = 1
RM_APP_TYPE_RmOtherWindow: RM_APP_TYPE = 2
RM_APP_TYPE_RmService: RM_APP_TYPE = 3
RM_APP_TYPE_RmExplorer: RM_APP_TYPE = 4
RM_APP_TYPE_RmConsole: RM_APP_TYPE = 5
RM_APP_TYPE_RmCritical: RM_APP_TYPE = 1000
RM_FILTER_ACTION = Int32
RM_FILTER_ACTION_RmInvalidFilterAction: RM_FILTER_ACTION = 0
RM_FILTER_ACTION_RmNoRestart: RM_FILTER_ACTION = 1
RM_FILTER_ACTION_RmNoShutdown: RM_FILTER_ACTION = 2
class RM_FILTER_INFO(Structure):
    FilterAction: win32more.System.RestartManager.RM_FILTER_ACTION
    FilterTrigger: win32more.System.RestartManager.RM_FILTER_TRIGGER
    cbNextOffset: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        strFilename: win32more.Foundation.PWSTR
        Process: win32more.System.RestartManager.RM_UNIQUE_PROCESS
        strServiceShortName: win32more.Foundation.PWSTR
RM_FILTER_TRIGGER = Int32
RM_FILTER_TRIGGER_RmFilterTriggerInvalid: RM_FILTER_TRIGGER = 0
RM_FILTER_TRIGGER_RmFilterTriggerFile: RM_FILTER_TRIGGER = 1
RM_FILTER_TRIGGER_RmFilterTriggerProcess: RM_FILTER_TRIGGER = 2
RM_FILTER_TRIGGER_RmFilterTriggerService: RM_FILTER_TRIGGER = 3
class RM_PROCESS_INFO(Structure):
    Process: win32more.System.RestartManager.RM_UNIQUE_PROCESS
    strAppName: Char * 256
    strServiceShortName: Char * 64
    ApplicationType: win32more.System.RestartManager.RM_APP_TYPE
    AppStatus: UInt32
    TSSessionId: UInt32
    bRestartable: win32more.Foundation.BOOL
RM_REBOOT_REASON = Int32
RM_REBOOT_REASON_RmRebootReasonNone: RM_REBOOT_REASON = 0
RM_REBOOT_REASON_RmRebootReasonPermissionDenied: RM_REBOOT_REASON = 1
RM_REBOOT_REASON_RmRebootReasonSessionMismatch: RM_REBOOT_REASON = 2
RM_REBOOT_REASON_RmRebootReasonCriticalProcess: RM_REBOOT_REASON = 4
RM_REBOOT_REASON_RmRebootReasonCriticalService: RM_REBOOT_REASON = 8
RM_REBOOT_REASON_RmRebootReasonDetectedSelf: RM_REBOOT_REASON = 16
RM_SHUTDOWN_TYPE = Int32
RM_SHUTDOWN_TYPE_RmForceShutdown: RM_SHUTDOWN_TYPE = 1
RM_SHUTDOWN_TYPE_RmShutdownOnlyRegistered: RM_SHUTDOWN_TYPE = 16
class RM_UNIQUE_PROCESS(Structure):
    dwProcessId: UInt32
    ProcessStartTime: win32more.Foundation.FILETIME
@winfunctype_pointer
def RM_WRITE_STATUS_CALLBACK(nPercentComplete: UInt32) -> Void: ...
make_head(_module, 'RM_FILTER_INFO')
make_head(_module, 'RM_PROCESS_INFO')
make_head(_module, 'RM_UNIQUE_PROCESS')
make_head(_module, 'RM_WRITE_STATUS_CALLBACK')
__all__ = [
    "CCH_RM_MAX_APP_NAME",
    "CCH_RM_MAX_SVC_NAME",
    "CCH_RM_SESSION_KEY",
    "RM_APP_STATUS",
    "RM_APP_STATUS_RmStatusErrorOnRestart",
    "RM_APP_STATUS_RmStatusErrorOnStop",
    "RM_APP_STATUS_RmStatusRestartMasked",
    "RM_APP_STATUS_RmStatusRestarted",
    "RM_APP_STATUS_RmStatusRunning",
    "RM_APP_STATUS_RmStatusShutdownMasked",
    "RM_APP_STATUS_RmStatusStopped",
    "RM_APP_STATUS_RmStatusStoppedOther",
    "RM_APP_STATUS_RmStatusUnknown",
    "RM_APP_TYPE",
    "RM_APP_TYPE_RmConsole",
    "RM_APP_TYPE_RmCritical",
    "RM_APP_TYPE_RmExplorer",
    "RM_APP_TYPE_RmMainWindow",
    "RM_APP_TYPE_RmOtherWindow",
    "RM_APP_TYPE_RmService",
    "RM_APP_TYPE_RmUnknownApp",
    "RM_FILTER_ACTION",
    "RM_FILTER_ACTION_RmInvalidFilterAction",
    "RM_FILTER_ACTION_RmNoRestart",
    "RM_FILTER_ACTION_RmNoShutdown",
    "RM_FILTER_INFO",
    "RM_FILTER_TRIGGER",
    "RM_FILTER_TRIGGER_RmFilterTriggerFile",
    "RM_FILTER_TRIGGER_RmFilterTriggerInvalid",
    "RM_FILTER_TRIGGER_RmFilterTriggerProcess",
    "RM_FILTER_TRIGGER_RmFilterTriggerService",
    "RM_INVALID_PROCESS",
    "RM_INVALID_TS_SESSION",
    "RM_PROCESS_INFO",
    "RM_REBOOT_REASON",
    "RM_REBOOT_REASON_RmRebootReasonCriticalProcess",
    "RM_REBOOT_REASON_RmRebootReasonCriticalService",
    "RM_REBOOT_REASON_RmRebootReasonDetectedSelf",
    "RM_REBOOT_REASON_RmRebootReasonNone",
    "RM_REBOOT_REASON_RmRebootReasonPermissionDenied",
    "RM_REBOOT_REASON_RmRebootReasonSessionMismatch",
    "RM_SHUTDOWN_TYPE",
    "RM_SHUTDOWN_TYPE_RmForceShutdown",
    "RM_SHUTDOWN_TYPE_RmShutdownOnlyRegistered",
    "RM_UNIQUE_PROCESS",
    "RM_WRITE_STATUS_CALLBACK",
    "RmAddFilter",
    "RmCancelCurrentTask",
    "RmEndSession",
    "RmGetFilterList",
    "RmGetList",
    "RmJoinSession",
    "RmRegisterResources",
    "RmRemoveFilter",
    "RmRestart",
    "RmShutdown",
    "RmStartSession",
]
