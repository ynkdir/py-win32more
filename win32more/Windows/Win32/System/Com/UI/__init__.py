from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Com.UI
import win32more.Windows.Win32.UI.WindowsAndMessaging
class IDummyHICONIncluder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{947990de-cc28-11d2-a0f7-00805f858fb1}')
    @commethod(3)
    def Dummy(self, h1: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, h2: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailExtractor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{969dc708-5c76-11d1-8d86-0000f804b057}')
    @commethod(3)
    def ExtractThumbnail(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ulLength: UInt32, ulHeight: UInt32, pulOutputLength: POINTER(UInt32), pulOutputHeight: POINTER(UInt32), phOutputBitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFileUpdated(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
