import asyncio
import tkinter as tk
from contextlib import ExitStack
from ctypes import (
    WinError,
)
from typing import Generic, TypeVar

from Windows import FAILED
from Windows.Foundation import (
    IAsyncOperation,
)
from Windows.UI.Popups import MessageDialog
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from Windows.Win32.UI.Shell import IInitializeWithWindow

T = TypeVar("T")


class AwaitAsyncOperation(Generic[T]):
    def __init__(self, iasync: IAsyncOperation[T]):
        self.iasync = iasync

    # TODO: Move to IAsyncOperation
    def __await__(self) -> T:
        event = asyncio.Event()
        self.iasync.Completed = lambda asyncInfo, asyncStatus: event.set()
        yield from event.wait().__await__()
        r = self.iasync.GetResults()
        self.iasync.Release()
        return r


def initialize_with_window(obj, hwnd):
    ii = IInitializeWithWindow()
    hr = obj.QueryInterface(IInitializeWithWindow._iid_, ii)
    if FAILED(hr):
        raise WinError(hr)
    ii.Initialize(hwnd)
    ii.Release()


async def winrt_dialog(hwnd):
    with ExitStack() as defer:
        dialog = MessageDialog.CreateWithTitle("This is WinRT MessageDialog", "WinRT MessageDialog")
        defer.callback(dialog.Release)

        initialize_with_window(dialog, hwnd)

        iasync = dialog.ShowAsync()

        uicommand = await AwaitAsyncOperation(iasync)
        defer.callback(uicommand.Release)

        print(uicommand, uicommand.Label)


async def main() -> None:
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

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

    RoUninitialize()


if __name__ == "__main__":
    asyncio.run(main())
