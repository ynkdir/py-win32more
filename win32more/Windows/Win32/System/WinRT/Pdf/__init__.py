from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.Dxgi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Pdf
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('Windows.Data.Pdf.dll')
def PdfCreateRenderer(pDevice: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, ppRenderer: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.IPdfRendererNative_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPdfRendererNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d9dcd91-d277-4947-8527-07a0daeda94a}')
    @commethod(3)
    def RenderPageToSurface(self, pdfPage: win32more.Windows.Win32.System.Com.IUnknown_head, pSurface: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface_head, offset: win32more.Windows.Win32.Foundation.POINT, pRenderParams: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderPageToDeviceContext(self, pdfPage: win32more.Windows.Win32.System.Com.IUnknown_head, pD2DDeviceContext: win32more.Windows.Win32.Graphics.Direct2D.ID2D1DeviceContext_head, pRenderParams: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PDF_RENDER_PARAMS(EasyCastStructure):
    SourceRect: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_RECT_F
    DestinationWidth: UInt32
    DestinationHeight: UInt32
    BackgroundColor: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_COLOR_F
    IgnoreHighContrast: win32more.Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_PDF_CREATE_RENDERER(param0: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, param1: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.IPdfRendererNative_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IPdfRendererNative')
make_head(_module, 'PDF_RENDER_PARAMS')
make_head(_module, 'PFN_PDF_CREATE_RENDERER')
