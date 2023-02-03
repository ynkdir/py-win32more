from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct2D
import Windows.Win32.Graphics.Direct2D.Common
import Windows.Win32.Graphics.Dxgi
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Pdf
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
@winfunctype('Windows.Data.Pdf.dll')
def PdfCreateRenderer(pDevice: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, ppRenderer: POINTER(Windows.Win32.System.WinRT.Pdf.IPdfRendererNative_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPdfRendererNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7d9dcd91-d277-4947-85-27-07-a0-da-ed-a9-4a')
    @commethod(3)
    def RenderPageToSurface(pdfPage: Windows.Win32.System.Com.IUnknown_head, pSurface: Windows.Win32.Graphics.Dxgi.IDXGISurface_head, offset: Windows.Win32.Foundation.POINT, pRenderParams: POINTER(Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderPageToDeviceContext(pdfPage: Windows.Win32.System.Com.IUnknown_head, pD2DDeviceContext: Windows.Win32.Graphics.Direct2D.ID2D1DeviceContext_head, pRenderParams: POINTER(Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class PDF_RENDER_PARAMS(Structure):
    SourceRect: Windows.Win32.Graphics.Direct2D.Common.D2D_RECT_F
    DestinationWidth: UInt32
    DestinationHeight: UInt32
    BackgroundColor: Windows.Win32.Graphics.Direct2D.Common.D2D_COLOR_F
    IgnoreHighContrast: Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_PDF_CREATE_RENDERER(param0: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, param1: POINTER(Windows.Win32.System.WinRT.Pdf.IPdfRendererNative_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IPdfRendererNative')
make_head(_module, 'PDF_RENDER_PARAMS')
make_head(_module, 'PFN_PDF_CREATE_RENDERER')
__all__ = [
    "IPdfRendererNative",
    "PDF_RENDER_PARAMS",
    "PFN_PDF_CREATE_RENDERER",
    "PdfCreateRenderer",
]
_arch_optional = [
]
