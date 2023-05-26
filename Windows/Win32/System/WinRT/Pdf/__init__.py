from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('Windows.Data.Pdf.dll')
def PdfCreateRenderer(pDevice: Windows.Win32.Graphics.Dxgi.IDXGIDevice_head, ppRenderer: POINTER(Windows.Win32.System.WinRT.Pdf.IPdfRendererNative_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPdfRendererNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d9dcd91-d277-4947-8527-07a0daeda94a}')
    @commethod(3)
    def RenderPageToSurface(self, pdfPage: Windows.Win32.System.Com.IUnknown_head, pSurface: Windows.Win32.Graphics.Dxgi.IDXGISurface_head, offset: Windows.Win32.Foundation.POINT, pRenderParams: POINTER(Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderPageToDeviceContext(self, pdfPage: Windows.Win32.System.Com.IUnknown_head, pD2DDeviceContext: Windows.Win32.Graphics.Direct2D.ID2D1DeviceContext_head, pRenderParams: POINTER(Windows.Win32.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class PDF_RENDER_PARAMS(EasyCastStructure):
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
