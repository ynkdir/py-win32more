from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Imaging
import win32more.Windows.Win32.Media.MediaFoundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Graphics.Imaging
CLSID_SoftwareBitmapNativeFactory: Guid = Guid('{84e65691-8602-4a84-be46-708be9cd4b74}')
class ISoftwareBitmapNative(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{94bc8415-04ea-4b2e-af13-4de95aa898eb}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISoftwareBitmapNativeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c3c181ec-2914-4791-af02-02d224a10b43}')
    @commethod(6)
    def CreateFromWICBitmap(self, data: win32more.Windows.Win32.Graphics.Imaging.IWICBitmap, forceReadOnly: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateFromMF2DBuffer2(self, data: win32more.Windows.Win32.Media.MediaFoundation.IMF2DBuffer2, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: win32more.Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(win32more.Windows.Win32.Media.MediaFoundation.MFVideoArea), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
