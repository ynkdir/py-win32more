from contextlib import ExitStack
from ctypes import (
    POINTER,
    WINFUNCTYPE,
    Structure,
    WinError,
    c_void_p,
    cast,
    pointer,
    py_object,
)
from threading import Event, Thread
from typing import Generic, TypeVar

from Windows import FAILED, Guid, UInt32, _ro_get_parameterized_type_instance_iid
from Windows.Foundation import (
    AsyncOperationCompletedHandler,
    AsyncStatus,
    IAsyncOperation,
)
from Windows.UI.Popups import IUICommand, MessageDialog
from Windows.Win32.Foundation import E_NOINTERFACE, HRESULT, HWND, LPARAM, S_OK, WPARAM
from Windows.Win32.Graphics.Gdi import (
    COLOR_WINDOW,
    HBRUSH,
    PAINTSTRUCT,
    BeginPaint,
    EndPaint,
    FillRect,
)
from Windows.Win32.System.Com import IUnknown
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

T = TypeVar("T")


class AsyncOperationCompletedHandlerImpl(Generic[T], Structure):
    Guid = AsyncOperationCompletedHandler.Guid

    _fields_ = [("vtable", POINTER(c_void_p)), ("self", py_object)]

    def __init__(self, event):
        print("AsyncOperationCompletedHandler.__init__()", self)
        self.vtable = (c_void_p * 4)()
        self.vtable[0] = cast(self._QueryInterface, c_void_p)
        self.vtable[1] = cast(self._AddRef, c_void_p)
        self.vtable[2] = cast(self._Release, c_void_p)
        self.vtable[3] = cast(self._Invoke, c_void_p)
        self.self = py_object(self)
        # FIXME: cannot get __orig_class__ in __init__()
        # self.guid_t = _ro_get_parameterized_type_instance_iid(self.__orig_class__)
        self.refcount = 0
        self.event = event
        self.AddRef()

    def __del__(self):
        print("AsyncOperationCompletedHandler.__del__()", self)

    @WINFUNCTYPE(HRESULT, c_void_p, c_void_p, POINTER(c_void_p))
    def _QueryInterface(this, riid, ppvObject):
        print(this)
        self = cast(this, POINTER(AsyncOperationCompletedHandlerImpl)).contents.self
        riid = cast(riid, POINTER(Guid))  # for Guid name conflict
        return self.QueryInterface(riid, ppvObject)

    def QueryInterface(self, riid, ppvObject):
        print(
            "AsyncOperationCompletedHandlerImpl.QueryInterface()",
            riid.contents,
            ppvObject.contents,
        )
        if str(riid.contents) == str(self.guid_t):
            ppvObject.contents.value = cast(pointer(self), c_void_p).value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == "{00000000-0000-0000-c000-000000000046}":  # IUnknown
            ppvObject.contents.value = cast(pointer(self), c_void_p).value
            self.AddRef()
            return S_OK
        return E_NOINTERFACE

    @WINFUNCTYPE(UInt32, c_void_p)
    def _AddRef(this):
        print(this)
        self = cast(this, POINTER(AsyncOperationCompletedHandlerImpl)).contents.self
        return self.AddRef()

    def AddRef(self):
        self.refcount += 1
        print("AsyncOperationCompletedHandlerImpl.AddRef()", self.refcount)
        return self.refcount

    @WINFUNCTYPE(UInt32, c_void_p)
    def _Release(this):
        print(this)
        self = cast(this, POINTER(AsyncOperationCompletedHandlerImpl)).contents.self
        return self.Release()

    def Release(self):
        self.refcount -= 1
        if self.refcount == 0:
            self.self = None
        print("AsyncOperationCompletedHandlerImpl.Release()", self.refcount)
        return self.refcount

    @WINFUNCTYPE(HRESULT, c_void_p, IAsyncOperation, AsyncStatus)
    def _Invoke(this, asyncInfo, asyncStatus):
        print(this)
        self = cast(this, POINTER(AsyncOperationCompletedHandlerImpl)).contents.self
        return self.Invoke(asyncInfo, asyncStatus)

    def Invoke(self, asyncInfo, asyncStatus):
        print("AsyncOperationCompletedHandlerImpl.Invoke()", asyncStatus)
        self.event.set()
        return S_OK


# FIXME: Keep reference.  handler.Release() will be called after winrt_dialog thread ends.
handler = None


def await_i_async_operation(iasync: IAsyncOperation[T]) -> T:
    global handler
    event = Event()
    handler = AsyncOperationCompletedHandlerImpl[iasync.__orig_class__.__args__[0]](
        event
    )
    handler.guid_t = _ro_get_parameterized_type_instance_iid(handler.__orig_class__)
    iasync.Completed = cast(pointer(handler), AsyncOperationCompletedHandler)
    while not event.wait(1):
        pass
    r = iasync.GetResults()
    iasync.Release()
    handler.Release()
    return r


def winrt_dialog(hwnd):
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_MULTITHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

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

        uicommand = await_i_async_operation(iasync)
        defer.callback(uicommand.Release)

        print(uicommand, uicommand.Label)


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
        Thread(target=winrt_dialog, args=[hwnd]).start()
        return 0
    return DefWindowProcW(hwnd, uMsg, wParam, lParam)


def main() -> None:
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

        WinMain()


if __name__ == "__main__":
    main()
