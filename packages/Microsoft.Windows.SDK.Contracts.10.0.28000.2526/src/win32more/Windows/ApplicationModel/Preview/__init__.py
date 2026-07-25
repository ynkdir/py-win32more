from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.ApplicationModel.Preview
import win32more.Windows.Foundation.Collections
class IStartupAppInfoPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.IStartupAppInfoPreview'
    _iid_ = Guid('{c3a147db-09fa-5aa5-b3bd-119a09963d58}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Publisher(self) -> hstr: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Impact(self) -> win32more.Windows.ApplicationModel.Preview.StartupAppImpactPreview: ...
    @winrt_commethod(10)
    def get_ExecutablePath(self) -> hstr: ...
    DisplayName = property(get_DisplayName, None)
    ExecutablePath = property(get_ExecutablePath, None)
    Impact = property(get_Impact, None)
    IsEnabled = property(get_IsEnabled, None)
    Publisher = property(get_Publisher, None)
class IStartupAppsManagerPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.IStartupAppsManagerPreview'
    _iid_ = Guid('{7197b9c1-03bb-5693-87c3-6f983cc70fb3}')
    @winrt_commethod(6)
    def GetStartupAppInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Preview.StartupAppInfoPreview]: ...
class IStartupAppsManagerPreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.IStartupAppsManagerPreviewStatics'
    _iid_ = Guid('{9d0331f5-343f-5cd7-9d66-762cfa2c0380}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.Preview.StartupAppsManagerPreview: ...
class StartupAppImpactPreview(Enum, Int32):
    _name_ = 'Windows.ApplicationModel.Preview.StartupAppImpactPreview'
    Unknown = 0
    None_ = 1
    Low = 2
    Medium = 3
    High = 4
class StartupAppInfoPreview(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview
    _classid_ = 'Windows.ApplicationModel.Preview.StartupAppInfoPreview'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview) -> hstr: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview) -> hstr: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview) -> Boolean: ...
    @winrt_mixinmethod
    def get_Impact(self: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview) -> win32more.Windows.ApplicationModel.Preview.StartupAppImpactPreview: ...
    @winrt_mixinmethod
    def get_ExecutablePath(self: win32more.Windows.ApplicationModel.Preview.IStartupAppInfoPreview) -> hstr: ...
    DisplayName = property(get_DisplayName, None)
    ExecutablePath = property(get_ExecutablePath, None)
    Impact = property(get_Impact, None)
    IsEnabled = property(get_IsEnabled, None)
    Publisher = property(get_Publisher, None)
class StartupAppsManagerPreview(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.IStartupAppsManagerPreview
    _classid_ = 'Windows.ApplicationModel.Preview.StartupAppsManagerPreview'
    @winrt_mixinmethod
    def GetStartupAppInfos(self: win32more.Windows.ApplicationModel.Preview.IStartupAppsManagerPreview) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Preview.StartupAppInfoPreview]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.Preview.IStartupAppsManagerPreviewStatics) -> win32more.Windows.ApplicationModel.Preview.StartupAppsManagerPreview: ...
StartupAppsPreviewContract: UInt32 = 65536


make_ready(__name__)
