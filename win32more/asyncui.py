import asyncio
import sys
import threading
from concurrent.futures import Future, ThreadPoolExecutor


class HandCrankRunner:
    def __init__(self, *, loop_factory=None):
        if loop_factory is None:
            self._loop_factory = maybe_eager_loop_factory
        else:
            self._loop_factory = loop_factory
        self._loop = None

    def __enter__(self):
        self._loop = self._loop_factory()
        self._loop.stop()
        if sys.version_info < (3, 13):
            asyncio.events._set_running_loop(self._loop)
        else:
            self._loop._run_forever_setup()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if sys.version_info < (3, 13):
            asyncio.events._set_running_loop(None)
        else:
            self._loop._run_forever_cleanup()
        self._loop.close()
        self._loop = None

    def update(self):
        self._loop._run_once()


def create_task(coro):
    try:
        executor = RunningLoopTaskExecutor()
    except RuntimeError:
        executor = ThreadPoolTaskExecutor(maybe_eager_loop_factory)
    future = executor.submit(coro)
    BackgroundTasks.add(future)
    future.add_done_callback(BackgroundTasks.discard)
    return future


def maybe_eager_loop_factory():
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

    def __init__(self, loop_factory):
        self._loop_factory = loop_factory
        self._init_thread_pool()

    @classmethod
    def _init_thread_pool(cls):
        with cls._lock:
            if cls._thread_pool is None:
                cls._thread_pool = ThreadPoolExecutor()

    def submit(self, coro):
        loop = self._loop_factory()
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
