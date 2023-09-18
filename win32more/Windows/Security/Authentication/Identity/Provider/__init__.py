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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Identity.Provider
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
    DeviceNonce = property(get_DeviceNonce, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
class ISecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult'
    _iid_ = Guid('{9cbb5987-ef6d-4bc2-bf49-4617515a0f9a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_commethod(7)
    def get_Authentication(self) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Status = property(get_Status, None)
    Authentication = property(get_Authentication, None)
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
    Stage = property(get_Stage, None)
    Scenario = property(get_Scenario, None)
    DeviceId = property(get_DeviceId, None)
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
    DeviceId = property(get_DeviceId, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
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
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
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
    Status = property(get_Status, None)
    Registration = property(get_Registration, None)
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
    ServiceAuthenticationHmac = property(get_ServiceAuthenticationHmac, None)
    SessionNonce = property(get_SessionNonce, None)
    DeviceNonce = property(get_DeviceNonce, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
SecondaryAuthenticationFactorAuthenticationMessage = Int32
SecondaryAuthenticationFactorAuthenticationMessage_Invalid: SecondaryAuthenticationFactorAuthenticationMessage = 0
SecondaryAuthenticationFactorAuthenticationMessage_SwipeUpWelcome: SecondaryAuthenticationFactorAuthenticationMessage = 1
SecondaryAuthenticationFactorAuthenticationMessage_TapWelcome: SecondaryAuthenticationFactorAuthenticationMessage = 2
SecondaryAuthenticationFactorAuthenticationMessage_DeviceNeedsAttention: SecondaryAuthenticationFactorAuthenticationMessage = 3
SecondaryAuthenticationFactorAuthenticationMessage_LookingForDevice: SecondaryAuthenticationFactorAuthenticationMessage = 4
SecondaryAuthenticationFactorAuthenticationMessage_LookingForDevicePluggedin: SecondaryAuthenticationFactorAuthenticationMessage = 5
SecondaryAuthenticationFactorAuthenticationMessage_BluetoothIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 6
SecondaryAuthenticationFactorAuthenticationMessage_NfcIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 7
SecondaryAuthenticationFactorAuthenticationMessage_WiFiIsDisabled: SecondaryAuthenticationFactorAuthenticationMessage = 8
SecondaryAuthenticationFactorAuthenticationMessage_ExtraTapIsRequired: SecondaryAuthenticationFactorAuthenticationMessage = 9
SecondaryAuthenticationFactorAuthenticationMessage_DisabledByPolicy: SecondaryAuthenticationFactorAuthenticationMessage = 10
SecondaryAuthenticationFactorAuthenticationMessage_TapOnDeviceRequired: SecondaryAuthenticationFactorAuthenticationMessage = 11
SecondaryAuthenticationFactorAuthenticationMessage_HoldFinger: SecondaryAuthenticationFactorAuthenticationMessage = 12
SecondaryAuthenticationFactorAuthenticationMessage_ScanFinger: SecondaryAuthenticationFactorAuthenticationMessage = 13
SecondaryAuthenticationFactorAuthenticationMessage_UnauthorizedUser: SecondaryAuthenticationFactorAuthenticationMessage = 14
SecondaryAuthenticationFactorAuthenticationMessage_ReregisterRequired: SecondaryAuthenticationFactorAuthenticationMessage = 15
SecondaryAuthenticationFactorAuthenticationMessage_TryAgain: SecondaryAuthenticationFactorAuthenticationMessage = 16
SecondaryAuthenticationFactorAuthenticationMessage_SayPassphrase: SecondaryAuthenticationFactorAuthenticationMessage = 17
SecondaryAuthenticationFactorAuthenticationMessage_ReadyToSignIn: SecondaryAuthenticationFactorAuthenticationMessage = 18
SecondaryAuthenticationFactorAuthenticationMessage_UseAnotherSignInOption: SecondaryAuthenticationFactorAuthenticationMessage = 19
SecondaryAuthenticationFactorAuthenticationMessage_ConnectionRequired: SecondaryAuthenticationFactorAuthenticationMessage = 20
SecondaryAuthenticationFactorAuthenticationMessage_TimeLimitExceeded: SecondaryAuthenticationFactorAuthenticationMessage = 21
SecondaryAuthenticationFactorAuthenticationMessage_CanceledByUser: SecondaryAuthenticationFactorAuthenticationMessage = 22
SecondaryAuthenticationFactorAuthenticationMessage_CenterHand: SecondaryAuthenticationFactorAuthenticationMessage = 23
SecondaryAuthenticationFactorAuthenticationMessage_MoveHandCloser: SecondaryAuthenticationFactorAuthenticationMessage = 24
SecondaryAuthenticationFactorAuthenticationMessage_MoveHandFarther: SecondaryAuthenticationFactorAuthenticationMessage = 25
SecondaryAuthenticationFactorAuthenticationMessage_PlaceHandAbove: SecondaryAuthenticationFactorAuthenticationMessage = 26
SecondaryAuthenticationFactorAuthenticationMessage_RecognitionFailed: SecondaryAuthenticationFactorAuthenticationMessage = 27
SecondaryAuthenticationFactorAuthenticationMessage_DeviceUnavailable: SecondaryAuthenticationFactorAuthenticationMessage = 28
class SecondaryAuthenticationFactorAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult
    _classid_ = 'Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_Authentication(self: win32more.Windows.Security.Authentication.Identity.Provider.ISecondaryAuthenticationFactorAuthenticationResult) -> win32more.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthentication: ...
    Status = property(get_Status, None)
    Authentication = property(get_Authentication, None)
SecondaryAuthenticationFactorAuthenticationScenario = Int32
SecondaryAuthenticationFactorAuthenticationScenario_SignIn: SecondaryAuthenticationFactorAuthenticationScenario = 0
SecondaryAuthenticationFactorAuthenticationScenario_CredentialPrompt: SecondaryAuthenticationFactorAuthenticationScenario = 1
SecondaryAuthenticationFactorAuthenticationStage = Int32
SecondaryAuthenticationFactorAuthenticationStage_NotStarted: SecondaryAuthenticationFactorAuthenticationStage = 0
SecondaryAuthenticationFactorAuthenticationStage_WaitingForUserConfirmation: SecondaryAuthenticationFactorAuthenticationStage = 1
SecondaryAuthenticationFactorAuthenticationStage_CollectingCredential: SecondaryAuthenticationFactorAuthenticationStage = 2
SecondaryAuthenticationFactorAuthenticationStage_SuspendingAuthentication: SecondaryAuthenticationFactorAuthenticationStage = 3
SecondaryAuthenticationFactorAuthenticationStage_CredentialCollected: SecondaryAuthenticationFactorAuthenticationStage = 4
SecondaryAuthenticationFactorAuthenticationStage_CredentialAuthenticated: SecondaryAuthenticationFactorAuthenticationStage = 5
SecondaryAuthenticationFactorAuthenticationStage_StoppingAuthentication: SecondaryAuthenticationFactorAuthenticationStage = 6
SecondaryAuthenticationFactorAuthenticationStage_ReadyForLock: SecondaryAuthenticationFactorAuthenticationStage = 7
SecondaryAuthenticationFactorAuthenticationStage_CheckingDevicePresence: SecondaryAuthenticationFactorAuthenticationStage = 8
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
    Stage = property(get_Stage, None)
    Scenario = property(get_Scenario, None)
    DeviceId = property(get_DeviceId, None)
SecondaryAuthenticationFactorAuthenticationStatus = Int32
SecondaryAuthenticationFactorAuthenticationStatus_Failed: SecondaryAuthenticationFactorAuthenticationStatus = 0
SecondaryAuthenticationFactorAuthenticationStatus_Started: SecondaryAuthenticationFactorAuthenticationStatus = 1
SecondaryAuthenticationFactorAuthenticationStatus_UnknownDevice: SecondaryAuthenticationFactorAuthenticationStatus = 2
SecondaryAuthenticationFactorAuthenticationStatus_DisabledByPolicy: SecondaryAuthenticationFactorAuthenticationStatus = 3
SecondaryAuthenticationFactorAuthenticationStatus_InvalidAuthenticationStage: SecondaryAuthenticationFactorAuthenticationStatus = 4
SecondaryAuthenticationFactorDeviceCapabilities = UInt32
SecondaryAuthenticationFactorDeviceCapabilities_None: SecondaryAuthenticationFactorDeviceCapabilities = 0
SecondaryAuthenticationFactorDeviceCapabilities_SecureStorage: SecondaryAuthenticationFactorDeviceCapabilities = 1
SecondaryAuthenticationFactorDeviceCapabilities_StoreKeys: SecondaryAuthenticationFactorDeviceCapabilities = 2
SecondaryAuthenticationFactorDeviceCapabilities_ConfirmUserIntentToAuthenticate: SecondaryAuthenticationFactorDeviceCapabilities = 4
SecondaryAuthenticationFactorDeviceCapabilities_SupportSecureUserPresenceCheck: SecondaryAuthenticationFactorDeviceCapabilities = 8
SecondaryAuthenticationFactorDeviceCapabilities_TransmittedDataIsEncrypted: SecondaryAuthenticationFactorDeviceCapabilities = 16
SecondaryAuthenticationFactorDeviceCapabilities_HMacSha256: SecondaryAuthenticationFactorDeviceCapabilities = 32
SecondaryAuthenticationFactorDeviceCapabilities_CloseRangeDataTransmission: SecondaryAuthenticationFactorDeviceCapabilities = 64
SecondaryAuthenticationFactorDeviceFindScope = Int32
SecondaryAuthenticationFactorDeviceFindScope_User: SecondaryAuthenticationFactorDeviceFindScope = 0
SecondaryAuthenticationFactorDeviceFindScope_AllUsers: SecondaryAuthenticationFactorDeviceFindScope = 1
SecondaryAuthenticationFactorDevicePresence = Int32
SecondaryAuthenticationFactorDevicePresence_Absent: SecondaryAuthenticationFactorDevicePresence = 0
SecondaryAuthenticationFactorDevicePresence_Present: SecondaryAuthenticationFactorDevicePresence = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringMode = Int32
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_Unsupported: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 0
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_AppManaged: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringMode_SystemManaged: SecondaryAuthenticationFactorDevicePresenceMonitoringMode = 2
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = Int32
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_Unsupported: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 0
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_Succeeded: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 1
SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus_DisabledByPolicy: SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus = 2
SecondaryAuthenticationFactorFinishAuthenticationStatus = Int32
SecondaryAuthenticationFactorFinishAuthenticationStatus_Failed: SecondaryAuthenticationFactorFinishAuthenticationStatus = 0
SecondaryAuthenticationFactorFinishAuthenticationStatus_Completed: SecondaryAuthenticationFactorFinishAuthenticationStatus = 1
SecondaryAuthenticationFactorFinishAuthenticationStatus_NonceExpired: SecondaryAuthenticationFactorFinishAuthenticationStatus = 2
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
    DeviceId = property(get_DeviceId, None)
    DeviceFriendlyName = property(get_DeviceFriendlyName, None)
    DeviceModelNumber = property(get_DeviceModelNumber, None)
    DeviceConfigurationData = property(get_DeviceConfigurationData, None)
    PresenceMonitoringMode = property(get_PresenceMonitoringMode, None)
    IsAuthenticationSupported = property(get_IsAuthenticationSupported, None)
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
    Status = property(get_Status, None)
    Registration = property(get_Registration, None)
SecondaryAuthenticationFactorRegistrationStatus = Int32
SecondaryAuthenticationFactorRegistrationStatus_Failed: SecondaryAuthenticationFactorRegistrationStatus = 0
SecondaryAuthenticationFactorRegistrationStatus_Started: SecondaryAuthenticationFactorRegistrationStatus = 1
SecondaryAuthenticationFactorRegistrationStatus_CanceledByUser: SecondaryAuthenticationFactorRegistrationStatus = 2
SecondaryAuthenticationFactorRegistrationStatus_PinSetupRequired: SecondaryAuthenticationFactorRegistrationStatus = 3
SecondaryAuthenticationFactorRegistrationStatus_DisabledByPolicy: SecondaryAuthenticationFactorRegistrationStatus = 4
make_head(_module, 'ISecondaryAuthenticationFactorAuthentication')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationResult')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStageInfo')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationStatics')
make_head(_module, 'ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics')
make_head(_module, 'ISecondaryAuthenticationFactorInfo')
make_head(_module, 'ISecondaryAuthenticationFactorInfo2')
make_head(_module, 'ISecondaryAuthenticationFactorRegistration')
make_head(_module, 'ISecondaryAuthenticationFactorRegistrationResult')
make_head(_module, 'ISecondaryAuthenticationFactorRegistrationStatics')
make_head(_module, 'SecondaryAuthenticationFactorAuthentication')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationResult')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationStageInfo')
make_head(_module, 'SecondaryAuthenticationFactorInfo')
make_head(_module, 'SecondaryAuthenticationFactorRegistration')
make_head(_module, 'SecondaryAuthenticationFactorRegistrationResult')
