from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.System
import Windows.System.Profile
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AnalyticsInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.AnalyticsInfo'
    @winrt_classmethod
    def GetSystemPropertiesAsync(cls: Windows.System.Profile.IAnalyticsInfoStatics2, attributeNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]]: ...
    @winrt_classmethod
    def get_VersionInfo(cls: Windows.System.Profile.IAnalyticsInfoStatics) -> Windows.System.Profile.AnalyticsVersionInfo: ...
    @winrt_classmethod
    def get_DeviceForm(cls: Windows.System.Profile.IAnalyticsInfoStatics) -> WinRT_String: ...
    VersionInfo = property(get_VersionInfo, None)
    DeviceForm = property(get_DeviceForm, None)
class AnalyticsVersionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.AnalyticsVersionInfo'
    @winrt_mixinmethod
    def get_DeviceFamily(self: Windows.System.Profile.IAnalyticsVersionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceFamilyVersion(self: Windows.System.Profile.IAnalyticsVersionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductName(self: Windows.System.Profile.IAnalyticsVersionInfo2) -> WinRT_String: ...
    DeviceFamily = property(get_DeviceFamily, None)
    DeviceFamilyVersion = property(get_DeviceFamilyVersion, None)
    ProductName = property(get_ProductName, None)
class AppApplicability(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.AppApplicability'
    @winrt_classmethod
    def GetUnsupportedAppRequirements(cls: Windows.System.Profile.IAppApplicabilityStatics, capabilities: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.Collections.IVectorView[Windows.System.Profile.UnsupportedAppRequirement]: ...
class EducationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.EducationSettings'
    @winrt_classmethod
    def get_IsEducationEnvironment(cls: Windows.System.Profile.IEducationSettingsStatics) -> Boolean: ...
    IsEducationEnvironment = property(get_IsEducationEnvironment, None)
class HardwareIdentification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.HardwareIdentification'
    @winrt_classmethod
    def GetPackageSpecificToken(cls: Windows.System.Profile.IHardwareIdentificationStatics, nonce: Windows.Storage.Streams.IBuffer) -> Windows.System.Profile.HardwareToken: ...
class HardwareToken(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.HardwareToken'
    @winrt_mixinmethod
    def get_Id(self: Windows.System.Profile.IHardwareToken) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Signature(self: Windows.System.Profile.IHardwareToken) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Certificate(self: Windows.System.Profile.IHardwareToken) -> Windows.Storage.Streams.IBuffer: ...
    Id = property(get_Id, None)
    Signature = property(get_Signature, None)
    Certificate = property(get_Certificate, None)
class IAnalyticsInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d5ee066-188d-5ba9-43-87-ac-ae-b0-e7-e3-05')
    @winrt_commethod(6)
    def get_VersionInfo(self) -> Windows.System.Profile.AnalyticsVersionInfo: ...
    @winrt_commethod(7)
    def get_DeviceForm(self) -> WinRT_String: ...
    VersionInfo = property(get_VersionInfo, None)
    DeviceForm = property(get_DeviceForm, None)
class IAnalyticsInfoStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('101704ea-a7f9-46d2-ab-94-01-68-65-af-db-25')
    @winrt_commethod(6)
    def GetSystemPropertiesAsync(self, attributeNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]]: ...
class IAnalyticsVersionInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('926130b8-9955-4c74-bd-c1-7c-d0-de-cf-9b-03')
    @winrt_commethod(6)
    def get_DeviceFamily(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceFamilyVersion(self) -> WinRT_String: ...
    DeviceFamily = property(get_DeviceFamily, None)
    DeviceFamilyVersion = property(get_DeviceFamilyVersion, None)
class IAnalyticsVersionInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('76e915b1-ff36-407c-9f-57-16-0d-3e-54-07-47')
    @winrt_commethod(6)
    def get_ProductName(self) -> WinRT_String: ...
    ProductName = property(get_ProductName, None)
class IAppApplicabilityStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1664a082-0f38-5c99-83-e4-48-99-59-70-86-1c')
    @winrt_commethod(6)
    def GetUnsupportedAppRequirements(self, capabilities: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.Collections.IVectorView[Windows.System.Profile.UnsupportedAppRequirement]: ...
class IEducationSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc53f0ef-4d3e-4e13-9b-23-50-5f-4d-09-1e-92')
    @winrt_commethod(6)
    def get_IsEducationEnvironment(self) -> Boolean: ...
    IsEducationEnvironment = property(get_IsEducationEnvironment, None)
class IHardwareIdentificationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('971260e0-f170-4a42-bd-55-a9-00-b2-12-da-e2')
    @winrt_commethod(6)
    def GetPackageSpecificToken(self, nonce: Windows.Storage.Streams.IBuffer) -> Windows.System.Profile.HardwareToken: ...
class IHardwareToken(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('28f6d4c0-fb12-40a4-81-67-7f-4e-03-d2-72-4c')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Signature(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Certificate(self) -> Windows.Storage.Streams.IBuffer: ...
    Id = property(get_Id, None)
    Signature = property(get_Signature, None)
    Certificate = property(get_Certificate, None)
class IKnownRetailInfoPropertiesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('99571178-500f-487e-8e-75-29-e5-51-72-87-12')
    @winrt_commethod(6)
    def get_RetailAccessCode(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ManufacturerName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ModelName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayModelName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Price(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_IsFeatured(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_FormFactor(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_ScreenSize(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Weight(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_DisplayDescription(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_BatteryLifeDescription(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_ProcessorDescription(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Memory(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_StorageDescription(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_GraphicsDescription(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_FrontCameraDescription(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_RearCameraDescription(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_HasNfc(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_HasSdSlot(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_HasOpticalDrive(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_IsOfficeInstalled(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_WindowsEdition(self) -> WinRT_String: ...
    RetailAccessCode = property(get_RetailAccessCode, None)
    ManufacturerName = property(get_ManufacturerName, None)
    ModelName = property(get_ModelName, None)
    DisplayModelName = property(get_DisplayModelName, None)
    Price = property(get_Price, None)
    IsFeatured = property(get_IsFeatured, None)
    FormFactor = property(get_FormFactor, None)
    ScreenSize = property(get_ScreenSize, None)
    Weight = property(get_Weight, None)
    DisplayDescription = property(get_DisplayDescription, None)
    BatteryLifeDescription = property(get_BatteryLifeDescription, None)
    ProcessorDescription = property(get_ProcessorDescription, None)
    Memory = property(get_Memory, None)
    StorageDescription = property(get_StorageDescription, None)
    GraphicsDescription = property(get_GraphicsDescription, None)
    FrontCameraDescription = property(get_FrontCameraDescription, None)
    RearCameraDescription = property(get_RearCameraDescription, None)
    HasNfc = property(get_HasNfc, None)
    HasSdSlot = property(get_HasSdSlot, None)
    HasOpticalDrive = property(get_HasOpticalDrive, None)
    IsOfficeInstalled = property(get_IsOfficeInstalled, None)
    WindowsEdition = property(get_WindowsEdition, None)
class IPlatformDiagnosticsAndUsageDataSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b6e24c1b-7b1c-4b32-8c-62-a6-65-97-ce-72-3a')
    @winrt_commethod(6)
    def get_CollectionLevel(self) -> Windows.System.Profile.PlatformDataCollectionLevel: ...
    @winrt_commethod(7)
    def add_CollectionLevelChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CollectionLevelChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CanCollectDiagnostics(self, level: Windows.System.Profile.PlatformDataCollectionLevel) -> Boolean: ...
    CollectionLevel = property(get_CollectionLevel, None)
class IRetailInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0712c6b8-8b92-4f2a-84-99-03-1f-17-98-d6-ef')
    @winrt_commethod(6)
    def get_IsDemoModeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    IsDemoModeEnabled = property(get_IsDemoModeEnabled, None)
    Properties = property(get_Properties, None)
class ISharedModeSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('893df40e-cad6-4d50-8c-49-6f-cf-c0-3e-db-29')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    IsEnabled = property(get_IsEnabled, None)
class ISharedModeSettingsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('608988a4-ccf1-4ee8-a5-e2-fd-6a-1d-0c-fa-c8')
    @winrt_commethod(6)
    def get_ShouldAvoidLocalStorage(self) -> Boolean: ...
    ShouldAvoidLocalStorage = property(get_ShouldAvoidLocalStorage, None)
class ISmartAppControlPolicyStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5ff8c75b-073e-5015-8d-98-5f-f2-24-18-0a-0b')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
class ISystemIdentificationInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c659e7d-c3c2-4d33-a2-df-21-bc-41-91-6e-b3')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Source(self) -> Windows.System.Profile.SystemIdentificationSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
class ISystemIdentificationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5581f42a-d3df-4d93-a3-7d-c4-1a-61-6c-6d-01')
    @winrt_commethod(6)
    def GetSystemIdForPublisher(self) -> Windows.System.Profile.SystemIdentificationInfo: ...
    @winrt_commethod(7)
    def GetSystemIdForUser(self, user: Windows.System.User) -> Windows.System.Profile.SystemIdentificationInfo: ...
class ISystemSetupInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b8366a4b-fb6a-4571-be-0a-9a-0f-67-95-41-23')
    @winrt_commethod(6)
    def get_OutOfBoxExperienceState(self) -> Windows.System.Profile.SystemOutOfBoxExperienceState: ...
    @winrt_commethod(7)
    def add_OutOfBoxExperienceStateChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_OutOfBoxExperienceStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    OutOfBoxExperienceState = property(get_OutOfBoxExperienceState, None)
class IUnsupportedAppRequirement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6182445c-894b-5cbc-89-76-a9-8e-0a-9b-99-8d')
    @winrt_commethod(6)
    def get_Requirement(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Reasons(self) -> Windows.System.Profile.UnsupportedAppRequirementReasons: ...
    Requirement = property(get_Requirement, None)
    Reasons = property(get_Reasons, None)
class IWindowsIntegrityPolicyStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d1d81db-8d63-4789-9e-a5-dd-cf-65-a9-4f-3c')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnabledForTrial(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanDisable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDisableSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_PolicyChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PolicyChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    IsEnabledForTrial = property(get_IsEnabledForTrial, None)
    CanDisable = property(get_CanDisable, None)
    IsDisableSupported = property(get_IsDisableSupported, None)
class KnownRetailInfoProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.KnownRetailInfoProperties'
    @winrt_classmethod
    def get_RetailAccessCode(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ManufacturerName(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ModelName(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayModelName(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Price(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsFeatured(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FormFactor(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ScreenSize(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Weight(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BatteryLifeDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProcessorDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Memory(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StorageDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GraphicsDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrontCameraDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RearCameraDescription(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasNfc(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasSdSlot(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasOpticalDrive(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsOfficeInstalled(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WindowsEdition(cls: Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    RetailAccessCode = property(get_RetailAccessCode, None)
    ManufacturerName = property(get_ManufacturerName, None)
    ModelName = property(get_ModelName, None)
    DisplayModelName = property(get_DisplayModelName, None)
    Price = property(get_Price, None)
    IsFeatured = property(get_IsFeatured, None)
    FormFactor = property(get_FormFactor, None)
    ScreenSize = property(get_ScreenSize, None)
    Weight = property(get_Weight, None)
    DisplayDescription = property(get_DisplayDescription, None)
    BatteryLifeDescription = property(get_BatteryLifeDescription, None)
    ProcessorDescription = property(get_ProcessorDescription, None)
    Memory = property(get_Memory, None)
    StorageDescription = property(get_StorageDescription, None)
    GraphicsDescription = property(get_GraphicsDescription, None)
    FrontCameraDescription = property(get_FrontCameraDescription, None)
    RearCameraDescription = property(get_RearCameraDescription, None)
    HasNfc = property(get_HasNfc, None)
    HasSdSlot = property(get_HasSdSlot, None)
    HasOpticalDrive = property(get_HasOpticalDrive, None)
    IsOfficeInstalled = property(get_IsOfficeInstalled, None)
    WindowsEdition = property(get_WindowsEdition, None)
PlatformDataCollectionLevel = Int32
PlatformDataCollectionLevel_Security: PlatformDataCollectionLevel = 0
PlatformDataCollectionLevel_Basic: PlatformDataCollectionLevel = 1
PlatformDataCollectionLevel_Enhanced: PlatformDataCollectionLevel = 2
PlatformDataCollectionLevel_Full: PlatformDataCollectionLevel = 3
class PlatformDiagnosticsAndUsageDataSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.PlatformDiagnosticsAndUsageDataSettings'
    @winrt_classmethod
    def get_CollectionLevel(cls: Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics) -> Windows.System.Profile.PlatformDataCollectionLevel: ...
    @winrt_classmethod
    def add_CollectionLevelChanged(cls: Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CollectionLevelChanged(cls: Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CanCollectDiagnostics(cls: Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, level: Windows.System.Profile.PlatformDataCollectionLevel) -> Boolean: ...
    CollectionLevel = property(get_CollectionLevel, None)
ProfileHardwareTokenContract: UInt32 = 65536
ProfileRetailInfoContract: UInt32 = 65536
ProfileSharedModeContract: UInt32 = 131072
class RetailInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.RetailInfo'
    @winrt_classmethod
    def get_IsDemoModeEnabled(cls: Windows.System.Profile.IRetailInfoStatics) -> Boolean: ...
    @winrt_classmethod
    def get_Properties(cls: Windows.System.Profile.IRetailInfoStatics) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    IsDemoModeEnabled = property(get_IsDemoModeEnabled, None)
    Properties = property(get_Properties, None)
class SharedModeSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SharedModeSettings'
    @winrt_classmethod
    def get_ShouldAvoidLocalStorage(cls: Windows.System.Profile.ISharedModeSettingsStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_IsEnabled(cls: Windows.System.Profile.ISharedModeSettingsStatics) -> Boolean: ...
    ShouldAvoidLocalStorage = property(get_ShouldAvoidLocalStorage, None)
    IsEnabled = property(get_IsEnabled, None)
class SmartAppControlPolicy(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SmartAppControlPolicy'
    @winrt_classmethod
    def get_IsEnabled(cls: Windows.System.Profile.ISmartAppControlPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def add_Changed(cls: Windows.System.Profile.ISmartAppControlPolicyStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Changed(cls: Windows.System.Profile.ISmartAppControlPolicyStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
class SystemIdentification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemIdentification'
    @winrt_classmethod
    def GetSystemIdForPublisher(cls: Windows.System.Profile.ISystemIdentificationStatics) -> Windows.System.Profile.SystemIdentificationInfo: ...
    @winrt_classmethod
    def GetSystemIdForUser(cls: Windows.System.Profile.ISystemIdentificationStatics, user: Windows.System.User) -> Windows.System.Profile.SystemIdentificationInfo: ...
class SystemIdentificationInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemIdentificationInfo'
    @winrt_mixinmethod
    def get_Id(self: Windows.System.Profile.ISystemIdentificationInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.System.Profile.ISystemIdentificationInfo) -> Windows.System.Profile.SystemIdentificationSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
SystemIdentificationSource = Int32
SystemIdentificationSource_None: SystemIdentificationSource = 0
SystemIdentificationSource_Tpm: SystemIdentificationSource = 1
SystemIdentificationSource_Uefi: SystemIdentificationSource = 2
SystemIdentificationSource_Registry: SystemIdentificationSource = 3
SystemOutOfBoxExperienceState = Int32
SystemOutOfBoxExperienceState_NotStarted: SystemOutOfBoxExperienceState = 0
SystemOutOfBoxExperienceState_InProgress: SystemOutOfBoxExperienceState = 1
SystemOutOfBoxExperienceState_Completed: SystemOutOfBoxExperienceState = 2
class SystemSetupInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemSetupInfo'
    @winrt_classmethod
    def get_OutOfBoxExperienceState(cls: Windows.System.Profile.ISystemSetupInfoStatics) -> Windows.System.Profile.SystemOutOfBoxExperienceState: ...
    @winrt_classmethod
    def add_OutOfBoxExperienceStateChanged(cls: Windows.System.Profile.ISystemSetupInfoStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_OutOfBoxExperienceStateChanged(cls: Windows.System.Profile.ISystemSetupInfoStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    OutOfBoxExperienceState = property(get_OutOfBoxExperienceState, None)
class UnsupportedAppRequirement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.UnsupportedAppRequirement'
    @winrt_mixinmethod
    def get_Requirement(self: Windows.System.Profile.IUnsupportedAppRequirement) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Reasons(self: Windows.System.Profile.IUnsupportedAppRequirement) -> Windows.System.Profile.UnsupportedAppRequirementReasons: ...
    Requirement = property(get_Requirement, None)
    Reasons = property(get_Reasons, None)
UnsupportedAppRequirementReasons = UInt32
UnsupportedAppRequirementReasons_Unknown: UnsupportedAppRequirementReasons = 0
UnsupportedAppRequirementReasons_DeniedBySystem: UnsupportedAppRequirementReasons = 1
class WindowsIntegrityPolicy(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.WindowsIntegrityPolicy'
    @winrt_classmethod
    def get_IsEnabled(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsEnabledForTrial(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_CanDisable(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsDisableSupported(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def add_PolicyChanged(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PolicyChanged(cls: Windows.System.Profile.IWindowsIntegrityPolicyStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    IsEnabledForTrial = property(get_IsEnabledForTrial, None)
    CanDisable = property(get_CanDisable, None)
    IsDisableSupported = property(get_IsDisableSupported, None)
make_head(_module, 'AnalyticsInfo')
make_head(_module, 'AnalyticsVersionInfo')
make_head(_module, 'AppApplicability')
make_head(_module, 'EducationSettings')
make_head(_module, 'HardwareIdentification')
make_head(_module, 'HardwareToken')
make_head(_module, 'IAnalyticsInfoStatics')
make_head(_module, 'IAnalyticsInfoStatics2')
make_head(_module, 'IAnalyticsVersionInfo')
make_head(_module, 'IAnalyticsVersionInfo2')
make_head(_module, 'IAppApplicabilityStatics')
make_head(_module, 'IEducationSettingsStatics')
make_head(_module, 'IHardwareIdentificationStatics')
make_head(_module, 'IHardwareToken')
make_head(_module, 'IKnownRetailInfoPropertiesStatics')
make_head(_module, 'IPlatformDiagnosticsAndUsageDataSettingsStatics')
make_head(_module, 'IRetailInfoStatics')
make_head(_module, 'ISharedModeSettingsStatics')
make_head(_module, 'ISharedModeSettingsStatics2')
make_head(_module, 'ISmartAppControlPolicyStatics')
make_head(_module, 'ISystemIdentificationInfo')
make_head(_module, 'ISystemIdentificationStatics')
make_head(_module, 'ISystemSetupInfoStatics')
make_head(_module, 'IUnsupportedAppRequirement')
make_head(_module, 'IWindowsIntegrityPolicyStatics')
make_head(_module, 'KnownRetailInfoProperties')
make_head(_module, 'PlatformDiagnosticsAndUsageDataSettings')
make_head(_module, 'RetailInfo')
make_head(_module, 'SharedModeSettings')
make_head(_module, 'SmartAppControlPolicy')
make_head(_module, 'SystemIdentification')
make_head(_module, 'SystemIdentificationInfo')
make_head(_module, 'SystemSetupInfo')
make_head(_module, 'UnsupportedAppRequirement')
make_head(_module, 'WindowsIntegrityPolicy')
