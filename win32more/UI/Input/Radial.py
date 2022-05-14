from win32more import *
import win32more.UI.Input.Radial
import win32more.Foundation
import win32more.System.WinRT

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.Input.Radial, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.Input.Radial, name)
def _define_IRadialControllerInterop_head():
    class IRadialControllerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('1b0535c9-57ad-45c1-9d79-ad5c34360513')
    return IRadialControllerInterop
def _define_IRadialControllerInterop():
    IRadialControllerInterop = win32more.UI.Input.Radial.IRadialControllerInterop_head
    IRadialControllerInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    return IRadialControllerInterop
def _define_IRadialControllerConfigurationInterop_head():
    class IRadialControllerConfigurationInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('787cdaac-3186-476d-87e4-b9374a7b9970')
    return IRadialControllerConfigurationInterop
def _define_IRadialControllerConfigurationInterop():
    IRadialControllerConfigurationInterop = win32more.UI.Input.Radial.IRadialControllerConfigurationInterop_head
    IRadialControllerConfigurationInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    return IRadialControllerConfigurationInterop
def _define_IRadialControllerIndependentInputSourceInterop_head():
    class IRadialControllerIndependentInputSourceInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('3d577eff-4cee-11e6-b535-001bdc06ab3b')
    return IRadialControllerIndependentInputSourceInterop
def _define_IRadialControllerIndependentInputSourceInterop():
    IRadialControllerIndependentInputSourceInterop = win32more.UI.Input.Radial.IRadialControllerIndependentInputSourceInterop_head
    IRadialControllerIndependentInputSourceInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    return IRadialControllerIndependentInputSourceInterop
__all__ = [
    "IRadialControllerInterop",
    "IRadialControllerConfigurationInterop",
    "IRadialControllerIndependentInputSourceInterop",
]
