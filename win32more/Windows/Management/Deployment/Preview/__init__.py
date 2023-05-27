from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Management.Deployment.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ClassicAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.ClassicAppManager'
    @winrt_classmethod
    def FindInstalledApp(cls: Windows.Management.Deployment.Preview.IClassicAppManagerStatics, appUninstallKey: WinRT_String) -> win32more.Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
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
make_head(_module, 'ClassicAppManager')
make_head(_module, 'IClassicAppManagerStatics')
make_head(_module, 'IInstalledClassicAppInfo')
make_head(_module, 'InstalledClassicAppInfo')
