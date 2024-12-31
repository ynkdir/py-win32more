import asyncio
import sys
import threading
import unittest

from win32more import asyncui


class TestAsyncui(unittest.TestCase):
    def test_task_will_start_in_current_running_loop(self):
        async def f():
            trace.append(2)
            await asyncio.sleep(0)
            trace.append(4)

        async def main():
            trace.append(1)
            future = asyncui.create_task(f())
            trace.append(3)
            await asyncio.sleep(0)
            trace.append(5)
            await future

        trace = []

        if sys.version_info >= (3, 12):
            expected = [1, 2, 3, 4, 5]
            asyncio.run(main(), loop_factory=asyncui.maybe_eager_loop_factory)
        else:
            expected = [1, 3, 2, 5, 4]
            asyncio.run(main())

        self.assertEqual(trace, expected)

    def test_task_will_start_eagerly_and_continue_in_background_thread(self):
        async def f():
            asyncio.current_task().add_done_callback(lambda _: event.set())
            trace.append(threading.get_ident())  # <- caller's thread
            await asyncio.sleep(0)
            trace.append(threading.get_ident())  # <- background thread

        trace = []
        event = threading.Event()
        asyncui.create_task(f())
        self.assertTrue(event.wait(5))
        self.assertEqual(trace[0], threading.get_ident())
        self.assertNotEqual(trace[1], threading.get_ident())

    def test_task_will_start_eagerly_and_dont_start_thread_when_task_was_done(self):
        async def f():
            asyncio.current_task().add_done_callback(lambda _: trace.append((2, threading.get_ident())))
            asyncio.current_task().add_done_callback(lambda _: event.set())
            trace.append((1, threading.get_ident()))

        trace = []
        event = threading.Event()
        asyncui.create_task(f())
        self.assertTrue(event.wait(5))
        self.assertEqual(trace[0], (1, threading.get_ident()))
        self.assertEqual(trace[1], (2, threading.get_ident()))


if __name__ == "__main__":
    unittest.main()
