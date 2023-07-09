import asyncio
import tkinter as tk
from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.Windows.Graphics.Imaging import BitmapDecoder
from win32more.Windows.Media.Ocr import OcrEngine
from win32more.Windows.Storage import FileAccessMode_Read
from win32more.Windows.Storage.Pickers import FileOpenPicker
from win32more.Windows.UI.Popups import MessageDialog
from win32more.Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from win32more.Windows.Win32.UI.Shell import IInitializeWithWindow

mainhwnd = None


def initialize_with_window(obj, hwnd):
    ii = IInitializeWithWindow()
    hr = obj.QueryInterface(IInitializeWithWindow._iid_, ii)
    if FAILED(hr):
        raise WinError(hr)
    ii.Initialize(hwnd)
    ii.Release()


async def show_message(title, msg):
    dialog = MessageDialog.CreateWithTitle(msg, title)
    initialize_with_window(dialog, mainhwnd)
    return await dialog.ShowAsync()


async def open_file(filter):
    picker = FileOpenPicker.CreateInstance()
    initialize_with_window(picker, mainhwnd)
    picker.FileTypeFilter.Append(filter)
    return await picker.PickSingleFileAsync_2()


async def read_image(storage_file):
    bitmap = await BitmapDecoder.CreateWithIdAsync(
        BitmapDecoder.PngDecoderId, await storage_file.OpenAsync(FileAccessMode_Read)
    )
    return await bitmap.GetSoftwareBitmapAsync()


def list_ocr_languages():
    print("AvailableRecognizerLanguages:")
    vec = OcrEngine.AvailableRecognizerLanguages
    for i in range(vec.Size):
        lang = vec.GetAt(i)
        print(f"{lang.LanguageTag}: {lang.DisplayName}")


async def ocr(software_image):
    # lang = Language.CreateLanguage("ja")
    engine = OcrEngine.TryCreateFromUserProfileLanguages()
    result = await engine.RecognizeAsync(software_image)
    return result.Text


async def run_ocr():
    storage_file = await open_file(".png")
    if not storage_file:
        return
    software_bitmap = await read_image(storage_file)
    text = await ocr(software_bitmap)
    await show_message("Ocr result", text)


async def main():
    global mainhwnd

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

    mainhwnd = root.winfo_id()

    list_ocr_languages()

    button = tk.Button(root, text="Open image for OCR", command=lambda: asyncio.create_task(run_ocr()))
    button.pack(padx=10, pady=10, fill="both", expand=True)

    while is_running:
        root.after(100, root.quit)
        root.mainloop()
        await asyncio.sleep(0)

    RoUninitialize()


asyncio.run(main())
