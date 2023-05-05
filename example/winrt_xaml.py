# https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/host-standard-control-with-xaml-islands-cpp
# This example requires "<maxversiontested Id="10.0.18362.0"/>" in python.exe's manifest.
# See scripts/download_python_for_winrt.ps1.

from ctypes import (
    WinError,
    sizeof,
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
from Windows.Win32.Graphics.Gdi import (
    COLOR_WINDOW,
    HBRUSH,
    HDC,
    PAINTSTRUCT,
    BeginPaint,
    EndPaint,
    TextOutW,
    UpdateWindow,
)
from Windows.Win32.System.LibraryLoader import (
    GetModuleHandleW,
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
    CW_USEDEFAULT,
    MB_OK,
    MSG,
    SW_SHOWNORMAL,
    SWP_SHOWWINDOW,
    WM_DESTROY,
    WM_PAINT,
    WNDCLASSEXW,
    WNDPROC,
    WS_OVERLAPPEDWINDOW,
    WS_VISIBLE,
    CreateWindowExW,
    DefWindowProcW,
    DispatchMessageW,
    GetMessageW,
    LoadIconW,
    MessageBoxW,
    PostQuitMessage,
    RegisterClassExW,
    SetWindowPos,
    ShowWindow,
    TranslateMessage,
)

# icon resource in python.exe
IDI_APPLICATION = 1

_hWnd = None


def WinMain():
    global _hWnd

    hInstance = GetModuleHandleW(None)
    nCmdShow = SW_SHOWNORMAL

    # The main window class name.
    szWindowClass = "Win32DesktopApp"

    windowClass = WNDCLASSEXW()
    windowClass.cbSize = sizeof(WNDCLASSEXW)
    windowClass.lpfnWndProc = WindowProc
    windowClass.hInstance = hInstance
    windowClass.lpszClassName = szWindowClass
    windowClass.hbrBackground = HBRUSH(COLOR_WINDOW + 1)

    windowClass.hIconSm = LoadIconW(windowClass.hInstance, IDI_APPLICATION)

    if RegisterClassExW(windowClass) == 0:
        MessageBoxW(0, "Windows registration failed!", "Error", MB_OK)
        raise WinError()

    _hWnd = CreateWindowExW(
        0,
        szWindowClass,
        "Windows c++ Win32 Desktop App",
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        0,
        0,
        hInstance,
        0,
    )
    if _hWnd == 0:
        MessageBoxW(0, "Call to CreateWindow failed!", "Error", MB_OK)
        raise WinError()

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
    hr = interop.AttachToWindow(_hWnd)
    if FAILED(hr):
        raise WinError(hr)

    # This HWND will be the window handler for the XAML Island: A child window that contains XAML.
    hWndXamlIsland = HWND(0)

    # Get the new child window's HWND.
    hr = interop.get_WindowHandle(hWndXamlIsland)
    if FAILED(hr):
        raise WinError(hr)

    # Update the XAML Island window size because initially it is 0,0.
    SetWindowPos(hWndXamlIsland, 0, 200, 100, 800, 200, SWP_SHOWWINDOW)

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
    brush = SolidColorBrush.CreateInstanceWithColor(Colors.get_LightGray())
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

    ShowWindow(_hWnd, nCmdShow)
    UpdateWindow(_hWnd)

    # Message loop:
    msg = MSG()
    while GetMessageW(msg, 0, 0, 0):
        TranslateMessage(msg)
        DispatchMessageW(msg)

    # someobj.Release() call omitted.

    RoUninitialize()

    return 0


@WNDPROC
def ChildWindowProc(hWnd, messageCode, wParam, lParam):
    return DefWindowProcW(hWnd, messageCode, wParam, lParam)


@WNDPROC
def WindowProc(hWnd, messageCode, wParam, lParam):
    if messageCode == WM_PAINT:
        if hWnd == _hWnd:  # ?
            ps = PAINTSTRUCT()
            hdc = HDC()
            greeting = "Hello World in Win32!"
            hdc = BeginPaint(hWnd, ps)
            TextOutW(hdc, 300, 5, greeting, len(greeting))
            EndPaint(hWnd, ps)
    elif messageCode == WM_DESTROY:
        PostQuitMessage(0)
    else:
        return DefWindowProcW(hWnd, messageCode, wParam, lParam)

    return 0


if __name__ == "__main__":
    WinMain()
