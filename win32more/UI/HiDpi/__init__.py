from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.UI.Controls
import win32more.UI.HiDpi
import win32more.UI.WindowsAndMessaging
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
DPI_AWARENESS_CONTEXT_UNAWARE: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT = -1
DPI_AWARENESS_CONTEXT_SYSTEM_AWARE: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT = -2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT = -3
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT = -4
DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT = -5
@winfunctype('UxTheme.dll')
def OpenThemeDataForDpi(hwnd: win32more.Foundation.HWND, pszClassList: win32more.Foundation.PWSTR, dpi: UInt32) -> win32more.UI.Controls.HTHEME: ...
@winfunctype('USER32.dll')
def SetDialogControlDpiChangeBehavior(hWnd: win32more.Foundation.HWND, mask: win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS, values: win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogControlDpiChangeBehavior(hWnd: win32more.Foundation.HWND) -> win32more.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def SetDialogDpiChangeBehavior(hDlg: win32more.Foundation.HWND, mask: win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS, values: win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogDpiChangeBehavior(hDlg: win32more.Foundation.HWND) -> win32more.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def GetSystemMetricsForDpi(nIndex: win32more.UI.WindowsAndMessaging.SYSTEM_METRICS_INDEX, dpi: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def AdjustWindowRectExForDpi(lpRect: POINTER(win32more.Foundation.RECT_head), dwStyle: win32more.UI.WindowsAndMessaging.WINDOW_STYLE, bMenu: win32more.Foundation.BOOL, dwExStyle: win32more.UI.WindowsAndMessaging.WINDOW_EX_STYLE, dpi: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LogicalToPhysicalPointForPerMonitorDPI(hWnd: win32more.Foundation.HWND, lpPoint: POINTER(win32more.Foundation.POINT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def PhysicalToLogicalPointForPerMonitorDPI(hWnd: win32more.Foundation.HWND, lpPoint: POINTER(win32more.Foundation.POINT_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SystemParametersInfoForDpi(uiAction: UInt32, uiParam: UInt32, pvParam: c_void_p, fWinIni: UInt32, dpi: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDpiAwarenessContext(dpiContext: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetThreadDpiAwarenessContext() -> win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetWindowDpiAwarenessContext(hwnd: win32more.Foundation.HWND) -> win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetAwarenessFromDpiAwarenessContext(value: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.UI.HiDpi.DPI_AWARENESS: ...
@winfunctype('USER32.dll')
def GetDpiFromDpiAwarenessContext(value: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> UInt32: ...
@winfunctype('USER32.dll')
def AreDpiAwarenessContextsEqual(dpiContextA: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT, dpiContextB: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsValidDpiAwarenessContext(value: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiForWindow(hwnd: win32more.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def GetDpiForSystem() -> UInt32: ...
@winfunctype('USER32.dll')
def GetSystemDpiForProcess(hProcess: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('USER32.dll')
def EnableNonClientDpiScaling(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessDpiAwarenessContext(value: win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiAwarenessContextForProcess(hProcess: win32more.Foundation.HANDLE) -> win32more.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def SetThreadDpiHostingBehavior(value: win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR) -> win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetThreadDpiHostingBehavior() -> win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetWindowDpiHostingBehavior(hwnd: win32more.Foundation.HWND) -> win32more.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def SetProcessDpiAwareness(value: win32more.UI.HiDpi.PROCESS_DPI_AWARENESS) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetProcessDpiAwareness(hprocess: win32more.Foundation.HANDLE, value: POINTER(win32more.UI.HiDpi.PROCESS_DPI_AWARENESS)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetDpiForMonitor(hmonitor: win32more.Graphics.Gdi.HMONITOR, dpiType: win32more.UI.HiDpi.MONITOR_DPI_TYPE, dpiX: POINTER(UInt32), dpiY: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = UInt32
DCDC_DEFAULT: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 0
DCDC_DISABLE_FONT_UPDATE: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 1
DCDC_DISABLE_RELAYOUT: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 2
DIALOG_DPI_CHANGE_BEHAVIORS = UInt32
DDC_DEFAULT: DIALOG_DPI_CHANGE_BEHAVIORS = 0
DDC_DISABLE_ALL: DIALOG_DPI_CHANGE_BEHAVIORS = 1
DDC_DISABLE_RESIZE: DIALOG_DPI_CHANGE_BEHAVIORS = 2
DDC_DISABLE_CONTROL_RELAYOUT: DIALOG_DPI_CHANGE_BEHAVIORS = 4
DPI_AWARENESS = Int32
DPI_AWARENESS_INVALID: DPI_AWARENESS = -1
DPI_AWARENESS_UNAWARE: DPI_AWARENESS = 0
DPI_AWARENESS_SYSTEM_AWARE: DPI_AWARENESS = 1
DPI_AWARENESS_PER_MONITOR_AWARE: DPI_AWARENESS = 2
DPI_AWARENESS_CONTEXT = IntPtr
DPI_HOSTING_BEHAVIOR = Int32
DPI_HOSTING_BEHAVIOR_INVALID: DPI_HOSTING_BEHAVIOR = -1
DPI_HOSTING_BEHAVIOR_DEFAULT: DPI_HOSTING_BEHAVIOR = 0
DPI_HOSTING_BEHAVIOR_MIXED: DPI_HOSTING_BEHAVIOR = 1
MONITOR_DPI_TYPE = Int32
MDT_EFFECTIVE_DPI: MONITOR_DPI_TYPE = 0
MDT_ANGULAR_DPI: MONITOR_DPI_TYPE = 1
MDT_RAW_DPI: MONITOR_DPI_TYPE = 2
MDT_DEFAULT: MONITOR_DPI_TYPE = 0
PROCESS_DPI_AWARENESS = Int32
PROCESS_DPI_UNAWARE: PROCESS_DPI_AWARENESS = 0
PROCESS_SYSTEM_DPI_AWARE: PROCESS_DPI_AWARENESS = 1
PROCESS_PER_MONITOR_DPI_AWARE: PROCESS_DPI_AWARENESS = 2
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
