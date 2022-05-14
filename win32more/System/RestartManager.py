from win32more import *
import win32more.System.RestartManager
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.RestartManager, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.RestartManager, name)
CCH_RM_SESSION_KEY = 32
CCH_RM_MAX_APP_NAME = 255
CCH_RM_MAX_SVC_NAME = 63
RM_INVALID_TS_SESSION = -1
RM_INVALID_PROCESS = -1
RM_APP_TYPE = Int32
RM_APP_TYPE_RmUnknownApp = 0
RM_APP_TYPE_RmMainWindow = 1
RM_APP_TYPE_RmOtherWindow = 2
RM_APP_TYPE_RmService = 3
RM_APP_TYPE_RmExplorer = 4
RM_APP_TYPE_RmConsole = 5
RM_APP_TYPE_RmCritical = 1000
RM_SHUTDOWN_TYPE = Int32
RM_SHUTDOWN_TYPE_RmForceShutdown = 1
RM_SHUTDOWN_TYPE_RmShutdownOnlyRegistered = 16
RM_APP_STATUS = Int32
RM_APP_STATUS_RmStatusUnknown = 0
RM_APP_STATUS_RmStatusRunning = 1
RM_APP_STATUS_RmStatusStopped = 2
RM_APP_STATUS_RmStatusStoppedOther = 4
RM_APP_STATUS_RmStatusRestarted = 8
RM_APP_STATUS_RmStatusErrorOnStop = 16
RM_APP_STATUS_RmStatusErrorOnRestart = 32
RM_APP_STATUS_RmStatusShutdownMasked = 64
RM_APP_STATUS_RmStatusRestartMasked = 128
RM_REBOOT_REASON = Int32
RM_REBOOT_REASON_RmRebootReasonNone = 0
RM_REBOOT_REASON_RmRebootReasonPermissionDenied = 1
RM_REBOOT_REASON_RmRebootReasonSessionMismatch = 2
RM_REBOOT_REASON_RmRebootReasonCriticalProcess = 4
RM_REBOOT_REASON_RmRebootReasonCriticalService = 8
RM_REBOOT_REASON_RmRebootReasonDetectedSelf = 16
def _define_RM_UNIQUE_PROCESS_head():
    class RM_UNIQUE_PROCESS(Structure):
        pass
    return RM_UNIQUE_PROCESS
def _define_RM_UNIQUE_PROCESS():
    RM_UNIQUE_PROCESS = win32more.System.RestartManager.RM_UNIQUE_PROCESS_head
    RM_UNIQUE_PROCESS._fields_ = [
        ("dwProcessId", UInt32),
        ("ProcessStartTime", win32more.Foundation.FILETIME),
    ]
    return RM_UNIQUE_PROCESS
def _define_RM_PROCESS_INFO_head():
    class RM_PROCESS_INFO(Structure):
        pass
    return RM_PROCESS_INFO
def _define_RM_PROCESS_INFO():
    RM_PROCESS_INFO = win32more.System.RestartManager.RM_PROCESS_INFO_head
    RM_PROCESS_INFO._fields_ = [
        ("Process", win32more.System.RestartManager.RM_UNIQUE_PROCESS),
        ("strAppName", Char * 256),
        ("strServiceShortName", Char * 64),
        ("ApplicationType", win32more.System.RestartManager.RM_APP_TYPE),
        ("AppStatus", UInt32),
        ("TSSessionId", UInt32),
        ("bRestartable", win32more.Foundation.BOOL),
    ]
    return RM_PROCESS_INFO
RM_FILTER_TRIGGER = Int32
RM_FILTER_TRIGGER_RmFilterTriggerInvalid = 0
RM_FILTER_TRIGGER_RmFilterTriggerFile = 1
RM_FILTER_TRIGGER_RmFilterTriggerProcess = 2
RM_FILTER_TRIGGER_RmFilterTriggerService = 3
RM_FILTER_ACTION = Int32
RM_FILTER_ACTION_RmInvalidFilterAction = 0
RM_FILTER_ACTION_RmNoRestart = 1
RM_FILTER_ACTION_RmNoShutdown = 2
def _define_RM_FILTER_INFO_head():
    class RM_FILTER_INFO(Structure):
        pass
    return RM_FILTER_INFO
def _define_RM_FILTER_INFO():
    RM_FILTER_INFO = win32more.System.RestartManager.RM_FILTER_INFO_head
    class RM_FILTER_INFO__Anonymous_e__Union(Union):
        pass
    RM_FILTER_INFO__Anonymous_e__Union._fields_ = [
        ("strFilename", win32more.Foundation.PWSTR),
        ("Process", win32more.System.RestartManager.RM_UNIQUE_PROCESS),
        ("strServiceShortName", win32more.Foundation.PWSTR),
    ]
    RM_FILTER_INFO._anonymous_ = [
        'Anonymous',
    ]
    RM_FILTER_INFO._fields_ = [
        ("FilterAction", win32more.System.RestartManager.RM_FILTER_ACTION),
        ("FilterTrigger", win32more.System.RestartManager.RM_FILTER_TRIGGER),
        ("cbNextOffset", UInt32),
        ("Anonymous", RM_FILTER_INFO__Anonymous_e__Union),
    ]
    return RM_FILTER_INFO
def _define_RM_WRITE_STATUS_CALLBACK():
    return CFUNCTYPE(Void,UInt32, use_last_error=False)
