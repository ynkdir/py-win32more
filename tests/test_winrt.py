import asyncio
import sys
import unittest
from concurrent.futures import Future
from pathlib import Path
from typing import Generic, TypeVar

from win32more import (
    FAILED,
    POINTER,
    WINFUNCTYPE,
    Byte,
    Enum,
    Guid,
    Int32,
    UInt32,
    VoidPtr,
    WinError,
    cast,
    pointer,
)
from win32more.winrt import (
    ComClass,
    ComError,
    MulticastDelegateImpl,
    PassArray,
    ReceiveArray,
    WinRT_String,
    box_value,
    unbox_value,
    winrt_commethod,
)
from win32more.winrt.vector import Vector
from win32more.winrt.base import _ro_get_parameterized_type_instance_iid
from win32more.Windows.Data.Json import JsonObject, JsonValue
from win32more.Windows.Data.Xml.Dom import XmlDocument
from win32more.Windows.Devices.Display import DisplayMonitor
from win32more.Windows.Devices.Enumeration import DeviceInformation
from win32more.Windows.Foundation import IAsyncInfo, IPropertyValue, PropertyValue, Uri
from win32more.Windows.Foundation.Collections import IVector, IVectorView, StringMap
from win32more.Windows.Storage import FileIO, PathIO, StorageFile
from win32more.Windows.System import DispatcherQueueController
from win32more.Windows.System.Threading import ThreadPool
from win32more.Windows.Win32.Foundation import HRESULT, S_OK
from win32more.Windows.Win32.System.Com import CoTaskMemAlloc, IUnknown
from win32more.Windows.Win32.System.WinRT import RO_INIT_MULTITHREADED, IInspectable, RoInitialize, RoUninitialize

if sys.platform == "cygwin":
    from win32more.win32.cygwin import posix_to_win
