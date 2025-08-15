from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Isolation
class IIsolatedEnvironmentInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85713c2e-8e62-46c5-8de2-c647e1d54636}')
    @commethod(3)
    def GetHostHwndInterop(self, containerHwnd: win32more.Windows.Win32.Foundation.HWND, hostHwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
