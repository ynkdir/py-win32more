# Microsoft.UI.Interop.h
from __future__ import annotations

import win32more.Microsoft.UI
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.UI.WindowsAndMessaging
from win32more import FAILED, WinError
from win32more._prelude import POINTER, winfunctype


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetWindowIdFromWindow(
    hwnd: win32more.Windows.Win32.Foundation.HWND, windowId: POINTER(win32more.Microsoft.UI.WindowId)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetWindowFromWindowId(
    windowId: win32more.Microsoft.UI.WindowId, hwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetDisplayIdFromMonitor(
    hmonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, displayId: POINTER(win32more.Microsoft.UI.DisplayId)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetMonitorFromDisplayId(
    displayId: win32more.Microsoft.UI.DisplayId, hmonitor: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetIconIdFromIcon(
    hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, iconId: POINTER(win32more.Microsoft.UI.IconId)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.Internal.FrameworkUdk.dll")
def Windowing_GetIconFromIconId(
    iconId: win32more.Microsoft.UI.IconId, hicon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


def GetWindowIdFromWindow(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Microsoft.UI.WindowId:
    windowId = win32more.Microsoft.UI.WindowId()
    r = Windowing_GetWindowIdFromWindow(hwnd, windowId)
    if FAILED(r):
        raise WinError(r)
    return windowId


def GetWindowFromWindowId(windowId: win32more.Microsoft.UI.WindowId) -> win32more.Windows.Win32.Foundation.HWND:
    hwnd = win32more.Windows.Win32.Foundation.HWND()
    r = Windowing_GetWindowFromWindowId(windowId, hwnd)
    if FAILED(r):
        raise WinError(r)
    return hwnd.value


def GetDisplayIdFromMonitor(
    hmonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR,
) -> win32more.Microsoft.UI.DisplayId:
    displayId = win32more.Microsoft.UI.DisplayId()
    r = Windowing_GetDisplayIdFromMonitor(hmonitor, displayId)
    if FAILED(r):
        raise WinError(r)
    return displayId


def GetMonitorFromDisplayId(
    displayId: win32more.Microsoft.UI.DisplayId,
) -> win32more.Windows.Win32.Graphics.Gdi.HMONITOR:
    hmonitor = win32more.Windows.Win32.Graphics.Gdi.HMONITOR()
    r = Windowing_GetMonitorFromDisplayId(displayId, hmonitor)
    if FAILED(r):
        raise WinError(r)
    return hmonitor.value


def GetIconIdFromIcon(hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> win32more.Microsoft.UI.IconId:
    iconId = win32more.Microsoft.UI.IconId()
    r = Windowing_GetIconIdFromIcon(hicon, iconId)
    if FAILED(r):
        raise WinError(r)
    return iconId


def GetIconFromIconId(iconId: win32more.Microsoft.UI.IconId) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON:
    hicon = win32more.Windows.Win32.UI.WindowsAndMessaging.HICON()
    r = Windowing_GetIconFromIconId(iconId, hicon)
    if FAILED(r):
        raise WinError(r)
    return hicon.value
