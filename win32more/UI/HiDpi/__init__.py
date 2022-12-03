from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.UI.Controls
import win32more.UI.HiDpi
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
DPI_AWARENESS_CONTEXT_UNAWARE = -1
DPI_AWARENESS_CONTEXT_SYSTEM_AWARE = -2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE = -3
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED = -5
def _define_OpenThemeDataForDpi():
    try:
        return WINFUNCTYPE(win32more.UI.Controls.HTHEME,win32more.Foundation.HWND,win32more.Foundation.PWSTR,UInt32)(('OpenThemeDataForDpi', windll['UxTheme.dll']), ((1, 'hwnd'),(1, 'pszClassList'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDialogControlDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS,win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS)(('SetDialogControlDpiChangeBehavior', windll['USER32.dll']), ((1, 'hWnd'),(1, 'mask'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDialogControlDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS,win32more.Foundation.HWND)(('GetDialogControlDpiChangeBehavior', windll['USER32.dll']), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDialogDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS,win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS)(('SetDialogDpiChangeBehavior', windll['USER32.dll']), ((1, 'hDlg'),(1, 'mask'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDialogDpiChangeBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS,win32more.Foundation.HWND)(('GetDialogDpiChangeBehavior', windll['USER32.dll']), ((1, 'hDlg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemMetricsForDpi():
    try:
        return WINFUNCTYPE(Int32,win32more.UI.WindowsAndMessaging.SYSTEM_METRICS_INDEX,UInt32)(('GetSystemMetricsForDpi', windll['USER32.dll']), ((1, 'nIndex'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdjustWindowRectExForDpi():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),win32more.UI.WindowsAndMessaging.WINDOW_STYLE,win32more.Foundation.BOOL,win32more.UI.WindowsAndMessaging.WINDOW_EX_STYLE,UInt32)(('AdjustWindowRectExForDpi', windll['USER32.dll']), ((1, 'lpRect'),(1, 'dwStyle'),(1, 'bMenu'),(1, 'dwExStyle'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogicalToPhysicalPointForPerMonitorDPI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head))(('LogicalToPhysicalPointForPerMonitorDPI', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PhysicalToLogicalPointForPerMonitorDPI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head))(('PhysicalToLogicalPointForPerMonitorDPI', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemParametersInfoForDpi():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,c_void_p,UInt32,UInt32)(('SystemParametersInfoForDpi', windll['USER32.dll']), ((1, 'uiAction'),(1, 'uiParam'),(1, 'pvParam'),(1, 'fWinIni'),(1, 'dpi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('SetThreadDpiAwarenessContext', windll['USER32.dll']), ((1, 'dpiContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,)(('GetThreadDpiAwarenessContext', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.Foundation.HWND)(('GetWindowDpiAwarenessContext', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAwarenessFromDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('GetAwarenessFromDpiAwarenessContext', windll['USER32.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiFromDpiAwarenessContext():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('GetDpiFromDpiAwarenessContext', windll['USER32.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreDpiAwarenessContextsEqual():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('AreDpiAwarenessContextsEqual', windll['USER32.dll']), ((1, 'dpiContextA'),(1, 'dpiContextB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('IsValidDpiAwarenessContext', windll['USER32.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForWindow():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND)(('GetDpiForWindow', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForSystem():
    try:
        return WINFUNCTYPE(UInt32,)(('GetDpiForSystem', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemDpiForProcess():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetSystemDpiForProcess', windll['USER32.dll']), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableNonClientDpiScaling():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('EnableNonClientDpiScaling', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDpiAwarenessContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT)(('SetProcessDpiAwarenessContext', windll['USER32.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiAwarenessContextForProcess():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT,win32more.Foundation.HANDLE)(('GetDpiAwarenessContextForProcess', windll['USER32.dll']), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetThreadDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR,win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR)(('SetThreadDpiHostingBehavior', windll['USER32.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetThreadDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR,)(('GetThreadDpiHostingBehavior', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowDpiHostingBehavior():
    try:
        return WINFUNCTYPE(win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR,win32more.Foundation.HWND)(('GetWindowDpiHostingBehavior', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessDpiAwareness():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.HiDpi.PROCESS_DPI_AWARENESS)(('SetProcessDpiAwareness', windll['api-ms-win-shcore-scaling-l1-1-1.dll']), ((1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessDpiAwareness():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.UI.HiDpi.PROCESS_DPI_AWARENESS))(('GetProcessDpiAwareness', windll['api-ms-win-shcore-scaling-l1-1-1.dll']), ((1, 'hprocess'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDpiForMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HMONITOR,win32more.UI.HiDpi.MONITOR_DPI_TYPE,POINTER(UInt32),POINTER(UInt32))(('GetDpiForMonitor', windll['api-ms-win-shcore-scaling-l1-1-1.dll']), ((1, 'hmonitor'),(1, 'dpiType'),(1, 'dpiX'),(1, 'dpiY'),))
    except (FileNotFoundError, AttributeError):
        return None
DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = UInt32
DCDC_DEFAULT = 0
DCDC_DISABLE_FONT_UPDATE = 1
DCDC_DISABLE_RELAYOUT = 2
DIALOG_DPI_CHANGE_BEHAVIORS = UInt32
DDC_DEFAULT = 0
DDC_DISABLE_ALL = 1
DDC_DISABLE_RESIZE = 2
DDC_DISABLE_CONTROL_RELAYOUT = 4
DPI_AWARENESS = Int32
DPI_AWARENESS_INVALID = -1
DPI_AWARENESS_UNAWARE = 0
DPI_AWARENESS_SYSTEM_AWARE = 1
DPI_AWARENESS_PER_MONITOR_AWARE = 2
DPI_AWARENESS_CONTEXT = IntPtr
DPI_HOSTING_BEHAVIOR = Int32
DPI_HOSTING_BEHAVIOR_INVALID = -1
DPI_HOSTING_BEHAVIOR_DEFAULT = 0
DPI_HOSTING_BEHAVIOR_MIXED = 1
MONITOR_DPI_TYPE = Int32
MDT_EFFECTIVE_DPI = 0
MDT_ANGULAR_DPI = 1
MDT_RAW_DPI = 2
MDT_DEFAULT = 0
PROCESS_DPI_AWARENESS = Int32
PROCESS_DPI_UNAWARE = 0
PROCESS_SYSTEM_DPI_AWARE = 1
PROCESS_PER_MONITOR_DPI_AWARE = 2
__all__ = [
    "AdjustWindowRectExForDpi",
    "AreDpiAwarenessContextsEqual",
    "DCDC_DEFAULT",
    "DCDC_DISABLE_FONT_UPDATE",
    "DCDC_DISABLE_RELAYOUT",
    "DDC_DEFAULT",
    "DDC_DISABLE_ALL",
    "DDC_DISABLE_CONTROL_RELAYOUT",
    "DDC_DISABLE_RESIZE",
    "DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS",
    "DIALOG_DPI_CHANGE_BEHAVIORS",
    "DPI_AWARENESS",
    "DPI_AWARENESS_CONTEXT",
    "DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE",
    "DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2",
    "DPI_AWARENESS_CONTEXT_SYSTEM_AWARE",
    "DPI_AWARENESS_CONTEXT_UNAWARE",
    "DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED",
    "DPI_AWARENESS_INVALID",
    "DPI_AWARENESS_PER_MONITOR_AWARE",
    "DPI_AWARENESS_SYSTEM_AWARE",
    "DPI_AWARENESS_UNAWARE",
    "DPI_HOSTING_BEHAVIOR",
    "DPI_HOSTING_BEHAVIOR_DEFAULT",
    "DPI_HOSTING_BEHAVIOR_INVALID",
    "DPI_HOSTING_BEHAVIOR_MIXED",
    "EnableNonClientDpiScaling",
    "GetAwarenessFromDpiAwarenessContext",
    "GetDialogControlDpiChangeBehavior",
    "GetDialogDpiChangeBehavior",
    "GetDpiAwarenessContextForProcess",
    "GetDpiForMonitor",
    "GetDpiForSystem",
    "GetDpiForWindow",
    "GetDpiFromDpiAwarenessContext",
    "GetProcessDpiAwareness",
    "GetSystemDpiForProcess",
    "GetSystemMetricsForDpi",
    "GetThreadDpiAwarenessContext",
    "GetThreadDpiHostingBehavior",
    "GetWindowDpiAwarenessContext",
    "GetWindowDpiHostingBehavior",
    "IsValidDpiAwarenessContext",
    "LogicalToPhysicalPointForPerMonitorDPI",
    "MDT_ANGULAR_DPI",
    "MDT_DEFAULT",
    "MDT_EFFECTIVE_DPI",
    "MDT_RAW_DPI",
    "MONITOR_DPI_TYPE",
    "OpenThemeDataForDpi",
    "PROCESS_DPI_AWARENESS",
    "PROCESS_DPI_UNAWARE",
    "PROCESS_PER_MONITOR_DPI_AWARE",
    "PROCESS_SYSTEM_DPI_AWARE",
    "PhysicalToLogicalPointForPerMonitorDPI",
    "SetDialogControlDpiChangeBehavior",
    "SetDialogDpiChangeBehavior",
    "SetProcessDpiAwareness",
    "SetProcessDpiAwarenessContext",
    "SetThreadDpiAwarenessContext",
    "SetThreadDpiHostingBehavior",
    "SystemParametersInfoForDpi",
]
