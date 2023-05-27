import asyncio
import tkinter as tk
from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.Windows.UI.Popups import MessageDialog
from win32more.Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from win32more.Windows.Win32.UI.Shell import IInitializeWithWindow


def initialize_with_window(obj, hwnd):
    ii = IInitializeWithWindow(own=True)
    hr = obj.QueryInterface(IInitializeWithWindow._iid_, ii)
    if FAILED(hr):
        raise WinError(hr)
    ii.Initialize(hwnd)


async def winrt_dialog(hwnd):
    dialog = MessageDialog.CreateWithTitle("This is WinRT MessageDialog", "WinRT MessageDialog")

    initialize_with_window(dialog, hwnd)

    uicommand = await dialog.ShowAsync()

    print(uicommand, uicommand.Label)


async def main2() -> None:
    is_running = True

    def on_delete():
        nonlocal is_running
        is_running = False

    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_delete)
    root.eval("tk::PlaceWindow . center")

    hwnd = root.winfo_id()

    button = tk.Button(root, text="Popup WinRT dialog", command=lambda: asyncio.create_task(winrt_dialog(hwnd)))
    button.pack(padx=10, pady=10, fill="both", expand=True)

    while is_running:
        root.after(100, root.quit)
        root.mainloop()
        await asyncio.sleep(0)


async def main() -> None:
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

    await main2()

    RoUninitialize()


if __name__ == "__main__":
    asyncio.run(main())
