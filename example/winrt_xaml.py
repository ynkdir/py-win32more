# https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/host-standard-control-with-xaml-islands-cpp
# This example requires "<maxversiontested Id="10.0.18362.0"/>" in python.exe's manifest.
# Use Microsoft Store version of Python.

# ruff: noqa: F841

import tkinter as tk

from win32more import FAILED, WinError
from win32more.Windows.UI import Colors
from win32more.Windows.UI.Xaml import HorizontalAlignment, VerticalAlignment
from win32more.Windows.UI.Xaml.Controls import StackPanel, TextBox
from win32more.Windows.UI.Xaml.Hosting import DesktopWindowXamlSource, WindowsXamlManager
from win32more.Windows.UI.Xaml.Media import SolidColorBrush
from win32more.Windows.Win32.Foundation import HWND
from win32more.Windows.Win32.System.WinRT import RO_INIT_SINGLETHREADED, RoInitialize, RoUninitialize
from win32more.Windows.Win32.System.WinRT.Xaml import IDesktopWindowXamlSourceNative
from win32more.Windows.Win32.UI.WindowsAndMessaging import SWP_SHOWWINDOW, SetWindowPos


def window_size_center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")


def main2():
    root = tk.Tk()
    window_size_center(root, 1000, 400)

    hWnd = root.winfo_id()

    # Begin XAML Island section.

    # The call to winrt::init_apartment initializes COM; by default, in a multithreaded apartment.
    # winrt::init_apartment(apartment_type::single_threaded);

    # Initialize the XAML framework's core window for the current thread.
    winxamlmanager = WindowsXamlManager.InitializeForCurrentThread()

    # This DesktopWindowXamlSource is the object that enables a non-UWP desktop application
    # to host WinRT XAML controls in any UI element that is associated with a window handle (HWND).
    desktopSource = DesktopWindowXamlSource.CreateInstance(None, None)

    # Get handle to the core window.
    interop = IDesktopWindowXamlSourceNative(own=True)
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
    SetWindowPos(hWndXamlIsland, 0, 100, 100, 800, 200, SWP_SHOWWINDOW)

    # Create the XAML content.
    xamlContainer = StackPanel.CreateInstance(None, None)
    xamlContainer.Background = SolidColorBrush.CreateInstanceWithColor(Colors.LightGray)

    tb = TextBox.CreateInstance(None, None)
    tb.Text = "Hello World from Xaml Islands!"
    tb.VerticalAlignment = VerticalAlignment.Center
    tb.HorizontalAlignment = HorizontalAlignment.Center
    tb.FontSize = 48

    xamlContainer.Children.Append(tb)
    xamlContainer.UpdateLayout()
    desktopSource.Content = xamlContainer

    # End XAML Island section.

    root.mainloop()


def main():
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

    main2()

    RoUninitialize()


if __name__ == "__main__":
    main()
