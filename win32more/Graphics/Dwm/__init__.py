from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Dwm
import win32more.Graphics.Gdi
import win32more.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
DWM_BB_ENABLE: UInt32 = 1
DWM_BB_BLURREGION: UInt32 = 2
DWM_BB_TRANSITIONONMAXIMIZED: UInt32 = 4
DWMWA_COLOR_DEFAULT: UInt32 = 4294967295
DWMWA_COLOR_NONE: UInt32 = 4294967294
DWM_CLOAKED_APP: UInt32 = 1
DWM_CLOAKED_SHELL: UInt32 = 2
DWM_CLOAKED_INHERITED: UInt32 = 4
DWM_TNP_RECTDESTINATION: UInt32 = 1
DWM_TNP_RECTSOURCE: UInt32 = 2
DWM_TNP_OPACITY: UInt32 = 4
DWM_TNP_VISIBLE: UInt32 = 8
DWM_TNP_SOURCECLIENTAREAONLY: UInt32 = 16
DWM_FRAME_DURATION_DEFAULT: Int32 = -1
DWM_EC_DISABLECOMPOSITION: UInt32 = 0
DWM_EC_ENABLECOMPOSITION: UInt32 = 1
DWM_SIT_DISPLAYFRAME: UInt32 = 1
c_DwmMaxQueuedBuffers: UInt32 = 8
c_DwmMaxMonitors: UInt32 = 16
c_DwmMaxAdapters: UInt32 = 16
@winfunctype('dwmapi.dll')
def DwmDefWindowProc(hWnd: win32more.Foundation.HWND, msg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, plResult: POINTER(win32more.Foundation.LRESULT)) -> win32more.Foundation.BOOL: ...
@winfunctype('dwmapi.dll')
def DwmEnableBlurBehindWindow(hWnd: win32more.Foundation.HWND, pBlurBehind: POINTER(win32more.Graphics.Dwm.DWM_BLURBEHIND_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmEnableComposition(uCompositionAction: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmEnableMMCSS(fEnableMMCSS: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmExtendFrameIntoClientArea(hWnd: win32more.Foundation.HWND, pMarInset: POINTER(win32more.UI.Controls.MARGINS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetColorizationColor(pcrColorization: POINTER(UInt32), pfOpaqueBlend: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetCompositionTimingInfo(hwnd: win32more.Foundation.HWND, pTimingInfo: POINTER(win32more.Graphics.Dwm.DWM_TIMING_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetWindowAttribute(hwnd: win32more.Foundation.HWND, dwAttribute: win32more.Graphics.Dwm.DWMWINDOWATTRIBUTE, pvAttribute: c_void_p, cbAttribute: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmIsCompositionEnabled(pfEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmModifyPreviousDxFrameDuration(hwnd: win32more.Foundation.HWND, cRefreshes: Int32, fRelative: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmQueryThumbnailSourceSize(hThumbnail: IntPtr, pSize: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmRegisterThumbnail(hwndDestination: win32more.Foundation.HWND, hwndSource: win32more.Foundation.HWND, phThumbnailId: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetDxFrameDuration(hwnd: win32more.Foundation.HWND, cRefreshes: Int32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetPresentParameters(hwnd: win32more.Foundation.HWND, pPresentParams: POINTER(win32more.Graphics.Dwm.DWM_PRESENT_PARAMETERS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetWindowAttribute(hwnd: win32more.Foundation.HWND, dwAttribute: win32more.Graphics.Dwm.DWMWINDOWATTRIBUTE, pvAttribute: c_void_p, cbAttribute: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmUnregisterThumbnail(hThumbnailId: IntPtr) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmUpdateThumbnailProperties(hThumbnailId: IntPtr, ptnProperties: POINTER(win32more.Graphics.Dwm.DWM_THUMBNAIL_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetIconicThumbnail(hwnd: win32more.Foundation.HWND, hbmp: win32more.Graphics.Gdi.HBITMAP, dwSITFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetIconicLivePreviewBitmap(hwnd: win32more.Foundation.HWND, hbmp: win32more.Graphics.Gdi.HBITMAP, pptClient: POINTER(win32more.Foundation.POINT_head), dwSITFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmInvalidateIconicBitmaps(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmAttachMilContent(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmDetachMilContent(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmFlush() -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetGraphicsStreamTransformHint(uIndex: UInt32, pTransform: POINTER(win32more.Graphics.Dwm.MilMatrix3x2D_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetGraphicsStreamClient(uIndex: UInt32, pClientUuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetTransportAttributes(pfIsRemoting: POINTER(win32more.Foundation.BOOL), pfIsConnected: POINTER(win32more.Foundation.BOOL), pDwGeneration: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmTransitionOwnedWindow(hwnd: win32more.Foundation.HWND, target: win32more.Graphics.Dwm.DWMTRANSITION_OWNEDWINDOW_TARGET) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmRenderGesture(gt: win32more.Graphics.Dwm.GESTURE_TYPE, cContacts: UInt32, pdwPointerID: POINTER(UInt32), pPoints: POINTER(win32more.Foundation.POINT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmTetherContact(dwPointerID: UInt32, fEnable: win32more.Foundation.BOOL, ptTether: win32more.Foundation.POINT) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmShowContact(dwPointerID: UInt32, eShowContact: win32more.Graphics.Dwm.DWM_SHOWCONTACT) -> win32more.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetUnmetTabRequirements(appWindow: win32more.Foundation.HWND, value: POINTER(win32more.Graphics.Dwm.DWM_TAB_WINDOW_REQUIREMENTS)) -> win32more.Foundation.HRESULT: ...
DWMFLIP3DWINDOWPOLICY = Int32
DWMFLIP3D_DEFAULT: DWMFLIP3DWINDOWPOLICY = 0
DWMFLIP3D_EXCLUDEBELOW: DWMFLIP3DWINDOWPOLICY = 1
DWMFLIP3D_EXCLUDEABOVE: DWMFLIP3DWINDOWPOLICY = 2
DWMFLIP3D_LAST: DWMFLIP3DWINDOWPOLICY = 3
DWMNCRENDERINGPOLICY = Int32
DWMNCRP_USEWINDOWSTYLE: DWMNCRENDERINGPOLICY = 0
DWMNCRP_DISABLED: DWMNCRENDERINGPOLICY = 1
DWMNCRP_ENABLED: DWMNCRENDERINGPOLICY = 2
DWMNCRP_LAST: DWMNCRENDERINGPOLICY = 3
DWMTRANSITION_OWNEDWINDOW_TARGET = Int32
DWMTRANSITION_OWNEDWINDOW_NULL: DWMTRANSITION_OWNEDWINDOW_TARGET = -1
DWMTRANSITION_OWNEDWINDOW_REPOSITION: DWMTRANSITION_OWNEDWINDOW_TARGET = 0
DWMWINDOWATTRIBUTE = Int32
DWMWA_NCRENDERING_ENABLED: DWMWINDOWATTRIBUTE = 1
DWMWA_NCRENDERING_POLICY: DWMWINDOWATTRIBUTE = 2
DWMWA_TRANSITIONS_FORCEDISABLED: DWMWINDOWATTRIBUTE = 3
DWMWA_ALLOW_NCPAINT: DWMWINDOWATTRIBUTE = 4
DWMWA_CAPTION_BUTTON_BOUNDS: DWMWINDOWATTRIBUTE = 5
DWMWA_NONCLIENT_RTL_LAYOUT: DWMWINDOWATTRIBUTE = 6
DWMWA_FORCE_ICONIC_REPRESENTATION: DWMWINDOWATTRIBUTE = 7
DWMWA_FLIP3D_POLICY: DWMWINDOWATTRIBUTE = 8
DWMWA_EXTENDED_FRAME_BOUNDS: DWMWINDOWATTRIBUTE = 9
DWMWA_HAS_ICONIC_BITMAP: DWMWINDOWATTRIBUTE = 10
DWMWA_DISALLOW_PEEK: DWMWINDOWATTRIBUTE = 11
DWMWA_EXCLUDED_FROM_PEEK: DWMWINDOWATTRIBUTE = 12
DWMWA_CLOAK: DWMWINDOWATTRIBUTE = 13
DWMWA_CLOAKED: DWMWINDOWATTRIBUTE = 14
DWMWA_FREEZE_REPRESENTATION: DWMWINDOWATTRIBUTE = 15
DWMWA_PASSIVE_UPDATE_MODE: DWMWINDOWATTRIBUTE = 16
DWMWA_USE_HOSTBACKDROPBRUSH: DWMWINDOWATTRIBUTE = 17
DWMWA_USE_IMMERSIVE_DARK_MODE: DWMWINDOWATTRIBUTE = 20
DWMWA_WINDOW_CORNER_PREFERENCE: DWMWINDOWATTRIBUTE = 33
DWMWA_BORDER_COLOR: DWMWINDOWATTRIBUTE = 34
DWMWA_CAPTION_COLOR: DWMWINDOWATTRIBUTE = 35
DWMWA_TEXT_COLOR: DWMWINDOWATTRIBUTE = 36
DWMWA_VISIBLE_FRAME_BORDER_THICKNESS: DWMWINDOWATTRIBUTE = 37
DWMWA_LAST: DWMWINDOWATTRIBUTE = 38
class DWM_BLURBEHIND(Structure):
    dwFlags: UInt32
    fEnable: win32more.Foundation.BOOL
    hRgnBlur: win32more.Graphics.Gdi.HRGN
    fTransitionOnMaximized: win32more.Foundation.BOOL
    _pack_ = 1
class DWM_PRESENT_PARAMETERS(Structure):
    cbSize: UInt32
    fQueue: win32more.Foundation.BOOL
    cRefreshStart: UInt64
    cBuffer: UInt32
    fUseSourceRate: win32more.Foundation.BOOL
    rateSource: win32more.Graphics.Dwm.UNSIGNED_RATIO
    cRefreshesPerFrame: UInt32
    eSampling: win32more.Graphics.Dwm.DWM_SOURCE_FRAME_SAMPLING
    _pack_ = 1
DWM_SHOWCONTACT = UInt32
DWMSC_DOWN: DWM_SHOWCONTACT = 1
DWMSC_UP: DWM_SHOWCONTACT = 2
DWMSC_DRAG: DWM_SHOWCONTACT = 4
DWMSC_HOLD: DWM_SHOWCONTACT = 8
DWMSC_PENBARREL: DWM_SHOWCONTACT = 16
DWMSC_NONE: DWM_SHOWCONTACT = 0
DWMSC_ALL: DWM_SHOWCONTACT = 4294967295
DWM_SOURCE_FRAME_SAMPLING = Int32
DWM_SOURCE_FRAME_SAMPLING_POINT: DWM_SOURCE_FRAME_SAMPLING = 0
DWM_SOURCE_FRAME_SAMPLING_COVERAGE: DWM_SOURCE_FRAME_SAMPLING = 1
DWM_SOURCE_FRAME_SAMPLING_LAST: DWM_SOURCE_FRAME_SAMPLING = 2
DWM_TAB_WINDOW_REQUIREMENTS = UInt32
DWMTWR_NONE: DWM_TAB_WINDOW_REQUIREMENTS = 0
DWMTWR_IMPLEMENTED_BY_SYSTEM: DWM_TAB_WINDOW_REQUIREMENTS = 1
DWMTWR_WINDOW_RELATIONSHIP: DWM_TAB_WINDOW_REQUIREMENTS = 2
DWMTWR_WINDOW_STYLES: DWM_TAB_WINDOW_REQUIREMENTS = 4
DWMTWR_WINDOW_REGION: DWM_TAB_WINDOW_REQUIREMENTS = 8
DWMTWR_WINDOW_DWM_ATTRIBUTES: DWM_TAB_WINDOW_REQUIREMENTS = 16
DWMTWR_WINDOW_MARGINS: DWM_TAB_WINDOW_REQUIREMENTS = 32
DWMTWR_TABBING_ENABLED: DWM_TAB_WINDOW_REQUIREMENTS = 64
DWMTWR_USER_POLICY: DWM_TAB_WINDOW_REQUIREMENTS = 128
DWMTWR_GROUP_POLICY: DWM_TAB_WINDOW_REQUIREMENTS = 256
DWMTWR_APP_COMPAT: DWM_TAB_WINDOW_REQUIREMENTS = 512
class DWM_THUMBNAIL_PROPERTIES(Structure):
    dwFlags: UInt32
    rcDestination: win32more.Foundation.RECT
    rcSource: win32more.Foundation.RECT
    opacity: Byte
    fVisible: win32more.Foundation.BOOL
    fSourceClientAreaOnly: win32more.Foundation.BOOL
    _pack_ = 1
class DWM_TIMING_INFO(Structure):
    cbSize: UInt32
    rateRefresh: win32more.Graphics.Dwm.UNSIGNED_RATIO
    qpcRefreshPeriod: UInt64
    rateCompose: win32more.Graphics.Dwm.UNSIGNED_RATIO
    qpcVBlank: UInt64
    cRefresh: UInt64
    cDXRefresh: UInt32
    qpcCompose: UInt64
    cFrame: UInt64
    cDXPresent: UInt32
    cRefreshFrame: UInt64
    cFrameSubmitted: UInt64
    cDXPresentSubmitted: UInt32
    cFrameConfirmed: UInt64
    cDXPresentConfirmed: UInt32
    cRefreshConfirmed: UInt64
    cDXRefreshConfirmed: UInt32
    cFramesLate: UInt64
    cFramesOutstanding: UInt32
    cFrameDisplayed: UInt64
    qpcFrameDisplayed: UInt64
    cRefreshFrameDisplayed: UInt64
    cFrameComplete: UInt64
    qpcFrameComplete: UInt64
    cFramePending: UInt64
    qpcFramePending: UInt64
    cFramesDisplayed: UInt64
    cFramesComplete: UInt64
    cFramesPending: UInt64
    cFramesAvailable: UInt64
    cFramesDropped: UInt64
    cFramesMissed: UInt64
    cRefreshNextDisplayed: UInt64
    cRefreshNextPresented: UInt64
    cRefreshesDisplayed: UInt64
    cRefreshesPresented: UInt64
    cRefreshStarted: UInt64
    cPixelsReceived: UInt64
    cPixelsDrawn: UInt64
    cBuffersEmpty: UInt64
    _pack_ = 1
DWM_WINDOW_CORNER_PREFERENCE = Int32
DWMWCP_DEFAULT: DWM_WINDOW_CORNER_PREFERENCE = 0
DWMWCP_DONOTROUND: DWM_WINDOW_CORNER_PREFERENCE = 1
DWMWCP_ROUND: DWM_WINDOW_CORNER_PREFERENCE = 2
DWMWCP_ROUNDSMALL: DWM_WINDOW_CORNER_PREFERENCE = 3
GESTURE_TYPE = Int32
GT_PEN_TAP: GESTURE_TYPE = 0
GT_PEN_DOUBLETAP: GESTURE_TYPE = 1
GT_PEN_RIGHTTAP: GESTURE_TYPE = 2
GT_PEN_PRESSANDHOLD: GESTURE_TYPE = 3
GT_PEN_PRESSANDHOLDABORT: GESTURE_TYPE = 4
GT_TOUCH_TAP: GESTURE_TYPE = 5
GT_TOUCH_DOUBLETAP: GESTURE_TYPE = 6
GT_TOUCH_RIGHTTAP: GESTURE_TYPE = 7
GT_TOUCH_PRESSANDHOLD: GESTURE_TYPE = 8
GT_TOUCH_PRESSANDHOLDABORT: GESTURE_TYPE = 9
GT_TOUCH_PRESSANDTAP: GESTURE_TYPE = 10
class MilMatrix3x2D(Structure):
    S_11: Double
    S_12: Double
    S_21: Double
    S_22: Double
    DX: Double
    DY: Double
    _pack_ = 1
class UNSIGNED_RATIO(Structure):
    uiNumerator: UInt32
    uiDenominator: UInt32
    _pack_ = 1
make_head(_module, 'DWM_BLURBEHIND')
make_head(_module, 'DWM_PRESENT_PARAMETERS')
make_head(_module, 'DWM_THUMBNAIL_PROPERTIES')
make_head(_module, 'DWM_TIMING_INFO')
make_head(_module, 'MilMatrix3x2D')
make_head(_module, 'UNSIGNED_RATIO')
__all__ = [
    "DWMFLIP3DWINDOWPOLICY",
    "DWMFLIP3D_DEFAULT",
    "DWMFLIP3D_EXCLUDEABOVE",
    "DWMFLIP3D_EXCLUDEBELOW",
    "DWMFLIP3D_LAST",
    "DWMNCRENDERINGPOLICY",
    "DWMNCRP_DISABLED",
    "DWMNCRP_ENABLED",
    "DWMNCRP_LAST",
    "DWMNCRP_USEWINDOWSTYLE",
    "DWMSC_ALL",
    "DWMSC_DOWN",
    "DWMSC_DRAG",
    "DWMSC_HOLD",
    "DWMSC_NONE",
    "DWMSC_PENBARREL",
    "DWMSC_UP",
    "DWMTRANSITION_OWNEDWINDOW_NULL",
    "DWMTRANSITION_OWNEDWINDOW_REPOSITION",
    "DWMTRANSITION_OWNEDWINDOW_TARGET",
    "DWMTWR_APP_COMPAT",
    "DWMTWR_GROUP_POLICY",
    "DWMTWR_IMPLEMENTED_BY_SYSTEM",
    "DWMTWR_NONE",
    "DWMTWR_TABBING_ENABLED",
    "DWMTWR_USER_POLICY",
    "DWMTWR_WINDOW_DWM_ATTRIBUTES",
    "DWMTWR_WINDOW_MARGINS",
    "DWMTWR_WINDOW_REGION",
    "DWMTWR_WINDOW_RELATIONSHIP",
    "DWMTWR_WINDOW_STYLES",
    "DWMWA_ALLOW_NCPAINT",
    "DWMWA_BORDER_COLOR",
    "DWMWA_CAPTION_BUTTON_BOUNDS",
    "DWMWA_CAPTION_COLOR",
    "DWMWA_CLOAK",
    "DWMWA_CLOAKED",
    "DWMWA_COLOR_DEFAULT",
    "DWMWA_COLOR_NONE",
    "DWMWA_DISALLOW_PEEK",
    "DWMWA_EXCLUDED_FROM_PEEK",
    "DWMWA_EXTENDED_FRAME_BOUNDS",
    "DWMWA_FLIP3D_POLICY",
    "DWMWA_FORCE_ICONIC_REPRESENTATION",
    "DWMWA_FREEZE_REPRESENTATION",
    "DWMWA_HAS_ICONIC_BITMAP",
    "DWMWA_LAST",
    "DWMWA_NCRENDERING_ENABLED",
    "DWMWA_NCRENDERING_POLICY",
    "DWMWA_NONCLIENT_RTL_LAYOUT",
    "DWMWA_PASSIVE_UPDATE_MODE",
    "DWMWA_TEXT_COLOR",
    "DWMWA_TRANSITIONS_FORCEDISABLED",
    "DWMWA_USE_HOSTBACKDROPBRUSH",
    "DWMWA_USE_IMMERSIVE_DARK_MODE",
    "DWMWA_VISIBLE_FRAME_BORDER_THICKNESS",
    "DWMWA_WINDOW_CORNER_PREFERENCE",
    "DWMWCP_DEFAULT",
    "DWMWCP_DONOTROUND",
    "DWMWCP_ROUND",
    "DWMWCP_ROUNDSMALL",
    "DWMWINDOWATTRIBUTE",
    "DWM_BB_BLURREGION",
    "DWM_BB_ENABLE",
    "DWM_BB_TRANSITIONONMAXIMIZED",
    "DWM_BLURBEHIND",
    "DWM_CLOAKED_APP",
    "DWM_CLOAKED_INHERITED",
    "DWM_CLOAKED_SHELL",
    "DWM_EC_DISABLECOMPOSITION",
    "DWM_EC_ENABLECOMPOSITION",
    "DWM_FRAME_DURATION_DEFAULT",
    "DWM_PRESENT_PARAMETERS",
    "DWM_SHOWCONTACT",
    "DWM_SIT_DISPLAYFRAME",
    "DWM_SOURCE_FRAME_SAMPLING",
    "DWM_SOURCE_FRAME_SAMPLING_COVERAGE",
    "DWM_SOURCE_FRAME_SAMPLING_LAST",
    "DWM_SOURCE_FRAME_SAMPLING_POINT",
    "DWM_TAB_WINDOW_REQUIREMENTS",
    "DWM_THUMBNAIL_PROPERTIES",
    "DWM_TIMING_INFO",
    "DWM_TNP_OPACITY",
    "DWM_TNP_RECTDESTINATION",
    "DWM_TNP_RECTSOURCE",
    "DWM_TNP_SOURCECLIENTAREAONLY",
    "DWM_TNP_VISIBLE",
    "DWM_WINDOW_CORNER_PREFERENCE",
    "DwmAttachMilContent",
    "DwmDefWindowProc",
    "DwmDetachMilContent",
    "DwmEnableBlurBehindWindow",
    "DwmEnableComposition",
    "DwmEnableMMCSS",
    "DwmExtendFrameIntoClientArea",
    "DwmFlush",
    "DwmGetColorizationColor",
    "DwmGetCompositionTimingInfo",
    "DwmGetGraphicsStreamClient",
    "DwmGetGraphicsStreamTransformHint",
    "DwmGetTransportAttributes",
    "DwmGetUnmetTabRequirements",
    "DwmGetWindowAttribute",
    "DwmInvalidateIconicBitmaps",
    "DwmIsCompositionEnabled",
    "DwmModifyPreviousDxFrameDuration",
    "DwmQueryThumbnailSourceSize",
    "DwmRegisterThumbnail",
    "DwmRenderGesture",
    "DwmSetDxFrameDuration",
    "DwmSetIconicLivePreviewBitmap",
    "DwmSetIconicThumbnail",
    "DwmSetPresentParameters",
    "DwmSetWindowAttribute",
    "DwmShowContact",
    "DwmTetherContact",
    "DwmTransitionOwnedWindow",
    "DwmUnregisterThumbnail",
    "DwmUpdateThumbnailProperties",
    "GESTURE_TYPE",
    "GT_PEN_DOUBLETAP",
    "GT_PEN_PRESSANDHOLD",
    "GT_PEN_PRESSANDHOLDABORT",
    "GT_PEN_RIGHTTAP",
    "GT_PEN_TAP",
    "GT_TOUCH_DOUBLETAP",
    "GT_TOUCH_PRESSANDHOLD",
    "GT_TOUCH_PRESSANDHOLDABORT",
    "GT_TOUCH_PRESSANDTAP",
    "GT_TOUCH_RIGHTTAP",
    "GT_TOUCH_TAP",
    "MilMatrix3x2D",
    "UNSIGNED_RATIO",
    "c_DwmMaxAdapters",
    "c_DwmMaxMonitors",
    "c_DwmMaxQueuedBuffers",
]
_arch_optional = [
]
