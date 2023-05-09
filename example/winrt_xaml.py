# https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/host-standard-control-with-xaml-islands-cpp
# This example requires "<maxversiontested Id="10.0.18362.0"/>" in python.exe's manifest.
# See scripts/download_python_for_winrt.ps1.

import tkinter as tk
from ctypes import (
    WinError,
)

from Windows import (
    FAILED,
)
from Windows.UI import (
    Colors,
)
from Windows.UI.Xaml import (
    HorizontalAlignment_Center,
    IFrameworkElement,
    IUIElement,
    VerticalAlignment_Center,
)
from Windows.UI.Xaml.Controls import (
    IPanel,
    StackPanel,
    TextBox,
)
from Windows.UI.Xaml.Hosting import (
    DesktopWindowXamlSource,
    WindowsXamlManager,
)
from Windows.UI.Xaml.Media import (
    SolidColorBrush,
)
from Windows.Win32.Foundation import (
    HWND,
)
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from Windows.Win32.System.WinRT.Xaml import (
    IDesktopWindowXamlSourceNative,
)
from Windows.Win32.UI.WindowsAndMessaging import (
    SWP_SHOWWINDOW,
    SetWindowPos,
)


def window_size_center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")


def main():
    root = tk.Tk()
    window_size_center(root, 700, 400)

    hWnd = root.winfo_id()

    # Begin XAML Island section.

    # The call to winrt::init_apartment initializes COM; by default, in a multithreaded apartment.
    # winrt::init_apartment(apartment_type::single_threaded);
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

    # Initialize the XAML framework's core window for the current thread.
    WindowsXamlManager.InitializeForCurrentThread()

    # This DesktopWindowXamlSource is the object that enables a non-UWP desktop application
    # to host WinRT XAML controls in any UI element that is associated with a window handle (HWND).
    desktopSource = DesktopWindowXamlSource.CreateInstance(None, None)

    # Get handle to the core window.
    interop = IDesktopWindowXamlSourceNative()
    hr = desktopSource.QueryInterface(IDesktopWindowXamlSourceNative._iid_, interop)
    if FAILED(hr):
        raise WinError(hr)

    # Parent the DesktopWindowXamlSource object to the current window.
    hr = interop.AttachToWindow(hWnd)
    if FAILED(hr):
        raise WinError(hr)

    # This HWND will be the window handler for the XAML Island: A child window that contains XAML.
    hWndXamlIsland = HWND(0)

    # Get the new child window's HWND.
    hr = interop.get_WindowHandle(hWndXamlIsland)
    if FAILED(hr):
        raise WinError(hr)

    # Update the XAML Island window size because initially it is 0,0.
    SetWindowPos(hWndXamlIsland, 0, 100, 100, 500, 200, SWP_SHOWWINDOW)

    # Create the XAML content.
    xamlContainer = StackPanel.CreateInstance(None, None)
    panel = IPanel()
    hr = xamlContainer.QueryInterface(IPanel._iid_, panel)
    if FAILED(hr):
        raise WinError(hr)
    uielement = IUIElement()
    hr = xamlContainer.QueryInterface(IUIElement._iid_, uielement)
    if FAILED(hr):
        raise WinError(hr)
    brush = SolidColorBrush.CreateInstanceWithColor(Colors.LightGray)
    panel.Background = brush

    tb = TextBox.CreateInstance(None, None)
    fe = IFrameworkElement()
    hr = tb.QueryInterface(IFrameworkElement._iid_, fe)
    if FAILED(hr):
        raise WinError(hr)
    tb.Text = "Hello World from Xaml Islands!"
    fe.VerticalAlignment = VerticalAlignment_Center
    fe.HorizontalAlignment = HorizontalAlignment_Center
    fe.FontSize = 48

    panel.Children.Append(tb)
    uielement.UpdateLayout()
    desktopSource.Content = xamlContainer

    # End XAML Island section.

    root.mainloop()

    RoUninitialize()


if __name__ == "__main__":
    main()
