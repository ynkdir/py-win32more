from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dxgi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Direct3D11
@winfunctype('d3d11.dll')
def CreateDirect3D11DeviceFromDXGIDevice(dxgiDevice: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice, graphicsDevice: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('d3d11.dll')
def CreateDirect3D11SurfaceFromDXGISurface(dgxiSurface: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface, graphicsSurface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDirect3DDxgiInterfaceAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9b3d012-3df2-4ee3-b8d1-8695f457d3c1}')
    @commethod(3)
    def GetInterface(self, iid: POINTER(Guid), p: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
