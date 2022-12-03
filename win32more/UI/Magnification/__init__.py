from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.UI.Magnification
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
WC_MAGNIFIERA = 'Magnifier'
WC_MAGNIFIERW = 'Magnifier'
WC_MAGNIFIER = 'Magnifier'
MS_SHOWMAGNIFIEDCURSOR = 1
MS_CLIPAROUNDCURSOR = 2
MS_INVERTCOLORS = 4
def _define_MagInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('MagInitialize', windll['MAGNIFICATION.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagUninitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('MagUninitialize', windll['MAGNIFICATION.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetWindowSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.RECT)(('MagSetWindowSource', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'rect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetWindowSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head))(('MagGetWindowSource', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pRect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetWindowTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.UI.Magnification.MAGTRANSFORM_head))(('MagSetWindowTransform', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pTransform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetWindowTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.UI.Magnification.MAGTRANSFORM_head))(('MagGetWindowTransform', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pTransform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetWindowFilterList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.Magnification.MW_FILTERMODE,Int32,POINTER(win32more.Foundation.HWND))(('MagSetWindowFilterList', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'dwFilterMode'),(1, 'count'),(1, 'pHWND'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetWindowFilterList():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,POINTER(win32more.UI.Magnification.MW_FILTERMODE),Int32,POINTER(win32more.Foundation.HWND))(('MagGetWindowFilterList', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pdwFilterMode'),(1, 'count'),(1, 'pHWND'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetImageScalingCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.Magnification.MagImageScalingCallback)(('MagSetImageScalingCallback', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetImageScalingCallback():
    try:
        return WINFUNCTYPE(win32more.UI.Magnification.MagImageScalingCallback,win32more.Foundation.HWND)(('MagGetImageScalingCallback', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetColorEffect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head))(('MagSetColorEffect', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetColorEffect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head))(('MagGetColorEffect', windll['MAGNIFICATION.dll']), ((1, 'hwnd'),(1, 'pEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetFullscreenTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Single,Int32,Int32)(('MagSetFullscreenTransform', windll['MAGNIFICATION.dll']), ((1, 'magLevel'),(1, 'xOffset'),(1, 'yOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetFullscreenTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Single),POINTER(Int32),POINTER(Int32))(('MagGetFullscreenTransform', windll['MAGNIFICATION.dll']), ((1, 'pMagLevel'),(1, 'pxOffset'),(1, 'pyOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetFullscreenColorEffect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head))(('MagSetFullscreenColorEffect', windll['MAGNIFICATION.dll']), ((1, 'pEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetFullscreenColorEffect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head))(('MagGetFullscreenColorEffect', windll['MAGNIFICATION.dll']), ((1, 'pEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagSetInputTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('MagSetInputTransform', windll['MAGNIFICATION.dll']), ((1, 'fEnabled'),(1, 'pRectSource'),(1, 'pRectDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagGetInputTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('MagGetInputTransform', windll['MAGNIFICATION.dll']), ((1, 'pfEnabled'),(1, 'pRectSource'),(1, 'pRectDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MagShowSystemCursor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('MagShowSystemCursor', windll['MAGNIFICATION.dll']), ((1, 'fShowCursor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MAGCOLOREFFECT_head():
    class MAGCOLOREFFECT(Structure):
        pass
    return MAGCOLOREFFECT
def _define_MAGCOLOREFFECT():
    MAGCOLOREFFECT = win32more.UI.Magnification.MAGCOLOREFFECT_head
    MAGCOLOREFFECT._fields_ = [
        ('transform', Single * 25),
    ]
    return MAGCOLOREFFECT
def _define_MAGIMAGEHEADER_head():
    class MAGIMAGEHEADER(Structure):
        pass
    return MAGIMAGEHEADER
def _define_MAGIMAGEHEADER():
    MAGIMAGEHEADER = win32more.UI.Magnification.MAGIMAGEHEADER_head
    MAGIMAGEHEADER._fields_ = [
        ('width', UInt32),
        ('height', UInt32),
        ('format', Guid),
        ('stride', UInt32),
        ('offset', UInt32),
        ('cbSize', UIntPtr),
    ]
    return MAGIMAGEHEADER
def _define_MagImageScalingCallback():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,c_void_p,win32more.UI.Magnification.MAGIMAGEHEADER,c_void_p,win32more.UI.Magnification.MAGIMAGEHEADER,win32more.Foundation.RECT,win32more.Foundation.RECT,win32more.Graphics.Gdi.HRGN)
def _define_MAGTRANSFORM_head():
    class MAGTRANSFORM(Structure):
        pass
    return MAGTRANSFORM
def _define_MAGTRANSFORM():
    MAGTRANSFORM = win32more.UI.Magnification.MAGTRANSFORM_head
    MAGTRANSFORM._fields_ = [
        ('v', Single * 9),
    ]
    return MAGTRANSFORM
MW_FILTERMODE = UInt32
MW_FILTERMODE_EXCLUDE = 0
MW_FILTERMODE_INCLUDE = 1
__all__ = [
    "MAGCOLOREFFECT",
    "MAGIMAGEHEADER",
    "MAGTRANSFORM",
    "MS_CLIPAROUNDCURSOR",
    "MS_INVERTCOLORS",
    "MS_SHOWMAGNIFIEDCURSOR",
    "MW_FILTERMODE",
    "MW_FILTERMODE_EXCLUDE",
    "MW_FILTERMODE_INCLUDE",
    "MagGetColorEffect",
    "MagGetFullscreenColorEffect",
    "MagGetFullscreenTransform",
    "MagGetImageScalingCallback",
    "MagGetInputTransform",
    "MagGetWindowFilterList",
    "MagGetWindowSource",
    "MagGetWindowTransform",
    "MagImageScalingCallback",
    "MagInitialize",
    "MagSetColorEffect",
    "MagSetFullscreenColorEffect",
    "MagSetFullscreenTransform",
    "MagSetImageScalingCallback",
    "MagSetInputTransform",
    "MagSetWindowFilterList",
    "MagSetWindowSource",
    "MagSetWindowTransform",
    "MagShowSystemCursor",
    "MagUninitialize",
    "WC_MAGNIFIER",
    "WC_MAGNIFIERA",
    "WC_MAGNIFIERW",
]
