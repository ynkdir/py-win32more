from contextlib import ExitStack
from ctypes import WinError

from Windows import FAILED, UInt32
from Windows.UI.Popups import MessageDialog
from Windows.Win32.Foundation import HWND, LPARAM, WPARAM
from Windows.Win32.Graphics.Gdi import (
    COLOR_WINDOW,
    HBRUSH,
    PAINTSTRUCT,
    BeginPaint,
    EndPaint,
    FillRect,
)
from Windows.Win32.System.LibraryLoader import GetModuleHandleW
from Windows.Win32.System.WinRT import (
    RO_INIT_MULTITHREADED,
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from Windows.Win32.UI.Shell import IInitializeWithWindow
from Windows.Win32.UI.WindowsAndMessaging import (
    CW_USEDEFAULT,
    MSG,
    SW_SHOWNORMAL,
    WM_DESTROY,
    WM_KEYDOWN,
    WM_PAINT,
    WNDCLASSW,
    WNDPROC,
    WS_OVERLAPPEDWINDOW,
    CreateWindowExW,
    DefWindowProcW,
    DispatchMessageW,
    GetMessageW,
    PostQuitMessage,
    RegisterClassW,
    ShowWindow,
    TranslateMessage,
)


def WinMain():
    hInstance = GetModuleHandleW(None)
    nCmdShow = SW_SHOWNORMAL

    # Register the window class.
    CLASS_NAME = "Sample Window Class"

    wc = WNDCLASSW()

    wc.lpfnWndProc = WNDPROC(WindowProc)
    wc.hInstance = hInstance
    wc.lpszClassName = CLASS_NAME

    RegisterClassW(wc)

    # Create the window.

    hwnd = CreateWindowExW(
        0,  # Optional window styles.
        CLASS_NAME,  # Window class
        "Press key to popup WinRT dialog",  # Window text
        WS_OVERLAPPEDWINDOW,  # Window style
        # Size and position
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        0,  # Parent window
        0,  # Menu
        hInstance,  # Instance handle
        0,  # Additional application data
    )

    if hwnd == 0:
        return 0

    ShowWindow(hwnd, nCmdShow)

    # Run the message loop.

    msg = MSG()
    while GetMessageW(msg, 0, 0, 0) > 0:
        TranslateMessage(msg)
        DispatchMessageW(msg)

    return 0


def WindowProc(hwnd: HWND, uMsg: UInt32, wParam: WPARAM, lParam: LPARAM):
    if uMsg == WM_DESTROY:
        PostQuitMessage(0)
        return 0
    elif uMsg == WM_PAINT:
        ps = PAINTSTRUCT()
        hdc = BeginPaint(hwnd, ps)

        # All painting occurs here, between BeginPaint and EndPaint.

        FillRect(hdc, ps.rcPaint, HBRUSH(COLOR_WINDOW + 1))

        EndPaint(hwnd, ps)

        return 0
    elif uMsg == WM_KEYDOWN:
        print("WM_KEYDOWN")
        winrt_dialog(hwnd)
        return 0
    return DefWindowProcW(hwnd, uMsg, wParam, lParam)


def winrt_dialog(hwnd):
    with ExitStack() as defer:
        dialog = MessageDialog.CreateWithTitle(
            "This is WinRT MessageDialog", "WinRT MessageDialog"
        )
        defer.callback(dialog.Release)

        ii = IInitializeWithWindow()
        hr = dialog.QueryInterface(IInitializeWithWindow.Guid, ii)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(ii.Release)
        ii.Initialize(hwnd)

        iasync = dialog.ShowAsync()
        defer.callback(iasync.Release)

        # FIXME: need more work
        # res = iasync.GetResults()
        # print(res)


def main() -> None:
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

        WinMain()


if __name__ == "__main__":
    main()
