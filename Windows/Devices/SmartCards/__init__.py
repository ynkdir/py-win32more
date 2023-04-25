from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.SmartCards
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Cryptography.Core
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
class CardAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.CardAddedEventArgs'
    @winrt_mixinmethod
    def get_SmartCard(self: Windows.Devices.SmartCards.ICardAddedEventArgs) -> Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class CardRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.CardRemovedEventArgs'
    @winrt_mixinmethod
    def get_SmartCard(self: Windows.Devices.SmartCards.ICardRemovedEventArgs) -> Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class ICardAddedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('18bbef98-f18b-4dd3-b1-18-df-b2-c8-e2-3c-c6')
    @winrt_commethod(6)
    def get_SmartCard(self) -> Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class ICardRemovedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('15331aaf-22d7-4945-af-c9-03-b4-6f-42-a6-cd')
    @winrt_commethod(6)
    def get_SmartCard(self) -> Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class IKnownSmartCardAppletIds(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b04d8d8-95b4-4c88-8c-ea-41-1e-55-51-1e-fc')
    @winrt_commethod(6)
    def get_PaymentSystemEnvironment(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ProximityPaymentSystemEnvironment(self) -> Windows.Storage.Streams.IBuffer: ...
    PaymentSystemEnvironment = property(get_PaymentSystemEnvironment, None)
    ProximityPaymentSystemEnvironment = property(get_ProximityPaymentSystemEnvironment, None)
class ISmartCard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b718871-6434-43f4-b5-5a-6a-29-62-38-70-aa')
    @winrt_commethod(6)
    def get_Reader(self) -> Windows.Devices.SmartCards.SmartCardReader: ...
    @winrt_commethod(7)
    def GetStatusAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardStatus]: ...
    @winrt_commethod(8)
    def GetAnswerToResetAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    Reader = property(get_Reader, None)
class ISmartCardAppletIdGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7db165e6-6264-56f4-5e-03-c8-63-85-39-5e-b1')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AppletIds(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def get_SmartCardEmulationCategory(self) -> Windows.Devices.SmartCards.SmartCardEmulationCategory: ...
    @winrt_commethod(10)
    def put_SmartCardEmulationCategory(self, value: Windows.Devices.SmartCards.SmartCardEmulationCategory) -> Void: ...
    @winrt_commethod(11)
    def get_SmartCardEmulationType(self) -> Windows.Devices.SmartCards.SmartCardEmulationType: ...
    @winrt_commethod(12)
    def put_SmartCardEmulationType(self, value: Windows.Devices.SmartCards.SmartCardEmulationType) -> Void: ...
    @winrt_commethod(13)
    def get_AutomaticEnablement(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_AutomaticEnablement(self, value: Boolean) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    AppletIds = property(get_AppletIds, None)
    SmartCardEmulationCategory = property(get_SmartCardEmulationCategory, put_SmartCardEmulationCategory)
    SmartCardEmulationType = property(get_SmartCardEmulationType, put_SmartCardEmulationType)
    AutomaticEnablement = property(get_AutomaticEnablement, put_AutomaticEnablement)
class ISmartCardAppletIdGroup2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b0ef9dc-9956-4a62-8d-4e-d3-7a-68-eb-c3-a6')
    @winrt_commethod(6)
    def get_Logo(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_Logo(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(11)
    def get_SecureUserAuthenticationRequired(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SecureUserAuthenticationRequired(self, value: Boolean) -> Void: ...
    Logo = property(get_Logo, put_Logo)
    Description = property(get_Description, put_Description)
    Properties = property(get_Properties, None)
    SecureUserAuthenticationRequired = property(get_SecureUserAuthenticationRequired, put_SecureUserAuthenticationRequired)
class ISmartCardAppletIdGroupFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9105eb4d-4a65-4e41-80-61-cb-e8-3f-36-95-e5')
    @winrt_commethod(6)
    def Create(self, displayName: WinRT_String, appletIds: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IBuffer], emulationCategory: Windows.Devices.SmartCards.SmartCardEmulationCategory, emulationType: Windows.Devices.SmartCards.SmartCardEmulationType) -> Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
class ISmartCardAppletIdGroupRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df1208d1-31bb-5596-43-b1-6d-69-a0-25-7b-3a')
    @winrt_commethod(6)
    def get_ActivationPolicy(self) -> Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy: ...
    @winrt_commethod(7)
    def get_AppletIdGroup(self) -> Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_commethod(8)
    def RequestActivationPolicyChangeAsync(self, policy: Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardActivationPolicyChangeResult]: ...
    @winrt_commethod(9)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(10)
    def SetAutomaticResponseApdusAsync(self, apdus: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu]) -> Windows.Foundation.IAsyncAction: ...
    ActivationPolicy = property(get_ActivationPolicy, None)
    AppletIdGroup = property(get_AppletIdGroup, None)
    Id = property(get_Id, None)
class ISmartCardAppletIdGroupRegistration2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f5508d8-98a7-4f2e-91-d9-6c-fc-ce-da-40-7f')
    @winrt_commethod(6)
    def get_SmartCardReaderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetPropertiesAsync(self, props: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncAction: ...
    SmartCardReaderId = property(get_SmartCardReaderId, None)
class ISmartCardAppletIdGroupStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab2899a9-e76c-45cf-bf-1d-90-ea-a6-20-59-27')
    @winrt_commethod(6)
    def get_MaxAppletIds(self) -> UInt16: ...
    MaxAppletIds = property(get_MaxAppletIds, None)
class ISmartCardAutomaticResponseApdu(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52152bab-c63e-4531-a8-57-d7-56-d9-9b-98-6a')
    @winrt_commethod(6)
    def get_CommandApdu(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_CommandApdu(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_CommandApduBitMask(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_CommandApduBitMask(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_ShouldMatchLength(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_ShouldMatchLength(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_AppletId(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(13)
    def put_AppletId(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(14)
    def get_ResponseApdu(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(15)
    def put_ResponseApdu(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    CommandApdu = property(get_CommandApdu, put_CommandApdu)
    CommandApduBitMask = property(get_CommandApduBitMask, put_CommandApduBitMask)
    ShouldMatchLength = property(get_ShouldMatchLength, put_ShouldMatchLength)
    AppletId = property(get_AppletId, put_AppletId)
    ResponseApdu = property(get_ResponseApdu, put_ResponseApdu)
class ISmartCardAutomaticResponseApdu2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('44aebb14-559d-4531-4e-51-89-db-6f-a8-a5-7a')
    @winrt_commethod(6)
    def get_InputState(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_InputState(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(8)
    def get_OutputState(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def put_OutputState(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    InputState = property(get_InputState, put_InputState)
    OutputState = property(get_OutputState, put_OutputState)
class ISmartCardAutomaticResponseApdu3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bf43da74-6576-4392-93-67-fe-3b-c9-e2-d4-96')
    @winrt_commethod(6)
    def get_AllowWhenCryptogramGeneratorNotPrepared(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowWhenCryptogramGeneratorNotPrepared(self, value: Boolean) -> Void: ...
    AllowWhenCryptogramGeneratorNotPrepared = property(get_AllowWhenCryptogramGeneratorNotPrepared, put_AllowWhenCryptogramGeneratorNotPrepared)
class ISmartCardAutomaticResponseApduFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e97ea2fa-d02c-4c55-b0-2a-8c-ff-7f-a9-f0-5b')
    @winrt_commethod(6)
    def Create(self, commandApdu: Windows.Storage.Streams.IBuffer, responseApdu: Windows.Storage.Streams.IBuffer) -> Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu: ...
class ISmartCardChallengeContext(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('192a5319-c9c4-4947-81-cc-44-79-4a-61-ef-91')
    @winrt_commethod(6)
    def get_Challenge(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def VerifyResponseAsync(self, response: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ProvisionAsync(self, response: Windows.Storage.Streams.IBuffer, formatCard: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ProvisionAsyncWithNewCardId(self, response: Windows.Storage.Streams.IBuffer, formatCard: Boolean, newCardId: Guid) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ChangeAdministrativeKeyAsync(self, response: Windows.Storage.Streams.IBuffer, newAdministrativeKey: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    Challenge = property(get_Challenge, None)
class ISmartCardConnect(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2fdf87e5-028d-491e-a0-58-33-82-c3-98-6f-40')
    @winrt_commethod(6)
    def ConnectAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardConnection]: ...
class ISmartCardConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7edb991a-a81a-47bc-a6-49-15-6b-e6-b7-f2-31')
    @winrt_commethod(6)
    def TransmitAsync(self, command: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
class ISmartCardCryptogramGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e39f587b-edd3-4e49-b5-94-0f-f5-e4-d0-c7-6f')
    @winrt_commethod(6)
    def get_SupportedCryptogramMaterialTypes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]: ...
    @winrt_commethod(7)
    def get_SupportedCryptogramAlgorithms(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(8)
    def get_SupportedCryptogramMaterialPackageFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]: ...
    @winrt_commethod(9)
    def get_SupportedCryptogramMaterialPackageConfirmationResponseFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_commethod(10)
    def get_SupportedSmartCardCryptogramStorageKeyCapabilities(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]: ...
    @winrt_commethod(11)
    def DeleteCryptogramMaterialStorageKeyAsync(self, storageKeyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(12)
    def CreateCryptogramMaterialStorageKeyAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, algorithm: Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm, capabilities: Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(13)
    def RequestCryptogramMaterialStorageKeyInfoAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, format: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo]: ...
    @winrt_commethod(14)
    def ImportCryptogramMaterialPackageAsync(self, format: Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat, storageKeyName: WinRT_String, materialPackageName: WinRT_String, cryptogramMaterialPackage: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(15)
    def TryProvePossessionOfCryptogramMaterialPackageAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, responseFormat: Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat, materialPackageName: WinRT_String, materialName: WinRT_String, challenge: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof]: ...
    @winrt_commethod(16)
    def RequestUnlockCryptogramMaterialForUseAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(17)
    def DeleteCryptogramMaterialPackageAsync(self, materialPackageName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    SupportedCryptogramMaterialTypes = property(get_SupportedCryptogramMaterialTypes, None)
    SupportedCryptogramAlgorithms = property(get_SupportedCryptogramAlgorithms, None)
    SupportedCryptogramMaterialPackageFormats = property(get_SupportedCryptogramMaterialPackageFormats, None)
    SupportedCryptogramMaterialPackageConfirmationResponseFormats = property(get_SupportedCryptogramMaterialPackageConfirmationResponseFormats, None)
    SupportedSmartCardCryptogramStorageKeyCapabilities = property(get_SupportedSmartCardCryptogramStorageKeyCapabilities, None)
class ISmartCardCryptogramGenerator2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7116aa34-5d6d-4b4a-96-a3-ef-a4-7d-2a-7e-25')
    @winrt_commethod(6)
    def ValidateRequestApduAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, apduToValidate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(7)
    def GetAllCryptogramStorageKeyCharacteristicsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult]: ...
    @winrt_commethod(8)
    def GetAllCryptogramMaterialPackageCharacteristicsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_commethod(9)
    def GetAllCryptogramMaterialPackageCharacteristicsWithStorageKeyAsync(self, storageKeyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_commethod(10)
    def GetAllCryptogramMaterialCharacteristicsAsync(self, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, materialPackageName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult]: ...
class ISmartCardCryptogramGeneratorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09933910-cb9c-4015-96-7d-52-34-f3-b0-29-00')
    @winrt_commethod(6)
    def GetSmartCardCryptogramGeneratorAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGenerator]: ...
class ISmartCardCryptogramGeneratorStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09bdf5e5-b4bd-4e23-a5-88-74-46-92-04-c1-28')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2798e029-d687-4c92-86-c6-39-9e-9a-0e-cb-09')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e6a8a5c-9773-46c4-a3-2f-b1-e5-43-15-9e-04')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8c7ce857-a7e7-489d-b9-d6-36-80-61-51-50-12')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramMaterialCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc9ac5cc-c1d7-4153-92-3b-a2-d4-3c-6c-8d-49')
    @winrt_commethod(6)
    def get_MaterialName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AllowedAlgorithms(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(8)
    def get_AllowedProofOfPossessionAlgorithms(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_commethod(9)
    def get_AllowedValidations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(10)
    def get_MaterialType(self) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialType: ...
    @winrt_commethod(11)
    def get_ProtectionMethod(self) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialProtectionMethod: ...
    @winrt_commethod(12)
    def get_ProtectionVersion(self) -> Int32: ...
    @winrt_commethod(13)
    def get_MaterialLength(self) -> Int32: ...
    MaterialName = property(get_MaterialName, None)
    AllowedAlgorithms = property(get_AllowedAlgorithms, None)
    AllowedProofOfPossessionAlgorithms = property(get_AllowedProofOfPossessionAlgorithms, None)
    AllowedValidations = property(get_AllowedValidations, None)
    MaterialType = property(get_MaterialType, None)
    ProtectionMethod = property(get_ProtectionMethod, None)
    ProtectionVersion = property(get_ProtectionVersion, None)
    MaterialLength = property(get_MaterialLength, None)
class ISmartCardCryptogramMaterialPackageCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ffb58e1f-0692-4c47-93-cf-34-d9-1f-9d-cd-00')
    @winrt_commethod(6)
    def get_PackageName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_StorageKeyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DateImported(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_PackageFormat(self) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat: ...
    PackageName = property(get_PackageName, None)
    StorageKeyName = property(get_StorageKeyName, None)
    DateImported = property(get_DateImported, None)
    PackageFormat = property(get_PackageFormat, None)
class ISmartCardCryptogramMaterialPossessionProof(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5b9ab8c-a141-4135-9a-dd-b0-d2-e3-aa-1f-c9')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Proof(self) -> Windows.Storage.Streams.IBuffer: ...
    OperationStatus = property(get_OperationStatus, None)
    Proof = property(get_Proof, None)
class ISmartCardCryptogramPlacementStep(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('947b03eb-8342-4792-a2-e5-92-56-36-37-8a-53')
    @winrt_commethod(6)
    def get_Algorithm(self) -> Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm: ...
    @winrt_commethod(7)
    def put_Algorithm(self, value: Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm) -> Void: ...
    @winrt_commethod(8)
    def get_SourceData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_SourceData(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_CryptogramMaterialPackageName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CryptogramMaterialPackageName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_CryptogramMaterialName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CryptogramMaterialName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_TemplateOffset(self) -> Int32: ...
    @winrt_commethod(15)
    def put_TemplateOffset(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_CryptogramOffset(self) -> Int32: ...
    @winrt_commethod(17)
    def put_CryptogramOffset(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_CryptogramLength(self) -> Int32: ...
    @winrt_commethod(19)
    def put_CryptogramLength(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_CryptogramPlacementOptions(self) -> Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions: ...
    @winrt_commethod(21)
    def put_CryptogramPlacementOptions(self, value: Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions) -> Void: ...
    @winrt_commethod(22)
    def get_ChainedOutputStep(self) -> Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_commethod(23)
    def put_ChainedOutputStep(self, value: Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep) -> Void: ...
    Algorithm = property(get_Algorithm, put_Algorithm)
    SourceData = property(get_SourceData, put_SourceData)
    CryptogramMaterialPackageName = property(get_CryptogramMaterialPackageName, put_CryptogramMaterialPackageName)
    CryptogramMaterialName = property(get_CryptogramMaterialName, put_CryptogramMaterialName)
    TemplateOffset = property(get_TemplateOffset, put_TemplateOffset)
    CryptogramOffset = property(get_CryptogramOffset, put_CryptogramOffset)
    CryptogramLength = property(get_CryptogramLength, put_CryptogramLength)
    CryptogramPlacementOptions = property(get_CryptogramPlacementOptions, put_CryptogramPlacementOptions)
    ChainedOutputStep = property(get_ChainedOutputStep, put_ChainedOutputStep)
class ISmartCardCryptogramStorageKeyCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8552546e-4457-4825-b4-64-63-54-71-a3-9f-5c')
    @winrt_commethod(6)
    def get_StorageKeyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DateCreated(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Algorithm(self) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm: ...
    @winrt_commethod(9)
    def get_Capabilities(self) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    StorageKeyName = property(get_StorageKeyName, None)
    DateCreated = property(get_DateCreated, None)
    Algorithm = property(get_Algorithm, None)
    Capabilities = property(get_Capabilities, None)
class ISmartCardCryptogramStorageKeyInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('77b0f00d-b097-4f61-a2-6a-95-61-63-9c-9c-3a')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_PublicKeyBlobType(self) -> Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType: ...
    @winrt_commethod(8)
    def get_PublicKey(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_AttestationStatus(self) -> Windows.Devices.SmartCards.SmartCardCryptographicKeyAttestationStatus: ...
    @winrt_commethod(10)
    def get_Attestation(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def get_AttestationCertificateChain(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Capabilities(self) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    OperationStatus = property(get_OperationStatus, None)
    PublicKeyBlobType = property(get_PublicKeyBlobType, None)
    PublicKey = property(get_PublicKey, None)
    AttestationStatus = property(get_AttestationStatus, None)
    Attestation = property(get_Attestation, None)
    AttestationCertificateChain = property(get_AttestationCertificateChain, None)
    Capabilities = property(get_Capabilities, None)
class ISmartCardCryptogramStorageKeyInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('000440f9-f7fd-417d-89-e1-fb-b0-38-2a-dc-4d')
    @winrt_commethod(6)
    def get_OperationalRequirements(self) -> WinRT_String: ...
    OperationalRequirements = property(get_OperationalRequirements, None)
class ISmartCardEmulator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dfb906b2-875e-47e5-80-77-e8-bf-f1-b1-c6-fb')
    @winrt_commethod(6)
    def get_EnablementPolicy(self) -> Windows.Devices.SmartCards.SmartCardEmulatorEnablementPolicy: ...
    EnablementPolicy = property(get_EnablementPolicy, None)
class ISmartCardEmulator2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe3fc0b8-8529-411a-80-7b-48-ed-c2-a0-ab-44')
    @winrt_commethod(6)
    def add_ApduReceived(self, value: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardEmulator, Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ApduReceived(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ConnectionDeactivated(self, value: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardEmulator, Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ConnectionDeactivated(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
    @winrt_commethod(11)
    def IsHostCardEmulationSupported(self) -> Boolean: ...
class ISmartCardEmulatorApduReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d55d1576-69d2-5333-5b-5f-f8-c0-d6-e9-f0-9f')
    @winrt_commethod(6)
    def get_CommandApdu(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ConnectionProperties(self) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_commethod(8)
    def TryRespondAsync(self, responseApdu: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def get_AutomaticResponseStatus(self) -> Windows.Devices.SmartCards.SmartCardAutomaticResponseStatus: ...
    CommandApdu = property(get_CommandApdu, None)
    ConnectionProperties = property(get_ConnectionProperties, None)
    AutomaticResponseStatus = property(get_AutomaticResponseStatus, None)
class ISmartCardEmulatorApduReceivedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8bf93df0-22e1-4238-86-10-94-ce-4a-96-54-25')
    @winrt_commethod(6)
    def get_State(self) -> UInt32: ...
    @winrt_commethod(7)
    def TryRespondWithStateAsync(self, responseApdu: Windows.Storage.Streams.IBuffer, nextState: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    State = property(get_State, None)
class ISmartCardEmulatorApduReceivedEventArgsWithCryptograms(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d550bac7-b7bf-4e29-92-94-0c-4a-c3-c9-41-bd')
    @winrt_commethod(6)
    def TryRespondWithCryptogramsAsync(self, responseTemplate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(7)
    def TryRespondWithCryptogramsAndStateAsync(self, responseTemplate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep], nextState: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
class ISmartCardEmulatorConnectionDeactivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2186d8d3-c5eb-5262-43-df-62-a0-a1-b5-55-57')
    @winrt_commethod(6)
    def get_ConnectionProperties(self) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_commethod(7)
    def get_Reason(self) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedReason: ...
    ConnectionProperties = property(get_ConnectionProperties, None)
    Reason = property(get_Reason, None)
class ISmartCardEmulatorConnectionProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e2ca5ee-f969-507d-6c-f9-34-e2-d1-8d-f3-11')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Source(self) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
class ISmartCardEmulatorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a9bfc4b-c4d3-494f-b8-a2-62-15-d8-1e-85-b2')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardEmulator]: ...
class ISmartCardEmulatorStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69ae9f8a-b775-488b-84-36-6c-1e-28-ed-73-1f')
    @winrt_commethod(6)
    def GetAppletIdGroupRegistrationsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]]: ...
    @winrt_commethod(7)
    def RegisterAppletIdGroupAsync(self, appletIdGroup: Windows.Devices.SmartCards.SmartCardAppletIdGroup) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]: ...
    @winrt_commethod(8)
    def UnregisterAppletIdGroupAsync(self, registration: Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_MaxAppletIdGroupRegistrations(self) -> UInt16: ...
    MaxAppletIdGroupRegistrations = property(get_MaxAppletIdGroupRegistrations, None)
class ISmartCardEmulatorStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59ea142a-9f09-43f5-85-65-cf-a8-14-8e-4c-b2')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class ISmartCardPinPolicy(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('183ce184-4db6-4841-ac-9e-2a-c1-f3-9b-73-04')
    @winrt_commethod(6)
    def get_MinLength(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MinLength(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_MaxLength(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_MaxLength(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_UppercaseLetters(self) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(11)
    def put_UppercaseLetters(self, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(12)
    def get_LowercaseLetters(self) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(13)
    def put_LowercaseLetters(self, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(14)
    def get_Digits(self) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(15)
    def put_Digits(self, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(16)
    def get_SpecialCharacters(self) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(17)
    def put_SpecialCharacters(self, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    MinLength = property(get_MinLength, put_MinLength)
    MaxLength = property(get_MaxLength, put_MaxLength)
    UppercaseLetters = property(get_UppercaseLetters, put_UppercaseLetters)
    LowercaseLetters = property(get_LowercaseLetters, put_LowercaseLetters)
    Digits = property(get_Digits, put_Digits)
    SpecialCharacters = property(get_SpecialCharacters, put_SpecialCharacters)
class ISmartCardPinResetDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('18c94aac-7805-4004-85-e4-bb-ef-ac-8f-68-84')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISmartCardPinResetRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12fe3c4d-5fb9-4e8e-9f-f6-61-f4-75-12-4f-ef')
    @winrt_commethod(6)
    def get_Challenge(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Devices.SmartCards.SmartCardPinResetDeferral: ...
    @winrt_commethod(9)
    def SetResponse(self, response: Windows.Storage.Streams.IBuffer) -> Void: ...
    Challenge = property(get_Challenge, None)
    Deadline = property(get_Deadline, None)
class ISmartCardProvisioning(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('19eeedbd-1fab-477c-b7-12-1a-2c-5a-f1-fd-6e')
    @winrt_commethod(6)
    def get_SmartCard(self) -> Windows.Devices.SmartCards.SmartCard: ...
    @winrt_commethod(7)
    def GetIdAsync(self) -> Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_commethod(8)
    def GetNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(9)
    def GetChallengeContextAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardChallengeContext]: ...
    @winrt_commethod(10)
    def RequestPinChangeAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestPinResetAsync(self, handler: Windows.Devices.SmartCards.SmartCardPinResetHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SmartCard = property(get_SmartCard, None)
class ISmartCardProvisioning2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('10fd28eb-3f79-4b66-9b-7c-11-c1-49-b7-d0-bc')
    @winrt_commethod(6)
    def GetAuthorityKeyContainerNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ISmartCardProvisioningStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('13882848-0d13-4e70-97-35-51-da-ec-a5-25-4f')
    @winrt_commethod(6)
    def FromSmartCardAsync(self, card: Windows.Devices.SmartCards.SmartCard) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(7)
    def RequestVirtualSmartCardCreationAsync(self, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(8)
    def RequestVirtualSmartCardCreationAsyncWithCardId(self, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(9)
    def RequestVirtualSmartCardDeletionAsync(self, card: Windows.Devices.SmartCards.SmartCard) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISmartCardProvisioningStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3447c6a8-c9a0-4bd6-b5-0d-25-1f-4e-8d-3a-62')
    @winrt_commethod(6)
    def RequestAttestedVirtualSmartCardCreationAsync(self, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(7)
    def RequestAttestedVirtualSmartCardCreationAsyncWithCardId(self, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
class ISmartCardReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1074b4e0-54c2-4df0-81-7a-14-c1-43-78-f0-6c')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> Windows.Devices.SmartCards.SmartCardReaderKind: ...
    @winrt_commethod(9)
    def GetStatusAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardReaderStatus]: ...
    @winrt_commethod(10)
    def FindAllCardsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCard]]: ...
    @winrt_commethod(11)
    def add_CardAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardReader, Windows.Devices.SmartCards.CardAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_CardAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_CardRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardReader, Windows.Devices.SmartCards.CardRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_CardRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
class ISmartCardReaderStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('103c04e1-a1ca-48f2-a2-81-5b-6f-66-9a-f1-07')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorWithKind(self, kind: Windows.Devices.SmartCards.SmartCardReaderKind) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardReader]: ...
class ISmartCardTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f9bf11e-39ef-4f2b-b4-4f-0a-91-55-b1-77-bc')
    @winrt_commethod(6)
    def get_TriggerType(self) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    @winrt_commethod(7)
    def get_SourceAppletId(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_TriggerData(self) -> Windows.Storage.Streams.IBuffer: ...
    TriggerType = property(get_TriggerType, None)
    SourceAppletId = property(get_SourceAppletId, None)
    TriggerData = property(get_TriggerData, None)
class ISmartCardTriggerDetails2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2945c569-8975-4a51-9e-1a-5f-8a-76-ee-51-af')
    @winrt_commethod(6)
    def get_Emulator(self) -> Windows.Devices.SmartCards.SmartCardEmulator: ...
    @winrt_commethod(7)
    def TryLaunchCurrentAppAsync(self, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryLaunchCurrentAppWithBehaviorAsync(self, arguments: WinRT_String, behavior: Windows.Devices.SmartCards.SmartCardLaunchBehavior) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Emulator = property(get_Emulator, None)
class ISmartCardTriggerDetails3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b3e2c27d-18c6-4ba8-83-76-ef-03-d4-91-26-66')
    @winrt_commethod(6)
    def get_SmartCard(self) -> Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class KnownSmartCardAppletIds(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.KnownSmartCardAppletIds'
    @winrt_classmethod
    def get_PaymentSystemEnvironment(cls: Windows.Devices.SmartCards.IKnownSmartCardAppletIds) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def get_ProximityPaymentSystemEnvironment(cls: Windows.Devices.SmartCards.IKnownSmartCardAppletIds) -> Windows.Storage.Streams.IBuffer: ...
    PaymentSystemEnvironment = property(get_PaymentSystemEnvironment, None)
    ProximityPaymentSystemEnvironment = property(get_ProximityPaymentSystemEnvironment, None)
class SmartCard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCard'
    @winrt_mixinmethod
    def get_Reader(self: Windows.Devices.SmartCards.ISmartCard) -> Windows.Devices.SmartCards.SmartCardReader: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: Windows.Devices.SmartCards.ISmartCard) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardStatus]: ...
    @winrt_mixinmethod
    def GetAnswerToResetAsync(self: Windows.Devices.SmartCards.ISmartCard) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def ConnectAsync(self: Windows.Devices.SmartCards.ISmartCardConnect) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardConnection]: ...
    Reader = property(get_Reader, None)
SmartCardActivationPolicyChangeResult = Int32
SmartCardActivationPolicyChangeResult_Denied: SmartCardActivationPolicyChangeResult = 0
SmartCardActivationPolicyChangeResult_Allowed: SmartCardActivationPolicyChangeResult = 1
class SmartCardAppletIdGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardAppletIdGroup'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.SmartCards.ISmartCardAppletIdGroupFactory, displayName: WinRT_String, appletIds: Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IBuffer], emulationCategory: Windows.Devices.SmartCards.SmartCardEmulationCategory, emulationType: Windows.Devices.SmartCards.SmartCardEmulationType) -> Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppletIds(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_SmartCardEmulationCategory(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> Windows.Devices.SmartCards.SmartCardEmulationCategory: ...
    @winrt_mixinmethod
    def put_SmartCardEmulationCategory(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: Windows.Devices.SmartCards.SmartCardEmulationCategory) -> Void: ...
    @winrt_mixinmethod
    def get_SmartCardEmulationType(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> Windows.Devices.SmartCards.SmartCardEmulationType: ...
    @winrt_mixinmethod
    def put_SmartCardEmulationType(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: Windows.Devices.SmartCards.SmartCardEmulationType) -> Void: ...
    @winrt_mixinmethod
    def get_AutomaticEnablement(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutomaticEnablement(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Logo(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Logo(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_SecureUserAuthenticationRequired(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> Boolean: ...
    @winrt_mixinmethod
    def put_SecureUserAuthenticationRequired(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_MaxAppletIds(cls: Windows.Devices.SmartCards.ISmartCardAppletIdGroupStatics) -> UInt16: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    AppletIds = property(get_AppletIds, None)
    SmartCardEmulationCategory = property(get_SmartCardEmulationCategory, put_SmartCardEmulationCategory)
    SmartCardEmulationType = property(get_SmartCardEmulationType, put_SmartCardEmulationType)
    AutomaticEnablement = property(get_AutomaticEnablement, put_AutomaticEnablement)
    Logo = property(get_Logo, put_Logo)
    Description = property(get_Description, put_Description)
    Properties = property(get_Properties, None)
    SecureUserAuthenticationRequired = property(get_SecureUserAuthenticationRequired, put_SecureUserAuthenticationRequired)
    MaxAppletIds = property(get_MaxAppletIds, None)
SmartCardAppletIdGroupActivationPolicy = Int32
SmartCardAppletIdGroupActivationPolicy_Disabled: SmartCardAppletIdGroupActivationPolicy = 0
SmartCardAppletIdGroupActivationPolicy_ForegroundOverride: SmartCardAppletIdGroupActivationPolicy = 1
SmartCardAppletIdGroupActivationPolicy_Enabled: SmartCardAppletIdGroupActivationPolicy = 2
class SmartCardAppletIdGroupRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration'
    @winrt_mixinmethod
    def get_ActivationPolicy(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy: ...
    @winrt_mixinmethod
    def get_AppletIdGroup(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_mixinmethod
    def RequestActivationPolicyChangeAsync(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration, policy: Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardActivationPolicyChangeResult]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> Guid: ...
    @winrt_mixinmethod
    def SetAutomaticResponseApdusAsync(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration, apdus: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_SmartCardReaderId(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPropertiesAsync(self: Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration2, props: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncAction: ...
    ActivationPolicy = property(get_ActivationPolicy, None)
    AppletIdGroup = property(get_AppletIdGroup, None)
    Id = property(get_Id, None)
    SmartCardReaderId = property(get_SmartCardReaderId, None)
class SmartCardAutomaticResponseApdu(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApduFactory, commandApdu: Windows.Storage.Streams.IBuffer, responseApdu: Windows.Storage.Streams.IBuffer) -> Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu: ...
    @winrt_mixinmethod
    def get_CommandApdu(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CommandApdu(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_CommandApduBitMask(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CommandApduBitMask(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldMatchLength(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldMatchLength(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppletId(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_AppletId(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseApdu(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ResponseApdu(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_InputState(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_InputState(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_OutputState(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_OutputState(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowWhenCryptogramGeneratorNotPrepared(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu3) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowWhenCryptogramGeneratorNotPrepared(self: Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu3, value: Boolean) -> Void: ...
    CommandApdu = property(get_CommandApdu, put_CommandApdu)
    CommandApduBitMask = property(get_CommandApduBitMask, put_CommandApduBitMask)
    ShouldMatchLength = property(get_ShouldMatchLength, put_ShouldMatchLength)
    AppletId = property(get_AppletId, put_AppletId)
    ResponseApdu = property(get_ResponseApdu, put_ResponseApdu)
    InputState = property(get_InputState, put_InputState)
    OutputState = property(get_OutputState, put_OutputState)
    AllowWhenCryptogramGeneratorNotPrepared = property(get_AllowWhenCryptogramGeneratorNotPrepared, put_AllowWhenCryptogramGeneratorNotPrepared)
SmartCardAutomaticResponseStatus = Int32
SmartCardAutomaticResponseStatus_None: SmartCardAutomaticResponseStatus = 0
SmartCardAutomaticResponseStatus_Success: SmartCardAutomaticResponseStatus = 1
SmartCardAutomaticResponseStatus_UnknownError: SmartCardAutomaticResponseStatus = 2
SmartCardBackgroundTriggerContract: UInt32 = 196608
class SmartCardChallengeContext(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardChallengeContext'
    @winrt_mixinmethod
    def get_Challenge(self: Windows.Devices.SmartCards.ISmartCardChallengeContext) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def VerifyResponseAsync(self: Windows.Devices.SmartCards.ISmartCardChallengeContext, response: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ProvisionAsync(self: Windows.Devices.SmartCards.ISmartCardChallengeContext, response: Windows.Storage.Streams.IBuffer, formatCard: Boolean) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ProvisionAsyncWithNewCardId(self: Windows.Devices.SmartCards.ISmartCardChallengeContext, response: Windows.Storage.Streams.IBuffer, formatCard: Boolean, newCardId: Guid) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ChangeAdministrativeKeyAsync(self: Windows.Devices.SmartCards.ISmartCardChallengeContext, response: Windows.Storage.Streams.IBuffer, newAdministrativeKey: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Challenge = property(get_Challenge, None)
class SmartCardConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardConnection'
    @winrt_mixinmethod
    def TransmitAsync(self: Windows.Devices.SmartCards.ISmartCardConnection, command: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
SmartCardCryptogramAlgorithm = Int32
SmartCardCryptogramAlgorithm_None: SmartCardCryptogramAlgorithm = 0
SmartCardCryptogramAlgorithm_CbcMac: SmartCardCryptogramAlgorithm = 1
SmartCardCryptogramAlgorithm_Cvc3Umd: SmartCardCryptogramAlgorithm = 2
SmartCardCryptogramAlgorithm_DecimalizedMsd: SmartCardCryptogramAlgorithm = 3
SmartCardCryptogramAlgorithm_Cvc3MD: SmartCardCryptogramAlgorithm = 4
SmartCardCryptogramAlgorithm_Sha1: SmartCardCryptogramAlgorithm = 5
SmartCardCryptogramAlgorithm_SignedDynamicApplicationData: SmartCardCryptogramAlgorithm = 6
SmartCardCryptogramAlgorithm_RsaPkcs1: SmartCardCryptogramAlgorithm = 7
SmartCardCryptogramAlgorithm_Sha256Hmac: SmartCardCryptogramAlgorithm = 8
class SmartCardCryptogramGenerator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramGenerator'
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialTypes(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramAlgorithms(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialPackageFormats(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialPackageConfirmationResponseFormats(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_mixinmethod
    def get_SupportedSmartCardCryptogramStorageKeyCapabilities(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]: ...
    @winrt_mixinmethod
    def DeleteCryptogramMaterialStorageKeyAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, storageKeyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def CreateCryptogramMaterialStorageKeyAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, algorithm: Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm, capabilities: Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def RequestCryptogramMaterialStorageKeyInfoAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, format: Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo]: ...
    @winrt_mixinmethod
    def ImportCryptogramMaterialPackageAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, format: Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat, storageKeyName: WinRT_String, materialPackageName: WinRT_String, cryptogramMaterialPackage: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def TryProvePossessionOfCryptogramMaterialPackageAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, responseFormat: Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat, materialPackageName: WinRT_String, materialName: WinRT_String, challenge: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof]: ...
    @winrt_mixinmethod
    def RequestUnlockCryptogramMaterialForUseAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def DeleteCryptogramMaterialPackageAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, materialPackageName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def ValidateRequestApduAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, apduToValidate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def GetAllCryptogramStorageKeyCharacteristicsAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialPackageCharacteristicsAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialPackageCharacteristicsWithStorageKeyAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, storageKeyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialCharacteristicsAsync(self: Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, promptingBehavior: Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, materialPackageName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult]: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetSmartCardCryptogramGeneratorAsync(cls: Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGenerator]: ...
    SupportedCryptogramMaterialTypes = property(get_SupportedCryptogramMaterialTypes, None)
    SupportedCryptogramAlgorithms = property(get_SupportedCryptogramAlgorithms, None)
    SupportedCryptogramMaterialPackageFormats = property(get_SupportedCryptogramMaterialPackageFormats, None)
    SupportedCryptogramMaterialPackageConfirmationResponseFormats = property(get_SupportedCryptogramMaterialPackageConfirmationResponseFormats, None)
    SupportedSmartCardCryptogramStorageKeyCapabilities = property(get_SupportedSmartCardCryptogramStorageKeyCapabilities, None)
SmartCardCryptogramGeneratorOperationStatus = Int32
SmartCardCryptogramGeneratorOperationStatus_Success: SmartCardCryptogramGeneratorOperationStatus = 0
SmartCardCryptogramGeneratorOperationStatus_AuthorizationFailed: SmartCardCryptogramGeneratorOperationStatus = 1
SmartCardCryptogramGeneratorOperationStatus_AuthorizationCanceled: SmartCardCryptogramGeneratorOperationStatus = 2
SmartCardCryptogramGeneratorOperationStatus_AuthorizationRequired: SmartCardCryptogramGeneratorOperationStatus = 3
SmartCardCryptogramGeneratorOperationStatus_CryptogramMaterialPackageStorageKeyExists: SmartCardCryptogramGeneratorOperationStatus = 4
SmartCardCryptogramGeneratorOperationStatus_NoCryptogramMaterialPackageStorageKey: SmartCardCryptogramGeneratorOperationStatus = 5
SmartCardCryptogramGeneratorOperationStatus_NoCryptogramMaterialPackage: SmartCardCryptogramGeneratorOperationStatus = 6
SmartCardCryptogramGeneratorOperationStatus_UnsupportedCryptogramMaterialPackage: SmartCardCryptogramGeneratorOperationStatus = 7
SmartCardCryptogramGeneratorOperationStatus_UnknownCryptogramMaterialName: SmartCardCryptogramGeneratorOperationStatus = 8
SmartCardCryptogramGeneratorOperationStatus_InvalidCryptogramMaterialUsage: SmartCardCryptogramGeneratorOperationStatus = 9
SmartCardCryptogramGeneratorOperationStatus_ApduResponseNotSent: SmartCardCryptogramGeneratorOperationStatus = 10
SmartCardCryptogramGeneratorOperationStatus_OtherError: SmartCardCryptogramGeneratorOperationStatus = 11
SmartCardCryptogramGeneratorOperationStatus_ValidationFailed: SmartCardCryptogramGeneratorOperationStatus = 12
SmartCardCryptogramGeneratorOperationStatus_NotSupported: SmartCardCryptogramGeneratorOperationStatus = 13
class SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramMaterialCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics: ...
    @winrt_mixinmethod
    def get_MaterialName(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowedAlgorithms(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_AllowedProofOfPossessionAlgorithms(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_mixinmethod
    def get_AllowedValidations(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_MaterialType(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialType: ...
    @winrt_mixinmethod
    def get_ProtectionMethod(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialProtectionMethod: ...
    @winrt_mixinmethod
    def get_ProtectionVersion(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Int32: ...
    @winrt_mixinmethod
    def get_MaterialLength(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Int32: ...
    MaterialName = property(get_MaterialName, None)
    AllowedAlgorithms = property(get_AllowedAlgorithms, None)
    AllowedProofOfPossessionAlgorithms = property(get_AllowedProofOfPossessionAlgorithms, None)
    AllowedValidations = property(get_AllowedValidations, None)
    MaterialType = property(get_MaterialType, None)
    ProtectionMethod = property(get_ProtectionMethod, None)
    ProtectionVersion = property(get_ProtectionVersion, None)
    MaterialLength = property(get_MaterialLength, None)
class SmartCardCryptogramMaterialPackageCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics: ...
    @winrt_mixinmethod
    def get_PackageName(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StorageKeyName(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateImported(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PackageFormat(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat: ...
    PackageName = property(get_PackageName, None)
    StorageKeyName = property(get_StorageKeyName, None)
    DateImported = property(get_DateImported, None)
    PackageFormat = property(get_PackageFormat, None)
SmartCardCryptogramMaterialPackageConfirmationResponseFormat = Int32
SmartCardCryptogramMaterialPackageConfirmationResponseFormat_None: SmartCardCryptogramMaterialPackageConfirmationResponseFormat = 0
SmartCardCryptogramMaterialPackageConfirmationResponseFormat_VisaHmac: SmartCardCryptogramMaterialPackageConfirmationResponseFormat = 1
SmartCardCryptogramMaterialPackageFormat = Int32
SmartCardCryptogramMaterialPackageFormat_None: SmartCardCryptogramMaterialPackageFormat = 0
SmartCardCryptogramMaterialPackageFormat_JweRsaPki: SmartCardCryptogramMaterialPackageFormat = 1
class SmartCardCryptogramMaterialPossessionProof(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof'
    @winrt_mixinmethod
    def get_OperationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Proof(self: Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof) -> Windows.Storage.Streams.IBuffer: ...
    OperationStatus = property(get_OperationStatus, None)
    Proof = property(get_Proof, None)
SmartCardCryptogramMaterialProtectionMethod = Int32
SmartCardCryptogramMaterialProtectionMethod_None: SmartCardCryptogramMaterialProtectionMethod = 0
SmartCardCryptogramMaterialProtectionMethod_WhiteBoxing: SmartCardCryptogramMaterialProtectionMethod = 1
SmartCardCryptogramMaterialType = Int32
SmartCardCryptogramMaterialType_None: SmartCardCryptogramMaterialType = 0
SmartCardCryptogramMaterialType_StaticDataAuthentication: SmartCardCryptogramMaterialType = 1
SmartCardCryptogramMaterialType_TripleDes112: SmartCardCryptogramMaterialType = 2
SmartCardCryptogramMaterialType_Aes: SmartCardCryptogramMaterialType = 3
SmartCardCryptogramMaterialType_RsaPkcs1: SmartCardCryptogramMaterialType = 4
SmartCardCryptogramPlacementOptions = UInt32
SmartCardCryptogramPlacementOptions_None: SmartCardCryptogramPlacementOptions = 0
SmartCardCryptogramPlacementOptions_UnitsAreInNibbles: SmartCardCryptogramPlacementOptions = 1
SmartCardCryptogramPlacementOptions_ChainOutput: SmartCardCryptogramPlacementOptions = 2
class SmartCardCryptogramPlacementStep(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_mixinmethod
    def get_Algorithm(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm: ...
    @winrt_mixinmethod
    def put_Algorithm(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_SourceData(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SourceData(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramMaterialPackageName(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CryptogramMaterialPackageName(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramMaterialName(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CryptogramMaterialName(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TemplateOffset(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_TemplateOffset(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramOffset(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_CryptogramOffset(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramLength(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_CryptogramLength(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramPlacementOptions(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions: ...
    @winrt_mixinmethod
    def put_CryptogramPlacementOptions(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ChainedOutputStep(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_mixinmethod
    def put_ChainedOutputStep(self: Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep) -> Void: ...
    Algorithm = property(get_Algorithm, put_Algorithm)
    SourceData = property(get_SourceData, put_SourceData)
    CryptogramMaterialPackageName = property(get_CryptogramMaterialPackageName, put_CryptogramMaterialPackageName)
    CryptogramMaterialName = property(get_CryptogramMaterialName, put_CryptogramMaterialName)
    TemplateOffset = property(get_TemplateOffset, put_TemplateOffset)
    CryptogramOffset = property(get_CryptogramOffset, put_CryptogramOffset)
    CryptogramLength = property(get_CryptogramLength, put_CryptogramLength)
    CryptogramPlacementOptions = property(get_CryptogramPlacementOptions, put_CryptogramPlacementOptions)
    ChainedOutputStep = property(get_ChainedOutputStep, put_ChainedOutputStep)
SmartCardCryptogramStorageKeyAlgorithm = Int32
SmartCardCryptogramStorageKeyAlgorithm_None: SmartCardCryptogramStorageKeyAlgorithm = 0
SmartCardCryptogramStorageKeyAlgorithm_Rsa2048: SmartCardCryptogramStorageKeyAlgorithm = 1
SmartCardCryptogramStorageKeyCapabilities = UInt32
SmartCardCryptogramStorageKeyCapabilities_None: SmartCardCryptogramStorageKeyCapabilities = 0
SmartCardCryptogramStorageKeyCapabilities_HardwareProtection: SmartCardCryptogramStorageKeyCapabilities = 1
SmartCardCryptogramStorageKeyCapabilities_UnlockPrompt: SmartCardCryptogramStorageKeyCapabilities = 2
class SmartCardCryptogramStorageKeyCharacteristics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics: ...
    @winrt_mixinmethod
    def get_StorageKeyName(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateCreated(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Algorithm(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    StorageKeyName = property(get_StorageKeyName, None)
    DateCreated = property(get_DateCreated, None)
    Algorithm = property(get_Algorithm, None)
    Capabilities = property(get_Capabilities, None)
class SmartCardCryptogramStorageKeyInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo'
    @winrt_mixinmethod
    def get_OperationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_PublicKeyBlobType(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType: ...
    @winrt_mixinmethod
    def get_PublicKey(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationStatus(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Devices.SmartCards.SmartCardCryptographicKeyAttestationStatus: ...
    @winrt_mixinmethod
    def get_Attestation(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationCertificateChain(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    @winrt_mixinmethod
    def get_OperationalRequirements(self: Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo2) -> WinRT_String: ...
    OperationStatus = property(get_OperationStatus, None)
    PublicKeyBlobType = property(get_PublicKeyBlobType, None)
    PublicKey = property(get_PublicKey, None)
    AttestationStatus = property(get_AttestationStatus, None)
    Attestation = property(get_Attestation, None)
    AttestationCertificateChain = property(get_AttestationCertificateChain, None)
    Capabilities = property(get_Capabilities, None)
    OperationalRequirements = property(get_OperationalRequirements, None)
SmartCardCryptographicKeyAttestationStatus = Int32
SmartCardCryptographicKeyAttestationStatus_NoAttestation: SmartCardCryptographicKeyAttestationStatus = 0
SmartCardCryptographicKeyAttestationStatus_SoftwareKeyWithoutTpm: SmartCardCryptographicKeyAttestationStatus = 1
SmartCardCryptographicKeyAttestationStatus_SoftwareKeyWithTpm: SmartCardCryptographicKeyAttestationStatus = 2
SmartCardCryptographicKeyAttestationStatus_TpmKeyUnknownAttestationStatus: SmartCardCryptographicKeyAttestationStatus = 3
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithoutAttestationCapability: SmartCardCryptographicKeyAttestationStatus = 4
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithTemporaryAttestationFailure: SmartCardCryptographicKeyAttestationStatus = 5
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithLongTermAttestationFailure: SmartCardCryptographicKeyAttestationStatus = 6
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithAttestation: SmartCardCryptographicKeyAttestationStatus = 7
SmartCardEmulationCategory = Int32
SmartCardEmulationCategory_Other: SmartCardEmulationCategory = 0
SmartCardEmulationCategory_Payment: SmartCardEmulationCategory = 1
SmartCardEmulationType = Int32
SmartCardEmulationType_Host: SmartCardEmulationType = 0
SmartCardEmulationType_Uicc: SmartCardEmulationType = 1
SmartCardEmulationType_EmbeddedSE: SmartCardEmulationType = 2
class SmartCardEmulator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardEmulator'
    @winrt_mixinmethod
    def get_EnablementPolicy(self: Windows.Devices.SmartCards.ISmartCardEmulator) -> Windows.Devices.SmartCards.SmartCardEmulatorEnablementPolicy: ...
    @winrt_mixinmethod
    def add_ApduReceived(self: Windows.Devices.SmartCards.ISmartCardEmulator2, value: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardEmulator, Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ApduReceived(self: Windows.Devices.SmartCards.ISmartCardEmulator2, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionDeactivated(self: Windows.Devices.SmartCards.ISmartCardEmulator2, value: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardEmulator, Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionDeactivated(self: Windows.Devices.SmartCards.ISmartCardEmulator2, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.SmartCards.ISmartCardEmulator2) -> Void: ...
    @winrt_mixinmethod
    def IsHostCardEmulationSupported(self: Windows.Devices.SmartCards.ISmartCardEmulator2) -> Boolean: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics3) -> Boolean: ...
    @winrt_classmethod
    def GetAppletIdGroupRegistrationsAsync(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics2) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]]: ...
    @winrt_classmethod
    def RegisterAppletIdGroupAsync(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics2, appletIdGroup: Windows.Devices.SmartCards.SmartCardAppletIdGroup) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]: ...
    @winrt_classmethod
    def UnregisterAppletIdGroupAsync(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics2, registration: Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_MaxAppletIdGroupRegistrations(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics2) -> UInt16: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.SmartCards.ISmartCardEmulatorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardEmulator]: ...
    EnablementPolicy = property(get_EnablementPolicy, None)
    MaxAppletIdGroupRegistrations = property(get_MaxAppletIdGroupRegistrations, None)
class SmartCardEmulatorApduReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs'
    @winrt_mixinmethod
    def get_CommandApdu(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ConnectionProperties(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_mixinmethod
    def TryRespondAsync(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs, responseApdu: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AutomaticResponseStatus(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> Windows.Devices.SmartCards.SmartCardAutomaticResponseStatus: ...
    @winrt_mixinmethod
    def TryRespondWithCryptogramsAsync(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgsWithCryptograms, responseTemplate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def TryRespondWithCryptogramsAndStateAsync(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgsWithCryptograms, responseTemplate: Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: Windows.Foundation.Collections.IIterable[Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep], nextState: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def TryRespondWithStateAsync(self: Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs2, responseApdu: Windows.Storage.Streams.IBuffer, nextState: Windows.Foundation.IReference[UInt32]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    CommandApdu = property(get_CommandApdu, None)
    ConnectionProperties = property(get_ConnectionProperties, None)
    AutomaticResponseStatus = property(get_AutomaticResponseStatus, None)
    State = property(get_State, None)
class SmartCardEmulatorConnectionDeactivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionProperties(self: Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedReason: ...
    ConnectionProperties = property(get_ConnectionProperties, None)
    Reason = property(get_Reason, None)
SmartCardEmulatorConnectionDeactivatedReason = Int32
SmartCardEmulatorConnectionDeactivatedReason_ConnectionLost: SmartCardEmulatorConnectionDeactivatedReason = 0
SmartCardEmulatorConnectionDeactivatedReason_ConnectionRedirected: SmartCardEmulatorConnectionDeactivatedReason = 1
class SmartCardEmulatorConnectionProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties) -> Guid: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties) -> Windows.Devices.SmartCards.SmartCardEmulatorConnectionSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
SmartCardEmulatorConnectionSource = Int32
SmartCardEmulatorConnectionSource_Unknown: SmartCardEmulatorConnectionSource = 0
SmartCardEmulatorConnectionSource_NfcReader: SmartCardEmulatorConnectionSource = 1
SmartCardEmulatorContract: UInt32 = 393216
SmartCardEmulatorEnablementPolicy = Int32
SmartCardEmulatorEnablementPolicy_Never: SmartCardEmulatorEnablementPolicy = 0
SmartCardEmulatorEnablementPolicy_Always: SmartCardEmulatorEnablementPolicy = 1
SmartCardEmulatorEnablementPolicy_ScreenOn: SmartCardEmulatorEnablementPolicy = 2
SmartCardEmulatorEnablementPolicy_ScreenUnlocked: SmartCardEmulatorEnablementPolicy = 3
SmartCardLaunchBehavior = Int32
SmartCardLaunchBehavior_Default: SmartCardLaunchBehavior = 0
SmartCardLaunchBehavior_AboveLock: SmartCardLaunchBehavior = 1
SmartCardPinCharacterPolicyOption = Int32
SmartCardPinCharacterPolicyOption_Allow: SmartCardPinCharacterPolicyOption = 0
SmartCardPinCharacterPolicyOption_RequireAtLeastOne: SmartCardPinCharacterPolicyOption = 1
SmartCardPinCharacterPolicyOption_Disallow: SmartCardPinCharacterPolicyOption = 2
class SmartCardPinPolicy(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardPinPolicy'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.SmartCards.SmartCardPinPolicy: ...
    @winrt_mixinmethod
    def get_MinLength(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> UInt32: ...
    @winrt_mixinmethod
    def put_MinLength(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxLength(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxLength(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_UppercaseLetters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_UppercaseLetters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_LowercaseLetters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_LowercaseLetters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_Digits(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_Digits(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_SpecialCharacters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy) -> Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_SpecialCharacters(self: Windows.Devices.SmartCards.ISmartCardPinPolicy, value: Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    MinLength = property(get_MinLength, put_MinLength)
    MaxLength = property(get_MaxLength, put_MaxLength)
    UppercaseLetters = property(get_UppercaseLetters, put_UppercaseLetters)
    LowercaseLetters = property(get_LowercaseLetters, put_LowercaseLetters)
    Digits = property(get_Digits, put_Digits)
    SpecialCharacters = property(get_SpecialCharacters, put_SpecialCharacters)
class SmartCardPinResetDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardPinResetDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Devices.SmartCards.ISmartCardPinResetDeferral) -> Void: ...
class SmartCardPinResetHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('138d5e40-f3bc-4a5c-b4-1d-4b-4e-f6-84-e2-37')
    ClassId = 'Windows.Devices.SmartCards.SmartCardPinResetHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Devices.SmartCards.SmartCardProvisioning, request: Windows.Devices.SmartCards.SmartCardPinResetRequest) -> Void: ...
class SmartCardPinResetRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardPinResetRequest'
    @winrt_mixinmethod
    def get_Challenge(self: Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> Windows.Devices.SmartCards.SmartCardPinResetDeferral: ...
    @winrt_mixinmethod
    def SetResponse(self: Windows.Devices.SmartCards.ISmartCardPinResetRequest, response: Windows.Storage.Streams.IBuffer) -> Void: ...
    Challenge = property(get_Challenge, None)
    Deadline = property(get_Deadline, None)
class SmartCardProvisioning(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardProvisioning'
    @winrt_mixinmethod
    def get_SmartCard(self: Windows.Devices.SmartCards.ISmartCardProvisioning) -> Windows.Devices.SmartCards.SmartCard: ...
    @winrt_mixinmethod
    def GetIdAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning) -> Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_mixinmethod
    def GetNameAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetChallengeContextAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardChallengeContext]: ...
    @winrt_mixinmethod
    def RequestPinChangeAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinResetAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning, handler: Windows.Devices.SmartCards.SmartCardPinResetHandler) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetAuthorityKeyContainerNameAsync(self: Windows.Devices.SmartCards.ISmartCardProvisioning2) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestAttestedVirtualSmartCardCreationAsync(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics2, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestAttestedVirtualSmartCardCreationAsyncWithCardId(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics2, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def FromSmartCardAsync(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics, card: Windows.Devices.SmartCards.SmartCard) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardCreationAsync(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardCreationAsyncWithCardId(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics, friendlyName: WinRT_String, administrativeKey: Windows.Storage.Streams.IBuffer, pinPolicy: Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardDeletionAsync(cls: Windows.Devices.SmartCards.ISmartCardProvisioningStatics, card: Windows.Devices.SmartCards.SmartCard) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SmartCard = property(get_SmartCard, None)
class SmartCardReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardReader'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.SmartCards.ISmartCardReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.SmartCards.ISmartCardReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Devices.SmartCards.ISmartCardReader) -> Windows.Devices.SmartCards.SmartCardReaderKind: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: Windows.Devices.SmartCards.ISmartCardReader) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardReaderStatus]: ...
    @winrt_mixinmethod
    def FindAllCardsAsync(self: Windows.Devices.SmartCards.ISmartCardReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.SmartCards.SmartCard]]: ...
    @winrt_mixinmethod
    def add_CardAdded(self: Windows.Devices.SmartCards.ISmartCardReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardReader, Windows.Devices.SmartCards.CardAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CardAdded(self: Windows.Devices.SmartCards.ISmartCardReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CardRemoved(self: Windows.Devices.SmartCards.ISmartCardReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.SmartCards.SmartCardReader, Windows.Devices.SmartCards.CardRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CardRemoved(self: Windows.Devices.SmartCards.ISmartCardReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.SmartCards.ISmartCardReaderStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorWithKind(cls: Windows.Devices.SmartCards.ISmartCardReaderStatics, kind: Windows.Devices.SmartCards.SmartCardReaderKind) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.SmartCards.ISmartCardReaderStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.SmartCards.SmartCardReader]: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
SmartCardReaderKind = Int32
SmartCardReaderKind_Any: SmartCardReaderKind = 0
SmartCardReaderKind_Generic: SmartCardReaderKind = 1
SmartCardReaderKind_Tpm: SmartCardReaderKind = 2
SmartCardReaderKind_Nfc: SmartCardReaderKind = 3
SmartCardReaderKind_Uicc: SmartCardReaderKind = 4
SmartCardReaderKind_EmbeddedSE: SmartCardReaderKind = 5
SmartCardReaderStatus = Int32
SmartCardReaderStatus_Disconnected: SmartCardReaderStatus = 0
SmartCardReaderStatus_Ready: SmartCardReaderStatus = 1
SmartCardReaderStatus_Exclusive: SmartCardReaderStatus = 2
SmartCardStatus = Int32
SmartCardStatus_Disconnected: SmartCardStatus = 0
SmartCardStatus_Ready: SmartCardStatus = 1
SmartCardStatus_Shared: SmartCardStatus = 2
SmartCardStatus_Exclusive: SmartCardStatus = 3
SmartCardStatus_Unresponsive: SmartCardStatus = 4
class SmartCardTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.SmartCards.SmartCardTriggerDetails'
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    @winrt_mixinmethod
    def get_SourceAppletId(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_TriggerData(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Emulator(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails2) -> Windows.Devices.SmartCards.SmartCardEmulator: ...
    @winrt_mixinmethod
    def TryLaunchCurrentAppAsync(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails2, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryLaunchCurrentAppWithBehaviorAsync(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails2, arguments: WinRT_String, behavior: Windows.Devices.SmartCards.SmartCardLaunchBehavior) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_SmartCard(self: Windows.Devices.SmartCards.ISmartCardTriggerDetails3) -> Windows.Devices.SmartCards.SmartCard: ...
    TriggerType = property(get_TriggerType, None)
    SourceAppletId = property(get_SourceAppletId, None)
    TriggerData = property(get_TriggerData, None)
    Emulator = property(get_Emulator, None)
    SmartCard = property(get_SmartCard, None)
SmartCardTriggerType = Int32
SmartCardTriggerType_EmulatorTransaction: SmartCardTriggerType = 0
SmartCardTriggerType_EmulatorNearFieldEntry: SmartCardTriggerType = 1
SmartCardTriggerType_EmulatorNearFieldExit: SmartCardTriggerType = 2
SmartCardTriggerType_EmulatorHostApplicationActivated: SmartCardTriggerType = 3
SmartCardTriggerType_EmulatorAppletIdGroupRegistrationChanged: SmartCardTriggerType = 4
SmartCardTriggerType_ReaderCardAdded: SmartCardTriggerType = 5
SmartCardUnlockPromptingBehavior = Int32
SmartCardUnlockPromptingBehavior_AllowUnlockPrompt: SmartCardUnlockPromptingBehavior = 0
SmartCardUnlockPromptingBehavior_RequireUnlockPrompt: SmartCardUnlockPromptingBehavior = 1
SmartCardUnlockPromptingBehavior_PreventUnlockPrompt: SmartCardUnlockPromptingBehavior = 2
make_head(_module, 'CardAddedEventArgs')
make_head(_module, 'CardRemovedEventArgs')
make_head(_module, 'ICardAddedEventArgs')
make_head(_module, 'ICardRemovedEventArgs')
make_head(_module, 'IKnownSmartCardAppletIds')
make_head(_module, 'ISmartCard')
make_head(_module, 'ISmartCardAppletIdGroup')
make_head(_module, 'ISmartCardAppletIdGroup2')
make_head(_module, 'ISmartCardAppletIdGroupFactory')
make_head(_module, 'ISmartCardAppletIdGroupRegistration')
make_head(_module, 'ISmartCardAppletIdGroupRegistration2')
make_head(_module, 'ISmartCardAppletIdGroupStatics')
make_head(_module, 'ISmartCardAutomaticResponseApdu')
make_head(_module, 'ISmartCardAutomaticResponseApdu2')
make_head(_module, 'ISmartCardAutomaticResponseApdu3')
make_head(_module, 'ISmartCardAutomaticResponseApduFactory')
make_head(_module, 'ISmartCardChallengeContext')
make_head(_module, 'ISmartCardConnect')
make_head(_module, 'ISmartCardConnection')
make_head(_module, 'ISmartCardCryptogramGenerator')
make_head(_module, 'ISmartCardCryptogramGenerator2')
make_head(_module, 'ISmartCardCryptogramGeneratorStatics')
make_head(_module, 'ISmartCardCryptogramGeneratorStatics2')
make_head(_module, 'ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult')
make_head(_module, 'ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult')
make_head(_module, 'ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult')
make_head(_module, 'ISmartCardCryptogramMaterialCharacteristics')
make_head(_module, 'ISmartCardCryptogramMaterialPackageCharacteristics')
make_head(_module, 'ISmartCardCryptogramMaterialPossessionProof')
make_head(_module, 'ISmartCardCryptogramPlacementStep')
make_head(_module, 'ISmartCardCryptogramStorageKeyCharacteristics')
make_head(_module, 'ISmartCardCryptogramStorageKeyInfo')
make_head(_module, 'ISmartCardCryptogramStorageKeyInfo2')
make_head(_module, 'ISmartCardEmulator')
make_head(_module, 'ISmartCardEmulator2')
make_head(_module, 'ISmartCardEmulatorApduReceivedEventArgs')
make_head(_module, 'ISmartCardEmulatorApduReceivedEventArgs2')
make_head(_module, 'ISmartCardEmulatorApduReceivedEventArgsWithCryptograms')
make_head(_module, 'ISmartCardEmulatorConnectionDeactivatedEventArgs')
make_head(_module, 'ISmartCardEmulatorConnectionProperties')
make_head(_module, 'ISmartCardEmulatorStatics')
make_head(_module, 'ISmartCardEmulatorStatics2')
make_head(_module, 'ISmartCardEmulatorStatics3')
make_head(_module, 'ISmartCardPinPolicy')
make_head(_module, 'ISmartCardPinResetDeferral')
make_head(_module, 'ISmartCardPinResetRequest')
make_head(_module, 'ISmartCardProvisioning')
make_head(_module, 'ISmartCardProvisioning2')
make_head(_module, 'ISmartCardProvisioningStatics')
make_head(_module, 'ISmartCardProvisioningStatics2')
make_head(_module, 'ISmartCardReader')
make_head(_module, 'ISmartCardReaderStatics')
make_head(_module, 'ISmartCardTriggerDetails')
make_head(_module, 'ISmartCardTriggerDetails2')
make_head(_module, 'ISmartCardTriggerDetails3')
make_head(_module, 'KnownSmartCardAppletIds')
make_head(_module, 'SmartCard')
make_head(_module, 'SmartCardAppletIdGroup')
make_head(_module, 'SmartCardAppletIdGroupRegistration')
make_head(_module, 'SmartCardAutomaticResponseApdu')
make_head(_module, 'SmartCardChallengeContext')
make_head(_module, 'SmartCardConnection')
make_head(_module, 'SmartCardCryptogramGenerator')
make_head(_module, 'SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult')
make_head(_module, 'SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult')
make_head(_module, 'SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult')
make_head(_module, 'SmartCardCryptogramMaterialCharacteristics')
make_head(_module, 'SmartCardCryptogramMaterialPackageCharacteristics')
make_head(_module, 'SmartCardCryptogramMaterialPossessionProof')
make_head(_module, 'SmartCardCryptogramPlacementStep')
make_head(_module, 'SmartCardCryptogramStorageKeyCharacteristics')
make_head(_module, 'SmartCardCryptogramStorageKeyInfo')
make_head(_module, 'SmartCardEmulator')
make_head(_module, 'SmartCardEmulatorApduReceivedEventArgs')
make_head(_module, 'SmartCardEmulatorConnectionDeactivatedEventArgs')
make_head(_module, 'SmartCardEmulatorConnectionProperties')
make_head(_module, 'SmartCardPinPolicy')
make_head(_module, 'SmartCardPinResetDeferral')
make_head(_module, 'SmartCardPinResetHandler')
make_head(_module, 'SmartCardPinResetRequest')
make_head(_module, 'SmartCardProvisioning')
make_head(_module, 'SmartCardReader')
make_head(_module, 'SmartCardTriggerDetails')
