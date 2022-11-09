from win32more.base import *
import win32more.Foundation
import win32more.Graphics.Dwm
import win32more.Graphics.Gdi
import win32more.UI.Controls

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
DWM_BB_ENABLE = 1
DWM_BB_BLURREGION = 2
DWM_BB_TRANSITIONONMAXIMIZED = 4
DWMWA_COLOR_DEFAULT = 4294967295
DWMWA_COLOR_NONE = 4294967294
DWM_CLOAKED_APP = 1
DWM_CLOAKED_SHELL = 2
DWM_CLOAKED_INHERITED = 4
DWM_TNP_RECTDESTINATION = 1
DWM_TNP_RECTSOURCE = 2
DWM_TNP_OPACITY = 4
DWM_TNP_VISIBLE = 8
DWM_TNP_SOURCECLIENTAREAONLY = 16
DWM_FRAME_DURATION_DEFAULT = -1
DWM_EC_DISABLECOMPOSITION = 0
DWM_EC_ENABLECOMPOSITION = 1
DWM_SIT_DISPLAYFRAME = 1
c_DwmMaxQueuedBuffers = 8
c_DwmMaxMonitors = 16
c_DwmMaxAdapters = 16
def _define_DWM_BLURBEHIND_head():
    class DWM_BLURBEHIND(Structure):
        pass
    return DWM_BLURBEHIND
def _define_DWM_BLURBEHIND():
    DWM_BLURBEHIND = win32more.Graphics.Dwm.DWM_BLURBEHIND_head
    DWM_BLURBEHIND._pack_ = 1
    DWM_BLURBEHIND._fields_ = [
        ("dwFlags", UInt32),
        ("fEnable", win32more.Foundation.BOOL),
        ("hRgnBlur", win32more.Graphics.Gdi.HRGN),
        ("fTransitionOnMaximized", win32more.Foundation.BOOL),
    ]
    return DWM_BLURBEHIND
DWMWINDOWATTRIBUTE = Int32
DWMWA_NCRENDERING_ENABLED = 1
DWMWA_NCRENDERING_POLICY = 2
DWMWA_TRANSITIONS_FORCEDISABLED = 3
DWMWA_ALLOW_NCPAINT = 4
DWMWA_CAPTION_BUTTON_BOUNDS = 5
DWMWA_NONCLIENT_RTL_LAYOUT = 6
DWMWA_FORCE_ICONIC_REPRESENTATION = 7
DWMWA_FLIP3D_POLICY = 8
DWMWA_EXTENDED_FRAME_BOUNDS = 9
DWMWA_HAS_ICONIC_BITMAP = 10
DWMWA_DISALLOW_PEEK = 11
DWMWA_EXCLUDED_FROM_PEEK = 12
DWMWA_CLOAK = 13
DWMWA_CLOAKED = 14
DWMWA_FREEZE_REPRESENTATION = 15
DWMWA_PASSIVE_UPDATE_MODE = 16
DWMWA_USE_HOSTBACKDROPBRUSH = 17
DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWA_BORDER_COLOR = 34
DWMWA_CAPTION_COLOR = 35
DWMWA_TEXT_COLOR = 36
DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 37
DWMWA_LAST = 38
DWM_WINDOW_CORNER_PREFERENCE = Int32
DWMWCP_DEFAULT = 0
DWMWCP_DONOTROUND = 1
DWMWCP_ROUND = 2
DWMWCP_ROUNDSMALL = 3
DWMNCRENDERINGPOLICY = Int32
DWMNCRP_USEWINDOWSTYLE = 0
DWMNCRP_DISABLED = 1
DWMNCRP_ENABLED = 2
DWMNCRP_LAST = 3
DWMFLIP3DWINDOWPOLICY = Int32
DWMFLIP3D_DEFAULT = 0
DWMFLIP3D_EXCLUDEBELOW = 1
DWMFLIP3D_EXCLUDEABOVE = 2
DWMFLIP3D_LAST = 3
def _define_DWM_THUMBNAIL_PROPERTIES_head():
    class DWM_THUMBNAIL_PROPERTIES(Structure):
        pass
    return DWM_THUMBNAIL_PROPERTIES
