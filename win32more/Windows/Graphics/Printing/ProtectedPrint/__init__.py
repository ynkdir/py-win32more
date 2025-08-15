from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Graphics.Printing.ProtectedPrint
class IWindowsProtectedPrintInfoStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Graphics.Printing.ProtectedPrint.IWindowsProtectedPrintInfoStatics'
    _iid_ = Guid('{a7d212f3-4168-5485-98ab-d89d04603b40}')
    @winrt_commethod(6)
    def get_IsProtectedPrintEnabled(self) -> Boolean: ...
    IsProtectedPrintEnabled = property(get_IsProtectedPrintEnabled, None)
class _WindowsProtectedPrintInfo_Meta_(ComPtr.__class__):
    pass
class WindowsProtectedPrintInfo(ComPtr, metaclass=_WindowsProtectedPrintInfo_Meta_):
    extends: IInspectable
    _classid_ = 'Windows.Graphics.Printing.ProtectedPrint.WindowsProtectedPrintInfo'
    @winrt_classmethod
    def get_IsProtectedPrintEnabled(cls: win32more.Windows.Graphics.Printing.ProtectedPrint.IWindowsProtectedPrintInfoStatics) -> Boolean: ...
    _WindowsProtectedPrintInfo_Meta_.IsProtectedPrintEnabled = property(get_IsProtectedPrintEnabled, None)


make_ready(__name__)
