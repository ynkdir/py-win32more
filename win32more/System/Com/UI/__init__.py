from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Com.UI
import win32more.UI.WindowsAndMessaging
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
def _define_IDummyHICONIncluder_head():
    class IDummyHICONIncluder(win32more.System.Com.IUnknown_head):
        Guid = Guid('947990de-cc28-11d2-a0-f7-00-80-5f-85-8f-b1')
    return IDummyHICONIncluder
def _define_IDummyHICONIncluder():
    IDummyHICONIncluder = win32more.System.Com.UI.IDummyHICONIncluder_head
    IDummyHICONIncluder.Dummy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON,win32more.Graphics.Gdi.HDC)(3, 'Dummy', ((1, 'h1'),(1, 'h2'),)))
    win32more.System.Com.IUnknown
    return IDummyHICONIncluder
def _define_IThumbnailExtractor_head():
    class IThumbnailExtractor(win32more.System.Com.IUnknown_head):
        Guid = Guid('969dc708-5c76-11d1-8d-86-00-00-f8-04-b0-57')
    return IThumbnailExtractor
def _define_IThumbnailExtractor():
    IThumbnailExtractor = win32more.System.Com.UI.IThumbnailExtractor_head
    IThumbnailExtractor.ExtractThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HBITMAP))(3, 'ExtractThumbnail', ((1, 'pStg'),(1, 'ulLength'),(1, 'ulHeight'),(1, 'pulOutputLength'),(1, 'pulOutputHeight'),(1, 'phOutputBitmap'),)))
    IThumbnailExtractor.OnFileUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head)(4, 'OnFileUpdated', ((1, 'pStg'),)))
    win32more.System.Com.IUnknown
    return IThumbnailExtractor
__all__ = [
    "IDummyHICONIncluder",
    "IThumbnailExtractor",
]
