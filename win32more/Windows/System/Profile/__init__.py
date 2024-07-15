from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.System.Profile
import win32more.Windows.Win32.System.WinRT
class _AnalyticsInfo_Meta_(ComPtr.__class__):
    pass
class AnalyticsInfo(ComPtr, metaclass=_AnalyticsInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.AnalyticsInfo'
    @winrt_classmethod
    def GetSystemPropertiesAsync(cls: win32more.Windows.System.Profile.IAnalyticsInfoStatics2, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]]: ...
    @winrt_classmethod
    def get_VersionInfo(cls: win32more.Windows.System.Profile.IAnalyticsInfoStatics) -> win32more.Windows.System.Profile.AnalyticsVersionInfo: ...
    @winrt_classmethod
    def get_DeviceForm(cls: win32more.Windows.System.Profile.IAnalyticsInfoStatics) -> WinRT_String: ...
    _AnalyticsInfo_Meta_.DeviceForm = property(get_DeviceForm, None)
    _AnalyticsInfo_Meta_.VersionInfo = property(get_VersionInfo, None)
class AnalyticsVersionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.IAnalyticsVersionInfo
    _classid_ = 'Windows.System.Profile.AnalyticsVersionInfo'
    @winrt_mixinmethod
    def get_DeviceFamily(self: win32more.Windows.System.Profile.IAnalyticsVersionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceFamilyVersion(self: win32more.Windows.System.Profile.IAnalyticsVersionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductName(self: win32more.Windows.System.Profile.IAnalyticsVersionInfo2) -> WinRT_String: ...
    DeviceFamily = property(get_DeviceFamily, None)
    DeviceFamilyVersion = property(get_DeviceFamilyVersion, None)
    ProductName = property(get_ProductName, None)
class AppApplicability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.AppApplicability'
    @winrt_classmethod
    def GetUnsupportedAppRequirements(cls: win32more.Windows.System.Profile.IAppApplicabilityStatics, capabilities: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Profile.UnsupportedAppRequirement]: ...
class _EducationSettings_Meta_(ComPtr.__class__):
    pass
class EducationSettings(ComPtr, metaclass=_EducationSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.EducationSettings'
    @winrt_classmethod
    def get_IsEducationEnvironment(cls: win32more.Windows.System.Profile.IEducationSettingsStatics) -> Boolean: ...
    _EducationSettings_Meta_.IsEducationEnvironment = property(get_IsEducationEnvironment, None)
class HardwareIdentification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.HardwareIdentification'
    @winrt_classmethod
    def GetPackageSpecificToken(cls: win32more.Windows.System.Profile.IHardwareIdentificationStatics, nonce: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.System.Profile.HardwareToken: ...
class HardwareToken(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.IHardwareToken
    _classid_ = 'Windows.System.Profile.HardwareToken'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Profile.IHardwareToken) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Signature(self: win32more.Windows.System.Profile.IHardwareToken) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Certificate(self: win32more.Windows.System.Profile.IHardwareToken) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Certificate = property(get_Certificate, None)
    Id = property(get_Id, None)
    Signature = property(get_Signature, None)
class IAnalyticsInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IAnalyticsInfoStatics'
    _iid_ = Guid('{1d5ee066-188d-5ba9-4387-acaeb0e7e305}')
    @winrt_commethod(6)
    def get_VersionInfo(self) -> win32more.Windows.System.Profile.AnalyticsVersionInfo: ...
    @winrt_commethod(7)
    def get_DeviceForm(self) -> WinRT_String: ...
    DeviceForm = property(get_DeviceForm, None)
    VersionInfo = property(get_VersionInfo, None)
class IAnalyticsInfoStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IAnalyticsInfoStatics2'
    _iid_ = Guid('{101704ea-a7f9-46d2-ab94-016865afdb25}')
    @winrt_commethod(6)
    def GetSystemPropertiesAsync(self, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]]: ...
class IAnalyticsVersionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IAnalyticsVersionInfo'
    _iid_ = Guid('{926130b8-9955-4c74-bdc1-7cd0decf9b03}')
    @winrt_commethod(6)
    def get_DeviceFamily(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DeviceFamilyVersion(self) -> WinRT_String: ...
    DeviceFamily = property(get_DeviceFamily, None)
    DeviceFamilyVersion = property(get_DeviceFamilyVersion, None)
class IAnalyticsVersionInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IAnalyticsVersionInfo2'
    _iid_ = Guid('{76e915b1-ff36-407c-9f57-160d3e540747}')
    @winrt_commethod(6)
    def get_ProductName(self) -> WinRT_String: ...
    ProductName = property(get_ProductName, None)
class IAppApplicabilityStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IAppApplicabilityStatics'
    _iid_ = Guid('{1664a082-0f38-5c99-83e4-48995970861c}')
    @winrt_commethod(6)
    def GetUnsupportedAppRequirements(self, capabilities: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Profile.UnsupportedAppRequirement]: ...
class IEducationSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IEducationSettingsStatics'
    _iid_ = Guid('{fc53f0ef-4d3e-4e13-9b23-505f4d091e92}')
    @winrt_commethod(6)
    def get_IsEducationEnvironment(self) -> Boolean: ...
    IsEducationEnvironment = property(get_IsEducationEnvironment, None)
class IHardwareIdentificationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IHardwareIdentificationStatics'
    _iid_ = Guid('{971260e0-f170-4a42-bd55-a900b212dae2}')
    @winrt_commethod(6)
    def GetPackageSpecificToken(self, nonce: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.System.Profile.HardwareToken: ...
class IHardwareToken(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IHardwareToken'
    _iid_ = Guid('{28f6d4c0-fb12-40a4-8167-7f4e03d2724c}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Signature(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_Certificate(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Certificate = property(get_Certificate, None)
    Id = property(get_Id, None)
    Signature = property(get_Signature, None)
class IKnownRetailInfoPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IKnownRetailInfoPropertiesStatics'
    _iid_ = Guid('{99571178-500f-487e-8e75-29e551728712}')
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
    BatteryLifeDescription = property(get_BatteryLifeDescription, None)
    DisplayDescription = property(get_DisplayDescription, None)
    DisplayModelName = property(get_DisplayModelName, None)
    FormFactor = property(get_FormFactor, None)
    FrontCameraDescription = property(get_FrontCameraDescription, None)
    GraphicsDescription = property(get_GraphicsDescription, None)
    HasNfc = property(get_HasNfc, None)
    HasOpticalDrive = property(get_HasOpticalDrive, None)
    HasSdSlot = property(get_HasSdSlot, None)
    IsFeatured = property(get_IsFeatured, None)
    IsOfficeInstalled = property(get_IsOfficeInstalled, None)
    ManufacturerName = property(get_ManufacturerName, None)
    Memory = property(get_Memory, None)
    ModelName = property(get_ModelName, None)
    Price = property(get_Price, None)
    ProcessorDescription = property(get_ProcessorDescription, None)
    RearCameraDescription = property(get_RearCameraDescription, None)
    RetailAccessCode = property(get_RetailAccessCode, None)
    ScreenSize = property(get_ScreenSize, None)
    StorageDescription = property(get_StorageDescription, None)
    Weight = property(get_Weight, None)
    WindowsEdition = property(get_WindowsEdition, None)
class IPlatformAutomaticAppSignInManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IPlatformAutomaticAppSignInManagerStatics'
    _iid_ = Guid('{1ac9afce-8dd5-5c2d-b420-767d1f3b7d03}')
    @winrt_commethod(6)
    def get_Policy(self) -> win32more.Windows.System.Profile.PlatformAutomaticAppSignInPolicy: ...
    Policy = property(get_Policy, None)
class IPlatformDiagnosticsAndUsageDataSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics'
    _iid_ = Guid('{b6e24c1b-7b1c-4b32-8c62-a66597ce723a}')
    @winrt_commethod(6)
    def get_CollectionLevel(self) -> win32more.Windows.System.Profile.PlatformDataCollectionLevel: ...
    @winrt_commethod(7)
    def add_CollectionLevelChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_CollectionLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CanCollectDiagnostics(self, level: win32more.Windows.System.Profile.PlatformDataCollectionLevel) -> Boolean: ...
    CollectionLevel = property(get_CollectionLevel, None)
    CollectionLevelChanged = event()
class IRetailInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IRetailInfoStatics'
    _iid_ = Guid('{0712c6b8-8b92-4f2a-8499-031f1798d6ef}')
    @winrt_commethod(6)
    def get_IsDemoModeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    IsDemoModeEnabled = property(get_IsDemoModeEnabled, None)
    Properties = property(get_Properties, None)
class ISharedModeSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISharedModeSettingsStatics'
    _iid_ = Guid('{893df40e-cad6-4d50-8c49-6fcfc03edb29}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    IsEnabled = property(get_IsEnabled, None)
class ISharedModeSettingsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISharedModeSettingsStatics2'
    _iid_ = Guid('{608988a4-ccf1-4ee8-a5e2-fd6a1d0cfac8}')
    @winrt_commethod(6)
    def get_ShouldAvoidLocalStorage(self) -> Boolean: ...
    ShouldAvoidLocalStorage = property(get_ShouldAvoidLocalStorage, None)
class ISmartAppControlPolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISmartAppControlPolicyStatics'
    _iid_ = Guid('{5ff8c75b-073e-5015-8d98-5ff224180a0b}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    Changed = event()
class ISystemIdentificationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISystemIdentificationInfo'
    _iid_ = Guid('{0c659e7d-c3c2-4d33-a2df-21bc41916eb3}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Source(self) -> win32more.Windows.System.Profile.SystemIdentificationSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
class ISystemIdentificationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISystemIdentificationStatics'
    _iid_ = Guid('{5581f42a-d3df-4d93-a37d-c41a616c6d01}')
    @winrt_commethod(6)
    def GetSystemIdForPublisher(self) -> win32more.Windows.System.Profile.SystemIdentificationInfo: ...
    @winrt_commethod(7)
    def GetSystemIdForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.Profile.SystemIdentificationInfo: ...
class ISystemSetupInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.ISystemSetupInfoStatics'
    _iid_ = Guid('{b8366a4b-fb6a-4571-be0a-9a0f67954123}')
    @winrt_commethod(6)
    def get_OutOfBoxExperienceState(self) -> win32more.Windows.System.Profile.SystemOutOfBoxExperienceState: ...
    @winrt_commethod(7)
    def add_OutOfBoxExperienceStateChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_OutOfBoxExperienceStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    OutOfBoxExperienceState = property(get_OutOfBoxExperienceState, None)
    OutOfBoxExperienceStateChanged = event()
class IUnsupportedAppRequirement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IUnsupportedAppRequirement'
    _iid_ = Guid('{6182445c-894b-5cbc-8976-a98e0a9b998d}')
    @winrt_commethod(6)
    def get_Requirement(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Reasons(self) -> win32more.Windows.System.Profile.UnsupportedAppRequirementReasons: ...
    Reasons = property(get_Reasons, None)
    Requirement = property(get_Requirement, None)
class IWindowsIntegrityPolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.IWindowsIntegrityPolicyStatics'
    _iid_ = Guid('{7d1d81db-8d63-4789-9ea5-ddcf65a94f3c}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnabledForTrial(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanDisable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsDisableSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def add_PolicyChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PolicyChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CanDisable = property(get_CanDisable, None)
    IsDisableSupported = property(get_IsDisableSupported, None)
    IsEnabled = property(get_IsEnabled, None)
    IsEnabledForTrial = property(get_IsEnabledForTrial, None)
    PolicyChanged = event()
class _KnownRetailInfoProperties_Meta_(ComPtr.__class__):
    pass
class KnownRetailInfoProperties(ComPtr, metaclass=_KnownRetailInfoProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.KnownRetailInfoProperties'
    @winrt_classmethod
    def get_RetailAccessCode(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ManufacturerName(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ModelName(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayModelName(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Price(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsFeatured(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FormFactor(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ScreenSize(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Weight(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BatteryLifeDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProcessorDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Memory(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StorageDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GraphicsDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrontCameraDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RearCameraDescription(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasNfc(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasSdSlot(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HasOpticalDrive(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsOfficeInstalled(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WindowsEdition(cls: win32more.Windows.System.Profile.IKnownRetailInfoPropertiesStatics) -> WinRT_String: ...
    _KnownRetailInfoProperties_Meta_.BatteryLifeDescription = property(get_BatteryLifeDescription, None)
    _KnownRetailInfoProperties_Meta_.DisplayDescription = property(get_DisplayDescription, None)
    _KnownRetailInfoProperties_Meta_.DisplayModelName = property(get_DisplayModelName, None)
    _KnownRetailInfoProperties_Meta_.FormFactor = property(get_FormFactor, None)
    _KnownRetailInfoProperties_Meta_.FrontCameraDescription = property(get_FrontCameraDescription, None)
    _KnownRetailInfoProperties_Meta_.GraphicsDescription = property(get_GraphicsDescription, None)
    _KnownRetailInfoProperties_Meta_.HasNfc = property(get_HasNfc, None)
    _KnownRetailInfoProperties_Meta_.HasOpticalDrive = property(get_HasOpticalDrive, None)
    _KnownRetailInfoProperties_Meta_.HasSdSlot = property(get_HasSdSlot, None)
    _KnownRetailInfoProperties_Meta_.IsFeatured = property(get_IsFeatured, None)
    _KnownRetailInfoProperties_Meta_.IsOfficeInstalled = property(get_IsOfficeInstalled, None)
    _KnownRetailInfoProperties_Meta_.ManufacturerName = property(get_ManufacturerName, None)
    _KnownRetailInfoProperties_Meta_.Memory = property(get_Memory, None)
    _KnownRetailInfoProperties_Meta_.ModelName = property(get_ModelName, None)
    _KnownRetailInfoProperties_Meta_.Price = property(get_Price, None)
    _KnownRetailInfoProperties_Meta_.ProcessorDescription = property(get_ProcessorDescription, None)
    _KnownRetailInfoProperties_Meta_.RearCameraDescription = property(get_RearCameraDescription, None)
    _KnownRetailInfoProperties_Meta_.RetailAccessCode = property(get_RetailAccessCode, None)
    _KnownRetailInfoProperties_Meta_.ScreenSize = property(get_ScreenSize, None)
    _KnownRetailInfoProperties_Meta_.StorageDescription = property(get_StorageDescription, None)
    _KnownRetailInfoProperties_Meta_.Weight = property(get_Weight, None)
    _KnownRetailInfoProperties_Meta_.WindowsEdition = property(get_WindowsEdition, None)
PlatformAutomaticAppSignInContract: UInt32 = 65536
class _PlatformAutomaticAppSignInManager_Meta_(ComPtr.__class__):
    pass
class PlatformAutomaticAppSignInManager(ComPtr, metaclass=_PlatformAutomaticAppSignInManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.PlatformAutomaticAppSignInManager'
    @winrt_classmethod
    def get_Policy(cls: win32more.Windows.System.Profile.IPlatformAutomaticAppSignInManagerStatics) -> win32more.Windows.System.Profile.PlatformAutomaticAppSignInPolicy: ...
    _PlatformAutomaticAppSignInManager_Meta_.Policy = property(get_Policy, None)
class PlatformAutomaticAppSignInPolicy(Enum, Int32):
    Unknown = 0
    PermissionRequired = 1
    AlwaysAllowed = 2
class PlatformDataCollectionLevel(Enum, Int32):
    Security = 0
    Basic = 1
    Enhanced = 2
    Full = 3
class _PlatformDiagnosticsAndUsageDataSettings_Meta_(ComPtr.__class__):
    pass
class PlatformDiagnosticsAndUsageDataSettings(ComPtr, metaclass=_PlatformDiagnosticsAndUsageDataSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.PlatformDiagnosticsAndUsageDataSettings'
    @winrt_classmethod
    def get_CollectionLevel(cls: win32more.Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics) -> win32more.Windows.System.Profile.PlatformDataCollectionLevel: ...
    @winrt_classmethod
    def add_CollectionLevelChanged(cls: win32more.Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CollectionLevelChanged(cls: win32more.Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CanCollectDiagnostics(cls: win32more.Windows.System.Profile.IPlatformDiagnosticsAndUsageDataSettingsStatics, level: win32more.Windows.System.Profile.PlatformDataCollectionLevel) -> Boolean: ...
    _PlatformDiagnosticsAndUsageDataSettings_Meta_.CollectionLevel = property(get_CollectionLevel, None)
ProfileHardwareTokenContract: UInt32 = 65536
ProfileRetailInfoContract: UInt32 = 65536
ProfileSharedModeContract: UInt32 = 131072
class _RetailInfo_Meta_(ComPtr.__class__):
    pass
class RetailInfo(ComPtr, metaclass=_RetailInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.RetailInfo'
    @winrt_classmethod
    def get_IsDemoModeEnabled(cls: win32more.Windows.System.Profile.IRetailInfoStatics) -> Boolean: ...
    @winrt_classmethod
    def get_Properties(cls: win32more.Windows.System.Profile.IRetailInfoStatics) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    _RetailInfo_Meta_.IsDemoModeEnabled = property(get_IsDemoModeEnabled, None)
    _RetailInfo_Meta_.Properties = property(get_Properties, None)
class _SharedModeSettings_Meta_(ComPtr.__class__):
    pass
class SharedModeSettings(ComPtr, metaclass=_SharedModeSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SharedModeSettings'
    @winrt_classmethod
    def get_ShouldAvoidLocalStorage(cls: win32more.Windows.System.Profile.ISharedModeSettingsStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_IsEnabled(cls: win32more.Windows.System.Profile.ISharedModeSettingsStatics) -> Boolean: ...
    _SharedModeSettings_Meta_.IsEnabled = property(get_IsEnabled, None)
    _SharedModeSettings_Meta_.ShouldAvoidLocalStorage = property(get_ShouldAvoidLocalStorage, None)
class _SmartAppControlPolicy_Meta_(ComPtr.__class__):
    pass
class SmartAppControlPolicy(ComPtr, metaclass=_SmartAppControlPolicy_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SmartAppControlPolicy'
    @winrt_classmethod
    def get_IsEnabled(cls: win32more.Windows.System.Profile.ISmartAppControlPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def add_Changed(cls: win32more.Windows.System.Profile.ISmartAppControlPolicyStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Changed(cls: win32more.Windows.System.Profile.ISmartAppControlPolicyStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _SmartAppControlPolicy_Meta_.IsEnabled = property(get_IsEnabled, None)
class SystemIdentification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemIdentification'
    @winrt_classmethod
    def GetSystemIdForPublisher(cls: win32more.Windows.System.Profile.ISystemIdentificationStatics) -> win32more.Windows.System.Profile.SystemIdentificationInfo: ...
    @winrt_classmethod
    def GetSystemIdForUser(cls: win32more.Windows.System.Profile.ISystemIdentificationStatics, user: win32more.Windows.System.User) -> win32more.Windows.System.Profile.SystemIdentificationInfo: ...
class SystemIdentificationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.ISystemIdentificationInfo
    _classid_ = 'Windows.System.Profile.SystemIdentificationInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Profile.ISystemIdentificationInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.System.Profile.ISystemIdentificationInfo) -> win32more.Windows.System.Profile.SystemIdentificationSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
class SystemIdentificationSource(Enum, Int32):
    None_ = 0
    Tpm = 1
    Uefi = 2
    Registry = 3
class SystemOutOfBoxExperienceState(Enum, Int32):
    NotStarted = 0
    InProgress = 1
    Completed = 2
class _SystemSetupInfo_Meta_(ComPtr.__class__):
    pass
class SystemSetupInfo(ComPtr, metaclass=_SystemSetupInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemSetupInfo'
    @winrt_classmethod
    def get_OutOfBoxExperienceState(cls: win32more.Windows.System.Profile.ISystemSetupInfoStatics) -> win32more.Windows.System.Profile.SystemOutOfBoxExperienceState: ...
    @winrt_classmethod
    def add_OutOfBoxExperienceStateChanged(cls: win32more.Windows.System.Profile.ISystemSetupInfoStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_OutOfBoxExperienceStateChanged(cls: win32more.Windows.System.Profile.ISystemSetupInfoStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _SystemSetupInfo_Meta_.OutOfBoxExperienceState = property(get_OutOfBoxExperienceState, None)
class UnsupportedAppRequirement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.IUnsupportedAppRequirement
    _classid_ = 'Windows.System.Profile.UnsupportedAppRequirement'
    @winrt_mixinmethod
    def get_Requirement(self: win32more.Windows.System.Profile.IUnsupportedAppRequirement) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Reasons(self: win32more.Windows.System.Profile.IUnsupportedAppRequirement) -> win32more.Windows.System.Profile.UnsupportedAppRequirementReasons: ...
    Reasons = property(get_Reasons, None)
    Requirement = property(get_Requirement, None)
class UnsupportedAppRequirementReasons(Enum, UInt32):
    Unknown = 0
    DeniedBySystem = 1
class _WindowsIntegrityPolicy_Meta_(ComPtr.__class__):
    pass
class WindowsIntegrityPolicy(ComPtr, metaclass=_WindowsIntegrityPolicy_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.WindowsIntegrityPolicy'
    @winrt_classmethod
    def get_IsEnabled(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsEnabledForTrial(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_CanDisable(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsDisableSupported(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def add_PolicyChanged(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PolicyChanged(cls: win32more.Windows.System.Profile.IWindowsIntegrityPolicyStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _WindowsIntegrityPolicy_Meta_.CanDisable = property(get_CanDisable, None)
    _WindowsIntegrityPolicy_Meta_.IsDisableSupported = property(get_IsDisableSupported, None)
    _WindowsIntegrityPolicy_Meta_.IsEnabled = property(get_IsEnabled, None)
    _WindowsIntegrityPolicy_Meta_.IsEnabledForTrial = property(get_IsEnabledForTrial, None)


make_ready(__name__)
