from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Devices.Sms
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Connectivity
import win32more.Windows.Networking.NetworkOperators
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class DataClasses(Enum, UInt32):
    None_ = 0
    Gprs = 1
    Edge = 2
    Umts = 4
    Hsdpa = 8
    Hsupa = 16
    LteAdvanced = 32
    NewRadioNonStandalone = 64
    NewRadioStandalone = 128
    Cdma1xRtt = 65536
    Cdma1xEvdo = 131072
    Cdma1xEvdoRevA = 262144
    Cdma1xEvdv = 524288
    Cdma3xRtt = 1048576
    Cdma1xEvdoRevB = 2097152
    CdmaUmb = 4194304
    Custom = 2147483648
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
    SlotIndex = property(get_SlotIndex, None)
    State = property(get_State, None)
    ProfileChanged = event()
class ESimAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimAddedEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.ESimAddedEventArgs'
    @winrt_mixinmethod
    def get_ESim(self: win32more.Windows.Networking.NetworkOperators.IESimAddedEventArgs) -> win32more.Windows.Networking.NetworkOperators.ESim: ...
    ESim = property(get_ESim, None)
class ESimAuthenticationPreference(Enum, Int32):
    OnEntry = 0
    OnAction = 1
    Never = 2
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
class ESimDiscoverResultKind(Enum, Int32):
    None_ = 0
    Events = 1
    ProfileMetadata = 2
class ESimDownloadProfileMetadataResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult
    _classid_ = 'Windows.Networking.NetworkOperators.ESimDownloadProfileMetadataResult'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> win32more.Windows.Networking.NetworkOperators.ESimOperationResult: ...
    @winrt_mixinmethod
    def get_ProfileMetadata(self: win32more.Windows.Networking.NetworkOperators.IESimDownloadProfileMetadataResult) -> win32more.Windows.Networking.NetworkOperators.ESimProfileMetadata: ...
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
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
    _ESimManager_Meta_.ServiceInfo = property(get_ServiceInfo, None)
class ESimOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IESimOperationResult
    _classid_ = 'Windows.Networking.NetworkOperators.ESimOperationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IESimOperationResult) -> win32more.Windows.Networking.NetworkOperators.ESimOperationStatus: ...
    Status = property(get_Status, None)
