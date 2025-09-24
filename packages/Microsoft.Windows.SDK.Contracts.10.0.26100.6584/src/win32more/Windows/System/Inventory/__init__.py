from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Inventory
class IInstalledDesktopApp(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Inventory.IInstalledDesktopApp'
    _iid_ = Guid('{75eab8ed-c0bc-5364-4c28-166e0545167a}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayVersion(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
    Id = property(get_Id, None)
    Publisher = property(get_Publisher, None)
class IInstalledDesktopAppStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Inventory.IInstalledDesktopAppStatics'
    _iid_ = Guid('{264cf74e-21cd-5f9b-6056-7866ad72489a}')
    @winrt_commethod(6)
    def GetInventoryAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Inventory.InstalledDesktopApp]]: ...
class InstalledDesktopApp(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.System.Inventory.IInstalledDesktopApp
    _classid_ = 'Windows.System.Inventory.InstalledDesktopApp'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayVersion(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def GetInventoryAsync(cls: win32more.Windows.System.Inventory.IInstalledDesktopAppStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Inventory.InstalledDesktopApp]]: ...
    DisplayName = property(get_DisplayName, None)
    DisplayVersion = property(get_DisplayVersion, None)
    Id = property(get_Id, None)
    Publisher = property(get_Publisher, None)


make_ready(__name__)
