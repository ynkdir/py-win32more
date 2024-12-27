import asyncio
import sys
import threading
import unittest

from win32more.asyncui import async_callback


class TestAsyncui(unittest.TestCase):
    @unittest.skipIf(sys.version_info < (3, 12), "eager task is not supported")
    def test_task_will_start_in_current_running_loop(self):
        @async_callback
        async def f():
            trace.append(2)
            await asyncio.sleep(0)
            trace.append(4)

        async def main():
            trace.append(1)
            f()
            trace.append(3)
            await asyncio.sleep(0)
            trace.append(5)

        trace = []
        asyncio.run(main())

        self.assertEqual(trace, [1, 2, 3, 4, 5])

    def test_task_will_start_eagerly_and_continue_in_background_thread(self):
        @async_callback
        async def f():
            asyncio.current_task().add_done_callback(lambda _: event.set())
            trace.append(threading.get_ident())  # <- caller's thread
            await asyncio.sleep(0)
            trace.append(threading.get_ident())  # <- background thread

        trace = []
        event = threading.Event()
        f()
        self.assertTrue(event.wait(5))
        self.assertEqual(trace[0], threading.get_ident())
        self.assertNotEqual(trace[1], threading.get_ident())

    def test_task_will_start_eagerly_and_dont_start_thread_when_task_was_done(self):
        @async_callback
        async def f():
            asyncio.current_task().add_done_callback(lambda _: event.set())
            asyncio.current_task().add_done_callback(lambda _: trace.append((2, threading.get_ident())))
            trace.append((1, threading.get_ident()))

        trace = []
        event = threading.Event()
        f()
        self.assertTrue(event.wait(5))
        self.assertEqual(trace[0], (1, threading.get_ident()))
        self.assertEqual(trace[1], (2, threading.get_ident()))


if __name__ == "__main__":
    unittest.main()
