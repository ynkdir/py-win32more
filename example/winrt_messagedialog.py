import tkinter as tk
from ctypes import WinError

from win32more import FAILED
from win32more.asyncui import async_callback, async_start_runner
from win32more.Windows.UI.Popups import MessageDialog
from win32more.Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from win32more.Windows.Win32.UI.Shell import IInitializeWithWindow


def initialize_with_window(obj, hwnd):
    ii = obj.as_(IInitializeWithWindow)
    ii.Initialize(hwnd)


@async_callback
async def winrt_dialog(hwnd):
    dialog = MessageDialog.CreateWithTitle("This is WinRT MessageDialog", "WinRT MessageDialog")

    initialize_with_window(dialog, hwnd)

    uicommand = await dialog.ShowAsync()

    print(uicommand, uicommand.Label)


def main() -> None:
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

    root = tk.Tk()
    root.eval("tk::PlaceWindow . center")

    hwnd = root.winfo_id()

    button = tk.Button(root, text="Popup WinRT dialog", command=lambda: winrt_dialog(hwnd))
    button.pack(padx=10, pady=10, fill="both", expand=True)

    async_start_runner()

    root.mainloop()

    RoUninitialize()


if __name__ == "__main__":
    main()
