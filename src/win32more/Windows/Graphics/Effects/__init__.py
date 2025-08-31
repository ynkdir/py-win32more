from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Graphics.Effects
class IGraphicsEffect(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Graphics.Effects.IGraphicsEffect'
    _iid_ = Guid('{cb51c0ce-8fe6-4636-b202-861faa07d8f3}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, name: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
class IGraphicsEffectSource(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Graphics.Effects.IGraphicsEffectSource'
    _iid_ = Guid('{2d8f9ddc-4339-4eb9-9216-f9deb75658a2}')


make_ready(__name__)
