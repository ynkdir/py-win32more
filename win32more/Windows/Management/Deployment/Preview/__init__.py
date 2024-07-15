from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Management.Deployment.Preview
import win32more.Windows.Win32.System.WinRT
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
