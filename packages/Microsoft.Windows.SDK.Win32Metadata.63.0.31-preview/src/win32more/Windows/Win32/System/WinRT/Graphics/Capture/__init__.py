from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Graphics.Capture
class IGraphicsCaptureItemInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3628e81b-3cac-4c60-b7f4-23ce0e0c3356}')
    @commethod(3)
    def CreateForWindow(self, window: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), result: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateForMonitor(self, monitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, riid: POINTER(Guid), result: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
