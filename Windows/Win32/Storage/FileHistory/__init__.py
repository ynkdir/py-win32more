from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Storage.FileHistory
import Windows.Win32.System.Com
import Windows.Win32.System.WindowsProgramming
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
FHCFG_E_CORRUPT_CONFIG_FILE: Windows.Win32.Foundation.HRESULT = -2147220736
FHCFG_E_CONFIG_FILE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147220735
FHCFG_E_CONFIG_ALREADY_EXISTS: Windows.Win32.Foundation.HRESULT = -2147220734
FHCFG_E_NO_VALID_CONFIGURATION_LOADED: Windows.Win32.Foundation.HRESULT = -2147220733
FHCFG_E_TARGET_NOT_CONNECTED: Windows.Win32.Foundation.HRESULT = -2147220732
FHCFG_E_CONFIGURATION_PREVIOUSLY_LOADED: Windows.Win32.Foundation.HRESULT = -2147220731
FHCFG_E_TARGET_VERIFICATION_FAILED: Windows.Win32.Foundation.HRESULT = -2147220730
FHCFG_E_TARGET_NOT_CONFIGURED: Windows.Win32.Foundation.HRESULT = -2147220729
FHCFG_E_TARGET_NOT_ENOUGH_FREE_SPACE: Windows.Win32.Foundation.HRESULT = -2147220728
FHCFG_E_TARGET_CANNOT_BE_USED: Windows.Win32.Foundation.HRESULT = -2147220727
FHCFG_E_INVALID_REHYDRATION_STATE: Windows.Win32.Foundation.HRESULT = -2147220726
FHCFG_E_RECOMMENDATION_CHANGE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2147220720
FHCFG_E_TARGET_REHYDRATED_ELSEWHERE: Windows.Win32.Foundation.HRESULT = -2147220719
FHCFG_E_LEGACY_TARGET_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -2147220718
FHCFG_E_LEGACY_TARGET_VALIDATION_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -2147220717
FHCFG_E_LEGACY_BACKUP_USER_EXCLUDED: Windows.Win32.Foundation.HRESULT = -2147220716
FHCFG_E_LEGACY_BACKUP_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147220715
FHSVC_E_BACKUP_BLOCKED: Windows.Win32.Foundation.HRESULT = -2147219968
FHSVC_E_NOT_CONFIGURED: Windows.Win32.Foundation.HRESULT = -2147219967
FHSVC_E_CONFIG_DISABLED: Windows.Win32.Foundation.HRESULT = -2147219966
FHSVC_E_CONFIG_DISABLED_GP: Windows.Win32.Foundation.HRESULT = -2147219965
FHSVC_E_FATAL_CONFIG_ERROR: Windows.Win32.Foundation.HRESULT = -2147219964
FHSVC_E_CONFIG_REHYDRATING: Windows.Win32.Foundation.HRESULT = -2147219963
FH_STATE_NOT_TRACKED: UInt32 = 0
FH_STATE_OFF: UInt32 = 1
FH_STATE_DISABLED_BY_GP: UInt32 = 2
FH_STATE_FATAL_CONFIG_ERROR: UInt32 = 3
FH_STATE_MIGRATING: UInt32 = 4
FH_STATE_REHYDRATING: UInt32 = 5
FH_STATE_TARGET_FS_LIMITATION: UInt32 = 13
FH_STATE_TARGET_ACCESS_DENIED: UInt32 = 14
FH_STATE_TARGET_VOLUME_DIRTY: UInt32 = 15
FH_STATE_TARGET_FULL_RETENTION_MAX: UInt32 = 16
FH_STATE_TARGET_FULL: UInt32 = 17
FH_STATE_STAGING_FULL: UInt32 = 18
FH_STATE_TARGET_LOW_SPACE_RETENTION_MAX: UInt32 = 19
FH_STATE_TARGET_LOW_SPACE: UInt32 = 20
FH_STATE_TARGET_ABSENT: UInt32 = 21
FH_STATE_TOO_MUCH_BEHIND: UInt32 = 240
FH_STATE_NO_ERROR: UInt32 = 255
FH_STATE_BACKUP_NOT_SUPPORTED: UInt32 = 2064
FH_STATE_RUNNING: UInt32 = 256
@winfunctype('fhsvcctl.dll')
def FhServiceOpenPipe(StartServiceIfStopped: Windows.Win32.Foundation.BOOL, Pipe: POINTER(Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceClosePipe(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceStartBackup(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, LowPriorityIo: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceStopBackup(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE, StopTracking: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceReloadConfiguration(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceBlockBackup(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceUnblockBackup(Pipe: Windows.Win32.System.WindowsProgramming.FH_SERVICE_PIPE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
FH_BACKUP_STATUS = Int32
FH_STATUS_DISABLED: FH_BACKUP_STATUS = 0
FH_STATUS_DISABLED_BY_GP: FH_BACKUP_STATUS = 1
FH_STATUS_ENABLED: FH_BACKUP_STATUS = 2
FH_STATUS_REHYDRATING: FH_BACKUP_STATUS = 3
MAX_BACKUP_STATUS: FH_BACKUP_STATUS = 4
FH_DEVICE_VALIDATION_RESULT = Int32
FH_ACCESS_DENIED: FH_DEVICE_VALIDATION_RESULT = 0
FH_INVALID_DRIVE_TYPE: FH_DEVICE_VALIDATION_RESULT = 1
FH_READ_ONLY_PERMISSION: FH_DEVICE_VALIDATION_RESULT = 2
FH_CURRENT_DEFAULT: FH_DEVICE_VALIDATION_RESULT = 3
FH_NAMESPACE_EXISTS: FH_DEVICE_VALIDATION_RESULT = 4
FH_TARGET_PART_OF_LIBRARY: FH_DEVICE_VALIDATION_RESULT = 5
FH_VALID_TARGET: FH_DEVICE_VALIDATION_RESULT = 6
MAX_VALIDATION_RESULT: FH_DEVICE_VALIDATION_RESULT = 7
FH_LOCAL_POLICY_TYPE = Int32
FH_FREQUENCY: FH_LOCAL_POLICY_TYPE = 0
FH_RETENTION_TYPE: FH_LOCAL_POLICY_TYPE = 1
FH_RETENTION_AGE: FH_LOCAL_POLICY_TYPE = 2
MAX_LOCAL_POLICY: FH_LOCAL_POLICY_TYPE = 3
FH_PROTECTED_ITEM_CATEGORY = Int32
FH_FOLDER: FH_PROTECTED_ITEM_CATEGORY = 0
FH_LIBRARY: FH_PROTECTED_ITEM_CATEGORY = 1
MAX_PROTECTED_ITEM_CATEGORY: FH_PROTECTED_ITEM_CATEGORY = 2
FH_RETENTION_TYPES = Int32
FH_RETENTION_DISABLED: FH_RETENTION_TYPES = 0
FH_RETENTION_UNLIMITED: FH_RETENTION_TYPES = 1
FH_RETENTION_AGE_BASED: FH_RETENTION_TYPES = 2
MAX_RETENTION_TYPE: FH_RETENTION_TYPES = 3
FH_TARGET_DRIVE_TYPES = Int32
FH_DRIVE_UNKNOWN: FH_TARGET_DRIVE_TYPES = 0
FH_DRIVE_REMOVABLE: FH_TARGET_DRIVE_TYPES = 2
FH_DRIVE_FIXED: FH_TARGET_DRIVE_TYPES = 3
FH_DRIVE_REMOTE: FH_TARGET_DRIVE_TYPES = 4
FH_TARGET_PROPERTY_TYPE = Int32
FH_TARGET_NAME: FH_TARGET_PROPERTY_TYPE = 0
FH_TARGET_URL: FH_TARGET_PROPERTY_TYPE = 1
FH_TARGET_DRIVE_TYPE: FH_TARGET_PROPERTY_TYPE = 2
MAX_TARGET_PROPERTY: FH_TARGET_PROPERTY_TYPE = 3
FhBackupStopReason = Int32
FhBackupStopReason_BackupInvalidStopReason: FhBackupStopReason = 0
FhBackupStopReason_BackupLimitUserBusyMachineOnAC: FhBackupStopReason = 1
FhBackupStopReason_BackupLimitUserIdleMachineOnDC: FhBackupStopReason = 2
FhBackupStopReason_BackupLimitUserBusyMachineOnDC: FhBackupStopReason = 3
FhBackupStopReason_BackupCancelled: FhBackupStopReason = 4
FhConfigMgr = Guid('ed43bb3c-09e9-498a-9d-f6-21-77-24-4c-6d-b4')
FhReassociation = Guid('4d728e35-16fa-4320-9e-8b-bf-d7-10-0a-88-46')
class IFhConfigMgr(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6a5fea5b-bf8f-4ee5-b8-c3-44-d8-a0-d7-33-1c')
    @commethod(3)
    def LoadConfiguration() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDefaultConfiguration(OverwriteIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveConfiguration() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddRemoveExcludeRule(Add: Windows.Win32.Foundation.BOOL, Category: Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY, Item: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIncludeExcludeRules(Include: Windows.Win32.Foundation.BOOL, Category: Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY, Iterator: POINTER(Windows.Win32.Storage.FileHistory.IFhScopeIterator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLocalPolicy(LocalPolicyType: Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE, PolicyValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetLocalPolicy(LocalPolicyType: Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE, PolicyValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackupStatus(BackupStatus: POINTER(Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetBackupStatus(BackupStatus: Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDefaultTarget(DefaultTarget: POINTER(Windows.Win32.Storage.FileHistory.IFhTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ValidateTarget(TargetUrl: Windows.Win32.Foundation.BSTR, ValidationResult: POINTER(Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProvisionAndSetNewTarget(TargetUrl: Windows.Win32.Foundation.BSTR, TargetName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ChangeDefaultTargetRecommendation(Recommend: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def QueryProtectionStatus(ProtectionState: POINTER(UInt32), ProtectedUntilTime: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IFhReassociation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6544a28a-f68d-47ac-91-ef-16-b2-b3-6a-a3-ee')
    @commethod(3)
    def ValidateTarget(TargetUrl: Windows.Win32.Foundation.BSTR, ValidationResult: POINTER(Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ScanTargetForConfigurations(TargetUrl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetConfigurationDetails(Index: UInt32, UserName: POINTER(Windows.Win32.Foundation.BSTR), PcName: POINTER(Windows.Win32.Foundation.BSTR), BackupTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SelectConfiguration(Index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PerformReassociation(OverwriteIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFhScopeIterator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3197abce-532a-44c6-86-15-f3-66-65-66-a7-20')
    @commethod(3)
    def MoveToNextItem() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(Item: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IFhTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d87965fd-2bad-4657-bd-3b-95-67-eb-30-0c-ed')
    @commethod(3)
    def GetStringProperty(PropertyType: Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE, PropertyValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumericalProperty(PropertyType: Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE, PropertyValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IFhConfigMgr')
make_head(_module, 'IFhReassociation')
make_head(_module, 'IFhScopeIterator')
make_head(_module, 'IFhTarget')
__all__ = [
    "FHCFG_E_CONFIGURATION_PREVIOUSLY_LOADED",
    "FHCFG_E_CONFIG_ALREADY_EXISTS",
    "FHCFG_E_CONFIG_FILE_NOT_FOUND",
    "FHCFG_E_CORRUPT_CONFIG_FILE",
    "FHCFG_E_INVALID_REHYDRATION_STATE",
    "FHCFG_E_LEGACY_BACKUP_NOT_FOUND",
    "FHCFG_E_LEGACY_BACKUP_USER_EXCLUDED",
    "FHCFG_E_LEGACY_TARGET_UNSUPPORTED",
    "FHCFG_E_LEGACY_TARGET_VALIDATION_UNSUPPORTED",
    "FHCFG_E_NO_VALID_CONFIGURATION_LOADED",
    "FHCFG_E_RECOMMENDATION_CHANGE_NOT_ALLOWED",
    "FHCFG_E_TARGET_CANNOT_BE_USED",
    "FHCFG_E_TARGET_NOT_CONFIGURED",
    "FHCFG_E_TARGET_NOT_CONNECTED",
    "FHCFG_E_TARGET_NOT_ENOUGH_FREE_SPACE",
    "FHCFG_E_TARGET_REHYDRATED_ELSEWHERE",
    "FHCFG_E_TARGET_VERIFICATION_FAILED",
    "FHSVC_E_BACKUP_BLOCKED",
    "FHSVC_E_CONFIG_DISABLED",
    "FHSVC_E_CONFIG_DISABLED_GP",
    "FHSVC_E_CONFIG_REHYDRATING",
    "FHSVC_E_FATAL_CONFIG_ERROR",
    "FHSVC_E_NOT_CONFIGURED",
    "FH_ACCESS_DENIED",
    "FH_BACKUP_STATUS",
    "FH_CURRENT_DEFAULT",
    "FH_DEVICE_VALIDATION_RESULT",
    "FH_DRIVE_FIXED",
    "FH_DRIVE_REMOTE",
    "FH_DRIVE_REMOVABLE",
    "FH_DRIVE_UNKNOWN",
    "FH_FOLDER",
    "FH_FREQUENCY",
    "FH_INVALID_DRIVE_TYPE",
    "FH_LIBRARY",
    "FH_LOCAL_POLICY_TYPE",
    "FH_NAMESPACE_EXISTS",
    "FH_PROTECTED_ITEM_CATEGORY",
    "FH_READ_ONLY_PERMISSION",
    "FH_RETENTION_AGE",
    "FH_RETENTION_AGE_BASED",
    "FH_RETENTION_DISABLED",
    "FH_RETENTION_TYPE",
    "FH_RETENTION_TYPES",
    "FH_RETENTION_UNLIMITED",
    "FH_STATE_BACKUP_NOT_SUPPORTED",
    "FH_STATE_DISABLED_BY_GP",
    "FH_STATE_FATAL_CONFIG_ERROR",
    "FH_STATE_MIGRATING",
    "FH_STATE_NOT_TRACKED",
    "FH_STATE_NO_ERROR",
    "FH_STATE_OFF",
    "FH_STATE_REHYDRATING",
    "FH_STATE_RUNNING",
    "FH_STATE_STAGING_FULL",
    "FH_STATE_TARGET_ABSENT",
    "FH_STATE_TARGET_ACCESS_DENIED",
    "FH_STATE_TARGET_FS_LIMITATION",
    "FH_STATE_TARGET_FULL",
    "FH_STATE_TARGET_FULL_RETENTION_MAX",
    "FH_STATE_TARGET_LOW_SPACE",
    "FH_STATE_TARGET_LOW_SPACE_RETENTION_MAX",
    "FH_STATE_TARGET_VOLUME_DIRTY",
    "FH_STATE_TOO_MUCH_BEHIND",
    "FH_STATUS_DISABLED",
    "FH_STATUS_DISABLED_BY_GP",
    "FH_STATUS_ENABLED",
    "FH_STATUS_REHYDRATING",
    "FH_TARGET_DRIVE_TYPE",
    "FH_TARGET_DRIVE_TYPES",
    "FH_TARGET_NAME",
    "FH_TARGET_PART_OF_LIBRARY",
    "FH_TARGET_PROPERTY_TYPE",
    "FH_TARGET_URL",
    "FH_VALID_TARGET",
    "FhBackupStopReason",
    "FhBackupStopReason_BackupCancelled",
    "FhBackupStopReason_BackupInvalidStopReason",
    "FhBackupStopReason_BackupLimitUserBusyMachineOnAC",
    "FhBackupStopReason_BackupLimitUserBusyMachineOnDC",
    "FhBackupStopReason_BackupLimitUserIdleMachineOnDC",
    "FhConfigMgr",
    "FhReassociation",
    "FhServiceBlockBackup",
    "FhServiceClosePipe",
    "FhServiceOpenPipe",
    "FhServiceReloadConfiguration",
    "FhServiceStartBackup",
    "FhServiceStopBackup",
    "FhServiceUnblockBackup",
    "IFhConfigMgr",
    "IFhReassociation",
    "IFhScopeIterator",
    "IFhTarget",
    "MAX_BACKUP_STATUS",
    "MAX_LOCAL_POLICY",
    "MAX_PROTECTED_ITEM_CATEGORY",
    "MAX_RETENTION_TYPE",
    "MAX_TARGET_PROPERTY",
    "MAX_VALIDATION_RESULT",
]
_arch_optional = [
]
