from win32more import *
import win32more.System.WinRT.Isolation
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.Isolation, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.Isolation, name)
def _define_IIsolatedEnvironmentInterop_head():
    class IIsolatedEnvironmentInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('85713c2e-8e62-46c5-8de2-c647e1d54636')
    return IIsolatedEnvironmentInterop
def _define_IIsolatedEnvironmentInterop():
    IIsolatedEnvironmentInterop = win32more.System.WinRT.Isolation.IIsolatedEnvironmentInterop_head
    IIsolatedEnvironmentInterop.GetHostHwndInterop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'GetHostHwndInterop', ((1, 'containerHwnd'),(1, 'hostHwnd'),)))
    return IIsolatedEnvironmentInterop
__all__ = [
    "IIsolatedEnvironmentInterop",
]
