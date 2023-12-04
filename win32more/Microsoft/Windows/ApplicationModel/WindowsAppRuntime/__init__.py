from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime
import win32more.Windows.Foundation
DeploymentContract: UInt32 = 262144
class DeploymentInitializeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics, deploymentInitializeOptions: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_classmethod
    def GetStatus(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class DeploymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 2:
            instance = win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
DeploymentStatus = Int32
DeploymentStatus_Unknown: DeploymentStatus = 0
DeploymentStatus_Ok: DeploymentStatus = 1
DeploymentStatus_PackageInstallRequired: DeploymentStatus = 2
DeploymentStatus_PackageInstallFailed: DeploymentStatus = 3
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
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IDeploymentResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory'
    _iid_ = Guid('{acd7bdae-4ae6-5cac-8205-1e8c305f953b}')
    @winrt_commethod(6)
    def CreateInstance(self, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
make_ready(__name__)
