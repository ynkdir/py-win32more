import re
from contextlib import ExitStack
from ctypes import POINTER, WinError, cast, create_string_buffer, create_unicode_buffer

from win32more.Windows.Win32.Foundation import (
    ERROR_CANCELLED,
    GENERIC_READ,
    GENERIC_WRITE,
    HWND,
    INVALID_HANDLE_VALUE,
    LPARAM,
    PWSTR,
    WPARAM,
    CloseHandle,
)
from win32more.Windows.Win32.Globalization import (
    CP_UTF8,
    MultiByteToWideChar,
    WideCharToMultiByte,
)
from win32more.Windows.Win32.Storage.FileSystem import (
    FILE_ATTRIBUTE_NORMAL,
    FILE_SHARE_READ,
    INVALID_FILE_SIZE,
    OPEN_ALWAYS,
    OPEN_EXISTING,
    CreateFileW,
    GetFileSize,
    ReadFile,
    WriteFile,
)
from win32more.Windows.Win32.System.Com import (
    CLSCTX_ALL,
    COINIT_APARTMENTTHREADED,
    CoCreateInstance,
    CoInitializeEx,
    CoTaskMemFree,
)
from win32more.Windows.Win32.System.LibraryLoader import GetModuleHandleW
from win32more.Windows.Win32.UI.Controls import EM_CANUNDO
from win32more.Windows.Win32.UI.Input.KeyboardAndMouse import SetFocus
from win32more.Windows.Win32.UI.Shell import (
    SIGDN_FILESYSPATH,
    FileOpenDialog,
    FileSaveDialog,
    IFileOpenDialog,
    IFileSaveDialog,
    IShellItem,
)
from win32more.Windows.Win32.UI.WindowsAndMessaging import (
    CW_USEDEFAULT,
    ES_AUTOVSCROLL,
    ES_LEFT,
    ES_MULTILINE,
    GWLP_HINSTANCE,
    MF_POPUP,
    MF_STRING,
    MSG,
    SW_SHOWNORMAL,
    WM_CLEAR,
    WM_COMMAND,
    WM_COPY,
    WM_CREATE,
    WM_CUT,
    WM_DESTROY,
    WM_PASTE,
    WM_SETFOCUS,
    WM_SIZE,
    WM_UNDO,
    WNDCLASSW,
    WS_CHILD,
    WS_OVERLAPPEDWINDOW,
    WS_VISIBLE,
    WS_VSCROLL,
    AppendMenuW,
    CreateMenu,
    CreateWindowExW,
    DefWindowProcW,
    DestroyWindow,
    DispatchMessageW,
    GetMessageW,
    GetWindowLongPtrW,
    GetWindowTextLengthW,
    GetWindowTextW,
    MoveWindow,
    PostQuitMessage,
    RegisterClassW,
    SendMessageW,
    SetWindowTextW,
    ShowWindow,
    TranslateMessage,
)

from win32more import FAILED, Byte, UInt32

IDM_FILE_OPEN = 101
IDM_FILE_SAVE = 102
IDM_FILE_SAVEAS = 103
IDM_FILE_EXIT = 104
IDM_EDIT_UNDO = 201
IDM_EDIT_CUT = 202
IDM_EDIT_COPY = 203
IDM_EDIT_PASTE = 204
IDM_EDIT_DEL = 205


editing_file = None
hEdit = None


def with_exitstack(f):
    def wrapper(*args):
        with ExitStack() as stack:
            return f(*args, stack)

    return wrapper


def LOWORD(x):
    return x & 0xFFFF


def HIWORD(x):
    return (x >> 16) & 0xFFFF


def HRESULT_CODE(x):
    return x & 0xFFFF


@with_exitstack
def ShowFileOpenDialog(stack):
    dialog = IFileOpenDialog()
    hr = CoCreateInstance(FileOpenDialog, None, CLSCTX_ALL, IFileOpenDialog._iid_, dialog)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(dialog.Release)

    hr = dialog.Show(0)
    if HRESULT_CODE(hr) == ERROR_CANCELLED:
        return None
    elif FAILED(hr):
        raise WinError(hr)

    item = IShellItem()
    hr = dialog.GetResult(item)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(item.Release)

    path = PWSTR()
    hr = item.GetDisplayName(SIGDN_FILESYSPATH, path)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(CoTaskMemFree, path)

    return path.value


