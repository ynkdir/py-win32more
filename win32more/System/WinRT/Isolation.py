from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Isolation

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IIsolatedEnvironmentInterop_head():
    class IIsolatedEnvironmentInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('85713c2e-8e62-46c5-8de2-c647e1d54636')
    return IIsolatedEnvironmentInterop
def _define_IIsolatedEnvironmentInterop():
    IIsolatedEnvironmentInterop = win32more.System.WinRT.Isolation.IIsolatedEnvironmentInterop_head
    IIsolatedEnvironmentInterop.GetHostHwndInterop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'GetHostHwndInterop', ((1, 'containerHwnd'),(1, 'hostHwnd'),)))
    win32more.System.Com.IUnknown
    return IIsolatedEnvironmentInterop
__all__ = [
    "IIsolatedEnvironmentInterop",
]
