from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Management.Deployment.Preview
class ClassicAppManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.ClassicAppManager'
    @winrt_classmethod
    def FindInstalledApp(cls: win32more.Windows.Management.Deployment.Preview.IClassicAppManagerStatics, appUninstallKey: WinRT_String) -> win32more.Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
DeploymentPreviewContract: UInt32 = 65536
class IClassicAppManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.IClassicAppManagerStatics'
    _iid_ = Guid('{e2fad668-882c-4f33-b035-0df7b90d67e6}')
    @winrt_commethod(6)
    def FindInstalledApp(self, appUninstallKey: WinRT_String) -> win32more.Windows.Management.Deployment.Preview.InstalledClassicAppInfo: ...
class IInstalledClassicAppInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Deployment.Preview.IInstalledClassicAppInfo'
    _iid_ = Guid('{0a7d3da3-65d0-4086-80d6-0610d760207d}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayVersion(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
class InstalledClassicAppInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo
    _classid_ = 'Windows.Management.Deployment.Preview.InstalledClassicAppInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayVersion(self: win32more.Windows.Management.Deployment.Preview.IInstalledClassicAppInfo) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)


make_ready(__name__)
