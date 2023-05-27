from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dxgi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Direct3D11
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('d3d11.dll')
def CreateDirect3D11DeviceFromDXGIDevice(dxgiDevice: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, graphicsDevice: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d11.dll')
def CreateDirect3D11SurfaceFromDXGISurface(dgxiSurface: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface_head, graphicsSurface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirect3DDxgiInterfaceAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9b3d012-3df2-4ee3-b8d1-8695f457d3c1}')
    @commethod(3)
    def GetInterface(self, iid: POINTER(Guid), p: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDirect3DDxgiInterfaceAccess')
