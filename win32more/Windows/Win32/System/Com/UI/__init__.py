from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Com.UI
import win32more.Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IDummyHICONIncluder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{947990de-cc28-11d2-a0f7-00805f858fb1}')
    @commethod(3)
    def Dummy(self, h1: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, h2: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailExtractor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{969dc708-5c76-11d1-8d86-0000f804b057}')
    @commethod(3)
    def ExtractThumbnail(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head, ulLength: UInt32, ulHeight: UInt32, pulOutputLength: POINTER(UInt32), pulOutputHeight: POINTER(UInt32), phOutputBitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFileUpdated(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDummyHICONIncluder')
make_head(_module, 'IThumbnailExtractor')