class ESimOperationStatus(Enum, Int32):
    Success = 0
    NotAuthorized = 1
    NotFound = 2
    PolicyViolation = 3
    InsufficientSpaceOnCard = 4
    ServerFailure = 5
    ServerNotReachable = 6
    TimeoutWaitingForUserConsent = 7
    IncorrectConfirmationCode = 8
    ConfirmationCodeMaxRetriesExceeded = 9
    CardRemoved = 10
    CardBusy = 11
    Other = 12
    CardGeneralFailure = 13
    ConfirmationCodeMissing = 14
    InvalidMatchingId = 15
    NoEligibleProfileForThisDevice = 16
    OperationAborted = 17
    EidMismatch = 18
    ProfileNotAvailableForNewBinding = 19
    ProfileNotReleasedByOperator = 20
    OperationProhibitedByProfileClass = 21
    ProfileNotPresent = 22
    NoCorrespondingRequest = 23
    TimeoutWaitingForResponse = 24
    IccidAlreadyExists = 25
    ProfileProcessingError = 26
    ServerNotTrusted = 27
    ProfileDownloadMaxRetriesExceeded = 28
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
    Id = property(get_Id, None)
    Nickname = property(get_Nickname, None)
    Policy = property(get_Policy, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
class ESimProfileClass(Enum, Int32):
    Operational = 0
    Test = 1
    Provisioning = 2
class ESimProfileInstallProgress(Structure):
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
    Id = property(get_Id, None)
    IsConfirmationCodeRequired = property(get_IsConfirmationCodeRequired, None)
    Policy = property(get_Policy, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
    StateChanged = event()
class ESimProfileMetadataState(Enum, Int32):
    Unknown = 0
    WaitingForInstall = 1
    Downloading = 2
    Installing = 3
    Expired = 4
    RejectingDownload = 5
    NoLongerAvailable = 6
    DeniedByPolicy = 7
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
class ESimProfileState(Enum, Int32):
    Unknown = 0
    Disabled = 1
    Enabled = 2
    Deleted = 3
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
class ESimState(Enum, Int32):
    Unknown = 0
    Idle = 1
    Removed = 2
    Busy = 3
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
    Added = event()
    EnumerationCompleted = event()
    Removed = event()
    Stopped = event()
    Updated = event()
class ESimWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
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
    def get_WirelessNetworkId(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationContext) -> ReceiveArray[Byte]: ...
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
    AuthenticationUrl = property(get_AuthenticationUrl, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    RedirectMessageUrl = property(get_RedirectMessageUrl, None)
    RedirectMessageXml = property(get_RedirectMessageXml, None)
    WirelessNetworkId = property(get_WirelessNetworkId, None)
class HotspotAuthenticationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails
    _classid_ = 'Windows.Networking.NetworkOperators.HotspotAuthenticationEventDetails'
    @winrt_mixinmethod
    def get_EventToken(self: win32more.Windows.Networking.NetworkOperators.IHotspotAuthenticationEventDetails) -> WinRT_String: ...
    EventToken = property(get_EventToken, None)
class HotspotAuthenticationResponseCode(Enum, Int32):
    NoError = 0
    LoginSucceeded = 50
    LoginFailed = 100
    RadiusServerError = 102
    NetworkAdministratorError = 105
    LoginAborted = 151
    AccessGatewayInternalError = 255
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
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    LogoffUrl = property(get_LogoffUrl, None)
    ResponseCode = property(get_ResponseCode, None)
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
    ProfileChanged = event()
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
    ProfileMetadata = property(get_ProfileMetadata, None)
    Result = property(get_Result, None)
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
    ServiceInfoChanged = event()
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
    Id = property(get_Id, None)
    Nickname = property(get_Nickname, None)
    Policy = property(get_Policy, None)
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
    Id = property(get_Id, None)
    IsConfirmationCodeRequired = property(get_IsConfirmationCodeRequired, None)
    Policy = property(get_Policy, None)
    ProviderIcon = property(get_ProviderIcon, None)
    ProviderId = property(get_ProviderId, None)
    ProviderName = property(get_ProviderName, None)
    State = property(get_State, None)
    StateChanged = event()
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
    Added = event()
    EnumerationCompleted = event()
    Removed = event()
    Stopped = event()
    Updated = event()
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
    def get_WirelessNetworkId(self) -> ReceiveArray[Byte]: ...
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
    AuthenticationUrl = property(get_AuthenticationUrl, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    RedirectMessageUrl = property(get_RedirectMessageUrl, None)
    RedirectMessageXml = property(get_RedirectMessageXml, None)
    WirelessNetworkId = property(get_WirelessNetworkId, None)
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
    AuthenticationReplyXml = property(get_AuthenticationReplyXml, None)
    HasNetworkErrorOccurred = property(get_HasNetworkErrorOccurred, None)
    LogoffUrl = property(get_LogoffUrl, None)
    ResponseCode = property(get_ResponseCode, None)
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
    EFOpl = property(get_EFOpl, None)
    EFPnn = property(get_EFPnn, None)
    EFSpn = property(get_EFSpn, None)
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
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
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
    HasDeviceInformationChanged = property(get_HasDeviceInformationChanged, None)
    HasNetworkChanged = property(get_HasNetworkChanged, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
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
    AccountAdded = event()
    AccountUpdated = event()
    AccountRemoved = event()
    EnumerationCompleted = event()
    Stopped = event()
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
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
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
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
    TimingAdvanceInNanoseconds = property(get_TimingAdvanceInNanoseconds, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
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
    CellularClass = property(get_CellularClass, None)
    CurrentRadioState = property(get_CurrentRadioState, None)
    CustomDataClass = property(get_CustomDataClass, None)
    DataClasses = property(get_DataClasses, None)
    DeviceId = property(get_DeviceId, None)
    DeviceType = property(get_DeviceType, None)
    FirmwareInformation = property(get_FirmwareInformation, None)
    Manufacturer = property(get_Manufacturer, None)
    MobileEquipmentId = property(get_MobileEquipmentId, None)
    Model = property(get_Model, None)
    NetworkDeviceStatus = property(get_NetworkDeviceStatus, None)
    SimIccId = property(get_SimIccId, None)
    SubscriberId = property(get_SubscriberId, None)
    TelephoneNumbers = property(get_TelephoneNumbers, None)
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
    SimGid1 = property(get_SimGid1, None)
    SimPnn = property(get_SimPnn, None)
    SimSpn = property(get_SimSpn, None)
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
class IMobileBroadbandDeviceServiceCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs'
    _iid_ = Guid('{28e4338f-cca4-5047-a20c-0a6d79acecba}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceServiceId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_EventId(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ReceivedData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeviceId = property(get_DeviceId, None)
    DeviceServiceId = property(get_DeviceServiceId, None)
    EventId = property(get_EventId, None)
    ReceivedData = property(get_ReceivedData, None)
class IMobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult'
    _iid_ = Guid('{b0f46abb-94d6-44b9-a538-f0810b645389}')
    @winrt_commethod(6)
    def get_StatusCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ResponseData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ResponseData = property(get_ResponseData, None)
    StatusCode = property(get_StatusCode, None)
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
class IMobileBroadbandDeviceServiceCommandSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession2'
    _iid_ = Guid('{ef004861-2546-5739-86e7-0fdc0e62411c}')
    @winrt_commethod(6)
    def add_CommandReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession, win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CommandReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CommandReceived = event()
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
    DataReceived = event()
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
    CurrentNetwork = property(get_CurrentNetwork, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceServices = property(get_DeviceServices, None)
    IsResetSupported = property(get_IsResetSupported, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
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
    IsInEmergencyCallModeChanged = event()
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
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
    Uicc = property(get_Uicc, None)
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
    AccessPointName = property(get_AccessPointName, None)
    ActivationNetworkError = property(get_ActivationNetworkError, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkRegistrationState = property(get_NetworkRegistrationState, None)
    PacketAttachNetworkError = property(get_PacketAttachNetworkError, None)
    RegisteredDataClass = property(get_RegisteredDataClass, None)
    RegisteredProviderId = property(get_RegisteredProviderId, None)
    RegisteredProviderName = property(get_RegisteredProviderName, None)
    RegistrationNetworkError = property(get_RegistrationNetworkError, None)
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
    DeviceId = property(get_DeviceId, None)
    IsComplete = property(get_IsComplete, None)
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
    AttemptsRemaining = property(get_AttemptsRemaining, None)
    Enabled = property(get_Enabled, None)
    Format = property(get_Format, None)
    LockState = property(get_LockState, None)
    MaxLength = property(get_MaxLength, None)
    MinLength = property(get_MinLength, None)
    Type = property(get_Type, None)
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
    PinLockState = property(get_PinLockState, None)
    PinType = property(get_PinType, None)
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
    AttemptsRemaining = property(get_AttemptsRemaining, None)
    IsSuccessful = property(get_IsSuccessful, None)
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
    Antennas = property(get_Antennas, None)
    HysteresisTimerPeriod = property(get_HysteresisTimerPeriod, None)
    IsBackoffEnabled = property(get_IsBackoffEnabled, None)
    IsSarControlledByHardware = property(get_IsSarControlledByHardware, None)
    IsWiFiHardwareIntegrated = property(get_IsWiFiHardwareIntegrated, None)
    TransmissionStateChanged = event()
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
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
    SlotInfos = property(get_SlotInfos, None)
    SlotInfoChanged = event()
    CurrentSlotIndexChanged = event()
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
    Data = property(get_Data, None)
    Status = property(get_Status, None)
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
    Kind = property(get_Kind, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    Status = property(get_Status, None)
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
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    NotificationType = property(get_NotificationType, None)
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
    Passphrase = property(get_Passphrase, put_Passphrase)
    Ssid = property(get_Ssid, put_Ssid)
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
class INetworkOperatorTetheringAccessPointConfiguration3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration3'
    _iid_ = Guid('{a9bb0081-9eed-5d18-b676-24b74a182b8c}')
    @winrt_commethod(6)
    def IsAuthenticationKindSupported(self, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Boolean: ...
    @winrt_commethod(7)
    def IsAuthenticationKindSupportedAsync(self, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_AuthenticationKind(self) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind: ...
    @winrt_commethod(9)
    def put_AuthenticationKind(self, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Void: ...
    AuthenticationKind = property(get_AuthenticationKind, put_AuthenticationKind)
class INetworkOperatorTetheringClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient'
    _iid_ = Guid('{709d254c-595f-4847-bb30-646935542918}')
    @winrt_commethod(6)
    def get_MacAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HostNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    HostNames = property(get_HostNames, None)
    MacAddress = property(get_MacAddress, None)
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
    ClientCount = property(get_ClientCount, None)
    MaxClientCount = property(get_MaxClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class INetworkOperatorTetheringManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager2'
    _iid_ = Guid('{7c1a4df2-b789-4fea-bc4e-1f2b9e76c1f7}')
    @winrt_commethod(6)
    def StartTetheringAsync(self, configuration: win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringSessionAccessPointConfiguration) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
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
    AdditionalErrorMessage = property(get_AdditionalErrorMessage, None)
    Status = property(get_Status, None)
class INetworkOperatorTetheringSessionAccessPointConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration'
    _iid_ = Guid('{0bcc1104-34b7-5212-858c-59d97404920a}')
    @winrt_commethod(6)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Passphrase(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Passphrase(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def IsBandSupported(self, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_commethod(11)
    def IsBandSupportedAsync(self, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def get_Band(self) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_commethod(13)
    def put_Band(self, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    @winrt_commethod(14)
    def IsAuthenticationKindSupported(self, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Boolean: ...
    @winrt_commethod(15)
    def IsAuthenticationKindSupportedAsync(self, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def get_AuthenticationKind(self) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind: ...
    @winrt_commethod(17)
    def put_AuthenticationKind(self, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Void: ...
    @winrt_commethod(18)
    def get_PerformancePriority(self) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiPerformancePriority: ...
    @winrt_commethod(19)
    def put_PerformancePriority(self, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiPerformancePriority) -> Void: ...
    AuthenticationKind = property(get_AuthenticationKind, put_AuthenticationKind)
    Band = property(get_Band, put_Band)
    Passphrase = property(get_Passphrase, put_Passphrase)
    PerformancePriority = property(get_PerformancePriority, put_PerformancePriority)
    Ssid = property(get_Ssid, put_Ssid)
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
    def GetPayload(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(9)
    def SetPayload(self, value: PassArray[Byte]) -> Void: ...
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
    Message = property(get_Message, None)
    ResultCode = property(get_ResultCode, None)
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
    _KnownCSimFilePaths_Meta_.EFSpn = property(get_EFSpn, None)
    _KnownCSimFilePaths_Meta_.Gid1 = property(get_Gid1, None)
    _KnownCSimFilePaths_Meta_.Gid2 = property(get_Gid2, None)
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
    _KnownRuimFilePaths_Meta_.EFSpn = property(get_EFSpn, None)
    _KnownRuimFilePaths_Meta_.Gid1 = property(get_Gid1, None)
    _KnownRuimFilePaths_Meta_.Gid2 = property(get_Gid2, None)
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
    _KnownSimFilePaths_Meta_.EFOns = property(get_EFOns, None)
    _KnownSimFilePaths_Meta_.EFSpn = property(get_EFSpn, None)
    _KnownSimFilePaths_Meta_.Gid1 = property(get_Gid1, None)
    _KnownSimFilePaths_Meta_.Gid2 = property(get_Gid2, None)
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
    _KnownUSimFilePaths_Meta_.EFOpl = property(get_EFOpl, None)
    _KnownUSimFilePaths_Meta_.EFPnn = property(get_EFPnn, None)
    _KnownUSimFilePaths_Meta_.EFSpn = property(get_EFSpn, None)
    _KnownUSimFilePaths_Meta_.Gid1 = property(get_Gid1, None)
    _KnownUSimFilePaths_Meta_.Gid2 = property(get_Gid2, None)
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
    AccountExperienceUrl = property(get_AccountExperienceUrl, None)
    CurrentDeviceInformation = property(get_CurrentDeviceInformation, None)
    CurrentNetwork = property(get_CurrentNetwork, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    ServiceProviderGuid = property(get_ServiceProviderGuid, None)
    ServiceProviderName = property(get_ServiceProviderName, None)
    _MobileBroadbandAccount_Meta_.AvailableNetworkAccountIds = property(get_AvailableNetworkAccountIds, None)
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
    HasDeviceInformationChanged = property(get_HasDeviceInformationChanged, None)
    HasNetworkChanged = property(get_HasNetworkChanged, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
class MobileBroadbandAccountWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAccountWatcher
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcher.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    AccountAdded = event()
    AccountUpdated = event()
    AccountRemoved = event()
    EnumerationCompleted = event()
    Stopped = event()
class MobileBroadbandAccountWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopped = 3
    Aborted = 4
class MobileBroadbandAntennaSar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandAntennaSar
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.MobileBroadbandAntennaSar.CreateWithIndex(*args))
        else:
            raise ValueError('no matched constructor')
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
    BaseStationLastBroadcastGpsTime = property(get_BaseStationLastBroadcastGpsTime, None)
    BaseStationLatitude = property(get_BaseStationLatitude, None)
    BaseStationLongitude = property(get_BaseStationLongitude, None)
    BaseStationPNCode = property(get_BaseStationPNCode, None)
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
    SignalToNoiseRatioInDB = property(get_SignalToNoiseRatioInDB, None)
    TimingAdvanceInNanoseconds = property(get_TimingAdvanceInNanoseconds, None)
    TrackingAreaCode = property(get_TrackingAreaCode, None)
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
    NeighboringCellsNR = property(get_NeighboringCellsNR, None)
    NeighboringCellsTdscdma = property(get_NeighboringCellsTdscdma, None)
    NeighboringCellsUmts = property(get_NeighboringCellsUmts, None)
    ServingCellsCdma = property(get_ServingCellsCdma, None)
    ServingCellsGsm = property(get_ServingCellsGsm, None)
    ServingCellsLte = property(get_ServingCellsLte, None)
    ServingCellsNR = property(get_ServingCellsNR, None)
    ServingCellsTdscdma = property(get_ServingCellsTdscdma, None)
    ServingCellsUmts = property(get_ServingCellsUmts, None)
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
    CellularClass = property(get_CellularClass, None)
    CurrentRadioState = property(get_CurrentRadioState, None)
    CustomDataClass = property(get_CustomDataClass, None)
    DataClasses = property(get_DataClasses, None)
    DeviceId = property(get_DeviceId, None)
    DeviceType = property(get_DeviceType, None)
    FirmwareInformation = property(get_FirmwareInformation, None)
    Manufacturer = property(get_Manufacturer, None)
    MobileEquipmentId = property(get_MobileEquipmentId, None)
    Model = property(get_Model, None)
    NetworkDeviceStatus = property(get_NetworkDeviceStatus, None)
    PinManager = property(get_PinManager, None)
    Revision = property(get_Revision, None)
    SerialNumber = property(get_SerialNumber, None)
    SimGid1 = property(get_SimGid1, None)
    SimIccId = property(get_SimIccId, None)
    SimPnn = property(get_SimPnn, None)
    SimSpn = property(get_SimSpn, None)
    SlotManager = property(get_SlotManager, None)
    SubscriberId = property(get_SubscriberId, None)
    TelephoneNumbers = property(get_TelephoneNumbers, None)
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
class MobileBroadbandDeviceServiceCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandEventArgs'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceServiceId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_EventId(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReceivedData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    DeviceId = property(get_DeviceId, None)
    DeviceServiceId = property(get_DeviceServiceId, None)
    EventId = property(get_EventId, None)
    ReceivedData = property(get_ReceivedData, None)
class MobileBroadbandDeviceServiceCommandResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandResult'
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ResponseData = property(get_ResponseData, None)
    StatusCode = property(get_StatusCode, None)
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
    @winrt_mixinmethod
    def add_CommandReceived(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandSession, win32more.Windows.Networking.NetworkOperators.MobileBroadbandDeviceServiceCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandReceived(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandDeviceServiceCommandSession2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CommandReceived = event()
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
    DataReceived = event()
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
    EventId = property(get_EventId, None)
    ReceivedData = property(get_ReceivedData, None)
class MobileBroadbandDeviceType(Enum, Int32):
    Unknown = 0
    Embedded = 1
    Removable = 2
    Remote = 3
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
    CurrentNetwork = property(get_CurrentNetwork, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceServices = property(get_DeviceServices, None)
    IsInEmergencyCallMode = property(get_IsInEmergencyCallMode, None)
    IsResetSupported = property(get_IsResetSupported, None)
    MaxDeviceServiceCommandSizeInBytes = property(get_MaxDeviceServiceCommandSizeInBytes, None)
    MaxDeviceServiceDataSizeInBytes = property(get_MaxDeviceServiceDataSizeInBytes, None)
    IsInEmergencyCallModeChanged = event()
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
    HomeProviderId = property(get_HomeProviderId, None)
    HomeProviderName = property(get_HomeProviderName, None)
    SarManager = property(get_SarManager, None)
    Uicc = property(get_Uicc, None)
class MobileBroadbandModemIsolation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandModemIsolation
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.MobileBroadbandModemIsolation.Create(*args))
        else:
            raise ValueError('no matched constructor')
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
class MobileBroadbandModemStatus(Enum, Int32):
    Success = 0
    OtherFailure = 1
    Busy = 2
    NoDeviceSupport = 3
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
    AccessPointName = property(get_AccessPointName, None)
    ActivationNetworkError = property(get_ActivationNetworkError, None)
    NetworkAdapter = property(get_NetworkAdapter, None)
    NetworkRegistrationState = property(get_NetworkRegistrationState, None)
    PacketAttachNetworkError = property(get_PacketAttachNetworkError, None)
    RegisteredDataClass = property(get_RegisteredDataClass, None)
    RegisteredProviderId = property(get_RegisteredProviderId, None)
    RegisteredProviderName = property(get_RegisteredProviderName, None)
    RegistrationNetworkError = property(get_RegistrationNetworkError, None)
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
    DeviceId = property(get_DeviceId, None)
    IsComplete = property(get_IsComplete, None)
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
    AttemptsRemaining = property(get_AttemptsRemaining, None)
    Enabled = property(get_Enabled, None)
    Format = property(get_Format, None)
    LockState = property(get_LockState, None)
    MaxLength = property(get_MaxLength, None)
    MinLength = property(get_MinLength, None)
    Type = property(get_Type, None)
class MobileBroadbandPinFormat(Enum, Int32):
    Unknown = 0
    Numeric = 1
    Alphanumeric = 2
class MobileBroadbandPinLockState(Enum, Int32):
    Unknown = 0
    Unlocked = 1
    PinRequired = 2
    PinUnblockKeyRequired = 3
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
    PinLockState = property(get_PinLockState, None)
    PinType = property(get_PinType, None)
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
    AttemptsRemaining = property(get_AttemptsRemaining, None)
    IsSuccessful = property(get_IsSuccessful, None)
class MobileBroadbandPinType(Enum, Int32):
    None_ = 0
    Custom = 1
    Pin1 = 2
    Pin2 = 3
    SimPin = 4
    FirstSimPin = 5
    NetworkPin = 6
    NetworkSubsetPin = 7
    ServiceProviderPin = 8
    CorporatePin = 9
    SubsidyLock = 10
class MobileBroadbandRadioState(Enum, Int32):
    Off = 0
    On = 1
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
    Antennas = property(get_Antennas, None)
    HysteresisTimerPeriod = property(get_HysteresisTimerPeriod, None)
    IsBackoffEnabled = property(get_IsBackoffEnabled, None)
    IsSarControlledByHardware = property(get_IsSarControlledByHardware, None)
    IsWiFiHardwareIntegrated = property(get_IsWiFiHardwareIntegrated, None)
    TransmissionStateChanged = event()
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
    IccId = property(get_IccId, None)
    Index = property(get_Index, None)
    State = property(get_State, None)
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
    CurrentSlotIndex = property(get_CurrentSlotIndex, None)
    SlotInfos = property(get_SlotInfos, None)
    SlotInfoChanged = event()
    CurrentSlotIndexChanged = event()
class MobileBroadbandSlotState(Enum, Int32):
    Unmanaged = 0
    Unknown = 1
    OffEmpty = 2
    Off = 3
    Empty = 4
    NotReady = 5
    Active = 6
    Error = 7
    ActiveEsim = 8
    ActiveEsimNoProfile = 9
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
class MobileBroadbandUiccAppOperationStatus(Enum, Int32):
    Success = 0
    InvalidUiccFilePath = 1
    AccessConditionNotHeld = 2
    UiccBusy = 3
class MobileBroadbandUiccAppReadRecordResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult
    _classid_ = 'Windows.Networking.NetworkOperators.MobileBroadbandUiccAppReadRecordResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> win32more.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Networking.NetworkOperators.IMobileBroadbandUiccAppReadRecordResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
    Status = property(get_Status, None)
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
    Kind = property(get_Kind, None)
    ReadAccessCondition = property(get_ReadAccessCondition, None)
    RecordCount = property(get_RecordCount, None)
    RecordSize = property(get_RecordSize, None)
    Status = property(get_Status, None)
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
class NetworkDeviceStatus(Enum, Int32):
    DeviceNotReady = 0
    DeviceReady = 1
    SimNotInserted = 2
    BadSim = 3
    DeviceHardwareFailure = 4
    AccountNotActivated = 5
    DeviceLocked = 6
    DeviceBlocked = 7
class NetworkOperatorDataUsageNotificationKind(Enum, Int32):
    DataUsageProgress = 0
class NetworkOperatorDataUsageTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorDataUsageTriggerDetails'
    @winrt_mixinmethod
    def get_NotificationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorDataUsageTriggerDetails) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind: ...
    NotificationKind = property(get_NotificationKind, None)
class NetworkOperatorEventMessageType(Enum, Int32):
    Gsm = 0
    Cdma = 1
    Ussd = 2
    DataPlanThresholdReached = 3
    DataPlanReset = 4
    DataPlanDeleted = 5
    ProfileConnected = 6
    ProfileDisconnected = 7
    RegisteredRoaming = 8
    RegisteredHome = 9
    TetheringEntitlementCheck = 10
    TetheringOperationalStateChanged = 11
    TetheringNumberOfClientsChanged = 12
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
    EncodingType = property(get_EncodingType, None)
    Message = property(get_Message, None)
    NetworkAccountId = property(get_NetworkAccountId, None)
    NotificationType = property(get_NotificationType, None)
    RuleId = property(get_RuleId, None)
    SmsMessage = property(get_SmsMessage, None)
class NetworkOperatorTetheringAccessPointConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringAccessPointConfiguration.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    @winrt_mixinmethod
    def IsAuthenticationKindSupported(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration3, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Boolean: ...
    @winrt_mixinmethod
    def IsAuthenticationKindSupportedAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration3, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AuthenticationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration3) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind: ...
    @winrt_mixinmethod
    def put_AuthenticationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringAccessPointConfiguration3, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Void: ...
    AuthenticationKind = property(get_AuthenticationKind, put_AuthenticationKind)
    Band = property(get_Band, put_Band)
    Passphrase = property(get_Passphrase, put_Passphrase)
    Ssid = property(get_Ssid, put_Ssid)
class NetworkOperatorTetheringClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient'
    @winrt_mixinmethod
    def get_MacAddress(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HostNames(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClient) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    HostNames = property(get_HostNames, None)
    MacAddress = property(get_MacAddress, None)
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
    @winrt_overload
    @winrt_mixinmethod
    def StartTetheringAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def StopTetheringAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
    @winrt_mixinmethod
    def GetTetheringClients(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringClientManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringClient]: ...
    @StartTetheringAsync.register
    @winrt_mixinmethod
    def StartTetheringAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringManager2, configuration: win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringSessionAccessPointConfiguration) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult]: ...
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
    ClientCount = property(get_ClientCount, None)
    MaxClientCount = property(get_MaxClientCount, None)
    TetheringOperationalState = property(get_TetheringOperationalState, None)
class NetworkOperatorTetheringOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> win32more.Windows.Networking.NetworkOperators.TetheringOperationStatus: ...
    @winrt_mixinmethod
    def get_AdditionalErrorMessage(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringOperationResult) -> WinRT_String: ...
    AdditionalErrorMessage = property(get_AdditionalErrorMessage, None)
    Status = property(get_Status, None)
class NetworkOperatorTetheringSessionAccessPointConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration
    _classid_ = 'Windows.Networking.NetworkOperators.NetworkOperatorTetheringSessionAccessPointConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringSessionAccessPointConfiguration.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.NetworkOperators.NetworkOperatorTetheringSessionAccessPointConfiguration: ...
    @winrt_mixinmethod
    def get_Ssid(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Passphrase(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Passphrase(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IsBandSupported(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Boolean: ...
    @winrt_mixinmethod
    def IsBandSupportedAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, band: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Band(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand: ...
    @winrt_mixinmethod
    def put_Band(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiBand) -> Void: ...
    @winrt_mixinmethod
    def IsAuthenticationKindSupported(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Boolean: ...
    @winrt_mixinmethod
    def IsAuthenticationKindSupportedAsync(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, authenticationKind: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AuthenticationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind: ...
    @winrt_mixinmethod
    def put_AuthenticationKind(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiAuthenticationKind) -> Void: ...
    @winrt_mixinmethod
    def get_PerformancePriority(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration) -> win32more.Windows.Networking.NetworkOperators.TetheringWiFiPerformancePriority: ...
    @winrt_mixinmethod
    def put_PerformancePriority(self: win32more.Windows.Networking.NetworkOperators.INetworkOperatorTetheringSessionAccessPointConfiguration, value: win32more.Windows.Networking.NetworkOperators.TetheringWiFiPerformancePriority) -> Void: ...
    AuthenticationKind = property(get_AuthenticationKind, put_AuthenticationKind)
    Band = property(get_Band, put_Band)
    Passphrase = property(get_Passphrase, put_Passphrase)
    PerformancePriority = property(get_PerformancePriority, put_PerformancePriority)
    Ssid = property(get_Ssid, put_Ssid)
NetworkOperatorsFdnContract: UInt32 = 65536
class NetworkRegistrationState(Enum, Int32):
    None_ = 0
    Deregistered = 1
    Searching = 2
    Home = 3
    Roaming = 4
    Partner = 5
    Denied = 6
class ProfileMediaType(Enum, Int32):
    Wlan = 0
    Wwan = 1
class ProfileUsage(Structure):
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.ProvisioningAgent.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.NetworkOperators.ProvisioningAgent: ...
    @winrt_mixinmethod
    def ProvisionFromXmlDocumentAsync(self: win32more.Windows.Networking.NetworkOperators.IProvisioningAgent, provisioningXmlDocument: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults]: ...
    @winrt_mixinmethod
    def GetProvisionedProfile(self: win32more.Windows.Networking.NetworkOperators.IProvisioningAgent, mediaType: win32more.Windows.Networking.NetworkOperators.ProfileMediaType, profileName: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisionedProfile: ...
    @winrt_classmethod
    def CreateFromNetworkAccountId(cls: win32more.Windows.Networking.NetworkOperators.IProvisioningAgentStaticMethods, networkAccountId: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.ProvisioningAgent: ...
class TetheringCapability(Enum, Int32):
    Enabled = 0
    DisabledByGroupPolicy = 1
    DisabledByHardwareLimitation = 2
    DisabledByOperator = 3
    DisabledBySku = 4
    DisabledByRequiredAppNotInstalled = 5
    DisabledDueToUnknownCause = 6
    DisabledBySystemCapability = 7
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
class TetheringOperationStatus(Enum, Int32):
    Success = 0
    Unknown = 1
    MobileBroadbandDeviceOff = 2
    WiFiDeviceOff = 3
    EntitlementCheckTimeout = 4
    EntitlementCheckFailure = 5
    OperationInProgress = 6
    BluetoothDeviceOff = 7
    NetworkLimitedConnectivity = 8
    AlreadyOn = 9
    RadioRestriction = 10
    BandInterference = 11
class TetheringOperationalState(Enum, Int32):
    Unknown = 0
    On = 1
    Off = 2
    InTransition = 3
class TetheringWiFiAuthenticationKind(Enum, Int32):
    Wpa2 = 0
    Wpa3TransitionMode = 1
    Wpa3 = 2
class TetheringWiFiBand(Enum, Int32):
    Auto = 0
    TwoPointFourGigahertz = 1
    FiveGigahertz = 2
    SixGigahertz = 3
class TetheringWiFiPerformancePriority(Enum, Int32):
    Default = 0
    TetheringOverStation = 1
class UiccAccessCondition(Enum, Int32):
    AlwaysAllowed = 0
    Pin1 = 1
    Pin2 = 2
    Pin3 = 3
    Pin4 = 4
    Administrative5 = 5
    Administrative6 = 6
    NeverAllowed = 7
class UiccAppKind(Enum, Int32):
    Unknown = 0
    MF = 1
    MFSim = 2
    MFRuim = 3
    USim = 4
    CSim = 5
    ISim = 6
class UiccAppRecordKind(Enum, Int32):
    Unknown = 0
    Transparent = 1
    RecordOriented = 2
class UssdMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.NetworkOperators.IUssdMessage
    _classid_ = 'Windows.Networking.NetworkOperators.UssdMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.NetworkOperators.UssdMessage.CreateMessage(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateMessage(cls: win32more.Windows.Networking.NetworkOperators.IUssdMessageFactory, messageText: WinRT_String) -> win32more.Windows.Networking.NetworkOperators.UssdMessage: ...
    @winrt_mixinmethod
    def get_DataCodingScheme(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage) -> Byte: ...
    @winrt_mixinmethod
    def put_DataCodingScheme(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def GetPayload(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def SetPayload(self: win32more.Windows.Networking.NetworkOperators.IUssdMessage, value: PassArray[Byte]) -> Void: ...
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
    Message = property(get_Message, None)
    ResultCode = property(get_ResultCode, None)
class UssdResultCode(Enum, Int32):
    NoActionRequired = 0
    ActionRequired = 1
    Terminated = 2
    OtherLocalClient = 3
    OperationNotSupported = 4
    NetworkTimeout = 5
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
