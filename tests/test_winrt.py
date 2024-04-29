import asyncio
import unittest
from ctypes import (
    WinError,
)
from pathlib import Path

from win32more import FAILED, Int32
from win32more._winrt import SZArray, WinRT_String, _ro_get_parameterized_type_instance_iid
from win32more.Windows.Devices.Display import DisplayMonitor, DisplayMonitorDescriptorKind
from win32more.Windows.Devices.Enumeration import DeviceInformation
from win32more.Windows.Foundation import IAsyncInfo, IPropertyValue, PropertyValue, Uri
from win32more.Windows.Foundation.Collections import IVector, StringMap
from win32more.Windows.Storage import FileIO, PathIO, StorageFile
from win32more.Windows.System.Threading import ThreadPool
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

    def test_fillarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(mainloop(winrt_readlines()))
        lines = Path(__file__).read_text().splitlines()
        array = SZArray[WinRT_String](length=10)
        ivector.GetMany(0, array)
        lines10 = [s.strvalue for s in array[0:10]]
        self.assertEqual(lines10, lines[0:10])

    def test_passarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(mainloop(winrt_readlines()))
        lines = [""] * 10
        array = SZArray[WinRT_String](length=10)
        for i in range(10):
            lines[i] = str(i)
            array[i] = WinRT_String(str(i), own=False)
        ivector.ReplaceAll(array)
        lines10 = [ivector.GetAt(i) for i in range(10)]
        self.assertEqual(lines10, lines[0:10])

    def test_receivearray_param(self):
        inarray = SZArray[Int32](1, 2, 3)

        prop = PropertyValue.CreateInt32Array(inarray).as_(IPropertyValue)

        outarray = SZArray[Int32]()
        prop.GetInt32Array(outarray)

        self.assertEqual(inarray[:], outarray[:])

    def test_receivearray_return(self):
        async def winrt_get_monitor_descriptor():
            device_information_collection = await DeviceInformation.FindAllAsyncAqsFilter(
                DisplayMonitor.GetDeviceSelector()
            )
            device_information = device_information_collection.GetAt(0)
            str_property = device_information.Properties.Lookup("System.Devices.DeviceInstanceId").as_(IPropertyValue)
            display_monitor = await DisplayMonitor.FromIdAsync(str_property.GetString())
            return display_monitor.GetDescriptor(DisplayMonitorDescriptorKind.Edid)

        descriptor = asyncio.run(mainloop(winrt_get_monitor_descriptor()))
        self.assertNotEqual(len(descriptor), 0)

    def test_guid_generation_for_parameterized_types(self):
        self.assertEqual(
            str(_ro_get_parameterized_type_instance_iid(IVector[IInspectable])),
            "{b32bdca4-5e52-5b27-bc5d-d66a1a268c2a}",
        )

    def test_constructor_with_arguments(self):
        self.assertEqual(Uri("http://example.com/").ToString(), "http://example.com/")

    def test_async_error(self):
        async def main():
            with self.assertRaises(OSError):
                await PathIO.ReadLinesAsync("NOT EXIST")

        asyncio.run(mainloop(main()))

    def test_async_cancel(self):
        def worker(async_action):
            async_action.as_(IAsyncInfo).Cancel()

        async def main():
            with self.assertRaises(asyncio.CancelledError):
                await ThreadPool.RunAsync(worker)

        asyncio.run(mainloop(main()))
