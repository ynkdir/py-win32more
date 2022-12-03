from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Com.Marshal
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
def _define_BSTR_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.BSTR))(('BSTR_UserSize', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR))(('BSTR_UserMarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR))(('BSTR_UserUnmarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(('BSTR_UserFree', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.HWND))(('HWND_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND))(('HWND_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND))(('HWND_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.HWND))(('HWND_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserSize', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserMarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserUnmarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserFree', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.BSTR))(('BSTR_UserSize64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR))(('BSTR_UserMarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR))(('BSTR_UserUnmarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(('BSTR_UserFree64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.HWND))(('HWND_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND))(('HWND_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND))(('HWND_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.HWND))(('HWND_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserSize64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserMarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserUnmarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.VARIANT_head))(('VARIANT_UserFree64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(UInt16))(('CLIPFORMAT_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16))(('CLIPFORMAT_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16))(('CLIPFORMAT_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt16))(('CLIPFORMAT_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserSize', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserMarshal', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserUnmarshal', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(POINTER(UInt16))))(('SNB_UserFree', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(UInt16))(('CLIPFORMAT_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16))(('CLIPFORMAT_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16))(('CLIPFORMAT_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt16))(('CLIPFORMAT_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HBITMAP))(('HBITMAP_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HDC))(('HDC_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HICON))(('HICON_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserSize64', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserMarshal64', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))))(('SNB_UserUnmarshal64', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(POINTER(UInt16))))(('SNB_UserFree64', windll['ole32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.STGMEDIUM_head))(('STGMEDIUM_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetMarshalSizeMax():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32)(('CoGetMarshalSizeMax', windll['OLE32.dll']), ((1, 'pulSize'),(1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalInterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32)(('CoMarshalInterface', windll['OLE32.dll']), ((1, 'pStm'),(1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoUnmarshalInterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p))(('CoUnmarshalInterface', windll['OLE32.dll']), ((1, 'pStm'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalHresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.HRESULT)(('CoMarshalHresult', windll['OLE32.dll']), ((1, 'pstm'),(1, 'hresult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoUnmarshalHresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.HRESULT))(('CoUnmarshalHresult', windll['OLE32.dll']), ((1, 'pstm'),(1, 'phresult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoReleaseMarshalData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(('CoReleaseMarshalData', windll['OLE32.dll']), ((1, 'pStm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetStandardMarshal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32,POINTER(win32more.System.Com.Marshal.IMarshal_head))(('CoGetStandardMarshal', windll['OLE32.dll']), ((1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'ppMarshal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetStdMarshalEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.System.Com.IUnknown_head))(('CoGetStdMarshalEx', windll['OLE32.dll']), ((1, 'pUnkOuter'),(1, 'smexflags'),(1, 'ppUnkInner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalInterThreadInterfaceInStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IStream_head))(('CoMarshalInterThreadInterfaceInStream', windll['OLE32.dll']), ((1, 'riid'),(1, 'pUnk'),(1, 'ppStm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserSize', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserMarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserUnmarshal', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserFree', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserSize64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserMarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserUnmarshal64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('LPSAFEARRAY_UserFree64', windll['OLEAUT32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(IntPtr))(('HGLOBAL_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr))(('HGLOBAL_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr))(('HGLOBAL_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(IntPtr))(('HGLOBAL_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HACCEL))(('HACCEL_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(IntPtr))(('HGLOBAL_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr))(('HGLOBAL_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr))(('HGLOBAL_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(IntPtr))(('HGLOBAL_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HMENU))(('HMENU_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserSize', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserMarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserUnmarshal', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserFree', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserSize64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserMarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserUnmarshal64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HPALETTE))(('HPALETTE_UserFree64', windll['OLE32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IMarshal_head():
    class IMarshal(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000003-0000-0000-c0-00-00-00-00-00-00-46')
    return IMarshal
def _define_IMarshal():
    IMarshal = win32more.System.Com.Marshal.IMarshal_head
    IMarshal.GetUnmarshalClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32,POINTER(Guid))(3, 'GetUnmarshalClass', ((1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'pCid'),)))
    IMarshal.GetMarshalSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(4, 'GetMarshalSizeMax', ((1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'pSize'),)))
    IMarshal.MarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32)(5, 'MarshalInterface', ((1, 'pStm'),(1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),)))
    IMarshal.UnmarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p))(6, 'UnmarshalInterface', ((1, 'pStm'),(1, 'riid'),(1, 'ppv'),)))
    IMarshal.ReleaseMarshalData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(7, 'ReleaseMarshalData', ((1, 'pStm'),)))
    IMarshal.DisconnectObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'DisconnectObject', ((1, 'dwReserved'),)))
    win32more.System.Com.IUnknown
    return IMarshal
def _define_IMarshal2_head():
    class IMarshal2(win32more.System.Com.Marshal.IMarshal_head):
        Guid = Guid('000001cf-0000-0000-c0-00-00-00-00-00-00-46')
    return IMarshal2
def _define_IMarshal2():
    IMarshal2 = win32more.System.Com.Marshal.IMarshal2_head
    win32more.System.Com.Marshal.IMarshal
    return IMarshal2
def _define_IMarshalingStream_head():
    class IMarshalingStream(win32more.System.Com.IStream_head):
        Guid = Guid('d8f2f5e6-6102-4863-9f-26-38-9a-46-76-ef-de')
    return IMarshalingStream
def _define_IMarshalingStream():
    IMarshalingStream = win32more.System.Com.Marshal.IMarshalingStream_head
    IMarshalingStream.GetMarshalingContextAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CO_MARSHALING_CONTEXT_ATTRIBUTES,POINTER(UIntPtr))(14, 'GetMarshalingContextAttribute', ((1, 'attribute'),(1, 'pAttributeValue'),)))
    win32more.System.Com.IStream
    return IMarshalingStream
STDMSHLFLAGS = Int32
SMEXF_SERVER = 1
SMEXF_HANDLER = 2
__all__ = [
    "BSTR_UserFree",
    "BSTR_UserFree64",
    "BSTR_UserMarshal",
    "BSTR_UserMarshal64",
    "BSTR_UserSize",
    "BSTR_UserSize64",
    "BSTR_UserUnmarshal",
    "BSTR_UserUnmarshal64",
    "CLIPFORMAT_UserFree",
    "CLIPFORMAT_UserFree64",
    "CLIPFORMAT_UserMarshal",
    "CLIPFORMAT_UserMarshal64",
    "CLIPFORMAT_UserSize",
    "CLIPFORMAT_UserSize64",
    "CLIPFORMAT_UserUnmarshal",
    "CLIPFORMAT_UserUnmarshal64",
    "CoGetMarshalSizeMax",
    "CoGetStandardMarshal",
    "CoGetStdMarshalEx",
    "CoMarshalHresult",
    "CoMarshalInterThreadInterfaceInStream",
    "CoMarshalInterface",
    "CoReleaseMarshalData",
    "CoUnmarshalHresult",
    "CoUnmarshalInterface",
    "HACCEL_UserFree",
    "HACCEL_UserFree64",
    "HACCEL_UserMarshal",
    "HACCEL_UserMarshal64",
    "HACCEL_UserSize",
    "HACCEL_UserSize64",
    "HACCEL_UserUnmarshal",
    "HACCEL_UserUnmarshal64",
    "HBITMAP_UserFree",
    "HBITMAP_UserFree64",
    "HBITMAP_UserMarshal",
    "HBITMAP_UserMarshal64",
    "HBITMAP_UserSize",
    "HBITMAP_UserSize64",
    "HBITMAP_UserUnmarshal",
    "HBITMAP_UserUnmarshal64",
    "HDC_UserFree",
    "HDC_UserFree64",
    "HDC_UserMarshal",
    "HDC_UserMarshal64",
    "HDC_UserSize",
    "HDC_UserSize64",
    "HDC_UserUnmarshal",
    "HDC_UserUnmarshal64",
    "HGLOBAL_UserFree",
    "HGLOBAL_UserFree64",
    "HGLOBAL_UserMarshal",
    "HGLOBAL_UserMarshal64",
    "HGLOBAL_UserSize",
    "HGLOBAL_UserSize64",
    "HGLOBAL_UserUnmarshal",
    "HGLOBAL_UserUnmarshal64",
    "HICON_UserFree",
    "HICON_UserFree64",
    "HICON_UserMarshal",
    "HICON_UserMarshal64",
    "HICON_UserSize",
    "HICON_UserSize64",
    "HICON_UserUnmarshal",
    "HICON_UserUnmarshal64",
    "HMENU_UserFree",
    "HMENU_UserFree64",
    "HMENU_UserMarshal",
    "HMENU_UserMarshal64",
    "HMENU_UserSize",
    "HMENU_UserSize64",
    "HMENU_UserUnmarshal",
    "HMENU_UserUnmarshal64",
    "HPALETTE_UserFree",
    "HPALETTE_UserFree64",
    "HPALETTE_UserMarshal",
    "HPALETTE_UserMarshal64",
    "HPALETTE_UserSize",
    "HPALETTE_UserSize64",
    "HPALETTE_UserUnmarshal",
    "HPALETTE_UserUnmarshal64",
    "HWND_UserFree",
    "HWND_UserFree64",
    "HWND_UserMarshal",
    "HWND_UserMarshal64",
    "HWND_UserSize",
    "HWND_UserSize64",
    "HWND_UserUnmarshal",
    "HWND_UserUnmarshal64",
    "IMarshal",
    "IMarshal2",
    "IMarshalingStream",
    "LPSAFEARRAY_UserFree",
    "LPSAFEARRAY_UserFree64",
    "LPSAFEARRAY_UserMarshal",
    "LPSAFEARRAY_UserMarshal64",
    "LPSAFEARRAY_UserSize",
    "LPSAFEARRAY_UserSize64",
    "LPSAFEARRAY_UserUnmarshal",
    "LPSAFEARRAY_UserUnmarshal64",
    "SMEXF_HANDLER",
    "SMEXF_SERVER",
    "SNB_UserFree",
    "SNB_UserFree64",
    "SNB_UserMarshal",
    "SNB_UserMarshal64",
    "SNB_UserSize",
    "SNB_UserSize64",
    "SNB_UserUnmarshal",
    "SNB_UserUnmarshal64",
    "STDMSHLFLAGS",
    "STGMEDIUM_UserFree",
    "STGMEDIUM_UserFree64",
    "STGMEDIUM_UserMarshal",
    "STGMEDIUM_UserMarshal64",
    "STGMEDIUM_UserSize",
    "STGMEDIUM_UserSize64",
    "STGMEDIUM_UserUnmarshal",
    "STGMEDIUM_UserUnmarshal64",
    "VARIANT_UserFree",
    "VARIANT_UserFree64",
    "VARIANT_UserMarshal",
    "VARIANT_UserMarshal64",
    "VARIANT_UserSize",
    "VARIANT_UserSize64",
    "VARIANT_UserUnmarshal",
    "VARIANT_UserUnmarshal64",
]
