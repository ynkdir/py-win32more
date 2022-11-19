from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.FileHistory
import win32more.System.Com
import win32more.System.WindowsProgramming

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
FHCFG_E_CORRUPT_CONFIG_FILE = -2147220736
FHCFG_E_CONFIG_FILE_NOT_FOUND = -2147220735
FHCFG_E_CONFIG_ALREADY_EXISTS = -2147220734
FHCFG_E_NO_VALID_CONFIGURATION_LOADED = -2147220733
FHCFG_E_TARGET_NOT_CONNECTED = -2147220732
FHCFG_E_CONFIGURATION_PREVIOUSLY_LOADED = -2147220731
FHCFG_E_TARGET_VERIFICATION_FAILED = -2147220730
FHCFG_E_TARGET_NOT_CONFIGURED = -2147220729
FHCFG_E_TARGET_NOT_ENOUGH_FREE_SPACE = -2147220728
FHCFG_E_TARGET_CANNOT_BE_USED = -2147220727
FHCFG_E_INVALID_REHYDRATION_STATE = -2147220726
FHCFG_E_RECOMMENDATION_CHANGE_NOT_ALLOWED = -2147220720
FHCFG_E_TARGET_REHYDRATED_ELSEWHERE = -2147220719
FHCFG_E_LEGACY_TARGET_UNSUPPORTED = -2147220718
FHCFG_E_LEGACY_TARGET_VALIDATION_UNSUPPORTED = -2147220717
FHCFG_E_LEGACY_BACKUP_USER_EXCLUDED = -2147220716
FHCFG_E_LEGACY_BACKUP_NOT_FOUND = -2147220715
FHSVC_E_BACKUP_BLOCKED = -2147219968
FHSVC_E_NOT_CONFIGURED = -2147219967
FHSVC_E_CONFIG_DISABLED = -2147219966
FHSVC_E_CONFIG_DISABLED_GP = -2147219965
FHSVC_E_FATAL_CONFIG_ERROR = -2147219964
FHSVC_E_CONFIG_REHYDRATING = -2147219963
FH_STATE_NOT_TRACKED = 0
FH_STATE_OFF = 1
FH_STATE_DISABLED_BY_GP = 2
FH_STATE_FATAL_CONFIG_ERROR = 3
FH_STATE_MIGRATING = 4
FH_STATE_REHYDRATING = 5
FH_STATE_TARGET_FS_LIMITATION = 13
FH_STATE_TARGET_ACCESS_DENIED = 14
FH_STATE_TARGET_VOLUME_DIRTY = 15
FH_STATE_TARGET_FULL_RETENTION_MAX = 16
FH_STATE_TARGET_FULL = 17
FH_STATE_STAGING_FULL = 18
FH_STATE_TARGET_LOW_SPACE_RETENTION_MAX = 19
FH_STATE_TARGET_LOW_SPACE = 20
FH_STATE_TARGET_ABSENT = 21
FH_STATE_TOO_MUCH_BEHIND = 240
FH_STATE_NO_ERROR = 255
FH_STATE_BACKUP_NOT_SUPPORTED = 2064
FH_STATE_RUNNING = 256
FhConfigMgr = Guid('ed43bb3c-09e9-498a-9df6-2177244c6db4')
FhReassociation = Guid('4d728e35-16fa-4320-9e8b-bfd7100a8846')
FH_TARGET_PROPERTY_TYPE = Int32
FH_TARGET_NAME = 0
FH_TARGET_URL = 1
FH_TARGET_DRIVE_TYPE = 2
MAX_TARGET_PROPERTY = 3
FH_TARGET_DRIVE_TYPES = Int32
FH_DRIVE_UNKNOWN = 0
FH_DRIVE_REMOVABLE = 2
FH_DRIVE_FIXED = 3
FH_DRIVE_REMOTE = 4
def _define_IFhTarget_head():
    class IFhTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('d87965fd-2bad-4657-bd3b-9567eb300ced')
    return IFhTarget
def _define_IFhTarget():
    IFhTarget = win32more.Storage.FileHistory.IFhTarget_head
    IFhTarget.GetStringProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetStringProperty', ((1, 'PropertyType'),(1, 'PropertyValue'),)))
    IFhTarget.GetNumericalProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE,POINTER(UInt64), use_last_error=False)(4, 'GetNumericalProperty', ((1, 'PropertyType'),(1, 'PropertyValue'),)))
    win32more.System.Com.IUnknown
    return IFhTarget
