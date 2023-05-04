from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Dxgi
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Direct3D11
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
def CreateDirect3D11DeviceFromDXGIDevice(dxgiDevice: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, graphicsDevice: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d11.dll')
def CreateDirect3D11SurfaceFromDXGISurface(dgxiSurface: Windows.Win32.Graphics.Dxgi.IDXGISurface_head, graphicsSurface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3DDxgiInterfaceAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9b3d012-3df2-4ee3-b8d1-8695f457d3c1}')
    @commethod(3)
    def GetInterface(self, iid: POINTER(Guid), p: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDirect3DDxgiInterfaceAccess')
