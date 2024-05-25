import unittest
from ctypes import CFUNCTYPE, Structure, c_char_p, c_void_p, c_wchar_p, py_object


class TestCtypes(unittest.TestCase):
    def test_function_c_void_p(self):
        @CFUNCTYPE(py_object, c_void_p)
        def f(x):
            return x

        @CFUNCTYPE(py_object, c_void_p)
        def g(x):
            return c_wchar_p(x).value

        @CFUNCTYPE(py_object, c_void_p)
        def h(x):
            return c_char_p(x).value

        x = f(42)
        self.assertIsInstance(x, int)
        self.assertEqual(x, 42)

        # str -> c_wchar_p -> int value of pointer address
        x = f("str")
        self.assertIsInstance(x, int)
        self.assertEqual(g("str"), "str")

        # bytes -> c_char_p -> int value of pointer address
        x = f(b"bytes")
        self.assertIsInstance(x, int)
        self.assertEqual(h(b"bytes"), b"bytes")

    def test_struct_c_void_p(self):
        class S(Structure):
            _fields_ = [("x", c_void_p)]

        s = S()

        s.x = 42
        self.assertIsInstance(s.x, int)
        self.assertEqual(s.x, 42)

        with self.assertRaises(TypeError):
            s.x = "str"

        with self.assertRaises(TypeError):
            s.x = b"bytes"


if __name__ == "__main__":
    unittest.main()