def _define_IFhScopeIterator_head():
    class IFhScopeIterator(win32more.System.Com.IUnknown_head):
        Guid = Guid('3197abce-532a-44c6-8615-f3666566a720')
    return IFhScopeIterator
def _define_IFhScopeIterator():
    IFhScopeIterator = win32more.Storage.FileHistory.IFhScopeIterator_head
    IFhScopeIterator.MoveToNextItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'MoveToNextItem', ()))
    IFhScopeIterator.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetItem', ((1, 'Item'),)))
    win32more.System.Com.IUnknown
    return IFhScopeIterator
FH_PROTECTED_ITEM_CATEGORY = Int32
FH_FOLDER = 0
FH_LIBRARY = 1
MAX_PROTECTED_ITEM_CATEGORY = 2
FH_LOCAL_POLICY_TYPE = Int32
FH_FREQUENCY = 0
FH_RETENTION_TYPE = 1
FH_RETENTION_AGE = 2
MAX_LOCAL_POLICY = 3
FH_RETENTION_TYPES = Int32
FH_RETENTION_DISABLED = 0
FH_RETENTION_UNLIMITED = 1
FH_RETENTION_AGE_BASED = 2
MAX_RETENTION_TYPE = 3
FH_BACKUP_STATUS = Int32
FH_STATUS_DISABLED = 0
FH_STATUS_DISABLED_BY_GP = 1
FH_STATUS_ENABLED = 2
FH_STATUS_REHYDRATING = 3
MAX_BACKUP_STATUS = 4
FH_DEVICE_VALIDATION_RESULT = Int32
FH_ACCESS_DENIED = 0
FH_INVALID_DRIVE_TYPE = 1
FH_READ_ONLY_PERMISSION = 2
FH_CURRENT_DEFAULT = 3
FH_NAMESPACE_EXISTS = 4
FH_TARGET_PART_OF_LIBRARY = 5
FH_VALID_TARGET = 6
MAX_VALIDATION_RESULT = 7
def _define_IFhConfigMgr_head():
    class IFhConfigMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('6a5fea5b-bf8f-4ee5-b8c3-44d8a0d7331c')
    return IFhConfigMgr
def _define_IFhConfigMgr():
    IFhConfigMgr = win32more.Storage.FileHistory.IFhConfigMgr_head
    IFhConfigMgr.LoadConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'LoadConfiguration', ()))
    IFhConfigMgr.CreateDefaultConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'CreateDefaultConfiguration', ((1, 'OverwriteIfExists'),)))
    IFhConfigMgr.SaveConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SaveConfiguration', ()))
    IFhConfigMgr.AddRemoveExcludeRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY,win32more.Foundation.BSTR, use_last_error=False)(6, 'AddRemoveExcludeRule', ((1, 'Add'),(1, 'Category'),(1, 'Item'),)))
    IFhConfigMgr.GetIncludeExcludeRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY,POINTER(win32more.Storage.FileHistory.IFhScopeIterator_head), use_last_error=False)(7, 'GetIncludeExcludeRules', ((1, 'Include'),(1, 'Category'),(1, 'Iterator'),)))
    IFhConfigMgr.GetLocalPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileHistory.FH_LOCAL_POLICY_TYPE,POINTER(UInt64), use_last_error=False)(8, 'GetLocalPolicy', ((1, 'LocalPolicyType'),(1, 'PolicyValue'),)))
    IFhConfigMgr.SetLocalPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileHistory.FH_LOCAL_POLICY_TYPE,UInt64, use_last_error=False)(9, 'SetLocalPolicy', ((1, 'LocalPolicyType'),(1, 'PolicyValue'),)))
    IFhConfigMgr.GetBackupStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileHistory.FH_BACKUP_STATUS), use_last_error=False)(10, 'GetBackupStatus', ((1, 'BackupStatus'),)))
    IFhConfigMgr.SetBackupStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileHistory.FH_BACKUP_STATUS, use_last_error=False)(11, 'SetBackupStatus', ((1, 'BackupStatus'),)))
    IFhConfigMgr.GetDefaultTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileHistory.IFhTarget_head), use_last_error=False)(12, 'GetDefaultTarget', ((1, 'DefaultTarget'),)))
    IFhConfigMgr.ValidateTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT), use_last_error=False)(13, 'ValidateTarget', ((1, 'TargetUrl'),(1, 'ValidationResult'),)))
    IFhConfigMgr.ProvisionAndSetNewTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(14, 'ProvisionAndSetNewTarget', ((1, 'TargetUrl'),(1, 'TargetName'),)))
    IFhConfigMgr.ChangeDefaultTargetRecommendation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(15, 'ChangeDefaultTargetRecommendation', ((1, 'Recommend'),)))
    IFhConfigMgr.QueryProtectionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'QueryProtectionStatus', ((1, 'ProtectionState'),(1, 'ProtectedUntilTime'),)))
    win32more.System.Com.IUnknown
    return IFhConfigMgr
