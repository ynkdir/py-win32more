from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Imaging
import win32more.Graphics.Imaging.D2D
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IWICImageEncoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('04c75bf8-3ce1-473b-ac-c5-3c-c4-f5-e9-49-99')
    @commethod(3)
    def WriteFrame(pImage: win32more.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: win32more.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(win32more.Graphics.Imaging.WICImageParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WriteFrameThumbnail(pImage: win32more.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: win32more.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(win32more.Graphics.Imaging.WICImageParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def WriteThumbnail(pImage: win32more.Graphics.Direct2D.ID2D1Image_head, pEncoder: win32more.Graphics.Imaging.IWICBitmapEncoder_head, pImageParameters: POINTER(win32more.Graphics.Imaging.WICImageParameters_head)) -> win32more.Foundation.HRESULT: ...
class IWICImagingFactory2(c_void_p):
    extends: win32more.Graphics.Imaging.IWICImagingFactory
    Guid = Guid('7b816b45-1996-4476-b1-32-de-9e-24-7c-8a-f0')
    @commethod(28)
    def CreateImageEncoder(pD2DDevice: win32more.Graphics.Direct2D.ID2D1Device_head, ppWICImageEncoder: POINTER(win32more.Graphics.Imaging.D2D.IWICImageEncoder_head)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IWICImageEncoder')
make_head(_module, 'IWICImagingFactory2')
__all__ = [
    "IWICImageEncoder",
    "IWICImagingFactory2",
]
