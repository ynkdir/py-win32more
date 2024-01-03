from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Management.Deployment.Preview
class ClassicAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.ClassicAppManager'
    @winrt_classmethod
    def FindInstalledApp(cls: win32more.Windows.Management.Deployment.Preview.IClassicAppManagerStatics, appUninstallKey: WinRT_String) -> win32more.Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
DeploymentPreviewContract: UInt32 = 65536
class IClassicAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.IClassicAppManagerStatics'
    _iid_ = Guid('{e2fad668-882c-4f33-b035-0df7b90d67e6}')
    @winrt_commethod(6)
    def FindInstalledApp(self, appUninstallKey: WinRT_String) -> win32more.Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
class IInstalledClassicAppInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.IInstalledClassicAppInfo'
    _iid_ = Guid('{0a7d3da3-65d0-4086-80d6-0610d760207d}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayVersion(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
class InstalledClassicAppInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo
    _classid_ = 'Windows.Management.Deployment.Preview.InstalledClassicAppInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayVersion(self: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)


make_ready(__name__)