def _define_DWM_THUMBNAIL_PROPERTIES():
    DWM_THUMBNAIL_PROPERTIES = win32more.Graphics.Dwm.DWM_THUMBNAIL_PROPERTIES_head
    DWM_THUMBNAIL_PROPERTIES._pack_ = 1
    DWM_THUMBNAIL_PROPERTIES._fields_ = [
        ("dwFlags", UInt32),
        ("rcDestination", win32more.Foundation.RECT),
        ("rcSource", win32more.Foundation.RECT),
        ("opacity", Byte),
        ("fVisible", win32more.Foundation.BOOL),
        ("fSourceClientAreaOnly", win32more.Foundation.BOOL),
    ]
    return DWM_THUMBNAIL_PROPERTIES
def _define_UNSIGNED_RATIO_head():
    class UNSIGNED_RATIO(Structure):
        pass
    return UNSIGNED_RATIO
def _define_UNSIGNED_RATIO():
    UNSIGNED_RATIO = win32more.Graphics.Dwm.UNSIGNED_RATIO_head
    UNSIGNED_RATIO._pack_ = 1
    UNSIGNED_RATIO._fields_ = [
        ("uiNumerator", UInt32),
        ("uiDenominator", UInt32),
    ]
    return UNSIGNED_RATIO
def _define_DWM_TIMING_INFO_head():
    class DWM_TIMING_INFO(Structure):
        pass
    return DWM_TIMING_INFO
def _define_DWM_TIMING_INFO():
    DWM_TIMING_INFO = win32more.Graphics.Dwm.DWM_TIMING_INFO_head
    DWM_TIMING_INFO._pack_ = 1
    DWM_TIMING_INFO._fields_ = [
        ("cbSize", UInt32),
        ("rateRefresh", win32more.Graphics.Dwm.UNSIGNED_RATIO),
        ("qpcRefreshPeriod", UInt64),
        ("rateCompose", win32more.Graphics.Dwm.UNSIGNED_RATIO),
        ("qpcVBlank", UInt64),
        ("cRefresh", UInt64),
        ("cDXRefresh", UInt32),
        ("qpcCompose", UInt64),
        ("cFrame", UInt64),
        ("cDXPresent", UInt32),
        ("cRefreshFrame", UInt64),
        ("cFrameSubmitted", UInt64),
        ("cDXPresentSubmitted", UInt32),
        ("cFrameConfirmed", UInt64),
        ("cDXPresentConfirmed", UInt32),
        ("cRefreshConfirmed", UInt64),
        ("cDXRefreshConfirmed", UInt32),
        ("cFramesLate", UInt64),
        ("cFramesOutstanding", UInt32),
        ("cFrameDisplayed", UInt64),
        ("qpcFrameDisplayed", UInt64),
        ("cRefreshFrameDisplayed", UInt64),
        ("cFrameComplete", UInt64),
        ("qpcFrameComplete", UInt64),
        ("cFramePending", UInt64),
        ("qpcFramePending", UInt64),
        ("cFramesDisplayed", UInt64),
        ("cFramesComplete", UInt64),
        ("cFramesPending", UInt64),
        ("cFramesAvailable", UInt64),
        ("cFramesDropped", UInt64),
        ("cFramesMissed", UInt64),
        ("cRefreshNextDisplayed", UInt64),
        ("cRefreshNextPresented", UInt64),
        ("cRefreshesDisplayed", UInt64),
        ("cRefreshesPresented", UInt64),
        ("cRefreshStarted", UInt64),
        ("cPixelsReceived", UInt64),
        ("cPixelsDrawn", UInt64),
        ("cBuffersEmpty", UInt64),
    ]
    return DWM_TIMING_INFO
DWM_SOURCE_FRAME_SAMPLING = Int32
DWM_SOURCE_FRAME_SAMPLING_POINT = 0
DWM_SOURCE_FRAME_SAMPLING_COVERAGE = 1
DWM_SOURCE_FRAME_SAMPLING_LAST = 2
def _define_DWM_PRESENT_PARAMETERS_head():
    class DWM_PRESENT_PARAMETERS(Structure):
        pass
    return DWM_PRESENT_PARAMETERS
