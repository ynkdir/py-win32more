# Microsoft.UI.Interop.h

from win32more import FAILED, WinError
from win32more._prelude import POINTER, winfunctype
from win32more.Microsoft.UI import DisplayId, IconId, WindowId
from win32more.Windows.Win32.Foundation import HRESULT, HWND
from win32more.Windows.Win32.Graphics.Gdi import HMONITOR
from win32more.Windows.Win32.UI.WindowsAndMessaging import HICON


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetWindowIdFromWindow")
def _GetWindowIdFromWindow(hwnd: HWND, windowId: POINTER(WindowId)) -> HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetWindowFromWindowId")
def _GetWindowFromWindowId(windowId: WindowId, hwnd: POINTER(HWND)) -> HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetDisplayIdFromMonitor")
def _GetDisplayIdFromMonitor(hmonitor: HMONITOR, displayId: POINTER(DisplayId)) -> HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetMonitorFromDisplayId")
def _GetMonitorFromDisplayId(displayId: DisplayId, hmonitor: POINTER(HMONITOR)) -> HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetIconIdFromIcon")
def _GetIconIdFromIcon(hicon: HICON, iconId: POINTER(IconId)) -> HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll", entry_point="Windowing_GetIconFromIconId")
def _GetIconFromIconId(iconId: IconId, hicon: POINTER(HICON)) -> HRESULT: ...


def GetWindowIdFromWindow(hwnd: HWND) -> WindowId:
    windowId = WindowId()
    r = _GetWindowIdFromWindow(hwnd, windowId)
    if FAILED(r):
        raise WinError(r)
    return windowId


def GetWindowFromWindowId(windowId: WindowId) -> HWND:
    hwnd = HWND()
    r = _GetWindowFromWindowId(windowId, hwnd)
    if FAILED(r):
        raise WinError(r)
    return hwnd.value


def GetDisplayIdFromMonitor(hmonitor: HMONITOR) -> DisplayId:
    displayId = DisplayId()
    r = _GetDisplayIdFromMonitor(hmonitor, displayId)
    if FAILED(r):
        raise WinError(r)
    return displayId


def GetMonitorFromDisplayId(displayId: DisplayId) -> HMONITOR:
    hmonitor = HMONITOR()
    r = _GetMonitorFromDisplayId(displayId, hmonitor)
    if FAILED(r):
        raise WinError(r)
    return hmonitor.value


def GetIconIdFromIcon(hicon: HICON) -> IconId:
    iconId = IconId()
    r = _GetIconIdFromIcon(hicon, iconId)
    if FAILED(r):
        raise WinError(r)
    return iconId


def GetIconFromIconId(iconId: IconId) -> HICON:
    hicon = HICON()
    r = _GetIconFromIconId(iconId, hicon)
    if FAILED(r):
        raise WinError(r)
    return hicon.value
