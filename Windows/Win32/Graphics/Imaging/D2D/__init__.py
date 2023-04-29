from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct2D
import Windows.Win32.Graphics.Imaging
import Windows.Win32.Graphics.Imaging.D2D
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWICImageEncoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('04c75bf8-3ce1-473b-ac-c5-3c-c4-f5-e9-49-99')
    @commethod(3)
    def WriteFrame(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteFrameThumbnail(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteThumbnail(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pEncoder: Windows.Win32.Graphics.Imaging.IWICBitmapEncoder_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICImagingFactory2(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICImagingFactory
    Guid = Guid('7b816b45-1996-4476-b1-32-de-9e-24-7c-8a-f0')
    @commethod(28)
    def CreateImageEncoder(self, pD2DDevice: Windows.Win32.Graphics.Direct2D.ID2D1Device_head, ppWICImageEncoder: POINTER(Windows.Win32.Graphics.Imaging.D2D.IWICImageEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IWICImageEncoder')
make_head(_module, 'IWICImagingFactory2')
