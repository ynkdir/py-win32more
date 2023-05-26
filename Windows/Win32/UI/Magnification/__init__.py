from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.UI.Magnification
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
def MagInitialize() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagUninitialize() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowSource(hwnd: Windows.Win32.Foundation.HWND, rect: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowSource(hwnd: Windows.Win32.Foundation.HWND, pRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowTransform(hwnd: Windows.Win32.Foundation.HWND, pTransform: POINTER(Windows.Win32.UI.Magnification.MAGTRANSFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowTransform(hwnd: Windows.Win32.Foundation.HWND, pTransform: POINTER(Windows.Win32.UI.Magnification.MAGTRANSFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetWindowFilterList(hwnd: Windows.Win32.Foundation.HWND, dwFilterMode: Windows.Win32.UI.Magnification.MW_FILTERMODE, count: Int32, pHWND: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetWindowFilterList(hwnd: Windows.Win32.Foundation.HWND, pdwFilterMode: POINTER(Windows.Win32.UI.Magnification.MW_FILTERMODE), count: Int32, pHWND: POINTER(Windows.Win32.Foundation.HWND)) -> Int32: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetImageScalingCallback(hwnd: Windows.Win32.Foundation.HWND, callback: Windows.Win32.UI.Magnification.MagImageScalingCallback) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetImageScalingCallback(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.UI.Magnification.MagImageScalingCallback: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetColorEffect(hwnd: Windows.Win32.Foundation.HWND, pEffect: POINTER(Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetColorEffect(hwnd: Windows.Win32.Foundation.HWND, pEffect: POINTER(Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenTransform(magLevel: Single, xOffset: Int32, yOffset: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenTransform(pMagLevel: POINTER(Single), pxOffset: POINTER(Int32), pyOffset: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetFullscreenColorEffect(pEffect: POINTER(Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetFullscreenColorEffect(pEffect: POINTER(Windows.Win32.UI.Magnification.MAGCOLOREFFECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagSetInputTransform(fEnabled: Windows.Win32.Foundation.BOOL, pRectSource: POINTER(Windows.Win32.Foundation.RECT_head), pRectDest: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagGetInputTransform(pfEnabled: POINTER(Windows.Win32.Foundation.BOOL), pRectSource: POINTER(Windows.Win32.Foundation.RECT_head), pRectDest: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAGNIFICATION.dll')
def MagShowSystemCursor(fShowCursor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
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
def MagImageScalingCallback(hwnd: Windows.Win32.Foundation.HWND, srcdata: VoidPtr, srcheader: Windows.Win32.UI.Magnification.MAGIMAGEHEADER, destdata: VoidPtr, destheader: Windows.Win32.UI.Magnification.MAGIMAGEHEADER, unclipped: Windows.Win32.Foundation.RECT, clipped: Windows.Win32.Foundation.RECT, dirty: Windows.Win32.Graphics.Gdi.HRGN) -> Windows.Win32.Foundation.BOOL: ...
make_head(_module, 'MAGCOLOREFFECT')
make_head(_module, 'MAGIMAGEHEADER')
make_head(_module, 'MAGTRANSFORM')
make_head(_module, 'MagImageScalingCallback')
