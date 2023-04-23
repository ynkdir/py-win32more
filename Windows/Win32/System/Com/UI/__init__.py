from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Com.UI
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IDummyHICONIncluder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('947990de-cc28-11d2-a0-f7-00-80-5f-85-8f-b1')
    @commethod(3)
    def Dummy(self, h1: Windows.Win32.UI.WindowsAndMessaging.HICON, h2: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailExtractor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('969dc708-5c76-11d1-8d-86-00-00-f8-04-b0-57')
    @commethod(3)
    def ExtractThumbnail(self, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ulLength: UInt32, ulHeight: UInt32, pulOutputLength: POINTER(UInt32), pulOutputHeight: POINTER(UInt32), phOutputBitmap: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFileUpdated(self, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDummyHICONIncluder')
make_head(_module, 'IThumbnailExtractor')
