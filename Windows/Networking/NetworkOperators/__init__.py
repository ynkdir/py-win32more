from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Data.Xml.Dom
import Windows.Devices.Sms
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Connectivity
import Windows.Networking.NetworkOperators
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESim'
    @winrt_mixinmethod
    def get_AvailableMemoryInBytes(self: Windows.Networking.NetworkOperators.IESim) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_Eid(self: Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirmwareVersion(self: Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MobileBroadbandModemDeviceId(self: Windows.Networking.NetworkOperators.IESim) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: Windows.Networking.NetworkOperators.IESim) -> Windows.Networking.NetworkOperators.ESimPolicy: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.NetworkOperators.IESim) -> Windows.Networking.NetworkOperators.ESimState: ...
    @winrt_mixinmethod
    def GetProfiles(self: Windows.Networking.NetworkOperators.IESim) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.ESimProfile]: ...
    @winrt_mixinmethod
    def DeleteProfileAsync(self: Windows.Networking.NetworkOperators.IESim, profileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def DownloadProfileMetadataAsync(self: Windows.Networking.NetworkOperators.IESim, activationCode: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult]: ...
    @winrt_mixinmethod
    def ResetAsync(self: Windows.Networking.NetworkOperators.IESim) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def add_ProfileChanged(self: Windows.Networking.NetworkOperators.IESim, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESim, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProfileChanged(self: Windows.Networking.NetworkOperators.IESim, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Discover(self: Windows.Networking.NetworkOperators.IESim2) -> Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_mixinmethod
    def DiscoverWithServerAddressAndMatchingId(self: Windows.Networking.NetworkOperators.IESim2, serverAddress: WinRT_String, matchingId: WinRT_String) -> Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_mixinmethod
    def DiscoverAsync(self: Windows.Networking.NetworkOperators.IESim2) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_mixinmethod
    def DiscoverWithServerAddressAndMatchingIdAsync(self: Windows.Networking.NetworkOperators.IESim2, serverAddress: WinRT_String, matchingId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_mixinmethod
    def get_SlotIndex(self: Windows.Networking.NetworkOperators.IESim3) -> Windows.Foundation.IReference[Int32]: ...
    AvailableMemoryInBytes = property(get_AvailableMemoryInBytes, None)
    Eid = property(get_Eid, None)
    FirmwareVersion = property(get_FirmwareVersion, None)
    MobileBroadbandModemDeviceId = property(get_MobileBroadbandModemDeviceId, None)
    Policy = property(get_Policy, None)
    State = property(get_State, None)
    SlotIndex = property(get_SlotIndex, None)
class ESimAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimAddedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: Windows.Networking.NetworkOperators.IESimAddedEventArgs) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
ESimAuthenticationPreference = Int32
ESimAuthenticationPreference_OnEntry: ESimAuthenticationPreference = 0
ESimAuthenticationPreference_OnAction: ESimAuthenticationPreference = 1
ESimAuthenticationPreference_Never: ESimAuthenticationPreference = 2
class ESimDiscoverEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDiscoverEvent'
    @winrt_mixinmethod
    def get_MatchingId(self: Windows.Networking.NetworkOperators.IESimDiscoverEvent) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RspServerAddress(self: Windows.Networking.NetworkOperators.IESimDiscoverEvent) -> WinRT_String: ...
    MatchingId = property(get_MatchingId, None)
    RspServerAddress = property(get_RspServerAddress, None)
class ESimDiscoverResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDiscoverResult'
    @winrt_mixinmethod
    def get_Events(self: Windows.Networking.NetworkOperators.IESimDiscoverResult) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.ESimDiscoverEvent]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Networking.NetworkOperators.IESimDiscoverResult) -> Windows.Networking.NetworkOperators.ESimDiscoverResultKind: ...
    @winrt_mixinmethod
    def get_ProfileMetadata(self: Windows.Networking.NetworkOperators.IESimDiscoverResult) -> Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    @winrt_mixinmethod
    def get_Result(self: Windows.Networking.NetworkOperators.IESimDiscoverResult) -> Windows.Networking.NetworkOperators.ESimOperationResult: ...
    Events = property(get_Events, None)
    Kind = property(get_Kind, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
ESimDiscoverResultKind = Int32
ESimDiscoverResultKind_None: ESimDiscoverResultKind = 0
ESimDiscoverResultKind_Events: ESimDiscoverResultKind = 1
ESimDiscoverResultKind_ProfileMetadata: ESimDiscoverResultKind = 2
class ESimDownloadProfileMetadataResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult'
    @winrt_mixinmethod
    def get_Result(self: Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> Windows.Networking.NetworkOperators.ESimOperationResult: ...
    @winrt_mixinmethod
    def get_ProfileMetadata(self: Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    Result = property(get_Result, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
class ESimManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimManager'
    @winrt_classmethod
    def get_ServiceInfo(cls: Windows.Networking.NetworkOperators.IESimManagerStatics) -> Windows.Networking.NetworkOperators.ESimServiceInfo: ...
    @winrt_classmethod
    def TryCreateESimWatcher(cls: Windows.Networking.NetworkOperators.IESimManagerStatics) -> Windows.Networking.NetworkOperators.ESimWatcher: ...
    @winrt_classmethod
    def add_ServiceInfoChanged(cls: Windows.Networking.NetworkOperators.IESimManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ServiceInfoChanged(cls: Windows.Networking.NetworkOperators.IESimManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ServiceInfo = property(get_ServiceInfo, None)
class ESimOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimOperationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IESimOperationResult) -> Windows.Networking.NetworkOperators.ESimOperationStatus: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimPolicy'
    @winrt_mixinmethod
    def get_ShouldEnableManagingUi(self: Windows.Networking.NetworkOperators.IESimPolicy) -> Boolean: ...
    ShouldEnableManagingUi = property(get_ShouldEnableManagingUi, None)
class ESimProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfile'
    @winrt_mixinmethod
    def get_Class(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Networking.NetworkOperators.ESimProfileClass: ...
    @winrt_mixinmethod
    def get_Nickname(self: Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Policy(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderIcon(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderName(self: Windows.Networking.NetworkOperators.IESimProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Networking.NetworkOperators.ESimProfileState: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Networking.NetworkOperators.IESimProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def SetNicknameAsync(self: Windows.Networking.NetworkOperators.IESimProfile, newNickname: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfileMetadata'
    @winrt_mixinmethod
    def get_IsConfirmationCodeRequired(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Boolean: ...
    @winrt_mixinmethod
    def get_Policy(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderIcon(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderName(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Networking.NetworkOperators.ESimProfileMetadataState: ...
    @winrt_mixinmethod
    def DenyInstallAsync(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def ConfirmInstallAsync(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.NetworkOperators.ESimOperationResult, Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_mixinmethod
    def ConfirmInstallWithConfirmationCodeAsync(self: Windows.Networking.NetworkOperators.IESimProfileMetadata, confirmationCode: WinRT_String) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.NetworkOperators.ESimOperationResult, Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_mixinmethod
    def PostponeInstallAsync(self: Windows.Networking.NetworkOperators.IESimProfileMetadata) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Networking.NetworkOperators.IESimProfileMetadata, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimProfileMetadata, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Networking.NetworkOperators.IESimProfileMetadata, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimProfilePolicy'
    @winrt_mixinmethod
    def get_CanDelete(self: Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanDisable(self: Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsManagedByEnterprise(self: Windows.Networking.NetworkOperators.IESimProfilePolicy) -> Boolean: ...
    CanDelete = property(get_CanDelete, None)
    CanDisable = property(get_CanDisable, None)
    IsManagedByEnterprise = property(get_IsManagedByEnterprise, None)
ESimProfileState = Int32
ESimProfileState_Unknown: ESimProfileState = 0
ESimProfileState_Disabled: ESimProfileState = 1
ESimProfileState_Enabled: ESimProfileState = 2
ESimProfileState_Deleted: ESimProfileState = 3
class ESimRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimRemovedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: Windows.Networking.NetworkOperators.IESimRemovedEventArgs) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class ESimServiceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimServiceInfo'
    @winrt_mixinmethod
    def get_AuthenticationPreference(self: Windows.Networking.NetworkOperators.IESimServiceInfo) -> Windows.Networking.NetworkOperators.ESimAuthenticationPreference: ...
    @winrt_mixinmethod
    def get_IsESimUiEnabled(self: Windows.Networking.NetworkOperators.IESimServiceInfo) -> Boolean: ...
    AuthenticationPreference = property(get_AuthenticationPreference, None)
    IsESimUiEnabled = property(get_IsESimUiEnabled, None)
ESimState = Int32
ESimState_Unknown: ESimState = 0
ESimState_Idle: ESimState = 1
ESimState_Removed: ESimState = 2
ESimState_Busy: ESimState = 3
class ESimUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimUpdatedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: Windows.Networking.NetworkOperators.IESimUpdatedEventArgs) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class ESimWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ESimWatcher'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IESimWatcher) -> Windows.Networking.NetworkOperators.ESimWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Networking.NetworkOperators.IESimWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Networking.NetworkOperators.IESimWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Added(self: Windows.Networking.NetworkOperators.IESimWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Networking.NetworkOperators.IESimWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Networking.NetworkOperators.IESimWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Networking.NetworkOperators.IESimWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Networking.NetworkOperators.IESimWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Networking.NetworkOperators.IESimWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Networking.NetworkOperators.IESimWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Networking.NetworkOperators.IESimWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Networking.NetworkOperators.IESimWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Networking.NetworkOperators.IESimWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
ESimWatcherStatus = Int32
ESimWatcherStatus_Created: ESimWatcherStatus = 0
ESimWatcherStatus_Started: ESimWatcherStatus = 1
ESimWatcherStatus_EnumerationCompleted: ESimWatcherStatus = 2
ESimWatcherStatus_Stopping: ESimWatcherStatus = 3
ESimWatcherStatus_Stopped: ESimWatcherStatus = 4
class FdnAccessManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.FdnAccessManager'
    @winrt_classmethod
    def RequestUnlockAsync(cls: Windows.Networking.NetworkOperators.IFdnAccessManagerStatics, contactListId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class HotspotAuthenticationContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotAuthenticationContext'
    @winrt_mixinmethod
    def get_WirelessNetworkId(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_NetworkAdapter(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def get_RedirectMessageUrl(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_RedirectMessageXml(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_AuthenticationUrl(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def IssueCredentials(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> Void: ...
    @winrt_mixinmethod
    def AbortAuthentication(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, markAsManual: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SkipAuthentication(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> Void: ...
    @winrt_mixinmethod
    def TriggerAttentionRequired(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext, packageRelativeApplicationId: WinRT_String, applicationParameters: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IssueCredentialsAsync(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationContext2, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult]: ...
    @winrt_classmethod
    def TryGetAuthenticationContext(cls: Windows.Networking.NetworkOperators.IHotspotAuthenticationContextStatics, evenToken: WinRT_String, context: POINTER(Windows.Networking.NetworkOperators.HotspotAuthenticationContext)) -> Boolean: ...
    WirelessNetworkId = property(get_WirelessNetworkId, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    RedirectMessageUrl = property(get_RedirectMessageUrl, None)
    RedirectMessageXml = property(get_RedirectMessageXml, None)
    AuthenticationUrl = property(get_AuthenticationUrl, None)
class HotspotAuthenticationEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotAuthenticationEventDetails'
    @winrt_mixinmethod
    def get_EventToken(self: Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails) -> WinRT_String: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult'
    @winrt_mixinmethod
    def get_HasNetworkErrorOccurred(self: Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResponseCode(self: Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> Windows.Networking.NetworkOperators.HotspotAuthenticationResponseCode: ...
    @winrt_mixinmethod
    def get_LogoffUrl(self: Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AuthenticationReplyXml(self: Windows.Networking.NetworkOperators.IHotspotCredentialsAuthenticationResult) -> Windows.Data.Xml.Dom.XmlDocument: ...
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    ResponseCode = property(get_ResponseCode, None)
    LogoffUrl = property(get_LogoffUrl, None)
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
class IESim(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6f6e6e26-f123-437d-8c-ed-dc-1d-2b-c0-c3-a9')
    @winrt_commethod(6)
    def get_AvailableMemoryInBytes(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_Eid(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FirmwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MobileBroadbandModemDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Policy(self) -> Windows.Networking.NetworkOperators.ESimPolicy: ...
    @winrt_commethod(11)
    def get_State(self) -> Windows.Networking.NetworkOperators.ESimState: ...
    @winrt_commethod(12)
    def GetProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.ESimProfile]: ...
    @winrt_commethod(13)
    def DeleteProfileAsync(self, profileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(14)
    def DownloadProfileMetadataAsync(self, activationCode: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult]: ...
    @winrt_commethod(15)
    def ResetAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(16)
    def add_ProfileChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESim, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AvailableMemoryInBytes = property(get_AvailableMemoryInBytes, None)
    Eid = property(get_Eid, None)
    FirmwareVersion = property(get_FirmwareVersion, None)
    MobileBroadbandModemDeviceId = property(get_MobileBroadbandModemDeviceId, None)
    Policy = property(get_Policy, None)
    State = property(get_State, None)
class IESim2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bd4fd0a0-c68f-56eb-b9-9b-8f-34-b8-10-02-99')
    @winrt_commethod(6)
    def Discover(self) -> Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_commethod(7)
    def DiscoverWithServerAddressAndMatchingId(self, serverAddress: WinRT_String, matchingId: WinRT_String) -> Windows.Networking.NetworkOperators.ESimDiscoverResult: ...
    @winrt_commethod(8)
    def DiscoverAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
    @winrt_commethod(9)
    def DiscoverWithServerAddressAndMatchingIdAsync(self, serverAddress: WinRT_String, matchingId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimDiscoverResult]: ...
class IESim3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fe1edf45-01b8-5d31-b8-d3-d9-cb-eb-b2-b8-31')
    @winrt_commethod(6)
    def get_SlotIndex(self) -> Windows.Foundation.IReference[Int32]: ...
    SlotIndex = property(get_SlotIndex, None)
class IESimAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38bd0a58-4d5a-4d08-8d-a7-e7-3e-ff-36-9d-dd')
    @winrt_commethod(6)
    def get_ESim(self) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimDiscoverEvent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e59ac3e3-39bc-5f6f-93-21-0d-4a-18-2d-26-1b')
    @winrt_commethod(6)
    def get_MatchingId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RspServerAddress(self) -> WinRT_String: ...
    MatchingId = property(get_MatchingId, None)
    RspServerAddress = property(get_RspServerAddress, None)
class IESimDiscoverResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('56b4bb5e-ab2f-5ac6-b3-59-dd-5a-8e-23-79-26')
    @winrt_commethod(6)
    def get_Events(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.ESimDiscoverEvent]: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.Networking.NetworkOperators.ESimDiscoverResultKind: ...
    @winrt_commethod(8)
    def get_ProfileMetadata(self) -> Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    @winrt_commethod(9)
    def get_Result(self) -> Windows.Networking.NetworkOperators.ESimOperationResult: ...
    Events = property(get_Events, None)
    Kind = property(get_Kind, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
class IESimDownloadProfileMetadataResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c4234d9e-5ad6-426d-8d-00-44-34-f4-49-af-ec')
    @winrt_commethod(6)
    def get_Result(self) -> Windows.Networking.NetworkOperators.ESimOperationResult: ...
    @winrt_commethod(7)
    def get_ProfileMetadata(self) -> Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    Result = property(get_Result, None)
    ProfileMetadata = property(get_ProfileMetadata, None)
class IESimManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0bfa2c0c-df88-4631-bf-04-c1-2e-28-1b-39-62')
    @winrt_commethod(6)
    def get_ServiceInfo(self) -> Windows.Networking.NetworkOperators.ESimServiceInfo: ...
    @winrt_commethod(7)
    def TryCreateESimWatcher(self) -> Windows.Networking.NetworkOperators.ESimWatcher: ...
    @winrt_commethod(8)
    def add_ServiceInfoChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ServiceInfoChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ServiceInfo = property(get_ServiceInfo, None)
class IESimOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a67b63b1-309b-4e77-9e-7e-cd-93-f1-dd-c7-b9')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.ESimOperationStatus: ...
    Status = property(get_Status, None)
class IESimPolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('41e1b99d-cf7e-4315-88-2b-6f-1e-74-b0-d3-8f')
    @winrt_commethod(6)
    def get_ShouldEnableManagingUi(self) -> Boolean: ...
    ShouldEnableManagingUi = property(get_ShouldEnableManagingUi, None)
class IESimProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ee1e7880-06a9-4027-b4-f8-dd-b2-3d-78-10-e0')
    @winrt_commethod(6)
    def get_Class(self) -> Windows.Networking.NetworkOperators.ESimProfileClass: ...
    @winrt_commethod(7)
    def get_Nickname(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Policy(self) -> Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_commethod(9)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ProviderIcon(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ProviderName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_State(self) -> Windows.Networking.NetworkOperators.ESimProfileState: ...
    @winrt_commethod(14)
    def DisableAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(15)
    def EnableAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(16)
    def SetNicknameAsync(self, newNickname: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    Class = property(get_Class, None)
    Nickname = property(get_Nickname, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
class IESimProfileMetadata(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ed25831f-90db-498d-a7-b4-eb-ce-80-7d-3c-23')
    @winrt_commethod(6)
    def get_IsConfirmationCodeRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Policy(self) -> Windows.Networking.NetworkOperators.ESimProfilePolicy: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ProviderIcon(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(10)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ProviderName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_State(self) -> Windows.Networking.NetworkOperators.ESimProfileMetadataState: ...
    @winrt_commethod(13)
    def DenyInstallAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(14)
    def ConfirmInstallAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.NetworkOperators.ESimOperationResult, Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_commethod(15)
    def ConfirmInstallWithConfirmationCodeAsync(self, confirmationCode: WinRT_String) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.NetworkOperators.ESimOperationResult, Windows.Networking.NetworkOperators.ESimProfileInstallProgress]: ...
    @winrt_commethod(16)
    def PostponeInstallAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ESimOperationResult]: ...
    @winrt_commethod(17)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimProfileMetadata, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsConfirmationCodeRequired = property(get_IsConfirmationCodeRequired, None)
    Policy = property(get_Policy, None)
    Id = property(get_Id, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
class IESimProfilePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e6dd0f1d-9c5c-46c5-a2-89-a9-48-99-9b-f0-62')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dec5277b-2fd9-4ed9-83-76-d9-b5-e4-12-78-a3')
    @winrt_commethod(6)
    def get_ESim(self) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimServiceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f16aabcf-7f59-4a51-84-94-bd-89-d5-ff-50-ee')
    @winrt_commethod(6)
    def get_AuthenticationPreference(self) -> Windows.Networking.NetworkOperators.ESimAuthenticationPreference: ...
    @winrt_commethod(7)
    def get_IsESimUiEnabled(self) -> Boolean: ...
    AuthenticationPreference = property(get_AuthenticationPreference, None)
    IsESimUiEnabled = property(get_IsESimUiEnabled, None)
class IESimUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4c125cec-508d-4b88-83-cb-68-be-f8-16-8d-12')
    @winrt_commethod(6)
    def get_ESim(self) -> Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class IESimWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c1f84ceb-a28d-4fbf-97-71-6e-31-b8-1c-cf-22')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.ESimWatcherStatus: ...
    @winrt_commethod(7)
    def Start(self) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.ESimWatcher, Windows.Networking.NetworkOperators.ESimUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IFdnAccessManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f2aa4395-f1e6-4319-aa-3e-47-7c-a6-4b-2b-df')
    @winrt_commethod(6)
    def RequestUnlockAsync(self, contactListId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IHotspotAuthenticationContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e756c791-1003-4de5-83-c7-de-61-d8-88-31-d0')
    @winrt_commethod(6)
    def get_WirelessNetworkId(self) -> c_char_p_no: ...
    @winrt_commethod(7)
    def get_NetworkAdapter(self) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(8)
    def get_RedirectMessageUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_RedirectMessageXml(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(10)
    def get_AuthenticationUrl(self) -> Windows.Foundation.Uri: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e756c791-1004-4de5-83-c7-de-61-d8-88-31-d0')
    @winrt_commethod(6)
    def IssueCredentialsAsync(self, userName: WinRT_String, password: WinRT_String, extraParameters: WinRT_String, markAsManualConnectOnFailure: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.HotspotCredentialsAuthenticationResult]: ...
class IHotspotAuthenticationContextStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e756c791-1002-4de5-83-c7-de-61-d8-88-31-d0')
    @winrt_commethod(6)
    def TryGetAuthenticationContext(self, evenToken: WinRT_String, context: POINTER(Windows.Networking.NetworkOperators.HotspotAuthenticationContext)) -> Boolean: ...
class IHotspotAuthenticationEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e756c791-1001-4de5-83-c7-de-61-d8-88-31-d0')
    @winrt_commethod(6)
    def get_EventToken(self) -> WinRT_String: ...
    EventToken = property(get_EventToken, None)
class IHotspotCredentialsAuthenticationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e756c791-1005-4de5-83-c7-de-61-d8-88-31-d0')
    @winrt_commethod(6)
    def get_HasNetworkErrorOccurred(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ResponseCode(self) -> Windows.Networking.NetworkOperators.HotspotAuthenticationResponseCode: ...
    @winrt_commethod(8)
    def get_LogoffUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_AuthenticationReplyXml(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    ResponseCode = property(get_ResponseCode, None)
    LogoffUrl = property(get_LogoffUrl, None)
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
class IKnownCSimFilePathsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b458aeed-49f1-4c22-b0-73-96-d5-11-bf-9c-35')
    @winrt_commethod(6)
    def get_EFSpn(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_Gid1(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid2(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownRuimFilePathsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3883c8b9-ff24-4571-a8-67-09-f9-60-42-6e-14')
    @winrt_commethod(6)
    def get_EFSpn(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_Gid1(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid2(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownSimFilePathsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('80cd1a63-37a5-43d3-80-a3-cc-d2-3e-8f-ec-ee')
    @winrt_commethod(6)
    def get_EFOns(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_EFSpn(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_Gid1(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(9)
    def get_Gid2(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFOns = property(get_EFOns, None)
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IKnownUSimFilePathsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7c34e581-1f1b-43f4-95-30-8b-09-2d-32-d7-1f')
    @winrt_commethod(6)
    def get_EFSpn(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def get_EFOpl(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_EFPnn(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(9)
    def get_Gid1(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(10)
    def get_Gid2(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    EFOpl = property(get_EFOpl, None)
    EFPnn = property(get_EFPnn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class IMobileBroadbandAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('36c24ccd-cee2-43e0-a6-03-ee-86-a3-6d-65-70')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceProviderGuid(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ServiceProviderName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CurrentNetwork(self) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_commethod(10)
    def get_CurrentDeviceInformation(self) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
class IMobileBroadbandAccount2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38f52f1c-1136-4257-95-9f-b6-58-a3-52-b6-d4')
    @winrt_commethod(6)
    def GetConnectionProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]: ...
class IMobileBroadbandAccount3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('092a1e21-9379-4b9b-ad-31-d5-fe-e2-f7-48-c6')
    @winrt_commethod(6)
    def get_AccountExperienceUrl(self) -> Windows.Foundation.Uri: ...
    AccountExperienceUrl = property(get_AccountExperienceUrl, None)
class IMobileBroadbandAccountEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3853c880-77de-4c04-be-ad-a1-23-b0-8c-9f-59')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class IMobileBroadbandAccountStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aa7f4d24-afc1-4fc8-ae-9a-a9-17-53-10-fa-ad')
    @winrt_commethod(6)
    def get_AvailableNetworkAccountIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    AvailableNetworkAccountIds = property(get_AvailableNetworkAccountIds, None)
class IMobileBroadbandAccountUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7bc31d88-a6bd-49e1-80-ab-6b-91-35-4a-57-d4')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6bf3335e-23b5-449f-92-8d-5e-0d-3e-04-47-1d')
    @winrt_commethod(6)
    def add_AccountAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountAdded(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_AccountUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AccountUpdated(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AccountRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AccountRemoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_Stopped(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IMobileBroadbandAntennaSar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b9af4b7e-cbf9-4109-90-be-5c-06-bf-d5-13-b6')
    @winrt_commethod(6)
    def get_AntennaIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def get_SarBackoffIndex(self) -> Int32: ...
    AntennaIndex = property(get_AntennaIndex, None)
    SarBackoffIndex = property(get_SarBackoffIndex, None)
class IMobileBroadbandAntennaSarFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a91e1716-c04d-4a21-86-98-14-59-dc-67-2c-6e')
    @winrt_commethod(6)
    def CreateWithIndex(self, antennaIndex: Int32, sarBackoffIndex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar: ...
class IMobileBroadbandCellCdma(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0601b3b4-411a-4f2e-82-87-76-f5-65-0c-60-cd')
    @winrt_commethod(6)
    def get_BaseStationId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_BaseStationPNCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_BaseStationLatitude(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_BaseStationLongitude(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(10)
    def get_BaseStationLastBroadcastGpsTime(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def get_NetworkId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(12)
    def get_PilotSignalStrengthInDB(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_SystemId(self) -> Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    NetworkId = property(get_NetworkId, None)
    PilotSignalStrengthInDB = property(get_PilotSignalStrengthInDB, None)
    SystemId = property(get_SystemId, None)
class IMobileBroadbandCellGsm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cc917f06-7ee0-47b8-9e-1f-c3-b4-8d-f9-df-5b')
    @winrt_commethod(6)
    def get_BaseStationId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_CellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ChannelNumber(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_LocationAreaCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ReceivedSignalStrengthInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInBitPeriods(self) -> Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalStrengthInDBm = property(get_ReceivedSignalStrengthInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class IMobileBroadbandCellLte(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9197c87b-2b78-456d-8b-53-aa-a2-5d-0a-f7-41')
    @winrt_commethod(6)
    def get_CellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_PhysicalCellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ReferenceSignalReceivedPowerInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ReferenceSignalReceivedQualityInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInBitPeriods(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def get_TrackingAreaCode(self) -> Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
class IMobileBroadbandCellNR(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a13f0deb-66fc-4b4b-83-a9-a4-87-a3-a5-a0-a6')
    @winrt_commethod(6)
    def get_CellId(self) -> Windows.Foundation.IReference[Int64]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_PhysicalCellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ReferenceSignalReceivedPowerInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ReferenceSignalReceivedQualityInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_TimingAdvanceInNanoseconds(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def get_TrackingAreaCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(14)
    def get_SignalToNoiseRatioInDB(self) -> Windows.Foundation.IReference[Double]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0eda1655-db0e-4182-8c-da-cc-41-9a-7b-de-08')
    @winrt_commethod(6)
    def get_CellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_CellParameterId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ChannelNumber(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_LocationAreaCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def get_PathLossInDB(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ReceivedSignalCodePowerInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_TimingAdvanceInBitPeriods(self) -> Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    CellParameterId = property(get_CellParameterId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class IMobileBroadbandCellUmts(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('77b4b5ae-49c8-4f15-b2-85-4c-26-a7-f6-72-15')
    @winrt_commethod(6)
    def get_CellId(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(7)
    def get_ChannelNumber(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_LocationAreaCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def get_PathLossInDB(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(10)
    def get_PrimaryScramblingCode(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ReceivedSignalCodePowerInDBm(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_SignalToNoiseRatioInDB(self) -> Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    PrimaryScramblingCode = property(get_PrimaryScramblingCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class IMobileBroadbandCellsInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('89a9562a-e472-4da5-92-9c-de-61-71-1d-d2-61')
    @winrt_commethod(6)
    def get_NeighboringCellsCdma(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_commethod(7)
    def get_NeighboringCellsGsm(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_commethod(8)
    def get_NeighboringCellsLte(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_commethod(9)
    def get_NeighboringCellsTdscdma(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_commethod(10)
    def get_NeighboringCellsUmts(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_commethod(11)
    def get_ServingCellsCdma(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_commethod(12)
    def get_ServingCellsGsm(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_commethod(13)
    def get_ServingCellsLte(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_commethod(14)
    def get_ServingCellsTdscdma(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_commethod(15)
    def get_ServingCellsUmts(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('66205912-b89f-4e12-bb-b6-d5-cf-09-a8-20-ca')
    @winrt_commethod(6)
    def get_NeighboringCellsNR(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    @winrt_commethod(7)
    def get_ServingCellsNR(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    NeighboringCellsNR = property(get_NeighboringCellsNR, None)
    ServingCellsNR = property(get_ServingCellsNR, None)
class IMobileBroadbandCurrentSlotIndexChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f718b184-c370-5fd4-a6-70-18-46-cb-9b-ce-47')
    @winrt_commethod(6)
    def get_CurrentSlotIndex(self) -> Int32: ...
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class IMobileBroadbandDeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e6d08168-e381-4c6e-9b-e8-fe-15-69-69-a4-46')
    @winrt_commethod(6)
    def get_NetworkDeviceStatus(self) -> Windows.Networking.NetworkOperators.NetworkDeviceStatus: ...
    @winrt_commethod(7)
    def get_Manufacturer(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Model(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_FirmwareInformation(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(11)
    def get_DataClasses(self) -> Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_commethod(12)
    def get_CustomDataClass(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_MobileEquipmentId(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_TelephoneNumbers(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(15)
    def get_SubscriberId(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_SimIccId(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_DeviceType(self) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceType: ...
    @winrt_commethod(18)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_CurrentRadioState(self) -> Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2e467af1-f932-4737-a7-22-03-ba-72-37-0c-b8')
    @winrt_commethod(6)
    def get_PinManager(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinManager: ...
    @winrt_commethod(7)
    def get_Revision(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> WinRT_String: ...
    PinManager = property(get_PinManager, None)
    Revision = property(get_Revision, None)
    SerialNumber = property(get_SerialNumber, None)
class IMobileBroadbandDeviceInformation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e08bb4bd-5d30-4b5a-92-cc-d5-4d-f8-81-d4-9e')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('263f3152-7b9d-582c-b1-7c-f8-0a-60-b5-00-31')
    @winrt_commethod(6)
    def get_SlotManager(self) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotManager: ...
    SlotManager = property(get_SlotManager, None)
class IMobileBroadbandDeviceService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('22be1a52-bd80-40ac-8e-1f-2e-07-83-6a-3d-bd')
    @winrt_commethod(6)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SupportedCommands(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def OpenDataSession(self) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession: ...
    @winrt_commethod(9)
    def OpenCommandSession(self) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    SupportedCommands = property(get_SupportedCommands, None)
class IMobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b0f46abb-94d6-44b9-a5-38-f0-81-0b-64-53-89')
    @winrt_commethod(6)
    def get_StatusCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ResponseData(self) -> Windows.Storage.Streams.IBuffer: ...
    StatusCode = property(get_StatusCode, None)
    ResponseData = property(get_ResponseData, None)
class IMobileBroadbandDeviceServiceCommandSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fc098a45-913b-4914-b6-c3-ae-63-04-59-3e-75')
    @winrt_commethod(6)
    def SendQueryCommandAsync(self, commandId: UInt32, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_commethod(7)
    def SendSetCommandAsync(self, commandId: UInt32, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_commethod(8)
    def CloseSession(self) -> Void: ...
class IMobileBroadbandDeviceServiceDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b6aa13de-1380-40e3-86-18-73-cb-ca-48-13-8c')
    @winrt_commethod(6)
    def get_ReceivedData(self) -> Windows.Storage.Streams.IBuffer: ...
    ReceivedData = property(get_ReceivedData, None)
class IMobileBroadbandDeviceServiceDataSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dad62333-8bcf-4289-8a-37-04-5c-21-69-48-6a')
    @winrt_commethod(6)
    def WriteDataAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def CloseSession(self) -> Void: ...
    @winrt_commethod(8)
    def add_DataReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession, Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMobileBroadbandDeviceServiceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('53d69b5b-c4ed-45f0-80-3a-d9-41-7a-6d-98-46')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4a055b70-b9ae-4458-92-41-a6-a5-fb-f1-8a-0c')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ReceivedData(self) -> Windows.Storage.Streams.IBuffer: ...
    DeviceId = property(get_DeviceId, None)
    DeviceServiceId = property(get_DeviceServiceId, None)
    ReceivedData = property(get_ReceivedData, None)
class IMobileBroadbandDeviceServiceTriggerDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d83d5f16-336a-553f-94-bb-0c-d1-a2-ff-0c-81')
    @winrt_commethod(6)
    def get_EventId(self) -> UInt32: ...
    EventId = property(get_EventId, None)
class IMobileBroadbandModem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d0356912-e9f9-4f67-a0-3d-43-18-9a-31-6b-f1')
    @winrt_commethod(6)
    def get_CurrentAccount(self) -> Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    @winrt_commethod(7)
    def get_DeviceInformation(self) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_commethod(8)
    def get_MaxDeviceServiceCommandSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_MaxDeviceServiceDataSizeInBytes(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DeviceServices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation]: ...
    @winrt_commethod(11)
    def GetDeviceService(self, deviceServiceId: Guid) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceService: ...
    @winrt_commethod(12)
    def get_IsResetSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def ResetAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def GetCurrentConfigurationAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration]: ...
    @winrt_commethod(15)
    def get_CurrentNetwork(self) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    CurrentAccount = property(get_CurrentAccount, None)
    DeviceInformation = property(get_DeviceInformation, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
    DeviceServices = property(get_DeviceServices, None)
    IsResetSupported = property(get_IsResetSupported, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
class IMobileBroadbandModem2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('12862b28-b9eb-4ee2-bb-e3-71-1f-53-ee-a3-73')
    @winrt_commethod(6)
    def GetIsPassthroughEnabledAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def SetIsPassthroughEnabledAsync(self, value: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
class IMobileBroadbandModem3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e9fec6ea-2f34-4582-91-02-c3-14-d2-a8-7e-ec')
    @winrt_commethod(6)
    def TryGetPcoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPco]: ...
    @winrt_commethod(7)
    def get_IsInEmergencyCallMode(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_IsInEmergencyCallModeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandModem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsInEmergencyCallModeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInEmergencyCallMode = property(get_IsInEmergencyCallMode, None)
class IMobileBroadbandModem4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4a0398c2-91be-412b-b5-69-58-6e-9f-00-30-d1')
    @winrt_commethod(6)
    def SetIsPassthroughEnabledWithSlotIndexAsync(self, value: Boolean, slotindex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_commethod(7)
    def GetIsPassthroughEnabledWithSlotIndexAsync(self, slotindex: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def SetIsPassthroughEnabledWithSlotIndex(self, value: Boolean, slotindex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_commethod(9)
    def GetIsPassthroughEnabledWithSlotIndex(self, slotindex: Int32) -> Boolean: ...
class IMobileBroadbandModemConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fce035a3-d6cd-4320-b9-82-be-9d-3e-c7-89-0f')
    @winrt_commethod(6)
    def get_Uicc(self) -> Windows.Networking.NetworkOperators.MobileBroadbandUicc: ...
    @winrt_commethod(7)
    def get_HomeProviderId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_HomeProviderName(self) -> WinRT_String: ...
    Uicc = property(get_Uicc, None)
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
class IMobileBroadbandModemConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('320ff5c5-e460-42ae-aa-51-69-62-1e-7a-44-77')
    @winrt_commethod(6)
    def get_SarManager(self) -> Windows.Networking.NetworkOperators.MobileBroadbandSarManager: ...
    SarManager = property(get_SarManager, None)
class IMobileBroadbandModemIsolation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b5618fec-e661-4330-9b-b4-34-80-21-2e-c3-54')
    @winrt_commethod(6)
    def AddAllowedHost(self, host: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def AddAllowedHostRange(self, first: Windows.Networking.HostName, last: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(8)
    def ApplyConfigurationAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearConfigurationAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IMobileBroadbandModemIsolationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('21d7ec58-c2b1-4c2f-a0-30-72-82-0a-24-ec-d9')
    @winrt_commethod(6)
    def Create(self, modemDeviceId: WinRT_String, ruleGroupId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation: ...
class IMobileBroadbandModemStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f99ed637-d6f1-4a78-8c-bc-64-21-a6-50-63-c8')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    @winrt_commethod(8)
    def GetDefault(self) -> Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
class IMobileBroadbandNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cb63928c-0309-4cb6-a8-c1-6a-5a-3c-8e-1f-f6')
    @winrt_commethod(6)
    def get_NetworkAdapter(self) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_commethod(7)
    def get_NetworkRegistrationState(self) -> Windows.Networking.NetworkOperators.NetworkRegistrationState: ...
    @winrt_commethod(8)
    def get_RegistrationNetworkError(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PacketAttachNetworkError(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ActivationNetworkError(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_AccessPointName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_RegisteredDataClass(self) -> Windows.Networking.NetworkOperators.DataClasses: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5a55db22-62f7-4bdd-ba-1d-47-74-41-96-0b-a0')
    @winrt_commethod(6)
    def GetVoiceCallSupportAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def get_RegistrationUiccApps(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    RegistrationUiccApps = property(get_RegistrationUiccApps, None)
class IMobileBroadbandNetwork3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('33670a8a-c7ef-444c-ab-6c-df-7e-f7-a3-90-fe')
    @winrt_commethod(6)
    def GetCellsInfoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo]: ...
class IMobileBroadbandNetworkRegistrationStateChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('beaf94e1-960f-49b4-a0-8d-7d-85-e9-68-c7-ec')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Network(self) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    DeviceId = property(get_DeviceId, None)
    Network = property(get_Network, None)
class IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('89135cff-28b8-46aa-b1-37-1c-4b-0f-21-ed-fe')
    @winrt_commethod(6)
    def get_NetworkRegistrationStateChanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange]: ...
    NetworkRegistrationStateChanges = property(get_NetworkRegistrationStateChanges, None)
class IMobileBroadbandPco(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d4e4fcbe-e3a3-43c5-a8-7b-6c-86-d2-29-d7-fa')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    Data = property(get_Data, None)
    IsComplete = property(get_IsComplete, None)
    DeviceId = property(get_DeviceId, None)
class IMobileBroadbandPcoDataChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('263f5114-64e0-4493-90-9b-2d-14-a0-19-62-b1')
    @winrt_commethod(6)
    def get_UpdatedData(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPco: ...
    UpdatedData = property(get_UpdatedData, None)
class IMobileBroadbandPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e661d709-e779-45bf-82-81-75-32-3d-f9-e3-21')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_commethod(7)
    def get_LockState(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    @winrt_commethod(8)
    def get_Format(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinFormat: ...
    @winrt_commethod(9)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_MaxLength(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_MinLength(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_AttemptsRemaining(self) -> UInt32: ...
    @winrt_commethod(13)
    def EnableAsync(self, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(14)
    def DisableAsync(self, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(15)
    def EnterAsync(self, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(16)
    def ChangeAsync(self, currentPin: WinRT_String, newPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_commethod(17)
    def UnblockAsync(self, pinUnblockKey: WinRT_String, newPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    Type = property(get_Type, None)
    LockState = property(get_LockState, None)
    Format = property(get_Format, None)
    Enabled = property(get_Enabled, None)
    MaxLength = property(get_MaxLength, None)
    MinLength = property(get_MinLength, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
class IMobileBroadbandPinLockStateChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('be16673e-1f04-4f95-8b-90-e7-f5-59-dd-e7-e5')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PinType(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_commethod(8)
    def get_PinLockState(self) -> Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    DeviceId = property(get_DeviceId, None)
    PinType = property(get_PinType, None)
    PinLockState = property(get_PinLockState, None)
class IMobileBroadbandPinLockStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d338c091-3e91-4d38-90-36-ae-e8-3a-6e-79-ad')
    @winrt_commethod(6)
    def get_PinLockStateChanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange]: ...
    PinLockStateChanges = property(get_PinLockStateChanges, None)
class IMobileBroadbandPinManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('83567edd-6e1f-4b9b-a4-13-2b-1f-50-cc-36-df')
    @winrt_commethod(6)
    def get_SupportedPins(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandPinType]: ...
    @winrt_commethod(7)
    def GetPin(self, pinType: Windows.Networking.NetworkOperators.MobileBroadbandPinType) -> Windows.Networking.NetworkOperators.MobileBroadbandPin: ...
    SupportedPins = property(get_SupportedPins, None)
class IMobileBroadbandPinOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('11dddc32-31e7-49f5-b6-63-12-3d-3b-ef-03-62')
    @winrt_commethod(6)
    def get_IsSuccessful(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AttemptsRemaining(self) -> UInt32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    AttemptsRemaining = property(get_AttemptsRemaining, None)
class IMobileBroadbandRadioStateChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b054a561-9833-4aed-97-17-43-48-b2-1a-24-b3')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RadioState(self) -> Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    DeviceId = property(get_DeviceId, None)
    RadioState = property(get_RadioState, None)
class IMobileBroadbandRadioStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('71301ace-093c-42c6-b0-db-ad-1f-75-a6-54-45')
    @winrt_commethod(6)
    def get_RadioStateChanges(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange]: ...
    RadioStateChanges = property(get_RadioStateChanges, None)
class IMobileBroadbandSarManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e5b26833-967e-40c9-a4-85-19-c0-dd-20-9e-22')
    @winrt_commethod(6)
    def get_IsBackoffEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsWiFiHardwareIntegrated(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsSarControlledByHardware(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Antennas(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]: ...
    @winrt_commethod(10)
    def get_HysteresisTimerPeriod(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def add_TransmissionStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSarManager, Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_TransmissionStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def EnableBackoffAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def DisableBackoffAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def SetConfigurationAsync(self, antennas: Windows.Foundation.Collections.IIterable[Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def RevertSarToHardwareControlAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def SetTransmissionStateChangedHysteresisAsync(self, timerPeriod: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GetIsTransmittingAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bd350b32-882e-542a-b1-7d-0b-b1-b4-9b-ae-9e')
    @winrt_commethod(6)
    def get_Index(self) -> Int32: ...
    @winrt_commethod(7)
    def get_State(self) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotState: ...
    Index = property(get_Index, None)
    State = property(get_State, None)
class IMobileBroadbandSlotInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('393cb039-ca44-524c-82-2d-83-a3-62-0f-0e-fc')
    @winrt_commethod(6)
    def get_IccId(self) -> WinRT_String: ...
    IccId = property(get_IccId, None)
class IMobileBroadbandSlotInfoChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3158839f-950c-54ce-a4-8d-ba-45-29-b4-8f-0f')
    @winrt_commethod(6)
    def get_SlotInfo(self) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo: ...
    SlotInfo = property(get_SlotInfo, None)
class IMobileBroadbandSlotManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('eba07cd6-2019-5f81-a2-94-cc-36-4a-11-d0-b2')
    @winrt_commethod(6)
    def get_SlotInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo]: ...
    @winrt_commethod(7)
    def get_CurrentSlotIndex(self) -> Int32: ...
    @winrt_commethod(8)
    def SetCurrentSlot(self, slotIndex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_commethod(9)
    def SetCurrentSlotAsync(self, slotIndex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_commethod(10)
    def add_SlotInfoChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SlotInfoChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CurrentSlotIndexChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CurrentSlotIndexChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SlotInfos = property(get_SlotInfos, None)
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class IMobileBroadbandTransmissionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('612e3875-040a-4f99-a4-f9-61-d7-c3-2d-a1-29')
    @winrt_commethod(6)
    def get_IsTransmitting(self) -> Boolean: ...
    IsTransmitting = property(get_IsTransmitting, None)
class IMobileBroadbandUicc(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e634f691-525a-4ce2-8f-ce-aa-41-62-57-91-54')
    @winrt_commethod(6)
    def get_SimIccId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetUiccAppsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult]: ...
    SimIccId = property(get_SimIccId, None)
class IMobileBroadbandUiccApp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4d170556-98a1-43dd-b2-ec-50-c9-0c-f2-48-df')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.Networking.NetworkOperators.UiccAppKind: ...
    @winrt_commethod(8)
    def GetRecordDetailsAsync(self, uiccFilePath: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult]: ...
    @winrt_commethod(9)
    def ReadRecordAsync(self, uiccFilePath: Windows.Foundation.Collections.IIterable[UInt32], recordIndex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class IMobileBroadbandUiccAppReadRecordResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('64c95285-358e-47c5-82-49-69-5f-38-3b-2b-db')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Data = property(get_Data, None)
class IMobileBroadbandUiccAppRecordDetailsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d919682f-be14-4934-98-1d-2f-57-b9-ed-83-e6')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.Networking.NetworkOperators.UiccAppRecordKind: ...
    @winrt_commethod(8)
    def get_RecordCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_RecordSize(self) -> Int32: ...
    @winrt_commethod(10)
    def get_ReadAccessCondition(self) -> Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    @winrt_commethod(11)
    def get_WriteAccessCondition(self) -> Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    Status = property(get_Status, None)
    Kind = property(get_Kind, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    WriteAccessCondition = property(get_WriteAccessCondition, None)
class IMobileBroadbandUiccAppsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('744930eb-8157-4a41-84-94-6b-f5-4c-9b-1d-2b')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_commethod(7)
    def get_UiccApps(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    Status = property(get_Status, None)
    UiccApps = property(get_UiccApps, None)
class INetworkOperatorDataUsageTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('50e3126d-a465-4eeb-93-17-28-a1-67-63-0c-ea')
    @winrt_commethod(6)
    def get_NotificationKind(self) -> Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind: ...
    NotificationKind = property(get_NotificationKind, None)
class INetworkOperatorNotificationEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bc68a9d1-82e1-4488-9f-2c-12-76-c2-46-8f-ac')
    @winrt_commethod(6)
    def get_NotificationType(self) -> Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType: ...
    @winrt_commethod(7)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EncodingType(self) -> Byte: ...
    @winrt_commethod(9)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_RuleId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SmsMessage(self) -> Windows.Devices.Sms.ISmsMessage: ...
    NotificationType = property(get_NotificationType, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    RuleId = property(get_RuleId, None)
    SmsMessage = property(get_SmsMessage, None)
class INetworkOperatorTetheringAccessPointConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0bcc0284-412e-403d-ac-c6-b7-57-e3-47-74-a4')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b1809142-7238-59a0-92-8b-74-ab-46-fd-64-b6')
    @winrt_commethod(6)
    def IsBandSupported(self, band: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_commethod(7)
    def IsBandSupportedAsync(self, band: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Band(self) -> Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_commethod(9)
    def put_Band(self, value: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    Band = property(get_Band, put_Band)
class INetworkOperatorTetheringClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('709d254c-595f-4847-bb-30-64-69-35-54-29-18')
    @winrt_commethod(6)
    def get_MacAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HostNames(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    MacAddress = property(get_MacAddress, None)
    HostNames = property(get_HostNames, None)
class INetworkOperatorTetheringClientManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('91b14016-8dca-4225-bb-ed-ee-f8-b8-d7-18-d7')
    @winrt_commethod(6)
    def GetTetheringClients(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient]: ...
class INetworkOperatorTetheringEntitlementCheck(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0108916d-9e9a-4af6-8d-a3-60-49-3b-19-c2-04')
    @winrt_commethod(6)
    def AuthorizeTethering(self, allow: Boolean, entitlementFailureReason: WinRT_String) -> Void: ...
class INetworkOperatorTetheringManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d45a8da0-0e86-4d98-8b-a4-dd-70-d4-b7-64-d3')
    @winrt_commethod(6)
    def get_MaxClientCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ClientCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_TetheringOperationalState(self) -> Windows.Networking.NetworkOperators.TetheringOperationalState: ...
    @winrt_commethod(9)
    def GetCurrentAccessPointConfiguration(self) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_commethod(10)
    def ConfigureAccessPointAsync(self, configuration: Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def StartTetheringAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_commethod(12)
    def StopTetheringAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    MaxClientCount = property(get_MaxClientCount, None)
    ClientCount = property(get_ClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class INetworkOperatorTetheringManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3ebcbacc-f8c3-405c-99-64-70-a1-ee-ab-e1-94')
    @winrt_commethod(6)
    def GetTetheringCapability(self, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_commethod(7)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5b235412-35f0-49e7-9b-08-16-d2-78-fb-aa-42')
    @winrt_commethod(6)
    def GetTetheringCapabilityFromConnectionProfile(self, profile: Windows.Networking.Connectivity.ConnectionProfile) -> Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_commethod(7)
    def CreateFromConnectionProfile(self, profile: Windows.Networking.Connectivity.ConnectionProfile) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8fdaadb6-4af9-4f21-9b-58-d5-3e-9f-24-23-1e')
    @winrt_commethod(6)
    def CreateFromConnectionProfileWithTargetAdapter(self, profile: Windows.Networking.Connectivity.ConnectionProfile, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
class INetworkOperatorTetheringManagerStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b3b9f9d0-ebff-46a4-a8-47-d6-63-d8-b0-97-7e')
    @winrt_commethod(6)
    def IsNoConnectionsTimeoutEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def EnableNoConnectionsTimeout(self) -> Void: ...
    @winrt_commethod(8)
    def EnableNoConnectionsTimeoutAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DisableNoConnectionsTimeout(self) -> Void: ...
    @winrt_commethod(10)
    def DisableNoConnectionsTimeoutAsync(self) -> Windows.Foundation.IAsyncAction: ...
class INetworkOperatorTetheringOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ebd203a1-01ba-476d-b4-b3-bf-3d-12-c8-f8-0c')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Networking.NetworkOperators.TetheringOperationStatus: ...
    @winrt_commethod(7)
    def get_AdditionalErrorMessage(self) -> WinRT_String: ...
    Status = property(get_Status, None)
    AdditionalErrorMessage = property(get_AdditionalErrorMessage, None)
class IProvisionFromXmlDocumentResults(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('217700e0-8203-11df-ad-b9-f4-ce-46-2d-91-37')
    @winrt_commethod(6)
    def get_AllElementsProvisioned(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ProvisionResultsXml(self) -> WinRT_String: ...
    AllElementsProvisioned = property(get_AllElementsProvisioned, None)
    ProvisionResultsXml = property(get_ProvisionResultsXml, None)
class IProvisionedProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('217700e0-8202-11df-ad-b9-f4-ce-46-2d-91-37')
    @winrt_commethod(6)
    def UpdateCost(self, value: Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_commethod(7)
    def UpdateUsage(self, value: Windows.Networking.NetworkOperators.ProfileUsage) -> Void: ...
class IProvisioningAgent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('217700e0-8201-11df-ad-b9-f4-ce-46-2d-91-37')
    @winrt_commethod(6)
    def ProvisionFromXmlDocumentAsync(self, provisioningXmlDocument: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults]: ...
    @winrt_commethod(7)
    def GetProvisionedProfile(self, mediaType: Windows.Networking.NetworkOperators.ProfileMediaType, profileName: WinRT_String) -> Windows.Networking.NetworkOperators.ProvisionedProfile: ...
class IProvisioningAgentStaticMethods(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('217700e0-8101-11df-ad-b9-f4-ce-46-2d-91-37')
    @winrt_commethod(6)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.ProvisioningAgent: ...
class ITetheringEntitlementCheckTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('03c65e9d-5926-41f3-a9-4e-b5-09-26-fc-42-1b')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def AllowTethering(self) -> Void: ...
    @winrt_commethod(8)
    def DenyTethering(self, entitlementFailureReason: WinRT_String) -> Void: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class IUssdMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f9acf82-2004-4d5d-bf-81-2a-ba-1b-4b-e4-a8')
    @winrt_commethod(6)
    def get_DataCodingScheme(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataCodingScheme(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def GetPayload(self) -> c_char_p_no: ...
    @winrt_commethod(9)
    def SetPayload(self, value: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def get_PayloadAsText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_PayloadAsText(self, value: WinRT_String) -> Void: ...
    DataCodingScheme = property(get_DataCodingScheme, put_DataCodingScheme)
    PayloadAsText = property(get_PayloadAsText, put_PayloadAsText)
class IUssdMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f9acf82-1003-4d5d-bf-81-2a-ba-1b-4b-e4-a8')
    @winrt_commethod(6)
    def CreateMessage(self, messageText: WinRT_String) -> Windows.Networking.NetworkOperators.UssdMessage: ...
class IUssdReply(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f9acf82-2005-4d5d-bf-81-2a-ba-1b-4b-e4-a8')
    @winrt_commethod(6)
    def get_ResultCode(self) -> Windows.Networking.NetworkOperators.UssdResultCode: ...
    @winrt_commethod(7)
    def get_Message(self) -> Windows.Networking.NetworkOperators.UssdMessage: ...
    ResultCode = property(get_ResultCode, None)
    Message = property(get_Message, None)
class IUssdSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f9acf82-2002-4d5d-bf-81-2a-ba-1b-4b-e4-a8')
    @winrt_commethod(6)
    def SendMessageAndGetReplyAsync(self, message: Windows.Networking.NetworkOperators.UssdMessage) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.UssdReply]: ...
    @winrt_commethod(7)
    def Close(self) -> Void: ...
class IUssdSessionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f9acf82-1001-4d5d-bf-81-2a-ba-1b-4b-e4-a8')
    @winrt_commethod(6)
    def CreateFromNetworkAccountId(self, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.UssdSession: ...
    @winrt_commethod(7)
    def CreateFromNetworkInterfaceId(self, networkInterfaceId: WinRT_String) -> Windows.Networking.NetworkOperators.UssdSession: ...
class KnownCSimFilePaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownCSimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: Windows.Networking.NetworkOperators.IKnownCSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class KnownRuimFilePaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownRuimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: Windows.Networking.NetworkOperators.IKnownRuimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class KnownSimFilePaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownSimFilePaths'
    @winrt_classmethod
    def get_EFOns(cls: Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFSpn(cls: Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: Windows.Networking.NetworkOperators.IKnownSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFOns = property(get_EFOns, None)
    EFSpn = property(get_EFSpn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
class KnownUSimFilePaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.KnownUSimFilePaths'
    @winrt_classmethod
    def get_EFSpn(cls: Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFOpl(cls: Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_EFPnn(cls: Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid1(cls: Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_classmethod
    def get_Gid2(cls: Windows.Networking.NetworkOperators.IKnownUSimFilePathsStatics) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    EFSpn = property(get_EFSpn, None)
    EFOpl = property(get_EFOpl, None)
    EFPnn = property(get_EFPnn, None)
    Gid1 = property(get_Gid1, None)
    Gid2 = property(get_Gid2, None)
LegacyNetworkOperatorsContract: UInt32 = 65536
class MobileBroadbandAccount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccount'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceProviderGuid(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> Guid: ...
    @winrt_mixinmethod
    def get_ServiceProviderName(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentNetwork(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_mixinmethod
    def get_CurrentDeviceInformation(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_mixinmethod
    def GetConnectionProfiles(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount2) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.Connectivity.ConnectionProfile]: ...
    @winrt_mixinmethod
    def get_AccountExperienceUrl(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccount3) -> Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AvailableNetworkAccountIds(cls: Windows.Networking.NetworkOperators.IMobileBroadbandAccountStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: Windows.Networking.NetworkOperators.IMobileBroadbandAccountStatics, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
    AccountExperienceUrl = property(get_AccountExperienceUrl, None)
    AvailableNetworkAccountIds = property(get_AvailableNetworkAccountIds, None)
class MobileBroadbandAccountEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountEventArgs) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class MobileBroadbandAccountUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasDeviceInformationChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNetworkChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountUpdatedEventArgs) -> Boolean: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
    HasDeviceInformationChanged = property(get_HasDeviceInformationChanged, None)
    HasNetworkChanged = property(get_HasNetworkChanged, None)
class MobileBroadbandAccountWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher: ...
    @winrt_mixinmethod
    def add_AccountAdded(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountAdded(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountUpdated(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountUpdated(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountRemoved(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Networking.NetworkOperators.MobileBroadbandAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountRemoved(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher) -> Void: ...
    Status = property(get_Status, None)
MobileBroadbandAccountWatcherStatus = Int32
MobileBroadbandAccountWatcherStatus_Created: MobileBroadbandAccountWatcherStatus = 0
MobileBroadbandAccountWatcherStatus_Started: MobileBroadbandAccountWatcherStatus = 1
MobileBroadbandAccountWatcherStatus_EnumerationCompleted: MobileBroadbandAccountWatcherStatus = 2
MobileBroadbandAccountWatcherStatus_Stopped: MobileBroadbandAccountWatcherStatus = 3
MobileBroadbandAccountWatcherStatus_Aborted: MobileBroadbandAccountWatcherStatus = 4
class MobileBroadbandAntennaSar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar'
    @winrt_factorymethod
    def CreateWithIndex(cls: Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSarFactory, antennaIndex: Int32, sarBackoffIndex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar: ...
    @winrt_mixinmethod
    def get_AntennaIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar) -> Int32: ...
    @winrt_mixinmethod
    def get_SarBackoffIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar) -> Int32: ...
    AntennaIndex = property(get_AntennaIndex, None)
    SarBackoffIndex = property(get_SarBackoffIndex, None)
class MobileBroadbandCellCdma(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellCdma'
    @winrt_mixinmethod
    def get_BaseStationId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_BaseStationPNCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_BaseStationLatitude(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_BaseStationLongitude(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_BaseStationLastBroadcastGpsTime(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_NetworkId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PilotSignalStrengthInDB(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SystemId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellCdma) -> Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    NetworkId = property(get_NetworkId, None)
    PilotSignalStrengthInDB = property(get_PilotSignalStrengthInDB, None)
    SystemId = property(get_SystemId, None)
class MobileBroadbandCellGsm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellGsm'
    @winrt_mixinmethod
    def get_BaseStationId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_CellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalStrengthInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellGsm) -> Windows.Foundation.IReference[Int32]: ...
    BaseStationId = property(get_BaseStationId, None)
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalStrengthInDBm = property(get_ReceivedSignalStrengthInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class MobileBroadbandCellLte(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellLte'
    @winrt_mixinmethod
    def get_CellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PhysicalCellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedPowerInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedQualityInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_TrackingAreaCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellLte) -> Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    PhysicalCellId = property(get_PhysicalCellId, None)
    ProviderId = property(get_ProviderId, None)
    ReferenceSignalReceivedPowerInDBm = property(get_ReferenceSignalReceivedPowerInDBm, None)
    ReferenceSignalReceivedQualityInDBm = property(get_ReferenceSignalReceivedQualityInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
class MobileBroadbandCellNR(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellNR'
    @winrt_mixinmethod
    def get_CellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Int64]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PhysicalCellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedPowerInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ReferenceSignalReceivedQualityInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInNanoseconds(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_TrackingAreaCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_SignalToNoiseRatioInDB(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellNR) -> Windows.Foundation.IReference[Double]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma'
    @winrt_mixinmethod
    def get_CellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_CellParameterId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PathLossInDB(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalCodePowerInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimingAdvanceInBitPeriods(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellTdscdma) -> Windows.Foundation.IReference[Int32]: ...
    CellId = property(get_CellId, None)
    CellParameterId = property(get_CellParameterId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    TimingAdvanceInBitPeriods = property(get_TimingAdvanceInBitPeriods, None)
class MobileBroadbandCellUmts(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellUmts'
    @winrt_mixinmethod
    def get_CellId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ChannelNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_LocationAreaCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_PathLossInDB(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_PrimaryScramblingCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReceivedSignalCodePowerInDBm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_SignalToNoiseRatioInDB(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellUmts) -> Windows.Foundation.IReference[Double]: ...
    CellId = property(get_CellId, None)
    ChannelNumber = property(get_ChannelNumber, None)
    LocationAreaCode = property(get_LocationAreaCode, None)
    PathLossInDB = property(get_PathLossInDB, None)
    PrimaryScramblingCode = property(get_PrimaryScramblingCode, None)
    ProviderId = property(get_ProviderId, None)
    ReceivedSignalCodePowerInDBm = property(get_ReceivedSignalCodePowerInDBm, None)
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
class MobileBroadbandCellsInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo'
    @winrt_mixinmethod
    def get_NeighboringCellsCdma(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsGsm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsLte(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsTdscdma(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsUmts(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_mixinmethod
    def get_ServingCellsCdma(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellCdma]: ...
    @winrt_mixinmethod
    def get_ServingCellsGsm(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellGsm]: ...
    @winrt_mixinmethod
    def get_ServingCellsLte(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellLte]: ...
    @winrt_mixinmethod
    def get_ServingCellsTdscdma(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellTdscdma]: ...
    @winrt_mixinmethod
    def get_ServingCellsUmts(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellUmts]: ...
    @winrt_mixinmethod
    def get_NeighboringCellsNR(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
    @winrt_mixinmethod
    def get_ServingCellsNR(self: Windows.Networking.NetworkOperators.IMobileBroadbandCellsInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandCellNR]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs'
    @winrt_mixinmethod
    def get_CurrentSlotIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandCurrentSlotIndexChangedEventArgs) -> Int32: ...
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
class MobileBroadbandDeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation'
    @winrt_mixinmethod
    def get_NetworkDeviceStatus(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Networking.NetworkOperators.NetworkDeviceStatus: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Model(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirmwareInformation(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_DataClasses(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_mixinmethod
    def get_CustomDataClass(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MobileEquipmentId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TelephoneNumbers(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SubscriberId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceType(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentRadioState(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation) -> Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    @winrt_mixinmethod
    def get_PinManager(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> Windows.Networking.NetworkOperators.MobileBroadbandPinManager: ...
    @winrt_mixinmethod
    def get_Revision(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimSpn(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimPnn(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SimGid1(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SlotManager(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceInformation4) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotManager: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceService'
    @winrt_mixinmethod
    def get_DeviceServiceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> Guid: ...
    @winrt_mixinmethod
    def get_SupportedCommands(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def OpenDataSession(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession: ...
    @winrt_mixinmethod
    def OpenCommandSession(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceService) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    SupportedCommands = property(get_SupportedCommands, None)
class MobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult'
    @winrt_mixinmethod
    def get_StatusCode(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ResponseData(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> Windows.Storage.Streams.IBuffer: ...
    StatusCode = property(get_StatusCode, None)
    ResponseData = property(get_ResponseData, None)
class MobileBroadbandDeviceServiceCommandSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession'
    @winrt_mixinmethod
    def SendQueryCommandAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession, commandId: UInt32, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_mixinmethod
    def SendSetCommandAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession, commandId: UInt32, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult]: ...
    @winrt_mixinmethod
    def CloseSession(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession) -> Void: ...
class MobileBroadbandDeviceServiceDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_ReceivedData(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataReceivedEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    ReceivedData = property(get_ReceivedData, None)
class MobileBroadbandDeviceServiceDataSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession'
    @winrt_mixinmethod
    def WriteDataAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CloseSession(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession) -> Void: ...
    @winrt_mixinmethod
    def add_DataReceived(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataSession, Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataReceived(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceDataSession, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class MobileBroadbandDeviceServiceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation'
    @winrt_mixinmethod
    def get_DeviceServiceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_IsDataReadSupported(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDataWriteSupported(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceInformation) -> Boolean: ...
    DeviceServiceId = property(get_DeviceServiceId, None)
    IsDataReadSupported = property(get_IsDataReadSupported, None)
    IsDataWriteSupported = property(get_IsDataWriteSupported, None)
class MobileBroadbandDeviceServiceTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceServiceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_ReceivedData(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_EventId(self: Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceTriggerDetails2) -> UInt32: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModem'
    @winrt_mixinmethod
    def get_CurrentAccount(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Networking.NetworkOperators.MobileBroadbandAccount: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation: ...
    @winrt_mixinmethod
    def get_MaxDeviceServiceCommandSizeInBytes(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxDeviceServiceDataSizeInBytes(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> UInt32: ...
    @winrt_mixinmethod
    def get_DeviceServices(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceInformation]: ...
    @winrt_mixinmethod
    def GetDeviceService(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem, deviceServiceId: Guid) -> Windows.Networking.NetworkOperators.MobileBroadbandDeviceService: ...
    @winrt_mixinmethod
    def get_IsResetSupported(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Boolean: ...
    @winrt_mixinmethod
    def ResetAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetCurrentConfigurationAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration]: ...
    @winrt_mixinmethod
    def get_CurrentNetwork(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem2, value: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def TryGetPcoAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem3) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPco]: ...
    @winrt_mixinmethod
    def get_IsInEmergencyCallMode(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem3) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsInEmergencyCallModeChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem3, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandModem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsInEmergencyCallModeChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledWithSlotIndexAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem4, value: Boolean, slotindex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledWithSlotIndexAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem4, slotindex: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetIsPassthroughEnabledWithSlotIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem4, value: Boolean, slotindex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_mixinmethod
    def GetIsPassthroughEnabledWithSlotIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandModem4, slotindex: Int32) -> Boolean: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics, deviceId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Networking.NetworkOperators.IMobileBroadbandModemStatics) -> Windows.Networking.NetworkOperators.MobileBroadbandModem: ...
    CurrentAccount = property(get_CurrentAccount, None)
    DeviceInformation = property(get_DeviceInformation, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
    DeviceServices = property(get_DeviceServices, None)
    IsResetSupported = property(get_IsResetSupported, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    IsInEmergencyCallMode = property(get_IsInEmergencyCallMode, None)
class MobileBroadbandModemConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModemConfiguration'
    @winrt_mixinmethod
    def get_Uicc(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> Windows.Networking.NetworkOperators.MobileBroadbandUicc: ...
    @winrt_mixinmethod
    def get_HomeProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HomeProviderName(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SarManager(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemConfiguration2) -> Windows.Networking.NetworkOperators.MobileBroadbandSarManager: ...
    Uicc = property(get_Uicc, None)
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
    SarManager = property(get_SarManager, None)
class MobileBroadbandModemIsolation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolationFactory, modemDeviceId: WinRT_String, ruleGroupId: WinRT_String) -> Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation: ...
    @winrt_mixinmethod
    def AddAllowedHost(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation, host: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def AddAllowedHostRange(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation, first: Windows.Networking.HostName, last: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def ApplyConfigurationAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearConfigurationAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation) -> Windows.Foundation.IAsyncAction: ...
MobileBroadbandModemStatus = Int32
MobileBroadbandModemStatus_Success: MobileBroadbandModemStatus = 0
MobileBroadbandModemStatus_OtherFailure: MobileBroadbandModemStatus = 1
MobileBroadbandModemStatus_Busy: MobileBroadbandModemStatus = 2
MobileBroadbandModemStatus_NoDeviceSupport: MobileBroadbandModemStatus = 3
class MobileBroadbandNetwork(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetwork'
    @winrt_mixinmethod
    def get_NetworkAdapter(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> Windows.Networking.Connectivity.NetworkAdapter: ...
    @winrt_mixinmethod
    def get_NetworkRegistrationState(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> Windows.Networking.NetworkOperators.NetworkRegistrationState: ...
    @winrt_mixinmethod
    def get_RegistrationNetworkError(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_PacketAttachNetworkError(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_ActivationNetworkError(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> UInt32: ...
    @winrt_mixinmethod
    def get_AccessPointName(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegisteredDataClass(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> Windows.Networking.NetworkOperators.DataClasses: ...
    @winrt_mixinmethod
    def get_RegisteredProviderId(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegisteredProviderName(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> WinRT_String: ...
    @winrt_mixinmethod
    def ShowConnectionUI(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork) -> Void: ...
    @winrt_mixinmethod
    def GetVoiceCallSupportAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_RegistrationUiccApps(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork2) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
    @winrt_mixinmethod
    def GetCellsInfoAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetwork3) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandCellsInfo]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Network(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChange) -> Windows.Networking.NetworkOperators.MobileBroadbandNetwork: ...
    DeviceId = property(get_DeviceId, None)
    Network = property(get_Network, None)
class MobileBroadbandNetworkRegistrationStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_NetworkRegistrationStateChanges(self: Windows.Networking.NetworkOperators.IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandNetworkRegistrationStateChange]: ...
    NetworkRegistrationStateChanges = property(get_NetworkRegistrationStateChanges, None)
class MobileBroadbandPco(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPco'
    @winrt_mixinmethod
    def get_Data(self: Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandPco) -> WinRT_String: ...
    Data = property(get_Data, None)
    IsComplete = property(get_IsComplete, None)
    DeviceId = property(get_DeviceId, None)
class MobileBroadbandPcoDataChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPcoDataChangeTriggerDetails'
    @winrt_mixinmethod
    def get_UpdatedData(self: Windows.Networking.NetworkOperators.IMobileBroadbandPcoDataChangeTriggerDetails) -> Windows.Networking.NetworkOperators.MobileBroadbandPco: ...
    UpdatedData = property(get_UpdatedData, None)
class MobileBroadbandPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPin'
    @winrt_mixinmethod
    def get_Type(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_mixinmethod
    def get_LockState(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> Windows.Networking.NetworkOperators.MobileBroadbandPinFormat: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxLength(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinLength(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def get_AttemptsRemaining(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin) -> UInt32: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def EnterAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def ChangeAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin, currentPin: WinRT_String, newPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
    @winrt_mixinmethod
    def UnblockAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandPin, pinUnblockKey: WinRT_String, newPin: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PinType(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> Windows.Networking.NetworkOperators.MobileBroadbandPinType: ...
    @winrt_mixinmethod
    def get_PinLockState(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChange) -> Windows.Networking.NetworkOperators.MobileBroadbandPinLockState: ...
    DeviceId = property(get_DeviceId, None)
    PinType = property(get_PinType, None)
    PinLockState = property(get_PinLockState, None)
class MobileBroadbandPinLockStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_PinLockStateChanges(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinLockStateChangeTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandPinLockStateChange]: ...
    PinLockStateChanges = property(get_PinLockStateChanges, None)
class MobileBroadbandPinManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinManager'
    @winrt_mixinmethod
    def get_SupportedPins(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinManager) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandPinType]: ...
    @winrt_mixinmethod
    def GetPin(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinManager, pinType: Windows.Networking.NetworkOperators.MobileBroadbandPinType) -> Windows.Networking.NetworkOperators.MobileBroadbandPin: ...
    SupportedPins = property(get_SupportedPins, None)
class MobileBroadbandPinOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandPinOperationResult'
    @winrt_mixinmethod
    def get_IsSuccessful(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_AttemptsRemaining(self: Windows.Networking.NetworkOperators.IMobileBroadbandPinOperationResult) -> UInt32: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RadioState(self: Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChange) -> Windows.Networking.NetworkOperators.MobileBroadbandRadioState: ...
    DeviceId = property(get_DeviceId, None)
    RadioState = property(get_RadioState, None)
class MobileBroadbandRadioStateChangeTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChangeTriggerDetails'
    @winrt_mixinmethod
    def get_RadioStateChanges(self: Windows.Networking.NetworkOperators.IMobileBroadbandRadioStateChangeTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandRadioStateChange]: ...
    RadioStateChanges = property(get_RadioStateChanges, None)
class MobileBroadbandSarManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSarManager'
    @winrt_mixinmethod
    def get_IsBackoffEnabled(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsWiFiHardwareIntegrated(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSarControlledByHardware(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_Antennas(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]: ...
    @winrt_mixinmethod
    def get_HysteresisTimerPeriod(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_TransmissionStateChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSarManager, Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransmissionStateChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def EnableBackoffAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DisableBackoffAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetConfigurationAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, antennas: Windows.Foundation.Collections.IIterable[Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RevertSarToHardwareControlAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetTransmissionStateChangedHysteresisAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager, timerPeriod: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetIsTransmittingAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def StartTransmissionStateMonitoring(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Void: ...
    @winrt_mixinmethod
    def StopTransmissionStateMonitoring(self: Windows.Networking.NetworkOperators.IMobileBroadbandSarManager) -> Void: ...
    IsBackoffEnabled = property(get_IsBackoffEnabled, None)
    IsWiFiHardwareIntegrated = property(get_IsWiFiHardwareIntegrated, None)
    IsSarControlledByHardware = property(get_IsSarControlledByHardware, None)
    Antennas = property(get_Antennas, None)
    HysteresisTimerPeriod = property(get_HysteresisTimerPeriod, None)
class MobileBroadbandSlotInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo'
    @winrt_mixinmethod
    def get_Index(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotState: ...
    @winrt_mixinmethod
    def get_IccId(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfo2) -> WinRT_String: ...
    Index = property(get_Index, None)
    State = property(get_State, None)
    IccId = property(get_IccId, None)
class MobileBroadbandSlotInfoChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs'
    @winrt_mixinmethod
    def get_SlotInfo(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotInfoChangedEventArgs) -> Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo: ...
    SlotInfo = property(get_SlotInfo, None)
class MobileBroadbandSlotManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandSlotManager'
    @winrt_mixinmethod
    def get_SlotInfos(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandSlotInfo]: ...
    @winrt_mixinmethod
    def get_CurrentSlotIndex(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager) -> Int32: ...
    @winrt_mixinmethod
    def SetCurrentSlot(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, slotIndex: Int32) -> Windows.Networking.NetworkOperators.MobileBroadbandModemStatus: ...
    @winrt_mixinmethod
    def SetCurrentSlotAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, slotIndex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]: ...
    @winrt_mixinmethod
    def add_SlotInfoChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, Windows.Networking.NetworkOperators.MobileBroadbandSlotInfoChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SlotInfoChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentSlotIndexChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.NetworkOperators.MobileBroadbandSlotManager, Windows.Networking.NetworkOperators.MobileBroadbandCurrentSlotIndexChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentSlotIndexChanged(self: Windows.Networking.NetworkOperators.IMobileBroadbandSlotManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandTransmissionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_IsTransmitting(self: Windows.Networking.NetworkOperators.IMobileBroadbandTransmissionStateChangedEventArgs) -> Boolean: ...
    IsTransmitting = property(get_IsTransmitting, None)
class MobileBroadbandUicc(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUicc'
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Networking.NetworkOperators.IMobileBroadbandUicc) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetUiccAppsAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandUicc) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult]: ...
    SimIccId = property(get_SimIccId, None)
class MobileBroadbandUiccApp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccApp'
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp) -> Windows.Networking.NetworkOperators.UiccAppKind: ...
    @winrt_mixinmethod
    def GetRecordDetailsAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp, uiccFilePath: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult]: ...
    @winrt_mixinmethod
    def ReadRecordAsync(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccApp, uiccFilePath: Windows.Foundation.Collections.IIterable[UInt32], recordIndex: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
MobileBroadbandUiccAppOperationStatus = Int32
MobileBroadbandUiccAppOperationStatus_Success: MobileBroadbandUiccAppOperationStatus = 0
MobileBroadbandUiccAppOperationStatus_InvalidUiccFilePath: MobileBroadbandUiccAppOperationStatus = 1
MobileBroadbandUiccAppOperationStatus_AccessConditionNotHeld: MobileBroadbandUiccAppOperationStatus = 2
MobileBroadbandUiccAppOperationStatus_UiccBusy: MobileBroadbandUiccAppOperationStatus = 3
class MobileBroadbandUiccAppReadRecordResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Data = property(get_Data, None)
class MobileBroadbandUiccAppRecordDetailsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppRecordDetailsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Windows.Networking.NetworkOperators.UiccAppRecordKind: ...
    @winrt_mixinmethod
    def get_RecordCount(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Int32: ...
    @winrt_mixinmethod
    def get_RecordSize(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Int32: ...
    @winrt_mixinmethod
    def get_ReadAccessCondition(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    @winrt_mixinmethod
    def get_WriteAccessCondition(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppRecordDetailsResult) -> Windows.Networking.NetworkOperators.UiccAccessCondition: ...
    Status = property(get_Status, None)
    Kind = property(get_Kind, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    WriteAccessCondition = property(get_WriteAccessCondition, None)
class MobileBroadbandUiccAppsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult) -> Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_UiccApps(self: Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.MobileBroadbandUiccApp]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorDataUsageTriggerDetails'
    @winrt_mixinmethod
    def get_NotificationKind(self: Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails) -> Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails'
    @winrt_mixinmethod
    def get_NotificationType(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EncodingType(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> Byte: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RuleId(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SmsMessage(self: Windows.Networking.NetworkOperators.INetworkOperatorNotificationEventDetails) -> Windows.Devices.Sms.ISmsMessage: ...
    @winrt_mixinmethod
    def AuthorizeTethering(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringEntitlementCheck, allow: Boolean, entitlementFailureReason: WinRT_String) -> Void: ...
    NotificationType = property(get_NotificationType, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    RuleId = property(get_RuleId, None)
    SmsMessage = property(get_SmsMessage, None)
class NetworkOperatorTetheringAccessPointConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_mixinmethod
    def get_Ssid(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Passphrase(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Passphrase(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IsBandSupported(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, band: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_mixinmethod
    def IsBandSupportedAsync(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, band: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Band(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2) -> Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_mixinmethod
    def put_Band(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration2, value: Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
    Band = property(get_Band, put_Band)
class NetworkOperatorTetheringClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient'
    @winrt_mixinmethod
    def get_MacAddress(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HostNames(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    MacAddress = property(get_MacAddress, None)
    HostNames = property(get_HostNames, None)
class NetworkOperatorTetheringManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager'
    @winrt_mixinmethod
    def get_MaxClientCount(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> UInt32: ...
    @winrt_mixinmethod
    def get_ClientCount(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> UInt32: ...
    @winrt_mixinmethod
    def get_TetheringOperationalState(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> Windows.Networking.NetworkOperators.TetheringOperationalState: ...
    @winrt_mixinmethod
    def GetCurrentAccessPointConfiguration(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration: ...
    @winrt_mixinmethod
    def ConfigureAccessPointAsync(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager, configuration: Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartTetheringAsync(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def StopTetheringAsync(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def GetTetheringClients(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringClientManager) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient]: ...
    @winrt_classmethod
    def IsNoConnectionsTimeoutEnabled(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Boolean: ...
    @winrt_classmethod
    def EnableNoConnectionsTimeout(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Void: ...
    @winrt_classmethod
    def EnableNoConnectionsTimeoutAsync(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def DisableNoConnectionsTimeout(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Void: ...
    @winrt_classmethod
    def DisableNoConnectionsTimeoutAsync(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics4) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateFromConnectionProfileWithTargetAdapter(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics3, profile: Windows.Networking.Connectivity.ConnectionProfile, adapter: Windows.Networking.Connectivity.NetworkAdapter) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    @winrt_classmethod
    def GetTetheringCapabilityFromConnectionProfile(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics2, profile: Windows.Networking.Connectivity.ConnectionProfile) -> Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_classmethod
    def CreateFromConnectionProfile(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics2, profile: Windows.Networking.Connectivity.ConnectionProfile) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    @winrt_classmethod
    def GetTetheringCapability(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.TetheringCapability: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: Windows.Networking.NetworkOperators.INetworkOperatorTetheringManagerStatics, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager: ...
    MaxClientCount = property(get_MaxClientCount, None)
    ClientCount = property(get_ClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class NetworkOperatorTetheringOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> Windows.Networking.NetworkOperators.TetheringOperationStatus: ...
    @winrt_mixinmethod
    def get_AdditionalErrorMessage(self: Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> WinRT_String: ...
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
    LastSyncTime: Windows.Foundation.DateTime
class ProvisionFromXmlDocumentResults(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults'
    @winrt_mixinmethod
    def get_AllElementsProvisioned(self: Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults) -> Boolean: ...
    @winrt_mixinmethod
    def get_ProvisionResultsXml(self: Windows.Networking.NetworkOperators.IProvisionFromXmlDocumentResults) -> WinRT_String: ...
    AllElementsProvisioned = property(get_AllElementsProvisioned, None)
    ProvisionResultsXml = property(get_ProvisionResultsXml, None)
class ProvisionedProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisionedProfile'
    @winrt_mixinmethod
    def UpdateCost(self: Windows.Networking.NetworkOperators.IProvisionedProfile, value: Windows.Networking.Connectivity.NetworkCostType) -> Void: ...
    @winrt_mixinmethod
    def UpdateUsage(self: Windows.Networking.NetworkOperators.IProvisionedProfile, value: Windows.Networking.NetworkOperators.ProfileUsage) -> Void: ...
class ProvisioningAgent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.ProvisioningAgent'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.NetworkOperators.ProvisioningAgent: ...
    @winrt_mixinmethod
    def ProvisionFromXmlDocumentAsync(self: Windows.Networking.NetworkOperators.IProvisioningAgent, provisioningXmlDocument: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults]: ...
    @winrt_mixinmethod
    def GetProvisionedProfile(self: Windows.Networking.NetworkOperators.IProvisioningAgent, mediaType: Windows.Networking.NetworkOperators.ProfileMediaType, profileName: WinRT_String) -> Windows.Networking.NetworkOperators.ProvisionedProfile: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: Windows.Networking.NetworkOperators.IProvisioningAgentStaticMethods, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.ProvisioningAgent: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.TetheringEntitlementCheckTriggerDetails'
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def AllowTethering(self: Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails) -> Void: ...
    @winrt_mixinmethod
    def DenyTethering(self: Windows.Networking.NetworkOperators.ITetheringEntitlementCheckTriggerDetails, entitlementFailureReason: WinRT_String) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.UssdMessage'
    @winrt_factorymethod
    def CreateMessage(cls: Windows.Networking.NetworkOperators.IUssdMessageFactory, messageText: WinRT_String) -> Windows.Networking.NetworkOperators.UssdMessage: ...
    @winrt_mixinmethod
    def get_DataCodingScheme(self: Windows.Networking.NetworkOperators.IUssdMessage) -> Byte: ...
    @winrt_mixinmethod
    def put_DataCodingScheme(self: Windows.Networking.NetworkOperators.IUssdMessage, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def GetPayload(self: Windows.Networking.NetworkOperators.IUssdMessage) -> c_char_p_no: ...
    @winrt_mixinmethod
    def SetPayload(self: Windows.Networking.NetworkOperators.IUssdMessage, value: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_PayloadAsText(self: Windows.Networking.NetworkOperators.IUssdMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayloadAsText(self: Windows.Networking.NetworkOperators.IUssdMessage, value: WinRT_String) -> Void: ...
    DataCodingScheme = property(get_DataCodingScheme, put_DataCodingScheme)
    PayloadAsText = property(get_PayloadAsText, put_PayloadAsText)
class UssdReply(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.UssdReply'
    @winrt_mixinmethod
    def get_ResultCode(self: Windows.Networking.NetworkOperators.IUssdReply) -> Windows.Networking.NetworkOperators.UssdResultCode: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Networking.NetworkOperators.IUssdReply) -> Windows.Networking.NetworkOperators.UssdMessage: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.UssdSession'
    @winrt_mixinmethod
    def SendMessageAndGetReplyAsync(self: Windows.Networking.NetworkOperators.IUssdSession, message: Windows.Networking.NetworkOperators.UssdMessage) -> Windows.Foundation.IAsyncOperation[Windows.Networking.NetworkOperators.UssdReply]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Networking.NetworkOperators.IUssdSession) -> Void: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: Windows.Networking.NetworkOperators.IUssdSessionStatics, networkAccountId: WinRT_String) -> Windows.Networking.NetworkOperators.UssdSession: ...
    @winrt_classmethod
    def CreateFromNetworkInterfaceId(cls: Windows.Networking.NetworkOperators.IUssdSessionStatics, networkInterfaceId: WinRT_String) -> Windows.Networking.NetworkOperators.UssdSession: ...
make_head(_module, 'ESim')
make_head(_module, 'ESimAddedEventArgs')
make_head(_module, 'ESimDiscoverEvent')
make_head(_module, 'ESimDiscoverResult')
make_head(_module, 'ESimDownloadProfileMetadataResult')
make_head(_module, 'ESimManager')
make_head(_module, 'ESimOperationResult')
make_head(_module, 'ESimPolicy')
make_head(_module, 'ESimProfile')
make_head(_module, 'ESimProfileInstallProgress')
make_head(_module, 'ESimProfileMetadata')
make_head(_module, 'ESimProfilePolicy')
make_head(_module, 'ESimRemovedEventArgs')
make_head(_module, 'ESimServiceInfo')
make_head(_module, 'ESimUpdatedEventArgs')
make_head(_module, 'ESimWatcher')
make_head(_module, 'FdnAccessManager')
make_head(_module, 'HotspotAuthenticationContext')
make_head(_module, 'HotspotAuthenticationEventDetails')
make_head(_module, 'HotspotCredentialsAuthenticationResult')
make_head(_module, 'IESim')
make_head(_module, 'IESim2')
make_head(_module, 'IESim3')
make_head(_module, 'IESimAddedEventArgs')
make_head(_module, 'IESimDiscoverEvent')
make_head(_module, 'IESimDiscoverResult')
make_head(_module, 'IESimDownloadProfileMetadataResult')
make_head(_module, 'IESimManagerStatics')
make_head(_module, 'IESimOperationResult')
make_head(_module, 'IESimPolicy')
make_head(_module, 'IESimProfile')
make_head(_module, 'IESimProfileMetadata')
make_head(_module, 'IESimProfilePolicy')
make_head(_module, 'IESimRemovedEventArgs')
make_head(_module, 'IESimServiceInfo')
make_head(_module, 'IESimUpdatedEventArgs')
make_head(_module, 'IESimWatcher')
make_head(_module, 'IFdnAccessManagerStatics')
make_head(_module, 'IHotspotAuthenticationContext')
make_head(_module, 'IHotspotAuthenticationContext2')
make_head(_module, 'IHotspotAuthenticationContextStatics')
make_head(_module, 'IHotspotAuthenticationEventDetails')
make_head(_module, 'IHotspotCredentialsAuthenticationResult')
make_head(_module, 'IKnownCSimFilePathsStatics')
make_head(_module, 'IKnownRuimFilePathsStatics')
make_head(_module, 'IKnownSimFilePathsStatics')
make_head(_module, 'IKnownUSimFilePathsStatics')
make_head(_module, 'IMobileBroadbandAccount')
make_head(_module, 'IMobileBroadbandAccount2')
make_head(_module, 'IMobileBroadbandAccount3')
make_head(_module, 'IMobileBroadbandAccountEventArgs')
make_head(_module, 'IMobileBroadbandAccountStatics')
make_head(_module, 'IMobileBroadbandAccountUpdatedEventArgs')
make_head(_module, 'IMobileBroadbandAccountWatcher')
make_head(_module, 'IMobileBroadbandAntennaSar')
make_head(_module, 'IMobileBroadbandAntennaSarFactory')
make_head(_module, 'IMobileBroadbandCellCdma')
make_head(_module, 'IMobileBroadbandCellGsm')
make_head(_module, 'IMobileBroadbandCellLte')
make_head(_module, 'IMobileBroadbandCellNR')
make_head(_module, 'IMobileBroadbandCellTdscdma')
make_head(_module, 'IMobileBroadbandCellUmts')
make_head(_module, 'IMobileBroadbandCellsInfo')
make_head(_module, 'IMobileBroadbandCellsInfo2')
make_head(_module, 'IMobileBroadbandCurrentSlotIndexChangedEventArgs')
make_head(_module, 'IMobileBroadbandDeviceInformation')
make_head(_module, 'IMobileBroadbandDeviceInformation2')
make_head(_module, 'IMobileBroadbandDeviceInformation3')
make_head(_module, 'IMobileBroadbandDeviceInformation4')
make_head(_module, 'IMobileBroadbandDeviceService')
make_head(_module, 'IMobileBroadbandDeviceServiceCommandResult')
make_head(_module, 'IMobileBroadbandDeviceServiceCommandSession')
make_head(_module, 'IMobileBroadbandDeviceServiceDataReceivedEventArgs')
make_head(_module, 'IMobileBroadbandDeviceServiceDataSession')
make_head(_module, 'IMobileBroadbandDeviceServiceInformation')
make_head(_module, 'IMobileBroadbandDeviceServiceTriggerDetails')
make_head(_module, 'IMobileBroadbandDeviceServiceTriggerDetails2')
make_head(_module, 'IMobileBroadbandModem')
make_head(_module, 'IMobileBroadbandModem2')
make_head(_module, 'IMobileBroadbandModem3')
make_head(_module, 'IMobileBroadbandModem4')
make_head(_module, 'IMobileBroadbandModemConfiguration')
make_head(_module, 'IMobileBroadbandModemConfiguration2')
make_head(_module, 'IMobileBroadbandModemIsolation')
make_head(_module, 'IMobileBroadbandModemIsolationFactory')
make_head(_module, 'IMobileBroadbandModemStatics')
make_head(_module, 'IMobileBroadbandNetwork')
make_head(_module, 'IMobileBroadbandNetwork2')
make_head(_module, 'IMobileBroadbandNetwork3')
make_head(_module, 'IMobileBroadbandNetworkRegistrationStateChange')
make_head(_module, 'IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails')
make_head(_module, 'IMobileBroadbandPco')
make_head(_module, 'IMobileBroadbandPcoDataChangeTriggerDetails')
make_head(_module, 'IMobileBroadbandPin')
make_head(_module, 'IMobileBroadbandPinLockStateChange')
make_head(_module, 'IMobileBroadbandPinLockStateChangeTriggerDetails')
make_head(_module, 'IMobileBroadbandPinManager')
make_head(_module, 'IMobileBroadbandPinOperationResult')
make_head(_module, 'IMobileBroadbandRadioStateChange')
make_head(_module, 'IMobileBroadbandRadioStateChangeTriggerDetails')
make_head(_module, 'IMobileBroadbandSarManager')
make_head(_module, 'IMobileBroadbandSlotInfo')
make_head(_module, 'IMobileBroadbandSlotInfo2')
make_head(_module, 'IMobileBroadbandSlotInfoChangedEventArgs')
make_head(_module, 'IMobileBroadbandSlotManager')
make_head(_module, 'IMobileBroadbandTransmissionStateChangedEventArgs')
make_head(_module, 'IMobileBroadbandUicc')
make_head(_module, 'IMobileBroadbandUiccApp')
make_head(_module, 'IMobileBroadbandUiccAppReadRecordResult')
make_head(_module, 'IMobileBroadbandUiccAppRecordDetailsResult')
make_head(_module, 'IMobileBroadbandUiccAppsResult')
make_head(_module, 'INetworkOperatorDataUsageTriggerDetails')
make_head(_module, 'INetworkOperatorNotificationEventDetails')
make_head(_module, 'INetworkOperatorTetheringAccessPointConfiguration')
make_head(_module, 'INetworkOperatorTetheringAccessPointConfiguration2')
make_head(_module, 'INetworkOperatorTetheringClient')
make_head(_module, 'INetworkOperatorTetheringClientManager')
make_head(_module, 'INetworkOperatorTetheringEntitlementCheck')
make_head(_module, 'INetworkOperatorTetheringManager')
make_head(_module, 'INetworkOperatorTetheringManagerStatics')
make_head(_module, 'INetworkOperatorTetheringManagerStatics2')
make_head(_module, 'INetworkOperatorTetheringManagerStatics3')
make_head(_module, 'INetworkOperatorTetheringManagerStatics4')
make_head(_module, 'INetworkOperatorTetheringOperationResult')
make_head(_module, 'IProvisionFromXmlDocumentResults')
make_head(_module, 'IProvisionedProfile')
make_head(_module, 'IProvisioningAgent')
make_head(_module, 'IProvisioningAgentStaticMethods')
make_head(_module, 'ITetheringEntitlementCheckTriggerDetails')
make_head(_module, 'IUssdMessage')
make_head(_module, 'IUssdMessageFactory')
make_head(_module, 'IUssdReply')
make_head(_module, 'IUssdSession')
make_head(_module, 'IUssdSessionStatics')
make_head(_module, 'KnownCSimFilePaths')
make_head(_module, 'KnownRuimFilePaths')
make_head(_module, 'KnownSimFilePaths')
make_head(_module, 'KnownUSimFilePaths')
make_head(_module, 'MobileBroadbandAccount')
make_head(_module, 'MobileBroadbandAccountEventArgs')
make_head(_module, 'MobileBroadbandAccountUpdatedEventArgs')
make_head(_module, 'MobileBroadbandAccountWatcher')
make_head(_module, 'MobileBroadbandAntennaSar')
make_head(_module, 'MobileBroadbandCellCdma')
make_head(_module, 'MobileBroadbandCellGsm')
make_head(_module, 'MobileBroadbandCellLte')
make_head(_module, 'MobileBroadbandCellNR')
make_head(_module, 'MobileBroadbandCellTdscdma')
make_head(_module, 'MobileBroadbandCellUmts')
make_head(_module, 'MobileBroadbandCellsInfo')
make_head(_module, 'MobileBroadbandCurrentSlotIndexChangedEventArgs')
make_head(_module, 'MobileBroadbandDeviceInformation')
make_head(_module, 'MobileBroadbandDeviceService')
make_head(_module, 'MobileBroadbandDeviceServiceCommandResult')
make_head(_module, 'MobileBroadbandDeviceServiceCommandSession')
make_head(_module, 'MobileBroadbandDeviceServiceDataReceivedEventArgs')
make_head(_module, 'MobileBroadbandDeviceServiceDataSession')
make_head(_module, 'MobileBroadbandDeviceServiceInformation')
make_head(_module, 'MobileBroadbandDeviceServiceTriggerDetails')
make_head(_module, 'MobileBroadbandModem')
make_head(_module, 'MobileBroadbandModemConfiguration')
make_head(_module, 'MobileBroadbandModemIsolation')
make_head(_module, 'MobileBroadbandNetwork')
make_head(_module, 'MobileBroadbandNetworkRegistrationStateChange')
make_head(_module, 'MobileBroadbandNetworkRegistrationStateChangeTriggerDetails')
make_head(_module, 'MobileBroadbandPco')
make_head(_module, 'MobileBroadbandPcoDataChangeTriggerDetails')
make_head(_module, 'MobileBroadbandPin')
make_head(_module, 'MobileBroadbandPinLockStateChange')
make_head(_module, 'MobileBroadbandPinLockStateChangeTriggerDetails')
make_head(_module, 'MobileBroadbandPinManager')
make_head(_module, 'MobileBroadbandPinOperationResult')
make_head(_module, 'MobileBroadbandRadioStateChange')
make_head(_module, 'MobileBroadbandRadioStateChangeTriggerDetails')
make_head(_module, 'MobileBroadbandSarManager')
make_head(_module, 'MobileBroadbandSlotInfo')
make_head(_module, 'MobileBroadbandSlotInfoChangedEventArgs')
make_head(_module, 'MobileBroadbandSlotManager')
make_head(_module, 'MobileBroadbandTransmissionStateChangedEventArgs')
make_head(_module, 'MobileBroadbandUicc')
make_head(_module, 'MobileBroadbandUiccApp')
make_head(_module, 'MobileBroadbandUiccAppReadRecordResult')
make_head(_module, 'MobileBroadbandUiccAppRecordDetailsResult')
make_head(_module, 'MobileBroadbandUiccAppsResult')
make_head(_module, 'NetworkOperatorDataUsageTriggerDetails')
make_head(_module, 'NetworkOperatorNotificationEventDetails')
make_head(_module, 'NetworkOperatorTetheringAccessPointConfiguration')
make_head(_module, 'NetworkOperatorTetheringClient')
make_head(_module, 'NetworkOperatorTetheringManager')
make_head(_module, 'NetworkOperatorTetheringOperationResult')
make_head(_module, 'ProfileUsage')
make_head(_module, 'ProvisionFromXmlDocumentResults')
make_head(_module, 'ProvisionedProfile')
make_head(_module, 'ProvisioningAgent')
make_head(_module, 'TetheringEntitlementCheckTriggerDetails')
make_head(_module, 'UssdMessage')
make_head(_module, 'UssdReply')
make_head(_module, 'UssdSession')
