from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
DeploymentContract: UInt32 = 262144
class DeploymentInitializeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions: ...
    @winrt_mixinmethod
    def get_ForceDeployment(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ForceDeployment(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OnErrorShowUI(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2) -> Boolean: ...
    @winrt_mixinmethod
    def put_OnErrorShowUI(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2, value: Boolean) -> Void: ...
    ForceDeployment = property(get_ForceDeployment, put_ForceDeployment)
    OnErrorShowUI = property(get_OnErrorShowUI, put_OnErrorShowUI)
class DeploymentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentManager'
    @winrt_overload
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics2, deploymentInitializeOptions: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_classmethod
    def GetStatus(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @Initialize.register
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class DeploymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class DeploymentStatus(Enum, Int32):
    Unknown = 0
    Ok = 1
    PackageInstallRequired = 2
    PackageInstallFailed = 3
class IDeploymentInitializeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions'
    _iid_ = Guid('{578a5fd4-9d7f-5e01-97b8-d8ea61db4027}')
    @winrt_commethod(6)
    def get_ForceDeployment(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ForceDeployment(self, value: Boolean) -> Void: ...
    ForceDeployment = property(get_ForceDeployment, put_ForceDeployment)
class IDeploymentInitializeOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2'
    _iid_ = Guid('{ad902820-149f-5e16-a566-9b2363997de2}')
    @winrt_commethod(6)
    def get_OnErrorShowUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_OnErrorShowUI(self, value: Boolean) -> Void: ...
    OnErrorShowUI = property(get_OnErrorShowUI, put_OnErrorShowUI)
class IDeploymentManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics'
    _iid_ = Guid('{6782a9d0-bfd0-50ea-81b0-32e9ed37cdf0}')
    @winrt_commethod(6)
    def GetStatus(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_commethod(7)
    def Initialize(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class IDeploymentManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics2'
    _iid_ = Guid('{f49c16ee-6ebc-5f15-bebb-2ba49f8c0b30}')
    @winrt_commethod(6)
    def Initialize(self, deploymentInitializeOptions: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class IDeploymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult'
    _iid_ = Guid('{27203f62-463d-587a-8eb7-870098901078}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IDeploymentResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory'
    _iid_ = Guid('{acd7bdae-4ae6-5cac-8205-1e8c305f953b}')
    @winrt_commethod(6)
    def CreateInstance(self, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class IReleaseInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics'
    _iid_ = Guid('{ed9be8ff-073c-5c66-bf97-ef0ce67405c3}')
    @winrt_commethod(6)
    def get_Major(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Minor(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_Patch(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_VersionTag(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AsString(self) -> WinRT_String: ...
    AsString = property(get_AsString, None)
    Major = property(get_Major, None)
    Minor = property(get_Minor, None)
    Patch = property(get_Patch, None)
    VersionTag = property(get_VersionTag, None)
class IRuntimeCompatibilityOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions'
    _iid_ = Guid('{d7403bd9-b25d-5b8f-8de1-9dcb57d99f6c}')
    @winrt_commethod(6)
    def get_PatchLevel1(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion: ...
    @winrt_commethod(7)
    def put_PatchLevel1(self, value: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion) -> Void: ...
    @winrt_commethod(8)
    def get_PatchLevel2(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion: ...
    @winrt_commethod(9)
    def put_PatchLevel2(self, value: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion) -> Void: ...
    @winrt_commethod(10)
    def get_DisabledChanges(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeCompatibilityChange]: ...
    @winrt_commethod(11)
    def Apply(self) -> Void: ...
    DisabledChanges = property(get_DisabledChanges, None)
    PatchLevel1 = property(get_PatchLevel1, put_PatchLevel1)
    PatchLevel2 = property(get_PatchLevel2, put_PatchLevel2)
class IRuntimeInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeInfoStatics'
    _iid_ = Guid('{e5cb9549-8951-590e-a753-8f281cd77ab5}')
    @winrt_commethod(6)
    def get_Version(self) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_commethod(7)
    def get_AsString(self) -> WinRT_String: ...
    AsString = property(get_AsString, None)
    Version = property(get_Version, None)
class _ReleaseInfo_Meta_(ComPtr.__class__):
    pass
class ReleaseInfo(ComPtr, metaclass=_ReleaseInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.ReleaseInfo'
    @winrt_classmethod
    def get_Major(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Minor(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Patch(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics) -> UInt16: ...
    @winrt_classmethod
    def get_VersionTag(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AsString(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IReleaseInfoStatics) -> WinRT_String: ...
    _ReleaseInfo_Meta_.AsString = property(get_AsString, None)
    _ReleaseInfo_Meta_.Major = property(get_Major, None)
    _ReleaseInfo_Meta_.Minor = property(get_Minor, None)
    _ReleaseInfo_Meta_.Patch = property(get_Patch, None)
    _ReleaseInfo_Meta_.VersionTag = property(get_VersionTag, None)
class RuntimeCompatibilityChange(Enum, Int32):
    None_ = 0
RuntimeCompatibilityContract: UInt32 = 65536
class RuntimeCompatibilityOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeCompatibilityOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeCompatibilityOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeCompatibilityOptions: ...
    @winrt_mixinmethod
    def get_PatchLevel1(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion: ...
    @winrt_mixinmethod
    def put_PatchLevel1(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions, value: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion) -> Void: ...
    @winrt_mixinmethod
    def get_PatchLevel2(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion: ...
    @winrt_mixinmethod
    def put_PatchLevel2(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions, value: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.WindowsAppRuntimeVersion) -> Void: ...
    @winrt_mixinmethod
    def get_DisabledChanges(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeCompatibilityChange]: ...
    @winrt_mixinmethod
    def Apply(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeCompatibilityOptions) -> Void: ...
    DisabledChanges = property(get_DisabledChanges, None)
    PatchLevel1 = property(get_PatchLevel1, put_PatchLevel1)
    PatchLevel2 = property(get_PatchLevel2, put_PatchLevel2)
class _RuntimeInfo_Meta_(ComPtr.__class__):
    pass
class RuntimeInfo(ComPtr, metaclass=_RuntimeInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.RuntimeInfo'
    @winrt_classmethod
    def get_Version(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeInfoStatics) -> win32more.Windows.ApplicationModel.PackageVersion: ...
    @winrt_classmethod
    def get_AsString(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IRuntimeInfoStatics) -> WinRT_String: ...
    _RuntimeInfo_Meta_.AsString = property(get_AsString, None)
    _RuntimeInfo_Meta_.Version = property(get_Version, None)
VersionInfoContract: UInt32 = 65536
class WindowsAppRuntimeVersion(Structure):
    Major: UInt32
    Minor: UInt32
    Patch: UInt32


make_ready(__name__)
