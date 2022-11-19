from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.UI.HiDpi

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
DPI_AWARENESS_CONTEXT_UNAWARE = -1
DPI_AWARENESS_CONTEXT_SYSTEM_AWARE = -2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE = -3
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED = -5
DPI_AWARENESS_CONTEXT = IntPtr
DPI_AWARENESS = Int32
DPI_AWARENESS_INVALID = -1
DPI_AWARENESS_UNAWARE = 0
DPI_AWARENESS_SYSTEM_AWARE = 1
DPI_AWARENESS_PER_MONITOR_AWARE = 2
DPI_HOSTING_BEHAVIOR = Int32
DPI_HOSTING_BEHAVIOR_INVALID = -1
DPI_HOSTING_BEHAVIOR_DEFAULT = 0
DPI_HOSTING_BEHAVIOR_MIXED = 1
DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = UInt32
DCDC_DEFAULT = 0
DCDC_DISABLE_FONT_UPDATE = 1
DCDC_DISABLE_RELAYOUT = 2
DIALOG_DPI_CHANGE_BEHAVIORS = UInt32
DDC_DEFAULT = 0
DDC_DISABLE_ALL = 1
DDC_DISABLE_RESIZE = 2
DDC_DISABLE_CONTROL_RELAYOUT = 4
PROCESS_DPI_AWARENESS = Int32
PROCESS_DPI_UNAWARE = 0
PROCESS_SYSTEM_DPI_AWARE = 1
PROCESS_PER_MONITOR_DPI_AWARE = 2
MONITOR_DPI_TYPE = Int32
MDT_EFFECTIVE_DPI = 0
MDT_ANGULAR_DPI = 1
MDT_RAW_DPI = 2
MDT_DEFAULT = 0
def _define_OpenThemeDataForDpi():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.HWND,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("OpenThemeDataForDpi", windll["UxTheme"]), ((1, 'hwnd'),(1, 'pszClassList'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDialogControlDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS,win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS, use_last_error=True)(("SetDialogControlDpiChangeBehavior", windll["USER32"]), ((1, 'hWnd'),(1, 'mask'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDialogControlDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS,win32more.Foundation.HWND, use_last_error=True)(("GetDialogControlDpiChangeBehavior", windll["USER32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDialogDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS,win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS, use_last_error=True)(("SetDialogDpiChangeBehavior", windll["USER32"]), ((1, 'hDlg'),(1, 'mask'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDialogDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS,win32more.Foundation.HWND, use_last_error=True)(("GetDialogDpiChangeBehavior", windll["USER32"]), ((1, 'hDlg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemMetricsForDpi():
    try:
        return WINFUNCTYPE(Int32,Int32,UInt32, use_last_error=True)(("GetSystemMetricsForDpi", windll["USER32"]), ((1, 'nIndex'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdjustWindowRectExForDpi():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),UInt32,win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=True)(("AdjustWindowRectExForDpi", windll["USER32"]), ((1, 'lpRect'),(1, 'dwStyle'),(1, 'bMenu'),(1, 'dwExStyle'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogicalToPhysicalPointForPerMonitorDPI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(("LogicalToPhysicalPointForPerMonitorDPI", windll["USER32"]), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PhysicalToLogicalPointForPerMonitorDPI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(("PhysicalToLogicalPointForPerMonitorDPI", windll["USER32"]), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemParametersInfoForDpi():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,c_void_p,UInt32,UInt32, use_last_error=True)(("SystemParametersInfoForDpi", windll["USER32"]), ((1, 'uiAction'),(1, 'uiParam'),(1, 'pvParam'),(1, 'fWinIni'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("SetThreadDpiAwarenessContext", windll["USER32"]), ((1, 'dpiContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("GetThreadDpiAwarenessContext", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.Foundation.HWND, use_last_error=False)(("GetWindowDpiAwarenessContext", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAwarenessFromDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("GetAwarenessFromDpiAwarenessContext", windll["USER32"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiFromDpiAwarenessContext():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("GetDpiFromDpiAwarenessContext", windll["USER32"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreDpiAwarenessContextsEqual():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("AreDpiAwarenessContextsEqual", windll["USER32"]), ((1, 'dpiContextA'),(1, 'dpiContextB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=False)(("IsValidDpiAwarenessContext", windll["USER32"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForWindow():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND, use_last_error=False)(("GetDpiForWindow", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForSystem():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetDpiForSystem", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDpiForProcess():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("GetSystemDpiForProcess", windll["USER32"]), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableNonClientDpiScaling():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("EnableNonClientDpiScaling", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, use_last_error=True)(("SetProcessDpiAwarenessContext", windll["USER32"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiAwarenessContextForProcess():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.Foundation.HANDLE, use_last_error=False)(("GetDpiAwarenessContextForProcess", windll["USER32"]), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR,win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR, use_last_error=False)(("SetThreadDpiHostingBehavior", windll["USER32"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR, use_last_error=False)(("GetThreadDpiHostingBehavior", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR,win32more.Foundation.HWND, use_last_error=False)(("GetWindowDpiHostingBehavior", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDpiAwareness():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.HiDpi.PROCESS_DPI_AWARENESS, use_last_error=False)(("SetProcessDpiAwareness", windll["api-ms-win-shcore-scaling-l1-1-1"]), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessDpiAwareness():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.UI.HiDpi.PROCESS_DPI_AWARENESS), use_last_error=False)(("GetProcessDpiAwareness", windll["api-ms-win-shcore-scaling-l1-1-1"]), ((1, 'hprocess'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HMONITOR,win32more.UI.HiDpi.MONITOR_DPI_TYPE,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetDpiForMonitor", windll["api-ms-win-shcore-scaling-l1-1-1"]), ((1, 'hmonitor'),(1, 'dpiType'),(1, 'dpiX'),(1, 'dpiY'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DPI_AWARENESS_CONTEXT_UNAWARE",
    "DPI_AWARENESS_CONTEXT_SYSTEM_AWARE",
    "DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE",
    "DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2",
    "DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED",
    "DPI_AWARENESS_CONTEXT",
    "DPI_AWARENESS",
    "DPI_AWARENESS_INVALID",
    "DPI_AWARENESS_UNAWARE",
    "DPI_AWARENESS_SYSTEM_AWARE",
    "DPI_AWARENESS_PER_MONITOR_AWARE",
    "DPI_HOSTING_BEHAVIOR",
    "DPI_HOSTING_BEHAVIOR_INVALID",
    "DPI_HOSTING_BEHAVIOR_DEFAULT",
    "DPI_HOSTING_BEHAVIOR_MIXED",
    "DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS",
    "DCDC_DEFAULT",
    "DCDC_DISABLE_FONT_UPDATE",
    "DCDC_DISABLE_RELAYOUT",
    "DIALOG_DPI_CHANGE_BEHAVIORS",
    "DDC_DEFAULT",
    "DDC_DISABLE_ALL",
    "DDC_DISABLE_RESIZE",
    "DDC_DISABLE_CONTROL_RELAYOUT",
    "PROCESS_DPI_AWARENESS",
    "PROCESS_DPI_UNAWARE",
    "PROCESS_SYSTEM_DPI_AWARE",
    "PROCESS_PER_MONITOR_DPI_AWARE",
    "MONITOR_DPI_TYPE",
    "MDT_EFFECTIVE_DPI",
    "MDT_ANGULAR_DPI",
    "MDT_RAW_DPI",
    "MDT_DEFAULT",
    "OpenThemeDataForDpi",
    "SetDialogControlDpiChangeBehavior",
    "GetDialogControlDpiChangeBehavior",
    "SetDialogDpiChangeBehavior",
    "GetDialogDpiChangeBehavior",
    "GetSystemMetricsForDpi",
    "AdjustWindowRectExForDpi",
    "LogicalToPhysicalPointForPerMonitorDPI",
    "PhysicalToLogicalPointForPerMonitorDPI",
    "SystemParametersInfoForDpi",
    "SetThreadDpiAwarenessContext",
    "GetThreadDpiAwarenessContext",
    "GetWindowDpiAwarenessContext",
    "GetAwarenessFromDpiAwarenessContext",
    "GetDpiFromDpiAwarenessContext",
    "AreDpiAwarenessContextsEqual",
    "IsValidDpiAwarenessContext",
    "GetDpiForWindow",
    "GetDpiForSystem",
    "GetSystemDpiForProcess",
    "EnableNonClientDpiScaling",
    "SetProcessDpiAwarenessContext",
    "GetDpiAwarenessContextForProcess",
    "SetThreadDpiHostingBehavior",
    "GetThreadDpiHostingBehavior",
    "GetWindowDpiHostingBehavior",
    "SetProcessDpiAwareness",
    "GetProcessDpiAwareness",
    "GetDpiForMonitor",
]
