from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Management.Deployment.Preview
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.ClassicAppManager'
    @winrt_classmethod
    def FindInstalledApp(cls: Windows.Management.Deployment.Preview.IClassicAppManagerStatics, appUninstallKey: WinRT_String) -> Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
DeploymentPreviewContract: UInt32 = 65536
class IClassicAppManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e2fad668-882c-4f33-b0-35-0d-f7-b9-0d-67-e6')
    @winrt_commethod(6)
    def FindInstalledApp(self, appUninstallKey: WinRT_String) -> Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
class IInstalledClassicAppInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0a7d3da3-65d0-4086-80-d6-06-10-d7-60-20-7d')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayVersion(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
class InstalledClassicAppInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.InstalledClassicAppInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayVersion(self: Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
make_head(_module, 'ClassicAppManager')
make_head(_module, 'IClassicAppManagerStatics')
make_head(_module, 'IInstalledClassicAppInfo')
make_head(_module, 'InstalledClassicAppInfo')
