import asyncio
import unittest
from ctypes import (
    WinError,
    pointer,
)
from pathlib import Path

from win32more import FAILED, Int32
from win32more._winrt import _ro_get_parameterized_type_instance_iid, box_value, unbox_value
from win32more._winrtrt import Vector
from win32more.Windows.Data.Json import JsonObject, JsonValue
from win32more.Windows.Devices.Display import DisplayMonitor, DisplayMonitorDescriptorKind
from win32more.Windows.Devices.Enumeration import DeviceInformation
from win32more.Windows.Foundation import IAsyncInfo, IPropertyValue, PropertyValue, Uri
from win32more.Windows.Foundation.Collections import IVector, IVectorView, StringMap
from win32more.Windows.Storage import FileIO, PathIO, StorageFile
from win32more.Windows.System.Threading import ThreadPool
from win32more.Windows.Win32.Foundation import S_OK
from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.System.WinRT import RO_INIT_MULTITHREADED, IInspectable, RoInitialize, RoUninitialize


class TestWinrt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        hr = RoInitialize(RO_INIT_MULTITHREADED)
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

        self.assertEqual(set(m.items()), {("key1", "value1"), ("key2", "value2")})

    def test_readfile(self):
        async def winrt_readfile():
            storage_file = await StorageFile.GetFileFromPathAsync(__file__)
            return await FileIO.ReadTextAsync(storage_file)

        text1 = asyncio.run(winrt_readfile())
        text2 = Path(__file__).read_text()
        self.assertEqual(text1, text2)

    def test_readfile2(self):
        async def winrt_readfile():
            return await PathIO.ReadTextAsync(__file__)

        text1 = asyncio.run(winrt_readfile())
        text2 = Path(__file__).read_text()
        self.assertEqual(text1, text2)

    def test_fillarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(winrt_readlines())
        lines = Path(__file__).read_text().splitlines()
        lines10 = [None] * 10  # FillArray ignores contents
        ivector.GetMany(0, lines10)
        self.assertEqual(lines10, lines[0:10])

    def test_passarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(__file__)

        ivector = asyncio.run(winrt_readlines())
        lines = [str(i) for i in range(10)]
        ivector.ReplaceAll(lines)
        lines10 = [ivector.GetAt(i) for i in range(10)]
        self.assertEqual(lines10, lines[0:10])

    def test_receivearray_param(self):
        inarray = [1, 2, 3]

        prop = PropertyValue.CreateInt32Array(inarray).as_(IPropertyValue)

        outarray = []
        prop.GetInt32Array(outarray)

        self.assertEqual(inarray, outarray)

    def test_receivearray_string_param(self):
        inarray = ["a", "b", "c"]

        prop = PropertyValue.CreateStringArray(inarray).as_(IPropertyValue)

        outarray = []
        prop.GetStringArray(outarray)

        self.assertEqual(inarray, outarray)

    def test_receivearray_object_param(self):
        obj = StringMap()
        inarray = [obj]

        prop = PropertyValue.CreateInspectableArray(inarray).as_(IPropertyValue)

        outarray = []
        prop.GetInspectableArray(outarray)

        self.assertEqual(obj.as_(IInspectable).value, outarray[0].value)

    def test_receivearray_return(self):
        async def winrt_get_monitor_descriptor():
            device_information_collection = await DeviceInformation.FindAllAsyncAqsFilter(
                DisplayMonitor.GetDeviceSelector()
            )
            device_information = device_information_collection.GetAt(0)
            str_property = device_information.Properties.Lookup("System.Devices.DeviceInstanceId").as_(IPropertyValue)
            display_monitor = await DisplayMonitor.FromIdAsync(str_property.GetString())
            return display_monitor.GetDescriptor(DisplayMonitorDescriptorKind.Edid)

        descriptor = asyncio.run(winrt_get_monitor_descriptor())
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

        asyncio.run(main())

    def test_async_cancel(self):
        def worker(async_action):
            async_action.as_(IAsyncInfo).Cancel()

        async def main():
            with self.assertRaises(asyncio.CancelledError):
                await ThreadPool.RunAsync(worker)

        asyncio.run(main())

    def test_box_value(self):
        self.assertIsInstance(box_value("str"), IInspectable)
        self.assertEqual(unbox_value(box_value("str")), "str")
        self.assertEqual(box_value("str").as_(str), "str")

        with self.assertRaises(OSError):  # E_NOINTERFACE
            unbox_value(StringMap.CreateInstance())

        with self.assertRaises(AttributeError):  # 'str' object has not attribute 'as_'
            unbox_value("non com object")

    def test_vector(self):
        v = Vector[Int32]([0, 1, 2])

        self.assertEqual(v.GetAt(0), 0)
        self.assertEqual(v.GetAt(1), 1)
        self.assertEqual(v.GetAt(2), 2)

        r = [None] * 3
        v.GetMany(0, r)
        self.assertEqual(r, [0, 1, 2])

    def test_sequence_protocol(self):
        async def device_information_find_all():
            return await DeviceInformation.FindAllAsyncAqsFilter(DisplayMonitor.GetDeviceSelector())

        device_information_collection = asyncio.run(device_information_find_all())

        self.assertNotEqual(len(device_information_collection), 0)

        iterator_succeeded = False
        for device_information in device_information_collection:
            self.assertIsInstance(device_information, DeviceInformation)
            iterator_succeeded = True
            break

        self.assertTrue(iterator_succeeded)

        self.assertEqual(
            device_information_collection[-1], device_information_collection[len(device_information_collection) - 1]
        )
        self.assertEqual(device_information_collection[0:1], [device_information_collection[0]])
        self.assertEqual(device_information_collection[0:1:1], [device_information_collection[0]])

    def test_mapping_protocol(self):
        json = JsonObject()
        json.SetNamedValue("name1", JsonValue.CreateStringValue("value1"))

        iterator_succeeded = False
        for key in json.GetView():
            self.assertEqual(key, "name1")
            self.assertEqual(json[key].GetString(), "value1")
            iterator_succeeded = True
            break

        self.assertTrue(iterator_succeeded)

    def test_comclass_handle_inherited_interfaces(self):
        v = Vector[Int32]([0, 1, 2])
        o = IInspectable()
        self.assertEqual(v.QueryInterface(pointer(IUnknown._iid_), pointer(o)), S_OK)
        self.assertEqual(v.QueryInterface(pointer(IInspectable._iid_), pointer(o)), S_OK)
        self.assertEqual(v.QueryInterface(pointer(IVector._iid_), pointer(o)), S_OK)
        self.assertEqual(v.QueryInterface(pointer(IVectorView._iid_), pointer(o)), S_OK)
