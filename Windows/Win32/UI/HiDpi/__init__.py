from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.UI.Controls
import Windows.Win32.UI.HiDpi
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DPI_AWARENESS_CONTEXT_UNAWARE: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -1
DPI_AWARENESS_CONTEXT_SYSTEM_AWARE: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -3
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -4
DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT = -5
@winfunctype('UxTheme.dll')
def OpenThemeDataForDpi(hwnd: Windows.Win32.Foundation.HWND, pszClassList: Windows.Win32.Foundation.PWSTR, dpi: UInt32) -> Windows.Win32.UI.Controls.HTHEME: ...
@winfunctype('USER32.dll')
def SetDialogControlDpiChangeBehavior(hWnd: Windows.Win32.Foundation.HWND, mask: Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS, values: Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogControlDpiChangeBehavior(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.UI.HiDpi.DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def SetDialogDpiChangeBehavior(hDlg: Windows.Win32.Foundation.HWND, mask: Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS, values: Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDialogDpiChangeBehavior(hDlg: Windows.Win32.Foundation.HWND) -> Windows.Win32.UI.HiDpi.DIALOG_DPI_CHANGE_BEHAVIORS: ...
@winfunctype('USER32.dll')
def GetSystemMetricsForDpi(nIndex: Windows.Win32.UI.WindowsAndMessaging.SYSTEM_METRICS_INDEX, dpi: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def AdjustWindowRectExForDpi(lpRect: POINTER(Windows.Win32.Foundation.RECT_head), dwStyle: Windows.Win32.UI.WindowsAndMessaging.WINDOW_STYLE, bMenu: Windows.Win32.Foundation.BOOL, dwExStyle: Windows.Win32.UI.WindowsAndMessaging.WINDOW_EX_STYLE, dpi: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LogicalToPhysicalPointForPerMonitorDPI(hWnd: Windows.Win32.Foundation.HWND, lpPoint: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def PhysicalToLogicalPointForPerMonitorDPI(hWnd: Windows.Win32.Foundation.HWND, lpPoint: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SystemParametersInfoForDpi(uiAction: UInt32, uiParam: UInt32, pvParam: VoidPtr, fWinIni: UInt32, dpi: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetThreadDpiAwarenessContext(dpiContext: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetThreadDpiAwarenessContext() -> Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetWindowDpiAwarenessContext(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def GetAwarenessFromDpiAwarenessContext(value: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> Windows.Win32.UI.HiDpi.DPI_AWARENESS: ...
@winfunctype('USER32.dll')
def GetDpiFromDpiAwarenessContext(value: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> UInt32: ...
@winfunctype('USER32.dll')
def AreDpiAwarenessContextsEqual(dpiContextA: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT, dpiContextB: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsValidDpiAwarenessContext(value: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiForWindow(hwnd: Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def GetDpiForSystem() -> UInt32: ...
@winfunctype('USER32.dll')
def GetSystemDpiForProcess(hProcess: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('USER32.dll')
def EnableNonClientDpiScaling(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetProcessDpiAwarenessContext(value: Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDpiAwarenessContextForProcess(hProcess: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.UI.HiDpi.DPI_AWARENESS_CONTEXT: ...
@winfunctype('USER32.dll')
def SetThreadDpiHostingBehavior(value: Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR) -> Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetThreadDpiHostingBehavior() -> Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('USER32.dll')
def GetWindowDpiHostingBehavior(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.UI.HiDpi.DPI_HOSTING_BEHAVIOR: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def SetProcessDpiAwareness(value: Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetProcessDpiAwareness(hprocess: Windows.Win32.Foundation.HANDLE, value: POINTER(Windows.Win32.UI.HiDpi.PROCESS_DPI_AWARENESS)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetDpiForMonitor(hmonitor: Windows.Win32.Graphics.Gdi.HMONITOR, dpiType: Windows.Win32.UI.HiDpi.MONITOR_DPI_TYPE, dpiX: POINTER(UInt32), dpiY: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = Int32
DCDC_DEFAULT: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 0
DCDC_DISABLE_FONT_UPDATE: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 1
DCDC_DISABLE_RELAYOUT: DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = 2
DIALOG_DPI_CHANGE_BEHAVIORS = Int32
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
