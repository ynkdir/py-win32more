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
import Windows.ApplicationModel
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Core
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.Streams
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AddResourcePackageOptions = UInt32
AddResourcePackageOptions_None: AddResourcePackageOptions = 0
AddResourcePackageOptions_ForceTargetAppShutdown: AddResourcePackageOptions = 1
AddResourcePackageOptions_ApplyUpdateIfAvailable: AddResourcePackageOptions = 2
class AppDisplayInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppDisplayInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.IAppDisplayInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.IAppDisplayInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLogo(self: Windows.ApplicationModel.IAppDisplayInfo, size: Windows.Foundation.Size) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
AppExecutionContext = Int32
AppExecutionContext_Unknown: AppExecutionContext = 0
AppExecutionContext_Host: AppExecutionContext = 1
AppExecutionContext_Guest: AppExecutionContext = 2
class AppInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppInfo'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayInfo(self: Windows.ApplicationModel.IAppInfo) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IAppInfo2) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_ExecutionContext(self: Windows.ApplicationModel.IAppInfo3) -> Windows.ApplicationModel.AppExecutionContext: ...
    @winrt_mixinmethod
    def get_SupportedFileExtensions(self: Windows.ApplicationModel.IAppInfo4) -> POINTER(WinRT_String): ...
    @winrt_classmethod
    def get_Current(cls: Windows.ApplicationModel.IAppInfoStatics) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_classmethod
    def GetFromAppUserModelId(cls: Windows.ApplicationModel.IAppInfoStatics, appUserModelId: WinRT_String) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_classmethod
    def GetFromAppUserModelIdForUser(cls: Windows.ApplicationModel.IAppInfoStatics, user: Windows.System.User, appUserModelId: WinRT_String) -> Windows.ApplicationModel.AppInfo: ...
    Id = property(get_Id, None)
    AppUserModelId = property(get_AppUserModelId, None)
    DisplayInfo = property(get_DisplayInfo, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    Package = property(get_Package, None)
    ExecutionContext = property(get_ExecutionContext, None)
    SupportedFileExtensions = property(get_SupportedFileExtensions, None)
    Current = property(get_Current, None)
class AppInstallerInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppInstallerInfo'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.IAppInstallerInfo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_OnLaunch(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_HoursBetweenUpdateChecks(self: Windows.ApplicationModel.IAppInstallerInfo2) -> UInt32: ...
    @winrt_mixinmethod
    def get_ShowPrompt(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_UpdateBlocksActivation(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutomaticBackgroundTask(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ForceUpdateFromAnyVersion(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAutoRepairEnabled(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.ApplicationModel.PackageVersion: ...
    @winrt_mixinmethod
    def get_LastChecked(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PausedUntil(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_UpdateUris(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_RepairUris(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_DependencyPackageUris(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_OptionalPackageUris(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_PolicySource(self: Windows.ApplicationModel.IAppInstallerInfo2) -> Windows.ApplicationModel.AppInstallerPolicySource: ...
    Uri = property(get_Uri, None)
    OnLaunch = property(get_OnLaunch, None)
    HoursBetweenUpdateChecks = property(get_HoursBetweenUpdateChecks, None)
    ShowPrompt = property(get_ShowPrompt, None)
    UpdateBlocksActivation = property(get_UpdateBlocksActivation, None)
    AutomaticBackgroundTask = property(get_AutomaticBackgroundTask, None)
    ForceUpdateFromAnyVersion = property(get_ForceUpdateFromAnyVersion, None)
    IsAutoRepairEnabled = property(get_IsAutoRepairEnabled, None)
    Version = property(get_Version, None)
    LastChecked = property(get_LastChecked, None)
    PausedUntil = property(get_PausedUntil, None)
    UpdateUris = property(get_UpdateUris, None)
    RepairUris = property(get_RepairUris, None)
    DependencyPackageUris = property(get_DependencyPackageUris, None)
    OptionalPackageUris = property(get_OptionalPackageUris, None)
    PolicySource = property(get_PolicySource, None)
AppInstallerPolicySource = Int32
AppInstallerPolicySource_Default: AppInstallerPolicySource = 0
AppInstallerPolicySource_System: AppInstallerPolicySource = 1
class AppInstance(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.AppInstance'
    @winrt_mixinmethod
    def get_Key(self: Windows.ApplicationModel.IAppInstance) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsCurrentInstance(self: Windows.ApplicationModel.IAppInstance) -> Boolean: ...
    @winrt_mixinmethod
    def RedirectActivationTo(self: Windows.ApplicationModel.IAppInstance) -> Void: ...
    @winrt_classmethod
    def get_RecommendedInstance(cls: Windows.ApplicationModel.IAppInstanceStatics) -> Windows.ApplicationModel.AppInstance: ...
    @winrt_classmethod
    def GetActivatedEventArgs(cls: Windows.ApplicationModel.IAppInstanceStatics) -> Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_classmethod
    def FindOrRegisterInstanceForKey(cls: Windows.ApplicationModel.IAppInstanceStatics, key: WinRT_String) -> Windows.ApplicationModel.AppInstance: ...
    @winrt_classmethod
    def Unregister(cls: Windows.ApplicationModel.IAppInstanceStatics) -> Void: ...
    @winrt_classmethod
    def GetInstances(cls: Windows.ApplicationModel.IAppInstanceStatics) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.AppInstance]: ...
    Key = property(get_Key, None)
    IsCurrentInstance = property(get_IsCurrentInstance, None)
    RecommendedInstance = property(get_RecommendedInstance, None)
class DesignMode(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DesignMode'
    @winrt_classmethod
    def get_DesignMode2Enabled(cls: Windows.ApplicationModel.IDesignModeStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_DesignModeEnabled(cls: Windows.ApplicationModel.IDesignModeStatics) -> Boolean: ...
    DesignMode2Enabled = property(get_DesignMode2Enabled, None)
    DesignModeEnabled = property(get_DesignModeEnabled, None)
class EnteredBackgroundEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.EnteredBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> Windows.Foundation.Deferral: ...
class FindRelatedPackagesOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.FindRelatedPackagesOptions'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.ApplicationModel.IFindRelatedPackagesOptionsFactory, Relationship: Windows.ApplicationModel.PackageRelationship) -> Windows.ApplicationModel.FindRelatedPackagesOptions: ...
    @winrt_mixinmethod
    def get_Relationship(self: Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Windows.ApplicationModel.PackageRelationship: ...
    @winrt_mixinmethod
    def put_Relationship(self: Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Windows.ApplicationModel.PackageRelationship) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeFrameworks(self: Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeFrameworks(self: Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeHostRuntimes(self: Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeHostRuntimes(self: Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeOptionals(self: Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeOptionals(self: Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeResources(self: Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeResources(self: Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    Relationship = property(get_Relationship, put_Relationship)
    IncludeFrameworks = property(get_IncludeFrameworks, put_IncludeFrameworks)
    IncludeHostRuntimes = property(get_IncludeHostRuntimes, put_IncludeHostRuntimes)
    IncludeOptionals = property(get_IncludeOptionals, put_IncludeOptionals)
    IncludeResources = property(get_IncludeResources, put_IncludeResources)
class IAppDisplayInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1aeb1103-e4d4-41aa-a4-f6-c4-a2-76-e7-9e-ac')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetLogo(self, size: Windows.Foundation.Size) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
class IAppInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cf7f59b3-6a09-4de8-a6-c0-57-92-d5-68-80-d1')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayInfo(self) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(9)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    AppUserModelId = property(get_AppUserModelId, None)
    DisplayInfo = property(get_DisplayInfo, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('be4b1f5a-2098-431b-bd-25-b3-08-78-74-8d-47')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class IAppInfo3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09a78e46-93a4-46de-93-97-08-43-b5-71-15-ea')
    @winrt_commethod(6)
    def get_ExecutionContext(self) -> Windows.ApplicationModel.AppExecutionContext: ...
    ExecutionContext = property(get_ExecutionContext, None)
class IAppInfo4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f34bdeb-1609-4554-9f-33-12-e1-e8-03-e0-d4')
    @winrt_commethod(6)
    def get_SupportedFileExtensions(self) -> POINTER(WinRT_String): ...
    SupportedFileExtensions = property(get_SupportedFileExtensions, None)
class IAppInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cf1f782a-e48b-4f0c-9b-0b-79-c3-f8-95-7d-d7')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def GetFromAppUserModelId(self, appUserModelId: WinRT_String) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(8)
    def GetFromAppUserModelIdForUser(self, user: Windows.System.User, appUserModelId: WinRT_String) -> Windows.ApplicationModel.AppInfo: ...
    Current = property(get_Current, None)
class IAppInstallerInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29ab2ac0-d4f6-42a3-ad-cd-d6-58-3c-65-95-08')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IAppInstallerInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d20f1388-8256-597c-85-11-c8-4e-c5-0d-5e-2b')
    @winrt_commethod(6)
    def get_OnLaunch(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HoursBetweenUpdateChecks(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ShowPrompt(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_UpdateBlocksActivation(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_AutomaticBackgroundTask(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_ForceUpdateFromAnyVersion(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsAutoRepairEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_Version(self) -> Windows.ApplicationModel.PackageVersion: ...
    @winrt_commethod(14)
    def get_LastChecked(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_PausedUntil(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(16)
    def get_UpdateUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(17)
    def get_RepairUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(18)
    def get_DependencyPackageUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(19)
    def get_OptionalPackageUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(20)
    def get_PolicySource(self) -> Windows.ApplicationModel.AppInstallerPolicySource: ...
    OnLaunch = property(get_OnLaunch, None)
    HoursBetweenUpdateChecks = property(get_HoursBetweenUpdateChecks, None)
    ShowPrompt = property(get_ShowPrompt, None)
    UpdateBlocksActivation = property(get_UpdateBlocksActivation, None)
    AutomaticBackgroundTask = property(get_AutomaticBackgroundTask, None)
    ForceUpdateFromAnyVersion = property(get_ForceUpdateFromAnyVersion, None)
    IsAutoRepairEnabled = property(get_IsAutoRepairEnabled, None)
    Version = property(get_Version, None)
    LastChecked = property(get_LastChecked, None)
    PausedUntil = property(get_PausedUntil, None)
    UpdateUris = property(get_UpdateUris, None)
    RepairUris = property(get_RepairUris, None)
    DependencyPackageUris = property(get_DependencyPackageUris, None)
    OptionalPackageUris = property(get_OptionalPackageUris, None)
    PolicySource = property(get_PolicySource, None)
class IAppInstance(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('675f2b47-f25f-4532-9f-d6-36-33-e0-63-4d-01')
    @winrt_commethod(6)
    def get_Key(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsCurrentInstance(self) -> Boolean: ...
    @winrt_commethod(8)
    def RedirectActivationTo(self) -> Void: ...
    Key = property(get_Key, None)
    IsCurrentInstance = property(get_IsCurrentInstance, None)
class IAppInstanceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9d11e77f-9ea6-47af-a6-ec-46-78-4c-5b-a2-54')
    @winrt_commethod(6)
    def get_RecommendedInstance(self) -> Windows.ApplicationModel.AppInstance: ...
    @winrt_commethod(7)
    def GetActivatedEventArgs(self) -> Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_commethod(8)
    def FindOrRegisterInstanceForKey(self, key: WinRT_String) -> Windows.ApplicationModel.AppInstance: ...
    @winrt_commethod(9)
    def Unregister(self) -> Void: ...
    @winrt_commethod(10)
    def GetInstances(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.AppInstance]: ...
    RecommendedInstance = property(get_RecommendedInstance, None)
class IDesignModeStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c3893cc-f81a-4e7a-b8-57-76-a8-08-87-e1-85')
    @winrt_commethod(6)
    def get_DesignModeEnabled(self) -> Boolean: ...
    DesignModeEnabled = property(get_DesignModeEnabled, None)
class IDesignModeStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('80cf8137-b064-4858-be-c8-3e-ba-22-35-75-35')
    @winrt_commethod(6)
    def get_DesignMode2Enabled(self) -> Boolean: ...
    DesignMode2Enabled = property(get_DesignMode2Enabled, None)
class IEnteredBackgroundEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f722dcc2-9827-403d-aa-ed-ec-ca-9a-c1-73-98')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IFindRelatedPackagesOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('41dd7eea-b335-521f-b9-6c-5e-a0-7f-5b-73-29')
    @winrt_commethod(6)
    def get_Relationship(self) -> Windows.ApplicationModel.PackageRelationship: ...
    @winrt_commethod(7)
    def put_Relationship(self, value: Windows.ApplicationModel.PackageRelationship) -> Void: ...
    @winrt_commethod(8)
    def get_IncludeFrameworks(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IncludeFrameworks(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IncludeHostRuntimes(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IncludeHostRuntimes(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IncludeOptionals(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IncludeOptionals(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IncludeResources(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IncludeResources(self, value: Boolean) -> Void: ...
    Relationship = property(get_Relationship, put_Relationship)
    IncludeFrameworks = property(get_IncludeFrameworks, put_IncludeFrameworks)
    IncludeHostRuntimes = property(get_IncludeHostRuntimes, put_IncludeHostRuntimes)
    IncludeOptionals = property(get_IncludeOptionals, put_IncludeOptionals)
    IncludeResources = property(get_IncludeResources, put_IncludeResources)
class IFindRelatedPackagesOptionsFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d7d17254-a4fd-55c4-98-cf-f2-71-0b-7d-8b-e2')
    @winrt_commethod(6)
    def CreateInstance(self, Relationship: Windows.ApplicationModel.PackageRelationship) -> Windows.ApplicationModel.FindRelatedPackagesOptions: ...
class ILeavingBackgroundEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('39c6ec9a-ae6e-46f9-a0-7a-cf-c2-3f-88-73-3e')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class ILimitedAccessFeatureRequestResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d45156a6-1e24-5ddd-ab-b4-61-88-ab-a4-d5-bf')
    @winrt_commethod(6)
    def get_FeatureId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.ApplicationModel.LimitedAccessFeatureStatus: ...
    @winrt_commethod(8)
    def get_EstimatedRemovalDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    FeatureId = property(get_FeatureId, None)
    Status = property(get_Status, None)
    EstimatedRemovalDate = property(get_EstimatedRemovalDate, None)
class ILimitedAccessFeaturesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8be612d4-302b-5fbf-a6-32-1a-99-e4-3e-89-25')
    @winrt_commethod(6)
    def TryUnlockFeature(self, featureId: WinRT_String, token: WinRT_String, attestation: WinRT_String) -> Windows.ApplicationModel.LimitedAccessFeatureRequestResult: ...
class IPackage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('163c792f-bd75-413c-bf-23-b1-fe-7b-95-d8-25')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.ApplicationModel.PackageId: ...
    @winrt_commethod(7)
    def get_InstalledLocation(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_IsFramework(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Dependencies(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    Id = property(get_Id, None)
    InstalledLocation = property(get_InstalledLocation, None)
    IsFramework = property(get_IsFramework, None)
    Dependencies = property(get_Dependencies, None)
class IPackage2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a6612fb6-7688-4ace-95-fb-35-95-38-e7-aa-01')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PublisherDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Logo(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_IsResourcePackage(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsBundle(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDevelopmentMode(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    PublisherDisplayName = property(get_PublisherDisplayName, None)
    Description = property(get_Description, None)
    Logo = property(get_Logo, None)
    IsResourcePackage = property(get_IsResourcePackage, None)
    IsBundle = property(get_IsBundle, None)
    IsDevelopmentMode = property(get_IsDevelopmentMode, None)
class IPackage3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f738b61-f86a-4917-93-d1-f1-ee-9d-3b-35-d9')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.PackageStatus: ...
    @winrt_commethod(7)
    def get_InstalledDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetAppListEntriesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.AppListEntry]]: ...
    Status = property(get_Status, None)
    InstalledDate = property(get_InstalledDate, None)
class IPackage4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('65aed1ae-b95b-450c-88-2b-62-55-18-7f-39-7e')
    @winrt_commethod(6)
    def get_SignatureKind(self) -> Windows.ApplicationModel.PackageSignatureKind: ...
    @winrt_commethod(7)
    def get_IsOptional(self) -> Boolean: ...
    @winrt_commethod(8)
    def VerifyContentIntegrityAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SignatureKind = property(get_SignatureKind, None)
    IsOptional = property(get_IsOptional, None)
class IPackage5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0e842dd4-d9ac-45ed-9a-1e-74-ce-05-6b-26-35')
    @winrt_commethod(6)
    def GetContentGroupsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(7)
    def GetContentGroupAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageContentGroup]: ...
    @winrt_commethod(8)
    def StageContentGroupsAsync(self, names: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(9)
    def StageContentGroupsWithPriorityAsync(self, names: Windows.Foundation.Collections.IIterable[WinRT_String], moveToHeadOfQueue: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(10)
    def SetInUseAsync(self, inUse: Boolean) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPackage6(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8b1ad942-12d7-4754-ae-4e-63-8c-bc-0e-3a-2e')
    @winrt_commethod(6)
    def GetAppInstallerInfo(self) -> Windows.ApplicationModel.AppInstallerInfo: ...
    @winrt_commethod(7)
    def CheckUpdateAvailabilityAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageUpdateAvailabilityResult]: ...
class IPackage7(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('86ff8d31-a2e4-45e0-97-32-28-3a-6d-88-fd-e1')
    @winrt_commethod(6)
    def get_MutableLocation(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_EffectiveLocation(self) -> Windows.Storage.StorageFolder: ...
    MutableLocation = property(get_MutableLocation, None)
    EffectiveLocation = property(get_EffectiveLocation, None)
class IPackage8(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c584f7b-ce2a-4be6-a0-93-77-cf-bb-2a-7e-a1')
    @winrt_commethod(6)
    def get_EffectiveExternalLocation(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_MachineExternalLocation(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_UserExternalLocation(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(9)
    def get_InstalledPath(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_MutablePath(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_EffectivePath(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_EffectiveExternalPath(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_MachineExternalPath(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_UserExternalPath(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def GetLogoAsRandomAccessStreamReference(self, size: Windows.Foundation.Size) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(16)
    def GetAppListEntries(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.AppListEntry]: ...
    @winrt_commethod(17)
    def get_IsStub(self) -> Boolean: ...
    EffectiveExternalLocation = property(get_EffectiveExternalLocation, None)
    MachineExternalLocation = property(get_MachineExternalLocation, None)
    UserExternalLocation = property(get_UserExternalLocation, None)
    InstalledPath = property(get_InstalledPath, None)
    MutablePath = property(get_MutablePath, None)
    EffectivePath = property(get_EffectivePath, None)
    EffectiveExternalPath = property(get_EffectiveExternalPath, None)
    MachineExternalPath = property(get_MachineExternalPath, None)
    UserExternalPath = property(get_UserExternalPath, None)
    IsStub = property(get_IsStub, None)
class IPackage9(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d5ab224f-d7e1-49ec-90-ce-72-0c-db-d0-2e-9c')
    @winrt_commethod(6)
    def FindRelatedPackages(self, options: Windows.ApplicationModel.FindRelatedPackagesOptions) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_SourceUriSchemeName(self) -> WinRT_String: ...
    SourceUriSchemeName = property(get_SourceUriSchemeName, None)
class IPackageCatalog(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('230a3751-9de3-4445-be-74-91-fb-32-5a-be-fe')
    @winrt_commethod(6)
    def add_PackageStaging(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageStagingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PackageStaging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PackageInstalling(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageInstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PackageInstalling(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PackageUpdating(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageUpdatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PackageUpdating(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PackageUninstalling(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageUninstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PackageUninstalling(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PackageStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PackageStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPackageCatalog2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96a60c36-8ff7-4344-b6-bf-ee-64-c2-20-7e-d2')
    @winrt_commethod(6)
    def add_PackageContentGroupStaging(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageContentGroupStagingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PackageContentGroupStaging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def AddOptionalPackageAsync(self, optionalPackageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult]: ...
class IPackageCatalog3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96dd5c88-8837-43f9-90-15-03-34-34-ba-14-f3')
    @winrt_commethod(6)
    def RemoveOptionalPackagesAsync(self, optionalPackageFamilyNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult]: ...
class IPackageCatalog4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c37c399b-44cc-4b7b-8b-af-79-6c-04-ea-d3-b9')
    @winrt_commethod(6)
    def AddResourcePackageAsync(self, resourcePackageFamilyName: WinRT_String, resourceID: WinRT_String, options: Windows.ApplicationModel.AddResourcePackageOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.ApplicationModel.PackageCatalogAddResourcePackageResult, Windows.ApplicationModel.PackageInstallProgress]: ...
    @winrt_commethod(7)
    def RemoveResourcePackagesAsync(self, resourcePackages: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult]: ...
class IPackageCatalogAddOptionalPackageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3bf10cd4-b4df-47b3-a9-63-e2-fa-83-2f-7d-d3')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Package = property(get_Package, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageCatalogAddResourcePackageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9636ce0d-3e17-493f-aa-08-cc-ec-6f-de-f6-99')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Package = property(get_Package, None)
    IsComplete = property(get_IsComplete, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageCatalogRemoveOptionalPackagesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29d2f97b-d974-4e64-93-59-22-ca-df-d7-98-28')
    @winrt_commethod(6)
    def get_PackagesRemoved(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    PackagesRemoved = property(get_PackagesRemoved, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageCatalogRemoveResourcePackagesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae719709-1a52-4321-87-b3-e5-a1-a1-79-81-a7')
    @winrt_commethod(6)
    def get_PackagesRemoved(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    PackagesRemoved = property(get_PackagesRemoved, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageCatalogStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a18c9696-e65b-4634-ba-21-5e-63-eb-72-44-a7')
    @winrt_commethod(6)
    def OpenForCurrentPackage(self) -> Windows.ApplicationModel.PackageCatalog: ...
    @winrt_commethod(7)
    def OpenForCurrentUser(self) -> Windows.ApplicationModel.PackageCatalog: ...
class IPackageCatalogStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4c11c159-9a28-598c-b1-85-55-e1-89-9b-2b-e4')
    @winrt_commethod(6)
    def OpenForPackage(self, package: Windows.ApplicationModel.Package) -> Windows.ApplicationModel.PackageCatalog: ...
class IPackageContentGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8f62695d-120a-4798-b5-e1-58-00-dd-a8-f2-e1')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.ApplicationModel.PackageContentGroupState: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    Package = property(get_Package, None)
    Name = property(get_Name, None)
    State = property(get_State, None)
    IsRequired = property(get_IsRequired, None)
class IPackageContentGroupStagingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d7bc27e-6f27-446c-98-6e-d4-73-3d-4d-91-13')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(11)
    def get_ContentGroupName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_IsContentGroupRequired(self) -> Boolean: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
    ContentGroupName = property(get_ContentGroupName, None)
    IsContentGroupRequired = property(get_IsContentGroupRequired, None)
class IPackageContentGroupStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('70ee7619-5f12-4b92-b9-ea-6c-ca-da-13-bc-75')
    @winrt_commethod(6)
    def get_RequiredGroupName(self) -> WinRT_String: ...
    RequiredGroupName = property(get_RequiredGroupName, None)
class IPackageId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1adb665e-37c7-4790-99-80-dd-7a-e7-4e-8b-b2')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Version(self) -> Windows.ApplicationModel.PackageVersion: ...
    @winrt_commethod(8)
    def get_Architecture(self) -> Windows.System.ProcessorArchitecture: ...
    @winrt_commethod(9)
    def get_ResourceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PublisherId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_FullName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_FamilyName(self) -> WinRT_String: ...
    Name = property(get_Name, None)
    Version = property(get_Version, None)
    Architecture = property(get_Architecture, None)
    ResourceId = property(get_ResourceId, None)
    Publisher = property(get_Publisher, None)
    PublisherId = property(get_PublisherId, None)
    FullName = property(get_FullName, None)
    FamilyName = property(get_FamilyName, None)
class IPackageIdWithMetadata(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40577a7c-0c9e-443d-90-74-85-5f-5c-e0-a0-8d')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Author(self) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    Author = property(get_Author, None)
class IPackageInstallingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('97741eb7-ab7a-401a-8b-61-eb-0e-7f-af-f2-37')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class IPackageStagingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1041682d-54e2-4f51-b8-28-9e-f7-04-6c-21-0f')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class IPackageStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e534bdf-2960-4878-97-a4-96-24-de-b7-2f-2d')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.ApplicationModel.Package: ...
    Current = property(get_Current, None)
class IPackageStatus(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5fe74f71-a365-4c09-a0-2d-04-6d-52-5e-a1-da')
    @winrt_commethod(6)
    def VerifyIsOK(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_NotAvailable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_PackageOffline(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_DataOffline(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Disabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_NeedsRemediation(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_LicenseIssue(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_Modified(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_Tampered(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_DependencyIssue(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Servicing(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_DeploymentInProgress(self) -> Boolean: ...
    NotAvailable = property(get_NotAvailable, None)
    PackageOffline = property(get_PackageOffline, None)
    DataOffline = property(get_DataOffline, None)
    Disabled = property(get_Disabled, None)
    NeedsRemediation = property(get_NeedsRemediation, None)
    LicenseIssue = property(get_LicenseIssue, None)
    Modified = property(get_Modified, None)
    Tampered = property(get_Tampered, None)
    DependencyIssue = property(get_DependencyIssue, None)
    Servicing = property(get_Servicing, None)
    DeploymentInProgress = property(get_DeploymentInProgress, None)
class IPackageStatus2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f428fa93-7c56-4862-ac-fa-ab-ae-dc-c0-69-4d')
    @winrt_commethod(6)
    def get_IsPartiallyStaged(self) -> Boolean: ...
    IsPartiallyStaged = property(get_IsPartiallyStaged, None)
class IPackageStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('437d714d-bd80-4a70-bc-50-f6-e7-96-50-95-75')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class IPackageUninstallingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4443aa52-ab22-44cd-82-bb-4e-c9-b8-27-36-7a')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class IPackageUpdateAvailabilityResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('114e5009-199a-48a1-a0-79-31-3c-45-63-4a-71')
    @winrt_commethod(6)
    def get_Availability(self) -> Windows.ApplicationModel.PackageUpdateAvailability: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Availability = property(get_Availability, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageUpdatingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd7b4228-fd74-443e-b1-14-23-e6-77-b0-e8-6f')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SourcePackage(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_TargetPackage(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(9)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(10)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    SourcePackage = property(get_SourcePackage, None)
    TargetPackage = property(get_TargetPackage, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class IPackageWithMetadata(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95949780-1de9-40f2-b4-52-0d-e9-f1-91-00-12')
    @winrt_commethod(6)
    def get_InstallDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def GetThumbnailToken(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def Launch(self, parameters: WinRT_String) -> Void: ...
    InstallDate = property(get_InstallDate, None)
class IStartupTask(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f75c23c8-b5f2-4f6c-88-dd-36-cb-1d-59-9d-17')
    @winrt_commethod(6)
    def RequestEnableAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.StartupTaskState]: ...
    @winrt_commethod(7)
    def Disable(self) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.ApplicationModel.StartupTaskState: ...
    @winrt_commethod(9)
    def get_TaskId(self) -> WinRT_String: ...
    State = property(get_State, None)
    TaskId = property(get_TaskId, None)
class IStartupTaskStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ee5b60bd-a148-41a7-b2-6e-e8-b8-8a-1e-62-f8')
    @winrt_commethod(6)
    def GetForCurrentPackageAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.StartupTask]]: ...
    @winrt_commethod(7)
    def GetAsync(self, taskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.StartupTask]: ...
class ISuspendingDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59140509-8bc9-4eb4-b6-36-da-bd-c4-f4-6f-66')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISuspendingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96061c05-2dba-4d08-b0-bd-2b-30-a1-31-c6-aa')
    @winrt_commethod(6)
    def get_SuspendingOperation(self) -> Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class ISuspendingOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9da4ca41-20e1-4e9b-9f-65-a9-f4-35-34-0c-3a')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class LeavingBackgroundEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LeavingBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> Windows.Foundation.Deferral: ...
class LimitedAccessFeatureRequestResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LimitedAccessFeatureRequestResult'
    @winrt_mixinmethod
    def get_FeatureId(self: Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> Windows.ApplicationModel.LimitedAccessFeatureStatus: ...
    @winrt_mixinmethod
    def get_EstimatedRemovalDate(self: Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    FeatureId = property(get_FeatureId, None)
    Status = property(get_Status, None)
    EstimatedRemovalDate = property(get_EstimatedRemovalDate, None)
LimitedAccessFeatureStatus = Int32
LimitedAccessFeatureStatus_Unavailable: LimitedAccessFeatureStatus = 0
LimitedAccessFeatureStatus_Available: LimitedAccessFeatureStatus = 1
LimitedAccessFeatureStatus_AvailableWithoutToken: LimitedAccessFeatureStatus = 2
LimitedAccessFeatureStatus_Unknown: LimitedAccessFeatureStatus = 3
class LimitedAccessFeatures(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.LimitedAccessFeatures'
    @winrt_classmethod
    def TryUnlockFeature(cls: Windows.ApplicationModel.ILimitedAccessFeaturesStatics, featureId: WinRT_String, token: WinRT_String, attestation: WinRT_String) -> Windows.ApplicationModel.LimitedAccessFeatureRequestResult: ...
class Package(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Package'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.IPackage) -> Windows.ApplicationModel.PackageId: ...
    @winrt_mixinmethod
    def get_InstalledLocation(self: Windows.ApplicationModel.IPackage) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_IsFramework(self: Windows.ApplicationModel.IPackage) -> Boolean: ...
    @winrt_mixinmethod
    def get_Dependencies(self: Windows.ApplicationModel.IPackage) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublisherDisplayName(self: Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Logo(self: Windows.ApplicationModel.IPackage2) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsResourcePackage(self: Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBundle(self: Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDevelopmentMode(self: Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.IPackage3) -> Windows.ApplicationModel.PackageStatus: ...
    @winrt_mixinmethod
    def get_InstalledDate(self: Windows.ApplicationModel.IPackage3) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetAppListEntriesAsync(self: Windows.ApplicationModel.IPackage3) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.AppListEntry]]: ...
    @winrt_mixinmethod
    def get_InstallDate(self: Windows.ApplicationModel.IPackageWithMetadata) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetThumbnailToken(self: Windows.ApplicationModel.IPackageWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def Launch(self: Windows.ApplicationModel.IPackageWithMetadata, parameters: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignatureKind(self: Windows.ApplicationModel.IPackage4) -> Windows.ApplicationModel.PackageSignatureKind: ...
    @winrt_mixinmethod
    def get_IsOptional(self: Windows.ApplicationModel.IPackage4) -> Boolean: ...
    @winrt_mixinmethod
    def VerifyContentIntegrityAsync(self: Windows.ApplicationModel.IPackage4) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetContentGroupsAsync(self: Windows.ApplicationModel.IPackage5) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def GetContentGroupAsync(self: Windows.ApplicationModel.IPackage5, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageContentGroup]: ...
    @winrt_mixinmethod
    def StageContentGroupsAsync(self: Windows.ApplicationModel.IPackage5, names: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def StageContentGroupsWithPriorityAsync(self: Windows.ApplicationModel.IPackage5, names: Windows.Foundation.Collections.IIterable[WinRT_String], moveToHeadOfQueue: Boolean) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def SetInUseAsync(self: Windows.ApplicationModel.IPackage5, inUse: Boolean) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetAppInstallerInfo(self: Windows.ApplicationModel.IPackage6) -> Windows.ApplicationModel.AppInstallerInfo: ...
    @winrt_mixinmethod
    def CheckUpdateAvailabilityAsync(self: Windows.ApplicationModel.IPackage6) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageUpdateAvailabilityResult]: ...
    @winrt_mixinmethod
    def get_MutableLocation(self: Windows.ApplicationModel.IPackage7) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_EffectiveLocation(self: Windows.ApplicationModel.IPackage7) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_EffectiveExternalLocation(self: Windows.ApplicationModel.IPackage8) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_MachineExternalLocation(self: Windows.ApplicationModel.IPackage8) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_UserExternalLocation(self: Windows.ApplicationModel.IPackage8) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_InstalledPath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MutablePath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EffectivePath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EffectiveExternalPath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MachineExternalPath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserExternalPath(self: Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLogoAsRandomAccessStreamReference(self: Windows.ApplicationModel.IPackage8, size: Windows.Foundation.Size) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetAppListEntries(self: Windows.ApplicationModel.IPackage8) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.AppListEntry]: ...
    @winrt_mixinmethod
    def get_IsStub(self: Windows.ApplicationModel.IPackage8) -> Boolean: ...
    @winrt_mixinmethod
    def FindRelatedPackages(self: Windows.ApplicationModel.IPackage9, options: Windows.ApplicationModel.FindRelatedPackagesOptions) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_SourceUriSchemeName(self: Windows.ApplicationModel.IPackage9) -> WinRT_String: ...
    @winrt_classmethod
    def get_Current(cls: Windows.ApplicationModel.IPackageStatics) -> Windows.ApplicationModel.Package: ...
    Id = property(get_Id, None)
    InstalledLocation = property(get_InstalledLocation, None)
    IsFramework = property(get_IsFramework, None)
    Dependencies = property(get_Dependencies, None)
    DisplayName = property(get_DisplayName, None)
    PublisherDisplayName = property(get_PublisherDisplayName, None)
    Description = property(get_Description, None)
    Logo = property(get_Logo, None)
    IsResourcePackage = property(get_IsResourcePackage, None)
    IsBundle = property(get_IsBundle, None)
    IsDevelopmentMode = property(get_IsDevelopmentMode, None)
    Status = property(get_Status, None)
    InstalledDate = property(get_InstalledDate, None)
    InstallDate = property(get_InstallDate, None)
    SignatureKind = property(get_SignatureKind, None)
    IsOptional = property(get_IsOptional, None)
    MutableLocation = property(get_MutableLocation, None)
    EffectiveLocation = property(get_EffectiveLocation, None)
    EffectiveExternalLocation = property(get_EffectiveExternalLocation, None)
    MachineExternalLocation = property(get_MachineExternalLocation, None)
    UserExternalLocation = property(get_UserExternalLocation, None)
    InstalledPath = property(get_InstalledPath, None)
    MutablePath = property(get_MutablePath, None)
    EffectivePath = property(get_EffectivePath, None)
    EffectiveExternalPath = property(get_EffectiveExternalPath, None)
    MachineExternalPath = property(get_MachineExternalPath, None)
    UserExternalPath = property(get_UserExternalPath, None)
    IsStub = property(get_IsStub, None)
    SourceUriSchemeName = property(get_SourceUriSchemeName, None)
    Current = property(get_Current, None)
class PackageCatalog(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageCatalog'
    @winrt_mixinmethod
    def add_PackageStaging(self: Windows.ApplicationModel.IPackageCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageStagingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStaging(self: Windows.ApplicationModel.IPackageCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageInstalling(self: Windows.ApplicationModel.IPackageCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageInstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageInstalling(self: Windows.ApplicationModel.IPackageCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdating(self: Windows.ApplicationModel.IPackageCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageUpdatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdating(self: Windows.ApplicationModel.IPackageCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUninstalling(self: Windows.ApplicationModel.IPackageCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageUninstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUninstalling(self: Windows.ApplicationModel.IPackageCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageStatusChanged(self: Windows.ApplicationModel.IPackageCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStatusChanged(self: Windows.ApplicationModel.IPackageCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageContentGroupStaging(self: Windows.ApplicationModel.IPackageCatalog2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.PackageCatalog, Windows.ApplicationModel.PackageContentGroupStagingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageContentGroupStaging(self: Windows.ApplicationModel.IPackageCatalog2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddOptionalPackageAsync(self: Windows.ApplicationModel.IPackageCatalog2, optionalPackageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult]: ...
    @winrt_mixinmethod
    def RemoveOptionalPackagesAsync(self: Windows.ApplicationModel.IPackageCatalog3, optionalPackageFamilyNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult]: ...
    @winrt_mixinmethod
    def AddResourcePackageAsync(self: Windows.ApplicationModel.IPackageCatalog4, resourcePackageFamilyName: WinRT_String, resourceID: WinRT_String, options: Windows.ApplicationModel.AddResourcePackageOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.ApplicationModel.PackageCatalogAddResourcePackageResult, Windows.ApplicationModel.PackageInstallProgress]: ...
    @winrt_mixinmethod
    def RemoveResourcePackagesAsync(self: Windows.ApplicationModel.IPackageCatalog4, resourcePackages: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Package]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult]: ...
    @winrt_classmethod
    def OpenForPackage(cls: Windows.ApplicationModel.IPackageCatalogStatics2, package: Windows.ApplicationModel.Package) -> Windows.ApplicationModel.PackageCatalog: ...
    @winrt_classmethod
    def OpenForCurrentPackage(cls: Windows.ApplicationModel.IPackageCatalogStatics) -> Windows.ApplicationModel.PackageCatalog: ...
    @winrt_classmethod
    def OpenForCurrentUser(cls: Windows.ApplicationModel.IPackageCatalogStatics) -> Windows.ApplicationModel.PackageCatalog: ...
class PackageCatalogAddOptionalPackageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult'
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult) -> Windows.Foundation.HResult: ...
    Package = property(get_Package, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageCatalogAddResourcePackageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageCatalogAddResourcePackageResult'
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> Windows.Foundation.HResult: ...
    Package = property(get_Package, None)
    IsComplete = property(get_IsComplete, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageCatalogRemoveOptionalPackagesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult'
    @winrt_mixinmethod
    def get_PackagesRemoved(self: Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult) -> Windows.Foundation.HResult: ...
    PackagesRemoved = property(get_PackagesRemoved, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageCatalogRemoveResourcePackagesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult'
    @winrt_mixinmethod
    def get_PackagesRemoved(self: Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult) -> Windows.Foundation.HResult: ...
    PackagesRemoved = property(get_PackagesRemoved, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageContentGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageContentGroup'
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageContentGroup) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.IPackageContentGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.ApplicationModel.IPackageContentGroup) -> Windows.ApplicationModel.PackageContentGroupState: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.ApplicationModel.IPackageContentGroup) -> Boolean: ...
    @winrt_classmethod
    def get_RequiredGroupName(cls: Windows.ApplicationModel.IPackageContentGroupStatics) -> WinRT_String: ...
    Package = property(get_Package, None)
    Name = property(get_Name, None)
    State = property(get_State, None)
    IsRequired = property(get_IsRequired, None)
    RequiredGroupName = property(get_RequiredGroupName, None)
class PackageContentGroupStagingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageContentGroupStagingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ContentGroupName(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsContentGroupRequired(self: Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Boolean: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
    ContentGroupName = property(get_ContentGroupName, None)
    IsContentGroupRequired = property(get_IsContentGroupRequired, None)
PackageContentGroupState = Int32
PackageContentGroupState_NotStaged: PackageContentGroupState = 0
PackageContentGroupState_Queued: PackageContentGroupState = 1
PackageContentGroupState_Staging: PackageContentGroupState = 2
PackageContentGroupState_Staged: PackageContentGroupState = 3
class PackageId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageId'
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.ApplicationModel.IPackageId) -> Windows.ApplicationModel.PackageVersion: ...
    @winrt_mixinmethod
    def get_Architecture(self: Windows.ApplicationModel.IPackageId) -> Windows.System.ProcessorArchitecture: ...
    @winrt_mixinmethod
    def get_ResourceId(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublisherId(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FullName(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FamilyName(self: Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.IPackageIdWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Author(self: Windows.ApplicationModel.IPackageIdWithMetadata) -> WinRT_String: ...
    Name = property(get_Name, None)
    Version = property(get_Version, None)
    Architecture = property(get_Architecture, None)
    ResourceId = property(get_ResourceId, None)
    Publisher = property(get_Publisher, None)
    PublisherId = property(get_PublisherId, None)
    FullName = property(get_FullName, None)
    FamilyName = property(get_FamilyName, None)
    ProductId = property(get_ProductId, None)
    Author = property(get_Author, None)
class PackageInstallProgress(EasyCastStructure):
    PercentComplete: UInt32
class PackageInstallingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageInstallingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.IPackageInstallingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageInstallingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.IPackageInstallingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageInstallingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.ApplicationModel.IPackageInstallingEventArgs) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
PackageRelationship = Int32
PackageRelationship_Dependencies: PackageRelationship = 0
PackageRelationship_Dependents: PackageRelationship = 1
PackageRelationship_All: PackageRelationship = 2
PackageSignatureKind = Int32
PackageSignatureKind_None: PackageSignatureKind = 0
PackageSignatureKind_Developer: PackageSignatureKind = 1
PackageSignatureKind_Enterprise: PackageSignatureKind = 2
PackageSignatureKind_Store: PackageSignatureKind = 3
PackageSignatureKind_System: PackageSignatureKind = 4
class PackageStagingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageStagingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.IPackageStagingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageStagingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.IPackageStagingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageStagingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.ApplicationModel.IPackageStagingEventArgs) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class PackageStatus(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageStatus'
    @winrt_mixinmethod
    def VerifyIsOK(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotAvailable(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_PackageOffline(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DataOffline(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Disabled(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_NeedsRemediation(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_LicenseIssue(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Modified(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Tampered(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DependencyIssue(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Servicing(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeploymentInProgress(self: Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPartiallyStaged(self: Windows.ApplicationModel.IPackageStatus2) -> Boolean: ...
    NotAvailable = property(get_NotAvailable, None)
    PackageOffline = property(get_PackageOffline, None)
    DataOffline = property(get_DataOffline, None)
    Disabled = property(get_Disabled, None)
    NeedsRemediation = property(get_NeedsRemediation, None)
    LicenseIssue = property(get_LicenseIssue, None)
    Modified = property(get_Modified, None)
    Tampered = property(get_Tampered, None)
    DependencyIssue = property(get_DependencyIssue, None)
    Servicing = property(get_Servicing, None)
    DeploymentInProgress = property(get_DeploymentInProgress, None)
    IsPartiallyStaged = property(get_IsPartiallyStaged, None)
class PackageStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageStatusChangedEventArgs) -> Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class PackageUninstallingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageUninstallingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
PackageUpdateAvailability = Int32
PackageUpdateAvailability_Unknown: PackageUpdateAvailability = 0
PackageUpdateAvailability_NoUpdates: PackageUpdateAvailability = 1
PackageUpdateAvailability_Available: PackageUpdateAvailability = 2
PackageUpdateAvailability_Required: PackageUpdateAvailability = 3
PackageUpdateAvailability_Error: PackageUpdateAvailability = 4
class PackageUpdateAvailabilityResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageUpdateAvailabilityResult'
    @winrt_mixinmethod
    def get_Availability(self: Windows.ApplicationModel.IPackageUpdateAvailabilityResult) -> Windows.ApplicationModel.PackageUpdateAvailability: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.IPackageUpdateAvailabilityResult) -> Windows.Foundation.HResult: ...
    Availability = property(get_Availability, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageUpdatingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.PackageUpdatingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_SourcePackage(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_TargetPackage(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    SourcePackage = property(get_SourcePackage, None)
    TargetPackage = property(get_TargetPackage, None)
    Progress = property(get_Progress, None)
    IsComplete = property(get_IsComplete, None)
    ErrorCode = property(get_ErrorCode, None)
class PackageVersion(EasyCastStructure):
    Major: UInt16
    Minor: UInt16
    Build: UInt16
    Revision: UInt16
class StartupTask(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.StartupTask'
    @winrt_mixinmethod
    def RequestEnableAsync(self: Windows.ApplicationModel.IStartupTask) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.StartupTaskState]: ...
    @winrt_mixinmethod
    def Disable(self: Windows.ApplicationModel.IStartupTask) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.ApplicationModel.IStartupTask) -> Windows.ApplicationModel.StartupTaskState: ...
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.IStartupTask) -> WinRT_String: ...
    @winrt_classmethod
    def GetForCurrentPackageAsync(cls: Windows.ApplicationModel.IStartupTaskStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.StartupTask]]: ...
    @winrt_classmethod
    def GetAsync(cls: Windows.ApplicationModel.IStartupTaskStatics, taskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.StartupTask]: ...
    State = property(get_State, None)
    TaskId = property(get_TaskId, None)
StartupTaskContract: UInt32 = 196608
StartupTaskState = Int32
StartupTaskState_Disabled: StartupTaskState = 0
StartupTaskState_DisabledByUser: StartupTaskState = 1
StartupTaskState_Enabled: StartupTaskState = 2
StartupTaskState_DisabledByPolicy: StartupTaskState = 3
StartupTaskState_EnabledByPolicy: StartupTaskState = 4
class SuspendingDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.SuspendingDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.ISuspendingDeferral) -> Void: ...
class SuspendingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.SuspendingEventArgs'
    @winrt_mixinmethod
    def get_SuspendingOperation(self: Windows.ApplicationModel.ISuspendingEventArgs) -> Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class SuspendingOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.SuspendingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.ISuspendingOperation) -> Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.ApplicationModel.ISuspendingOperation) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
make_head(_module, 'AppDisplayInfo')
make_head(_module, 'AppInfo')
make_head(_module, 'AppInstallerInfo')
make_head(_module, 'AppInstance')
make_head(_module, 'DesignMode')
make_head(_module, 'EnteredBackgroundEventArgs')
make_head(_module, 'FindRelatedPackagesOptions')
make_head(_module, 'IAppDisplayInfo')
make_head(_module, 'IAppInfo')
make_head(_module, 'IAppInfo2')
make_head(_module, 'IAppInfo3')
make_head(_module, 'IAppInfo4')
make_head(_module, 'IAppInfoStatics')
make_head(_module, 'IAppInstallerInfo')
make_head(_module, 'IAppInstallerInfo2')
make_head(_module, 'IAppInstance')
make_head(_module, 'IAppInstanceStatics')
make_head(_module, 'IDesignModeStatics')
make_head(_module, 'IDesignModeStatics2')
make_head(_module, 'IEnteredBackgroundEventArgs')
make_head(_module, 'IFindRelatedPackagesOptions')
make_head(_module, 'IFindRelatedPackagesOptionsFactory')
make_head(_module, 'ILeavingBackgroundEventArgs')
make_head(_module, 'ILimitedAccessFeatureRequestResult')
make_head(_module, 'ILimitedAccessFeaturesStatics')
make_head(_module, 'IPackage')
make_head(_module, 'IPackage2')
make_head(_module, 'IPackage3')
make_head(_module, 'IPackage4')
make_head(_module, 'IPackage5')
make_head(_module, 'IPackage6')
make_head(_module, 'IPackage7')
make_head(_module, 'IPackage8')
make_head(_module, 'IPackage9')
make_head(_module, 'IPackageCatalog')
make_head(_module, 'IPackageCatalog2')
make_head(_module, 'IPackageCatalog3')
make_head(_module, 'IPackageCatalog4')
make_head(_module, 'IPackageCatalogAddOptionalPackageResult')
make_head(_module, 'IPackageCatalogAddResourcePackageResult')
make_head(_module, 'IPackageCatalogRemoveOptionalPackagesResult')
make_head(_module, 'IPackageCatalogRemoveResourcePackagesResult')
make_head(_module, 'IPackageCatalogStatics')
make_head(_module, 'IPackageCatalogStatics2')
make_head(_module, 'IPackageContentGroup')
make_head(_module, 'IPackageContentGroupStagingEventArgs')
make_head(_module, 'IPackageContentGroupStatics')
make_head(_module, 'IPackageId')
make_head(_module, 'IPackageIdWithMetadata')
make_head(_module, 'IPackageInstallingEventArgs')
make_head(_module, 'IPackageStagingEventArgs')
make_head(_module, 'IPackageStatics')
make_head(_module, 'IPackageStatus')
make_head(_module, 'IPackageStatus2')
make_head(_module, 'IPackageStatusChangedEventArgs')
make_head(_module, 'IPackageUninstallingEventArgs')
make_head(_module, 'IPackageUpdateAvailabilityResult')
make_head(_module, 'IPackageUpdatingEventArgs')
make_head(_module, 'IPackageWithMetadata')
make_head(_module, 'IStartupTask')
make_head(_module, 'IStartupTaskStatics')
make_head(_module, 'ISuspendingDeferral')
make_head(_module, 'ISuspendingEventArgs')
make_head(_module, 'ISuspendingOperation')
make_head(_module, 'LeavingBackgroundEventArgs')
make_head(_module, 'LimitedAccessFeatureRequestResult')
make_head(_module, 'LimitedAccessFeatures')
make_head(_module, 'Package')
make_head(_module, 'PackageCatalog')
make_head(_module, 'PackageCatalogAddOptionalPackageResult')
make_head(_module, 'PackageCatalogAddResourcePackageResult')
make_head(_module, 'PackageCatalogRemoveOptionalPackagesResult')
make_head(_module, 'PackageCatalogRemoveResourcePackagesResult')
make_head(_module, 'PackageContentGroup')
make_head(_module, 'PackageContentGroupStagingEventArgs')
make_head(_module, 'PackageId')
make_head(_module, 'PackageInstallProgress')
make_head(_module, 'PackageInstallingEventArgs')
make_head(_module, 'PackageStagingEventArgs')
make_head(_module, 'PackageStatus')
make_head(_module, 'PackageStatusChangedEventArgs')
make_head(_module, 'PackageUninstallingEventArgs')
make_head(_module, 'PackageUpdateAvailabilityResult')
make_head(_module, 'PackageUpdatingEventArgs')
make_head(_module, 'PackageVersion')
make_head(_module, 'StartupTask')
make_head(_module, 'SuspendingDeferral')
make_head(_module, 'SuspendingEventArgs')
make_head(_module, 'SuspendingOperation')
