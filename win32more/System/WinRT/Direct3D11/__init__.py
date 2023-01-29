from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Direct3D11
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
@winfunctype('d3d11.dll')
def CreateDirect3D11DeviceFromDXGIDevice(dxgiDevice: win32more.Graphics.Dxgi.IDXGIDevice_head, graphicsDevice: POINTER(win32more.System.WinRT.IInspectable_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('d3d11.dll')
def CreateDirect3D11SurfaceFromDXGISurface(dgxiSurface: win32more.Graphics.Dxgi.IDXGISurface_head, graphicsSurface: POINTER(win32more.System.WinRT.IInspectable_head)) -> win32more.Foundation.HRESULT: ...
class IDirect3DDxgiInterfaceAccess(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9b3d012-3df2-4ee3-b8-d1-86-95-f4-57-d3-c1')
    @commethod(3)
    def GetInterface(iid: POINTER(Guid), p: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IDirect3DDxgiInterfaceAccess')
__all__ = [
    "CreateDirect3D11DeviceFromDXGIDevice",
    "CreateDirect3D11SurfaceFromDXGISurface",
    "IDirect3DDxgiInterfaceAccess",
]
_arch_optional = [
]
