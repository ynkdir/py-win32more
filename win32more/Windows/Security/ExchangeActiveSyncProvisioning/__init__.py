from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Security.ExchangeActiveSyncProvisioning
class EasClientDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_OperatingSystem(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemManufacturer(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemProductName(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemSku(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHardwareVersion(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemFirmwareVersion(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation2) -> WinRT_String: ...
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
class EasClientSecurityPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.EasClientSecurityPolicy'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasClientSecurityPolicy: ...
    @winrt_mixinmethod
    def get_RequireEncryption(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireEncryption(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MinPasswordLength(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> Byte: ...
    @winrt_mixinmethod
    def put_MinPasswordLength(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_DisallowConvenienceLogon(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisallowConvenienceLogon(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MinPasswordComplexCharacters(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> Byte: ...
    @winrt_mixinmethod
    def put_MinPasswordComplexCharacters(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PasswordExpiration(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_PasswordExpiration(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_PasswordHistory(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> UInt32: ...
    @winrt_mixinmethod
    def put_PasswordHistory(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxPasswordFailedAttempts(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> Byte: ...
    @winrt_mixinmethod
    def put_MaxPasswordFailedAttempts(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_MaxInactivityTimeLock(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_MaxInactivityTimeLock(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def CheckCompliance(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasComplianceResults: ...
    @winrt_mixinmethod
    def ApplyAsync(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasComplianceResults]: ...
    RequireEncryption = property(get_RequireEncryption, put_RequireEncryption)
    MinPasswordLength = property(get_MinPasswordLength, put_MinPasswordLength)
    DisallowConvenienceLogon = property(get_DisallowConvenienceLogon, put_DisallowConvenienceLogon)
    MinPasswordComplexCharacters = property(get_MinPasswordComplexCharacters, put_MinPasswordComplexCharacters)
    PasswordExpiration = property(get_PasswordExpiration, put_PasswordExpiration)
    PasswordHistory = property(get_PasswordHistory, put_PasswordHistory)
    MaxPasswordFailedAttempts = property(get_MaxPasswordFailedAttempts, put_MaxPasswordFailedAttempts)
    MaxInactivityTimeLock = property(get_MaxInactivityTimeLock, put_MaxInactivityTimeLock)
class EasComplianceResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.EasComplianceResults'
    @winrt_mixinmethod
    def get_Compliant(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequireEncryptionResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasRequireEncryptionResult: ...
    @winrt_mixinmethod
    def get_MinPasswordLengthResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordLengthResult: ...
    @winrt_mixinmethod
    def get_DisallowConvenienceLogonResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasDisallowConvenienceLogonResult: ...
    @winrt_mixinmethod
    def get_MinPasswordComplexCharactersResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordComplexCharactersResult: ...
    @winrt_mixinmethod
    def get_PasswordExpirationResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordExpirationResult: ...
    @winrt_mixinmethod
    def get_PasswordHistoryResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordHistoryResult: ...
    @winrt_mixinmethod
    def get_MaxPasswordFailedAttemptsResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxPasswordFailedAttemptsResult: ...
    @winrt_mixinmethod
    def get_MaxInactivityTimeLockResult(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxInactivityTimeLockResult: ...
    @winrt_mixinmethod
    def get_EncryptionProviderType(self: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults2) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasEncryptionProviderType: ...
    Compliant = property(get_Compliant, None)
    RequireEncryptionResult = property(get_RequireEncryptionResult, None)
    MinPasswordLengthResult = property(get_MinPasswordLengthResult, None)
    DisallowConvenienceLogonResult = property(get_DisallowConvenienceLogonResult, None)
    MinPasswordComplexCharactersResult = property(get_MinPasswordComplexCharactersResult, None)
    PasswordExpirationResult = property(get_PasswordExpirationResult, None)
    PasswordHistoryResult = property(get_PasswordHistoryResult, None)
    MaxPasswordFailedAttemptsResult = property(get_MaxPasswordFailedAttemptsResult, None)
    MaxInactivityTimeLockResult = property(get_MaxInactivityTimeLockResult, None)
    EncryptionProviderType = property(get_EncryptionProviderType, None)
EasContract: UInt32 = 65536
EasDisallowConvenienceLogonResult = Int32
EasDisallowConvenienceLogonResult_NotEvaluated: EasDisallowConvenienceLogonResult = 0
EasDisallowConvenienceLogonResult_Compliant: EasDisallowConvenienceLogonResult = 1
EasDisallowConvenienceLogonResult_CanBeCompliant: EasDisallowConvenienceLogonResult = 2
EasDisallowConvenienceLogonResult_RequestedPolicyIsStricter: EasDisallowConvenienceLogonResult = 3
EasEncryptionProviderType = Int32
EasEncryptionProviderType_NotEvaluated: EasEncryptionProviderType = 0
EasEncryptionProviderType_WindowsEncryption: EasEncryptionProviderType = 1
EasEncryptionProviderType_OtherEncryption: EasEncryptionProviderType = 2
EasMaxInactivityTimeLockResult = Int32
EasMaxInactivityTimeLockResult_NotEvaluated: EasMaxInactivityTimeLockResult = 0
EasMaxInactivityTimeLockResult_Compliant: EasMaxInactivityTimeLockResult = 1
EasMaxInactivityTimeLockResult_CanBeCompliant: EasMaxInactivityTimeLockResult = 2
EasMaxInactivityTimeLockResult_RequestedPolicyIsStricter: EasMaxInactivityTimeLockResult = 3
EasMaxInactivityTimeLockResult_InvalidParameter: EasMaxInactivityTimeLockResult = 4
EasMaxPasswordFailedAttemptsResult = Int32
EasMaxPasswordFailedAttemptsResult_NotEvaluated: EasMaxPasswordFailedAttemptsResult = 0
EasMaxPasswordFailedAttemptsResult_Compliant: EasMaxPasswordFailedAttemptsResult = 1
EasMaxPasswordFailedAttemptsResult_CanBeCompliant: EasMaxPasswordFailedAttemptsResult = 2
EasMaxPasswordFailedAttemptsResult_RequestedPolicyIsStricter: EasMaxPasswordFailedAttemptsResult = 3
EasMaxPasswordFailedAttemptsResult_InvalidParameter: EasMaxPasswordFailedAttemptsResult = 4
EasMinPasswordComplexCharactersResult = Int32
EasMinPasswordComplexCharactersResult_NotEvaluated: EasMinPasswordComplexCharactersResult = 0
EasMinPasswordComplexCharactersResult_Compliant: EasMinPasswordComplexCharactersResult = 1
EasMinPasswordComplexCharactersResult_CanBeCompliant: EasMinPasswordComplexCharactersResult = 2
EasMinPasswordComplexCharactersResult_RequestedPolicyIsStricter: EasMinPasswordComplexCharactersResult = 3
EasMinPasswordComplexCharactersResult_RequestedPolicyNotEnforceable: EasMinPasswordComplexCharactersResult = 4
EasMinPasswordComplexCharactersResult_InvalidParameter: EasMinPasswordComplexCharactersResult = 5
EasMinPasswordComplexCharactersResult_CurrentUserHasBlankPassword: EasMinPasswordComplexCharactersResult = 6
EasMinPasswordComplexCharactersResult_AdminsHaveBlankPassword: EasMinPasswordComplexCharactersResult = 7
EasMinPasswordComplexCharactersResult_UserCannotChangePassword: EasMinPasswordComplexCharactersResult = 8
EasMinPasswordComplexCharactersResult_AdminsCannotChangePassword: EasMinPasswordComplexCharactersResult = 9
EasMinPasswordComplexCharactersResult_LocalControlledUsersCannotChangePassword: EasMinPasswordComplexCharactersResult = 10
EasMinPasswordComplexCharactersResult_ConnectedAdminsProviderPolicyIsWeak: EasMinPasswordComplexCharactersResult = 11
EasMinPasswordComplexCharactersResult_ConnectedUserProviderPolicyIsWeak: EasMinPasswordComplexCharactersResult = 12
EasMinPasswordComplexCharactersResult_ChangeConnectedAdminsPassword: EasMinPasswordComplexCharactersResult = 13
EasMinPasswordComplexCharactersResult_ChangeConnectedUserPassword: EasMinPasswordComplexCharactersResult = 14
EasMinPasswordLengthResult = Int32
EasMinPasswordLengthResult_NotEvaluated: EasMinPasswordLengthResult = 0
EasMinPasswordLengthResult_Compliant: EasMinPasswordLengthResult = 1
EasMinPasswordLengthResult_CanBeCompliant: EasMinPasswordLengthResult = 2
EasMinPasswordLengthResult_RequestedPolicyIsStricter: EasMinPasswordLengthResult = 3
EasMinPasswordLengthResult_RequestedPolicyNotEnforceable: EasMinPasswordLengthResult = 4
EasMinPasswordLengthResult_InvalidParameter: EasMinPasswordLengthResult = 5
EasMinPasswordLengthResult_CurrentUserHasBlankPassword: EasMinPasswordLengthResult = 6
EasMinPasswordLengthResult_AdminsHaveBlankPassword: EasMinPasswordLengthResult = 7
EasMinPasswordLengthResult_UserCannotChangePassword: EasMinPasswordLengthResult = 8
EasMinPasswordLengthResult_AdminsCannotChangePassword: EasMinPasswordLengthResult = 9
EasMinPasswordLengthResult_LocalControlledUsersCannotChangePassword: EasMinPasswordLengthResult = 10
EasMinPasswordLengthResult_ConnectedAdminsProviderPolicyIsWeak: EasMinPasswordLengthResult = 11
EasMinPasswordLengthResult_ConnectedUserProviderPolicyIsWeak: EasMinPasswordLengthResult = 12
EasMinPasswordLengthResult_ChangeConnectedAdminsPassword: EasMinPasswordLengthResult = 13
EasMinPasswordLengthResult_ChangeConnectedUserPassword: EasMinPasswordLengthResult = 14
EasPasswordExpirationResult = Int32
EasPasswordExpirationResult_NotEvaluated: EasPasswordExpirationResult = 0
EasPasswordExpirationResult_Compliant: EasPasswordExpirationResult = 1
EasPasswordExpirationResult_CanBeCompliant: EasPasswordExpirationResult = 2
EasPasswordExpirationResult_RequestedPolicyIsStricter: EasPasswordExpirationResult = 3
EasPasswordExpirationResult_RequestedExpirationIncompatible: EasPasswordExpirationResult = 4
EasPasswordExpirationResult_InvalidParameter: EasPasswordExpirationResult = 5
EasPasswordExpirationResult_UserCannotChangePassword: EasPasswordExpirationResult = 6
EasPasswordExpirationResult_AdminsCannotChangePassword: EasPasswordExpirationResult = 7
EasPasswordExpirationResult_LocalControlledUsersCannotChangePassword: EasPasswordExpirationResult = 8
EasPasswordHistoryResult = Int32
EasPasswordHistoryResult_NotEvaluated: EasPasswordHistoryResult = 0
EasPasswordHistoryResult_Compliant: EasPasswordHistoryResult = 1
EasPasswordHistoryResult_CanBeCompliant: EasPasswordHistoryResult = 2
EasPasswordHistoryResult_RequestedPolicyIsStricter: EasPasswordHistoryResult = 3
EasPasswordHistoryResult_InvalidParameter: EasPasswordHistoryResult = 4
EasRequireEncryptionResult = Int32
EasRequireEncryptionResult_NotEvaluated: EasRequireEncryptionResult = 0
EasRequireEncryptionResult_Compliant: EasRequireEncryptionResult = 1
EasRequireEncryptionResult_CanBeCompliant: EasRequireEncryptionResult = 2
EasRequireEncryptionResult_NotProvisionedOnAllVolumes: EasRequireEncryptionResult = 3
EasRequireEncryptionResult_DeFixedDataNotSupported: EasRequireEncryptionResult = 4
EasRequireEncryptionResult_FixedDataNotSupported: EasRequireEncryptionResult = 4
EasRequireEncryptionResult_DeHardwareNotCompliant: EasRequireEncryptionResult = 5
EasRequireEncryptionResult_HardwareNotCompliant: EasRequireEncryptionResult = 5
EasRequireEncryptionResult_DeWinReNotConfigured: EasRequireEncryptionResult = 6
EasRequireEncryptionResult_LockNotConfigured: EasRequireEncryptionResult = 6
EasRequireEncryptionResult_DeProtectionSuspended: EasRequireEncryptionResult = 7
EasRequireEncryptionResult_ProtectionSuspended: EasRequireEncryptionResult = 7
EasRequireEncryptionResult_DeOsVolumeNotProtected: EasRequireEncryptionResult = 8
EasRequireEncryptionResult_OsVolumeNotProtected: EasRequireEncryptionResult = 8
EasRequireEncryptionResult_DeProtectionNotYetEnabled: EasRequireEncryptionResult = 9
EasRequireEncryptionResult_ProtectionNotYetEnabled: EasRequireEncryptionResult = 9
EasRequireEncryptionResult_NoFeatureLicense: EasRequireEncryptionResult = 10
EasRequireEncryptionResult_OsNotProtected: EasRequireEncryptionResult = 11
EasRequireEncryptionResult_UnexpectedFailure: EasRequireEncryptionResult = 12
class IEasClientDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation'
    _iid_ = Guid('{54dfd981-1968-4ca3-b958-e595d16505eb}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_OperatingSystem(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SystemManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SystemProductName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SystemSku(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
class IEasClientDeviceInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation2'
    _iid_ = Guid('{ffb35923-bb26-4d6a-81bc-165aee0ad754}')
    @winrt_commethod(6)
    def get_SystemHardwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SystemFirmwareVersion(self) -> WinRT_String: ...
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
class IEasClientSecurityPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy'
    _iid_ = Guid('{45b72362-dfba-4a9b-aced-6fe2adcb6420}')
    @winrt_commethod(6)
    def get_RequireEncryption(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_RequireEncryption(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MinPasswordLength(self) -> Byte: ...
    @winrt_commethod(9)
    def put_MinPasswordLength(self, value: Byte) -> Void: ...
    @winrt_commethod(10)
    def get_DisallowConvenienceLogon(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_DisallowConvenienceLogon(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_MinPasswordComplexCharacters(self) -> Byte: ...
    @winrt_commethod(13)
    def put_MinPasswordComplexCharacters(self, value: Byte) -> Void: ...
    @winrt_commethod(14)
    def get_PasswordExpiration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_PasswordExpiration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def get_PasswordHistory(self) -> UInt32: ...
    @winrt_commethod(17)
    def put_PasswordHistory(self, value: UInt32) -> Void: ...
    @winrt_commethod(18)
    def get_MaxPasswordFailedAttempts(self) -> Byte: ...
    @winrt_commethod(19)
    def put_MaxPasswordFailedAttempts(self, value: Byte) -> Void: ...
    @winrt_commethod(20)
    def get_MaxInactivityTimeLock(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(21)
    def put_MaxInactivityTimeLock(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(22)
    def CheckCompliance(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasComplianceResults: ...
    @winrt_commethod(23)
    def ApplyAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasComplianceResults]: ...
    RequireEncryption = property(get_RequireEncryption, put_RequireEncryption)
    MinPasswordLength = property(get_MinPasswordLength, put_MinPasswordLength)
    DisallowConvenienceLogon = property(get_DisallowConvenienceLogon, put_DisallowConvenienceLogon)
    MinPasswordComplexCharacters = property(get_MinPasswordComplexCharacters, put_MinPasswordComplexCharacters)
    PasswordExpiration = property(get_PasswordExpiration, put_PasswordExpiration)
    PasswordHistory = property(get_PasswordHistory, put_PasswordHistory)
    MaxPasswordFailedAttempts = property(get_MaxPasswordFailedAttempts, put_MaxPasswordFailedAttempts)
    MaxInactivityTimeLock = property(get_MaxInactivityTimeLock, put_MaxInactivityTimeLock)
class IEasComplianceResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults'
    _iid_ = Guid('{463c299c-7f19-4c66-b403-cb45dd57a2b3}')
    @winrt_commethod(6)
    def get_Compliant(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_RequireEncryptionResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasRequireEncryptionResult: ...
    @winrt_commethod(8)
    def get_MinPasswordLengthResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordLengthResult: ...
    @winrt_commethod(9)
    def get_DisallowConvenienceLogonResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasDisallowConvenienceLogonResult: ...
    @winrt_commethod(10)
    def get_MinPasswordComplexCharactersResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordComplexCharactersResult: ...
    @winrt_commethod(11)
    def get_PasswordExpirationResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordExpirationResult: ...
    @winrt_commethod(12)
    def get_PasswordHistoryResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordHistoryResult: ...
    @winrt_commethod(13)
    def get_MaxPasswordFailedAttemptsResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxPasswordFailedAttemptsResult: ...
    @winrt_commethod(14)
    def get_MaxInactivityTimeLockResult(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxInactivityTimeLockResult: ...
    Compliant = property(get_Compliant, None)
    RequireEncryptionResult = property(get_RequireEncryptionResult, None)
    MinPasswordLengthResult = property(get_MinPasswordLengthResult, None)
    DisallowConvenienceLogonResult = property(get_DisallowConvenienceLogonResult, None)
    MinPasswordComplexCharactersResult = property(get_MinPasswordComplexCharactersResult, None)
    PasswordExpirationResult = property(get_PasswordExpirationResult, None)
    PasswordHistoryResult = property(get_PasswordHistoryResult, None)
    MaxPasswordFailedAttemptsResult = property(get_MaxPasswordFailedAttemptsResult, None)
    MaxInactivityTimeLockResult = property(get_MaxInactivityTimeLockResult, None)
class IEasComplianceResults2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults2'
    _iid_ = Guid('{2fbe60c9-1aa8-47f5-88bb-cb3ef0bffb15}')
    @winrt_commethod(6)
    def get_EncryptionProviderType(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasEncryptionProviderType: ...
    EncryptionProviderType = property(get_EncryptionProviderType, None)
make_ready(__name__)
