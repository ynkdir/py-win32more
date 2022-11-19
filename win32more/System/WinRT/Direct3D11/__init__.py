from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Direct3D11

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
def _define_IDirect3DDxgiInterfaceAccess_head():
    class IDirect3DDxgiInterfaceAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9b3d012-3df2-4ee3-b8d1-8695f457d3c1')
    return IDirect3DDxgiInterfaceAccess
def _define_IDirect3DDxgiInterfaceAccess():
    IDirect3DDxgiInterfaceAccess = win32more.System.WinRT.Direct3D11.IDirect3DDxgiInterfaceAccess_head
    IDirect3DDxgiInterfaceAccess.GetInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetInterface', ((1, 'iid'),(1, 'p'),)))
    win32more.System.Com.IUnknown
    return IDirect3DDxgiInterfaceAccess
def _define_CreateDirect3D11DeviceFromDXGIDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.System.WinRT.IInspectable_head), use_last_error=False)(("CreateDirect3D11DeviceFromDXGIDevice", windll["d3d11"]), ((1, 'dxgiDevice'),(1, 'graphicsDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirect3D11SurfaceFromDXGISurface():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head,POINTER(win32more.System.WinRT.IInspectable_head), use_last_error=False)(("CreateDirect3D11SurfaceFromDXGISurface", windll["d3d11"]), ((1, 'dgxiSurface'),(1, 'graphicsSurface'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "IDirect3DDxgiInterfaceAccess",
    "CreateDirect3D11DeviceFromDXGIDevice",
    "CreateDirect3D11SurfaceFromDXGISurface",
]
