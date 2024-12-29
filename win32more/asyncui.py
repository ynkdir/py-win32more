import asyncio
import sys
import threading
from concurrent.futures import Future, ThreadPoolExecutor

from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer


# Asyncio runner for Windows message loop.
def async_start_runner(delay_ms=100):
    def timer_proc(*args):
        loop._run_once()

    loop = _loop_factory()
    loop.stop()
    loop._run_forever_setup()
    SetTimer(0, 0, delay_ms, timer_proc)


def async_callback(coroutine_function):
    def wrapper(*args):
        _addref(args)
        try:
            executor = RunningLoopTaskExecutor()
        except RuntimeError:
            executor = ThreadPoolTaskExecutor()
        future = executor.submit(coroutine_function(*args))
        future.add_done_callback(lambda _: _release(args))
        BackgroundTasks.add(future)
        future.add_done_callback(BackgroundTasks.discard)

    return wrapper


def _addref(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.AddRef()


def _release(args):
    for obj in args:
        if isinstance(obj, IUnknown) and obj.value:
            obj.Release()


def _loop_factory():
    loop = asyncio.new_event_loop()
    # Use eager task.
    # Some method can not be called after returned.
    # (e.g. CoreWebView2NewWindowRequestedEventArgs.GetDeferral())
    if sys.version_info >= (3, 12):
        loop.set_task_factory(asyncio.eager_task_factory)
    return loop


# keep reference to tasks
class BackgroundTasks:
    _tasks = set()
    _lock = threading.Lock()

    @classmethod
    def add(cls, task):
        with cls._lock:
            cls._tasks.add(task)

    @classmethod
    def discard(cls, task):
        with cls._lock:
            cls._tasks.discard(task)


class RunningLoopTaskExecutor:
    def __init__(self):
        self._loop = asyncio.get_running_loop()

    def submit(self, coro):
        return self._loop.create_task(coro)


class ThreadPoolTaskExecutor:
    _thread_pool = None
    _lock = threading.Lock()

    def __init__(self):
        self._init_thread_pool()

    @classmethod
    def _init_thread_pool(cls):
        with cls._lock:
            if cls._thread_pool is None:
                cls._thread_pool = ThreadPoolExecutor()

    def submit(self, coro):
        loop = _loop_factory()
        # Run task in current thread context until first await.
        # eager_task_factory doesn't start task eagerly when loop is not running.
        task = loop.create_task(coro)
        loop.stop()
        loop.run_forever()
        if task.done():
            loop.run_until_complete(task)  # ensure calling done callback
            future = Future()
            future.set_result(task.result())
            return future
        # continue in background thread
        return self._thread_pool.submit(loop.run_until_complete, task)
