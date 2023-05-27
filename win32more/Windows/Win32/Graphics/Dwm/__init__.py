from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dwm
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def DwmDefWindowProc(hWnd: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('dwmapi.dll')
def DwmEnableBlurBehindWindow(hWnd: win32more.Windows.Win32.Foundation.HWND, pBlurBehind: POINTER(win32more.Windows.Win32.Graphics.Dwm.DWM_BLURBEHIND_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmEnableComposition(uCompositionAction: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmEnableMMCSS(fEnableMMCSS: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmExtendFrameIntoClientArea(hWnd: win32more.Windows.Win32.Foundation.HWND, pMarInset: POINTER(win32more.Windows.Win32.UI.Controls.MARGINS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetColorizationColor(pcrColorization: POINTER(UInt32), pfOpaqueBlend: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetCompositionTimingInfo(hwnd: win32more.Windows.Win32.Foundation.HWND, pTimingInfo: POINTER(win32more.Windows.Win32.Graphics.Dwm.DWM_TIMING_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetWindowAttribute(hwnd: win32more.Windows.Win32.Foundation.HWND, dwAttribute: UInt32, pvAttribute: VoidPtr, cbAttribute: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmIsCompositionEnabled(pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmModifyPreviousDxFrameDuration(hwnd: win32more.Windows.Win32.Foundation.HWND, cRefreshes: Int32, fRelative: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmQueryThumbnailSourceSize(hThumbnail: IntPtr, pSize: POINTER(win32more.Windows.Win32.Foundation.SIZE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmRegisterThumbnail(hwndDestination: win32more.Windows.Win32.Foundation.HWND, hwndSource: win32more.Windows.Win32.Foundation.HWND, phThumbnailId: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetDxFrameDuration(hwnd: win32more.Windows.Win32.Foundation.HWND, cRefreshes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetPresentParameters(hwnd: win32more.Windows.Win32.Foundation.HWND, pPresentParams: POINTER(win32more.Windows.Win32.Graphics.Dwm.DWM_PRESENT_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetWindowAttribute(hwnd: win32more.Windows.Win32.Foundation.HWND, dwAttribute: UInt32, pvAttribute: VoidPtr, cbAttribute: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmUnregisterThumbnail(hThumbnailId: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmUpdateThumbnailProperties(hThumbnailId: IntPtr, ptnProperties: POINTER(win32more.Windows.Win32.Graphics.Dwm.DWM_THUMBNAIL_PROPERTIES_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetIconicThumbnail(hwnd: win32more.Windows.Win32.Foundation.HWND, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, dwSITFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmSetIconicLivePreviewBitmap(hwnd: win32more.Windows.Win32.Foundation.HWND, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, pptClient: POINTER(win32more.Windows.Win32.Foundation.POINT_head), dwSITFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmInvalidateIconicBitmaps(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmAttachMilContent(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmDetachMilContent(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmFlush() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetGraphicsStreamTransformHint(uIndex: UInt32, pTransform: POINTER(win32more.Windows.Win32.Graphics.Dwm.MilMatrix3x2D_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetGraphicsStreamClient(uIndex: UInt32, pClientUuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetTransportAttributes(pfIsRemoting: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfIsConnected: POINTER(win32more.Windows.Win32.Foundation.BOOL), pDwGeneration: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmTransitionOwnedWindow(hwnd: win32more.Windows.Win32.Foundation.HWND, target: win32more.Windows.Win32.Graphics.Dwm.DWMTRANSITION_OWNEDWINDOW_TARGET) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmRenderGesture(gt: win32more.Windows.Win32.Graphics.Dwm.GESTURE_TYPE, cContacts: UInt32, pdwPointerID: POINTER(UInt32), pPoints: POINTER(win32more.Windows.Win32.Foundation.POINT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmTetherContact(dwPointerID: UInt32, fEnable: win32more.Windows.Win32.Foundation.BOOL, ptTether: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmShowContact(dwPointerID: UInt32, eShowContact: win32more.Windows.Win32.Graphics.Dwm.DWM_SHOWCONTACT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dwmapi.dll')
def DwmGetUnmetTabRequirements(appWindow: win32more.Windows.Win32.Foundation.HWND, value: POINTER(win32more.Windows.Win32.Graphics.Dwm.DWM_TAB_WINDOW_REQUIREMENTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
DWMWA_SYSTEMBACKDROP_TYPE: DWMWINDOWATTRIBUTE = 38
DWMWA_LAST: DWMWINDOWATTRIBUTE = 39
class DWM_BLURBEHIND(EasyCastStructure):
    dwFlags: UInt32
    fEnable: win32more.Windows.Win32.Foundation.BOOL
    hRgnBlur: win32more.Windows.Win32.Graphics.Gdi.HRGN
    fTransitionOnMaximized: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class DWM_PRESENT_PARAMETERS(EasyCastStructure):
    cbSize: UInt32
    fQueue: win32more.Windows.Win32.Foundation.BOOL
    cRefreshStart: UInt64
    cBuffer: UInt32
    fUseSourceRate: win32more.Windows.Win32.Foundation.BOOL
    rateSource: win32more.Windows.Win32.Graphics.Dwm.UNSIGNED_RATIO
    cRefreshesPerFrame: UInt32
    eSampling: win32more.Windows.Win32.Graphics.Dwm.DWM_SOURCE_FRAME_SAMPLING
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
DWM_SYSTEMBACKDROP_TYPE = Int32
DWMSBT_AUTO: DWM_SYSTEMBACKDROP_TYPE = 0
DWMSBT_NONE: DWM_SYSTEMBACKDROP_TYPE = 1
DWMSBT_MAINWINDOW: DWM_SYSTEMBACKDROP_TYPE = 2
DWMSBT_TRANSIENTWINDOW: DWM_SYSTEMBACKDROP_TYPE = 3
DWMSBT_TABBEDWINDOW: DWM_SYSTEMBACKDROP_TYPE = 4
DWM_TAB_WINDOW_REQUIREMENTS = Int32
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
class DWM_THUMBNAIL_PROPERTIES(EasyCastStructure):
    dwFlags: UInt32
    rcDestination: win32more.Windows.Win32.Foundation.RECT
    rcSource: win32more.Windows.Win32.Foundation.RECT
    opacity: Byte
    fVisible: win32more.Windows.Win32.Foundation.BOOL
    fSourceClientAreaOnly: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class DWM_TIMING_INFO(EasyCastStructure):
    cbSize: UInt32
    rateRefresh: win32more.Windows.Win32.Graphics.Dwm.UNSIGNED_RATIO
    qpcRefreshPeriod: UInt64
    rateCompose: win32more.Windows.Win32.Graphics.Dwm.UNSIGNED_RATIO
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
class MilMatrix3x2D(EasyCastStructure):
    S_11: Double
    S_12: Double
    S_21: Double
    S_22: Double
    DX: Double
    DY: Double
    _pack_ = 1
class UNSIGNED_RATIO(EasyCastStructure):
    uiNumerator: UInt32
    uiDenominator: UInt32
    _pack_ = 1
make_head(_module, 'DWM_BLURBEHIND')
make_head(_module, 'DWM_PRESENT_PARAMETERS')
make_head(_module, 'DWM_THUMBNAIL_PROPERTIES')
make_head(_module, 'DWM_TIMING_INFO')
make_head(_module, 'MilMatrix3x2D')
make_head(_module, 'UNSIGNED_RATIO')
