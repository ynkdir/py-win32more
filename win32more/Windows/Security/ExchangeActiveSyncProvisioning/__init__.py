from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Security.ExchangeActiveSyncProvisioning
import win32more.Windows.Win32.System.WinRT
class EasClientDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    FriendlyName = property(get_FriendlyName, None)
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
class EasClientSecurityPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.ExchangeActiveSyncProvisioning.IEasClientSecurityPolicy
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.EasClientSecurityPolicy'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasClientSecurityPolicy.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    DisallowConvenienceLogon = property(get_DisallowConvenienceLogon, put_DisallowConvenienceLogon)
    MaxInactivityTimeLock = property(get_MaxInactivityTimeLock, put_MaxInactivityTimeLock)
    MaxPasswordFailedAttempts = property(get_MaxPasswordFailedAttempts, put_MaxPasswordFailedAttempts)
    MinPasswordComplexCharacters = property(get_MinPasswordComplexCharacters, put_MinPasswordComplexCharacters)
    MinPasswordLength = property(get_MinPasswordLength, put_MinPasswordLength)
    PasswordExpiration = property(get_PasswordExpiration, put_PasswordExpiration)
    PasswordHistory = property(get_PasswordHistory, put_PasswordHistory)
    RequireEncryption = property(get_RequireEncryption, put_RequireEncryption)
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
    DisallowConvenienceLogonResult = property(get_DisallowConvenienceLogonResult, None)
    EncryptionProviderType = property(get_EncryptionProviderType, None)
    MaxInactivityTimeLockResult = property(get_MaxInactivityTimeLockResult, None)
    MaxPasswordFailedAttemptsResult = property(get_MaxPasswordFailedAttemptsResult, None)
    MinPasswordComplexCharactersResult = property(get_MinPasswordComplexCharactersResult, None)
    MinPasswordLengthResult = property(get_MinPasswordLengthResult, None)
    PasswordExpirationResult = property(get_PasswordExpirationResult, None)
    PasswordHistoryResult = property(get_PasswordHistoryResult, None)
    RequireEncryptionResult = property(get_RequireEncryptionResult, None)
EasContract: UInt32 = 65536
class EasDisallowConvenienceLogonResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
class EasEncryptionProviderType(Enum, Int32):
    NotEvaluated = 0
    WindowsEncryption = 1
    OtherEncryption = 2
class EasMaxInactivityTimeLockResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    InvalidParameter = 4
class EasMaxPasswordFailedAttemptsResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    InvalidParameter = 4
class EasMinPasswordComplexCharactersResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    RequestedPolicyNotEnforceable = 4
    InvalidParameter = 5
    CurrentUserHasBlankPassword = 6
    AdminsHaveBlankPassword = 7
    UserCannotChangePassword = 8
    AdminsCannotChangePassword = 9
    LocalControlledUsersCannotChangePassword = 10
    ConnectedAdminsProviderPolicyIsWeak = 11
    ConnectedUserProviderPolicyIsWeak = 12
    ChangeConnectedAdminsPassword = 13
    ChangeConnectedUserPassword = 14
class EasMinPasswordLengthResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    RequestedPolicyNotEnforceable = 4
    InvalidParameter = 5
    CurrentUserHasBlankPassword = 6
    AdminsHaveBlankPassword = 7
    UserCannotChangePassword = 8
    AdminsCannotChangePassword = 9
    LocalControlledUsersCannotChangePassword = 10
    ConnectedAdminsProviderPolicyIsWeak = 11
    ConnectedUserProviderPolicyIsWeak = 12
    ChangeConnectedAdminsPassword = 13
    ChangeConnectedUserPassword = 14
class EasPasswordExpirationResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    RequestedExpirationIncompatible = 4
    InvalidParameter = 5
    UserCannotChangePassword = 6
    AdminsCannotChangePassword = 7
    LocalControlledUsersCannotChangePassword = 8
class EasPasswordHistoryResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    RequestedPolicyIsStricter = 3
    InvalidParameter = 4
class EasRequireEncryptionResult(Enum, Int32):
    NotEvaluated = 0
    Compliant = 1
    CanBeCompliant = 2
    NotProvisionedOnAllVolumes = 3
    DeFixedDataNotSupported = 4
    FixedDataNotSupported = 4
    DeHardwareNotCompliant = 5
    HardwareNotCompliant = 5
    DeWinReNotConfigured = 6
    LockNotConfigured = 6
    DeProtectionSuspended = 7
    ProtectionSuspended = 7
    DeOsVolumeNotProtected = 8
    OsVolumeNotProtected = 8
    DeProtectionNotYetEnabled = 9
    ProtectionNotYetEnabled = 9
    NoFeatureLicense = 10
    OsNotProtected = 11
    UnexpectedFailure = 12
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
    FriendlyName = property(get_FriendlyName, None)
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
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
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
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
    DisallowConvenienceLogon = property(get_DisallowConvenienceLogon, put_DisallowConvenienceLogon)
    MaxInactivityTimeLock = property(get_MaxInactivityTimeLock, put_MaxInactivityTimeLock)
    MaxPasswordFailedAttempts = property(get_MaxPasswordFailedAttempts, put_MaxPasswordFailedAttempts)
    MinPasswordComplexCharacters = property(get_MinPasswordComplexCharacters, put_MinPasswordComplexCharacters)
    MinPasswordLength = property(get_MinPasswordLength, put_MinPasswordLength)
    PasswordExpiration = property(get_PasswordExpiration, put_PasswordExpiration)
    PasswordHistory = property(get_PasswordHistory, put_PasswordHistory)
    RequireEncryption = property(get_RequireEncryption, put_RequireEncryption)
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
    DisallowConvenienceLogonResult = property(get_DisallowConvenienceLogonResult, None)
    MaxInactivityTimeLockResult = property(get_MaxInactivityTimeLockResult, None)
    MaxPasswordFailedAttemptsResult = property(get_MaxPasswordFailedAttemptsResult, None)
    MinPasswordComplexCharactersResult = property(get_MinPasswordComplexCharactersResult, None)
    MinPasswordLengthResult = property(get_MinPasswordLengthResult, None)
    PasswordExpirationResult = property(get_PasswordExpirationResult, None)
    PasswordHistoryResult = property(get_PasswordHistoryResult, None)
    RequireEncryptionResult = property(get_RequireEncryptionResult, None)
class IEasComplianceResults2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.ExchangeActiveSyncProvisioning.IEasComplianceResults2'
    _iid_ = Guid('{2fbe60c9-1aa8-47f5-88bb-cb3ef0bffb15}')
    @winrt_commethod(6)
    def get_EncryptionProviderType(self) -> win32more.Windows.Security.ExchangeActiveSyncProvisioning.EasEncryptionProviderType: ...
    EncryptionProviderType = property(get_EncryptionProviderType, None)


make_ready(__name__)
