import asyncio
from ctypes import sizeof

from win32more.Windows.Graphics.Imaging import BitmapDecoder
from win32more.Windows.Media.Ocr import OcrEngine
from win32more.Windows.Storage import FileAccessMode
from win32more.Windows.Storage.Pickers import FileOpenPicker
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

from win32more import FAILED, WinError


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


async def show_message(owner_window, title, msg):
    dialog = MessageDialog.CreateWithTitle(msg, title)
    dialog.as_(IInitializeWithWindow).Initialize(owner_window)
    return await dialog.ShowAsync()


async def open_file(owner_window, filter):
    picker = FileOpenPicker.CreateInstance()
    picker.as_(IInitializeWithWindow).Initialize(owner_window)
    picker.FileTypeFilter.Append(filter)
    return await picker.PickSingleFileAsync()


async def read_image(storage_file):
    bitmap = await BitmapDecoder.CreateWithIdAsync(
        BitmapDecoder.PngDecoderId, await storage_file.OpenAsync(FileAccessMode.Read)
    )
    return await bitmap.GetSoftwareBitmapAsync()


def list_ocr_languages():
    print("AvailableRecognizerLanguages:")
    for lang in OcrEngine.AvailableRecognizerLanguages:
        print(f"{lang.LanguageTag}: {lang.DisplayName}")


async def ocr(software_image):
    # lang = Language.CreateLanguage("ja")
    engine = OcrEngine.TryCreateFromUserProfileLanguages()
    result = await engine.RecognizeAsync(software_image)
    return result.Text


async def winrt_ocr(owner_window):
    list_ocr_languages()
    storage_file = await open_file(owner_window, ".png")
    if not storage_file:
        return
    software_bitmap = await read_image(storage_file)
    text = await ocr(software_bitmap)
    await show_message(owner_window, "Ocr result", text)


async def main():
    hr = RoInitialize(RO_INIT_MULTITHREADED)
    if FAILED(hr):
        raise WinError(hr)

    task = asyncio.create_task(winrt_ocr(create_owner_window()))
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