def _define_IFhReassociation_head():
    class IFhReassociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('6544a28a-f68d-47ac-91ef-16b2b36aa3ee')
    return IFhReassociation
def _define_IFhReassociation():
    IFhReassociation = win32more.Storage.FileHistory.IFhReassociation_head
    IFhReassociation.ValidateTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT), use_last_error=False)(3, 'ValidateTarget', ((1, 'TargetUrl'),(1, 'ValidationResult'),)))
    IFhReassociation.ScanTargetForConfigurations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'ScanTargetForConfigurations', ((1, 'TargetUrl'),)))
    IFhReassociation.GetConfigurationDetails = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(5, 'GetConfigurationDetails', ((1, 'Index'),(1, 'UserName'),(1, 'PcName'),(1, 'BackupTime'),)))
    IFhReassociation.SelectConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SelectConfiguration', ((1, 'Index'),)))
    IFhReassociation.PerformReassociation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'PerformReassociation', ((1, 'OverwriteIfExists'),)))
    win32more.System.Com.IUnknown
    return IFhReassociation
FhBackupStopReason = Int32
FhBackupStopReason_BackupInvalidStopReason = 0
FhBackupStopReason_BackupLimitUserBusyMachineOnAC = 1
FhBackupStopReason_BackupLimitUserIdleMachineOnDC = 2
FhBackupStopReason_BackupLimitUserBusyMachineOnDC = 3
FhBackupStopReason_BackupCancelled = 4
def _define_FhServiceOpenPipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE), use_last_error=False)(("FhServiceOpenPipe", windll["fhsvcctl"]), ((1, 'StartServiceIfStopped'),(1, 'Pipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceClosePipe():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, use_last_error=False)(("FhServiceClosePipe", windll["fhsvcctl"]), ((1, 'Pipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceStartBackup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE,win32more.Foundation.BOOL, use_last_error=False)(("FhServiceStartBackup", windll["fhsvcctl"]), ((1, 'Pipe'),(1, 'LowPriorityIo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceStopBackup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE,win32more.Foundation.BOOL, use_last_error=False)(("FhServiceStopBackup", windll["fhsvcctl"]), ((1, 'Pipe'),(1, 'StopTracking'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceReloadConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, use_last_error=False)(("FhServiceReloadConfiguration", windll["fhsvcctl"]), ((1, 'Pipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceBlockBackup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, use_last_error=False)(("FhServiceBlockBackup", windll["fhsvcctl"]), ((1, 'Pipe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FhServiceUnblockBackup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, use_last_error=False)(("FhServiceUnblockBackup", windll["fhsvcctl"]), ((1, 'Pipe'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FHCFG_E_CORRUPT_CONFIG_FILE",
    "FHCFG_E_CONFIG_FILE_NOT_FOUND",
    "FHCFG_E_CONFIG_ALREADY_EXISTS",
    "FHCFG_E_NO_VALID_CONFIGURATION_LOADED",
    "FHCFG_E_TARGET_NOT_CONNECTED",
    "FHCFG_E_CONFIGURATION_PREVIOUSLY_LOADED",
    "FHCFG_E_TARGET_VERIFICATION_FAILED",
    "FHCFG_E_TARGET_NOT_CONFIGURED",
    "FHCFG_E_TARGET_NOT_ENOUGH_FREE_SPACE",
    "FHCFG_E_TARGET_CANNOT_BE_USED",
    "FHCFG_E_INVALID_REHYDRATION_STATE",
    "FHCFG_E_RECOMMENDATION_CHANGE_NOT_ALLOWED",
    "FHCFG_E_TARGET_REHYDRATED_ELSEWHERE",
    "FHCFG_E_LEGACY_TARGET_UNSUPPORTED",
    "FHCFG_E_LEGACY_TARGET_VALIDATION_UNSUPPORTED",
    "FHCFG_E_LEGACY_BACKUP_USER_EXCLUDED",
    "FHCFG_E_LEGACY_BACKUP_NOT_FOUND",
    "FHSVC_E_BACKUP_BLOCKED",
    "FHSVC_E_NOT_CONFIGURED",
    "FHSVC_E_CONFIG_DISABLED",
    "FHSVC_E_CONFIG_DISABLED_GP",
    "FHSVC_E_FATAL_CONFIG_ERROR",
    "FHSVC_E_CONFIG_REHYDRATING",
    "FH_STATE_NOT_TRACKED",
    "FH_STATE_OFF",
    "FH_STATE_DISABLED_BY_GP",
    "FH_STATE_FATAL_CONFIG_ERROR",
    "FH_STATE_MIGRATING",
    "FH_STATE_REHYDRATING",
    "FH_STATE_TARGET_FS_LIMITATION",
    "FH_STATE_TARGET_ACCESS_DENIED",
    "FH_STATE_TARGET_VOLUME_DIRTY",
    "FH_STATE_TARGET_FULL_RETENTION_MAX",
    "FH_STATE_TARGET_FULL",
    "FH_STATE_STAGING_FULL",
    "FH_STATE_TARGET_LOW_SPACE_RETENTION_MAX",
    "FH_STATE_TARGET_LOW_SPACE",
    "FH_STATE_TARGET_ABSENT",
    "FH_STATE_TOO_MUCH_BEHIND",
    "FH_STATE_NO_ERROR",
    "FH_STATE_BACKUP_NOT_SUPPORTED",
    "FH_STATE_RUNNING",
    "FhConfigMgr",
    "FhReassociation",
    "FH_TARGET_PROPERTY_TYPE",
    "FH_TARGET_NAME",
    "FH_TARGET_URL",
    "FH_TARGET_DRIVE_TYPE",
    "MAX_TARGET_PROPERTY",
    "FH_TARGET_DRIVE_TYPES",
    "FH_DRIVE_UNKNOWN",
    "FH_DRIVE_REMOVABLE",
    "FH_DRIVE_FIXED",
    "FH_DRIVE_REMOTE",
    "IFhTarget",
    "IFhScopeIterator",
    "FH_PROTECTED_ITEM_CATEGORY",
    "FH_FOLDER",
    "FH_LIBRARY",
    "MAX_PROTECTED_ITEM_CATEGORY",
    "FH_LOCAL_POLICY_TYPE",
    "FH_FREQUENCY",
    "FH_RETENTION_TYPE",
    "FH_RETENTION_AGE",
    "MAX_LOCAL_POLICY",
    "FH_RETENTION_TYPES",
    "FH_RETENTION_DISABLED",
    "FH_RETENTION_UNLIMITED",
    "FH_RETENTION_AGE_BASED",
    "MAX_RETENTION_TYPE",
    "FH_BACKUP_STATUS",
    "FH_STATUS_DISABLED",
    "FH_STATUS_DISABLED_BY_GP",
    "FH_STATUS_ENABLED",
    "FH_STATUS_REHYDRATING",
    "MAX_BACKUP_STATUS",
    "FH_DEVICE_VALIDATION_RESULT",
    "FH_ACCESS_DENIED",
    "FH_INVALID_DRIVE_TYPE",
    "FH_READ_ONLY_PERMISSION",
    "FH_CURRENT_DEFAULT",
    "FH_NAMESPACE_EXISTS",
    "FH_TARGET_PART_OF_LIBRARY",
    "FH_VALID_TARGET",
    "MAX_VALIDATION_RESULT",
    "IFhConfigMgr",
    "IFhReassociation",
    "FhBackupStopReason",
    "FhBackupStopReason_BackupInvalidStopReason",
    "FhBackupStopReason_BackupLimitUserBusyMachineOnAC",
    "FhBackupStopReason_BackupLimitUserIdleMachineOnDC",
    "FhBackupStopReason_BackupLimitUserBusyMachineOnDC",
    "FhBackupStopReason_BackupCancelled",
    "FhServiceOpenPipe",
    "FhServiceClosePipe",
    "FhServiceStartBackup",
    "FhServiceStopBackup",
    "FhServiceReloadConfiguration",
    "FhServiceBlockBackup",
    "FhServiceUnblockBackup",
]
