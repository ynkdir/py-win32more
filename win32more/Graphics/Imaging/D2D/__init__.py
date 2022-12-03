from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Imaging
import win32more.Graphics.Imaging.D2D
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IWICImageEncoder_head():
    class IWICImageEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('04c75bf8-3ce1-473b-ac-c5-3c-c4-f5-e9-49-99')
    return IWICImageEncoder
def _define_IWICImageEncoder():
    IWICImageEncoder = win32more.Graphics.Imaging.D2D.IWICImageEncoder_head
    IWICImageEncoder.WriteFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapFrameEncode_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head))(3, 'WriteFrame', ((1, 'pImage'),(1, 'pFrameEncode'),(1, 'pImageParameters'),)))
    IWICImageEncoder.WriteFrameThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapFrameEncode_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head))(4, 'WriteFrameThumbnail', ((1, 'pImage'),(1, 'pFrameEncode'),(1, 'pImageParameters'),)))
    IWICImageEncoder.WriteThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Imaging.IWICBitmapEncoder_head,POINTER(win32more.Graphics.Imaging.WICImageParameters_head))(5, 'WriteThumbnail', ((1, 'pImage'),(1, 'pEncoder'),(1, 'pImageParameters'),)))
    win32more.System.Com.IUnknown
    return IWICImageEncoder
def _define_IWICImagingFactory2_head():
    class IWICImagingFactory2(win32more.Graphics.Imaging.IWICImagingFactory_head):
        Guid = Guid('7b816b45-1996-4476-b1-32-de-9e-24-7c-8a-f0')
    return IWICImagingFactory2
def _define_IWICImagingFactory2():
    IWICImagingFactory2 = win32more.Graphics.Imaging.D2D.IWICImagingFactory2_head
    IWICImagingFactory2.CreateImageEncoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Device_head,POINTER(win32more.Graphics.Imaging.D2D.IWICImageEncoder_head))(28, 'CreateImageEncoder', ((1, 'pD2DDevice'),(1, 'ppWICImageEncoder'),)))
    win32more.Graphics.Imaging.IWICImagingFactory
    return IWICImagingFactory2
__all__ = [
    "IWICImageEncoder",
    "IWICImagingFactory2",
]
