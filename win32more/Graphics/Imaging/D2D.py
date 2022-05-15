from win32more import *
import win32more.Graphics.Imaging.D2D
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Imaging
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Graphics.Imaging.D2D, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Graphics.Imaging.D2D, name)
def __dir__():
    return __all__
def _define_IWICImageEncoder_head():
    class IWICImageEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('04c75bf8-3ce1-473b-acc5-3cc4f5e94999')
    return IWICImageEncoder
def _define_IWICImageEncoder():
    IWICImageEncoder = win32more.Graphics.Imaging.D2D.IWICImageEncoder_head
    IWICImageEncoder.WriteFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapFrameEncode_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head), use_last_error=False)(3, 'WriteFrame', ((1, 'pImage'),(1, 'pFrameEncode'),(1, 'pImageParameters'),)))
    IWICImageEncoder.WriteFrameThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapFrameEncode_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head), use_last_error=False)(4, 'WriteFrameThumbnail', ((1, 'pImage'),(1, 'pFrameEncode'),(1, 'pImageParameters'),)))
    IWICImageEncoder.WriteThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapEncoder_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head), use_last_error=False)(5, 'WriteThumbnail', ((1, 'pImage'),(1, 'pEncoder'),(1, 'pImageParameters'),)))
    return IWICImageEncoder
def _define_IWICImagingFactory2_head():
    class IWICImagingFactory2(win32more.Graphics.Imaging.IWICImagingFactory_head):
        Guid = Guid('7b816b45-1996-4476-b132-de9e247c8af0')
    return IWICImagingFactory2
def _define_IWICImagingFactory2():
    IWICImagingFactory2 = win32more.Graphics.Imaging.D2D.IWICImagingFactory2_head
    IWICImagingFactory2.CreateImageEncoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Device_head,POINTER(win32more.Graphics.Imaging.D2D.IWICImageEncoder_head), use_last_error=False)(28, 'CreateImageEncoder', ((1, 'pD2DDevice'),(1, 'ppWICImageEncoder'),)))
    return IWICImagingFactory2
__all__ = [
    "IWICImageEncoder",
    "IWICImagingFactory2",
]