@with_exitstack
def ShowFileSaveDialog(stack):
    dialog = IFileSaveDialog()
    hr = CoCreateInstance(FileSaveDialog, None, CLSCTX_ALL, IFileSaveDialog._iid_, dialog)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(dialog.Release)

    hr = dialog.Show(0)
    if HRESULT_CODE(hr) == ERROR_CANCELLED:
        return None
    elif FAILED(hr):
        raise WinError(hr)

    item = IShellItem()
    hr = dialog.GetResult(item)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(item.Release)

    path = PWSTR()
    hr = item.GetDisplayName(SIGDN_FILESYSPATH, path)
    if FAILED(hr):
        raise WinError(hr)
    stack.callback(CoTaskMemFree, path)

    return path.value


@with_exitstack
def read_text(path: str, stack) -> str:
    hFile = CreateFileW(path, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0)
    if hFile == INVALID_HANDLE_VALUE:
        raise WinError()
    stack.callback(CloseHandle, hFile)

    size = GetFileSize(hFile, None)
    if size == INVALID_FILE_SIZE:
        raise WinError()

    buf = create_string_buffer(size)

    bytesread = UInt32()
    r = ReadFile(hFile, cast(buf, POINTER(Byte)), size, bytesread, None)
    if not r:
        raise WinError()

    return utf8_to_widechar(buf.value)


@with_exitstack
def write_text(path: str, text: str, stack) -> None:
    hFile = CreateFileW(path, GENERIC_WRITE, 0, None, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, 0)
    if hFile == INVALID_FILE_SIZE:
        raise WinError()
    stack.callback(CloseHandle, hFile)

    buf = widechar_to_utf8(text)

    byteswritten = UInt32()
    r = WriteFile(hFile, cast(buf, POINTER(Byte)), len(buf), byteswritten, None)
    if not r:
        raise WinError()


def utf8_to_widechar(buf: bytes) -> str:
    if len(buf) == 0:
        return ""

    size = MultiByteToWideChar(CP_UTF8, 0, buf, len(buf), None, 0)
    if size == 0:
        raise WinError()

    wbuf = create_unicode_buffer(size)
    r = MultiByteToWideChar(CP_UTF8, 0, buf, len(buf), wbuf, size)
    if r == 0:
        raise WinError()

    return wbuf.value


def widechar_to_utf8(wbuf: str) -> bytes:
    if len(wbuf) == 0:
        return b""

    size = WideCharToMultiByte(CP_UTF8, 0, wbuf, len(wbuf), None, 0, None, None)
    if size == 0:
        raise WinError()

    buf = create_string_buffer(size)
    r = WideCharToMultiByte(CP_UTF8, 0, wbuf, len(wbuf), buf, size, None, None)
    if r == 0:
        raise WinError()

    return buf.value


