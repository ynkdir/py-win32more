import asyncio

from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer

running_loop = None


# Asyncio runner for Windows message loop.
def async_start_runner(delay_ms=100):
    global running_loop

    # safety check for compatibility
    if running_loop is not None:
        return running_loop

    def timer_proc(*args):
        running_loop.stop()
        running_loop.run_forever()

    running_loop = asyncio.new_event_loop()

    SetTimer(0, 0, delay_ms, timer_proc)

    return running_loop


def async_callback(coroutine_function):
    def wrapper(*args):
        _run_coroutine_threadsafe_with_addref(coroutine_function(*args), loop, args)

    loop = _get_running_loop()

    return wrapper


def _get_running_loop():
    return running_loop or asyncio.get_running_loop()


def _run_coroutine_threadsafe_with_addref(coro, loop, args):
    _addref(args)
    future = asyncio.run_coroutine_threadsafe(coro, loop)
    future.add_done_callback(lambda future: _release(args))
    return future


def _addref(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.AddRef()


def _release(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.Release()