def _define_RmStartSession():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RmStartSession", windll["rstrtmgr"]), ((1, 'pSessionHandle'),(1, 'dwSessionFlags'),(1, 'strSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmJoinSession():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.Foundation.PWSTR, use_last_error=False)(("RmJoinSession", windll["RstrtMgr"]), ((1, 'pSessionHandle'),(1, 'strSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmEndSession():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("RmEndSession", windll["rstrtmgr"]), ((1, 'dwSessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmRegisterResources():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS),UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("RmRegisterResources", windll["rstrtmgr"]), ((1, 'dwSessionHandle'),(1, 'nFiles'),(1, 'rgsFileNames'),(1, 'nApplications'),(1, 'rgApplications'),(1, 'nServices'),(1, 'rgsServiceNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmGetList():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.RestartManager.RM_PROCESS_INFO),POINTER(UInt32), use_last_error=False)(("RmGetList", windll["rstrtmgr"]), ((1, 'dwSessionHandle'),(1, 'pnProcInfoNeeded'),(1, 'pnProcInfo'),(1, 'rgAffectedApps'),(1, 'lpdwRebootReasons'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmShutdown():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.System.RestartManager.RM_WRITE_STATUS_CALLBACK, use_last_error=False)(("RmShutdown", windll["rstrtmgr"]), ((1, 'dwSessionHandle'),(1, 'lActionFlags'),(1, 'fnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmRestart():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.System.RestartManager.RM_WRITE_STATUS_CALLBACK, use_last_error=False)(("RmRestart", windll["rstrtmgr"]), ((1, 'dwSessionHandle'),(1, 'dwRestartFlags'),(1, 'fnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmCancelCurrentTask():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("RmCancelCurrentTask", windll["RstrtMgr"]), ((1, 'dwSessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmAddFilter():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS_head),win32more.Foundation.PWSTR,win32more.System.RestartManager.RM_FILTER_ACTION, use_last_error=False)(("RmAddFilter", windll["RstrtMgr"]), ((1, 'dwSessionHandle'),(1, 'strModuleName'),(1, 'pProcess'),(1, 'strServiceShortName'),(1, 'FilterAction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmRemoveFilter():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.RestartManager.RM_UNIQUE_PROCESS_head),win32more.Foundation.PWSTR, use_last_error=False)(("RmRemoveFilter", windll["RstrtMgr"]), ((1, 'dwSessionHandle'),(1, 'strModuleName'),(1, 'pProcess'),(1, 'strServiceShortName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RmGetFilterList():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(("RmGetFilterList", windll["RstrtMgr"]), ((1, 'dwSessionHandle'),(1, 'pbFilterBuf'),(1, 'cbFilterBuf'),(1, 'cbFilterBufNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CCH_RM_SESSION_KEY",
    "CCH_RM_MAX_APP_NAME",
    "CCH_RM_MAX_SVC_NAME",
    "RM_INVALID_TS_SESSION",
    "RM_INVALID_PROCESS",
    "RM_APP_TYPE",
    "RM_APP_TYPE_RmUnknownApp",
    "RM_APP_TYPE_RmMainWindow",
    "RM_APP_TYPE_RmOtherWindow",
    "RM_APP_TYPE_RmService",
    "RM_APP_TYPE_RmExplorer",
    "RM_APP_TYPE_RmConsole",
    "RM_APP_TYPE_RmCritical",
    "RM_SHUTDOWN_TYPE",
    "RM_SHUTDOWN_TYPE_RmForceShutdown",
    "RM_SHUTDOWN_TYPE_RmShutdownOnlyRegistered",
    "RM_APP_STATUS",
    "RM_APP_STATUS_RmStatusUnknown",
    "RM_APP_STATUS_RmStatusRunning",
    "RM_APP_STATUS_RmStatusStopped",
    "RM_APP_STATUS_RmStatusStoppedOther",
    "RM_APP_STATUS_RmStatusRestarted",
    "RM_APP_STATUS_RmStatusErrorOnStop",
    "RM_APP_STATUS_RmStatusErrorOnRestart",
    "RM_APP_STATUS_RmStatusShutdownMasked",
    "RM_APP_STATUS_RmStatusRestartMasked",
    "RM_REBOOT_REASON",
    "RM_REBOOT_REASON_RmRebootReasonNone",
    "RM_REBOOT_REASON_RmRebootReasonPermissionDenied",
    "RM_REBOOT_REASON_RmRebootReasonSessionMismatch",
    "RM_REBOOT_REASON_RmRebootReasonCriticalProcess",
    "RM_REBOOT_REASON_RmRebootReasonCriticalService",
    "RM_REBOOT_REASON_RmRebootReasonDetectedSelf",
    "RM_UNIQUE_PROCESS",
    "RM_PROCESS_INFO",
    "RM_FILTER_TRIGGER",
    "RM_FILTER_TRIGGER_RmFilterTriggerInvalid",
    "RM_FILTER_TRIGGER_RmFilterTriggerFile",
    "RM_FILTER_TRIGGER_RmFilterTriggerProcess",
    "RM_FILTER_TRIGGER_RmFilterTriggerService",
    "RM_FILTER_ACTION",
    "RM_FILTER_ACTION_RmInvalidFilterAction",
    "RM_FILTER_ACTION_RmNoRestart",
    "RM_FILTER_ACTION_RmNoShutdown",
    "RM_FILTER_INFO",
    "RM_WRITE_STATUS_CALLBACK",
    "RmStartSession",
    "RmJoinSession",
    "RmEndSession",
    "RmRegisterResources",
    "RmGetList",
    "RmShutdown",
    "RmRestart",
    "RmCancelCurrentTask",
    "RmAddFilter",
    "RmRemoveFilter",
    "RmGetFilterList",
]
