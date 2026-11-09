import os
import sys
import unittest
from ctypes import POINTER, c_uint32, c_wchar, sizeof, wstring_at

from win32more import ComClass, Guid, Int32
from win32more._posix import (
    CoTaskMemAlloc,
    CoTaskMemFree,
    LibraryLoader,
    SysAllocStringLen,
    SysFreeString,
    SysStringLen,
)
from win32more._win32 import commethod
from win32more._win32api import HRESULT, IUnknown

POSIX = sys.platform not in ("win32", "cygwin")


class ICalc(IUnknown):
    _iid_ = Guid("{5b3f1d52-9f47-4bd8-9a3f-0f4f3c1f2e10}")

    @commethod(3)
    def Add(self, a: Int32, b: Int32, result: POINTER(Int32)) -> HRESULT: ...


class INotImplemented(IUnknown):
    _iid_ = Guid("{5b3f1d52-9f47-4bd8-9a3f-0f4f3c1f2e11}")


class Calc(ComClass, ICalc):
    def Add(self, a, b, result):
        result[0] = a + b
        return 0


class TestVtableCall(unittest.TestCase):
    def test_call_python_com_object_through_vtable(self):
        calc = Calc().as_(ICalc)
        result = Int32()
        self.assertEqual(calc.Add(2, 3, result), 0)
        self.assertEqual(result.value, 5)

    def test_query_interface(self):
        calc = Calc().as_(ICalc)
        self.assertIsNotNone(calc.try_as(IUnknown))
        self.assertIsNone(calc.try_as(INotImplemented))


class TestLibraryLoader(unittest.TestCase):
    def test_candidates(self):
        candidates = LibraryLoader().candidates("dxcompiler.dll")
        self.assertEqual(candidates[-1], "libdxcompiler.so")
        if sys.platform == "darwin":
            self.assertEqual(candidates[0], "libdxcompiler.dylib")

    def test_register_library_takes_precedence(self):
        windll = LibraryLoader()
        windll.register_library("DXCOMPILER.dll", "/opt/dxc/lib/libdxcompiler.so")
        self.assertEqual(windll.candidates("dxcompiler.dll"), ["/opt/dxc/lib/libdxcompiler.so"])

    def test_missing_library_raises(self):
        with self.assertRaises(OSError):
            LibraryLoader()["win32more_no_such_library.dll"]


class TestDxcMemoryLayout(unittest.TestCase):
    def test_bstr_layout_with_non_bmp_text(self):
        s = "abc é\U0001f642"
        units = len(s) if sizeof(c_wchar) == 4 else len(s.encode("utf-16-le")) // 2
        p = SysAllocStringLen(s, units, _as_intptr=True)
        try:
            self.assertEqual(c_uint32.from_address(p - 4).value, units * sizeof(c_wchar))
            self.assertEqual(wstring_at(p, units), s)
            self.assertEqual(c_wchar.from_address(p + units * sizeof(c_wchar)).value, "\0")
            self.assertEqual(SysStringLen(p), units)
        finally:
            SysFreeString(p)

    def test_bstr_without_text_is_zero_filled(self):
        p = SysAllocStringLen(None, 3, _as_intptr=True)
        try:
            self.assertEqual(SysStringLen(p), 3)
            self.assertEqual(wstring_at(p, 3), "\0\0\0")
        finally:
            SysFreeString(p)

    def test_null(self):
        self.assertEqual(SysStringLen(None), 0)
        SysFreeString(None)
        CoTaskMemFree(None)

    def test_cotaskmem(self):
        p = CoTaskMemAlloc(16)
        self.assertIsInstance(p, int)
        CoTaskMemFree(p)


@unittest.skipUnless(POSIX, "posix backend only")
class TestPosixBackend(unittest.TestCase):
    def test_bstr_round_trip_with_non_bmp_text(self):
        from win32more._bstr import bstr

        s = "abc é\U0001f642"
        b = bstr(s, own=True)
        self.assertEqual(len(b), len(s))
        self.assertEqual(str(b), s)

    def test_winerror(self):
        from win32more import WinError

        e = WinError(-2147467262)
        self.assertEqual(e.winerror, -2147467262)
        self.assertIn("0x80004002", str(e))

    def test_windll(self):
        from win32more import windll

        self.assertIsInstance(windll, LibraryLoader)


@unittest.skipUnless(POSIX and os.environ.get("DXC_LIBRARY"), "set DXC_LIBRARY to the path of libdxcompiler.so")
class TestDxc(unittest.TestCase):
    def test_create_instance(self):
        from win32more import windll
        from win32more.Windows.Win32.Graphics.Direct3D.Dxc import CLSID_DxcUtils, DxcCreateInstance, IDxcUtils

        windll.register_library("dxcompiler.dll", os.environ["DXC_LIBRARY"])
        utils = IDxcUtils(own=True)
        self.assertEqual(DxcCreateInstance(CLSID_DxcUtils, IDxcUtils._iid_, utils), 0)
        self.assertTrue(utils.value)
        self.assertIsNotNone(utils.try_as(IUnknown))
        self.assertIsNone(utils.try_as(INotImplemented))


if __name__ == "__main__":
    unittest.main()
