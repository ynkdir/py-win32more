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
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Devices.Sms
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Networking.NetworkOperators
import win32more.Windows.Storage.Streams
DataClasses = UInt32
DataClasses_None: DataClasses = 0
DataClasses_Gprs: DataClasses = 1
DataClasses_Edge: DataClasses = 2
DataClasses_Umts: DataClasses = 4
DataClasses_Hsdpa: DataClasses = 8
DataClasses_Hsupa: DataClasses = 16
DataClasses_LteAdvanced: DataClasses = 32
DataClasses_NewRadioNonStandalone: DataClasses = 64
DataClasses_NewRadioStandalone: DataClasses = 128
DataClasses_Cdma1xRtt: DataClasses = 65536
DataClasses_Cdma1xEvdo: DataClasses = 131072
DataClasses_Cdma1xEvdoRevA: DataClasses = 262144
DataClasses_Cdma1xEvdv: DataClasses = 524288
DataClasses_Cdma3xRtt: DataClasses = 1048576
DataClasses_Cdma1xEvdoRevB: DataClasses = 2097152
DataClasses_CdmaUmb: DataClasses = 4194304
DataClasses_Custom: DataClasses = 2147483648
class ESim(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESim
    _classid_ = 'Windows.Networking.NetworkOperators.ESim'
    @winrt_mixinmethod
    def get_AvailableMemoryInBytes(self: win32more.Windows.Networking.NetworkOperators.IESim) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Eid(self: win32more.Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirmwareVersion(self: win32more.Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MobileBroadbandModemDeviceId(self: win32more.Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: win32more.Windows.Networking.NetworkOperators.IESim) -> win32more.Windows.Networking.NetworkOperators.ESimPolicy: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Networking.NetworkOperators.IESim) -> win32more.Windows.Networking.NetworkOperators.ESimState: ...
    @winrt_mixinmethod
    def GetProfiles(self: win32more.Windows.Networking.NetworkOperators.IESim) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.ESimProfile]: ...
    @winrt_mixinmethod
    def DeleteProfileAsync(self: win32more.Windows.Networking.NetworkOperators.IESim, profileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def DownloadProfileMetadataAsync(self: win32more.Windows.Networking.NetworkOperators.IESim, activationCode: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult]: ...
    @winrt_mixinmethod
    def ResetAsync(self: win32more.Windows.Networking.NetworkOperators.IESim) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def add_ProfileChanged(self: win32more.Windows.Networking.NetworkOperators.IESim, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESim, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProfileChanged(self: win32more.Windows.Networking.NetworkOperators.IESim, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Discover(self: win32more.Windows.Networking.NetworkOperators.IESim2) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_mixinmethod
    def DiscoverWithServerAddressAndMatchingId(self: win32more.Windows.Networking.NetworkOperators.IESim2, serverAddress: WinRT_String, matchingId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_mixinmethod
    def DiscoverAsync(self: win32more.Windows.Networking.NetworkOperators.IESim2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_mixinmethod
    def DiscoverWithServerAddressAndMatchingIdAsync(self: win32more.Windows.Networking.NetworkOperators.IESim2, serverAddress: WinRT_String, matchingId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_mixinmethod
    def get_SlotIndex(self: win32more.Windows.Networking.NetworkOperators.IESim3) -> win32more.Windows.Foundation.IReference[Int32]: ...
    AvailableMemoryInBytes = property(get_AvailableMemoryInBytes, None)
    Eid = property(get_Eid, None)
    FirmwareVersion = property(get_FirmwareVersion, None)
    MobileBroadbandModemDeviceId = property(get_MobileBroadbandModemDeviceId, None)
    Policy = property(get_Policy, None)
    State = property(get_State, None)
    SlotIndex = property(get_SlotIndex, None)
class ESimAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimAddedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.ESimAddedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: win32more.Windows.Networking.NetworkOperators.IESimAddedEventArgs) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
ESimAuthenticationPreference = Int32
ESimAuthenticationPreference_OnEntry: ESimAuthenticationPreference = 0
ESimAuthenticationPreference_OnAction: ESimAuthenticationPreference = 1
ESimAuthenticationPreference_Never: ESimAuthenticationPreference = 2
class ESimDiscoverEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimDiscoverEvent
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDiscoverEvent'
    @winrt_mixinmethod
    def get_MatchingId(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverEvent) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RspServerAddress(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverEvent) -> WinRT_String: ...
    MatchingId = property(get_MatchingId, None)
    RspServerAddress = property(get_RspServerAddress, None)
class ESimDiscoverResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimDiscoverResult
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDiscoverResult'
    @winrt_mixinmethod
    def get_Events(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.ESimDiscoverEvent]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverResult) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResultKind: ...
    @winrt_mixinmethod
    def get_ProfileMetadata(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverResult) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Networking.NetworkOperators.IESimDiscoverResult) -> win32more.Windows.Networking.NetworkOperators.ESimOperationResult: ...
    Events = property(get_Events, None)
    Kind = property(get_Kind, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
ESimDiscoverResultKind = Int32
ESimDiscoverResultKind_None: ESimDiscoverResultKind = 0
ESimDiscoverResultKind_Events: ESimDiscoverResultKind = 1
ESimDiscoverResultKind_ProfileMetadata: ESimDiscoverResultKind = 2
class ESimDownloadProfileMetadataResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> win32more.Windows.Networking.NetworkOperators.ESimOperationResult: ...
    @winrt_mixinmethod
    def get_ProfileMetadata(self: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    Result = property(get_Result, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
class _ESimManager_Meta_(ComPtr.__class__):
    pass
class ESimManager(ComPtr, metaclass=_ESimManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimManager'
    @winrt_classmethod
    def get_ServiceInfo(cls: win32more.Windows.Networking.NetworkOperators.IESimManagerStatics) -> win32more.Windows.Networking.NetworkOperators.ESimServiceInfo: ...
    @winrt_classmethod
    def TryCreateESimWatcher(cls: win32more.Windows.Networking.NetworkOperators.IESimManagerStatics) -> win32more.Windows.Networking.NetworkOperators.ESimWatcher: ...
    @winrt_classmethod
    def add_ServiceInfoChanged(cls: win32more.Windows.Networking.NetworkOperators.IESimManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ServiceInfoChanged(cls: win32more.Windows.Networking.NetworkOperators.IESimManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _ESimManager_Meta_.ServiceInfo = property(get_ServiceInfo.__wrapped__, None)
class ESimOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimOperationResult
    _classid_ = 'Windows.Networking.NetworkOperators.ESimOperationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IESimOperationResult) -> win32more.Windows.Networking.NetworkOperators.ESimOperationStatus: ...
    Status = property(get_Status, None)
ESimOperationStatus = Int32
ESimOperationStatus_Success: ESimOperationStatus = 0
ESimOperationStatus_NotAuthorized: ESimOperationStatus = 1
ESimOperationStatus_NotFound: ESimOperationStatus = 2
ESimOperationStatus_PolicyViolation: ESimOperationStatus = 3
ESimOperationStatus_InsufficientSpaceOnCard: ESimOperationStatus = 4
ESimOperationStatus_ServerFailure: ESimOperationStatus = 5
ESimOperationStatus_ServerNotReachable: ESimOperationStatus = 6
ESimOperationStatus_TimeoutWaitingForUserConsent: ESimOperationStatus = 7
ESimOperationStatus_IncorrectConfirmationCode: ESimOperationStatus = 8
ESimOperationStatus_ConfirmationCodeMaxRetriesExceeded: ESimOperationStatus = 9
ESimOperationStatus_CardRemoved: ESimOperationStatus = 10
ESimOperationStatus_CardBusy: ESimOperationStatus = 11
ESimOperationStatus_Other: ESimOperationStatus = 12
ESimOperationStatus_CardGeneralFailure: ESimOperationStatus = 13
ESimOperationStatus_ConfirmationCodeMissing: ESimOperationStatus = 14
ESimOperationStatus_InvalidMatchingId: ESimOperationStatus = 15
ESimOperationStatus_NoEligibleProfileForThisDevice: ESimOperationStatus = 16
ESimOperationStatus_OperationAborted: ESimOperationStatus = 17
ESimOperationStatus_EidMismatch: ESimOperationStatus = 18
ESimOperationStatus_ProfileNotAvailableForNewBinding: ESimOperationStatus = 19
ESimOperationStatus_ProfileNotReleasedByOperator: ESimOperationStatus = 20
ESimOperationStatus_OperationProhibitedByProfileClass: ESimOperationStatus = 21
ESimOperationStatus_ProfileNotPresent: ESimOperationStatus = 22
ESimOperationStatus_NoCorrespondingRequest: ESimOperationStatus = 23
ESimOperationStatus_TimeoutWaitingForResponse: ESimOperationStatus = 24
ESimOperationStatus_IccidAlreadyExists: ESimOperationStatus = 25
ESimOperationStatus_ProfileProcessingError: ESimOperationStatus = 26
ESimOperationStatus_ServerNotTrusted: ESimOperationStatus = 27
ESimOperationStatus_ProfileDownloadMaxRetriesExceeded: ESimOperationStatus = 28
class ESimPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimPolicy
    _classid_ = 'Windows.Networking.NetworkOperators.ESimPolicy'
    @winrt_mixinmethod
    def get_ShouldEnableManagingUi(self: win32more.Windows.Networking.NetworkOperators.IESimPolicy) -> Boolean: ...
    ShouldEnableManagingUi = property(get_ShouldEnableManagingUi, None)
class ESimProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimProfile
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfile'
    @winrt_mixinmethod
    def get_Class(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Networking.NetworkOperators.ESimProfileClass: ...
    @winrt_mixinmethod
    def get_Nickname(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderIcon(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderName(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Networking.NetworkOperators.ESimProfileState: ...
    @winrt_mixinmethod
    def DisableAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def EnableAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def SetNicknameAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfile, newNickname: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    Class = property(get_Class, None)
    Nickname = property(get_Nickname, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
ESimProfileClass = Int32
ESimProfileClass_Operational: ESimProfileClass = 0
ESimProfileClass_Test: ESimProfileClass = 1
ESimProfileClass_Provisioning: ESimProfileClass = 2
class ESimProfileInstallProgress(EasyCastStructure):
    TotalSizeInBytes: Int32
    InstalledSizeInBytes: Int32
class ESimProfileMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfileMetadata'
    @winrt_mixinmethod
    def get_IsConfirmationCodeRequired(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Boolean: ...
    @winrt_mixinmethod
    def get_Policy(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderIcon(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderName(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadataState: ...
    @winrt_mixinmethod
    def DenyInstallAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def ConfirmInstallAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.NetworkOperators.ESimOperationResult, win32more.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_mixinmethod
    def ConfirmInstallWithConfirmationCodeAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata, confirmationCode: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.NetworkOperators.ESimOperationResult, win32more.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_mixinmethod
    def PostponeInstallAsync(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Networking.NetworkOperators.IESimProfileMetadata, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsConfirmationCodeRequired = property(get_IsConfirmationCodeRequired, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
ESimProfileMetadataState = Int32
ESimProfileMetadataState_Unknown: ESimProfileMetadataState = 0
ESimProfileMetadataState_WaitingForInstall: ESimProfileMetadataState = 1
ESimProfileMetadataState_Downloading: ESimProfileMetadataState = 2
ESimProfileMetadataState_Installing: ESimProfileMetadataState = 3
ESimProfileMetadataState_Expired: ESimProfileMetadataState = 4
ESimProfileMetadataState_RejectingDownload: ESimProfileMetadataState = 5
ESimProfileMetadataState_NoLongerAvailable: ESimProfileMetadataState = 6
ESimProfileMetadataState_DeniedByPolicy: ESimProfileMetadataState = 7
class ESimProfilePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimProfilePolicy
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfilePolicy'
    @winrt_mixinmethod
    def get_CanDelete(self: win32more.Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanDisable(self: win32more.Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsManagedByEnterprise(self: win32more.Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    CanDelete = property(get_CanDelete, None)
    CanDisable = property(get_CanDisable, None)
    IsManagedByEnterprise = property(get_IsManagedByEnterprise, None)
ESimProfileState = Int32
ESimProfileState_Unknown: ESimProfileState = 0
ESimProfileState_Disabled: ESimProfileState = 1
ESimProfileState_Enabled: ESimProfileState = 2
ESimProfileState_Deleted: ESimProfileState = 3
class ESimRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimRemovedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.ESimRemovedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: win32more.Windows.Networking.NetworkOperators.IESimRemovedEventArgs) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class ESimServiceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimServiceInfo
    _classid_ = 'Windows.Networking.NetworkOperators.ESimServiceInfo'
    @winrt_mixinmethod
    def get_AuthenticationPreference(self: win32more.Windows.Networking.NetworkOperators.IESimServiceInfo) -> win32more.Windows.Networking.NetworkOperators.ESimAuthenticationPreference: ...
    @winrt_mixinmethod
    def get_IsESimUiEnabled(self: win32more.Windows.Networking.NetworkOperators.IESimServiceInfo) -> Boolean: ...
    AuthenticationPreference = property(get_AuthenticationPreference, None)
    IsESimUiEnabled = property(get_IsESimUiEnabled, None)
ESimState = Int32
ESimState_Unknown: ESimState = 0
ESimState_Idle: ESimState = 1
ESimState_Removed: ESimState = 2
ESimState_Busy: ESimState = 3
class ESimUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimUpdatedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.ESimUpdatedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: win32more.Windows.Networking.NetworkOperators.IESimUpdatedEventArgs) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class ESimWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimWatcher
    _classid_ = 'Windows.Networking.NetworkOperators.ESimWatcher'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher) -> win32more.Windows.Networking.NetworkOperators.ESimWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Networking.NetworkOperators.IESimWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
ESimWatcherStatus = Int32
ESimWatcherStatus_Created: ESimWatcherStatus = 0
ESimWatcherStatus_Started: ESimWatcherStatus = 1
ESimWatcherStatus_EnumerationCompleted: ESimWatcherStatus = 2
ESimWatcherStatus_Stopping: ESimWatcherStatus = 3
ESimWatcherStatus_Stopped: ESimWatcherStatus = 4
class FdnAccessManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.FdnAccessManager'
    @winrt_classmethod
    def RequestUnlockAsync(cls: win32more.Windows.Networking.NetworkOperators.IFdnAccessManagerStatics, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class HotspotAuthenticationContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotAuthenticationContext'
    @winrt_mixinmethod
    def get_WirelessNetworkId(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> SZArray[Byte]: ...
    @winrt_mixinmethod
    def get_NetworkAdapter(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def get_RedirectMessageUrl(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_RedirectMessageXml(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_AuthenticationUrl(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def IssueCredentials(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> Void: ...
    @winrt_mixinmethod
    def AbortAuthentication(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, markAsManual: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SkipAuthentication(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Void: ...
    @winrt_mixinmethod
    def TriggerAttentionRequired(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, packageRelativeApplicationId: WinRT_String, applicationParameters: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IssueCredentialsAsync(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext2, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult]: ...
    @winrt_classmethod
    def TryGetAuthenticationContext(cls: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContextStatics, evenToken: WinRT_String, context: POINTER(win32more.Windows.Networking.NetworkOperators.HotspotAuthenticationContext)) -> Boolean: ...
    WirelessNetworkId = property(get_WirelessNetworkId, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    RedirectMessageUrl = property(get_RedirectMessageUrl, None)
    RedirectMessageXml = property(get_RedirectMessageXml, None)
    AuthenticationUrl = property(get_AuthenticationUrl, None)
class HotspotAuthenticationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotAuthenticationEventDetails'
    @winrt_mixinmethod
    def get_EventToken(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails) -> WinRT_String: ...
    EventToken = property(get_EventToken, None)
HotspotAuthenticationResponseCode = Int32
HotspotAuthenticationResponseCode_NoError: HotspotAuthenticationResponseCode = 0
HotspotAuthenticationResponseCode_LoginSucceeded: HotspotAuthenticationResponseCode = 50
HotspotAuthenticationResponseCode_LoginFailed: HotspotAuthenticationResponseCode = 100
HotspotAuthenticationResponseCode_RadiusServerError: HotspotAuthenticationResponseCode = 102
HotspotAuthenticationResponseCode_NetworkAdministratorError: HotspotAuthenticationResponseCode = 105
HotspotAuthenticationResponseCode_LoginAborted: HotspotAuthenticationResponseCode = 151
HotspotAuthenticationResponseCode_AccessGatewayInternalError: HotspotAuthenticationResponseCode = 255
class HotspotCredentialsAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult'
    @winrt_mixinmethod
    def get_HasNetworkErrorOccurred(self: win32more.Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResponseCode(self: win32more.Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> win32more.Windows.Networking.NetworkOperators.HotspotAuthenticationResponseCode: ...
    @winrt_mixinmethod
    def get_LogoffUrl(self: win32more.Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AuthenticationReplyXml(self: win32more.Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    ResponseCode = property(get_ResponseCode, None)
    LogoffUrl = property(get_LogoffUrl, None)
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
class IESim(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESim'
    _iid_ = Guid('{6f6e6e26-f123-437d-8ced-dc1d2bc0c3a9}')
    @winrt_commethod(6)
    def get_AvailableMemoryInBytes(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_Eid(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FirmwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MobileBroadbandModemDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Policy(self) -> win32more.Windows.Networking.NetworkOperators.ESimPolicy: ...
    @winrt_commethod(11)
    def get_State(self) -> win32more.Windows.Networking.NetworkOperators.ESimState: ...
    @winrt_commethod(12)
    def GetProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.ESimProfile]: ...
    @winrt_commethod(13)
    def DeleteProfileAsync(self, profileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(14)
    def DownloadProfileMetadataAsync(self, activationCode: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult]: ...
    @winrt_commethod(15)
    def ResetAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(16)
    def add_ProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESim, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AvailableMemoryInBytes = property(get_AvailableMemoryInBytes, None)
    Eid = property(get_Eid, None)
    FirmwareVersion = property(get_FirmwareVersion, None)
    MobileBroadbandModemDeviceId = property(get_MobileBroadbandModemDeviceId, None)
    Policy = property(get_Policy, None)
    State = property(get_State, None)
class IESim2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESim2'
    _iid_ = Guid('{bd4fd0a0-c68f-56eb-b99b-8f34b8100299}')
    @winrt_commethod(6)
    def Discover(self) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_commethod(7)
    def DiscoverWithServerAddressAndMatchingId(self, serverAddress: WinRT_String, matchingId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_commethod(8)
    def DiscoverAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_commethod(9)
    def DiscoverWithServerAddressAndMatchingIdAsync(self, serverAddress: WinRT_String, matchingId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
class IESim3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESim3'
    _iid_ = Guid('{fe1edf45-01b8-5d31-b8d3-d9cbebb2b831}')
    @winrt_commethod(6)
    def get_SlotIndex(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    SlotIndex = property(get_SlotIndex, None)
class IESimAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimAddedEventArgs'
    _iid_ = Guid('{38bd0a58-4d5a-4d08-8da7-e73eff369ddd}')
    @winrt_commethod(6)
    def get_ESim(self) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimDiscoverEvent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimDiscoverEvent'
    _iid_ = Guid('{e59ac3e3-39bc-5f6f-9321-0d4a182d261b}')
    @winrt_commethod(6)
    def get_MatchingId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RspServerAddress(self) -> WinRT_String: ...
    MatchingId = property(get_MatchingId, None)
    RspServerAddress = property(get_RspServerAddress, None)
class IESimDiscoverResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimDiscoverResult'
    _iid_ = Guid('{56b4bb5e-ab2f-5ac6-b359-dd5a8e237926}')
    @winrt_commethod(6)
    def get_Events(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.ESimDiscoverEvent]: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.Networking.NetworkOperators.ESimDiscoverResultKind: ...
    @winrt_commethod(8)
    def get_ProfileMetadata(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    @winrt_commethod(9)
    def get_Result(self) -> win32more.Windows.Networking.NetworkOperators.ESimOperationResult: ...
    Events = property(get_Events, None)
    Kind = property(get_Kind, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
class IESimDownloadProfileMetadataResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult'
    _iid_ = Guid('{c4234d9e-5ad6-426d-8d00-4434f449afec}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Networking.NetworkOperators.ESimOperationResult: ...
    @winrt_commethod(7)
    def get_ProfileMetadata(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    Result = property(get_Result, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
class IESimManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimManagerStatics'
    _iid_ = Guid('{0bfa2c0c-df88-4631-bf04-c12e281b3962}')
    @winrt_commethod(6)
    def get_ServiceInfo(self) -> win32more.Windows.Networking.NetworkOperators.ESimServiceInfo: ...
    @winrt_commethod(7)
    def TryCreateESimWatcher(self) -> win32more.Windows.Networking.NetworkOperators.ESimWatcher: ...
    @winrt_commethod(8)
    def add_ServiceInfoChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ServiceInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ServiceInfo = property(get_ServiceInfo, None)
class IESimOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimOperationResult'
    _iid_ = Guid('{a67b63b1-309b-4e77-9e7e-cd93f1ddc7b9}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.ESimOperationStatus: ...
    Status = property(get_Status, None)
class IESimPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimPolicy'
    _iid_ = Guid('{41e1b99d-cf7e-4315-882b-6f1e74b0d38f}')
    @winrt_commethod(6)
    def get_ShouldEnableManagingUi(self) -> Boolean: ...
    ShouldEnableManagingUi = property(get_ShouldEnableManagingUi, None)
class IESimProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimProfile'
    _iid_ = Guid('{ee1e7880-06a9-4027-b4f8-ddb23d7810e0}')
    @winrt_commethod(6)
    def get_Class(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfileClass: ...
    @winrt_commethod(7)
    def get_Nickname(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Policy(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_commethod(9)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ProviderIcon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ProviderName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_State(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfileState: ...
    @winrt_commethod(14)
    def DisableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(15)
    def EnableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(16)
    def SetNicknameAsync(self, newNickname: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    Class = property(get_Class, None)
    Nickname = property(get_Nickname, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
class IESimProfileMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimProfileMetadata'
    _iid_ = Guid('{ed25831f-90db-498d-a7b4-ebce807d3c23}')
    @winrt_commethod(6)
    def get_IsConfirmationCodeRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Policy(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ProviderIcon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(10)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ProviderName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_State(self) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadataState: ...
    @winrt_commethod(13)
    def DenyInstallAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(14)
    def ConfirmInstallAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.NetworkOperators.ESimOperationResult, win32more.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_commethod(15)
    def ConfirmInstallWithConfirmationCodeAsync(self, confirmationCode: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.NetworkOperators.ESimOperationResult, win32more.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_commethod(16)
    def PostponeInstallAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(17)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsConfirmationCodeRequired = property(get_IsConfirmationCodeRequired, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
class IESimProfilePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimProfilePolicy'
    _iid_ = Guid('{e6dd0f1d-9c5c-46c5-a289-a948999bf062}')
    @winrt_commethod(6)
    def get_CanDelete(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanDisable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsManagedByEnterprise(self) -> Boolean: ...
    CanDelete = property(get_CanDelete, None)
    CanDisable = property(get_CanDisable, None)
    IsManagedByEnterprise = property(get_IsManagedByEnterprise, None)
class IESimRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimRemovedEventArgs'
    _iid_ = Guid('{dec5277b-2fd9-4ed9-8376-d9b5e41278a3}')
    @winrt_commethod(6)
    def get_ESim(self) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimServiceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimServiceInfo'
    _iid_ = Guid('{f16aabcf-7f59-4a51-8494-bd89d5ff50ee}')
    @winrt_commethod(6)
    def get_AuthenticationPreference(self) -> win32more.Windows.Networking.NetworkOperators.ESimAuthenticationPreference: ...
    @winrt_commethod(7)
    def get_IsESimUiEnabled(self) -> Boolean: ...
    AuthenticationPreference = property(get_AuthenticationPreference, None)
    IsESimUiEnabled = property(get_IsESimUiEnabled, None)
class IESimUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimUpdatedEventArgs'
    _iid_ = Guid('{4c125cec-508d-4b88-83cb-68bef8168d12}')
    @winrt_commethod(6)
    def get_ESim(self) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IESimWatcher'
    _iid_ = Guid('{c1f84ceb-a28d-4fbf-9771-6e31b81ccf22}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.ESimWatcherStatus: ...
    @winrt_commethod(7)
    def Start(self) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.ESimWatcher, win32more.Windows.Networking.NetworkOperators.ESimUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IFdnAccessManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IFdnAccessManagerStatics'
    _iid_ = Guid('{f2aa4395-f1e6-4319-aa3e-477ca64b2bdf}')
    @winrt_commethod(6)
    def RequestUnlockAsync(self, contactListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IHotspotAuthenticationContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IHotspotAuthenticationContext'
    _iid_ = Guid('{e756c791-1003-4de5-83c7-de61d88831d0}')
    @winrt_commethod(6)
    def get_WirelessNetworkId(self) -> SZArray[Byte]: ...
    @winrt_commethod(7)
    def get_NetworkAdapter(self) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(8)
    def get_RedirectMessageUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_RedirectMessageXml(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(10)
    def get_AuthenticationUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def IssueCredentials(self, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> Void: ...
    @winrt_commethod(12)
    def AbortAuthentication(self, markAsManual: Boolean) -> Void: ...
    @winrt_commethod(13)
    def SkipAuthentication(self) -> Void: ...
    @winrt_commethod(14)
    def TriggerAttentionRequired(self, packageRelativeApplicationId: WinRT_String, applicationParameters: WinRT_String) -> Void: ...
    WirelessNetworkId = property(get_WirelessNetworkId, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    RedirectMessageUrl = property(get_RedirectMessageUrl, None)
    RedirectMessageXml = property(get_RedirectMessageXml, None)
    AuthenticationUrl = property(get_AuthenticationUrl, None)
class IHotspotAuthenticationContext2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IHotspotAuthenticationContext2'
    _iid_ = Guid('{e756c791-1004-4de5-83c7-de61d88831d0}')
    @winrt_commethod(6)
    def IssueCredentialsAsync(self, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult]: ...
class IHotspotAuthenticationContextStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IHotspotAuthenticationContextStatics'
    _iid_ = Guid('{e756c791-1002-4de5-83c7-de61d88831d0}')
    @winrt_commethod(6)
    def TryGetAuthenticationContext(self, evenToken: WinRT_String, context: POINTER(win32more.Windows.Networking.NetworkOperators.HotspotAuthenticationContext)) -> Boolean: ...
class IHotspotAuthenticationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails'
    _iid_ = Guid('{e756c791-1001-4de5-83c7-de61d88831d0}')
    @winrt_commethod(6)
    def get_EventToken(self) -> WinRT_String: ...
    EventToken = property(get_EventToken, None)
class IHotspotCredentialsAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult'
    _iid_ = Guid('{e756c791-1005-4de5-83c7-de61d88831d0}')
    @winrt_commethod(6)
    def get_HasNetworkErrorOccurred(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ResponseCode(self) -> win32more.Windows.Networking.NetworkOperators.HotspotAuthenticationResponseCode: ...
    @winrt_commethod(8)
    def get_LogoffUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_AuthenticationReplyXml(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    ResponseCode = property(get_ResponseCode, None)
    LogoffUrl = property(get_LogoffUrl, None)
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
class IKnownCSimFilePathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics'
    _iid_ = Guid('{b458aeed-49f1-4c22-b073-96d511bf9c35}')
    @winrt_commethod(6)
    def get_EFSpn(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_Gid1(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid2(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownRuimFilePathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics'
    _iid_ = Guid('{3883c8b9-ff24-4571-a867-09f960426e14}')
    @winrt_commethod(6)
    def get_EFSpn(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_Gid1(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid2(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownSimFilePathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics'
    _iid_ = Guid('{80cd1a63-37a5-43d3-80a3-ccd23e8fecee}')
    @winrt_commethod(6)
    def get_EFOns(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_EFSpn(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid1(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(9)
    def get_Gid2(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFOns = property(get_EFOns, None)
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownUSimFilePathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics'
    _iid_ = Guid('{7c34e581-1f1b-43f4-9530-8b092d32d71f}')
    @winrt_commethod(6)
    def get_EFSpn(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_EFOpl(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_EFPnn(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(9)
    def get_Gid1(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(10)
    def get_Gid2(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    EFOpl = property(get_EFOpl, None)
    EFPnn = property(get_EFPnn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IMobileBroadbandAccount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccount'
    _iid_ = Guid('{36c24ccd-cee2-43e0-a603-ee86a36d6570}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceProviderGuid(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ServiceProviderName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CurrentNetwork(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_commethod(10)
    def get_CurrentDeviceInformation(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
class IMobileBroadbandAccount2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccount2'
    _iid_ = Guid('{38f52f1c-1136-4257-959f-b658a352b6d4}')
    @winrt_commethod(6)
    def GetConnectionProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Connectivity.ConnectionProfile]: ...
class IMobileBroadbandAccount3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccount3'
    _iid_ = Guid('{092a1e21-9379-4b9b-ad31-d5fee2f748c6}')
    @winrt_commethod(6)
    def get_AccountExperienceUrl(self) -> win32more.Windows.Foundation.Uri: ...
    AccountExperienceUrl = property(get_AccountExperienceUrl, None)
class IMobileBroadbandAccountEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccountEventArgs'
    _iid_ = Guid('{3853c880-77de-4c04-bead-a123b08c9f59}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class IMobileBroadbandAccountStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccountStatics'
    _iid_ = Guid('{aa7f4d24-afc1-4fc8-ae9a-a9175310faad}')
    @winrt_commethod(6)
    def get_AvailableNetworkAccountIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    AvailableNetworkAccountIds = property(get_AvailableNetworkAccountIds, None)
class IMobileBroadbandAccountUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs'
    _iid_ = Guid('{7bc31d88-a6bd-49e1-80ab-6b91354a57d4}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HasDeviceInformationChanged(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HasNetworkChanged(self) -> Boolean: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    HasDeviceInformationChanged = property(get_HasDeviceInformationChanged, None)
    HasNetworkChanged = property(get_HasNetworkChanged, None)
class IMobileBroadbandAccountWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher'
    _iid_ = Guid('{6bf3335e-23b5-449f-928d-5e0d3e04471d}')
    @winrt_commethod(6)
    def add_AccountAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountAdded(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_AccountUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AccountUpdated(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AccountRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AccountRemoved(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IMobileBroadbandAntennaSar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar'
    _iid_ = Guid('{b9af4b7e-cbf9-4109-90be-5c06bfd513b6}')
    @winrt_commethod(6)
    def get_AntennaIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def get_SarBackoffIndex(self) -> Int32: ...
    AntennaIndex = property(get_AntennaIndex, None)
    SarBackoffIndex = property(get_SarBackoffIndex, None)
class IMobileBroadbandAntennaSarFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSarFactory'
    _iid_ = Guid('{a91e1716-c04d-4a21-8698-1459dc672c6e}')
    @winrt_commethod(6)
    def CreateWithIndex(self, antennaIndex: Int32, sarBackoffIndex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar: ...
class IMobileBroadbandCellCdma(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma'
    _iid_ = Guid('{0601b3b4-411a-4f2e-8287-76f5650c60cd}')
    @winrt_commethod(6)
    def get_BaseStationId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_BaseStationPNCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_BaseStationLatitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_BaseStationLongitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(10)
    def get_BaseStationLastBroadcastGpsTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def get_NetworkId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(12)
    def get_PilotSignalStrengthInDB(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_SystemId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    NetworkId = property(get_NetworkId, None)
    PilotSignalStrengthInDB = property(get_PilotSignalStrengthInDB, None)
    SystemId = property(get_SystemId, None)
class IMobileBroadbandCellGsm(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm'
    _iid_ = Guid('{cc917f06-7ee0-47b8-9e1f-c3b48df9df5b}')
    @winrt_commethod(6)
    def get_BaseStationId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_CellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ChannelNumber(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_LocationAreaCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ReceivedSignalStrengthInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInBitPeriods(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalStrengthInDBm = property(get_ReceivedSignalStrengthInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class IMobileBroadbandCellLte(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellLte'
    _iid_ = Guid('{9197c87b-2b78-456d-8b53-aaa25d0af741}')
    @winrt_commethod(6)
    def get_CellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_PhysicalCellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ReferenceSignalReceivedPowerInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ReferenceSignalReceivedQualityInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInBitPeriods(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def get_TrackingAreaCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
class IMobileBroadbandCellNR(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellNR'
    _iid_ = Guid('{a13f0deb-66fc-4b4b-83a9-a487a3a5a0a6}')
    @winrt_commethod(6)
    def get_CellId(self) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_PhysicalCellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ReferenceSignalReceivedPowerInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ReferenceSignalReceivedQualityInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInNanoseconds(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def get_TrackingAreaCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(14)
    def get_SignalToNoiseRatioInDB(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInNanoseconds = property(get_TimingAdvanceInNanoseconds, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class IMobileBroadbandCellTdscdma(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma'
    _iid_ = Guid('{0eda1655-db0e-4182-8cda-cc419a7bde08}')
    @winrt_commethod(6)
    def get_CellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_CellParameterId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ChannelNumber(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_LocationAreaCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_PathLossInDB(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ReceivedSignalCodePowerInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_TimingAdvanceInBitPeriods(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    CellParameterId = property(get_CellParameterId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class IMobileBroadbandCellUmts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts'
    _iid_ = Guid('{77b4b5ae-49c8-4f15-b285-4c26a7f67215}')
    @winrt_commethod(6)
    def get_CellId(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_LocationAreaCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_PathLossInDB(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(10)
    def get_PrimaryScramblingCode(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ReceivedSignalCodePowerInDBm(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_SignalToNoiseRatioInDB(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    PrimaryScramblingCode = property(get_PrimaryScramblingCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class IMobileBroadbandCellsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo'
    _iid_ = Guid('{89a9562a-e472-4da5-929c-de61711dd261}')
    @winrt_commethod(6)
    def get_NeighboringCellsCdma(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_commethod(7)
    def get_NeighboringCellsGsm(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_commethod(8)
    def get_NeighboringCellsLte(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_commethod(9)
    def get_NeighboringCellsTdscdma(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_commethod(10)
    def get_NeighboringCellsUmts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_commethod(11)
    def get_ServingCellsCdma(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_commethod(12)
    def get_ServingCellsGsm(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_commethod(13)
    def get_ServingCellsLte(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_commethod(14)
    def get_ServingCellsTdscdma(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_commethod(15)
    def get_ServingCellsUmts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    NeighboringCellsCdma = property(get_NeighboringCellsCdma, None)
    NeighboringCellsGsm = property(get_NeighboringCellsGsm, None)
    NeighboringCellsLte = property(get_NeighboringCellsLte, None)
    NeighboringCellsTdscdma = property(get_NeighboringCellsTdscdma, None)
    NeighboringCellsUmts = property(get_NeighboringCellsUmts, None)
    ServingCellsCdma = property(get_ServingCellsCdma, None)
    ServingCellsGsm = property(get_ServingCellsGsm, None)
    ServingCellsLte = property(get_ServingCellsLte, None)
    ServingCellsTdscdma = property(get_ServingCellsTdscdma, None)
    ServingCellsUmts = property(get_ServingCellsUmts, None)
class IMobileBroadbandCellsInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo2'
    _iid_ = Guid('{66205912-b89f-4e12-bbb6-d5cf09a820ca}')
    @winrt_commethod(6)
    def get_NeighboringCellsNR(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    @winrt_commethod(7)
    def get_ServingCellsNR(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    NeighboringCellsNR = property(get_NeighboringCellsNR, None)
    ServingCellsNR = property(get_ServingCellsNR, None)
class IMobileBroadbandCurrentSlotIndexChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandCurrentSlotIndexChangedEventArgs'
    _iid_ = Guid('{f718b184-c370-5fd4-a670-1846cb9bce47}')
    @winrt_commethod(6)
    def get_CurrentSlotIndex(self) -> Int32: ...
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class IMobileBroadbandDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation'
    _iid_ = Guid('{e6d08168-e381-4c6e-9be8-fe156969a446}')
    @winrt_commethod(6)
    def get_NetworkDeviceStatus(self) -> win32more.Windows.Networking.NetworkOperators.NetworkDeviceStatus: ...
    @winrt_commethod(7)
    def get_Manufacturer(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Model(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_FirmwareInformation(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(11)
    def get_DataClasses(self) -> win32more.Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_commethod(12)
    def get_CustomDataClass(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_MobileEquipmentId(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_TelephoneNumbers(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(15)
    def get_SubscriberId(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_SimIccId(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_DeviceType(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceType: ...
    @winrt_commethod(18)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_CurrentRadioState(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    NetworkDeviceStatus = property(get_NetworkDeviceStatus, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    FirmwareInformation = property(get_FirmwareInformation, None)
    CellularClass = property(get_CellularClass, None)
    DataClasses = property(get_DataClasses, None)
    CustomDataClass = property(get_CustomDataClass, None)
    MobileEquipmentId = property(get_MobileEquipmentId, None)
    TelephoneNumbers = property(get_TelephoneNumbers, None)
    SubscriberId = property(get_SubscriberId, None)
    SimIccId = property(get_SimIccId, None)
    DeviceType = property(get_DeviceType, None)
    DeviceId = property(get_DeviceId, None)
    CurrentRadioState = property(get_CurrentRadioState, None)
class IMobileBroadbandDeviceInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2'
    _iid_ = Guid('{2e467af1-f932-4737-a722-03ba72370cb8}')
    @winrt_commethod(6)
    def get_PinManager(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinManager: ...
    @winrt_commethod(7)
    def get_Revision(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> WinRT_String: ...
    PinManager = property(get_PinManager, None)
    Revision = property(get_Revision, None)
    SerialNumber = property(get_SerialNumber, None)
class IMobileBroadbandDeviceInformation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3'
    _iid_ = Guid('{e08bb4bd-5d30-4b5a-92cc-d54df881d49e}')
    @winrt_commethod(6)
    def get_SimSpn(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SimPnn(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SimGid1(self) -> WinRT_String: ...
    SimSpn = property(get_SimSpn, None)
    SimPnn = property(get_SimPnn, None)
    SimGid1 = property(get_SimGid1, None)
class IMobileBroadbandDeviceInformation4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation4'
    _iid_ = Guid('{263f3152-7b9d-582c-b17c-f80a60b50031}')
    @winrt_commethod(6)
    def get_SlotManager(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager: ...
    SlotManager = property(get_SlotManager, None)
class IMobileBroadbandDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService'
    _iid_ = Guid('{22be1a52-bd80-40ac-8e1f-2e07836a3dbd}')
    @winrt_commethod(6)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SupportedCommands(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def OpenDataSession(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession: ...
    @winrt_commethod(9)
    def OpenCommandSession(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    SupportedCommands = property(get_SupportedCommands, None)
class IMobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult'
    _iid_ = Guid('{b0f46abb-94d6-44b9-a538-f0810b645389}')
    @winrt_commethod(6)
    def get_StatusCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ResponseData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    StatusCode = property(get_StatusCode, None)
    ResponseData = property(get_ResponseData, None)
class IMobileBroadbandDeviceServiceCommandSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession'
    _iid_ = Guid('{fc098a45-913b-4914-b6c3-ae6304593e75}')
    @winrt_commethod(6)
    def SendQueryCommandAsync(self, commandId: UInt32, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_commethod(7)
    def SendSetCommandAsync(self, commandId: UInt32, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_commethod(8)
    def CloseSession(self) -> Void: ...
class IMobileBroadbandDeviceServiceDataReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataReceivedEventArgs'
    _iid_ = Guid('{b6aa13de-1380-40e3-8618-73cbca48138c}')
    @winrt_commethod(6)
    def get_ReceivedData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ReceivedData = property(get_ReceivedData, None)
class IMobileBroadbandDeviceServiceDataSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession'
    _iid_ = Guid('{dad62333-8bcf-4289-8a37-045c2169486a}')
    @winrt_commethod(6)
    def WriteDataAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def CloseSession(self) -> Void: ...
    @winrt_commethod(8)
    def add_DataReceived(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession, win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMobileBroadbandDeviceServiceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation'
    _iid_ = Guid('{53d69b5b-c4ed-45f0-803a-d9417a6d9846}')
    @winrt_commethod(6)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_IsDataReadSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsDataWriteSupported(self) -> Boolean: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    IsDataReadSupported = property(get_IsDataReadSupported, None)
    IsDataWriteSupported = property(get_IsDataWriteSupported, None)
class IMobileBroadbandDeviceServiceTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails'
    _iid_ = Guid('{4a055b70-b9ae-4458-9241-a6a5fbf18a0c}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ReceivedData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeviceId = property(get_DeviceId, None)
    DeviceServiceId = property(get_DeviceServiceId, None)
    ReceivedData = property(get_ReceivedData, None)
class IMobileBroadbandDeviceServiceTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails2'
    _iid_ = Guid('{d83d5f16-336a-553f-94bb-0cd1a2ff0c81}')
    @winrt_commethod(6)
    def get_EventId(self) -> UInt32: ...
    EventId = property(get_EventId, None)
class IMobileBroadbandModem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModem'
    _iid_ = Guid('{d0356912-e9f9-4f67-a03d-43189a316bf1}')
    @winrt_commethod(6)
    def get_CurrentAccount(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    @winrt_commethod(7)
    def get_DeviceInformation(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_commethod(8)
    def get_MaxDeviceServiceCommandSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_MaxDeviceServiceDataSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DeviceServices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation]: ...
    @winrt_commethod(11)
    def GetDeviceService(self, deviceServiceId: Guid) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceService: ...
    @winrt_commethod(12)
    def get_IsResetSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def ResetAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def GetCurrentConfigurationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration]: ...
    @winrt_commethod(15)
    def get_CurrentNetwork(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    CurrentAccount = property(get_CurrentAccount, None)
    DeviceInformation = property(get_DeviceInformation, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
    DeviceServices = property(get_DeviceServices, None)
    IsResetSupported = property(get_IsResetSupported, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
class IMobileBroadbandModem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModem2'
    _iid_ = Guid('{12862b28-b9eb-4ee2-bbe3-711f53eea373}')
    @winrt_commethod(6)
    def GetIsPassthroughEnabledAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def SetIsPassthroughEnabledAsync(self, value: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
class IMobileBroadbandModem3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModem3'
    _iid_ = Guid('{e9fec6ea-2f34-4582-9102-c314d2a87eec}')
    @winrt_commethod(6)
    def TryGetPcoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPco]: ...
    @winrt_commethod(7)
    def get_IsInEmergencyCallMode(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_IsInEmergencyCallModeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsInEmergencyCallModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInEmergencyCallMode = property(get_IsInEmergencyCallMode, None)
class IMobileBroadbandModem4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModem4'
    _iid_ = Guid('{4a0398c2-91be-412b-b569-586e9f0030d1}')
    @winrt_commethod(6)
    def SetIsPassthroughEnabledWithSlotIndexAsync(self, value: Boolean, slotindex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_commethod(7)
    def GetIsPassthroughEnabledWithSlotIndexAsync(self, slotindex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def SetIsPassthroughEnabledWithSlotIndex(self, value: Boolean, slotindex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_commethod(9)
    def GetIsPassthroughEnabledWithSlotIndex(self, slotindex: Int32) -> Boolean: ...
class IMobileBroadbandModemConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration'
    _iid_ = Guid('{fce035a3-d6cd-4320-b982-be9d3ec7890f}')
    @winrt_commethod(6)
    def get_Uicc(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUicc: ...
    @winrt_commethod(7)
    def get_HomeProviderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_HomeProviderName(self) -> WinRT_String: ...
    Uicc = property(get_Uicc, None)
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
class IMobileBroadbandModemConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration2'
    _iid_ = Guid('{320ff5c5-e460-42ae-aa51-69621e7a4477}')
    @winrt_commethod(6)
    def get_SarManager(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSarManager: ...
    SarManager = property(get_SarManager, None)
class IMobileBroadbandModemIsolation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation'
    _iid_ = Guid('{b5618fec-e661-4330-9bb4-3480212ec354}')
    @winrt_commethod(6)
    def AddAllowedHost(self, host: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def AddAllowedHostRange(self, first: win32more.Windows.Networking.HostName, last: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(8)
    def ApplyConfigurationAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearConfigurationAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMobileBroadbandModemIsolationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolationFactory'
    _iid_ = Guid('{21d7ec58-c2b1-4c2f-a030-72820a24ecd9}')
    @winrt_commethod(6)
    def Create(self, modemDeviceId: WinRT_String, ruleGroupId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation: ...
class IMobileBroadbandModemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics'
    _iid_ = Guid('{f99ed637-d6f1-4a78-8cbc-6421a65063c8}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    @winrt_commethod(8)
    def GetDefault(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
class IMobileBroadbandNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandNetwork'
    _iid_ = Guid('{cb63928c-0309-4cb6-a8c1-6a5a3c8e1ff6}')
    @winrt_commethod(6)
    def get_NetworkAdapter(self) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(7)
    def get_NetworkRegistrationState(self) -> win32more.Windows.Networking.NetworkOperators.NetworkRegistrationState: ...
    @winrt_commethod(8)
    def get_RegistrationNetworkError(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PacketAttachNetworkError(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ActivationNetworkError(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_AccessPointName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_RegisteredDataClass(self) -> win32more.Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_commethod(13)
    def get_RegisteredProviderId(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_RegisteredProviderName(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def ShowConnectionUI(self) -> Void: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkRegistrationState = property(get_NetworkRegistrationState, None)
    RegistrationNetworkError = property(get_RegistrationNetworkError, None)
    PacketAttachNetworkError = property(get_PacketAttachNetworkError, None)
    ActivationNetworkError = property(get_ActivationNetworkError, None)
    AccessPointName = property(get_AccessPointName, None)
    RegisteredDataClass = property(get_RegisteredDataClass, None)
    RegisteredProviderId = property(get_RegisteredProviderId, None)
    RegisteredProviderName = property(get_RegisteredProviderName, None)
class IMobileBroadbandNetwork2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandNetwork2'
    _iid_ = Guid('{5a55db22-62f7-4bdd-ba1d-477441960ba0}')
    @winrt_commethod(6)
    def GetVoiceCallSupportAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def get_RegistrationUiccApps(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    RegistrationUiccApps = property(get_RegistrationUiccApps, None)
class IMobileBroadbandNetwork3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandNetwork3'
    _iid_ = Guid('{33670a8a-c7ef-444c-ab6c-df7ef7a390fe}')
    @winrt_commethod(6)
    def GetCellsInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo]: ...
class IMobileBroadbandNetworkRegistrationStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange'
    _iid_ = Guid('{beaf94e1-960f-49b4-a08d-7d85e968c7ec}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Network(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    DeviceId = property(get_DeviceId, None)
    Network = property(get_Network, None)
class IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails'
    _iid_ = Guid('{89135cff-28b8-46aa-b137-1c4b0f21edfe}')
    @winrt_commethod(6)
    def get_NetworkRegistrationStateChanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange]: ...
    NetworkRegistrationStateChanges = property(get_NetworkRegistrationStateChanges, None)
class IMobileBroadbandPco(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPco'
    _iid_ = Guid('{d4e4fcbe-e3a3-43c5-a87b-6c86d229d7fa}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    Data = property(get_Data, None)
    IsComplete = property(get_IsComplete, None)
    DeviceId = property(get_DeviceId, None)
class IMobileBroadbandPcoDataChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPcoDataChangeTriggerDetails'
    _iid_ = Guid('{263f5114-64e0-4493-909b-2d14a01962b1}')
    @winrt_commethod(6)
    def get_UpdatedData(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPco: ...
    UpdatedData = property(get_UpdatedData, None)
class IMobileBroadbandPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPin'
    _iid_ = Guid('{e661d709-e779-45bf-8281-75323df9e321}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_commethod(7)
    def get_LockState(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    @winrt_commethod(8)
    def get_Format(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinFormat: ...
    @winrt_commethod(9)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_MaxLength(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_MinLength(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_AttemptsRemaining(self) -> UInt32: ...
    @winrt_commethod(13)
    def EnableAsync(self, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(14)
    def DisableAsync(self, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(15)
    def EnterAsync(self, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(16)
    def ChangeAsync(self, currentPin: WinRT_String, newPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(17)
    def UnblockAsync(self, pinUnblockKey: WinRT_String, newPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    Type = property(get_Type, None)
    LockState = property(get_LockState, None)
    Format = property(get_Format, None)
    Enabled = property(get_Enabled, None)
    MaxLength = property(get_MaxLength, None)
    MinLength = property(get_MinLength, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
class IMobileBroadbandPinLockStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange'
    _iid_ = Guid('{be16673e-1f04-4f95-8b90-e7f559dde7e5}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PinType(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_commethod(8)
    def get_PinLockState(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    DeviceId = property(get_DeviceId, None)
    PinType = property(get_PinType, None)
    PinLockState = property(get_PinLockState, None)
class IMobileBroadbandPinLockStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChangeTriggerDetails'
    _iid_ = Guid('{d338c091-3e91-4d38-9036-aee83a6e79ad}')
    @winrt_commethod(6)
    def get_PinLockStateChanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange]: ...
    PinLockStateChanges = property(get_PinLockStateChanges, None)
class IMobileBroadbandPinManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPinManager'
    _iid_ = Guid('{83567edd-6e1f-4b9b-a413-2b1f50cc36df}')
    @winrt_commethod(6)
    def get_SupportedPins(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType]: ...
    @winrt_commethod(7)
    def GetPin(self, pinType: win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPin: ...
    SupportedPins = property(get_SupportedPins, None)
class IMobileBroadbandPinOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult'
    _iid_ = Guid('{11dddc32-31e7-49f5-b663-123d3bef0362}')
    @winrt_commethod(6)
    def get_IsSuccessful(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AttemptsRemaining(self) -> UInt32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
class IMobileBroadbandRadioStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange'
    _iid_ = Guid('{b054a561-9833-4aed-9717-4348b21a24b3}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RadioState(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    DeviceId = property(get_DeviceId, None)
    RadioState = property(get_RadioState, None)
class IMobileBroadbandRadioStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChangeTriggerDetails'
    _iid_ = Guid('{71301ace-093c-42c6-b0db-ad1f75a65445}')
    @winrt_commethod(6)
    def get_RadioStateChanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange]: ...
    RadioStateChanges = property(get_RadioStateChanges, None)
class IMobileBroadbandSarManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandSarManager'
    _iid_ = Guid('{e5b26833-967e-40c9-a485-19c0dd209e22}')
    @winrt_commethod(6)
    def get_IsBackoffEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsWiFiHardwareIntegrated(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsSarControlledByHardware(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Antennas(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]: ...
    @winrt_commethod(10)
    def get_HysteresisTimerPeriod(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def add_TransmissionStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSarManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_TransmissionStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def EnableBackoffAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def DisableBackoffAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def SetConfigurationAsync(self, antennas: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def RevertSarToHardwareControlAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def SetTransmissionStateChangedHysteresisAsync(self, timerPeriod: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GetIsTransmittingAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def StartTransmissionStateMonitoring(self) -> Void: ...
    @winrt_commethod(20)
    def StopTransmissionStateMonitoring(self) -> Void: ...
    IsBackoffEnabled = property(get_IsBackoffEnabled, None)
    IsWiFiHardwareIntegrated = property(get_IsWiFiHardwareIntegrated, None)
    IsSarControlledByHardware = property(get_IsSarControlledByHardware, None)
    Antennas = property(get_Antennas, None)
    HysteresisTimerPeriod = property(get_HysteresisTimerPeriod, None)
class IMobileBroadbandSlotInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo'
    _iid_ = Guid('{bd350b32-882e-542a-b17d-0bb1b49bae9e}')
    @winrt_commethod(6)
    def get_Index(self) -> Int32: ...
    @winrt_commethod(7)
    def get_State(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotState: ...
    Index = property(get_Index, None)
    State = property(get_State, None)
class IMobileBroadbandSlotInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo2'
    _iid_ = Guid('{393cb039-ca44-524c-822d-83a3620f0efc}')
    @winrt_commethod(6)
    def get_IccId(self) -> WinRT_String: ...
    IccId = property(get_IccId, None)
class IMobileBroadbandSlotInfoChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfoChangedEventArgs'
    _iid_ = Guid('{3158839f-950c-54ce-a48d-ba4529b48f0f}')
    @winrt_commethod(6)
    def get_SlotInfo(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo: ...
    SlotInfo = property(get_SlotInfo, None)
class IMobileBroadbandSlotManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager'
    _iid_ = Guid('{eba07cd6-2019-5f81-a294-cc364a11d0b2}')
    @winrt_commethod(6)
    def get_SlotInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo]: ...
    @winrt_commethod(7)
    def get_CurrentSlotIndex(self) -> Int32: ...
    @winrt_commethod(8)
    def SetCurrentSlot(self, slotIndex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_commethod(9)
    def SetCurrentSlotAsync(self, slotIndex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_commethod(10)
    def add_SlotInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SlotInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CurrentSlotIndexChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentSlotIndexChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SlotInfos = property(get_SlotInfos, None)
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class IMobileBroadbandTransmissionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandTransmissionStateChangedEventArgs'
    _iid_ = Guid('{612e3875-040a-4f99-a4f9-61d7c32da129}')
    @winrt_commethod(6)
    def get_IsTransmitting(self) -> Boolean: ...
    IsTransmitting = property(get_IsTransmitting, None)
class IMobileBroadbandUicc(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandUicc'
    _iid_ = Guid('{e634f691-525a-4ce2-8fce-aa4162579154}')
    @winrt_commethod(6)
    def get_SimIccId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetUiccAppsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult]: ...
    SimIccId = property(get_SimIccId, None)
class IMobileBroadbandUiccApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp'
    _iid_ = Guid('{4d170556-98a1-43dd-b2ec-50c90cf248df}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.Networking.NetworkOperators.UiccAppKind: ...
    @winrt_commethod(8)
    def GetRecordDetailsAsync(self, uiccFilePath: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult]: ...
    @winrt_commethod(9)
    def ReadRecordAsync(self, uiccFilePath: win32more.Windows.Foundation.Collections.IIterable[UInt32], recordIndex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class IMobileBroadbandUiccAppReadRecordResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult'
    _iid_ = Guid('{64c95285-358e-47c5-8249-695f383b2bdb}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Data = property(get_Data, None)
class IMobileBroadbandUiccAppRecordDetailsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult'
    _iid_ = Guid('{d919682f-be14-4934-981d-2f57b9ed83e6}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.Networking.NetworkOperators.UiccAppRecordKind: ...
    @winrt_commethod(8)
    def get_RecordCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_RecordSize(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ReadAccessCondition(self) -> win32more.Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    @winrt_commethod(11)
    def get_WriteAccessCondition(self) -> win32more.Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    Status = property(get_Status, None)
    Kind = property(get_Kind, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    WriteAccessCondition = property(get_WriteAccessCondition, None)
class IMobileBroadbandUiccAppsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult'
    _iid_ = Guid('{744930eb-8157-4a41-8494-6bf54c9b1d2b}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_UiccApps(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    Status = property(get_Status, None)
    UiccApps = property(get_UiccApps, None)
class INetworkOperatorDataUsageTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails'
    _iid_ = Guid('{50e3126d-a465-4eeb-9317-28a167630cea}')
    @winrt_commethod(6)
    def get_NotificationKind(self) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind: ...
    NotificationKind = property(get_NotificationKind, None)
class INetworkOperatorNotificationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails'
    _iid_ = Guid('{bc68a9d1-82e1-4488-9f2c-1276c2468fac}')
    @winrt_commethod(6)
    def get_NotificationType(self) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType: ...
    @winrt_commethod(7)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EncodingType(self) -> Byte: ...
    @winrt_commethod(9)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_RuleId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SmsMessage(self) -> win32more.Windows.Devices.Sms.ISmsMessage: ...
    NotificationType = property(get_NotificationType, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    RuleId = property(get_RuleId, None)
    SmsMessage = property(get_SmsMessage, None)
class INetworkOperatorTetheringAccessPointConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration'
    _iid_ = Guid('{0bcc0284-412e-403d-acc6-b757e34774a4}')
    @winrt_commethod(6)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Passphrase(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Passphrase(self, value: WinRT_String) -> Void: ...
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
class INetworkOperatorTetheringAccessPointConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2'
    _iid_ = Guid('{b1809142-7238-59a0-928b-74ab46fd64b6}')
    @winrt_commethod(6)
    def IsBandSupported(self, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_commethod(7)
    def IsBandSupportedAsync(self, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Band(self) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_commethod(9)
    def put_Band(self, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    Band = property(get_Band, put_Band)
class INetworkOperatorTetheringClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient'
    _iid_ = Guid('{709d254c-595f-4847-bb30-646935542918}')
    @winrt_commethod(6)
    def get_MacAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HostNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    MacAddress = property(get_MacAddress, None)
    HostNames = property(get_HostNames, None)
class INetworkOperatorTetheringClientManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringClientManager'
    _iid_ = Guid('{91b14016-8dca-4225-bbed-eef8b8d718d7}')
    @winrt_commethod(6)
    def GetTetheringClients(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient]: ...
class INetworkOperatorTetheringEntitlementCheck(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringEntitlementCheck'
    _iid_ = Guid('{0108916d-9e9a-4af6-8da3-60493b19c204}')
    @winrt_commethod(6)
    def AuthorizeTethering(self, allow: Boolean, entitlementFailureReason: WinRT_String) -> Void: ...
class INetworkOperatorTetheringManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager'
    _iid_ = Guid('{d45a8da0-0e86-4d98-8ba4-dd70d4b764d3}')
    @winrt_commethod(6)
    def get_MaxClientCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ClientCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_TetheringOperationalState(self) -> win32more.Windows.Networking.NetworkOperators.TetheringOperationalState: ...
    @winrt_commethod(9)
    def GetCurrentAccessPointConfiguration(self) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_commethod(10)
    def ConfigureAccessPointAsync(self, configuration: win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def StartTetheringAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_commethod(12)
    def StopTetheringAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    MaxClientCount = property(get_MaxClientCount, None)
    ClientCount = property(get_ClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class INetworkOperatorTetheringManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics'
    _iid_ = Guid('{3ebcbacc-f8c3-405c-9964-70a1eeabe194}')
    @winrt_commethod(6)
    def GetTetheringCapability(self, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_commethod(7)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics2'
    _iid_ = Guid('{5b235412-35f0-49e7-9b08-16d278fbaa42}')
    @winrt_commethod(6)
    def GetTetheringCapabilityFromConnectionProfile(self, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile) -> win32more.Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_commethod(7)
    def CreateFromConnectionProfile(self, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics3'
    _iid_ = Guid('{8fdaadb6-4af9-4f21-9b58-d53e9f24231e}')
    @winrt_commethod(6)
    def CreateFromConnectionProfileWithTargetAdapter(self, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4'
    _iid_ = Guid('{b3b9f9d0-ebff-46a4-a847-d663d8b0977e}')
    @winrt_commethod(6)
    def IsNoConnectionsTimeoutEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def EnableNoConnectionsTimeout(self) -> Void: ...
    @winrt_commethod(8)
    def EnableNoConnectionsTimeoutAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DisableNoConnectionsTimeout(self) -> Void: ...
    @winrt_commethod(10)
    def DisableNoConnectionsTimeoutAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class INetworkOperatorTetheringOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult'
    _iid_ = Guid('{ebd203a1-01ba-476d-b4b3-bf3d12c8f80c}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.NetworkOperators.TetheringOperationStatus: ...
    @winrt_commethod(7)
    def get_AdditionalErrorMessage(self) -> WinRT_String: ...
    Status = property(get_Status, None)
    AdditionalErrorMessage = property(get_AdditionalErrorMessage, None)
class IProvisionFromXmlDocumentResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults'
    _iid_ = Guid('{217700e0-8203-11df-adb9-f4ce462d9137}')
    @winrt_commethod(6)
    def get_AllElementsProvisioned(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ProvisionResultsXml(self) -> WinRT_String: ...
    AllElementsProvisioned = property(get_AllElementsProvisioned, None)
    ProvisionResultsXml = property(get_ProvisionResultsXml, None)
class IProvisionedProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IProvisionedProfile'
    _iid_ = Guid('{217700e0-8202-11df-adb9-f4ce462d9137}')
    @winrt_commethod(6)
    def UpdateCost(self, value: win32more.Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_commethod(7)
    def UpdateUsage(self, value: win32more.Windows.Networking.NetworkOperators.ProfileUsage) -> Void: ...
class IProvisioningAgent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IProvisioningAgent'
    _iid_ = Guid('{217700e0-8201-11df-adb9-f4ce462d9137}')
    @winrt_commethod(6)
    def ProvisionFromXmlDocumentAsync(self, provisioningXmlDocument: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults]: ...
    @winrt_commethod(7)
    def GetProvisionedProfile(self, mediaType: win32more.Windows.Networking.NetworkOperators.ProfileMediaType, profileName: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisionedProfile: ...
class IProvisioningAgentStaticMethods(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IProvisioningAgentStaticMethods'
    _iid_ = Guid('{217700e0-8101-11df-adb9-f4ce462d9137}')
    @winrt_commethod(6)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisioningAgent: ...
class ITetheringEntitlementCheckTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails'
    _iid_ = Guid('{03c65e9d-5926-41f3-a94e-b50926fc421b}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def AllowTethering(self) -> Void: ...
    @winrt_commethod(8)
    def DenyTethering(self, entitlementFailureReason: WinRT_String) -> Void: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class IUssdMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IUssdMessage'
    _iid_ = Guid('{2f9acf82-2004-4d5d-bf81-2aba1b4be4a8}')
    @winrt_commethod(6)
    def get_DataCodingScheme(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataCodingScheme(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def GetPayload(self) -> SZArray[Byte]: ...
    @winrt_commethod(9)
    def SetPayload(self, value: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(10)
    def get_PayloadAsText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_PayloadAsText(self, value: WinRT_String) -> Void: ...
    DataCodingScheme = property(get_DataCodingScheme, put_DataCodingScheme)
    PayloadAsText = property(get_PayloadAsText, put_PayloadAsText)
class IUssdMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IUssdMessageFactory'
    _iid_ = Guid('{2f9acf82-1003-4d5d-bf81-2aba1b4be4a8}')
    @winrt_commethod(6)
    def CreateMessage(self, messageText: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdMessage: ...
class IUssdReply(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IUssdReply'
    _iid_ = Guid('{2f9acf82-2005-4d5d-bf81-2aba1b4be4a8}')
    @winrt_commethod(6)
    def get_ResultCode(self) -> win32more.Windows.Networking.NetworkOperators.UssdResultCode: ...
    @winrt_commethod(7)
    def get_Message(self) -> win32more.Windows.Networking.NetworkOperators.UssdMessage: ...
    ResultCode = property(get_ResultCode, None)
    Message = property(get_Message, None)
class IUssdSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IUssdSession'
    _iid_ = Guid('{2f9acf82-2002-4d5d-bf81-2aba1b4be4a8}')
    @winrt_commethod(6)
    def SendMessageAndGetReplyAsync(self, message: win32more.Windows.Networking.NetworkOperators.UssdMessage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.UssdReply]: ...
    @winrt_commethod(7)
    def Close(self) -> Void: ...
class IUssdSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IUssdSessionStatics'
    _iid_ = Guid('{2f9acf82-1001-4d5d-bf81-2aba1b4be4a8}')
    @winrt_commethod(6)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdSession: ...
    @winrt_commethod(7)
    def CreateFromNetworkInterfaceId(self, networkInterfaceId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdSession: ...
class _KnownCSimFilePaths_Meta_(ComPtr.__class__):
    pass
class KnownCSimFilePaths(ComPtr, metaclass=_KnownCSimFilePaths_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownCSimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: win32more.Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: win32more.Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: win32more.Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    _KnownCSimFilePaths_Meta_.EFSpn = property(get_EFSpn.__wrapped__, None)
    _KnownCSimFilePaths_Meta_.Gid1 = property(get_Gid1.__wrapped__, None)
    _KnownCSimFilePaths_Meta_.Gid2 = property(get_Gid2.__wrapped__, None)
class _KnownRuimFilePaths_Meta_(ComPtr.__class__):
    pass
class KnownRuimFilePaths(ComPtr, metaclass=_KnownRuimFilePaths_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownRuimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: win32more.Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: win32more.Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: win32more.Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    _KnownRuimFilePaths_Meta_.EFSpn = property(get_EFSpn.__wrapped__, None)
    _KnownRuimFilePaths_Meta_.Gid1 = property(get_Gid1.__wrapped__, None)
    _KnownRuimFilePaths_Meta_.Gid2 = property(get_Gid2.__wrapped__, None)
class _KnownSimFilePaths_Meta_(ComPtr.__class__):
    pass
class KnownSimFilePaths(ComPtr, metaclass=_KnownSimFilePaths_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownSimFilePaths'
    @winrt_classmethod
    def get_EFOns(cls: win32more.Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFSpn(cls: win32more.Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: win32more.Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: win32more.Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    _KnownSimFilePaths_Meta_.EFOns = property(get_EFOns.__wrapped__, None)
    _KnownSimFilePaths_Meta_.EFSpn = property(get_EFSpn.__wrapped__, None)
    _KnownSimFilePaths_Meta_.Gid1 = property(get_Gid1.__wrapped__, None)
    _KnownSimFilePaths_Meta_.Gid2 = property(get_Gid2.__wrapped__, None)
class _KnownUSimFilePaths_Meta_(ComPtr.__class__):
    pass
class KnownUSimFilePaths(ComPtr, metaclass=_KnownUSimFilePaths_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownUSimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: win32more.Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFOpl(cls: win32more.Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFPnn(cls: win32more.Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: win32more.Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: win32more.Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    _KnownUSimFilePaths_Meta_.EFSpn = property(get_EFSpn.__wrapped__, None)
    _KnownUSimFilePaths_Meta_.EFOpl = property(get_EFOpl.__wrapped__, None)
    _KnownUSimFilePaths_Meta_.EFPnn = property(get_EFPnn.__wrapped__, None)
    _KnownUSimFilePaths_Meta_.Gid1 = property(get_Gid1.__wrapped__, None)
    _KnownUSimFilePaths_Meta_.Gid2 = property(get_Gid2.__wrapped__, None)
LegacyNetworkOperatorsContract: UInt32 = 65536
class _MobileBroadbandAccount_Meta_(ComPtr.__class__):
    pass
class MobileBroadbandAccount(ComPtr, metaclass=_MobileBroadbandAccount_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccount'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceProviderGuid(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> Guid: ...
    @winrt_mixinmethod
    def get_ServiceProviderName(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentNetwork(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_mixinmethod
    def get_CurrentDeviceInformation(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_mixinmethod
    def GetConnectionProfiles(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Connectivity.ConnectionProfile]: ...
    @winrt_mixinmethod
    def get_AccountExperienceUrl(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccount3) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AvailableNetworkAccountIds(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountStatics, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
    AccountExperienceUrl = property(get_AccountExperienceUrl, None)
    _MobileBroadbandAccount_Meta_.AvailableNetworkAccountIds = property(get_AvailableNetworkAccountIds.__wrapped__, None)
class MobileBroadbandAccountEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountEventArgs) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class MobileBroadbandAccountUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasDeviceInformationChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNetworkChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> Boolean: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    HasDeviceInformationChanged = property(get_HasDeviceInformationChanged, None)
    HasNetworkChanged = property(get_HasNetworkChanged, None)
class MobileBroadbandAccountWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher: ...
    @winrt_mixinmethod
    def add_AccountAdded(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountAdded(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountUpdated(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountUpdated(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountRemoved(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountRemoved(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> Void: ...
    Status = property(get_Status, None)
MobileBroadbandAccountWatcherStatus = Int32
MobileBroadbandAccountWatcherStatus_Created: MobileBroadbandAccountWatcherStatus = 0
MobileBroadbandAccountWatcherStatus_Started: MobileBroadbandAccountWatcherStatus = 1
MobileBroadbandAccountWatcherStatus_EnumerationCompleted: MobileBroadbandAccountWatcherStatus = 2
MobileBroadbandAccountWatcherStatus_Stopped: MobileBroadbandAccountWatcherStatus = 3
MobileBroadbandAccountWatcherStatus_Aborted: MobileBroadbandAccountWatcherStatus = 4
class MobileBroadbandAntennaSar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 2:
            instance = win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar.CreateWithIndex(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateWithIndex(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSarFactory, antennaIndex: Int32, sarBackoffIndex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar: ...
    @winrt_mixinmethod
    def get_AntennaIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar) -> Int32: ...
    @winrt_mixinmethod
    def get_SarBackoffIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar) -> Int32: ...
    AntennaIndex = property(get_AntennaIndex, None)
    SarBackoffIndex = property(get_SarBackoffIndex, None)
class MobileBroadbandCellCdma(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellCdma'
    @winrt_mixinmethod
    def get_BaseStationId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_BaseStationPNCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_BaseStationLatitude(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_BaseStationLongitude(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_BaseStationLastBroadcastGpsTime(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_NetworkId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PilotSignalStrengthInDB(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SystemId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    NetworkId = property(get_NetworkId, None)
    PilotSignalStrengthInDB = property(get_PilotSignalStrengthInDB, None)
    SystemId = property(get_SystemId, None)
class MobileBroadbandCellGsm(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellGsm'
    @winrt_mixinmethod
    def get_BaseStationId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_CellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalStrengthInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> win32more.Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalStrengthInDBm = property(get_ReceivedSignalStrengthInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class MobileBroadbandCellLte(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellLte'
    @winrt_mixinmethod
    def get_CellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PhysicalCellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedPowerInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedQualityInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_TrackingAreaCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> win32more.Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
class MobileBroadbandCellNR(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellNR'
    @winrt_mixinmethod
    def get_CellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PhysicalCellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedPowerInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedQualityInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInNanoseconds(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_TrackingAreaCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_SignalToNoiseRatioInDB(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> win32more.Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInNanoseconds = property(get_TimingAdvanceInNanoseconds, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class MobileBroadbandCellTdscdma(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma'
    @winrt_mixinmethod
    def get_CellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_CellParameterId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PathLossInDB(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalCodePowerInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> win32more.Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    CellParameterId = property(get_CellParameterId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class MobileBroadbandCellUmts(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellUmts'
    @winrt_mixinmethod
    def get_CellId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PathLossInDB(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_PrimaryScramblingCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalCodePowerInDBm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SignalToNoiseRatioInDB(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> win32more.Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    PrimaryScramblingCode = property(get_PrimaryScramblingCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class MobileBroadbandCellsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo'
    @winrt_mixinmethod
    def get_NeighboringCellsCdma(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsGsm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsLte(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsTdscdma(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsUmts(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_mixinmethod
    def get_ServingCellsCdma(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_mixinmethod
    def get_ServingCellsGsm(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_mixinmethod
    def get_ServingCellsLte(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_mixinmethod
    def get_ServingCellsTdscdma(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_mixinmethod
    def get_ServingCellsUmts(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsNR(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    @winrt_mixinmethod
    def get_ServingCellsNR(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    NeighboringCellsCdma = property(get_NeighboringCellsCdma, None)
    NeighboringCellsGsm = property(get_NeighboringCellsGsm, None)
    NeighboringCellsLte = property(get_NeighboringCellsLte, None)
    NeighboringCellsTdscdma = property(get_NeighboringCellsTdscdma, None)
    NeighboringCellsUmts = property(get_NeighboringCellsUmts, None)
    ServingCellsCdma = property(get_ServingCellsCdma, None)
    ServingCellsGsm = property(get_ServingCellsGsm, None)
    ServingCellsLte = property(get_ServingCellsLte, None)
    ServingCellsTdscdma = property(get_ServingCellsTdscdma, None)
    ServingCellsUmts = property(get_ServingCellsUmts, None)
    NeighboringCellsNR = property(get_NeighboringCellsNR, None)
    ServingCellsNR = property(get_ServingCellsNR, None)
class MobileBroadbandCurrentSlotIndexChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCurrentSlotIndexChangedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs'
    @winrt_mixinmethod
    def get_CurrentSlotIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandCurrentSlotIndexChangedEventArgs) -> Int32: ...
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class MobileBroadbandDeviceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation'
    @winrt_mixinmethod
    def get_NetworkDeviceStatus(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Networking.NetworkOperators.NetworkDeviceStatus: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Model(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirmwareInformation(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_DataClasses(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_mixinmethod
    def get_CustomDataClass(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MobileEquipmentId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TelephoneNumbers(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SubscriberId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceType(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentRadioState(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    @winrt_mixinmethod
    def get_PinManager(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinManager: ...
    @winrt_mixinmethod
    def get_Revision(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimSpn(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimPnn(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimGid1(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SlotManager(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation4) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager: ...
    NetworkDeviceStatus = property(get_NetworkDeviceStatus, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    FirmwareInformation = property(get_FirmwareInformation, None)
    CellularClass = property(get_CellularClass, None)
    DataClasses = property(get_DataClasses, None)
    CustomDataClass = property(get_CustomDataClass, None)
    MobileEquipmentId = property(get_MobileEquipmentId, None)
    TelephoneNumbers = property(get_TelephoneNumbers, None)
    SubscriberId = property(get_SubscriberId, None)
    SimIccId = property(get_SimIccId, None)
    DeviceType = property(get_DeviceType, None)
    DeviceId = property(get_DeviceId, None)
    CurrentRadioState = property(get_CurrentRadioState, None)
    PinManager = property(get_PinManager, None)
    Revision = property(get_Revision, None)
    SerialNumber = property(get_SerialNumber, None)
    SimSpn = property(get_SimSpn, None)
    SimPnn = property(get_SimPnn, None)
    SimGid1 = property(get_SimGid1, None)
    SlotManager = property(get_SlotManager, None)
class MobileBroadbandDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceService'
    @winrt_mixinmethod
    def get_DeviceServiceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> Guid: ...
    @winrt_mixinmethod
    def get_SupportedCommands(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def OpenDataSession(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession: ...
    @winrt_mixinmethod
    def OpenCommandSession(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    SupportedCommands = property(get_SupportedCommands, None)
class MobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult'
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    StatusCode = property(get_StatusCode, None)
    ResponseData = property(get_ResponseData, None)
class MobileBroadbandDeviceServiceCommandSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession'
    @winrt_mixinmethod
    def SendQueryCommandAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession, commandId: UInt32, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_mixinmethod
    def SendSetCommandAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession, commandId: UInt32, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_mixinmethod
    def CloseSession(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession) -> Void: ...
class MobileBroadbandDeviceServiceDataReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataReceivedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_ReceivedData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataReceivedEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ReceivedData = property(get_ReceivedData, None)
class MobileBroadbandDeviceServiceDataSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession'
    @winrt_mixinmethod
    def WriteDataAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CloseSession(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession) -> Void: ...
    @winrt_mixinmethod
    def add_DataReceived(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession, win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataReceived(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class MobileBroadbandDeviceServiceInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation'
    @winrt_mixinmethod
    def get_DeviceServiceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_IsDataReadSupported(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDataWriteSupported(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Boolean: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    IsDataReadSupported = property(get_IsDataReadSupported, None)
    IsDataWriteSupported = property(get_IsDataWriteSupported, None)
class MobileBroadbandDeviceServiceTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceServiceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_ReceivedData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_EventId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails2) -> UInt32: ...
    DeviceId = property(get_DeviceId, None)
    DeviceServiceId = property(get_DeviceServiceId, None)
    ReceivedData = property(get_ReceivedData, None)
    EventId = property(get_EventId, None)
MobileBroadbandDeviceType = Int32
MobileBroadbandDeviceType_Unknown: MobileBroadbandDeviceType = 0
MobileBroadbandDeviceType_Embedded: MobileBroadbandDeviceType = 1
MobileBroadbandDeviceType_Removable: MobileBroadbandDeviceType = 2
MobileBroadbandDeviceType_Remote: MobileBroadbandDeviceType = 3
class MobileBroadbandModem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModem'
    @winrt_mixinmethod
    def get_CurrentAccount(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_mixinmethod
    def get_MaxDeviceServiceCommandSizeInBytes(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxDeviceServiceDataSizeInBytes(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> UInt32: ...
    @winrt_mixinmethod
    def get_DeviceServices(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation]: ...
    @winrt_mixinmethod
    def GetDeviceService(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem, deviceServiceId: Guid) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceService: ...
    @winrt_mixinmethod
    def get_IsResetSupported(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Boolean: ...
    @winrt_mixinmethod
    def ResetAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetCurrentConfigurationAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration]: ...
    @winrt_mixinmethod
    def get_CurrentNetwork(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem2, value: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def TryGetPcoAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPco]: ...
    @winrt_mixinmethod
    def get_IsInEmergencyCallMode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem3) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsInEmergencyCallModeChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsInEmergencyCallModeChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledWithSlotIndexAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem4, value: Boolean, slotindex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledWithSlotIndexAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem4, slotindex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledWithSlotIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem4, value: Boolean, slotindex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledWithSlotIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModem4, slotindex: Int32) -> Boolean: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics, deviceId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    CurrentAccount = property(get_CurrentAccount, None)
    DeviceInformation = property(get_DeviceInformation, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
    DeviceServices = property(get_DeviceServices, None)
    IsResetSupported = property(get_IsResetSupported, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    IsInEmergencyCallMode = property(get_IsInEmergencyCallMode, None)
class MobileBroadbandModemConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration'
    @winrt_mixinmethod
    def get_Uicc(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUicc: ...
    @winrt_mixinmethod
    def get_HomeProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HomeProviderName(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SarManager(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration2) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSarManager: ...
    Uicc = property(get_Uicc, None)
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
    SarManager = property(get_SarManager, None)
class MobileBroadbandModemIsolation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 2:
            instance = win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolationFactory, modemDeviceId: WinRT_String, ruleGroupId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation: ...
    @winrt_mixinmethod
    def AddAllowedHost(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation, host: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def AddAllowedHostRange(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation, first: win32more.Windows.Networking.HostName, last: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def ApplyConfigurationAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearConfigurationAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation) -> win32more.Windows.Foundation.IAsyncAction: ...
MobileBroadbandModemStatus = Int32
MobileBroadbandModemStatus_Success: MobileBroadbandModemStatus = 0
MobileBroadbandModemStatus_OtherFailure: MobileBroadbandModemStatus = 1
MobileBroadbandModemStatus_Busy: MobileBroadbandModemStatus = 2
MobileBroadbandModemStatus_NoDeviceSupport: MobileBroadbandModemStatus = 3
class MobileBroadbandNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetwork'
    @winrt_mixinmethod
    def get_NetworkAdapter(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> win32more.Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def get_NetworkRegistrationState(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> win32more.Windows.Networking.NetworkOperators.NetworkRegistrationState: ...
    @winrt_mixinmethod
    def get_RegistrationNetworkError(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_PacketAttachNetworkError(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_ActivationNetworkError(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_AccessPointName(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegisteredDataClass(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> win32more.Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_mixinmethod
    def get_RegisteredProviderId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegisteredProviderName(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def ShowConnectionUI(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> Void: ...
    @winrt_mixinmethod
    def GetVoiceCallSupportAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_RegistrationUiccApps(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    @winrt_mixinmethod
    def GetCellsInfoAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetwork3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo]: ...
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkRegistrationState = property(get_NetworkRegistrationState, None)
    RegistrationNetworkError = property(get_RegistrationNetworkError, None)
    PacketAttachNetworkError = property(get_PacketAttachNetworkError, None)
    ActivationNetworkError = property(get_ActivationNetworkError, None)
    AccessPointName = property(get_AccessPointName, None)
    RegisteredDataClass = property(get_RegisteredDataClass, None)
    RegisteredProviderId = property(get_RegisteredProviderId, None)
    RegisteredProviderName = property(get_RegisteredProviderName, None)
    RegistrationUiccApps = property(get_RegistrationUiccApps, None)
class MobileBroadbandNetworkRegistrationStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Network(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    DeviceId = property(get_DeviceId, None)
    Network = property(get_Network, None)
class MobileBroadbandNetworkRegistrationStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_NetworkRegistrationStateChanges(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange]: ...
    NetworkRegistrationStateChanges = property(get_NetworkRegistrationStateChanges, None)
class MobileBroadbandPco(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPco
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPco'
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> WinRT_String: ...
    Data = property(get_Data, None)
    IsComplete = property(get_IsComplete, None)
    DeviceId = property(get_DeviceId, None)
class MobileBroadbandPcoDataChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPcoDataChangeTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPcoDataChangeTriggerDetails'
    @winrt_mixinmethod
    def get_UpdatedData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPcoDataChangeTriggerDetails) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPco: ...
    UpdatedData = property(get_UpdatedData, None)
class MobileBroadbandPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPin'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_mixinmethod
    def get_LockState(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinFormat: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxLength(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinLength(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def get_AttemptsRemaining(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def EnableAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def DisableAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def EnterAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def ChangeAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String, newPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def UnblockAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPin, pinUnblockKey: WinRT_String, newPin: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    Type = property(get_Type, None)
    LockState = property(get_LockState, None)
    Format = property(get_Format, None)
    Enabled = property(get_Enabled, None)
    MaxLength = property(get_MaxLength, None)
    MinLength = property(get_MinLength, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
MobileBroadbandPinFormat = Int32
MobileBroadbandPinFormat_Unknown: MobileBroadbandPinFormat = 0
MobileBroadbandPinFormat_Numeric: MobileBroadbandPinFormat = 1
MobileBroadbandPinFormat_Alphanumeric: MobileBroadbandPinFormat = 2
MobileBroadbandPinLockState = Int32
MobileBroadbandPinLockState_Unknown: MobileBroadbandPinLockState = 0
MobileBroadbandPinLockState_Unlocked: MobileBroadbandPinLockState = 1
MobileBroadbandPinLockState_PinRequired: MobileBroadbandPinLockState = 2
MobileBroadbandPinLockState_PinUnblockKeyRequired: MobileBroadbandPinLockState = 3
class MobileBroadbandPinLockStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PinType(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_mixinmethod
    def get_PinLockState(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    DeviceId = property(get_DeviceId, None)
    PinType = property(get_PinType, None)
    PinLockState = property(get_PinLockState, None)
class MobileBroadbandPinLockStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChangeTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_PinLockStateChanges(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChangeTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange]: ...
    PinLockStateChanges = property(get_PinLockStateChanges, None)
class MobileBroadbandPinManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinManager
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinManager'
    @winrt_mixinmethod
    def get_SupportedPins(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType]: ...
    @winrt_mixinmethod
    def GetPin(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinManager, pinType: win32more.Windows.Networking.NetworkOperators.MobileBroadbandPinType) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandPin: ...
    SupportedPins = property(get_SupportedPins, None)
class MobileBroadbandPinOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult'
    @winrt_mixinmethod
    def get_IsSuccessful(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_AttemptsRemaining(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult) -> UInt32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
MobileBroadbandPinType = Int32
MobileBroadbandPinType_None: MobileBroadbandPinType = 0
MobileBroadbandPinType_Custom: MobileBroadbandPinType = 1
MobileBroadbandPinType_Pin1: MobileBroadbandPinType = 2
MobileBroadbandPinType_Pin2: MobileBroadbandPinType = 3
MobileBroadbandPinType_SimPin: MobileBroadbandPinType = 4
MobileBroadbandPinType_FirstSimPin: MobileBroadbandPinType = 5
MobileBroadbandPinType_NetworkPin: MobileBroadbandPinType = 6
MobileBroadbandPinType_NetworkSubsetPin: MobileBroadbandPinType = 7
MobileBroadbandPinType_ServiceProviderPin: MobileBroadbandPinType = 8
MobileBroadbandPinType_CorporatePin: MobileBroadbandPinType = 9
MobileBroadbandPinType_SubsidyLock: MobileBroadbandPinType = 10
MobileBroadbandRadioState = Int32
MobileBroadbandRadioState_Off: MobileBroadbandRadioState = 0
MobileBroadbandRadioState_On: MobileBroadbandRadioState = 1
class MobileBroadbandRadioStateChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RadioState(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    DeviceId = property(get_DeviceId, None)
    RadioState = property(get_RadioState, None)
class MobileBroadbandRadioStateChangeTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChangeTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_RadioStateChanges(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChangeTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange]: ...
    RadioStateChanges = property(get_RadioStateChanges, None)
class MobileBroadbandSarManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSarManager'
    @winrt_mixinmethod
    def get_IsBackoffEnabled(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsWiFiHardwareIntegrated(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSarControlledByHardware(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_Antennas(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]: ...
    @winrt_mixinmethod
    def get_HysteresisTimerPeriod(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_TransmissionStateChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSarManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransmissionStateChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def EnableBackoffAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DisableBackoffAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetConfigurationAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, antennas: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RevertSarToHardwareControlAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetTransmissionStateChangedHysteresisAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, timerPeriod: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetIsTransmittingAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def StartTransmissionStateMonitoring(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Void: ...
    @winrt_mixinmethod
    def StopTransmissionStateMonitoring(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Void: ...
    IsBackoffEnabled = property(get_IsBackoffEnabled, None)
    IsWiFiHardwareIntegrated = property(get_IsWiFiHardwareIntegrated, None)
    IsSarControlledByHardware = property(get_IsSarControlledByHardware, None)
    Antennas = property(get_Antennas, None)
    HysteresisTimerPeriod = property(get_HysteresisTimerPeriod, None)
class MobileBroadbandSlotInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo'
    @winrt_mixinmethod
    def get_Index(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotState: ...
    @winrt_mixinmethod
    def get_IccId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo2) -> WinRT_String: ...
    Index = property(get_Index, None)
    State = property(get_State, None)
    IccId = property(get_IccId, None)
class MobileBroadbandSlotInfoChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfoChangedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs'
    @winrt_mixinmethod
    def get_SlotInfo(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfoChangedEventArgs) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo: ...
    SlotInfo = property(get_SlotInfo, None)
class MobileBroadbandSlotManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotManager'
    @winrt_mixinmethod
    def get_SlotInfos(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo]: ...
    @winrt_mixinmethod
    def get_CurrentSlotIndex(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager) -> Int32: ...
    @winrt_mixinmethod
    def SetCurrentSlot(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, slotIndex: Int32) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_mixinmethod
    def SetCurrentSlotAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, slotIndex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def add_SlotInfoChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SlotInfoChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentSlotIndexChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, win32more.Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentSlotIndexChanged(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SlotInfos = property(get_SlotInfos, None)
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
MobileBroadbandSlotState = Int32
MobileBroadbandSlotState_Unmanaged: MobileBroadbandSlotState = 0
MobileBroadbandSlotState_Unknown: MobileBroadbandSlotState = 1
MobileBroadbandSlotState_OffEmpty: MobileBroadbandSlotState = 2
MobileBroadbandSlotState_Off: MobileBroadbandSlotState = 3
MobileBroadbandSlotState_Empty: MobileBroadbandSlotState = 4
MobileBroadbandSlotState_NotReady: MobileBroadbandSlotState = 5
MobileBroadbandSlotState_Active: MobileBroadbandSlotState = 6
MobileBroadbandSlotState_Error: MobileBroadbandSlotState = 7
MobileBroadbandSlotState_ActiveEsim: MobileBroadbandSlotState = 8
MobileBroadbandSlotState_ActiveEsimNoProfile: MobileBroadbandSlotState = 9
class MobileBroadbandTransmissionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandTransmissionStateChangedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_IsTransmitting(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandTransmissionStateChangedEventArgs) -> Boolean: ...
    IsTransmitting = property(get_IsTransmitting, None)
class MobileBroadbandUicc(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUicc
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUicc'
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUicc) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetUiccAppsAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUicc) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult]: ...
    SimIccId = property(get_SimIccId, None)
class MobileBroadbandUiccApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccApp'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp) -> win32more.Windows.Networking.NetworkOperators.UiccAppKind: ...
    @winrt_mixinmethod
    def GetRecordDetailsAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp, uiccFilePath: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult]: ...
    @winrt_mixinmethod
    def ReadRecordAsync(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp, uiccFilePath: win32more.Windows.Foundation.Collections.IIterable[UInt32], recordIndex: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
MobileBroadbandUiccAppOperationStatus = Int32
MobileBroadbandUiccAppOperationStatus_Success: MobileBroadbandUiccAppOperationStatus = 0
MobileBroadbandUiccAppOperationStatus_InvalidUiccFilePath: MobileBroadbandUiccAppOperationStatus = 1
MobileBroadbandUiccAppOperationStatus_AccessConditionNotHeld: MobileBroadbandUiccAppOperationStatus = 2
MobileBroadbandUiccAppOperationStatus_UiccBusy: MobileBroadbandUiccAppOperationStatus = 3
class MobileBroadbandUiccAppReadRecordResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Data = property(get_Data, None)
class MobileBroadbandUiccAppRecordDetailsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> win32more.Windows.Networking.NetworkOperators.UiccAppRecordKind: ...
    @winrt_mixinmethod
    def get_RecordCount(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Int32: ...
    @winrt_mixinmethod
    def get_RecordSize(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Int32: ...
    @winrt_mixinmethod
    def get_ReadAccessCondition(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> win32more.Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    @winrt_mixinmethod
    def get_WriteAccessCondition(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> win32more.Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    Status = property(get_Status, None)
    Kind = property(get_Kind, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    WriteAccessCondition = property(get_WriteAccessCondition, None)
class MobileBroadbandUiccAppsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_UiccApps(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    Status = property(get_Status, None)
    UiccApps = property(get_UiccApps, None)
NetworkDeviceStatus = Int32
NetworkDeviceStatus_DeviceNotReady: NetworkDeviceStatus = 0
NetworkDeviceStatus_DeviceReady: NetworkDeviceStatus = 1
NetworkDeviceStatus_SimNotInserted: NetworkDeviceStatus = 2
NetworkDeviceStatus_BadSim: NetworkDeviceStatus = 3
NetworkDeviceStatus_DeviceHardwareFailure: NetworkDeviceStatus = 4
NetworkDeviceStatus_AccountNotActivated: NetworkDeviceStatus = 5
NetworkDeviceStatus_DeviceLocked: NetworkDeviceStatus = 6
NetworkDeviceStatus_DeviceBlocked: NetworkDeviceStatus = 7
NetworkOperatorDataUsageNotificationKind = Int32
NetworkOperatorDataUsageNotificationKind_DataUsageProgress: NetworkOperatorDataUsageNotificationKind = 0
class NetworkOperatorDataUsageTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorDataUsageTriggerDetails'
    @winrt_mixinmethod
    def get_NotificationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind: ...
    NotificationKind = property(get_NotificationKind, None)
NetworkOperatorEventMessageType = Int32
NetworkOperatorEventMessageType_Gsm: NetworkOperatorEventMessageType = 0
NetworkOperatorEventMessageType_Cdma: NetworkOperatorEventMessageType = 1
NetworkOperatorEventMessageType_Ussd: NetworkOperatorEventMessageType = 2
NetworkOperatorEventMessageType_DataPlanThresholdReached: NetworkOperatorEventMessageType = 3
NetworkOperatorEventMessageType_DataPlanReset: NetworkOperatorEventMessageType = 4
NetworkOperatorEventMessageType_DataPlanDeleted: NetworkOperatorEventMessageType = 5
NetworkOperatorEventMessageType_ProfileConnected: NetworkOperatorEventMessageType = 6
NetworkOperatorEventMessageType_ProfileDisconnected: NetworkOperatorEventMessageType = 7
NetworkOperatorEventMessageType_RegisteredRoaming: NetworkOperatorEventMessageType = 8
NetworkOperatorEventMessageType_RegisteredHome: NetworkOperatorEventMessageType = 9
NetworkOperatorEventMessageType_TetheringEntitlementCheck: NetworkOperatorEventMessageType = 10
NetworkOperatorEventMessageType_TetheringOperationalStateChanged: NetworkOperatorEventMessageType = 11
NetworkOperatorEventMessageType_TetheringNumberOfClientsChanged: NetworkOperatorEventMessageType = 12
class NetworkOperatorNotificationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails'
    @winrt_mixinmethod
    def get_NotificationType(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EncodingType(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> Byte: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RuleId(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SmsMessage(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> win32more.Windows.Devices.Sms.ISmsMessage: ...
    @winrt_mixinmethod
    def AuthorizeTethering(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringEntitlementCheck, allow: Boolean, entitlementFailureReason: WinRT_String) -> Void: ...
    NotificationType = property(get_NotificationType, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    RuleId = property(get_RuleId, None)
    SmsMessage = property(get_SmsMessage, None)
class NetworkOperatorTetheringAccessPointConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_mixinmethod
    def get_Ssid(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Passphrase(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Passphrase(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IsBandSupported(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_mixinmethod
    def IsBandSupportedAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Band(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_mixinmethod
    def put_Band(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
    Band = property(get_Band, put_Band)
class NetworkOperatorTetheringClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient'
    @winrt_mixinmethod
    def get_MacAddress(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HostNames(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    MacAddress = property(get_MacAddress, None)
    HostNames = property(get_HostNames, None)
class NetworkOperatorTetheringManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager'
    @winrt_mixinmethod
    def get_MaxClientCount(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> UInt32: ...
    @winrt_mixinmethod
    def get_ClientCount(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> UInt32: ...
    @winrt_mixinmethod
    def get_TetheringOperationalState(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Networking.NetworkOperators.TetheringOperationalState: ...
    @winrt_mixinmethod
    def GetCurrentAccessPointConfiguration(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_mixinmethod
    def ConfigureAccessPointAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager, configuration: win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartTetheringAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def StopTetheringAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def GetTetheringClients(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClientManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient]: ...
    @winrt_classmethod
    def IsNoConnectionsTimeoutEnabled(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Boolean: ...
    @winrt_classmethod
    def EnableNoConnectionsTimeout(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Void: ...
    @winrt_classmethod
    def EnableNoConnectionsTimeoutAsync(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def DisableNoConnectionsTimeout(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Void: ...
    @winrt_classmethod
    def DisableNoConnectionsTimeoutAsync(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateFromConnectionProfileWithTargetAdapter(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics3, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile, adapter: win32more.Windows.Networking.Connectivity.NetworkAdapter) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    @winrt_classmethod
    def GetTetheringCapabilityFromConnectionProfile(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics2, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile) -> win32more.Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_classmethod
    def CreateFromConnectionProfile(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics2, profile: win32more.Windows.Networking.Connectivity.ConnectionProfile) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    @winrt_classmethod
    def GetTetheringCapability(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    MaxClientCount = property(get_MaxClientCount, None)
    ClientCount = property(get_ClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class NetworkOperatorTetheringOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> win32more.Windows.Networking.NetworkOperators.TetheringOperationStatus: ...
    @winrt_mixinmethod
    def get_AdditionalErrorMessage(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> WinRT_String: ...
    Status = property(get_Status, None)
    AdditionalErrorMessage = property(get_AdditionalErrorMessage, None)
NetworkOperatorsFdnContract: UInt32 = 65536
NetworkRegistrationState = Int32
NetworkRegistrationState_None: NetworkRegistrationState = 0
NetworkRegistrationState_Deregistered: NetworkRegistrationState = 1
NetworkRegistrationState_Searching: NetworkRegistrationState = 2
NetworkRegistrationState_Home: NetworkRegistrationState = 3
NetworkRegistrationState_Roaming: NetworkRegistrationState = 4
NetworkRegistrationState_Partner: NetworkRegistrationState = 5
NetworkRegistrationState_Denied: NetworkRegistrationState = 6
ProfileMediaType = Int32
ProfileMediaType_Wlan: ProfileMediaType = 0
ProfileMediaType_Wwan: ProfileMediaType = 1
class ProfileUsage(EasyCastStructure):
    UsageInMegabytes: UInt32
    LastSyncTime: win32more.Windows.Foundation.DateTime
class ProvisionFromXmlDocumentResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults'
    @winrt_mixinmethod
    def get_AllElementsProvisioned(self: win32more.Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults) -> Boolean: ...
    @winrt_mixinmethod
    def get_ProvisionResultsXml(self: win32more.Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults) -> WinRT_String: ...
    AllElementsProvisioned = property(get_AllElementsProvisioned, None)
    ProvisionResultsXml = property(get_ProvisionResultsXml, None)
class ProvisionedProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IProvisionedProfile
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisionedProfile'
    @winrt_mixinmethod
    def UpdateCost(self: win32more.Windows.Networking.NetworkOperators.IProvisionedProfile, value: win32more.Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_mixinmethod
    def UpdateUsage(self: win32more.Windows.Networking.NetworkOperators.IProvisionedProfile, value: win32more.Windows.Networking.NetworkOperators.ProfileUsage) -> Void: ...
class ProvisioningAgent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IProvisioningAgent
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisioningAgent'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Networking.NetworkOperators.ProvisioningAgent.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.NetworkOperators.ProvisioningAgent: ...
    @winrt_mixinmethod
    def ProvisionFromXmlDocumentAsync(self: win32more.Windows.Networking.NetworkOperators.IProvisioningAgent, provisioningXmlDocument: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults]: ...
    @winrt_mixinmethod
    def GetProvisionedProfile(self: win32more.Windows.Networking.NetworkOperators.IProvisioningAgent, mediaType: win32more.Windows.Networking.NetworkOperators.ProfileMediaType, profileName: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisionedProfile: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: win32more.Windows.Networking.NetworkOperators.IProvisioningAgentStaticMethods, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisioningAgent: ...
TetheringCapability = Int32
TetheringCapability_Enabled: TetheringCapability = 0
TetheringCapability_DisabledByGroupPolicy: TetheringCapability = 1
TetheringCapability_DisabledByHardwareLimitation: TetheringCapability = 2
TetheringCapability_DisabledByOperator: TetheringCapability = 3
TetheringCapability_DisabledBySku: TetheringCapability = 4
TetheringCapability_DisabledByRequiredAppNotInstalled: TetheringCapability = 5
TetheringCapability_DisabledDueToUnknownCause: TetheringCapability = 6
TetheringCapability_DisabledBySystemCapability: TetheringCapability = 7
class TetheringEntitlementCheckTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.TetheringEntitlementCheckTriggerDetails'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def AllowTethering(self: win32more.Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails) -> Void: ...
    @winrt_mixinmethod
    def DenyTethering(self: win32more.Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails, entitlementFailureReason: WinRT_String) -> Void: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
TetheringOperationStatus = Int32
TetheringOperationStatus_Success: TetheringOperationStatus = 0
TetheringOperationStatus_Unknown: TetheringOperationStatus = 1
TetheringOperationStatus_MobileBroadbandDeviceOff: TetheringOperationStatus = 2
TetheringOperationStatus_WiFiDeviceOff: TetheringOperationStatus = 3
TetheringOperationStatus_EntitlementCheckTimeout: TetheringOperationStatus = 4
TetheringOperationStatus_EntitlementCheckFailure: TetheringOperationStatus = 5
TetheringOperationStatus_OperationInProgress: TetheringOperationStatus = 6
TetheringOperationStatus_BluetoothDeviceOff: TetheringOperationStatus = 7
TetheringOperationStatus_NetworkLimitedConnectivity: TetheringOperationStatus = 8
TetheringOperationalState = Int32
TetheringOperationalState_Unknown: TetheringOperationalState = 0
TetheringOperationalState_On: TetheringOperationalState = 1
TetheringOperationalState_Off: TetheringOperationalState = 2
TetheringOperationalState_InTransition: TetheringOperationalState = 3
TetheringWiFiBand = Int32
TetheringWiFiBand_Auto: TetheringWiFiBand = 0
TetheringWiFiBand_TwoPointFourGigahertz: TetheringWiFiBand = 1
TetheringWiFiBand_FiveGigahertz: TetheringWiFiBand = 2
UiccAccessCondition = Int32
UiccAccessCondition_AlwaysAllowed: UiccAccessCondition = 0
UiccAccessCondition_Pin1: UiccAccessCondition = 1
UiccAccessCondition_Pin2: UiccAccessCondition = 2
UiccAccessCondition_Pin3: UiccAccessCondition = 3
UiccAccessCondition_Pin4: UiccAccessCondition = 4
UiccAccessCondition_Administrative5: UiccAccessCondition = 5
UiccAccessCondition_Administrative6: UiccAccessCondition = 6
UiccAccessCondition_NeverAllowed: UiccAccessCondition = 7
UiccAppKind = Int32
UiccAppKind_Unknown: UiccAppKind = 0
UiccAppKind_MF: UiccAppKind = 1
UiccAppKind_MFSim: UiccAppKind = 2
UiccAppKind_MFRuim: UiccAppKind = 3
UiccAppKind_USim: UiccAppKind = 4
UiccAppKind_CSim: UiccAppKind = 5
UiccAppKind_ISim: UiccAppKind = 6
UiccAppRecordKind = Int32
UiccAppRecordKind_Unknown: UiccAppRecordKind = 0
UiccAppRecordKind_Transparent: UiccAppRecordKind = 1
UiccAppRecordKind_RecordOriented: UiccAppRecordKind = 2
class UssdMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IUssdMessage
    _classid_ = 'Windows.Networking.NetworkOperators.UssdMessage'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Networking.NetworkOperators.UssdMessage.CreateMessage(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateMessage(cls: win32more.Windows.Networking.NetworkOperators.IUssdMessageFactory, messageText: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdMessage: ...
    @winrt_mixinmethod
    def get_DataCodingScheme(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage) -> Byte: ...
    @winrt_mixinmethod
    def put_DataCodingScheme(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def GetPayload(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage) -> SZArray[Byte]: ...
    @winrt_mixinmethod
    def SetPayload(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage, value: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def get_PayloadAsText(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayloadAsText(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage, value: WinRT_String) -> Void: ...
    DataCodingScheme = property(get_DataCodingScheme, put_DataCodingScheme)
    PayloadAsText = property(get_PayloadAsText, put_PayloadAsText)
class UssdReply(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IUssdReply
    _classid_ = 'Windows.Networking.NetworkOperators.UssdReply'
    @winrt_mixinmethod
    def get_ResultCode(self: win32more.Windows.Networking.NetworkOperators.IUssdReply) -> win32more.Windows.Networking.NetworkOperators.UssdResultCode: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Networking.NetworkOperators.IUssdReply) -> win32more.Windows.Networking.NetworkOperators.UssdMessage: ...
    ResultCode = property(get_ResultCode, None)
    Message = property(get_Message, None)
UssdResultCode = Int32
UssdResultCode_NoActionRequired: UssdResultCode = 0
UssdResultCode_ActionRequired: UssdResultCode = 1
UssdResultCode_Terminated: UssdResultCode = 2
UssdResultCode_OtherLocalClient: UssdResultCode = 3
UssdResultCode_OperationNotSupported: UssdResultCode = 4
UssdResultCode_NetworkTimeout: UssdResultCode = 5
class UssdSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IUssdSession
    _classid_ = 'Windows.Networking.NetworkOperators.UssdSession'
    @winrt_mixinmethod
    def SendMessageAndGetReplyAsync(self: win32more.Windows.Networking.NetworkOperators.IUssdSession, message: win32more.Windows.Networking.NetworkOperators.UssdMessage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.UssdReply]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Networking.NetworkOperators.IUssdSession) -> Void: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: win32more.Windows.Networking.NetworkOperators.IUssdSessionStatics, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdSession: ...
    @winrt_classmethod
    def CreateFromNetworkInterfaceId(cls: win32more.Windows.Networking.NetworkOperators.IUssdSessionStatics, networkInterfaceId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdSession: ...
make_ready(__name__)
