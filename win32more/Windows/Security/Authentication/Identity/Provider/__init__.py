from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Identity.Provider
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ISecondaryAuthenticationFactorAuthentication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication'
    _iid_ = Guid('{020a16e5-6a25-40a3-8c00-50a023f619d1}')
    @winrt_commethod(6)
    def get_ServiceAuthenticationHmac(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_SessionNonce(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_DeviceNonce(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_DeviceConfigurationData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def FinishAuthenticationAsync(self, deviceHmac: win32more.Windows.Storage.Streams.IBuffer, sessionHmac: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorFinishAuthenticationStatus]: ...
    @winrt_commethod(11)
    def AbortAuthenticationAsync(self, errorLogMessage: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    DeviceNonce = property(get_DeviceNonce, None)
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
class ISecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult'
    _iid_ = Guid('{9cbb5987-ef6d-4bc2-bf49-4617515a0f9a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_commethod(7)
    def get_Authentication(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Authentication = property(get_Authentication, None)
    Status = property(get_Status, None)
class ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs'
    _iid_ = Guid('{d4a5ee56-7291-4073-bc1f-ccb8f5afdf96}')
    @winrt_commethod(6)
    def get_StageInfo(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo: ...
    StageInfo = property(get_StageInfo, None)
class ISecondaryAuthenticationFactorAuthenticationStageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo'
    _iid_ = Guid('{56fec28b-e8aa-4c0f-8e4c-a559e73add88}')
    @winrt_commethod(6)
    def get_Stage(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStage: ...
    @winrt_commethod(7)
    def get_Scenario(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationScenario: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Scenario = property(get_Scenario, None)
    Stage = property(get_Stage, None)
class ISecondaryAuthenticationFactorAuthenticationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics'
    _iid_ = Guid('{3f582656-28f8-4e0f-ae8c-5898b9ae2469}')
    @winrt_commethod(6)
    def ShowNotificationMessageAsync(self, deviceName: WinRT_String, message: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StartAuthenticationAsync(self, deviceId: WinRT_String, serviceAuthenticationNonce: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult]: ...
    @winrt_commethod(8)
    def add_AuthenticationStageChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AuthenticationStageChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetAuthenticationStageInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo]: ...
    AuthenticationStageChanged = event()
class ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics'
    _iid_ = Guid('{90499a19-7ef2-4523-951c-a417a24acf93}')
    @winrt_commethod(6)
    def RegisterDevicePresenceMonitoringAsync(self, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_commethod(7)
    def RegisterDevicePresenceMonitoringWithNewDeviceAsync(self, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_commethod(8)
    def UnregisterDevicePresenceMonitoringAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def IsDevicePresenceMonitoringSupported(self) -> Boolean: ...
class ISecondaryAuthenticationFactorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo'
    _iid_ = Guid('{1e2ba861-8533-4fce-839b-ecb72410ac14}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DeviceModelNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DeviceConfigurationData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceId = property(get_DeviceId, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
class ISecondaryAuthenticationFactorInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2'
    _iid_ = Guid('{14d981a3-fc26-4ff7-abc3-48e82a512a0a}')
    @winrt_commethod(6)
    def get_PresenceMonitoringMode(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode: ...
    @winrt_commethod(7)
    def UpdateDevicePresenceAsync(self, presenceState: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresence) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_IsAuthenticationSupported(self) -> Boolean: ...
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
class ISecondaryAuthenticationFactorRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration'
    _iid_ = Guid('{9f4cbbb4-8cba-48b0-840d-dbb22a54c678}')
    @winrt_commethod(6)
    def FinishRegisteringDeviceAsync(self, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def AbortRegisteringDeviceAsync(self, errorLogMessage: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class ISecondaryAuthenticationFactorRegistrationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult'
    _iid_ = Guid('{a4fe35f0-ade3-4981-af6b-ec195921682a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationStatus: ...
    @winrt_commethod(7)
    def get_Registration(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration: ...
    Registration = property(get_Registration, None)
    Status = property(get_Status, None)
class ISecondaryAuthenticationFactorRegistrationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics'
    _iid_ = Guid('{1adf0f65-e3b7-4155-997f-b756ef65beba}')
    @winrt_commethod(6)
    def RequestStartRegisteringDeviceAsync(self, deviceId: WinRT_String, capabilities: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceCapabilities, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceKey: win32more.Windows.Storage.Streams.IBuffer, mutualAuthenticationKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult]: ...
    @winrt_commethod(7)
    def FindAllRegisteredDeviceInfoAsync(self, queryType: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceFindScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo]]: ...
    @winrt_commethod(8)
    def UnregisterDeviceAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UpdateDeviceConfigurationDataAsync(self, deviceId: WinRT_String, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
class SecondaryAuthenticationFactorAuthentication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication'
    @winrt_mixinmethod
    def get_ServiceAuthenticationHmac(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_SessionNonce(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DeviceNonce(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DeviceConfigurationData(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def FinishAuthenticationAsync(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication, deviceHmac: win32more.Windows.Storage.Streams.IBuffer, sessionHmac: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorFinishAuthenticationStatus]: ...
    @winrt_mixinmethod
    def AbortAuthenticationAsync(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthentication, errorLogMessage: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowNotificationMessageAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, deviceName: WinRT_String, message: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationMessage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def StartAuthenticationAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, deviceId: WinRT_String, serviceAuthenticationNonce: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult]: ...
    @winrt_classmethod
    def add_AuthenticationStageChanged(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AuthenticationStageChanged(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetAuthenticationStageInfoAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo]: ...
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    DeviceNonce = property(get_DeviceNonce, None)
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
class SecondaryAuthenticationFactorAuthenticationMessage(Enum, Int32):
    Invalid = 0
    SwipeUpWelcome = 1
    TapWelcome = 2
    DeviceNeedsAttention = 3
    LookingForDevice = 4
    LookingForDevicePluggedin = 5
    BluetoothIsDisabled = 6
    NfcIsDisabled = 7
    WiFiIsDisabled = 8
    ExtraTapIsRequired = 9
    DisabledByPolicy = 10
    TapOnDeviceRequired = 11
    HoldFinger = 12
    ScanFinger = 13
    UnauthorizedUser = 14
    ReregisterRequired = 15
    TryAgain = 16
    SayPassphrase = 17
    ReadyToSignIn = 18
    UseAnotherSignInOption = 19
    ConnectionRequired = 20
    TimeLimitExceeded = 21
    CanceledByUser = 22
    CenterHand = 23
    MoveHandCloser = 24
    MoveHandFarther = 25
    PlaceHandAbove = 26
    RecognitionFailed = 27
    DeviceUnavailable = 28
class SecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_Authentication(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Authentication = property(get_Authentication, None)
    Status = property(get_Status, None)
class SecondaryAuthenticationFactorAuthenticationScenario(Enum, Int32):
    SignIn = 0
    CredentialPrompt = 1
class SecondaryAuthenticationFactorAuthenticationStage(Enum, Int32):
    NotStarted = 0
    WaitingForUserConfirmation = 1
    CollectingCredential = 2
    SuspendingAuthentication = 3
    CredentialCollected = 4
    CredentialAuthenticated = 5
    StoppingAuthentication = 6
    ReadyForLock = 7
    CheckingDevicePresence = 8
class SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs'
    @winrt_mixinmethod
    def get_StageInfo(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo: ...
    StageInfo = property(get_StageInfo, None)
class SecondaryAuthenticationFactorAuthenticationStageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStageInfo'
    @winrt_mixinmethod
    def get_Stage(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStage: ...
    @winrt_mixinmethod
    def get_Scenario(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationScenario: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationStageInfo) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Scenario = property(get_Scenario, None)
    Stage = property(get_Stage, None)
class SecondaryAuthenticationFactorAuthenticationStatus(Enum, Int32):
    Failed = 0
    Started = 1
    UnknownDevice = 2
    DisabledByPolicy = 3
    InvalidAuthenticationStage = 4
class SecondaryAuthenticationFactorDeviceCapabilities(Enum, UInt32):
    None_ = 0
    SecureStorage = 1
    StoreKeys = 2
    ConfirmUserIntentToAuthenticate = 4
    SupportSecureUserPresenceCheck = 8
    TransmittedDataIsEncrypted = 16
    HMacSha256 = 32
    CloseRangeDataTransmission = 64
class SecondaryAuthenticationFactorDeviceFindScope(Enum, Int32):
    User = 0
    AllUsers = 1
class SecondaryAuthenticationFactorDevicePresence(Enum, Int32):
    Absent = 0
    Present = 1
class SecondaryAuthenticationFactorDevicePresenceMonitoringMode(Enum, Int32):
    Unsupported = 0
    AppManaged = 1
    SystemManaged = 2
class SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus(Enum, Int32):
    Unsupported = 0
    Succeeded = 1
    DisabledByPolicy = 2
class SecondaryAuthenticationFactorFinishAuthenticationStatus(Enum, Int32):
    Failed = 0
    Completed = 1
    NonceExpired = 2
class SecondaryAuthenticationFactorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceFriendlyName(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceModelNumber(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceConfigurationData(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_PresenceMonitoringMode(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode: ...
    @winrt_mixinmethod
    def UpdateDevicePresenceAsync(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2, presenceState: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresence) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_IsAuthenticationSupported(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorInfo2) -> Boolean: ...
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceId = property(get_DeviceId, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
class SecondaryAuthenticationFactorRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration'
    @winrt_mixinmethod
    def FinishRegisteringDeviceAsync(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def AbortRegisteringDeviceAsync(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistration, errorLogMessage: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RegisterDevicePresenceMonitoringAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_classmethod
    def RegisterDevicePresenceMonitoringWithNewDeviceAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String, deviceInstancePath: WinRT_String, monitoringMode: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]: ...
    @winrt_classmethod
    def UnregisterDevicePresenceMonitoringAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def IsDevicePresenceMonitoringSupported(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics) -> Boolean: ...
    @winrt_classmethod
    def RequestStartRegisteringDeviceAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String, capabilities: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceCapabilities, deviceFriendlyName: WinRT_String, deviceModelNumber: WinRT_String, deviceKey: win32more.Windows.Storage.Streams.IBuffer, mutualAuthenticationKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult]: ...
    @winrt_classmethod
    def FindAllRegisteredDeviceInfoAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, queryType: win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceFindScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorInfo]]: ...
    @winrt_classmethod
    def UnregisterDeviceAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def UpdateDeviceConfigurationDataAsync(cls: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationStatics, deviceId: WinRT_String, deviceConfigurationData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
class SecondaryAuthenticationFactorRegistrationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationStatus: ...
    @winrt_mixinmethod
    def get_Registration(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorRegistrationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistration: ...
    Registration = property(get_Registration, None)
    Status = property(get_Status, None)
class SecondaryAuthenticationFactorRegistrationStatus(Enum, Int32):
    Failed = 0
    Started = 1
    CanceledByUser = 2
    PinSetupRequired = 3
    DisabledByPolicy = 4


make_ready(__name__)
