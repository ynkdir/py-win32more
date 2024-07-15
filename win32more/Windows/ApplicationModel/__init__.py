from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class AddResourcePackageOptions(Enum, UInt32):
    None_ = 0
    ForceTargetAppShutdown = 1
    ApplyUpdateIfAvailable = 2
class AppDisplayInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IAppDisplayInfo
    _classid_ = 'Windows.ApplicationModel.AppDisplayInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.IAppDisplayInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.IAppDisplayInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLogo(self: win32more.Windows.ApplicationModel.IAppDisplayInfo, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
class AppExecutionContext(Enum, Int32):
    Unknown = 0
    Host = 1
    Guest = 2
class _AppInfo_Meta_(ComPtr.__class__):
    pass
class AppInfo(ComPtr, metaclass=_AppInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IAppInfo
    _classid_ = 'Windows.ApplicationModel.AppInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayInfo(self: win32more.Windows.ApplicationModel.IAppInfo) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.ApplicationModel.IAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IAppInfo2) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_ExecutionContext(self: win32more.Windows.ApplicationModel.IAppInfo3) -> win32more.Windows.ApplicationModel.AppExecutionContext: ...
    @winrt_mixinmethod
    def get_SupportedFileExtensions(self: win32more.Windows.ApplicationModel.IAppInfo4) -> ReceiveArray[WinRT_String]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.ApplicationModel.IAppInfoStatics) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_classmethod
    def GetFromAppUserModelId(cls: win32more.Windows.ApplicationModel.IAppInfoStatics, appUserModelId: WinRT_String) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_classmethod
    def GetFromAppUserModelIdForUser(cls: win32more.Windows.ApplicationModel.IAppInfoStatics, user: win32more.Windows.System.User, appUserModelId: WinRT_String) -> win32more.Windows.ApplicationModel.AppInfo: ...
    AppUserModelId = property(get_AppUserModelId, None)
    DisplayInfo = property(get_DisplayInfo, None)
    ExecutionContext = property(get_ExecutionContext, None)
    Id = property(get_Id, None)
    Package = property(get_Package, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    SupportedFileExtensions = property(get_SupportedFileExtensions, None)
    _AppInfo_Meta_.Current = property(get_Current, None)
class AppInstallerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IAppInstallerInfo
    _classid_ = 'Windows.ApplicationModel.AppInstallerInfo'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.IAppInstallerInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_OnLaunch(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_HoursBetweenUpdateChecks(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> UInt32: ...
    @winrt_mixinmethod
    def get_ShowPrompt(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_UpdateBlocksActivation(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutomaticBackgroundTask(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ForceUpdateFromAnyVersion(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAutoRepairEnabled(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_mixinmethod
    def get_LastChecked(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PausedUntil(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_UpdateUris(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_RepairUris(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_DependencyPackageUris(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_OptionalPackageUris(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_PolicySource(self: win32more.Windows.ApplicationModel.IAppInstallerInfo2) -> win32more.Windows.ApplicationModel.AppInstallerPolicySource: ...
    AutomaticBackgroundTask = property(get_AutomaticBackgroundTask, None)
    DependencyPackageUris = property(get_DependencyPackageUris, None)
    ForceUpdateFromAnyVersion = property(get_ForceUpdateFromAnyVersion, None)
    HoursBetweenUpdateChecks = property(get_HoursBetweenUpdateChecks, None)
    IsAutoRepairEnabled = property(get_IsAutoRepairEnabled, None)
    LastChecked = property(get_LastChecked, None)
    OnLaunch = property(get_OnLaunch, None)
    OptionalPackageUris = property(get_OptionalPackageUris, None)
    PausedUntil = property(get_PausedUntil, None)
    PolicySource = property(get_PolicySource, None)
    RepairUris = property(get_RepairUris, None)
    ShowPrompt = property(get_ShowPrompt, None)
    UpdateBlocksActivation = property(get_UpdateBlocksActivation, None)
    UpdateUris = property(get_UpdateUris, None)
    Uri = property(get_Uri, None)
    Version = property(get_Version, None)
class AppInstallerPolicySource(Enum, Int32):
    Default = 0
    System = 1
class _AppInstance_Meta_(ComPtr.__class__):
    pass
class AppInstance(ComPtr, metaclass=_AppInstance_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IAppInstance
    _classid_ = 'Windows.ApplicationModel.AppInstance'
    @winrt_mixinmethod
    def get_Key(self: win32more.Windows.ApplicationModel.IAppInstance) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsCurrentInstance(self: win32more.Windows.ApplicationModel.IAppInstance) -> Boolean: ...
    @winrt_mixinmethod
    def RedirectActivationTo(self: win32more.Windows.ApplicationModel.IAppInstance) -> Void: ...
    @winrt_classmethod
    def get_RecommendedInstance(cls: win32more.Windows.ApplicationModel.IAppInstanceStatics) -> win32more.Windows.ApplicationModel.AppInstance: ...
    @winrt_classmethod
    def GetActivatedEventArgs(cls: win32more.Windows.ApplicationModel.IAppInstanceStatics) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_classmethod
    def FindOrRegisterInstanceForKey(cls: win32more.Windows.ApplicationModel.IAppInstanceStatics, key: WinRT_String) -> win32more.Windows.ApplicationModel.AppInstance: ...
    @winrt_classmethod
    def Unregister(cls: win32more.Windows.ApplicationModel.IAppInstanceStatics) -> Void: ...
    @winrt_classmethod
    def GetInstances(cls: win32more.Windows.ApplicationModel.IAppInstanceStatics) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.AppInstance]: ...
    IsCurrentInstance = property(get_IsCurrentInstance, None)
    Key = property(get_Key, None)
    _AppInstance_Meta_.RecommendedInstance = property(get_RecommendedInstance, None)
class CameraApplicationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CameraApplicationManager'
    @winrt_classmethod
    def ShowInstalledApplicationsUI(cls: win32more.Windows.ApplicationModel.ICameraApplicationManagerStatics) -> Void: ...
class _DesignMode_Meta_(ComPtr.__class__):
    pass
class DesignMode(ComPtr, metaclass=_DesignMode_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DesignMode'
    @winrt_classmethod
    def get_DesignMode2Enabled(cls: win32more.Windows.ApplicationModel.IDesignModeStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_DesignModeEnabled(cls: win32more.Windows.ApplicationModel.IDesignModeStatics) -> Boolean: ...
    _DesignMode_Meta_.DesignMode2Enabled = property(get_DesignMode2Enabled, None)
    _DesignMode_Meta_.DesignModeEnabled = property(get_DesignModeEnabled, None)
class EnteredBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs
    _classid_ = 'Windows.ApplicationModel.EnteredBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class FindRelatedPackagesOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions
    _classid_ = 'Windows.ApplicationModel.FindRelatedPackagesOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.FindRelatedPackagesOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptionsFactory, Relationship: win32more.Windows.ApplicationModel.PackageRelationship) -> win32more.Windows.ApplicationModel.FindRelatedPackagesOptions: ...
    @winrt_mixinmethod
    def get_Relationship(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions) -> win32more.Windows.ApplicationModel.PackageRelationship: ...
    @winrt_mixinmethod
    def put_Relationship(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions, value: win32more.Windows.ApplicationModel.PackageRelationship) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeFrameworks(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeFrameworks(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeHostRuntimes(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeHostRuntimes(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeOptionals(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeOptionals(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeResources(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeResources(self: win32more.Windows.ApplicationModel.IFindRelatedPackagesOptions, value: Boolean) -> Void: ...
    IncludeFrameworks = property(get_IncludeFrameworks, put_IncludeFrameworks)
    IncludeHostRuntimes = property(get_IncludeHostRuntimes, put_IncludeHostRuntimes)
    IncludeOptionals = property(get_IncludeOptionals, put_IncludeOptionals)
    IncludeResources = property(get_IncludeResources, put_IncludeResources)
    Relationship = property(get_Relationship, put_Relationship)
FullTrustAppContract: UInt32 = 131072
class FullTrustLaunchResult(Enum, Int32):
    Success = 0
    AccessDenied = 1
    FileNotFound = 2
    Unknown = 3
class FullTrustProcessLaunchResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IFullTrustProcessLaunchResult
    _classid_ = 'Windows.ApplicationModel.FullTrustProcessLaunchResult'
    @winrt_mixinmethod
    def get_LaunchResult(self: win32more.Windows.ApplicationModel.IFullTrustProcessLaunchResult) -> win32more.Windows.ApplicationModel.FullTrustLaunchResult: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IFullTrustProcessLaunchResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    LaunchResult = property(get_LaunchResult, None)
class FullTrustProcessLauncher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.FullTrustProcessLauncher'
    @winrt_classmethod
    def LaunchFullTrustProcessForCurrentAppWithArgumentsAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics2, commandLine: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.FullTrustProcessLaunchResult]: ...
    @winrt_classmethod
    def LaunchFullTrustProcessForAppWithArgumentsAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics2, fullTrustPackageRelativeAppId: WinRT_String, commandLine: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.FullTrustProcessLaunchResult]: ...
    @winrt_classmethod
    def LaunchFullTrustProcessForCurrentAppAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def LaunchFullTrustProcessForCurrentAppWithParametersAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics, parameterGroupId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def LaunchFullTrustProcessForAppAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics, fullTrustPackageRelativeAppId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def LaunchFullTrustProcessForAppWithParametersAsync(cls: win32more.Windows.ApplicationModel.IFullTrustProcessLauncherStatics, fullTrustPackageRelativeAppId: WinRT_String, parameterGroupId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IAppDisplayInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppDisplayInfo'
    _iid_ = Guid('{1aeb1103-e4d4-41aa-a4f6-c4a276e79eac}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetLogo(self, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
class IAppInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInfo'
    _iid_ = Guid('{cf7f59b3-6a09-4de8-a6c0-5792d56880d1}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayInfo(self) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(9)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
    DisplayInfo = property(get_DisplayInfo, None)
    Id = property(get_Id, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInfo2'
    _iid_ = Guid('{be4b1f5a-2098-431b-bd25-b30878748d47}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class IAppInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInfo3'
    _iid_ = Guid('{09a78e46-93a4-46de-9397-0843b57115ea}')
    @winrt_commethod(6)
    def get_ExecutionContext(self) -> win32more.Windows.ApplicationModel.AppExecutionContext: ...
    ExecutionContext = property(get_ExecutionContext, None)
class IAppInfo4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInfo4'
    _iid_ = Guid('{2f34bdeb-1609-4554-9f33-12e1e803e0d4}')
    @winrt_commethod(6)
    def get_SupportedFileExtensions(self) -> ReceiveArray[WinRT_String]: ...
    SupportedFileExtensions = property(get_SupportedFileExtensions, None)
class IAppInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInfoStatics'
    _iid_ = Guid('{cf1f782a-e48b-4f0c-9b0b-79c3f8957dd7}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def GetFromAppUserModelId(self, appUserModelId: WinRT_String) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(8)
    def GetFromAppUserModelIdForUser(self, user: win32more.Windows.System.User, appUserModelId: WinRT_String) -> win32more.Windows.ApplicationModel.AppInfo: ...
    Current = property(get_Current, None)
class IAppInstallerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInstallerInfo'
    _iid_ = Guid('{29ab2ac0-d4f6-42a3-adcd-d6583c659508}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IAppInstallerInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInstallerInfo2'
    _iid_ = Guid('{d20f1388-8256-597c-8511-c84ec50d5e2b}')
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
    def get_Version(self) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_commethod(14)
    def get_LastChecked(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_PausedUntil(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(16)
    def get_UpdateUris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(17)
    def get_RepairUris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(18)
    def get_DependencyPackageUris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(19)
    def get_OptionalPackageUris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(20)
    def get_PolicySource(self) -> win32more.Windows.ApplicationModel.AppInstallerPolicySource: ...
    AutomaticBackgroundTask = property(get_AutomaticBackgroundTask, None)
    DependencyPackageUris = property(get_DependencyPackageUris, None)
    ForceUpdateFromAnyVersion = property(get_ForceUpdateFromAnyVersion, None)
    HoursBetweenUpdateChecks = property(get_HoursBetweenUpdateChecks, None)
    IsAutoRepairEnabled = property(get_IsAutoRepairEnabled, None)
    LastChecked = property(get_LastChecked, None)
    OnLaunch = property(get_OnLaunch, None)
    OptionalPackageUris = property(get_OptionalPackageUris, None)
    PausedUntil = property(get_PausedUntil, None)
    PolicySource = property(get_PolicySource, None)
    RepairUris = property(get_RepairUris, None)
    ShowPrompt = property(get_ShowPrompt, None)
    UpdateBlocksActivation = property(get_UpdateBlocksActivation, None)
    UpdateUris = property(get_UpdateUris, None)
    Version = property(get_Version, None)
class IAppInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInstance'
    _iid_ = Guid('{675f2b47-f25f-4532-9fd6-3633e0634d01}')
    @winrt_commethod(6)
    def get_Key(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsCurrentInstance(self) -> Boolean: ...
    @winrt_commethod(8)
    def RedirectActivationTo(self) -> Void: ...
    IsCurrentInstance = property(get_IsCurrentInstance, None)
    Key = property(get_Key, None)
class IAppInstanceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IAppInstanceStatics'
    _iid_ = Guid('{9d11e77f-9ea6-47af-a6ec-46784c5ba254}')
    @winrt_commethod(6)
    def get_RecommendedInstance(self) -> win32more.Windows.ApplicationModel.AppInstance: ...
    @winrt_commethod(7)
    def GetActivatedEventArgs(self) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_commethod(8)
    def FindOrRegisterInstanceForKey(self, key: WinRT_String) -> win32more.Windows.ApplicationModel.AppInstance: ...
    @winrt_commethod(9)
    def Unregister(self) -> Void: ...
    @winrt_commethod(10)
    def GetInstances(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.AppInstance]: ...
    RecommendedInstance = property(get_RecommendedInstance, None)
class ICameraApplicationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ICameraApplicationManagerStatics'
    _iid_ = Guid('{9599ddce-9bd3-435c-8054-c1add50028fe}')
    @winrt_commethod(6)
    def ShowInstalledApplicationsUI(self) -> Void: ...
class IDesignModeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IDesignModeStatics'
    _iid_ = Guid('{2c3893cc-f81a-4e7a-b857-76a80887e185}')
    @winrt_commethod(6)
    def get_DesignModeEnabled(self) -> Boolean: ...
    DesignModeEnabled = property(get_DesignModeEnabled, None)
class IDesignModeStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IDesignModeStatics2'
    _iid_ = Guid('{80cf8137-b064-4858-bec8-3eba22357535}')
    @winrt_commethod(6)
    def get_DesignMode2Enabled(self) -> Boolean: ...
    DesignMode2Enabled = property(get_DesignMode2Enabled, None)
class IEnteredBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IEnteredBackgroundEventArgs'
    _iid_ = Guid('{f722dcc2-9827-403d-aaed-ecca9ac17398}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IFindRelatedPackagesOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IFindRelatedPackagesOptions'
    _iid_ = Guid('{41dd7eea-b335-521f-b96c-5ea07f5b7329}')
    @winrt_commethod(6)
    def get_Relationship(self) -> win32more.Windows.ApplicationModel.PackageRelationship: ...
    @winrt_commethod(7)
    def put_Relationship(self, value: win32more.Windows.ApplicationModel.PackageRelationship) -> Void: ...
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
    IncludeFrameworks = property(get_IncludeFrameworks, put_IncludeFrameworks)
    IncludeHostRuntimes = property(get_IncludeHostRuntimes, put_IncludeHostRuntimes)
    IncludeOptionals = property(get_IncludeOptionals, put_IncludeOptionals)
    IncludeResources = property(get_IncludeResources, put_IncludeResources)
    Relationship = property(get_Relationship, put_Relationship)
class IFindRelatedPackagesOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IFindRelatedPackagesOptionsFactory'
    _iid_ = Guid('{d7d17254-a4fd-55c4-98cf-f2710b7d8be2}')
    @winrt_commethod(6)
    def CreateInstance(self, Relationship: win32more.Windows.ApplicationModel.PackageRelationship) -> win32more.Windows.ApplicationModel.FindRelatedPackagesOptions: ...
class IFullTrustProcessLaunchResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IFullTrustProcessLaunchResult'
    _iid_ = Guid('{8917d888-edfb-515f-8e22-5ebceb69dfd9}')
    @winrt_commethod(6)
    def get_LaunchResult(self) -> win32more.Windows.ApplicationModel.FullTrustLaunchResult: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    LaunchResult = property(get_LaunchResult, None)
class IFullTrustProcessLauncherStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IFullTrustProcessLauncherStatics'
    _iid_ = Guid('{d784837f-1100-3c6b-a455-f6262cc331b6}')
    @winrt_commethod(6)
    def LaunchFullTrustProcessForCurrentAppAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def LaunchFullTrustProcessForCurrentAppWithParametersAsync(self, parameterGroupId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def LaunchFullTrustProcessForAppAsync(self, fullTrustPackageRelativeAppId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def LaunchFullTrustProcessForAppWithParametersAsync(self, fullTrustPackageRelativeAppId: WinRT_String, parameterGroupId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IFullTrustProcessLauncherStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IFullTrustProcessLauncherStatics2'
    _iid_ = Guid('{8b8ed72f-b65c-56cf-a1a7-2bf77cbc6ea8}')
    @winrt_commethod(6)
    def LaunchFullTrustProcessForCurrentAppWithArgumentsAsync(self, commandLine: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.FullTrustProcessLaunchResult]: ...
    @winrt_commethod(7)
    def LaunchFullTrustProcessForAppWithArgumentsAsync(self, fullTrustPackageRelativeAppId: WinRT_String, commandLine: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.FullTrustProcessLaunchResult]: ...
class ILeavingBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ILeavingBackgroundEventArgs'
    _iid_ = Guid('{39c6ec9a-ae6e-46f9-a07a-cfc23f88733e}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class ILimitedAccessFeatureRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ILimitedAccessFeatureRequestResult'
    _iid_ = Guid('{d45156a6-1e24-5ddd-abb4-6188aba4d5bf}')
    @winrt_commethod(6)
    def get_FeatureId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.ApplicationModel.LimitedAccessFeatureStatus: ...
    @winrt_commethod(8)
    def get_EstimatedRemovalDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    EstimatedRemovalDate = property(get_EstimatedRemovalDate, None)
    FeatureId = property(get_FeatureId, None)
    Status = property(get_Status, None)
class ILimitedAccessFeaturesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ILimitedAccessFeaturesStatics'
    _iid_ = Guid('{8be612d4-302b-5fbf-a632-1a99e43e8925}')
    @winrt_commethod(6)
    def TryUnlockFeature(self, featureId: WinRT_String, token: WinRT_String, attestation: WinRT_String) -> win32more.Windows.ApplicationModel.LimitedAccessFeatureRequestResult: ...
class IPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage'
    _iid_ = Guid('{163c792f-bd75-413c-bf23-b1fe7b95d825}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.ApplicationModel.PackageId: ...
    @winrt_commethod(7)
    def get_InstalledLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_IsFramework(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Dependencies(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    Dependencies = property(get_Dependencies, None)
    Id = property(get_Id, None)
    InstalledLocation = property(get_InstalledLocation, None)
    IsFramework = property(get_IsFramework, None)
class IPackage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage2'
    _iid_ = Guid('{a6612fb6-7688-4ace-95fb-359538e7aa01}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PublisherDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Logo(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_IsResourcePackage(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsBundle(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDevelopmentMode(self) -> Boolean: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    IsBundle = property(get_IsBundle, None)
    IsDevelopmentMode = property(get_IsDevelopmentMode, None)
    IsResourcePackage = property(get_IsResourcePackage, None)
    Logo = property(get_Logo, None)
    PublisherDisplayName = property(get_PublisherDisplayName, None)
class IPackage3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage3'
    _iid_ = Guid('{5f738b61-f86a-4917-93d1-f1ee9d3b35d9}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.PackageStatus: ...
    @winrt_commethod(7)
    def get_InstalledDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetAppListEntriesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.AppListEntry]]: ...
    InstalledDate = property(get_InstalledDate, None)
    Status = property(get_Status, None)
class IPackage4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage4'
    _iid_ = Guid('{65aed1ae-b95b-450c-882b-6255187f397e}')
    @winrt_commethod(6)
    def get_SignatureKind(self) -> win32more.Windows.ApplicationModel.PackageSignatureKind: ...
    @winrt_commethod(7)
    def get_IsOptional(self) -> Boolean: ...
    @winrt_commethod(8)
    def VerifyContentIntegrityAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsOptional = property(get_IsOptional, None)
    SignatureKind = property(get_SignatureKind, None)
class IPackage5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage5'
    _iid_ = Guid('{0e842dd4-d9ac-45ed-9a1e-74ce056b2635}')
    @winrt_commethod(6)
    def GetContentGroupsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(7)
    def GetContentGroupAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageContentGroup]: ...
    @winrt_commethod(8)
    def StageContentGroupsAsync(self, names: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(9)
    def StageContentGroupsWithPriorityAsync(self, names: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], moveToHeadOfQueue: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_commethod(10)
    def SetInUseAsync(self, inUse: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPackage6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage6'
    _iid_ = Guid('{8b1ad942-12d7-4754-ae4e-638cbc0e3a2e}')
    @winrt_commethod(6)
    def GetAppInstallerInfo(self) -> win32more.Windows.ApplicationModel.AppInstallerInfo: ...
    @winrt_commethod(7)
    def CheckUpdateAvailabilityAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageUpdateAvailabilityResult]: ...
class IPackage7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage7'
    _iid_ = Guid('{86ff8d31-a2e4-45e0-9732-283a6d88fde1}')
    @winrt_commethod(6)
    def get_MutableLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_EffectiveLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
    EffectiveLocation = property(get_EffectiveLocation, None)
    MutableLocation = property(get_MutableLocation, None)
class IPackage8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage8'
    _iid_ = Guid('{2c584f7b-ce2a-4be6-a093-77cfbb2a7ea1}')
    @winrt_commethod(6)
    def get_EffectiveExternalLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_MachineExternalLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_UserExternalLocation(self) -> win32more.Windows.Storage.StorageFolder: ...
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
    def GetLogoAsRandomAccessStreamReference(self, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(16)
    def GetAppListEntries(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.AppListEntry]: ...
    @winrt_commethod(17)
    def get_IsStub(self) -> Boolean: ...
    EffectiveExternalLocation = property(get_EffectiveExternalLocation, None)
    EffectiveExternalPath = property(get_EffectiveExternalPath, None)
    EffectivePath = property(get_EffectivePath, None)
    InstalledPath = property(get_InstalledPath, None)
    IsStub = property(get_IsStub, None)
    MachineExternalLocation = property(get_MachineExternalLocation, None)
    MachineExternalPath = property(get_MachineExternalPath, None)
    MutablePath = property(get_MutablePath, None)
    UserExternalLocation = property(get_UserExternalLocation, None)
    UserExternalPath = property(get_UserExternalPath, None)
class IPackage9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackage9'
    _iid_ = Guid('{d5ab224f-d7e1-49ec-90ce-720cdbd02e9c}')
    @winrt_commethod(6)
    def FindRelatedPackages(self, options: win32more.Windows.ApplicationModel.FindRelatedPackagesOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_SourceUriSchemeName(self) -> WinRT_String: ...
    SourceUriSchemeName = property(get_SourceUriSchemeName, None)
class IPackageCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalog'
    _iid_ = Guid('{230a3751-9de3-4445-be74-91fb325abefe}')
    @winrt_commethod(6)
    def add_PackageStaging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageStagingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PackageStaging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PackageInstalling(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageInstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PackageInstalling(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PackageUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PackageUpdating(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PackageUninstalling(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PackageUninstalling(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PackageStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PackageStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PackageStaging = event()
    PackageInstalling = event()
    PackageUpdating = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
class IPackageCatalog2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalog2'
    _iid_ = Guid('{96a60c36-8ff7-4344-b6bf-ee64c2207ed2}')
    @winrt_commethod(6)
    def add_PackageContentGroupStaging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageContentGroupStagingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PackageContentGroupStaging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def AddOptionalPackageAsync(self, optionalPackageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult]: ...
    PackageContentGroupStaging = event()
class IPackageCatalog3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalog3'
    _iid_ = Guid('{96dd5c88-8837-43f9-9015-033434ba14f3}')
    @winrt_commethod(6)
    def RemoveOptionalPackagesAsync(self, optionalPackageFamilyNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult]: ...
class IPackageCatalog4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalog4'
    _iid_ = Guid('{c37c399b-44cc-4b7b-8baf-796c04ead3b9}')
    @winrt_commethod(6)
    def AddResourcePackageAsync(self, resourcePackageFamilyName: WinRT_String, resourceID: WinRT_String, options: win32more.Windows.ApplicationModel.AddResourcePackageOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.ApplicationModel.PackageCatalogAddResourcePackageResult, win32more.Windows.ApplicationModel.PackageInstallProgress]: ...
    @winrt_commethod(7)
    def RemoveResourcePackagesAsync(self, resourcePackages: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult]: ...
class IPackageCatalogAddOptionalPackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult'
    _iid_ = Guid('{3bf10cd4-b4df-47b3-a963-e2fa832f7dd3}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Package = property(get_Package, None)
class IPackageCatalogAddResourcePackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult'
    _iid_ = Guid('{9636ce0d-3e17-493f-aa08-ccec6fdef699}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
class IPackageCatalogRemoveOptionalPackagesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult'
    _iid_ = Guid('{29d2f97b-d974-4e64-9359-22cadfd79828}')
    @winrt_commethod(6)
    def get_PackagesRemoved(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    PackagesRemoved = property(get_PackagesRemoved, None)
class IPackageCatalogRemoveResourcePackagesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult'
    _iid_ = Guid('{ae719709-1a52-4321-87b3-e5a1a17981a7}')
    @winrt_commethod(6)
    def get_PackagesRemoved(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    PackagesRemoved = property(get_PackagesRemoved, None)
class IPackageCatalogStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogStatics'
    _iid_ = Guid('{a18c9696-e65b-4634-ba21-5e63eb7244a7}')
    @winrt_commethod(6)
    def OpenForCurrentPackage(self) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
    @winrt_commethod(7)
    def OpenForCurrentUser(self) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
class IPackageCatalogStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageCatalogStatics2'
    _iid_ = Guid('{4c11c159-9a28-598c-b185-55e1899b2be4}')
    @winrt_commethod(6)
    def OpenForPackage(self, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
class IPackageContentGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageContentGroup'
    _iid_ = Guid('{8f62695d-120a-4798-b5e1-5800dda8f2e1}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.ApplicationModel.PackageContentGroupState: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    IsRequired = property(get_IsRequired, None)
    Name = property(get_Name, None)
    Package = property(get_Package, None)
    State = property(get_State, None)
class IPackageContentGroupStagingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageContentGroupStagingEventArgs'
    _iid_ = Guid('{3d7bc27e-6f27-446c-986e-d4733d4d9113}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(11)
    def get_ContentGroupName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_IsContentGroupRequired(self) -> Boolean: ...
    ActivityId = property(get_ActivityId, None)
    ContentGroupName = property(get_ContentGroupName, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    IsContentGroupRequired = property(get_IsContentGroupRequired, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class IPackageContentGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageContentGroupStatics'
    _iid_ = Guid('{70ee7619-5f12-4b92-b9ea-6ccada13bc75}')
    @winrt_commethod(6)
    def get_RequiredGroupName(self) -> WinRT_String: ...
    RequiredGroupName = property(get_RequiredGroupName, None)
class IPackageId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageId'
    _iid_ = Guid('{1adb665e-37c7-4790-9980-dd7ae74e8bb2}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Version(self) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_commethod(8)
    def get_Architecture(self) -> win32more.Windows.System.ProcessorArchitecture: ...
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
    Architecture = property(get_Architecture, None)
    FamilyName = property(get_FamilyName, None)
    FullName = property(get_FullName, None)
    Name = property(get_Name, None)
    Publisher = property(get_Publisher, None)
    PublisherId = property(get_PublisherId, None)
    ResourceId = property(get_ResourceId, None)
    Version = property(get_Version, None)
class IPackageIdWithMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageIdWithMetadata'
    _iid_ = Guid('{40577a7c-0c9e-443d-9074-855f5ce0a08d}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Author(self) -> WinRT_String: ...
    Author = property(get_Author, None)
    ProductId = property(get_ProductId, None)
class IPackageInstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageInstallingEventArgs'
    _iid_ = Guid('{97741eb7-ab7a-401a-8b61-eb0e7faff237}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class IPackageStagingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageStagingEventArgs'
    _iid_ = Guid('{1041682d-54e2-4f51-b828-9ef7046c210f}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class IPackageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageStatics'
    _iid_ = Guid('{4e534bdf-2960-4878-97a4-9624deb72f2d}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.ApplicationModel.Package: ...
    Current = property(get_Current, None)
class IPackageStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageStatus'
    _iid_ = Guid('{5fe74f71-a365-4c09-a02d-046d525ea1da}')
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
    DataOffline = property(get_DataOffline, None)
    DependencyIssue = property(get_DependencyIssue, None)
    DeploymentInProgress = property(get_DeploymentInProgress, None)
    Disabled = property(get_Disabled, None)
    LicenseIssue = property(get_LicenseIssue, None)
    Modified = property(get_Modified, None)
    NeedsRemediation = property(get_NeedsRemediation, None)
    NotAvailable = property(get_NotAvailable, None)
    PackageOffline = property(get_PackageOffline, None)
    Servicing = property(get_Servicing, None)
    Tampered = property(get_Tampered, None)
class IPackageStatus2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageStatus2'
    _iid_ = Guid('{f428fa93-7c56-4862-acfa-abaedcc0694d}')
    @winrt_commethod(6)
    def get_IsPartiallyStaged(self) -> Boolean: ...
    IsPartiallyStaged = property(get_IsPartiallyStaged, None)
class IPackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageStatusChangedEventArgs'
    _iid_ = Guid('{437d714d-bd80-4a70-bc50-f6e796509575}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class IPackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageUninstallingEventArgs'
    _iid_ = Guid('{4443aa52-ab22-44cd-82bb-4ec9b827367a}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class IPackageUpdateAvailabilityResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageUpdateAvailabilityResult'
    _iid_ = Guid('{114e5009-199a-48a1-a079-313c45634a71}')
    @winrt_commethod(6)
    def get_Availability(self) -> win32more.Windows.ApplicationModel.PackageUpdateAvailability: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Availability = property(get_Availability, None)
    ExtendedError = property(get_ExtendedError, None)
class IPackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageUpdatingEventArgs'
    _iid_ = Guid('{cd7b4228-fd74-443e-b114-23e677b0e86f}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SourcePackage(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_TargetPackage(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(9)
    def get_Progress(self) -> Double: ...
    @winrt_commethod(10)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Progress = property(get_Progress, None)
    SourcePackage = property(get_SourcePackage, None)
    TargetPackage = property(get_TargetPackage, None)
class IPackageWithMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IPackageWithMetadata'
    _iid_ = Guid('{95949780-1de9-40f2-b452-0de9f1910012}')
    @winrt_commethod(6)
    def get_InstallDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def GetThumbnailToken(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def Launch(self, parameters: WinRT_String) -> Void: ...
    InstallDate = property(get_InstallDate, None)
class IStartupTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IStartupTask'
    _iid_ = Guid('{f75c23c8-b5f2-4f6c-88dd-36cb1d599d17}')
    @winrt_commethod(6)
    def RequestEnableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.StartupTaskState]: ...
    @winrt_commethod(7)
    def Disable(self) -> Void: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.ApplicationModel.StartupTaskState: ...
    @winrt_commethod(9)
    def get_TaskId(self) -> WinRT_String: ...
    State = property(get_State, None)
    TaskId = property(get_TaskId, None)
class IStartupTaskStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.IStartupTaskStatics'
    _iid_ = Guid('{ee5b60bd-a148-41a7-b26e-e8b88a1e62f8}')
    @winrt_commethod(6)
    def GetForCurrentPackageAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.StartupTask]]: ...
    @winrt_commethod(7)
    def GetAsync(self, taskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.StartupTask]: ...
class ISuspendingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ISuspendingDeferral'
    _iid_ = Guid('{59140509-8bc9-4eb4-b636-dabdc4f46f66}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ISuspendingEventArgs'
    _iid_ = Guid('{96061c05-2dba-4d08-b0bd-2b30a131c6aa}')
    @winrt_commethod(6)
    def get_SuspendingOperation(self) -> win32more.Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class ISuspendingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ISuspendingOperation'
    _iid_ = Guid('{9da4ca41-20e1-4e9b-9f65-a9f435340c3a}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class LeavingBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs
    _classid_ = 'Windows.ApplicationModel.LeavingBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class LimitedAccessFeatureRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ILimitedAccessFeatureRequestResult
    _classid_ = 'Windows.ApplicationModel.LimitedAccessFeatureRequestResult'
    @winrt_mixinmethod
    def get_FeatureId(self: win32more.Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> win32more.Windows.ApplicationModel.LimitedAccessFeatureStatus: ...
    @winrt_mixinmethod
    def get_EstimatedRemovalDate(self: win32more.Windows.ApplicationModel.ILimitedAccessFeatureRequestResult) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    EstimatedRemovalDate = property(get_EstimatedRemovalDate, None)
    FeatureId = property(get_FeatureId, None)
    Status = property(get_Status, None)
class LimitedAccessFeatureStatus(Enum, Int32):
    Unavailable = 0
    Available = 1
    AvailableWithoutToken = 2
    Unknown = 3
class LimitedAccessFeatures(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LimitedAccessFeatures'
    @winrt_classmethod
    def TryUnlockFeature(cls: win32more.Windows.ApplicationModel.ILimitedAccessFeaturesStatics, featureId: WinRT_String, token: WinRT_String, attestation: WinRT_String) -> win32more.Windows.ApplicationModel.LimitedAccessFeatureRequestResult: ...
class _Package_Meta_(ComPtr.__class__):
    pass
class Package(ComPtr, metaclass=_Package_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackage
    _classid_ = 'Windows.ApplicationModel.Package'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.IPackage) -> win32more.Windows.ApplicationModel.PackageId: ...
    @winrt_mixinmethod
    def get_InstalledLocation(self: win32more.Windows.ApplicationModel.IPackage) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_IsFramework(self: win32more.Windows.ApplicationModel.IPackage) -> Boolean: ...
    @winrt_mixinmethod
    def get_Dependencies(self: win32more.Windows.ApplicationModel.IPackage) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublisherDisplayName(self: win32more.Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.IPackage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.ApplicationModel.IPackage2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsResourcePackage(self: win32more.Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBundle(self: win32more.Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDevelopmentMode(self: win32more.Windows.ApplicationModel.IPackage2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.IPackage3) -> win32more.Windows.ApplicationModel.PackageStatus: ...
    @winrt_mixinmethod
    def get_InstalledDate(self: win32more.Windows.ApplicationModel.IPackage3) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetAppListEntriesAsync(self: win32more.Windows.ApplicationModel.IPackage3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.AppListEntry]]: ...
    @winrt_mixinmethod
    def get_InstallDate(self: win32more.Windows.ApplicationModel.IPackageWithMetadata) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetThumbnailToken(self: win32more.Windows.ApplicationModel.IPackageWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def Launch(self: win32more.Windows.ApplicationModel.IPackageWithMetadata, parameters: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SignatureKind(self: win32more.Windows.ApplicationModel.IPackage4) -> win32more.Windows.ApplicationModel.PackageSignatureKind: ...
    @winrt_mixinmethod
    def get_IsOptional(self: win32more.Windows.ApplicationModel.IPackage4) -> Boolean: ...
    @winrt_mixinmethod
    def VerifyContentIntegrityAsync(self: win32more.Windows.ApplicationModel.IPackage4) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetContentGroupsAsync(self: win32more.Windows.ApplicationModel.IPackage5) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def GetContentGroupAsync(self: win32more.Windows.ApplicationModel.IPackage5, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageContentGroup]: ...
    @winrt_mixinmethod
    def StageContentGroupsAsync(self: win32more.Windows.ApplicationModel.IPackage5, names: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def StageContentGroupsWithPriorityAsync(self: win32more.Windows.ApplicationModel.IPackage5, names: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], moveToHeadOfQueue: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.PackageContentGroup]]: ...
    @winrt_mixinmethod
    def SetInUseAsync(self: win32more.Windows.ApplicationModel.IPackage5, inUse: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetAppInstallerInfo(self: win32more.Windows.ApplicationModel.IPackage6) -> win32more.Windows.ApplicationModel.AppInstallerInfo: ...
    @winrt_mixinmethod
    def CheckUpdateAvailabilityAsync(self: win32more.Windows.ApplicationModel.IPackage6) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageUpdateAvailabilityResult]: ...
    @winrt_mixinmethod
    def get_MutableLocation(self: win32more.Windows.ApplicationModel.IPackage7) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_EffectiveLocation(self: win32more.Windows.ApplicationModel.IPackage7) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_EffectiveExternalLocation(self: win32more.Windows.ApplicationModel.IPackage8) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_MachineExternalLocation(self: win32more.Windows.ApplicationModel.IPackage8) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_UserExternalLocation(self: win32more.Windows.ApplicationModel.IPackage8) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_InstalledPath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MutablePath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EffectivePath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EffectiveExternalPath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MachineExternalPath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserExternalPath(self: win32more.Windows.ApplicationModel.IPackage8) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLogoAsRandomAccessStreamReference(self: win32more.Windows.ApplicationModel.IPackage8, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetAppListEntries(self: win32more.Windows.ApplicationModel.IPackage8) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.AppListEntry]: ...
    @winrt_mixinmethod
    def get_IsStub(self: win32more.Windows.ApplicationModel.IPackage8) -> Boolean: ...
    @winrt_mixinmethod
    def FindRelatedPackages(self: win32more.Windows.ApplicationModel.IPackage9, options: win32more.Windows.ApplicationModel.FindRelatedPackagesOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_SourceUriSchemeName(self: win32more.Windows.ApplicationModel.IPackage9) -> WinRT_String: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.ApplicationModel.IPackageStatics) -> win32more.Windows.ApplicationModel.Package: ...
    Dependencies = property(get_Dependencies, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    EffectiveExternalLocation = property(get_EffectiveExternalLocation, None)
    EffectiveExternalPath = property(get_EffectiveExternalPath, None)
    EffectiveLocation = property(get_EffectiveLocation, None)
    EffectivePath = property(get_EffectivePath, None)
    Id = property(get_Id, None)
    InstallDate = property(get_InstallDate, None)
    InstalledDate = property(get_InstalledDate, None)
    InstalledLocation = property(get_InstalledLocation, None)
    InstalledPath = property(get_InstalledPath, None)
    IsBundle = property(get_IsBundle, None)
    IsDevelopmentMode = property(get_IsDevelopmentMode, None)
    IsFramework = property(get_IsFramework, None)
    IsOptional = property(get_IsOptional, None)
    IsResourcePackage = property(get_IsResourcePackage, None)
    IsStub = property(get_IsStub, None)
    Logo = property(get_Logo, None)
    MachineExternalLocation = property(get_MachineExternalLocation, None)
    MachineExternalPath = property(get_MachineExternalPath, None)
    MutableLocation = property(get_MutableLocation, None)
    MutablePath = property(get_MutablePath, None)
    PublisherDisplayName = property(get_PublisherDisplayName, None)
    SignatureKind = property(get_SignatureKind, None)
    SourceUriSchemeName = property(get_SourceUriSchemeName, None)
    Status = property(get_Status, None)
    UserExternalLocation = property(get_UserExternalLocation, None)
    UserExternalPath = property(get_UserExternalPath, None)
    _Package_Meta_.Current = property(get_Current, None)
class PackageCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageCatalog
    _classid_ = 'Windows.ApplicationModel.PackageCatalog'
    @winrt_mixinmethod
    def add_PackageStaging(self: win32more.Windows.ApplicationModel.IPackageCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageStagingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStaging(self: win32more.Windows.ApplicationModel.IPackageCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageInstalling(self: win32more.Windows.ApplicationModel.IPackageCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageInstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageInstalling(self: win32more.Windows.ApplicationModel.IPackageCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdating(self: win32more.Windows.ApplicationModel.IPackageCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdating(self: win32more.Windows.ApplicationModel.IPackageCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUninstalling(self: win32more.Windows.ApplicationModel.IPackageCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUninstalling(self: win32more.Windows.ApplicationModel.IPackageCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageStatusChanged(self: win32more.Windows.ApplicationModel.IPackageCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStatusChanged(self: win32more.Windows.ApplicationModel.IPackageCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageContentGroupStaging(self: win32more.Windows.ApplicationModel.IPackageCatalog2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageCatalog, win32more.Windows.ApplicationModel.PackageContentGroupStagingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageContentGroupStaging(self: win32more.Windows.ApplicationModel.IPackageCatalog2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddOptionalPackageAsync(self: win32more.Windows.ApplicationModel.IPackageCatalog2, optionalPackageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult]: ...
    @winrt_mixinmethod
    def RemoveOptionalPackagesAsync(self: win32more.Windows.ApplicationModel.IPackageCatalog3, optionalPackageFamilyNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult]: ...
    @winrt_mixinmethod
    def AddResourcePackageAsync(self: win32more.Windows.ApplicationModel.IPackageCatalog4, resourcePackageFamilyName: WinRT_String, resourceID: WinRT_String, options: win32more.Windows.ApplicationModel.AddResourcePackageOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.ApplicationModel.PackageCatalogAddResourcePackageResult, win32more.Windows.ApplicationModel.PackageInstallProgress]: ...
    @winrt_mixinmethod
    def RemoveResourcePackagesAsync(self: win32more.Windows.ApplicationModel.IPackageCatalog4, resourcePackages: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult]: ...
    @winrt_classmethod
    def OpenForPackage(cls: win32more.Windows.ApplicationModel.IPackageCatalogStatics2, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
    @winrt_classmethod
    def OpenForCurrentPackage(cls: win32more.Windows.ApplicationModel.IPackageCatalogStatics) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
    @winrt_classmethod
    def OpenForCurrentUser(cls: win32more.Windows.ApplicationModel.IPackageCatalogStatics) -> win32more.Windows.ApplicationModel.PackageCatalog: ...
    PackageStaging = event()
    PackageInstalling = event()
    PackageUpdating = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
    PackageContentGroupStaging = event()
class PackageCatalogAddOptionalPackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult
    _classid_ = 'Windows.ApplicationModel.PackageCatalogAddOptionalPackageResult'
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IPackageCatalogAddOptionalPackageResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Package = property(get_Package, None)
class PackageCatalogAddResourcePackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult
    _classid_ = 'Windows.ApplicationModel.PackageCatalogAddResourcePackageResult'
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IPackageCatalogAddResourcePackageResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
class PackageCatalogRemoveOptionalPackagesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult
    _classid_ = 'Windows.ApplicationModel.PackageCatalogRemoveOptionalPackagesResult'
    @winrt_mixinmethod
    def get_PackagesRemoved(self: win32more.Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IPackageCatalogRemoveOptionalPackagesResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    PackagesRemoved = property(get_PackagesRemoved, None)
class PackageCatalogRemoveResourcePackagesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult
    _classid_ = 'Windows.ApplicationModel.PackageCatalogRemoveResourcePackagesResult'
    @winrt_mixinmethod
    def get_PackagesRemoved(self: win32more.Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IPackageCatalogRemoveResourcePackagesResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    PackagesRemoved = property(get_PackagesRemoved, None)
class _PackageContentGroup_Meta_(ComPtr.__class__):
    pass
class PackageContentGroup(ComPtr, metaclass=_PackageContentGroup_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageContentGroup
    _classid_ = 'Windows.ApplicationModel.PackageContentGroup'
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageContentGroup) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.IPackageContentGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.ApplicationModel.IPackageContentGroup) -> win32more.Windows.ApplicationModel.PackageContentGroupState: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.ApplicationModel.IPackageContentGroup) -> Boolean: ...
    @winrt_classmethod
    def get_RequiredGroupName(cls: win32more.Windows.ApplicationModel.IPackageContentGroupStatics) -> WinRT_String: ...
    IsRequired = property(get_IsRequired, None)
    Name = property(get_Name, None)
    Package = property(get_Package, None)
    State = property(get_State, None)
    _PackageContentGroup_Meta_.RequiredGroupName = property(get_RequiredGroupName, None)
class PackageContentGroupStagingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageContentGroupStagingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ContentGroupName(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsContentGroupRequired(self: win32more.Windows.ApplicationModel.IPackageContentGroupStagingEventArgs) -> Boolean: ...
    ActivityId = property(get_ActivityId, None)
    ContentGroupName = property(get_ContentGroupName, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    IsContentGroupRequired = property(get_IsContentGroupRequired, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class PackageContentGroupState(Enum, Int32):
    NotStaged = 0
    Queued = 1
    Staging = 2
    Staged = 3
class PackageId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageId
    _classid_ = 'Windows.ApplicationModel.PackageId'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.ApplicationModel.IPackageId) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_mixinmethod
    def get_Architecture(self: win32more.Windows.ApplicationModel.IPackageId) -> win32more.Windows.System.ProcessorArchitecture: ...
    @winrt_mixinmethod
    def get_ResourceId(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublisherId(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FullName(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FamilyName(self: win32more.Windows.ApplicationModel.IPackageId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.IPackageIdWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.ApplicationModel.IPackageIdWithMetadata) -> WinRT_String: ...
    Architecture = property(get_Architecture, None)
    Author = property(get_Author, None)
    FamilyName = property(get_FamilyName, None)
    FullName = property(get_FullName, None)
    Name = property(get_Name, None)
    ProductId = property(get_ProductId, None)
    Publisher = property(get_Publisher, None)
    PublisherId = property(get_PublisherId, None)
    ResourceId = property(get_ResourceId, None)
    Version = property(get_Version, None)
class PackageInstallProgress(Structure):
    PercentComplete: UInt32
class PackageInstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageInstallingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.ApplicationModel.IPackageInstallingEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class PackageRelationship(Enum, Int32):
    Dependencies = 0
    Dependents = 1
    All = 2
class PackageSignatureKind(Enum, Int32):
    None_ = 0
    Developer = 1
    Enterprise = 2
    Store = 3
    System = 4
class PackageStagingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageStagingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageStagingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.IPackageStagingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageStagingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.IPackageStagingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageStagingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.ApplicationModel.IPackageStagingEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class PackageStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageStatus
    _classid_ = 'Windows.ApplicationModel.PackageStatus'
    @winrt_mixinmethod
    def VerifyIsOK(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotAvailable(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_PackageOffline(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DataOffline(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Disabled(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_NeedsRemediation(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_LicenseIssue(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Modified(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Tampered(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DependencyIssue(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Servicing(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeploymentInProgress(self: win32more.Windows.ApplicationModel.IPackageStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPartiallyStaged(self: win32more.Windows.ApplicationModel.IPackageStatus2) -> Boolean: ...
    DataOffline = property(get_DataOffline, None)
    DependencyIssue = property(get_DependencyIssue, None)
    DeploymentInProgress = property(get_DeploymentInProgress, None)
    Disabled = property(get_Disabled, None)
    IsPartiallyStaged = property(get_IsPartiallyStaged, None)
    LicenseIssue = property(get_LicenseIssue, None)
    Modified = property(get_Modified, None)
    NeedsRemediation = property(get_NeedsRemediation, None)
    NotAvailable = property(get_NotAvailable, None)
    PackageOffline = property(get_PackageOffline, None)
    Servicing = property(get_Servicing, None)
    Tampered = property(get_Tampered, None)
class PackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageStatusChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageStatusChangedEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
class PackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageUninstallingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.ApplicationModel.IPackageUninstallingEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Package = property(get_Package, None)
    Progress = property(get_Progress, None)
class PackageUpdateAvailability(Enum, Int32):
    Unknown = 0
    NoUpdates = 1
    Available = 2
    Required = 3
    Error = 4
class PackageUpdateAvailabilityResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageUpdateAvailabilityResult
    _classid_ = 'Windows.ApplicationModel.PackageUpdateAvailabilityResult'
    @winrt_mixinmethod
    def get_Availability(self: win32more.Windows.ApplicationModel.IPackageUpdateAvailabilityResult) -> win32more.Windows.ApplicationModel.PackageUpdateAvailability: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.IPackageUpdateAvailabilityResult) -> win32more.Windows.Foundation.HResult: ...
    Availability = property(get_Availability, None)
    ExtendedError = property(get_ExtendedError, None)
class PackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageUpdatingEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_SourcePackage(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_TargetPackage(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Double: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.ApplicationModel.IPackageUpdatingEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ActivityId = property(get_ActivityId, None)
    ErrorCode = property(get_ErrorCode, None)
    IsComplete = property(get_IsComplete, None)
    Progress = property(get_Progress, None)
    SourcePackage = property(get_SourcePackage, None)
    TargetPackage = property(get_TargetPackage, None)
class PackageVersion(Structure):
    Major: UInt16
    Minor: UInt16
    Build: UInt16
    Revision: UInt16
class StartupTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IStartupTask
    _classid_ = 'Windows.ApplicationModel.StartupTask'
    @winrt_mixinmethod
    def RequestEnableAsync(self: win32more.Windows.ApplicationModel.IStartupTask) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.StartupTaskState]: ...
    @winrt_mixinmethod
    def Disable(self: win32more.Windows.ApplicationModel.IStartupTask) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.ApplicationModel.IStartupTask) -> win32more.Windows.ApplicationModel.StartupTaskState: ...
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.IStartupTask) -> WinRT_String: ...
    @winrt_classmethod
    def GetForCurrentPackageAsync(cls: win32more.Windows.ApplicationModel.IStartupTaskStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.StartupTask]]: ...
    @winrt_classmethod
    def GetAsync(cls: win32more.Windows.ApplicationModel.IStartupTaskStatics, taskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.StartupTask]: ...
    State = property(get_State, None)
    TaskId = property(get_TaskId, None)
StartupTaskContract: UInt32 = 196608
class StartupTaskState(Enum, Int32):
    Disabled = 0
    DisabledByUser = 1
    Enabled = 2
    DisabledByPolicy = 3
    EnabledByPolicy = 4
class SuspendingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingDeferral
    _classid_ = 'Windows.ApplicationModel.SuspendingDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.ISuspendingDeferral) -> Void: ...
class SuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingEventArgs
    _classid_ = 'Windows.ApplicationModel.SuspendingEventArgs'
    @winrt_mixinmethod
    def get_SuspendingOperation(self: win32more.Windows.ApplicationModel.ISuspendingEventArgs) -> win32more.Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class SuspendingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingOperation
    _classid_ = 'Windows.ApplicationModel.SuspendingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)


make_ready(__name__)
