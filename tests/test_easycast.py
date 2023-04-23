import unittest
from ctypes import (
    CFUNCTYPE,
    POINTER,
    addressof,
    c_void_p,
    c_wchar_p,
    cast,
    py_object,
    wstring_at,
)

from Windows import ForeignFunction, Int16, UInt16


def functype(prototype):
    def factory(name, types, params):
        return CFUNCTYPE(*types)(prototype)

    return ForeignFunction(prototype, factory)


def to_intptr(p):
    return cast(p, c_void_p).value


class TestEasyCast(unittest.TestCase):
    def test_str_to_pointer_int16(self):
        @functype
        def f(p: POINTER(Int16)) -> py_object:
            return p, wstring_at(to_intptr(p))

        p, s = f("abcdefg")
        self.assertIsInstance(p, POINTER(Int16))
        self.assertEqual(s, "abcdefg")

    def test_str_to_pointer_uint16(self):
        @functype
        def f(p: POINTER(UInt16)) -> py_object:
            return p, wstring_at(to_intptr(p))

        p, s = f("abcdefg")
        self.assertIsInstance(p, POINTER(UInt16))
        self.assertEqual(s, "abcdefg")

    def test_c_wchar_p_to_pointer_int16(self):
        @functype
        def f(p: POINTER(Int16)) -> py_object:
            return p

        s = c_wchar_p("abcdefg")
        p = f(s)
        self.assertIsInstance(p, POINTER(Int16))
        self.assertEqual(to_intptr(p), to_intptr(s))

    def test_c_wchar_p_to_pointer_uint16(self):
        @functype
        def f(p: POINTER(UInt16)) -> py_object:
            return p

        s = c_wchar_p("abcdefg")
        p = f(s)
        self.assertIsInstance(p, POINTER(UInt16))
        self.assertEqual(to_intptr(p), to_intptr(s))

    def test_c_wchar_p_to_pointer_pointer_int16(self):
        @functype
        def f(p: POINTER(POINTER(Int16))) -> py_object:
            return p

        s = c_wchar_p("abcdefg")
        p = f(s)
        self.assertIsInstance(p, POINTER(POINTER(Int16)))
        self.assertEqual(to_intptr(p), addressof(s))

    def test_c_wchar_p_to_pointer_pointer_uint16(self):
        @functype
        def f(p: POINTER(POINTER(UInt16))) -> py_object:
            return p

        s = c_wchar_p("abcdefg")
        p = f(s)
        self.assertIsInstance(p, POINTER(POINTER(UInt16)))
        self.assertEqual(to_intptr(p), addressof(s))


if __name__ == "__main__":
    unittest.main()
