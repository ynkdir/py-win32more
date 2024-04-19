import unittest
from ctypes import (
    CFUNCTYPE,
    POINTER,
    addressof,
    c_char,
    c_void_p,
    c_wchar_p,
    cast,
    py_object,
    wstring_at,
)

from win32more import (
    EasyCastStructure,
    ForeignFunction,
    Int16,
    UInt16,
    Void,
    cfunctype_pointer,
    winfunctype_pointer,
)


def commit(prototype):
    return prototype.__commit__()


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

    # default behavior of ctypes
    def test_function_array_to_c_void_p(self):
        @functype
        def f(p: c_void_p) -> py_object:
            return p

        a = (c_char * 1)()
        p = f(a)
        self.assertIsInstance(p, int)
        self.assertEqual(p, addressof(a))

    def test_struct_array_to_c_void_p(self):
        @commit
        class S(EasyCastStructure):
            p: c_void_p

        a = (c_char * 1)()
        s = S()
        s.p = a
        self.assertIsInstance(s.p, int)
        self.assertEqual(s.p, addressof(a))

    def test_callable_to_cfunctype(self):
        @commit
        @cfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        def h():
            pass

        r = g(h)
        self.assertTrue(bool(r))

        r = g(lambda: None)
        self.assertTrue(bool(r))

    def test_callable_to_winfunctype(self):
        @commit
        @winfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        def h():
            pass

        r = g(h)
        self.assertTrue(bool(r))

        r = g(lambda: None)
        self.assertTrue(bool(r))

    def test_none_to_cfunctype(self):
        @commit
        @cfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        r = g(None)
        self.assertFalse(bool(r))

    def test_none_to_winfunctype(self):
        @commit
        @winfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        r = g(None)
        self.assertFalse(bool(r))

    def test_cfunctype_is_not_converted(self):
        @commit
        @cfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        h = f(lambda: 0)
        r = g(h)
        self.assertEqual(cast(r, c_void_p).value, cast(h, c_void_p).value)

    def test_winfunctype_is_not_converted(self):
        @commit
        @winfunctype_pointer
        def f() -> Void:
            ...

        @functype
        def g(f: f) -> py_object:
            return f

        h = f(lambda: 0)
        r = g(h)
        self.assertEqual(cast(r, c_void_p).value, cast(h, c_void_p).value)

    def test_converted_function_pointer_remains_after_it_is_passed_to_c_function(self):
        @commit
        @cfunctype_pointer
        def f() -> Int16:
            ...

        in_c_callback = None

        @functype
        def g(callback: f) -> Void:
            # emulate that C function receives function pointer insted of python object.
            nonlocal in_c_callback
            in_c_callback = cast(callback, c_void_p).value

        @functype
        def h() -> Int16:
            callback = cast(in_c_callback, f)
            return callback()

        g(lambda: 99)
        r = h()
        self.assertEqual(r, 99)


if __name__ == "__main__":
    unittest.main()