def _define_DWM_PRESENT_PARAMETERS():
    DWM_PRESENT_PARAMETERS = win32more.Graphics.Dwm.DWM_PRESENT_PARAMETERS_head
    DWM_PRESENT_PARAMETERS._pack_ = 1
    DWM_PRESENT_PARAMETERS._fields_ = [
        ("cbSize", UInt32),
        ("fQueue", win32more.Foundation.BOOL),
        ("cRefreshStart", UInt64),
        ("cBuffer", UInt32),
        ("fUseSourceRate", win32more.Foundation.BOOL),
        ("rateSource", win32more.Graphics.Dwm.UNSIGNED_RATIO),
        ("cRefreshesPerFrame", UInt32),
        ("eSampling", win32more.Graphics.Dwm.DWM_SOURCE_FRAME_SAMPLING),
    ]
    return DWM_PRESENT_PARAMETERS
def _define_MilMatrix3x2D_head():
    class MilMatrix3x2D(Structure):
        pass
    return MilMatrix3x2D
def _define_MilMatrix3x2D():
    MilMatrix3x2D = win32more.Graphics.Dwm.MilMatrix3x2D_head
    MilMatrix3x2D._pack_ = 1
    MilMatrix3x2D._fields_ = [
        ("S_11", Double),
        ("S_12", Double),
        ("S_21", Double),
        ("S_22", Double),
        ("DX", Double),
        ("DY", Double),
    ]
    return MilMatrix3x2D
