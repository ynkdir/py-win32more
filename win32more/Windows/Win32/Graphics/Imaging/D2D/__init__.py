from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.Graphics.Imaging
import win32more.Windows.Win32.Graphics.Imaging.D2D
import win32more.Windows.Win32.System.Com
class IWICImageEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04c75bf8-3ce1-473b-acc5-3cc4f5e94999}')
    @commethod(3)
    def WriteFrame(self, pImage: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Image, pFrameEncode: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode, pImageParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICImageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteFrameThumbnail(self, pImage: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Image, pFrameEncode: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode, pImageParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICImageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteThumbnail(self, pImage: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Image, pEncoder: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapEncoder, pImageParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICImageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICImagingFactory2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICImagingFactory
    _iid_ = Guid('{7b816b45-1996-4476-b132-de9e247c8af0}')
    @commethod(28)
    def CreateImageEncoder(self, pD2DDevice: win32more.Windows.Win32.Graphics.Direct2D.ID2D1Device, ppWICImageEncoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.D2D.IWICImageEncoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
