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
        _async_task(coroutine_function, args, loop)

    loop = _get_running_loop()

    return wrapper


def _get_running_loop():
    return running_loop or asyncio.get_running_loop()


class _async_task:
    # Need to keep reference to task.  The event loop only keeps weak references to tasks.
    background_tasks = set()

    def __init__(self, coroutine_function, args, loop):
        self._args = args
        self._addref_args()
        self._task = loop.create_task(coroutine_function(*args))
        self._task.add_done_callback(self._done_callback)
        self.background_tasks.add(self)

    def _done_callback(self, task):
        self._release_args()
        self.background_tasks.discard(self)

    def _addref_args(self):
        for obj in self._args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.AddRef()

    def _release_args(self):
        for obj in self._args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.Release()
