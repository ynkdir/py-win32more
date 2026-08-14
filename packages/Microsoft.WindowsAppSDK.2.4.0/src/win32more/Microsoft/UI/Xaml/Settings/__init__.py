from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.UI.Xaml.Settings
class IXamlOptionalChanges(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Settings.IXamlOptionalChanges'
    _iid_ = Guid('{387572ae-ac51-5cb0-8317-2d6e118bea6a}')
class IXamlOptionalChangesStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics'
    _iid_ = Guid('{edb65323-1884-51c9-8b79-719554de4dd9}')
    @winrt_commethod(6)
    def EnableChange(self, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_commethod(7)
    def DisableChange(self, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_commethod(8)
    def IsChangeEnabled(self, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_commethod(9)
    def Lock(self) -> Boolean: ...
    @winrt_commethod(10)
    def IsLocked(self) -> Boolean: ...
class XamlChangeId(Enum, Int32):
    _name_ = 'Microsoft.UI.Xaml.Settings.XamlChangeId'
    _Reserved = 0
    IconNoGridOptimization = 61276805
    OptimizeApplyStyles = 61697456
    DefaultStyleOptimizations = 60995620
    DeferContextFlyoutInit = 61098986
class XamlOptionalChanges(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChanges
    _classid_ = 'Microsoft.UI.Xaml.Settings.XamlOptionalChanges'
    @winrt_classmethod
    def EnableChange(cls: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_classmethod
    def DisableChange(cls: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_classmethod
    def IsChangeEnabled(cls: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics, changeId: win32more.Microsoft.UI.Xaml.Settings.XamlChangeId) -> Boolean: ...
    @winrt_classmethod
    def Lock(cls: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics) -> Boolean: ...
    @winrt_classmethod
    def IsLocked(cls: win32more.Microsoft.UI.Xaml.Settings.IXamlOptionalChangesStatics) -> Boolean: ...


make_ready(__name__)
