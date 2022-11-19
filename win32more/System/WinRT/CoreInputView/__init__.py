from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.WinRT
import win32more.System.WinRT.CoreInputView

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
def _define_ICoreFrameworkInputViewInterop_head():
    class ICoreFrameworkInputViewInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('0e3da342-b11c-484b-9c1c-be0d61c2f6c5')
    return ICoreFrameworkInputViewInterop
def _define_ICoreFrameworkInputViewInterop():
    ICoreFrameworkInputViewInterop = win32more.System.WinRT.CoreInputView.ICoreFrameworkInputViewInterop_head
    ICoreFrameworkInputViewInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'coreFrameworkInputView'),)))
    win32more.System.WinRT.IInspectable
    return ICoreFrameworkInputViewInterop
__all__ = [
    "ICoreFrameworkInputViewInterop",
]
