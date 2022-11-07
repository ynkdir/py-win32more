from win32more import *
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.WinRT.Graphics.Capture

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
def _define_IGraphicsCaptureItemInterop_head():
    class IGraphicsCaptureItemInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('3628e81b-3cac-4c60-b7f4-23ce0e0c3356')
    return IGraphicsCaptureItemInterop
def _define_IGraphicsCaptureItemInterop():
    IGraphicsCaptureItemInterop = win32more.System.WinRT.Graphics.Capture.IGraphicsCaptureItemInterop_head
    IGraphicsCaptureItemInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateForWindow', ((1, 'window'),(1, 'riid'),(1, 'result'),)))
    IGraphicsCaptureItemInterop.CreateForMonitor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HMONITOR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'CreateForMonitor', ((1, 'monitor'),(1, 'riid'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return IGraphicsCaptureItemInterop
__all__ = [
    "IGraphicsCaptureItemInterop",
]