else:

    def posix_to_win(path):
        return path


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
            storage_file = await StorageFile.GetFileFromPathAsync(posix_to_win(__file__))
            return await FileIO.ReadTextAsync(storage_file)

        text1 = asyncio.run(winrt_readfile())
        # >=3.13: text2 = Path(__file__).read_text(newline="")
        text2 = Path(__file__).read_bytes().decode("utf-8")
        self.assertEqual(text1, text2)

    def test_readfile2(self):
        async def winrt_readfile():
            return await PathIO.ReadTextAsync(posix_to_win(__file__))

        text1 = asyncio.run(winrt_readfile())
        # git clone might change eol format.
        # >=3.13: text2 = Path(__file__).read_text(newline="")
        text2 = Path(__file__).read_bytes().decode("utf-8")
        self.assertEqual(text1, text2)

    def test_fillarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(posix_to_win(__file__))

        ivector = asyncio.run(winrt_readlines())
        lines = Path(__file__).read_text().splitlines()
        lines10 = [None] * 10  # FillArray ignores contents
        ivector.GetMany(0, lines10)
        self.assertEqual(lines10, lines[0:10])

    def test_passarray(self):
        async def winrt_readlines():
            return await PathIO.ReadLinesAsync(posix_to_win(__file__))

        ivector = asyncio.run(winrt_readlines())
        lines = [str(i) for i in range(10)]
        ivector.ReplaceAll(lines)
        lines10 = [ivector.GetAt(i) for i in range(10)]
        self.assertEqual(lines10, lines[0:10])

    def test_passarray_convert_hstring_to_str(self):
        class IMock(IInspectable):
            _classid_ = "IMock"
            _iid_ = Guid("{00000000-0000-0000-0000-000000000000}")

            @winrt_commethod(6)
            def f(self, p: PassArray[WinRT_String]) -> WinRT_String: ...

        class Mock(ComClass, IMock):
            def f(self, p: list[str]) -> str:
                return p[0]

        mock = Mock().as_(IMock)

        # winrt call: mock.f(["str"]) -> WinrtMethod([hstring])
        # winrt callback: vtbl.f([hstring]) -> Mock.f(["str"])
        self.assertEqual(mock.f(["hello"]), "hello")

    def test_passarray_callback_simple_cdata(self):
        class IMock(IInspectable):
            _classid_ = "IMock"
            _iid_ = Guid("{00000000-0000-0000-0000-000000000000}")

            @winrt_commethod(6)
            def f(self, p: PassArray[Int32]) -> WinRT_String: ...

        class Mock(ComClass, IMock):
            def f(self, p: list[str]) -> str:
                return str(p)

        mock = Mock().as_(IMock)

        self.assertEqual(mock.f([1, 2, 3]), "[1, 2, 3]")

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
        # Use mock for portability.

        @WINFUNCTYPE(HRESULT, VoidPtr, UInt32, POINTER(UInt32), POINTER(POINTER(Byte)))
        def GetArrayMock(this, n, return_length, return_):
            return_length[0] = 1
            return_[0] = cast(CoTaskMemAlloc(1), POINTER(Byte))
            return_[0][0] = n
            return S_OK

        this = pointer(pointer(GetArrayMock))

        @winrt_commethod(0)
        def GetArray(self, n: UInt32) -> ReceiveArray[Byte]: ...

        r = GetArray(this, 42)
        self.assertEqual(r, [42])

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

    def test_multicastdelegate_must_support_IAgileObject(self):
        def f():
            future.set_result(42)

        future = Future()

        controller = DispatcherQueueController.CreateOnDedicatedThread()
        dispatcher = controller.DispatcherQueue

        # For non IAgileObject
        # OSError: [WinError -2147483620] The object must support the IAgileObject interface
        dispatcher.TryEnqueue(f)

        self.assertEqual(future.result(), 42)

    def test_async_callback_calls_addref_and_release_of_comobject(self):
        @WINFUNCTYPE(UInt32, VoidPtr)
        def AddRef(this):
            trace.append("AddRef")
            return 1

        @WINFUNCTYPE(UInt32, VoidPtr)
        def Release(this):
            trace.append("Release")
            return 0

        mock = cast(pointer(pointer((VoidPtr * 3)(None, cast(AddRef, VoidPtr), cast(Release, VoidPtr)))), IUnknown)

        async def callback(o, f):
            trace.append("worker")
            f.set_result(0)

        async def main():
            delegate = MulticastDelegateImpl(IUnknown, callback)
            future = asyncio.get_running_loop().create_future()
            delegate.Invoke(mock, future)
            await future

        trace = []

        asyncio.run(main())

        self.assertEqual(trace, ["AddRef", "worker", "Release"])

    def test_enum_value_will_be_returned_as_int(self):
        class E(Enum, Int32):
            A = 42

        T = TypeVar("T")

        class IMock(Generic[T], IInspectable):
            _classid_ = "IMockT"
            _piid_ = Guid("{00000000-0000-0000-0000-000000000000}")

            @winrt_commethod(6)
            def f(self) -> E: ...

            @winrt_commethod(7)
            def g(self) -> T: ...

        class Mock(ComClass, IMock[E]):
            def f(self) -> E:
                return E.A

            def g(self) -> E:
                return E.A

        mock = Mock().as_(IMock[E])

        self.assertEqual(mock.f(), E.A)
        self.assertEqual(mock.g(), E.A)

    def test_null_com_pointer_will_be_returned_as_none(self):
        class IMock(IInspectable):
            _classid_ = "IMock"
            _iid_ = Guid("{00000000-0000-0000-0000-000000000000}")

            @winrt_commethod(6)
            def f(self) -> IInspectable: ...

        class Mock(ComClass, IMock):
            def f(self) -> IInspectable:
                return None

        mock = Mock().as_(IMock)

        self.assertIsNone(mock.f())

    def test_restricted_error_info(self):
        with self.assertRaises(ComError) as cm:
            Uri("bad")

        self.assertEqual(cm.exception._error_info["restricted_description"], "bad is not a valid absolute URI.")

    def test_restricted_error_info_async(self):
        async def main():
            with self.assertRaises(ComError) as cm:
                await StorageFile.GetFileFromPathAsync("bad")

            # FIXME:
            # On my PC: The specified path (UNABLE_TO_MASK_PATH) is too long. It exceeds the maximum length of 1888614568.
            # On github runner: The specified path (bad) is not an absolute path, and relative paths are not permitted.
            #self.assertRegex(cm.exception._error_info["restricted_description"], r"It exceeds the maximum length")

            self.assertEqual(cm.exception._error_info["description"], "The parameter is incorrect.")

        asyncio.run(main())

    @unittest.skip("faulthandler shows stacktrace for 'Windows fatal exception' which might not be user space error.")
    def test_error_info(self):
        # import faulthandler
        # faulthandler.disable()

        with self.assertRaises(ComError) as cm:
            XmlDocument().LoadXml("bad")

        self.assertEqual(cm.exception._error_info["description"], "Invalid at the top level of the document.")


if __name__ == "__main__":
    unittest.main()
