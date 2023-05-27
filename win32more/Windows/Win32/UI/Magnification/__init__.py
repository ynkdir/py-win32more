from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.UI.Magnification
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WC_MAGNIFIERA: String = 'Magnifier'
WC_MAGNIFIERW: String = 'Magnifier'
WC_MAGNIFIER: String = 'Magnifier'
MS_SHOWMAGNIFIEDCURSOR: Int32 = 1
MS_CLIPAROUNDCURSOR: Int32 = 2
MS_INVERTCOLORS: Int32 = 4
@winfunctype('MAGNIFICATION.dll')
def MagInitialize() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagUninitialize() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowSource(hwnd: win32more.Windows.Win32.Foundation.HWND, rect: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowSource(hwnd: win32more.Windows.Win32.Foundation.HWND, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowTransform(hwnd: win32more.Windows.Win32.Foundation.HWND, pTransform: POINTER(win32more.Windows.Win32.UI.Magnification.MAGTRANSFORM_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowTransform(hwnd: win32more.Windows.Win32.Foundation.HWND, pTransform: POINTER(win32more.Windows.Win32.UI.Magnification.MAGTRANSFORM_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowFilterList(hwnd: win32more.Windows.Win32.Foundation.HWND, dwFilterMode: win32more.Windows.Win32.UI.Magnification.MW_FILTERMODE, count: Int32, pHWND: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowFilterList(hwnd: win32more.Windows.Win32.Foundation.HWND, pdwFilterMode: POINTER(win32more.Windows.Win32.UI.Magnification.MW_FILTERMODE), count: Int32, pHWND: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> Int32: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetImageScalingCallback(hwnd: win32more.Windows.Win32.Foundation.HWND, callback: win32more.Windows.Win32.UI.Magnification.MagImageScalingCallback) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetImageScalingCallback(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.Magnification.MagImageScalingCallback: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetColorEffect(hwnd: win32more.Windows.Win32.Foundation.HWND, pEffect: POINTER(win32more.Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetColorEffect(hwnd: win32more.Windows.Win32.Foundation.HWND, pEffect: POINTER(win32more.Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenTransform(magLevel: Single, xOffset: Int32, yOffset: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenTransform(pMagLevel: POINTER(Single), pxOffset: POINTER(Int32), pyOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenColorEffect(pEffect: POINTER(win32more.Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenColorEffect(pEffect: POINTER(win32more.Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetInputTransform(fEnabled: win32more.Windows.Win32.Foundation.BOOL, pRectSource: POINTER(win32more.Windows.Win32.Foundation.RECT_head), pRectDest: POINTER(win32more.Windows.Win32.Foundation.RECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetInputTransform(pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), pRectSource: POINTER(win32more.Windows.Win32.Foundation.RECT_head), pRectDest: POINTER(win32more.Windows.Win32.Foundation.RECT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagShowSystemCursor(fShowCursor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
class MAGCOLOREFFECT(EasyCastStructure):
    transform: Single * 25
class MAGIMAGEHEADER(EasyCastStructure):
    width: UInt32
    height: UInt32
    format: Guid
    stride: UInt32
    offset: UInt32
    cbSize: UIntPtr
class MAGTRANSFORM(EasyCastStructure):
    v: Single * 9
MW_FILTERMODE = UInt32
MW_FILTERMODE_EXCLUDE: MW_FILTERMODE = 0
MW_FILTERMODE_INCLUDE: MW_FILTERMODE = 1
@winfunctype_pointer
def MagImageScalingCallback(hwnd: win32more.Windows.Win32.Foundation.HWND, srcdata: VoidPtr, srcheader: win32more.Windows.Win32.UI.Magnification.MAGIMAGEHEADER, destdata: VoidPtr, destheader: win32more.Windows.Win32.UI.Magnification.MAGIMAGEHEADER, unclipped: win32more.Windows.Win32.Foundation.RECT, clipped: win32more.Windows.Win32.Foundation.RECT, dirty: win32more.Windows.Win32.Graphics.Gdi.HRGN) -> win32more.Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'MAGCOLOREFFECT')
make_head(_module, 'MAGIMAGEHEADER')
make_head(_module, 'MAGTRANSFORM')
make_head(_module, 'MagImageScalingCallback')
