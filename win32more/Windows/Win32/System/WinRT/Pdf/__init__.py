from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.Dxgi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Pdf
@winfunctype('Windows.Data.Pdf.dll')
def PdfCreateRenderer(pDevice: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice, ppRenderer: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.IPdfRendererNative)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPdfRendererNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d9dcd91-d277-4947-8527-07a0daeda94a}')
    @commethod(3)
    def RenderPageToSurface(self, pdfPage: win32more.Windows.Win32.System.Com.IUnknown, pSurface: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface, offset: win32more.Windows.Win32.Foundation.POINT, pRenderParams: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderPageToDeviceContext(self, pdfPage: win32more.Windows.Win32.System.Com.IUnknown, pD2DDeviceContext: win32more.Windows.Win32.Graphics.Direct2D.ID2D1DeviceContext, pRenderParams: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PDF_RENDER_PARAMS(Structure):
    SourceRect: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_RECT_F
    DestinationWidth: UInt32
    DestinationHeight: UInt32
    BackgroundColor: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_COLOR_F
    IgnoreHighContrast: win32more.Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_PDF_CREATE_RENDERER(param0: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice, param1: POINTER(win32more.Windows.Win32.System.WinRT.Pdf.IPdfRendererNative)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
