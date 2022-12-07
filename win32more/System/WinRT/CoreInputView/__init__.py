from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.WinRT
import win32more.System.WinRT.CoreInputView
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
class ICoreFrameworkInputViewInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('0e3da342-b11c-484b-9c-1c-be-0d-61-c2-f6-c5')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), coreFrameworkInputView: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'ICoreFrameworkInputViewInterop')
__all__ = [
    "ICoreFrameworkInputViewInterop",
]
