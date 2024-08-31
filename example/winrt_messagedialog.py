import asyncio
from ctypes import sizeof

from win32more import FAILED, WinError
from win32more.Windows.UI.Popups import MessageDialog
from win32more.Windows.Win32.System.LibraryLoader import GetModuleHandle
from win32more.Windows.Win32.System.WinRT import (
    RO_INIT_MULTITHREADED,
    RoInitialize,
    RoUninitialize,
)
from win32more.Windows.Win32.UI.Input.KeyboardAndMouse import SetActiveWindow
from win32more.Windows.Win32.UI.Shell import IInitializeWithWindow
from win32more.Windows.Win32.UI.WindowsAndMessaging import (
    CW_USEDEFAULT,
    MSG,
    WNDCLASS,
    WS_OVERLAPPED,
    CreateWindowEx,
    DefWindowProc,
    DispatchMessage,
    GetMessage,
    PostQuitMessage,
    RegisterClass,
    SetTimer,
    TranslateMessage,
)


def create_owner_window():
    CLASS_NAME = "Owner Window"
    hInstance = GetModuleHandle(None)

    wc = WNDCLASS()
    wc.cbSize = sizeof(WNDCLASS)
    wc.lpfnWndProc = DefWindowProc
    wc.hInstance = hInstance
    wc.lpszClassName = CLASS_NAME

    atom = RegisterClass(wc)
    if not atom:
        raise WinError()

    hwnd = CreateWindowEx(
        0, CLASS_NAME, "", WS_OVERLAPPED, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, 0, 0, hInstance, 0
    )
    if not hwnd:
        raise WinError()

    # workaround to avoid that dialog window appear in background.
    SetActiveWindow(hwnd)

    return hwnd


async def winrt_messagedialog(owner_window):
    dialog = MessageDialog.CreateWithTitle("This is WinRT MessageDialog", "WinRT MessageDialog")
    dialog.as_(IInitializeWithWindow).Initialize(owner_window)
    uicommand = await dialog.ShowAsync()
    print(uicommand, uicommand.Label)


async def main():
    hr = RoInitialize(RO_INIT_MULTITHREADED)
    if FAILED(hr):
        raise WinError(hr)

    task = asyncio.create_task(winrt_messagedialog(create_owner_window()))
    task.add_done_callback(lambda _: PostQuitMessage(0))

    SetTimer(0, 0, 100, None)  # to poll asyncio

    msg = MSG()
    while GetMessage(msg, 0, 0, 0) > 0:
        TranslateMessage(msg)
        DispatchMessage(msg)
        await asyncio.sleep(0)

    RoUninitialize()


if __name__ == "__main__":
    asyncio.run(main())
