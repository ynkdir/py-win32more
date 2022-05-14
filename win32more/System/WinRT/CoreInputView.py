from win32more import *
import win32more.System.WinRT.CoreInputView
import win32more.Foundation
import win32more.System.WinRT

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.CoreInputView, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.CoreInputView, name)
def _define_ICoreFrameworkInputViewInterop_head():
    class ICoreFrameworkInputViewInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('0e3da342-b11c-484b-9c1c-be0d61c2f6c5')
    return ICoreFrameworkInputViewInterop
def _define_ICoreFrameworkInputViewInterop():
    ICoreFrameworkInputViewInterop = win32more.System.WinRT.CoreInputView.ICoreFrameworkInputViewInterop_head
    ICoreFrameworkInputViewInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'coreFrameworkInputView'),)))
    return ICoreFrameworkInputViewInterop
__all__ = [
    "ICoreFrameworkInputViewInterop",
]
