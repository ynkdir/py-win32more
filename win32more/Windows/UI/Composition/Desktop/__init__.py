from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Desktop
class DesktopWindowTarget(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionTarget
    default_interface: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget
    _classid_ = 'Windows.UI.Composition.Desktop.DesktopWindowTarget'
    @winrt_mixinmethod
    def get_IsTopmost(self: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)
class IDesktopWindowTarget(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Composition.Desktop.IDesktopWindowTarget'
    _iid_ = Guid('{6329d6ca-3366-490e-9db3-25312929ac51}')
    @winrt_commethod(6)
    def get_IsTopmost(self) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)


make_ready(__name__)
