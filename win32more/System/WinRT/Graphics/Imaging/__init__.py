from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Imaging
import win32more.Media.MediaFoundation
import win32more.System.WinRT
import win32more.System.WinRT.Graphics.Imaging
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
def _define_CLSID_SoftwareBitmapNativeFactory():
    return Guid('84e65691-8602-4a84-be-46-70-8b-e9-cd-4b-74')
def _define_ISoftwareBitmapNative_head():
    class ISoftwareBitmapNative(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('94bc8415-04ea-4b2e-af-13-4d-e9-5a-a8-98-eb')
    return ISoftwareBitmapNative
def _define_ISoftwareBitmapNative():
    ISoftwareBitmapNative = win32more.System.WinRT.Graphics.Imaging.ISoftwareBitmapNative_head
    ISoftwareBitmapNative.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(6, 'GetData', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return ISoftwareBitmapNative
def _define_ISoftwareBitmapNativeFactory_head():
    class ISoftwareBitmapNativeFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('c3c181ec-2914-4791-af-02-02-d2-24-a1-0b-43')
    return ISoftwareBitmapNativeFactory
def _define_ISoftwareBitmapNativeFactory():
    ISoftwareBitmapNativeFactory = win32more.System.WinRT.Graphics.Imaging.ISoftwareBitmapNativeFactory_head
    ISoftwareBitmapNativeFactory.CreateFromWICBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmap_head,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p))(6, 'CreateFromWICBitmap', ((1, 'data'),(1, 'forceReadOnly'),(1, 'riid'),(1, 'ppv'),)))
    ISoftwareBitmapNativeFactory.CreateFromMF2DBuffer2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMF2DBuffer2_head,POINTER(Guid),UInt32,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Media.MediaFoundation.MFVideoArea_head),POINTER(Guid),POINTER(c_void_p))(7, 'CreateFromMF2DBuffer2', ((1, 'data'),(1, 'subtype'),(1, 'width'),(1, 'height'),(1, 'forceReadOnly'),(1, 'minDisplayAperture'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return ISoftwareBitmapNativeFactory
__all__ = [
    "CLSID_SoftwareBitmapNativeFactory",
    "ISoftwareBitmapNative",
    "ISoftwareBitmapNativeFactory",
]
