from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.FileHistory
import win32more.Windows.Win32.System.Com
FHCFG_E_CORRUPT_CONFIG_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2147220736
FHCFG_E_CONFIG_FILE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220735
FHCFG_E_CONFIG_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147220734
FHCFG_E_NO_VALID_CONFIGURATION_LOADED: win32more.Windows.Win32.Foundation.HRESULT = -2147220733
FHCFG_E_TARGET_NOT_CONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220732
FHCFG_E_CONFIGURATION_PREVIOUSLY_LOADED: win32more.Windows.Win32.Foundation.HRESULT = -2147220731
FHCFG_E_TARGET_VERIFICATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220730
FHCFG_E_TARGET_NOT_CONFIGURED: win32more.Windows.Win32.Foundation.HRESULT = -2147220729
FHCFG_E_TARGET_NOT_ENOUGH_FREE_SPACE: win32more.Windows.Win32.Foundation.HRESULT = -2147220728
FHCFG_E_TARGET_CANNOT_BE_USED: win32more.Windows.Win32.Foundation.HRESULT = -2147220727
FHCFG_E_INVALID_REHYDRATION_STATE: win32more.Windows.Win32.Foundation.HRESULT = -2147220726
FHCFG_E_RECOMMENDATION_CHANGE_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -2147220720
FHCFG_E_TARGET_REHYDRATED_ELSEWHERE: win32more.Windows.Win32.Foundation.HRESULT = -2147220719
FHCFG_E_LEGACY_TARGET_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220718
FHCFG_E_LEGACY_TARGET_VALIDATION_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220717
FHCFG_E_LEGACY_BACKUP_USER_EXCLUDED: win32more.Windows.Win32.Foundation.HRESULT = -2147220716
FHCFG_E_LEGACY_BACKUP_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147220715
FHSVC_E_BACKUP_BLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147219968
FHSVC_E_NOT_CONFIGURED: win32more.Windows.Win32.Foundation.HRESULT = -2147219967
FHSVC_E_CONFIG_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147219966
FHSVC_E_CONFIG_DISABLED_GP: win32more.Windows.Win32.Foundation.HRESULT = -2147219965
FHSVC_E_FATAL_CONFIG_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147219964
FHSVC_E_CONFIG_REHYDRATING: win32more.Windows.Win32.Foundation.HRESULT = -2147219963
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
def FhServiceOpenPipe(StartServiceIfStopped: win32more.Windows.Win32.Foundation.BOOL, Pipe: POINTER(win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceClosePipe(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceStartBackup(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE, LowPriorityIo: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceStopBackup(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE, StopTracking: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceReloadConfiguration(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceBlockBackup(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('fhsvcctl.dll')
def FhServiceUnblockBackup(Pipe: win32more.Windows.Win32.Storage.FileHistory.FH_SERVICE_PIPE_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
FH_BACKUP_STATUS = Int32
FH_STATUS_DISABLED: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS = 0
FH_STATUS_DISABLED_BY_GP: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS = 1
FH_STATUS_ENABLED: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS = 2
FH_STATUS_REHYDRATING: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS = 3
MAX_BACKUP_STATUS: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS = 4
FH_DEVICE_VALIDATION_RESULT = Int32
FH_ACCESS_DENIED: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 0
FH_INVALID_DRIVE_TYPE: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 1
FH_READ_ONLY_PERMISSION: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 2
FH_CURRENT_DEFAULT: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 3
FH_NAMESPACE_EXISTS: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 4
FH_TARGET_PART_OF_LIBRARY: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 5
FH_VALID_TARGET: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 6
MAX_VALIDATION_RESULT: win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT = 7
FH_LOCAL_POLICY_TYPE = Int32
FH_FREQUENCY: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE = 0
FH_RETENTION_TYPE: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE = 1
FH_RETENTION_AGE: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE = 2
MAX_LOCAL_POLICY: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE = 3
FH_PROTECTED_ITEM_CATEGORY = Int32
FH_FOLDER: win32more.Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY = 0
FH_LIBRARY: win32more.Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY = 1
MAX_PROTECTED_ITEM_CATEGORY: win32more.Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY = 2
FH_RETENTION_TYPES = Int32
FH_RETENTION_DISABLED: win32more.Windows.Win32.Storage.FileHistory.FH_RETENTION_TYPES = 0
FH_RETENTION_UNLIMITED: win32more.Windows.Win32.Storage.FileHistory.FH_RETENTION_TYPES = 1
FH_RETENTION_AGE_BASED: win32more.Windows.Win32.Storage.FileHistory.FH_RETENTION_TYPES = 2
MAX_RETENTION_TYPE: win32more.Windows.Win32.Storage.FileHistory.FH_RETENTION_TYPES = 3
FH_SERVICE_PIPE_HANDLE = VoidPtr
FH_TARGET_DRIVE_TYPES = Int32
FH_DRIVE_UNKNOWN: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_DRIVE_TYPES = 0
FH_DRIVE_REMOVABLE: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_DRIVE_TYPES = 2
FH_DRIVE_FIXED: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_DRIVE_TYPES = 3
FH_DRIVE_REMOTE: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_DRIVE_TYPES = 4
FH_TARGET_PROPERTY_TYPE = Int32
FH_TARGET_NAME: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE = 0
FH_TARGET_URL: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE = 1
FH_TARGET_DRIVE_TYPE: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE = 2
MAX_TARGET_PROPERTY: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE = 3
FhBackupStopReason = Int32
BackupInvalidStopReason: win32more.Windows.Win32.Storage.FileHistory.FhBackupStopReason = 0
BackupLimitUserBusyMachineOnAC: win32more.Windows.Win32.Storage.FileHistory.FhBackupStopReason = 1
BackupLimitUserIdleMachineOnDC: win32more.Windows.Win32.Storage.FileHistory.FhBackupStopReason = 2
BackupLimitUserBusyMachineOnDC: win32more.Windows.Win32.Storage.FileHistory.FhBackupStopReason = 3
BackupCancelled: win32more.Windows.Win32.Storage.FileHistory.FhBackupStopReason = 4
FhConfigMgr = Guid('{ed43bb3c-09e9-498a-9df6-2177244c6db4}')
FhReassociation = Guid('{4d728e35-16fa-4320-9e8b-bfd7100a8846}')
class IFhConfigMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a5fea5b-bf8f-4ee5-b8c3-44d8a0d7331c}')
    @commethod(3)
    def LoadConfiguration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDefaultConfiguration(self, OverwriteIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveConfiguration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddRemoveExcludeRule(self, Add: win32more.Windows.Win32.Foundation.BOOL, Category: win32more.Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY, Item: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIncludeExcludeRules(self, Include: win32more.Windows.Win32.Foundation.BOOL, Category: win32more.Windows.Win32.Storage.FileHistory.FH_PROTECTED_ITEM_CATEGORY, Iterator: POINTER(win32more.Windows.Win32.Storage.FileHistory.IFhScopeIterator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLocalPolicy(self, LocalPolicyType: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE, PolicyValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetLocalPolicy(self, LocalPolicyType: win32more.Windows.Win32.Storage.FileHistory.FH_LOCAL_POLICY_TYPE, PolicyValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackupStatus(self, BackupStatus: POINTER(win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetBackupStatus(self, BackupStatus: win32more.Windows.Win32.Storage.FileHistory.FH_BACKUP_STATUS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDefaultTarget(self, DefaultTarget: POINTER(win32more.Windows.Win32.Storage.FileHistory.IFhTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ValidateTarget(self, TargetUrl: win32more.Windows.Win32.Foundation.BSTR, ValidationResult: POINTER(win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProvisionAndSetNewTarget(self, TargetUrl: win32more.Windows.Win32.Foundation.BSTR, TargetName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ChangeDefaultTargetRecommendation(self, Recommend: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def QueryProtectionStatus(self, ProtectionState: POINTER(UInt32), ProtectedUntilTime: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFhReassociation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6544a28a-f68d-47ac-91ef-16b2b36aa3ee}')
    @commethod(3)
    def ValidateTarget(self, TargetUrl: win32more.Windows.Win32.Foundation.BSTR, ValidationResult: POINTER(win32more.Windows.Win32.Storage.FileHistory.FH_DEVICE_VALIDATION_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ScanTargetForConfigurations(self, TargetUrl: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetConfigurationDetails(self, Index: UInt32, UserName: POINTER(win32more.Windows.Win32.Foundation.BSTR), PcName: POINTER(win32more.Windows.Win32.Foundation.BSTR), BackupTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SelectConfiguration(self, Index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PerformReassociation(self, OverwriteIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFhScopeIterator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3197abce-532a-44c6-8615-f3666566a720}')
    @commethod(3)
    def MoveToNextItem(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, Item: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFhTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d87965fd-2bad-4657-bd3b-9567eb300ced}')
    @commethod(3)
    def GetStringProperty(self, PropertyType: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE, PropertyValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumericalProperty(self, PropertyType: win32more.Windows.Win32.Storage.FileHistory.FH_TARGET_PROPERTY_TYPE, PropertyValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
