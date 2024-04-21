import asyncio

from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer


# Asyncio runner for Windows event loop.
def async_start_runner(delay_ms=100):
    def timer_proc(*args):
        loop.stop()
        loop.run_forever()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    SetTimer(0, 0, delay_ms, timer_proc)


def async_callback(coroutine_function):
    def wrapper(*args):
        async_task(coroutine_function, args)

    return wrapper


class async_task:
    # Need to keep reference to task.  The event loop only keeps weak references to tasks.
    background_tasks = set()

    def __init__(self, coroutine_function, args):
        self._args = args
        self._addref_args()
        self._task = asyncio.get_event_loop().create_task(coroutine_function(*args))
        self._task.add_done_callback(self._done_callback)
        self.background_tasks.add(self)

    def _done_callback(self, task):
        self._release_args()
        self.background_tasks.discard(self)

    def _addref_args(self):
        for obj in self._args:
            if isinstance(obj, IUnknown):
                obj.AddRef()

    def _release_args(self):
        for obj in self._args:
            if isinstance(obj, IUnknown):
                obj.Release()
