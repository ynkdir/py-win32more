from win32more import *
import win32more.System.WinRT.Pdf
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Dxgi
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.WinRT.Pdf, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.WinRT.Pdf, name)
def __dir__():
    return __all__
def _define_PFN_PDF_CREATE_RENDERER():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head), use_last_error=False)
def _define_PDF_RENDER_PARAMS_head():
    class PDF_RENDER_PARAMS(Structure):
        pass
    return PDF_RENDER_PARAMS
def _define_PDF_RENDER_PARAMS():
    PDF_RENDER_PARAMS = win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head
    PDF_RENDER_PARAMS._fields_ = [
        ("SourceRect", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ("DestinationWidth", UInt32),
        ("DestinationHeight", UInt32),
        ("BackgroundColor", win32more.Graphics.Direct2D.Common.D2D_COLOR_F),
        ("IgnoreHighContrast", win32more.Foundation.BOOLEAN),
    ]
    return PDF_RENDER_PARAMS
def _define_IPdfRendererNative_head():
    class IPdfRendererNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d9dcd91-d277-4947-8527-07a0daeda94a')
    return IPdfRendererNative
def _define_IPdfRendererNative():
    IPdfRendererNative = win32more.System.WinRT.Pdf.IPdfRendererNative_head
    IPdfRendererNative.RenderPageToSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.Dxgi.IDXGISurface_head,win32more.Foundation.POINT,POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head), use_last_error=False)(3, 'RenderPageToSurface', ((1, 'pdfPage'),(1, 'pSurface'),(1, 'offset'),(1, 'pRenderParams'),)))
    IPdfRendererNative.RenderPageToDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.Direct2D.ID2D1DeviceContext_head,POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head), use_last_error=False)(4, 'RenderPageToDeviceContext', ((1, 'pdfPage'),(1, 'pD2DDeviceContext'),(1, 'pRenderParams'),)))
    return IPdfRendererNative
def _define_PdfCreateRenderer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head), use_last_error=False)(("PdfCreateRenderer", windll["Windows.Data.Pdf"]), ((1, 'pDevice'),(1, 'ppRenderer'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PFN_PDF_CREATE_RENDERER",
    "PDF_RENDER_PARAMS",
    "IPdfRendererNative",
    "PdfCreateRenderer",
]
