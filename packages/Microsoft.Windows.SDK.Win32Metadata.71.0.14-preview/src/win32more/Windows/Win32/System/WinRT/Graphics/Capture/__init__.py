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
class IMonitorGraphicsCaptureItemInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33274d14-a076-4048-8416-747e9b04db7b}')
    @commethod(3)
    def GetMonitor(self, monitor: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowGraphicsCaptureItemInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38e4c48b-94e6-4c44-9cfa-968193316c0c}')
    @commethod(3)
    def GetWindow(self, window: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
