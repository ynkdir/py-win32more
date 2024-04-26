import asyncio
import unittest
from ctypes import (
    WinError,
)
from pathlib import Path

from win32more import FAILED
from win32more._winrt import SZArray, WinRT_String, _ro_get_parameterized_type_instance_iid
from win32more.Windows.Foundation import Uri
from win32more.Windows.Foundation.Collections import IVector, StringMap
from win32more.Windows.Storage import FileIO, PathIO, StorageFile
from win32more.Windows.Win32.Foundation import WAIT_FAILED, WAIT_TIMEOUT
from win32more.Windows.Win32.System.WinRT import RO_INIT_SINGLETHREADED, IInspectable, RoInitialize, RoUninitialize
from win32more.Windows.Win32.UI.WindowsAndMessaging import (
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
            # for com messages remains.
            while wait_message(100):
                pump_message()
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

    def test_stringmap(self):
        m = StringMap.CreateInstance()

        m.Insert("key1", "value1")
        self.assertEqual(m.Lookup("key1"), "value1")

        m.Insert("key2", "value2")
        self.assertEqual(m.Lookup("key2"), "value2")

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

    def test_szarray_out(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(mainloop(winrt_readlines()))
        lines = Path(__file__).read_text().splitlines()
        array = SZArray[WinRT_String]((WinRT_String * 10)())
        ivector.GetMany(0, array)
        lines10 = [s.strvalue for s in array[0:10]]
        self.assertEqual(lines10, lines[0:10])

    def test_szarray_in(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(mainloop(winrt_readlines()))
        lines = [""] * 10
        array = SZArray[WinRT_String]((WinRT_String * 10)())
        for i in range(10):
            lines[i] = str(i)
            array[i] = WinRT_String(str(i), own=False)
        ivector.ReplaceAll(array)
        lines10 = [ivector.GetAt(i) for i in range(10)]
        self.assertEqual(lines10, lines[0:10])

    def test_guid_generation_for_parameterized_types(self):
        self.assertEqual(
            str(_ro_get_parameterized_type_instance_iid(IVector[IInspectable])),
            "{b32bdca4-5e52-5b27-bc5d-d66a1a268c2a}",
        )

    def test_constructor_with_arguments(self):
        self.assertEqual(Uri("http://example.com/").ToString(), "http://example.com/")
