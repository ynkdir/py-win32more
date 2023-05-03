import asyncio
import tkinter as tk
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
from Windows.Win32.Foundation import E_NOINTERFACE, HRESULT, S_OK
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from Windows.Win32.UI.Shell import IInitializeWithWindow

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
