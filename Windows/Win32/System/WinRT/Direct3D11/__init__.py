from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
    def GetInterface(self, iid: POINTER(Guid), p: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDirect3DDxgiInterfaceAccess')
