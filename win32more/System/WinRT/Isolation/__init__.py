from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Isolation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IIsolatedEnvironmentInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('85713c2e-8e62-46c5-8d-e2-c6-47-e1-d5-46-36')
    @commethod(3)
    def GetHostHwndInterop(containerHwnd: win32more.Foundation.HWND, hostHwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IIsolatedEnvironmentInterop')
__all__ = [
    "IIsolatedEnvironmentInterop",
]
