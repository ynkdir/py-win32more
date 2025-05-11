import sys
import unittest
from ctypes import CFUNCTYPE, Structure, Union, c_char_p, c_void_p, c_wchar_p, py_object


class TestCtypes(unittest.TestCase):
    def test_c_void_p(self):
        @CFUNCTYPE(py_object, c_void_p)
        def f(x):
            return x

        @CFUNCTYPE(py_object, c_void_p, py_object)
        def g(x, convert):
            return convert(x)

        class S(Structure):
            _fields_ = [("x", c_void_p)]

        self.assertIsInstance(f(42), int)
        self.assertEqual(f(42), 42)

        self.assertIsNone(f(None))
        self.assertIsNone(f(0))

        # str -> c_wchar_p -> int value of pointer address
        self.assertIsInstance(f("str"), int)
        self.assertEqual(g("str", lambda x: c_wchar_p(x).value), "str")

        # bytes -> c_char_p -> int value of pointer address
        self.assertIsInstance(f(b"bytes"), int)
        self.assertEqual(g(b"bytes", lambda x: c_char_p(x).value), b"bytes")

        s = S()

        s.x = 42
        self.assertIsInstance(s.x, int)
        self.assertEqual(s.x, 42)

        s.x = None
        self.assertIsNone(s.x)

        s.x = 0
        self.assertIsNone(s.x)

        with self.assertRaises(TypeError):
            s.x = "str"

        with self.assertRaises(TypeError):
            s.x = b"bytes"

    # hasattr(Union, "_fields_") returns False,
    # when it has been called before setting _fields_,
    # Fixed by https://github.com/python/cpython/commit/5a1618a2c8c108b8c73aa9459b63f0dbd66b60f6
    @unittest.skipIf(sys.version_info < (3, 13), "doesn't work until 3.13")
    def test_union_hasattr_fields_works(self):
        class U(Union):
            pass

        self.assertFalse(hasattr(U, "_fields_"))

        U._fields_ = [("x", c_void_p)]

        self.assertTrue(hasattr(U, "_fields_"))


if __name__ == "__main__":
    unittest.main()
