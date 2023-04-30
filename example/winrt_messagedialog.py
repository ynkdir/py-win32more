import asyncio
from contextlib import ExitStack
from ctypes import (
    POINTER,
    WINFUNCTYPE,
    Structure,
    WinError,
    addressof,
    c_void_p,
    cast,
    py_object,
)
from typing import Generic, TypeVar

from Windows import FAILED, Guid, UInt32
from Windows._winrt import _ro_get_parameterized_type_instance_iid
from Windows.Foundation import (
    AsyncOperationCompletedHandler,
    AsyncStatus,
    IAsyncOperation,
)
from Windows.UI.Popups import MessageDialog
from Windows.Win32.Foundation import E_NOINTERFACE, HRESULT, HWND, LPARAM, S_OK, WPARAM
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


class PyAsyncOperationCompletedHandlerImpl(Generic[T], Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p)), ("comptr", py_object)]

    def __init__(self, comptr):
        self.lpvtbl = (c_void_p * 4)()
        self.lpvtbl[0] = cast(self.QueryInterface, c_void_p)
        self.lpvtbl[1] = cast(self.AddRef, c_void_p)
        self.lpvtbl[2] = cast(self.Release, c_void_p)
        self.lpvtbl[3] = cast(self.Invoke, c_void_p)
        self.comptr = py_object(comptr)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(Guid), POINTER(c_void_p))
    def QueryInterface(this, riid, ppvObject):
        print(this)
        self = cast(this, POINTER(PyAsyncOperationCompletedHandlerImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef(this):
        print(this)
        self = cast(this, POINTER(PyAsyncOperationCompletedHandlerImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release(this):
        print(this)
        self = cast(this, POINTER(PyAsyncOperationCompletedHandlerImpl)).contents
        return self.comptr.Release()

    @WINFUNCTYPE(HRESULT, c_void_p, IAsyncOperation, AsyncStatus)
    def Invoke(this, asyncInfo, asyncStatus):
        print(this)
        self = cast(this, POINTER(PyAsyncOperationCompletedHandlerImpl)).contents
        return self.comptr.Invoke(asyncInfo, asyncStatus)


class PyAsyncOperationCompletedHandler(Generic[T], AsyncOperationCompletedHandler[T]):
    _iid_ = AsyncOperationCompletedHandler._iid_

    _keep_reference_in_python_world_ = {}

    def __init__(self):
        print("PyAsyncOperationCompletedHandler.__init__()", self)

    def __del__(self):
        print("PyAsyncOperationCompletedHandler.__del__()", self)

    # FIXME: How to get __orig_class__.__args__ in class method?
    # @classmethod
    def CreateInstance(self, event):
        self.comobj = PyAsyncOperationCompletedHandlerImpl[self.__orig_class__.__args__[0]](self)
        self.value = addressof(self.comobj)
        self._generic_iid_ = _ro_get_parameterized_type_instance_iid(self.__orig_class__)
        self.refcount = 0
        self.event = event
        self.AddRef()
        self._keep_reference_in_python_world_[id(self)] = self
        return self

    def QueryInterface(self, riid, ppvObject):
        print(
            "PyAsyncOperationCompletedHandler.QueryInterface()",
            riid.contents,
            ppvObject.contents,
        )
        if str(riid.contents) == str(self._generic_iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == "{00000000-0000-0000-c000-000000000046}":  # IUnknown
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        return E_NOINTERFACE

    def AddRef(self):
        self.refcount += 1
        print("PyAsyncOperationCompletedHandler.AddRef()", self.refcount)
        return self.refcount

    def Release(self):
        self.refcount -= 1
        if self.refcount == 0:
            self.comobj.comptr = None
            del self._keep_reference_in_python_world_[id(self)]
        print("PyAsyncOperationCompletedHandler.Release()", self.refcount)
        return self.refcount

    def Invoke(self, asyncInfo, asyncStatus):
        print("PyAsyncOperationCompletedHandler.Invoke()", asyncStatus)
        self.event.set()
        return S_OK


class AwaitAsyncOperation(Generic[T]):
    def __init__(self, iasync: IAsyncOperation[T]):
        self.iasync = iasync

    # TODO: Move to IAsyncOperation
    def __await__(self) -> T:
        event = asyncio.Event()
        handler = PyAsyncOperationCompletedHandler[self.iasync.__orig_class__.__args__[0]]().CreateInstance(event)
        self.iasync.Completed = handler
        yield from event.wait().__await__()
        r = self.iasync.GetResults()
        self.iasync.Release()
        handler.Release()
        return r


async def winrt_dialog(hwnd):
    with ExitStack() as defer:
        dialog = MessageDialog.CreateWithTitle("This is WinRT MessageDialog", "WinRT MessageDialog")
        defer.callback(dialog.Release)

        ii = IInitializeWithWindow()
        hr = dialog.QueryInterface(IInitializeWithWindow._iid_, ii)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(ii.Release)
        ii.Initialize(hwnd)

        iasync = dialog.ShowAsync()

        uicommand = await AwaitAsyncOperation(iasync)
        defer.callback(uicommand.Release)

        print(uicommand, uicommand.Label)


async def WinMain():
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
        await asyncio.sleep(0)

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
        asyncio.create_task(winrt_dialog(hwnd))
        return 0
    return DefWindowProcW(hwnd, uMsg, wParam, lParam)


async def main() -> None:
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

        await WinMain()


if __name__ == "__main__":
    asyncio.run(main())