def WindowProc(hwnd: HWND, uMsg: UInt32, wParam: WPARAM, lParam: LPARAM):
    global editing_file
    global hEdit

    if uMsg == WM_CREATE:
        hEdit = CreateWindowExW(
            0,
            "EDIT",
            None,
            WS_CHILD | WS_VISIBLE | WS_VSCROLL | ES_LEFT | ES_MULTILINE | ES_AUTOVSCROLL,
            0,
            0,
            0,
            0,
            hwnd,
            0,
            GetWindowLongPtrW(hwnd, GWLP_HINSTANCE),
            None,
        )
        return 0
    elif uMsg == WM_COMMAND:
        if wParam == IDM_FILE_OPEN:
            path = ShowFileOpenDialog()
            if path is not None:
                SetWindowTextW(hEdit, re.sub(r"\r\n|\r|\n", "\r\n", read_text(path)))
                SetWindowTextW(hwnd, path)
                editing_file = path
            return 0
        elif wParam == IDM_FILE_SAVE:
            path = editing_file
            if path is None:
                path = ShowFileSaveDialog()
            if path is not None:
                buflen = GetWindowTextLengthW(hEdit) + 1
                buf = create_unicode_buffer(buflen)
                GetWindowTextW(hEdit, buf, buflen)
                write_text(path, re.sub(r"\r\n", "\n", buf.value))
                SetWindowTextW(hwnd, path)
                editing_file = path
            return 0
        elif wParam == IDM_FILE_SAVEAS:
            path = ShowFileSaveDialog()
            if path is not None:
                buflen = GetWindowTextLengthW(hEdit) + 1
                buf = create_unicode_buffer(buflen)
                GetWindowTextW(hEdit, buf, buflen)
                write_text(path, re.sub(r"\r\n", "\n", buf.value))
                SetWindowTextW(hwnd, path)
                editing_file = path
            return 0
        elif wParam == IDM_FILE_EXIT:
            DestroyWindow(hwnd)
            return 0
        elif wParam == IDM_EDIT_UNDO:
            if SendMessageW(hEdit, EM_CANUNDO, 0, 0):
                SendMessageW(hEdit, WM_UNDO, 0, 0)
            return 0
        elif wParam == IDM_EDIT_CUT:
            SendMessageW(hEdit, WM_CUT, 0, 0)
            return 0
        elif wParam == IDM_EDIT_COPY:
            SendMessageW(hEdit, WM_COPY, 0, 0)
            return 0
        elif wParam == IDM_EDIT_PASTE:
            SendMessageW(hEdit, WM_PASTE, 0, 0)
            return 0
        elif wParam == IDM_EDIT_DEL:
            SendMessageW(hEdit, WM_CLEAR, 0, 0)
            return 0
    elif uMsg == WM_SETFOCUS:
        SetFocus(hEdit)
        return 0
    elif uMsg == WM_SIZE:
        MoveWindow(hEdit, 0, 0, LOWORD(lParam), HIWORD(lParam), True)
        return 0
    elif uMsg == WM_DESTROY:
        PostQuitMessage(0)
        return 0
    return DefWindowProcW(hwnd, uMsg, wParam, lParam)


def WinMain():
    hInstance = GetModuleHandleW(None)
    nCmdShow = SW_SHOWNORMAL

    hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED)
    if FAILED(hr):
        raise WinError(hr)

    hMenu = CreateMenu()

    hMenuFile = CreateMenu()
    AppendMenuW(hMenu, MF_POPUP, hMenuFile, "File")
    AppendMenuW(hMenuFile, MF_STRING, IDM_FILE_OPEN, "Open")
    AppendMenuW(hMenuFile, MF_STRING, IDM_FILE_SAVE, "Save")
    AppendMenuW(hMenuFile, MF_STRING, IDM_FILE_SAVEAS, "Save As")
    AppendMenuW(hMenuFile, MF_STRING, IDM_FILE_EXIT, "Exit")

    hMenuEdit = CreateMenu()
    AppendMenuW(hMenu, MF_POPUP, hMenuEdit, "Edit")
    AppendMenuW(hMenuEdit, MF_STRING, IDM_EDIT_UNDO, "Undo")
    AppendMenuW(hMenuEdit, MF_STRING, IDM_EDIT_CUT, "Cut")
    AppendMenuW(hMenuEdit, MF_STRING, IDM_EDIT_COPY, "Copy")
    AppendMenuW(hMenuEdit, MF_STRING, IDM_EDIT_PASTE, "Paste")
    AppendMenuW(hMenuEdit, MF_STRING, IDM_EDIT_DEL, "Del")

    CLASS_NAME = "MainWindow"

    wc = WNDCLASSW()

    wc.lpfnWndProc = WindowProc
    wc.hInstance = hInstance
    wc.lpszClassName = CLASS_NAME

    RegisterClassW(wc)

    # Create the window.

    hwnd = CreateWindowExW(
        0,  # Optional window styles.
        CLASS_NAME,  # Window class
        "Text Editor",  # Window text
        WS_OVERLAPPEDWINDOW,  # Window style
        # Size and position
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        0,  # Parent window
        hMenu,  # Menu
        hInstance,  # Instance handle
        0,  # Additional application data
    )

    if not hwnd:
        raise WinError()

    ShowWindow(hwnd, nCmdShow)

    # Run the message loop.

    msg = MSG()
    while GetMessageW(msg, 0, 0, 0) > 0:
        TranslateMessage(msg)
        DispatchMessageW(msg)

    return 0


if __name__ == "__main__":
    WinMain()
