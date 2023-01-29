from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.WinRT.Graphics.Capture
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IGraphicsCaptureItemInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3628e81b-3cac-4c60-b7-f4-23-ce-0e-0c-33-56')
    @commethod(3)
    def CreateForWindow(window: win32more.Foundation.HWND, riid: POINTER(Guid), result: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateForMonitor(monitor: win32more.Graphics.Gdi.HMONITOR, riid: POINTER(Guid), result: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IGraphicsCaptureItemInterop')
__all__ = [
    "IGraphicsCaptureItemInterop",
]
_arch_optional = [
]
