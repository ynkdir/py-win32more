import asyncio
import unittest
from ctypes import (
    WinError,
)
from pathlib import Path

from Windows import FAILED
from Windows.Storage import FileIO, PathIO, StorageFile
from Windows.Win32.Foundation import WAIT_FAILED, WAIT_TIMEOUT
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)
from Windows.Win32.UI.WindowsAndMessaging import (
    MSG,
    MWMO_INPUTAVAILABLE,
    PM_REMOVE,
    QS_ALLINPUT,
    DispatchMessageW,
    MsgWaitForMultipleObjectsEx,
    PeekMessageW,
    TranslateMessage,
)


def wait_message(timeout):
    r = MsgWaitForMultipleObjectsEx(0, None, timeout, QS_ALLINPUT, MWMO_INPUTAVAILABLE)
    if r == WAIT_FAILED:
        raise WinError()
    elif r == WAIT_TIMEOUT:
        return False
    return True


def pump_message():
    msg = MSG()
    while PeekMessageW(msg, 0, 0, 0, PM_REMOVE) != 0:
        TranslateMessage(msg)
        DispatchMessageW(msg)


async def mainloop(coro):
    task = asyncio.create_task(coro)
    while True:
        await asyncio.sleep(0)
        if task.done():
            pump_message()  # for com messages remains.
            return task.result()
        if wait_message(0):
            pump_message()
            continue
        wait_message(100)
        pump_message()


class TestWinrt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)

    @classmethod
    def tearDownClass(cls):
        RoUninitialize()

    def test_readfile(self):
        async def winrt_readfile():
            storage_file = await StorageFile.GetFileFromPathAsync(__file__)
            return await FileIO.ReadTextAsync(storage_file)

        text1 = asyncio.run(mainloop(winrt_readfile()))
        text2 = Path(__file__).read_text()
        self.assertEqual(text1, text2)

    def test_readfile2(self):
        async def winrt_readfile():
            return await PathIO.ReadTextAsync(__file__)

        text1 = asyncio.run(mainloop(winrt_readfile()))
        text2 = Path(__file__).read_text()
        self.assertEqual(text1, text2)
