from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Graphics.Capture
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
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3628e81b-3cac-4c60-b7-f4-23-ce-0e-0c-33-56')
    @commethod(3)
    def CreateForWindow(window: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), result: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateForMonitor(monitor: Windows.Win32.Graphics.Gdi.HMONITOR, riid: POINTER(Guid), result: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IGraphicsCaptureItemInterop')
__all__ = [
    "IGraphicsCaptureItemInterop",
]
_arch_optional = [
]
