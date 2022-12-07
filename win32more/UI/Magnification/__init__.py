from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.UI.Magnification
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
WC_MAGNIFIERA: String = 'Magnifier'
WC_MAGNIFIERW: String = 'Magnifier'
WC_MAGNIFIER: String = 'Magnifier'
MS_SHOWMAGNIFIEDCURSOR: Int32 = 1
MS_CLIPAROUNDCURSOR: Int32 = 2
MS_INVERTCOLORS: Int32 = 4
@winfunctype('MAGNIFICATION.dll')
def MagInitialize() -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagUninitialize() -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowSource(hwnd: win32more.Foundation.HWND, rect: win32more.Foundation.RECT) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowSource(hwnd: win32more.Foundation.HWND, pRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowTransform(hwnd: win32more.Foundation.HWND, pTransform: POINTER(win32more.UI.Magnification.MAGTRANSFORM_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowTransform(hwnd: win32more.Foundation.HWND, pTransform: POINTER(win32more.UI.Magnification.MAGTRANSFORM_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowFilterList(hwnd: win32more.Foundation.HWND, dwFilterMode: win32more.UI.Magnification.MW_FILTERMODE, count: Int32, pHWND: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowFilterList(hwnd: win32more.Foundation.HWND, pdwFilterMode: POINTER(win32more.UI.Magnification.MW_FILTERMODE), count: Int32, pHWND: POINTER(win32more.Foundation.HWND)) -> Int32: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetImageScalingCallback(hwnd: win32more.Foundation.HWND, callback: win32more.UI.Magnification.MagImageScalingCallback) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetImageScalingCallback(hwnd: win32more.Foundation.HWND) -> win32more.UI.Magnification.MagImageScalingCallback: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetColorEffect(hwnd: win32more.Foundation.HWND, pEffect: POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetColorEffect(hwnd: win32more.Foundation.HWND, pEffect: POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenTransform(magLevel: Single, xOffset: Int32, yOffset: Int32) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenTransform(pMagLevel: POINTER(Single), pxOffset: POINTER(Int32), pyOffset: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenColorEffect(pEffect: POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenColorEffect(pEffect: POINTER(win32more.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetInputTransform(fEnabled: win32more.Foundation.BOOL, pRectSource: POINTER(win32more.Foundation.RECT_head), pRectDest: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetInputTransform(pfEnabled: POINTER(win32more.Foundation.BOOL), pRectSource: POINTER(win32more.Foundation.RECT_head), pRectDest: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagShowSystemCursor(fShowCursor: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
class MAGCOLOREFFECT(Structure):
    transform: Single * 25
class MAGIMAGEHEADER(Structure):
    width: UInt32
    height: UInt32
    format: Guid
    stride: UInt32
    offset: UInt32
    cbSize: UIntPtr
@winfunctype_pointer
def MagImageScalingCallback(hwnd: win32more.Foundation.HWND, srcdata: c_void_p, srcheader: win32more.UI.Magnification.MAGIMAGEHEADER, destdata: c_void_p, destheader: win32more.UI.Magnification.MAGIMAGEHEADER, unclipped: win32more.Foundation.RECT, clipped: win32more.Foundation.RECT, dirty: win32more.Graphics.Gdi.HRGN) -> win32more.Foundation.BOOL: ...
class MAGTRANSFORM(Structure):
    v: Single * 9
MW_FILTERMODE = UInt32
MW_FILTERMODE_EXCLUDE: MW_FILTERMODE = 0
MW_FILTERMODE_INCLUDE: MW_FILTERMODE = 1
make_head(_module, 'MAGCOLOREFFECT')
make_head(_module, 'MAGIMAGEHEADER')
make_head(_module, 'MagImageScalingCallback')
make_head(_module, 'MAGTRANSFORM')
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
