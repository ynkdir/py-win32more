from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.HiDpi
import win32more.Windows.Win32.UI.WindowsAndMessaging
DPI_AWARENESS_CONTEXT_UNAWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -1
DPI_AWARENESS_CONTEXT_SYSTEM_AWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -3
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -4
DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -5
@winfunctype('UxTheme.dll')
def OpenThemeDataForDpi(hwnd: win32more.Windows.Win32.Foundation.HWND, pszClassList: win32more.Windows.Win32.Foundation.PWSTR, dpi: UInt32) -> win32more.Windows.Win32.UI.Controls.HTHEME: ...
@winfunctype('USER32.dll')
def SetDialogControlDpiChangeBehavior(hWnd: win32more.Windows.Win32.Foundation.HWND, mask: win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS, values: win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogControlDpiChangeBehavior(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def SetDialogDpiChangeBehavior(hDlg: win32more.Windows.Win32.Foundation.HWND, mask: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS, values: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogDpiChangeBehavior(hDlg: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def GetSystemMetricsForDpi(nIndex: win32more.Windows.Win32.UI.WindowsAndMessaging.SYSTEM_METRICS_INDEX, dpi: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def AdjustWindowRectExForDpi(lpRect: POINTER(win32more.Windows.Win32.Foundation.RECT), dwStyle: win32more.Windows.Win32.UI.WindowsAndMessaging.WINDOW_STYLE, bMenu: win32more.Windows.Win32.Foundation.BOOL, dwExStyle: win32more.Windows.Win32.UI.WindowsAndMessaging.WINDOW_EX_STYLE, dpi: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LogicalToPhysicalPointForPerMonitorDPI(hWnd: win32more.Windows.Win32.Foundation.HWND, lpPoint: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def PhysicalToLogicalPointForPerMonitorDPI(hWnd: win32more.Windows.Win32.Foundation.HWND, lpPoint: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SystemParametersInfoForDpi(uiAction: UInt32, uiParam: UInt32, pvParam: VoidPtr, fWinIni: UInt32, dpi: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDpiAwarenessContext(dpiContext: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetThreadDpiAwarenessContext() -> win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetWindowDpiAwarenessContext(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetAwarenessFromDpiAwarenessContext(value: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS: ...
@winfunctype('USER32.dll')
def GetDpiFromDpiAwarenessContext(value: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> UInt32: ...
@winfunctype('USER32.dll')
def AreDpiAwarenessContextsEqual(dpiContextA: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT, dpiContextB: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsValidDpiAwarenessContext(value: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiForWindow(hwnd: win32more.Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def GetDpiForSystem() -> UInt32: ...
@winfunctype('USER32.dll')
def GetSystemDpiForProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('USER32.dll')
def EnableNonClientDpiScaling(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessDpiAwarenessContext(value: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiAwarenessContextForProcess(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def SetThreadDpiHostingBehavior(value: win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR) -> win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetThreadDpiHostingBehavior() -> win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetWindowDpiHostingBehavior(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def SetProcessDpiAwareness(value: win32more.Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetProcessDpiAwareness(hprocess: win32more.Windows.Win32.Foundation.HANDLE, value: POINTER(win32more.Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetDpiForMonitor(hmonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, dpiType: win32more.Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE, dpiX: POINTER(UInt32), dpiY: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = Int32
DCDC_DEFAULT: win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 0
DCDC_DISABLE_FONT_UPDATE: win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 1
DCDC_DISABLE_RELAYOUT: win32more.Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 2
DIALOG_DPI_CHANGE_BEHAVIORS = Int32
DDC_DEFAULT: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS = 0
DDC_DISABLE_ALL: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS = 1
DDC_DISABLE_RESIZE: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS = 2
DDC_DISABLE_CONTROL_RELAYOUT: win32more.Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS = 4
DPI_AWARENESS = Int32
DPI_AWARENESS_INVALID: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS = -1
DPI_AWARENESS_UNAWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS = 0
DPI_AWARENESS_SYSTEM_AWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS = 1
DPI_AWARENESS_PER_MONITOR_AWARE: win32more.Windows.Win32.UI.HiDpi.DPI_AWARENESS = 2
DPI_AWARENESS_CONTEXT = VoidPtr
DPI_HOSTING_BEHAVIOR = Int32
DPI_HOSTING_BEHAVIOR_INVALID: win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR = -1
DPI_HOSTING_BEHAVIOR_DEFAULT: win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR = 0
DPI_HOSTING_BEHAVIOR_MIXED: win32more.Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR = 1
MONITOR_DPI_TYPE = Int32
MDT_EFFECTIVE_DPI: win32more.Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE = 0
MDT_ANGULAR_DPI: win32more.Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE = 1
MDT_RAW_DPI: win32more.Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE = 2
MDT_DEFAULT: win32more.Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE = 0
PROCESS_DPI_AWARENESS = Int32
PROCESS_DPI_UNAWARE: win32more.Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS = 0
PROCESS_SYSTEM_DPI_AWARE: win32more.Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS = 1
PROCESS_PER_MONITOR_DPI_AWARE: win32more.Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS = 2


make_ready(__name__)
