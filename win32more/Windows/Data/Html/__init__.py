from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Data.Html
class HtmlUtilities(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Data.Html.HtmlUtilities'
    @winrt_classmethod
    def ConvertToText(cls: win32more.Windows.Data.Html.IHtmlUtilities, html: WinRT_String) -> WinRT_String: ...
class IHtmlUtilities(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Data.Html.IHtmlUtilities'
    _iid_ = Guid('{fec00add-2399-4fac-b5a7-05e9acd7181d}')
    @winrt_commethod(6)
    def ConvertToText(self, html: WinRT_String) -> WinRT_String: ...


make_ready(__name__)
