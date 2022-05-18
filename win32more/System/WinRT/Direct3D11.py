from win32more import *
import win32more.Foundation
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Direct3D11

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_IDirect3DDxgiInterfaceAccess_head():
    class IDirect3DDxgiInterfaceAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9b3d012-3df2-4ee3-b8d1-8695f457d3c1')
    return IDirect3DDxgiInterfaceAccess
def _define_IDirect3DDxgiInterfaceAccess():
    IDirect3DDxgiInterfaceAccess = win32more.System.WinRT.Direct3D11.IDirect3DDxgiInterfaceAccess_head
    IDirect3DDxgiInterfaceAccess.GetInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetInterface', ((1, 'iid'),(1, 'p'),)))
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
