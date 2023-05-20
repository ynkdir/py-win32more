from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.ConversationalAgent
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.Audio
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
class ActivationSignalDetectionConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration'
    @winrt_mixinmethod
    def get_SignalId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def SetEnabled(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetEnabledAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, value: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_AvailabilityInfo(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration, Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetModelData(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def SetModelDataAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetModelDataType(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetModelDataTypeAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetModelData(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetModelDataAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IInputStream]: ...
    @winrt_mixinmethod
    def ClearModelData(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Void: ...
    @winrt_mixinmethod
    def ClearModelDataAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TrainingStepsCompleted(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrainingStepsRemaining(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrainingDataFormat(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat: ...
    @winrt_mixinmethod
    def ApplyTrainingData(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, trainingDataFormat: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: Windows.Storage.Streams.IInputStream) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus: ...
    @winrt_mixinmethod
    def ApplyTrainingDataAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration, trainingDataFormat: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]: ...
    @winrt_mixinmethod
    def ClearTrainingData(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Void: ...
    @winrt_mixinmethod
    def ClearTrainingDataAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def SetModelDataWithResult(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult: ...
    @winrt_mixinmethod
    def SetModelDataWithResultAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]: ...
    @winrt_mixinmethod
    def SetEnabledWithResultAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, value: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]: ...
    @winrt_mixinmethod
    def SetEnabledWithResult(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2, value: Boolean) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult: ...
    @winrt_mixinmethod
    def get_TrainingStepCompletionMaxAllowedTime(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2) -> UInt32: ...
    SignalId = property(get_SignalId, None)
    ModelId = property(get_ModelId, None)
    DisplayName = property(get_DisplayName, None)
    IsActive = property(get_IsActive, None)
    AvailabilityInfo = property(get_AvailabilityInfo, None)
    TrainingStepsCompleted = property(get_TrainingStepsCompleted, None)
    TrainingStepsRemaining = property(get_TrainingStepsRemaining, None)
    TrainingDataFormat = property(get_TrainingDataFormat, None)
    TrainingStepCompletionMaxAllowedTime = property(get_TrainingStepCompletionMaxAllowedTime, None)
class ActivationSignalDetectionConfigurationCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationStatus: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    Status = property(get_Status, None)
    Configuration = property(get_Configuration, None)
ActivationSignalDetectionConfigurationCreationStatus = Int32
ActivationSignalDetectionConfigurationCreationStatus_Success: ActivationSignalDetectionConfigurationCreationStatus = 0
ActivationSignalDetectionConfigurationCreationStatus_SignalIdNotAvailable: ActivationSignalDetectionConfigurationCreationStatus = 1
ActivationSignalDetectionConfigurationCreationStatus_ModelIdNotSupported: ActivationSignalDetectionConfigurationCreationStatus = 2
ActivationSignalDetectionConfigurationCreationStatus_InvalidSignalId: ActivationSignalDetectionConfigurationCreationStatus = 3
ActivationSignalDetectionConfigurationCreationStatus_InvalidModelId: ActivationSignalDetectionConfigurationCreationStatus = 4
ActivationSignalDetectionConfigurationCreationStatus_InvalidDisplayName: ActivationSignalDetectionConfigurationCreationStatus = 5
ActivationSignalDetectionConfigurationCreationStatus_ConfigurationAlreadyExists: ActivationSignalDetectionConfigurationCreationStatus = 6
ActivationSignalDetectionConfigurationCreationStatus_CreationNotSupported: ActivationSignalDetectionConfigurationCreationStatus = 7
ActivationSignalDetectionConfigurationRemovalResult = Int32
ActivationSignalDetectionConfigurationRemovalResult_Success: ActivationSignalDetectionConfigurationRemovalResult = 0
ActivationSignalDetectionConfigurationRemovalResult_NotFound: ActivationSignalDetectionConfigurationRemovalResult = 1
ActivationSignalDetectionConfigurationRemovalResult_CurrentlyEnabled: ActivationSignalDetectionConfigurationRemovalResult = 2
ActivationSignalDetectionConfigurationRemovalResult_RemovalNotSupported: ActivationSignalDetectionConfigurationRemovalResult = 3
ActivationSignalDetectionConfigurationSetModelDataResult = Int32
ActivationSignalDetectionConfigurationSetModelDataResult_Success: ActivationSignalDetectionConfigurationSetModelDataResult = 0
ActivationSignalDetectionConfigurationSetModelDataResult_EmptyModelData: ActivationSignalDetectionConfigurationSetModelDataResult = 1
ActivationSignalDetectionConfigurationSetModelDataResult_UnsupportedFormat: ActivationSignalDetectionConfigurationSetModelDataResult = 2
ActivationSignalDetectionConfigurationSetModelDataResult_ConfigurationCurrentlyEnabled: ActivationSignalDetectionConfigurationSetModelDataResult = 3
ActivationSignalDetectionConfigurationSetModelDataResult_InvalidData: ActivationSignalDetectionConfigurationSetModelDataResult = 4
ActivationSignalDetectionConfigurationSetModelDataResult_SetModelDataNotSupported: ActivationSignalDetectionConfigurationSetModelDataResult = 5
ActivationSignalDetectionConfigurationSetModelDataResult_ConfigurationNotFound: ActivationSignalDetectionConfigurationSetModelDataResult = 6
ActivationSignalDetectionConfigurationSetModelDataResult_UnknownError: ActivationSignalDetectionConfigurationSetModelDataResult = 7
ActivationSignalDetectionConfigurationStateChangeResult = Int32
ActivationSignalDetectionConfigurationStateChangeResult_Success: ActivationSignalDetectionConfigurationStateChangeResult = 0
ActivationSignalDetectionConfigurationStateChangeResult_NoModelData: ActivationSignalDetectionConfigurationStateChangeResult = 1
ActivationSignalDetectionConfigurationStateChangeResult_ConfigurationNotFound: ActivationSignalDetectionConfigurationStateChangeResult = 2
ActivationSignalDetectionTrainingDataFormat = Int32
ActivationSignalDetectionTrainingDataFormat_Voice8kHz8BitMono: ActivationSignalDetectionTrainingDataFormat = 0
ActivationSignalDetectionTrainingDataFormat_Voice8kHz16BitMono: ActivationSignalDetectionTrainingDataFormat = 1
ActivationSignalDetectionTrainingDataFormat_Voice16kHz8BitMono: ActivationSignalDetectionTrainingDataFormat = 2
ActivationSignalDetectionTrainingDataFormat_Voice16kHz16BitMono: ActivationSignalDetectionTrainingDataFormat = 3
ActivationSignalDetectionTrainingDataFormat_VoiceOEMDefined: ActivationSignalDetectionTrainingDataFormat = 4
ActivationSignalDetectionTrainingDataFormat_Audio44kHz8BitMono: ActivationSignalDetectionTrainingDataFormat = 5
ActivationSignalDetectionTrainingDataFormat_Audio44kHz16BitMono: ActivationSignalDetectionTrainingDataFormat = 6
ActivationSignalDetectionTrainingDataFormat_Audio48kHz8BitMono: ActivationSignalDetectionTrainingDataFormat = 7
ActivationSignalDetectionTrainingDataFormat_Audio48kHz16BitMono: ActivationSignalDetectionTrainingDataFormat = 8
ActivationSignalDetectionTrainingDataFormat_AudioOEMDefined: ActivationSignalDetectionTrainingDataFormat = 9
ActivationSignalDetectionTrainingDataFormat_OtherOEMDefined: ActivationSignalDetectionTrainingDataFormat = 10
class ActivationSignalDetector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector'
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    @winrt_mixinmethod
    def get_CanCreateConfigurations(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedModelDataTypes(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SupportedTrainingDataFormats(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]: ...
    @winrt_mixinmethod
    def get_SupportedPowerStates(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorPowerState]: ...
    @winrt_mixinmethod
    def GetSupportedModelIdsForSignalId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetSupportedModelIdsForSignalIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def CreateConfiguration(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def CreateConfigurationAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetConfigurations(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_mixinmethod
    def GetConfigurationsAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]]: ...
    @winrt_mixinmethod
    def GetConfiguration(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    @winrt_mixinmethod
    def GetConfigurationAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_mixinmethod
    def RemoveConfiguration(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveConfigurationAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetAvailableModelIdsForSignalIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_mixinmethod
    def GetAvailableModelIdsForSignalId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def CreateConfigurationWithResultAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult]: ...
    @winrt_mixinmethod
    def CreateConfigurationWithResult(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult: ...
    @winrt_mixinmethod
    def RemoveConfigurationWithResultAsync(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]: ...
    @winrt_mixinmethod
    def RemoveConfigurationWithResult(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2, signalId: WinRT_String, modelId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult: ...
    @winrt_mixinmethod
    def get_DetectorId(self: Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2) -> WinRT_String: ...
    ProviderId = property(get_ProviderId, None)
    Kind = property(get_Kind, None)
    CanCreateConfigurations = property(get_CanCreateConfigurations, None)
    SupportedModelDataTypes = property(get_SupportedModelDataTypes, None)
    SupportedTrainingDataFormats = property(get_SupportedTrainingDataFormats, None)
    SupportedPowerStates = property(get_SupportedPowerStates, None)
    DetectorId = property(get_DetectorId, None)
ActivationSignalDetectorKind = Int32
ActivationSignalDetectorKind_AudioPattern: ActivationSignalDetectorKind = 0
ActivationSignalDetectorKind_AudioImpulse: ActivationSignalDetectorKind = 1
ActivationSignalDetectorKind_HardwareEvent: ActivationSignalDetectorKind = 2
ActivationSignalDetectorPowerState = Int32
ActivationSignalDetectorPowerState_HighPower: ActivationSignalDetectorPowerState = 0
ActivationSignalDetectorPowerState_ConnectedLowPower: ActivationSignalDetectorPowerState = 1
ActivationSignalDetectorPowerState_DisconnectedLowPower: ActivationSignalDetectorPowerState = 2
ConversationalAgentActivationKind = Int32
ConversationalAgentActivationKind_VoiceActivationPreview: ConversationalAgentActivationKind = 0
ConversationalAgentActivationKind_Foreground: ConversationalAgentActivationKind = 1
ConversationalAgentActivationResult = Int32
ConversationalAgentActivationResult_Success: ConversationalAgentActivationResult = 0
ConversationalAgentActivationResult_AgentInactive: ConversationalAgentActivationResult = 1
ConversationalAgentActivationResult_ScreenNotAvailable: ConversationalAgentActivationResult = 2
ConversationalAgentActivationResult_AgentInterrupted: ConversationalAgentActivationResult = 3
class _ConversationalAgentDetectorManager_Meta_(ComPtr.__class__):
    pass
class ConversationalAgentDetectorManager(ComPtr, metaclass=_ConversationalAgentDetectorManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager'
    @winrt_mixinmethod
    def GetAllActivationSignalDetectors(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_mixinmethod
    def GetAllActivationSignalDetectorsAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectors(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager, kind: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorsAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager, kind: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorFromId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2, detectorId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector: ...
    @winrt_mixinmethod
    def GetActivationSignalDetectorFromIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2, detectorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_classmethod
    def get_Default(cls: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManagerStatics) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager: ...
    _ConversationalAgentDetectorManager_Meta_.Default = property(get_Default.__wrapped__, None)
class ConversationalAgentSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession'
    @winrt_mixinmethod
    def add_SessionInterrupted(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionInterrupted(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SignalDetected(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SignalDetected(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemStateChanged(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemStateChanged(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AgentState(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState: ...
    @winrt_mixinmethod
    def get_Signal(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal: ...
    @winrt_mixinmethod
    def get_IsIndicatorLightAvailable(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScreenAvailable(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserAuthenticated(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVoiceActivationAvailable(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInterruptible(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInterrupted(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Boolean: ...
    @winrt_mixinmethod
    def RequestInterruptibleAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, interruptible: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestInterruptible(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, interruptible: Boolean) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def RequestAgentStateChangeAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, state: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestAgentStateChange(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, state: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def RequestForegroundActivationAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_mixinmethod
    def RequestForegroundActivation(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_mixinmethod
    def GetAudioClientAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def GetAudioClient(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def CreateAudioDeviceInputNodeAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, graph: Windows.Media.Audio.AudioGraph) -> Windows.Foundation.IAsyncOperation[Windows.Media.Audio.AudioDeviceInputNode]: ...
    @winrt_mixinmethod
    def CreateAudioDeviceInputNode(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, graph: Windows.Media.Audio.AudioGraph) -> Windows.Media.Audio.AudioDeviceInputNode: ...
    @winrt_mixinmethod
    def GetAudioCaptureDeviceIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAudioCaptureDeviceId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAudioRenderDeviceIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAudioRenderDeviceId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetSignalModelIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetSignalModelId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> UInt32: ...
    @winrt_mixinmethod
    def SetSignalModelIdAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, signalModelId: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def SetSignalModelId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession, signalModelId: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def GetSupportedSignalModelIdsAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_mixinmethod
    def GetSupportedSignalModelIds(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def RequestActivationAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, activationKind: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]: ...
    @winrt_mixinmethod
    def RequestActivation(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, activationKind: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult: ...
    @winrt_mixinmethod
    def SetSupportLockScreenActivationAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, lockScreenActivationSupported: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetSupportLockScreenActivation(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2, lockScreenActivationSupported: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetMissingPrerequisites(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]: ...
    @winrt_mixinmethod
    def GetMissingPrerequisitesAsync(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetCurrentSessionAsync(cls: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession]: ...
    @winrt_classmethod
    def GetCurrentSessionSync(cls: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession: ...
    AgentState = property(get_AgentState, None)
    Signal = property(get_Signal, None)
    IsIndicatorLightAvailable = property(get_IsIndicatorLightAvailable, None)
    IsScreenAvailable = property(get_IsScreenAvailable, None)
    IsUserAuthenticated = property(get_IsUserAuthenticated, None)
    IsVoiceActivationAvailable = property(get_IsVoiceActivationAvailable, None)
    IsInterruptible = property(get_IsInterruptible, None)
    IsInterrupted = property(get_IsInterrupted, None)
class ConversationalAgentSessionInterruptedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionInterruptedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs'
ConversationalAgentSessionUpdateResponse = Int32
ConversationalAgentSessionUpdateResponse_Success: ConversationalAgentSessionUpdateResponse = 0
ConversationalAgentSessionUpdateResponse_Failed: ConversationalAgentSessionUpdateResponse = 1
class ConversationalAgentSignal(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal'
    @winrt_mixinmethod
    def get_IsSignalVerificationRequired(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSignalVerificationRequired(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SignalId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SignalId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignalName(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SignalName(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignalContext(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_SignalContext(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_SignalStart(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SignalStart(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SignalEnd(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SignalEnd(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DetectorId(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DetectorKind(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    IsSignalVerificationRequired = property(get_IsSignalVerificationRequired, put_IsSignalVerificationRequired)
    SignalId = property(get_SignalId, put_SignalId)
    SignalName = property(get_SignalName, put_SignalName)
    SignalContext = property(get_SignalContext, put_SignalContext)
    SignalStart = property(get_SignalStart, put_SignalStart)
    SignalEnd = property(get_SignalEnd, put_SignalEnd)
    DetectorId = property(get_DetectorId, None)
    DetectorKind = property(get_DetectorKind, None)
class ConversationalAgentSignalDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignalDetectedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs'
ConversationalAgentState = Int32
ConversationalAgentState_Inactive: ConversationalAgentState = 0
ConversationalAgentState_Detecting: ConversationalAgentState = 1
ConversationalAgentState_Listening: ConversationalAgentState = 2
ConversationalAgentState_Working: ConversationalAgentState = 3
ConversationalAgentState_Speaking: ConversationalAgentState = 4
ConversationalAgentState_ListeningAndSpeaking: ConversationalAgentState = 5
ConversationalAgentSystemStateChangeType = Int32
ConversationalAgentSystemStateChangeType_UserAuthentication: ConversationalAgentSystemStateChangeType = 0
ConversationalAgentSystemStateChangeType_ScreenAvailability: ConversationalAgentSystemStateChangeType = 1
ConversationalAgentSystemStateChangeType_IndicatorLightAvailability: ConversationalAgentSystemStateChangeType = 2
ConversationalAgentSystemStateChangeType_VoiceActivationAvailability: ConversationalAgentSystemStateChangeType = 3
class ConversationalAgentSystemStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs'
    @winrt_mixinmethod
    def get_SystemStateChangeType(self: Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangeType: ...
    SystemStateChangeType = property(get_SystemStateChangeType, None)
ConversationalAgentVoiceActivationPrerequisiteKind = Int32
ConversationalAgentVoiceActivationPrerequisiteKind_MicrophonePermission: ConversationalAgentVoiceActivationPrerequisiteKind = 0
ConversationalAgentVoiceActivationPrerequisiteKind_KnownAgents: ConversationalAgentVoiceActivationPrerequisiteKind = 1
ConversationalAgentVoiceActivationPrerequisiteKind_AgentAllowed: ConversationalAgentVoiceActivationPrerequisiteKind = 2
ConversationalAgentVoiceActivationPrerequisiteKind_AppCapability: ConversationalAgentVoiceActivationPrerequisiteKind = 3
ConversationalAgentVoiceActivationPrerequisiteKind_BackgroundTaskRegistration: ConversationalAgentVoiceActivationPrerequisiteKind = 4
ConversationalAgentVoiceActivationPrerequisiteKind_PolicyPermission: ConversationalAgentVoiceActivationPrerequisiteKind = 5
DetectionConfigurationAvailabilityChangeKind = Int32
DetectionConfigurationAvailabilityChangeKind_SystemResourceAccess: DetectionConfigurationAvailabilityChangeKind = 0
DetectionConfigurationAvailabilityChangeKind_Permission: DetectionConfigurationAvailabilityChangeKind = 1
DetectionConfigurationAvailabilityChangeKind_LockScreenPermission: DetectionConfigurationAvailabilityChangeKind = 2
class DetectionConfigurationAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangeKind: ...
    Kind = property(get_Kind, None)
class DetectionConfigurationAvailabilityInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasSystemResourceAccess(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasPermission(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasLockScreenPermission(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_UnavailableSystemResources(self: Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.SignalDetectorResourceKind]: ...
    IsEnabled = property(get_IsEnabled, None)
    HasSystemResourceAccess = property(get_HasSystemResourceAccess, None)
    HasPermission = property(get_HasPermission, None)
    HasLockScreenPermission = property(get_HasLockScreenPermission, None)
    UnavailableSystemResources = property(get_UnavailableSystemResources, None)
DetectionConfigurationTrainingStatus = Int32
DetectionConfigurationTrainingStatus_Success: DetectionConfigurationTrainingStatus = 0
DetectionConfigurationTrainingStatus_FormatNotSupported: DetectionConfigurationTrainingStatus = 1
DetectionConfigurationTrainingStatus_VoiceTooQuiet: DetectionConfigurationTrainingStatus = 2
DetectionConfigurationTrainingStatus_VoiceTooLoud: DetectionConfigurationTrainingStatus = 3
DetectionConfigurationTrainingStatus_VoiceTooFast: DetectionConfigurationTrainingStatus = 4
DetectionConfigurationTrainingStatus_VoiceTooSlow: DetectionConfigurationTrainingStatus = 5
DetectionConfigurationTrainingStatus_VoiceQualityProblem: DetectionConfigurationTrainingStatus = 6
DetectionConfigurationTrainingStatus_TrainingSystemInternalError: DetectionConfigurationTrainingStatus = 7
DetectionConfigurationTrainingStatus_TrainingTimedOut: DetectionConfigurationTrainingStatus = 8
DetectionConfigurationTrainingStatus_ConfigurationNotFound: DetectionConfigurationTrainingStatus = 9
class IActivationSignalDetectionConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def SetEnabledAsync(self, value: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_AvailabilityInfo(self) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityInfo: ...
    @winrt_commethod(13)
    def add_AvailabilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration, Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AvailabilityChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def SetModelData(self, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(16)
    def SetModelDataAsync(self, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def GetModelDataType(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def GetModelDataTypeAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(19)
    def GetModelData(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(20)
    def GetModelDataAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IInputStream]: ...
    @winrt_commethod(21)
    def ClearModelData(self) -> Void: ...
    @winrt_commethod(22)
    def ClearModelDataAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(23)
    def get_TrainingStepsCompleted(self) -> UInt32: ...
    @winrt_commethod(24)
    def get_TrainingStepsRemaining(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_TrainingDataFormat(self) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat: ...
    @winrt_commethod(26)
    def ApplyTrainingData(self, trainingDataFormat: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: Windows.Storage.Streams.IInputStream) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus: ...
    @winrt_commethod(27)
    def ApplyTrainingDataAsync(self, trainingDataFormat: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat, trainingData: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]: ...
    @winrt_commethod(28)
    def ClearTrainingData(self) -> Void: ...
    @winrt_commethod(29)
    def ClearTrainingDataAsync(self) -> Windows.Foundation.IAsyncAction: ...
    SignalId = property(get_SignalId, None)
    ModelId = property(get_ModelId, None)
    DisplayName = property(get_DisplayName, None)
    IsActive = property(get_IsActive, None)
    AvailabilityInfo = property(get_AvailabilityInfo, None)
    TrainingStepsCompleted = property(get_TrainingStepsCompleted, None)
    TrainingStepsRemaining = property(get_TrainingStepsRemaining, None)
    TrainingDataFormat = property(get_TrainingDataFormat, None)
class IActivationSignalDetectionConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfiguration2'
    _iid_ = Guid('{71d9b022-562c-57ce-a78b-8b4ff0145bab}')
    @winrt_commethod(6)
    def SetModelDataWithResult(self, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult: ...
    @winrt_commethod(7)
    def SetModelDataWithResultAsync(self, dataType: WinRT_String, data: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]: ...
    @winrt_commethod(8)
    def SetEnabledWithResultAsync(self, value: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]: ...
    @winrt_commethod(9)
    def SetEnabledWithResult(self, value: Boolean) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult: ...
    @winrt_commethod(10)
    def get_TrainingStepCompletionMaxAllowedTime(self) -> UInt32: ...
    TrainingStepCompletionMaxAllowedTime = property(get_TrainingStepCompletionMaxAllowedTime, None)
class IActivationSignalDetectionConfigurationCreationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetectionConfigurationCreationResult'
    _iid_ = Guid('{4c89bc1b-8d12-5e48-a71c-7f6bc1cd66e0}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationStatus: ...
    @winrt_commethod(7)
    def get_Configuration(self) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    Status = property(get_Status, None)
    Configuration = property(get_Configuration, None)
class IActivationSignalDetector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector'
    _iid_ = Guid('{b5bf345f-a4d0-5b2b-8e65-b3c55ee756ff}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    @winrt_commethod(8)
    def get_CanCreateConfigurations(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SupportedModelDataTypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_SupportedTrainingDataFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]: ...
    @winrt_commethod(11)
    def get_SupportedPowerStates(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorPowerState]: ...
    @winrt_commethod(12)
    def GetSupportedModelIdsForSignalId(self, signalId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def GetSupportedModelIdsForSignalIdAsync(self, signalId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(14)
    def CreateConfiguration(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def CreateConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def GetConfigurations(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_commethod(17)
    def GetConfigurationsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]]: ...
    @winrt_commethod(18)
    def GetConfiguration(self, signalId: WinRT_String, modelId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration: ...
    @winrt_commethod(19)
    def GetConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfiguration]: ...
    @winrt_commethod(20)
    def RemoveConfiguration(self, signalId: WinRT_String, modelId: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def RemoveConfigurationAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    ProviderId = property(get_ProviderId, None)
    Kind = property(get_Kind, None)
    CanCreateConfigurations = property(get_CanCreateConfigurations, None)
    SupportedModelDataTypes = property(get_SupportedModelDataTypes, None)
    SupportedTrainingDataFormats = property(get_SupportedTrainingDataFormats, None)
    SupportedPowerStates = property(get_SupportedPowerStates, None)
class IActivationSignalDetector2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IActivationSignalDetector2'
    _iid_ = Guid('{c7e2490a-baa5-59d2-85d1-ba42f7cf78c9}')
    @winrt_commethod(6)
    def GetAvailableModelIdsForSignalIdAsync(self, signalId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(7)
    def GetAvailableModelIdsForSignalId(self, signalId: WinRT_String) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def CreateConfigurationWithResultAsync(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult]: ...
    @winrt_commethod(9)
    def CreateConfigurationWithResult(self, signalId: WinRT_String, modelId: WinRT_String, displayName: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationResult: ...
    @winrt_commethod(10)
    def RemoveConfigurationWithResultAsync(self, signalId: WinRT_String, modelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]: ...
    @winrt_commethod(11)
    def RemoveConfigurationWithResult(self, signalId: WinRT_String, modelId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult: ...
    @winrt_commethod(12)
    def get_DetectorId(self) -> WinRT_String: ...
    DetectorId = property(get_DetectorId, None)
class IConversationalAgentDetectorManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager'
    _iid_ = Guid('{de94fbb0-597a-5df8-8cfb-9dbb583ba3ff}')
    @winrt_commethod(6)
    def GetAllActivationSignalDetectors(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_commethod(7)
    def GetAllActivationSignalDetectorsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
    @winrt_commethod(8)
    def GetActivationSignalDetectors(self, kind: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
    @winrt_commethod(9)
    def GetActivationSignalDetectorsAsync(self, kind: Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]]: ...
class IConversationalAgentDetectorManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManager2'
    _iid_ = Guid('{84610f31-d7f3-52fe-9311-c9eb4e3eb30a}')
    @winrt_commethod(6)
    def GetActivationSignalDetectorFromId(self, detectorId: WinRT_String) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector: ...
    @winrt_commethod(7)
    def GetActivationSignalDetectorFromIdAsync(self, detectorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetector]: ...
class IConversationalAgentDetectorManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentDetectorManagerStatics'
    _iid_ = Guid('{36a8d283-fa0e-5693-8489-0fb2f0ab40d3}')
    @winrt_commethod(6)
    def get_Default(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentDetectorManager: ...
    Default = property(get_Default, None)
class IConversationalAgentSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession'
    _iid_ = Guid('{daaae09a-b7ba-57e5-ad13-df520f9b6fa7}')
    @winrt_commethod(6)
    def add_SessionInterrupted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionInterruptedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SessionInterrupted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SignalDetected(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignalDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SignalDetected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SystemStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession, Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SystemStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_AgentState(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState: ...
    @winrt_commethod(13)
    def get_Signal(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSignal: ...
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
    def RequestInterruptibleAsync(self, interruptible: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(21)
    def RequestInterruptible(self, interruptible: Boolean) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(22)
    def RequestAgentStateChangeAsync(self, state: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(23)
    def RequestAgentStateChange(self, state: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(24)
    def RequestForegroundActivationAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]: ...
    @winrt_commethod(25)
    def RequestForegroundActivation(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse: ...
    @winrt_commethod(26)
    def GetAudioClientAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(27)
    def GetAudioClient(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(28)
    def CreateAudioDeviceInputNodeAsync(self, graph: Windows.Media.Audio.AudioGraph) -> Windows.Foundation.IAsyncOperation[Windows.Media.Audio.AudioDeviceInputNode]: ...
    @winrt_commethod(29)
    def CreateAudioDeviceInputNode(self, graph: Windows.Media.Audio.AudioGraph) -> Windows.Media.Audio.AudioDeviceInputNode: ...
    @winrt_commethod(30)
    def GetAudioCaptureDeviceIdAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(31)
    def GetAudioCaptureDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def GetAudioRenderDeviceIdAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(33)
    def GetAudioRenderDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def GetSignalModelIdAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(35)
    def GetSignalModelId(self) -> UInt32: ...
    @winrt_commethod(36)
    def SetSignalModelIdAsync(self, signalModelId: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(37)
    def SetSignalModelId(self, signalModelId: UInt32) -> Boolean: ...
    @winrt_commethod(38)
    def GetSupportedSignalModelIdsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_commethod(39)
    def GetSupportedSignalModelIds(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    AgentState = property(get_AgentState, None)
    Signal = property(get_Signal, None)
    IsIndicatorLightAvailable = property(get_IsIndicatorLightAvailable, None)
    IsScreenAvailable = property(get_IsScreenAvailable, None)
    IsUserAuthenticated = property(get_IsUserAuthenticated, None)
    IsVoiceActivationAvailable = property(get_IsVoiceActivationAvailable, None)
    IsInterruptible = property(get_IsInterruptible, None)
    IsInterrupted = property(get_IsInterrupted, None)
class IConversationalAgentSession2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSession2'
    _iid_ = Guid('{a7a9fbf9-ac78-57ff-9596-acc7a1c9a607}')
    @winrt_commethod(6)
    def RequestActivationAsync(self, activationKind: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]: ...
    @winrt_commethod(7)
    def RequestActivation(self, activationKind: Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult: ...
    @winrt_commethod(8)
    def SetSupportLockScreenActivationAsync(self, lockScreenActivationSupported: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def SetSupportLockScreenActivation(self, lockScreenActivationSupported: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetMissingPrerequisites(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]: ...
    @winrt_commethod(11)
    def GetMissingPrerequisitesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]: ...
class IConversationalAgentSessionInterruptedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionInterruptedEventArgs'
    _iid_ = Guid('{9766591f-f63d-5d3e-9bf2-bd0760552686}')
class IConversationalAgentSessionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSessionStatics'
    _iid_ = Guid('{a005166e-e954-576e-be04-11b8ed10f37b}')
    @winrt_commethod(6)
    def GetCurrentSessionAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession]: ...
    @winrt_commethod(7)
    def GetCurrentSessionSync(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSession: ...
class IConversationalAgentSignal(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_SignalContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def put_SignalContext(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(14)
    def get_SignalStart(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_SignalStart(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def get_SignalEnd(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_SignalEnd(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    IsSignalVerificationRequired = property(get_IsSignalVerificationRequired, put_IsSignalVerificationRequired)
    SignalId = property(get_SignalId, put_SignalId)
    SignalName = property(get_SignalName, put_SignalName)
    SignalContext = property(get_SignalContext, put_SignalContext)
    SignalStart = property(get_SignalStart, put_SignalStart)
    SignalEnd = property(get_SignalEnd, put_SignalEnd)
class IConversationalAgentSignal2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignal2'
    _iid_ = Guid('{d0cc7ba9-9a7b-5c34-880e-b6146c904ecb}')
    @winrt_commethod(6)
    def get_DetectorId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DetectorKind(self) -> Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind: ...
    DetectorId = property(get_DetectorId, None)
    DetectorKind = property(get_DetectorKind, None)
class IConversationalAgentSignalDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSignalDetectedEventArgs'
    _iid_ = Guid('{4d57eb8f-f88a-599b-91d3-d604876708bc}')
class IConversationalAgentSystemStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IConversationalAgentSystemStateChangedEventArgs'
    _iid_ = Guid('{1c2c6e3e-2785-59a7-8e71-38adeef79928}')
    @winrt_commethod(6)
    def get_SystemStateChangeType(self) -> Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangeType: ...
    SystemStateChangeType = property(get_SystemStateChangeType, None)
class IDetectionConfigurationAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityChangedEventArgs'
    _iid_ = Guid('{5129c9fb-4be8-5f14-af2b-88d62b1b4462}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangeKind: ...
    Kind = property(get_Kind, None)
class IDetectionConfigurationAvailabilityInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    IsEnabled = property(get_IsEnabled, None)
    HasSystemResourceAccess = property(get_HasSystemResourceAccess, None)
    HasPermission = property(get_HasPermission, None)
    HasLockScreenPermission = property(get_HasLockScreenPermission, None)
class IDetectionConfigurationAvailabilityInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ConversationalAgent.IDetectionConfigurationAvailabilityInfo2'
    _iid_ = Guid('{30e06433-38b3-5c4b-84c3-62b6e685b2ff}')
    @winrt_commethod(6)
    def get_UnavailableSystemResources(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.ConversationalAgent.SignalDetectorResourceKind]: ...
    UnavailableSystemResources = property(get_UnavailableSystemResources, None)
SignalDetectorResourceKind = Int32
SignalDetectorResourceKind_ParallelModelSupport: SignalDetectorResourceKind = 0
SignalDetectorResourceKind_ParallelModelSupportForAgent: SignalDetectorResourceKind = 1
SignalDetectorResourceKind_ParallelSignalSupport: SignalDetectorResourceKind = 2
SignalDetectorResourceKind_ParallelSignalSupportForAgent: SignalDetectorResourceKind = 3
SignalDetectorResourceKind_DisplayOffSupport: SignalDetectorResourceKind = 4
SignalDetectorResourceKind_PluggedInPower: SignalDetectorResourceKind = 5
SignalDetectorResourceKind_Detector: SignalDetectorResourceKind = 6
SignalDetectorResourceKind_SupportedSleepState: SignalDetectorResourceKind = 7
SignalDetectorResourceKind_SupportedBatterySaverState: SignalDetectorResourceKind = 8
SignalDetectorResourceKind_ScreenAvailability: SignalDetectorResourceKind = 9
SignalDetectorResourceKind_InputHardware: SignalDetectorResourceKind = 10
SignalDetectorResourceKind_AcousticEchoCancellation: SignalDetectorResourceKind = 11
SignalDetectorResourceKind_ModelIdSupport: SignalDetectorResourceKind = 12
SignalDetectorResourceKind_DataChannel: SignalDetectorResourceKind = 13
make_head(_module, 'ActivationSignalDetectionConfiguration')
make_head(_module, 'ActivationSignalDetectionConfigurationCreationResult')
make_head(_module, 'ActivationSignalDetector')
make_head(_module, 'ConversationalAgentDetectorManager')
make_head(_module, 'ConversationalAgentSession')
make_head(_module, 'ConversationalAgentSessionInterruptedEventArgs')
make_head(_module, 'ConversationalAgentSignal')
make_head(_module, 'ConversationalAgentSignalDetectedEventArgs')
make_head(_module, 'ConversationalAgentSystemStateChangedEventArgs')
make_head(_module, 'DetectionConfigurationAvailabilityChangedEventArgs')
make_head(_module, 'DetectionConfigurationAvailabilityInfo')
make_head(_module, 'IActivationSignalDetectionConfiguration')
make_head(_module, 'IActivationSignalDetectionConfiguration2')
make_head(_module, 'IActivationSignalDetectionConfigurationCreationResult')
make_head(_module, 'IActivationSignalDetector')
make_head(_module, 'IActivationSignalDetector2')
make_head(_module, 'IConversationalAgentDetectorManager')
make_head(_module, 'IConversationalAgentDetectorManager2')
make_head(_module, 'IConversationalAgentDetectorManagerStatics')
make_head(_module, 'IConversationalAgentSession')
make_head(_module, 'IConversationalAgentSession2')
make_head(_module, 'IConversationalAgentSessionInterruptedEventArgs')
make_head(_module, 'IConversationalAgentSessionStatics')
make_head(_module, 'IConversationalAgentSignal')
make_head(_module, 'IConversationalAgentSignal2')
make_head(_module, 'IConversationalAgentSignalDetectedEventArgs')
make_head(_module, 'IConversationalAgentSystemStateChangedEventArgs')
make_head(_module, 'IDetectionConfigurationAvailabilityChangedEventArgs')
make_head(_module, 'IDetectionConfigurationAvailabilityInfo')
make_head(_module, 'IDetectionConfigurationAvailabilityInfo2')
