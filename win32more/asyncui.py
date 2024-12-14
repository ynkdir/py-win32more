import asyncio
import sys

from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer

running_loop = None


# Asyncio runner for Windows message loop.
def async_start_runner(delay_ms=100):
    global running_loop

    def timer_proc(*args):
        running_loop._run_once()

    running_loop = asyncio.new_event_loop()
    running_loop.stop()
    running_loop._run_forever_setup()

    SetTimer(0, 0, delay_ms, timer_proc)


_tasks_keep = set()


def async_callback(coroutine_function):
    def wrapper(*args):
        _addref(args)
        if sys.version_info < (3, 12):
            task = loop.create_task(coroutine_function(*args))
        else:
            # Start task eagerly.
            # Some method can not be called after returned.
            # (e.g. CoreWebView2NewWindowRequestedEventArgs.GetDeferral())
            task = asyncio.eager_task_factory(loop, coroutine_function(*args))
        _tasks_keep.add(task)
        task.add_done_callback(_tasks_keep.remove)
        task.add_done_callback(lambda _: _release(args))

    loop = _get_running_loop()

    return wrapper


def _get_running_loop():
    return running_loop or asyncio.get_running_loop()


def _addref(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.AddRef()


def _release(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.Release()