DWMTRANSITION_OWNEDWINDOW_TARGET = Int32
DWMTRANSITION_OWNEDWINDOW_NULL = -1
DWMTRANSITION_OWNEDWINDOW_REPOSITION = 0
GESTURE_TYPE = Int32
GT_PEN_TAP = 0
GT_PEN_DOUBLETAP = 1
GT_PEN_RIGHTTAP = 2
GT_PEN_PRESSANDHOLD = 3
GT_PEN_PRESSANDHOLDABORT = 4
GT_TOUCH_TAP = 5
GT_TOUCH_DOUBLETAP = 6
GT_TOUCH_RIGHTTAP = 7
GT_TOUCH_PRESSANDHOLD = 8
GT_TOUCH_PRESSANDHOLDABORT = 9
GT_TOUCH_PRESSANDTAP = 10
DWM_SHOWCONTACT = UInt32
DWMSC_DOWN = 1
DWMSC_UP = 2
DWMSC_DRAG = 4
DWMSC_HOLD = 8
DWMSC_PENBARREL = 16
DWMSC_NONE = 0
DWMSC_ALL = 4294967295
DWM_TAB_WINDOW_REQUIREMENTS = UInt32
DWMTWR_NONE = 0
DWMTWR_IMPLEMENTED_BY_SYSTEM = 1
DWMTWR_WINDOW_RELATIONSHIP = 2
DWMTWR_WINDOW_STYLES = 4
DWMTWR_WINDOW_REGION = 8
DWMTWR_WINDOW_DWM_ATTRIBUTES = 16
DWMTWR_WINDOW_MARGINS = 32
DWMTWR_TABBING_ENABLED = 64
DWMTWR_USER_POLICY = 128
DWMTWR_GROUP_POLICY = 256
DWMTWR_APP_COMPAT = 512
def _define_DwmDefWindowProc():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(("DwmDefWindowProc", windll["dwmapi"]), ((1, 'hWnd'),(1, 'msg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmEnableBlurBehindWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Graphics.Dwm.DWM_BLURBEHIND_head), use_last_error=False)(("DwmEnableBlurBehindWindow", windll["dwmapi"]), ((1, 'hWnd'),(1, 'pBlurBehind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmEnableComposition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("DwmEnableComposition", windll["dwmapi"]), ((1, 'uCompositionAction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmEnableMMCSS():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(("DwmEnableMMCSS", windll["dwmapi"]), ((1, 'fEnableMMCSS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmExtendFrameIntoClientArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Controls.MARGINS_head), use_last_error=False)(("DwmExtendFrameIntoClientArea", windll["dwmapi"]), ((1, 'hWnd'),(1, 'pMarInset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetColorizationColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DwmGetColorizationColor", windll["dwmapi"]), ((1, 'pcrColorization'),(1, 'pfOpaqueBlend'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetCompositionTimingInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Graphics.Dwm.DWM_TIMING_INFO_head), use_last_error=False)(("DwmGetCompositionTimingInfo", windll["dwmapi"]), ((1, 'hwnd'),(1, 'pTimingInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetWindowAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.Dwm.DWMWINDOWATTRIBUTE,c_void_p,UInt32, use_last_error=False)(("DwmGetWindowAttribute", windll["dwmapi"]), ((1, 'hwnd'),(1, 'dwAttribute'),(1, 'pvAttribute'),(1, 'cbAttribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmIsCompositionEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("DwmIsCompositionEnabled", windll["dwmapi"]), ((1, 'pfEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmModifyPreviousDxFrameDuration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,win32more.Foundation.BOOL, use_last_error=False)(("DwmModifyPreviousDxFrameDuration", windll["dwmapi"]), ((1, 'hwnd'),(1, 'cRefreshes'),(1, 'fRelative'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmQueryThumbnailSourceSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(("DwmQueryThumbnailSourceSize", windll["dwmapi"]), ((1, 'hThumbnail'),(1, 'pSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmRegisterThumbnail():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HWND,POINTER(IntPtr), use_last_error=False)(("DwmRegisterThumbnail", windll["dwmapi"]), ((1, 'hwndDestination'),(1, 'hwndSource'),(1, 'phThumbnailId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmSetDxFrameDuration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32, use_last_error=False)(("DwmSetDxFrameDuration", windll["dwmapi"]), ((1, 'hwnd'),(1, 'cRefreshes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmSetPresentParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Graphics.Dwm.DWM_PRESENT_PARAMETERS_head), use_last_error=False)(("DwmSetPresentParameters", windll["dwmapi"]), ((1, 'hwnd'),(1, 'pPresentParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmSetWindowAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.Dwm.DWMWINDOWATTRIBUTE,c_void_p,UInt32, use_last_error=False)(("DwmSetWindowAttribute", windll["dwmapi"]), ((1, 'hwnd'),(1, 'dwAttribute'),(1, 'pvAttribute'),(1, 'cbAttribute'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmUnregisterThumbnail():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(("DwmUnregisterThumbnail", windll["dwmapi"]), ((1, 'hThumbnailId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmUpdateThumbnailProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.Graphics.Dwm.DWM_THUMBNAIL_PROPERTIES_head), use_last_error=False)(("DwmUpdateThumbnailProperties", windll["dwmapi"]), ((1, 'hThumbnailId'),(1, 'ptnProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmSetIconicThumbnail():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.Gdi.HBITMAP,UInt32, use_last_error=False)(("DwmSetIconicThumbnail", windll["dwmapi"]), ((1, 'hwnd'),(1, 'hbmp'),(1, 'dwSITFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmSetIconicLivePreviewBitmap():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.Gdi.HBITMAP,POINTER(win32more.Foundation.POINT_head),UInt32, use_last_error=False)(("DwmSetIconicLivePreviewBitmap", windll["dwmapi"]), ((1, 'hwnd'),(1, 'hbmp'),(1, 'pptClient'),(1, 'dwSITFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmInvalidateIconicBitmaps():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(("DwmInvalidateIconicBitmaps", windll["dwmapi"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmAttachMilContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(("DwmAttachMilContent", windll["dwmapi"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmDetachMilContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(("DwmDetachMilContent", windll["dwmapi"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmFlush():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("DwmFlush", windll["dwmapi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetGraphicsStreamTransformHint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dwm.MilMatrix3x2D_head), use_last_error=False)(("DwmGetGraphicsStreamTransformHint", windll["dwmapi"]), ((1, 'uIndex'),(1, 'pTransform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetGraphicsStreamClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(("DwmGetGraphicsStreamClient", windll["dwmapi"]), ((1, 'uIndex'),(1, 'pClientUuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetTransportAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(UInt32), use_last_error=False)(("DwmGetTransportAttributes", windll["dwmapi"]), ((1, 'pfIsRemoting'),(1, 'pfIsConnected'),(1, 'pDwGeneration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmTransitionOwnedWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.Dwm.DWMTRANSITION_OWNEDWINDOW_TARGET, use_last_error=False)(("DwmTransitionOwnedWindow", windll["dwmapi"]), ((1, 'hwnd'),(1, 'target'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmRenderGesture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dwm.GESTURE_TYPE,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.POINT), use_last_error=False)(("DwmRenderGesture", windll["dwmapi"]), ((1, 'gt'),(1, 'cContacts'),(1, 'pdwPointerID'),(1, 'pPoints'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmTetherContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.POINT, use_last_error=False)(("DwmTetherContact", windll["dwmapi"]), ((1, 'dwPointerID'),(1, 'fEnable'),(1, 'ptTether'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmShowContact():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Dwm.DWM_SHOWCONTACT, use_last_error=False)(("DwmShowContact", windll["dwmapi"]), ((1, 'dwPointerID'),(1, 'eShowContact'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DwmGetUnmetTabRequirements():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Graphics.Dwm.DWM_TAB_WINDOW_REQUIREMENTS), use_last_error=False)(("DwmGetUnmetTabRequirements", windll["dwmapi"]), ((1, 'appWindow'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DWM_BB_ENABLE",
    "DWM_BB_BLURREGION",
    "DWM_BB_TRANSITIONONMAXIMIZED",
    "DWMWA_COLOR_DEFAULT",
    "DWMWA_COLOR_NONE",
    "DWM_CLOAKED_APP",
    "DWM_CLOAKED_SHELL",
    "DWM_CLOAKED_INHERITED",
    "DWM_TNP_RECTDESTINATION",
    "DWM_TNP_RECTSOURCE",
    "DWM_TNP_OPACITY",
    "DWM_TNP_VISIBLE",
    "DWM_TNP_SOURCECLIENTAREAONLY",
    "DWM_FRAME_DURATION_DEFAULT",
    "DWM_EC_DISABLECOMPOSITION",
    "DWM_EC_ENABLECOMPOSITION",
    "DWM_SIT_DISPLAYFRAME",
    "c_DwmMaxQueuedBuffers",
    "c_DwmMaxMonitors",
    "c_DwmMaxAdapters",
    "DWM_BLURBEHIND",
    "DWMWINDOWATTRIBUTE",
    "DWMWA_NCRENDERING_ENABLED",
    "DWMWA_NCRENDERING_POLICY",
    "DWMWA_TRANSITIONS_FORCEDISABLED",
    "DWMWA_ALLOW_NCPAINT",
    "DWMWA_CAPTION_BUTTON_BOUNDS",
    "DWMWA_NONCLIENT_RTL_LAYOUT",
    "DWMWA_FORCE_ICONIC_REPRESENTATION",
    "DWMWA_FLIP3D_POLICY",
    "DWMWA_EXTENDED_FRAME_BOUNDS",
    "DWMWA_HAS_ICONIC_BITMAP",
    "DWMWA_DISALLOW_PEEK",
    "DWMWA_EXCLUDED_FROM_PEEK",
    "DWMWA_CLOAK",
    "DWMWA_CLOAKED",
    "DWMWA_FREEZE_REPRESENTATION",
    "DWMWA_PASSIVE_UPDATE_MODE",
    "DWMWA_USE_HOSTBACKDROPBRUSH",
    "DWMWA_USE_IMMERSIVE_DARK_MODE",
    "DWMWA_WINDOW_CORNER_PREFERENCE",
    "DWMWA_BORDER_COLOR",
    "DWMWA_CAPTION_COLOR",
    "DWMWA_TEXT_COLOR",
    "DWMWA_VISIBLE_FRAME_BORDER_THICKNESS",
    "DWMWA_LAST",
    "DWM_WINDOW_CORNER_PREFERENCE",
    "DWMWCP_DEFAULT",
    "DWMWCP_DONOTROUND",
    "DWMWCP_ROUND",
    "DWMWCP_ROUNDSMALL",
    "DWMNCRENDERINGPOLICY",
    "DWMNCRP_USEWINDOWSTYLE",
    "DWMNCRP_DISABLED",
    "DWMNCRP_ENABLED",
    "DWMNCRP_LAST",
    "DWMFLIP3DWINDOWPOLICY",
    "DWMFLIP3D_DEFAULT",
    "DWMFLIP3D_EXCLUDEBELOW",
    "DWMFLIP3D_EXCLUDEABOVE",
    "DWMFLIP3D_LAST",
    "DWM_THUMBNAIL_PROPERTIES",
    "UNSIGNED_RATIO",
    "DWM_TIMING_INFO",
    "DWM_SOURCE_FRAME_SAMPLING",
    "DWM_SOURCE_FRAME_SAMPLING_POINT",
    "DWM_SOURCE_FRAME_SAMPLING_COVERAGE",
    "DWM_SOURCE_FRAME_SAMPLING_LAST",
    "DWM_PRESENT_PARAMETERS",
    "MilMatrix3x2D",
    "DWMTRANSITION_OWNEDWINDOW_TARGET",
    "DWMTRANSITION_OWNEDWINDOW_NULL",
    "DWMTRANSITION_OWNEDWINDOW_REPOSITION",
    "GESTURE_TYPE",
    "GT_PEN_TAP",
    "GT_PEN_DOUBLETAP",
    "GT_PEN_RIGHTTAP",
    "GT_PEN_PRESSANDHOLD",
    "GT_PEN_PRESSANDHOLDABORT",
    "GT_TOUCH_TAP",
    "GT_TOUCH_DOUBLETAP",
    "GT_TOUCH_RIGHTTAP",
    "GT_TOUCH_PRESSANDHOLD",
    "GT_TOUCH_PRESSANDHOLDABORT",
    "GT_TOUCH_PRESSANDTAP",
    "DWM_SHOWCONTACT",
    "DWMSC_DOWN",
    "DWMSC_UP",
    "DWMSC_DRAG",
    "DWMSC_HOLD",
    "DWMSC_PENBARREL",
    "DWMSC_NONE",
    "DWMSC_ALL",
    "DWM_TAB_WINDOW_REQUIREMENTS",
    "DWMTWR_NONE",
    "DWMTWR_IMPLEMENTED_BY_SYSTEM",
    "DWMTWR_WINDOW_RELATIONSHIP",
    "DWMTWR_WINDOW_STYLES",
    "DWMTWR_WINDOW_REGION",
    "DWMTWR_WINDOW_DWM_ATTRIBUTES",
    "DWMTWR_WINDOW_MARGINS",
    "DWMTWR_TABBING_ENABLED",
    "DWMTWR_USER_POLICY",
    "DWMTWR_GROUP_POLICY",
    "DWMTWR_APP_COMPAT",
    "DwmDefWindowProc",
    "DwmEnableBlurBehindWindow",
    "DwmEnableComposition",
    "DwmEnableMMCSS",
    "DwmExtendFrameIntoClientArea",
    "DwmGetColorizationColor",
    "DwmGetCompositionTimingInfo",
    "DwmGetWindowAttribute",
    "DwmIsCompositionEnabled",
    "DwmModifyPreviousDxFrameDuration",
    "DwmQueryThumbnailSourceSize",
    "DwmRegisterThumbnail",
    "DwmSetDxFrameDuration",
    "DwmSetPresentParameters",
    "DwmSetWindowAttribute",
    "DwmUnregisterThumbnail",
    "DwmUpdateThumbnailProperties",
    "DwmSetIconicThumbnail",
    "DwmSetIconicLivePreviewBitmap",
    "DwmInvalidateIconicBitmaps",
    "DwmAttachMilContent",
    "DwmDetachMilContent",
    "DwmFlush",
    "DwmGetGraphicsStreamTransformHint",
    "DwmGetGraphicsStreamClient",
    "DwmGetTransportAttributes",
    "DwmTransitionOwnedWindow",
    "DwmRenderGesture",
    "DwmTetherContact",
    "DwmShowContact",
    "DwmGetUnmetTabRequirements",
]
