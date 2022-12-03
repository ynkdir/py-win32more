from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.WinRT
import win32more.UI.Input.Radial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IRadialControllerConfigurationInterop_head():
    class IRadialControllerConfigurationInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('787cdaac-3186-476d-87-e4-b9-37-4a-7b-99-70')
    return IRadialControllerConfigurationInterop
def _define_IRadialControllerConfigurationInterop():
    IRadialControllerConfigurationInterop = win32more.UI.Input.Radial.IRadialControllerConfigurationInterop_head
    IRadialControllerConfigurationInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IRadialControllerConfigurationInterop
def _define_IRadialControllerIndependentInputSourceInterop_head():
    class IRadialControllerIndependentInputSourceInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('3d577eff-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    return IRadialControllerIndependentInputSourceInterop
def _define_IRadialControllerIndependentInputSourceInterop():
    IRadialControllerIndependentInputSourceInterop = win32more.UI.Input.Radial.IRadialControllerIndependentInputSourceInterop_head
    IRadialControllerIndependentInputSourceInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'CreateForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IRadialControllerIndependentInputSourceInterop
def _define_IRadialControllerInterop_head():
    class IRadialControllerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('1b0535c9-57ad-45c1-9d-79-ad-5c-34-36-05-13')
    return IRadialControllerInterop
def _define_IRadialControllerInterop():
    IRadialControllerInterop = win32more.UI.Input.Radial.IRadialControllerInterop_head
    IRadialControllerInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'CreateForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IRadialControllerInterop
__all__ = [
    "IRadialControllerConfigurationInterop",
    "IRadialControllerIndependentInputSourceInterop",
    "IRadialControllerInterop",
]
