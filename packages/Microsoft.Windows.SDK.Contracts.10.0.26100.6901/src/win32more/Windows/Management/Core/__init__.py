from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Management.Core
import win32more.Windows.Storage
class ApplicationDataManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Core.IApplicationDataManager
    _classid_ = 'Windows.Management.Core.ApplicationDataManager'
    @winrt_classmethod
    def CreateForPackageFamily(cls: win32more.Windows.Management.Core.IApplicationDataManagerStatics, packageFamilyName: WinRT_String) -> win32more.Windows.Storage.ApplicationData: ...
class IApplicationDataManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManager'
    _iid_ = Guid('{74d10432-2e99-4000-9a3a-64307e858129}')
class IApplicationDataManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManagerStatics'
    _iid_ = Guid('{1e1862e3-698e-49a1-9752-dee94925b9b3}')
    @winrt_commethod(6)
    def CreateForPackageFamily(self, packageFamilyName: WinRT_String) -> win32more.Windows.Storage.ApplicationData: ...


make_ready(__name__)
