from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.ConversationalAgent
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Audio
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ActivationSignalDetectionConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration'
    @winrt_mixinmethod
    def get_SignalId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def SetEnabled(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetEnabledAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, value: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_AvailabilityInfo(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration, win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetModelData(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def SetModelDataAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetModelDataType(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetModelDataTypeAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetModelData(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetModelDataAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IInputStream]: ...
    @winrt_mixinmethod
    def ClearModelData(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Void: ...
    @winrt_mixinmethod
    def ClearModelDataAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TrainingStepsCompleted(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrainingStepsRemaining(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrainingDataFormat(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat: ...
    @winrt_mixinmethod
    def ApplyTrainingData(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, trainingDataFormat: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus: ...
    @winrt_mixinmethod
    def ApplyTrainingDataAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, trainingDataFormat: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]: ...
    @winrt_mixinmethod
    def ClearTrainingData(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Void: ...
    @winrt_mixinmethod
    def ClearTrainingDataAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def SetModelDataWithResult(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult: ...
    @winrt_mixinmethod
    def SetModelDataWithResultAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]: ...
    @winrt_mixinmethod
    def SetEnabledWithResultAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, value: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]: ...
    @winrt_mixinmethod
    def SetEnabledWithResult(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, value: Boolean) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult: ...
    @winrt_mixinmethod
    def get_TrainingStepCompletionMaxAllowedTime(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2) -> UInt32: ...
    AvailabilityInfo = property(get_AvailabilityInfo, None)
    DisplayName = property(get_DisplayName, None)
    IsActive = property(get_IsActive, None)
    ModelId = property(get_ModelId, None)
    SignalId = property(get_SignalId, None)
    TrainingDataFormat = property(get_TrainingDataFormat, None)
    TrainingStepCompletionMaxAllowedTime = property(get_TrainingStepCompletionMaxAllowedTime, None)
    TrainingStepsCompleted = property(get_TrainingStepsCompleted, None)
    TrainingStepsRemaining = property(get_TrainingStepsRemaining, None)
    AvailabilityChanged = event()
class ActivationSignalDetectionConfigurationCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationStatus: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    Configuration = property(get_Configuration, None)
    Status = property(get_Status, None)
class ActivationSignalDetectionConfigurationCreationStatus(Enum, Int32):
    Success = 0
    SignalIdNotAvailable = 1
    ModelIdNotSupported = 2
    InvalidSignalId = 3
    InvalidModelId = 4
    InvalidDisplayName = 5
    ConfigurationAlreadyExists = 6
    CreationNotSupported = 7
class ActivationSignalDetectionConfigurationRemovalResult(Enum, Int32):
    Success = 0
    NotFound = 1
    CurrentlyEnabled = 2
    RemovalNotSupported = 3
class ActivationSignalDetectionConfigurationSetModelDataResult(Enum, Int32):
    Success = 0
    EmptyModelData = 1
    UnsupportedFormat = 2
    ConfigurationCurrentlyEnabled = 3
    InvalidData = 4
    SetModelDataNotSupported = 5
    ConfigurationNotFound = 6
    UnknownError = 7
class ActivationSignalDetectionConfigurationStateChangeResult(Enum, Int32):
    Success = 0
    NoModelData = 1
    ConfigurationNotFound = 2
class ActivationSignalDetectionTrainingDataFormat(Enum, Int32):
    Voice8kHz8BitMono = 0
    Voice8kHz16BitMono = 1
    Voice16kHz8BitMono = 2
    Voice16kHz16BitMono = 3
    VoiceOEMDefined = 4
    Audio44kHz8BitMono = 5
    Audio44kHz16BitMono = 6
    Audio48kHz8BitMono = 7
    Audio48kHz16BitMono = 8
    AudioOEMDefined = 9
    OtherOEMDefined = 10
class ActivationSignalDetector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    @winrt_mixinmethod
    def get_CanCreateConfigurations(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModelDataTypes(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SupportedTrainingDataFormats(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]: ...
    @winrt_mixinmethod
    def get_SupportedPowerStates(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorPowerState]: ...
    @winrt_mixinmethod
    def GetSupportedModelIdsForSignalId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetSupportedModelIdsForSignalIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def CreateConfiguration(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def CreateConfigurationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetConfigurations(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_mixinmethod
    def GetConfigurationsAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]]: ...
    @winrt_mixinmethod
    def GetConfiguration(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    @winrt_mixinmethod
    def GetConfigurationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_mixinmethod
    def RemoveConfiguration(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveConfigurationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetAvailableModelIdsForSignalIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetAvailableModelIdsForSignalId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def CreateConfigurationWithResultAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult]: ...
    @winrt_mixinmethod
    def CreateConfigurationWithResult(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult: ...
    @winrt_mixinmethod
    def RemoveConfigurationWithResultAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]: ...
    @winrt_mixinmethod
    def RemoveConfigurationWithResult(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult: ...
    @winrt_mixinmethod
    def get_DetectorId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2) -> WinRT_String: ...
    CanCreateConfigurations = property(get_CanCreateConfigurations, None)
    DetectorId = property(get_DetectorId, None)
    Kind = property(get_Kind, None)
    ProviderId = property(get_ProviderId, None)
    SupportedModelDataTypes = property(get_SupportedModelDataTypes, None)
    SupportedPowerStates = property(get_SupportedPowerStates, None)
    SupportedTrainingDataFormats = property(get_SupportedTrainingDataFormats, None)
class ActivationSignalDetectorKind(Enum, Int32):
    AudioPattern = 0
    AudioImpulse = 1
    HardwareEvent = 2
class ActivationSignalDetectorPowerState(Enum, Int32):
    HighPower = 0
    ConnectedLowPower = 1
    DisconnectedLowPower = 2
class ConversationalAgentActivationKind(Enum, Int32):
    VoiceActivationPreview = 0
    Foreground = 1
class ConversationalAgentActivationResult(Enum, Int32):
    Success = 0
    AgentInactive = 1
    ScreenNotAvailable = 2
    AgentInterrupted = 3
class _ConversationalAgentDetectorManager_Meta_(ComPtr.__class__):
    pass
class ConversationalAgentDetectorManager(ComPtr, metaclass=_ConversationalAgentDetectorManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager'
    @winrt_mixinmethod
    def GetAllActivationSignalDetectors(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_mixinmethod
    def GetAllActivationSignalDetectorsAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectors(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager, kind: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorsAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager, kind: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorFromId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2, detectorId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorFromIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2, detectorId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_classmethod
    def get_Default(cls: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManagerStatics) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager: ...
    _ConversationalAgentDetectorManager_Meta_.Default = property(get_Default, None)
class ConversationalAgentSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession'
    @winrt_mixinmethod
    def add_SessionInterrupted(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionInterrupted(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SignalDetected(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SignalDetected(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemStateChanged(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemStateChanged(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AgentState(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState: ...
    @winrt_mixinmethod
    def get_Signal(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal: ...
    @winrt_mixinmethod
    def get_IsIndicatorLightAvailable(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScreenAvailable(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserAuthenticated(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVoiceActivationAvailable(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInterruptible(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInterrupted(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def RequestInterruptibleAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, interruptible: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestInterruptible(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, interruptible: Boolean) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def RequestAgentStateChangeAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, state: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestAgentStateChange(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, state: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def RequestForegroundActivationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestForegroundActivation(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def GetAudioClientAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def GetAudioClient(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def CreateAudioDeviceInputNodeAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, graph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.AudioDeviceInputNode]: ...
    @winrt_mixinmethod
    def CreateAudioDeviceInputNode(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, graph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.AudioDeviceInputNode: ...
    @winrt_mixinmethod
    def GetAudioCaptureDeviceIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAudioCaptureDeviceId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAudioRenderDeviceIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAudioRenderDeviceId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetSignalModelIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetSignalModelId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> UInt32: ...
    @winrt_mixinmethod
    def SetSignalModelIdAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, signalModelId: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetSignalModelId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, signalModelId: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def GetSupportedSignalModelIdsAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_mixinmethod
    def GetSupportedSignalModelIds(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def RequestActivationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, activationKind: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]: ...
    @winrt_mixinmethod
    def RequestActivation(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, activationKind: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult: ...
    @winrt_mixinmethod
    def SetSupportLockScreenActivationAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, lockScreenActivationSupported: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetSupportLockScreenActivation(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, lockScreenActivationSupported: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetMissingPrerequisites(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]: ...
    @winrt_mixinmethod
    def GetMissingPrerequisitesAsync(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetCurrentSessionAsync(cls: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession]: ...
    @winrt_classmethod
    def GetCurrentSessionSync(cls: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession: ...
    AgentState = property(get_AgentState, None)
    IsIndicatorLightAvailable = property(get_IsIndicatorLightAvailable, None)
    IsInterrupted = property(get_IsInterrupted, None)
    IsInterruptible = property(get_IsInterruptible, None)
    IsScreenAvailable = property(get_IsScreenAvailable, None)
    IsUserAuthenticated = property(get_IsUserAuthenticated, None)
    IsVoiceActivationAvailable = property(get_IsVoiceActivationAvailable, None)
    Signal = property(get_Signal, None)
    SessionInterrupted = event()
    SignalDetected = event()
    SystemStateChanged = event()
class ConversationalAgentSessionInterruptedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionInterruptedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs'
class ConversationalAgentSessionUpdateResponse(Enum, Int32):
    Success = 0
    Failed = 1
class ConversationalAgentSignal(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal'
    @winrt_mixinmethod
    def get_IsSignalVerificationRequired(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSignalVerificationRequired(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SignalId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SignalId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignalName(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SignalName(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignalContext(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_SignalContext(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_SignalStart(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SignalStart(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SignalEnd(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SignalEnd(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DetectorId(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DetectorKind(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    DetectorId = property(get_DetectorId, None)
    DetectorKind = property(get_DetectorKind, None)
    IsSignalVerificationRequired = property(get_IsSignalVerificationRequired, put_IsSignalVerificationRequired)
    SignalContext = property(get_SignalContext, put_SignalContext)
    SignalEnd = property(get_SignalEnd, put_SignalEnd)
    SignalId = property(get_SignalId, put_SignalId)
    SignalName = property(get_SignalName, put_SignalName)
    SignalStart = property(get_SignalStart, put_SignalStart)
class ConversationalAgentSignalDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignalDetectedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs'
class ConversationalAgentState(Enum, Int32):
    Inactive = 0
    Detecting = 1
    Listening = 2
    Working = 3
    Speaking = 4
    ListeningAndSpeaking = 5
class ConversationalAgentSystemStateChangeType(Enum, Int32):
    UserAuthentication = 0
    ScreenAvailability = 1
    IndicatorLightAvailability = 2
    VoiceActivationAvailability = 3
class ConversationalAgentSystemStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs'
    @winrt_mixinmethod
    def get_SystemStateChangeType(self: win32more.Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangeType: ...
    SystemStateChangeType = property(get_SystemStateChangeType, None)
class ConversationalAgentVoiceActivationPrerequisiteKind(Enum, Int32):
    MicrophonePermission = 0
    KnownAgents = 1
    AgentAllowed = 2
    AppCapability = 3
    BackgroundTaskRegistration = 4
    PolicyPermission = 5
class DetectionConfigurationAvailabilityChangeKind(Enum, Int32):
    SystemResourceAccess = 0
    Permission = 1
    LockScreenPermission = 2
class DetectionConfigurationAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangeKind: ...
    Kind = property(get_Kind, None)
class DetectionConfigurationAvailabilityInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasSystemResourceAccess(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasPermission(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasLockScreenPermission(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_UnavailableSystemResources(self: win32more.Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.SignalDetectorResourceKind]: ...
    HasLockScreenPermission = property(get_HasLockScreenPermission, None)
    HasPermission = property(get_HasPermission, None)
    HasSystemResourceAccess = property(get_HasSystemResourceAccess, None)
    IsEnabled = property(get_IsEnabled, None)
    UnavailableSystemResources = property(get_UnavailableSystemResources, None)
class DetectionConfigurationTrainingStatus(Enum, Int32):
    Success = 0
    FormatNotSupported = 1
    VoiceTooQuiet = 2
    VoiceTooLoud = 3
    VoiceTooFast = 4
    VoiceTooSlow = 5
    VoiceQualityProblem = 6
    TrainingSystemInternalError = 7
    TrainingTimedOut = 8
    ConfigurationNotFound = 9
class IActivationSignalDetectionConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration'
    _iid_ = Guid('{40d8be16-5217-581c-9ab2-ce9b2f2e8e00}')
    @winrt_commethod(6)
    def get_SignalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(10)
    def SetEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def SetEnabledAsync(self, value: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_AvailabilityInfo(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo: ...
    @winrt_commethod(13)
    def add_AvailabilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration, win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AvailabilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def SetModelData(self, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(16)
    def SetModelDataAsync(self, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def GetModelDataType(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def GetModelDataTypeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(19)
    def GetModelData(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(20)
    def GetModelDataAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IInputStream]: ...
    @winrt_commethod(21)
    def ClearModelData(self) -> Void: ...
    @winrt_commethod(22)
    def ClearModelDataAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(23)
    def get_TrainingStepsCompleted(self) -> UInt32: ...
    @winrt_commethod(24)
    def get_TrainingStepsRemaining(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_TrainingDataFormat(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat: ...
    @winrt_commethod(26)
    def ApplyTrainingData(self, trainingDataFormat: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus: ...
    @winrt_commethod(27)
    def ApplyTrainingDataAsync(self, trainingDataFormat: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]: ...
    @winrt_commethod(28)
    def ClearTrainingData(self) -> Void: ...
    @winrt_commethod(29)
    def ClearTrainingDataAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AvailabilityInfo = property(get_AvailabilityInfo, None)
    DisplayName = property(get_DisplayName, None)
    IsActive = property(get_IsActive, None)
    ModelId = property(get_ModelId, None)
    SignalId = property(get_SignalId, None)
    TrainingDataFormat = property(get_TrainingDataFormat, None)
    TrainingStepsCompleted = property(get_TrainingStepsCompleted, None)
    TrainingStepsRemaining = property(get_TrainingStepsRemaining, None)
    AvailabilityChanged = event()
class IActivationSignalDetectionConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2'
    _iid_ = Guid('{71d9b022-562c-57ce-a78b-8b4ff0145bab}')
    @winrt_commethod(6)
    def SetModelDataWithResult(self, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult: ...
    @winrt_commethod(7)
    def SetModelDataWithResultAsync(self, dataType: WinRT_String, data: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]: ...
    @winrt_commethod(8)
    def SetEnabledWithResultAsync(self, value: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]: ...
    @winrt_commethod(9)
    def SetEnabledWithResult(self, value: Boolean) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult: ...
    @winrt_commethod(10)
    def get_TrainingStepCompletionMaxAllowedTime(self) -> UInt32: ...
    TrainingStepCompletionMaxAllowedTime = property(get_TrainingStepCompletionMaxAllowedTime, None)
class IActivationSignalDetectionConfigurationCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult'
    _iid_ = Guid('{4c89bc1b-8d12-5e48-a71c-7f6bc1cd66e0}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationStatus: ...
    @winrt_commethod(7)
    def get_Configuration(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    Configuration = property(get_Configuration, None)
    Status = property(get_Status, None)
class IActivationSignalDetector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector'
    _iid_ = Guid('{b5bf345f-a4d0-5b2b-8e65-b3c55ee756ff}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    @winrt_commethod(8)
    def get_CanCreateConfigurations(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SupportedModelDataTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_SupportedTrainingDataFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]: ...
    @winrt_commethod(11)
    def get_SupportedPowerStates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorPowerState]: ...
    @winrt_commethod(12)
    def GetSupportedModelIdsForSignalId(self, signalId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def GetSupportedModelIdsForSignalIdAsync(self, signalId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(14)
    def CreateConfiguration(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def CreateConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def GetConfigurations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_commethod(17)
    def GetConfigurationsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]]: ...
    @winrt_commethod(18)
    def GetConfiguration(self, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    @winrt_commethod(19)
    def GetConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_commethod(20)
    def RemoveConfiguration(self, signalId: WinRT_String, modelId: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def RemoveConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    CanCreateConfigurations = property(get_CanCreateConfigurations, None)
    Kind = property(get_Kind, None)
    ProviderId = property(get_ProviderId, None)
    SupportedModelDataTypes = property(get_SupportedModelDataTypes, None)
    SupportedPowerStates = property(get_SupportedPowerStates, None)
    SupportedTrainingDataFormats = property(get_SupportedTrainingDataFormats, None)
class IActivationSignalDetector2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2'
    _iid_ = Guid('{c7e2490a-baa5-59d2-85d1-ba42f7cf78c9}')
    @winrt_commethod(6)
    def GetAvailableModelIdsForSignalIdAsync(self, signalId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(7)
    def GetAvailableModelIdsForSignalId(self, signalId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def CreateConfigurationWithResultAsync(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult]: ...
    @winrt_commethod(9)
    def CreateConfigurationWithResult(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult: ...
    @winrt_commethod(10)
    def RemoveConfigurationWithResultAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]: ...
    @winrt_commethod(11)
    def RemoveConfigurationWithResult(self, signalId: WinRT_String, modelId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult: ...
    @winrt_commethod(12)
    def get_DetectorId(self) -> WinRT_String: ...
    DetectorId = property(get_DetectorId, None)
class IConversationalAgentDetectorManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager'
    _iid_ = Guid('{de94fbb0-597a-5df8-8cfb-9dbb583ba3ff}')
    @winrt_commethod(6)
    def GetAllActivationSignalDetectors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_commethod(7)
    def GetAllActivationSignalDetectorsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_commethod(8)
    def GetActivationSignalDetectors(self, kind: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_commethod(9)
    def GetActivationSignalDetectorsAsync(self, kind: win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
class IConversationalAgentDetectorManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2'
    _iid_ = Guid('{84610f31-d7f3-52fe-9311-c9eb4e3eb30a}')
    @winrt_commethod(6)
    def GetActivationSignalDetectorFromId(self, detectorId: WinRT_String) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector: ...
    @winrt_commethod(7)
    def GetActivationSignalDetectorFromIdAsync(self, detectorId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
class IConversationalAgentDetectorManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManagerStatics'
    _iid_ = Guid('{36a8d283-fa0e-5693-8489-0fb2f0ab40d3}')
    @winrt_commethod(6)
    def get_Default(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager: ...
    Default = property(get_Default, None)
class IConversationalAgentSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession'
    _iid_ = Guid('{daaae09a-b7ba-57e5-ad13-df520f9b6fa7}')
    @winrt_commethod(6)
    def add_SessionInterrupted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SessionInterrupted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SignalDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SignalDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SystemStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SystemStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_AgentState(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState: ...
    @winrt_commethod(13)
    def get_Signal(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal: ...
    @winrt_commethod(14)
    def get_IsIndicatorLightAvailable(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsScreenAvailable(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsUserAuthenticated(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsVoiceActivationAvailable(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsInterruptible(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsInterrupted(self) -> Boolean: ...
    @winrt_commethod(20)
    def RequestInterruptibleAsync(self, interruptible: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(21)
    def RequestInterruptible(self, interruptible: Boolean) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(22)
    def RequestAgentStateChangeAsync(self, state: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(23)
    def RequestAgentStateChange(self, state: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(24)
    def RequestForegroundActivationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(25)
    def RequestForegroundActivation(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(26)
    def GetAudioClientAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(27)
    def GetAudioClient(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(28)
    def CreateAudioDeviceInputNodeAsync(self, graph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Audio.AudioDeviceInputNode]: ...
    @winrt_commethod(29)
    def CreateAudioDeviceInputNode(self, graph: win32more.Windows.Media.Audio.AudioGraph) -> win32more.Windows.Media.Audio.AudioDeviceInputNode: ...
    @winrt_commethod(30)
    def GetAudioCaptureDeviceIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(31)
    def GetAudioCaptureDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def GetAudioRenderDeviceIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(33)
    def GetAudioRenderDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def GetSignalModelIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(35)
    def GetSignalModelId(self) -> UInt32: ...
    @winrt_commethod(36)
    def SetSignalModelIdAsync(self, signalModelId: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(37)
    def SetSignalModelId(self, signalModelId: UInt32) -> Boolean: ...
    @winrt_commethod(38)
    def GetSupportedSignalModelIdsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_commethod(39)
    def GetSupportedSignalModelIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    AgentState = property(get_AgentState, None)
    IsIndicatorLightAvailable = property(get_IsIndicatorLightAvailable, None)
    IsInterrupted = property(get_IsInterrupted, None)
    IsInterruptible = property(get_IsInterruptible, None)
    IsScreenAvailable = property(get_IsScreenAvailable, None)
    IsUserAuthenticated = property(get_IsUserAuthenticated, None)
    IsVoiceActivationAvailable = property(get_IsVoiceActivationAvailable, None)
    Signal = property(get_Signal, None)
    SessionInterrupted = event()
    SignalDetected = event()
    SystemStateChanged = event()
class IConversationalAgentSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2'
    _iid_ = Guid('{a7a9fbf9-ac78-57ff-9596-acc7a1c9a607}')
    @winrt_commethod(6)
    def RequestActivationAsync(self, activationKind: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]: ...
    @winrt_commethod(7)
    def RequestActivation(self, activationKind: win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult: ...
    @winrt_commethod(8)
    def SetSupportLockScreenActivationAsync(self, lockScreenActivationSupported: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def SetSupportLockScreenActivation(self, lockScreenActivationSupported: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetMissingPrerequisites(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]: ...
    @winrt_commethod(11)
    def GetMissingPrerequisitesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]: ...
class IConversationalAgentSessionInterruptedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionInterruptedEventArgs'
    _iid_ = Guid('{9766591f-f63d-5d3e-9bf2-bd0760552686}')
class IConversationalAgentSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics'
    _iid_ = Guid('{a005166e-e954-576e-be04-11b8ed10f37b}')
    @winrt_commethod(6)
    def GetCurrentSessionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession]: ...
    @winrt_commethod(7)
    def GetCurrentSessionSync(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession: ...
class IConversationalAgentSignal(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal'
    _iid_ = Guid('{20ed25f7-b120-51f2-8603-265d6a47f232}')
    @winrt_commethod(6)
    def get_IsSignalVerificationRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSignalVerificationRequired(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SignalId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SignalId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SignalName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_SignalName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_SignalContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def put_SignalContext(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(14)
    def get_SignalStart(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_SignalStart(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def get_SignalEnd(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_SignalEnd(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    IsSignalVerificationRequired = property(get_IsSignalVerificationRequired, put_IsSignalVerificationRequired)
    SignalContext = property(get_SignalContext, put_SignalContext)
    SignalEnd = property(get_SignalEnd, put_SignalEnd)
    SignalId = property(get_SignalId, put_SignalId)
    SignalName = property(get_SignalName, put_SignalName)
    SignalStart = property(get_SignalStart, put_SignalStart)
class IConversationalAgentSignal2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2'
    _iid_ = Guid('{d0cc7ba9-9a7b-5c34-880e-b6146c904ecb}')
    @winrt_commethod(6)
    def get_DetectorId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DetectorKind(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    DetectorId = property(get_DetectorId, None)
    DetectorKind = property(get_DetectorKind, None)
class IConversationalAgentSignalDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignalDetectedEventArgs'
    _iid_ = Guid('{4d57eb8f-f88a-599b-91d3-d604876708bc}')
class IConversationalAgentSystemStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs'
    _iid_ = Guid('{1c2c6e3e-2785-59a7-8e71-38adeef79928}')
    @winrt_commethod(6)
    def get_SystemStateChangeType(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangeType: ...
    SystemStateChangeType = property(get_SystemStateChangeType, None)
class IDetectionConfigurationAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs'
    _iid_ = Guid('{5129c9fb-4be8-5f14-af2b-88d62b1b4462}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangeKind: ...
    Kind = property(get_Kind, None)
class IDetectionConfigurationAvailabilityInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo'
    _iid_ = Guid('{b5affeb0-40f0-5398-b838-91979c2c6208}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasSystemResourceAccess(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HasPermission(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_HasLockScreenPermission(self) -> Boolean: ...
    HasLockScreenPermission = property(get_HasLockScreenPermission, None)
    HasPermission = property(get_HasPermission, None)
    HasSystemResourceAccess = property(get_HasSystemResourceAccess, None)
    IsEnabled = property(get_IsEnabled, None)
class IDetectionConfigurationAvailabilityInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo2'
    _iid_ = Guid('{30e06433-38b3-5c4b-84c3-62b6e685b2ff}')
    @winrt_commethod(6)
    def get_UnavailableSystemResources(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.ConversationalAgent.SignalDetectorResourceKind]: ...
    UnavailableSystemResources = property(get_UnavailableSystemResources, None)
class SignalDetectorResourceKind(Enum, Int32):
    ParallelModelSupport = 0
    ParallelModelSupportForAgent = 1
    ParallelSignalSupport = 2
    ParallelSignalSupportForAgent = 3
    DisplayOffSupport = 4
    PluggedInPower = 5
    Detector = 6
    SupportedSleepState = 7
    SupportedBatterySaverState = 8
    ScreenAvailability = 9
    InputHardware = 10
    AcousticEchoCancellation = 11
    ModelIdSupport = 12
    DataChannel = 13


make_ready(__name__)
