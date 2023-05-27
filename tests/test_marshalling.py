import unittest
from ctypes import (
    CFUNCTYPE,
    POINTER,
    WINFUNCTYPE,
    Array,
    Structure,
    c_char_p,
    c_void_p,
    c_wchar_p,
    cast,
    pointer,
    py_object,
)

from win32more import (
    Boolean,
    Char,
    Double,
    EasyCastStructure,
    ForeignFunction,
    Int32,
    UInt32,
    UIntPtr,
    commethod,
    press,
)


def functype(prototype):
    def factory(name, types, params):
        return CFUNCTYPE(*types)(prototype)

    return ForeignFunction(prototype, factory)


class TestMarshalling(unittest.TestCase):
    def test_c_void_p(self):
        @press
        class S(EasyCastStructure):
            c_void_p: c_void_p

        s = S()

        self.assertIsNone(s.c_void_p)

        s.c_void_p = False
        self.assertIsNone(s.c_void_p)

        s.c_void_p = True
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, 1)

        s.c_void_p = 0
        self.assertIsNone(s.c_void_p)

        s.c_void_p = 1234
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, 1234)

        s.c_void_p = -1
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_void_p = 0.14

        with self.assertRaises(TypeError):
            s.c_void_p = "abcdefg"

        with self.assertRaises(TypeError):
            s.c_void_p = b"abcdefg"

    def test_c_char_p(self):
        @press
        class S(EasyCastStructure):
            c_char_p: c_char_p

        s = S()

        self.assertIsNone(s.c_char_p)

        s.c_char_p = False
        self.assertIsNone(s.c_char_p)

        # Test with c_char_p_as_intptr for invalid address.
        s.c_char_p = True
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, 1)

        s.c_char_p = 0
        self.assertIsNone(s.c_char_p)

        s.c_char_p = 1234
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, 1234)

        s.c_char_p = -1
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_char_p = 0.14

        s.c_char_p = b"abcdefg"
        self.assertIsInstance(s.c_char_p, bytes)
        self.assertEqual(s.c_char_p, b"abcdefg")

        with self.assertRaises(TypeError):
            s.c_char_p = "abcdefg"

        s.c_char_p = c_char_p(b"abcdefg")
        self.assertIsInstance(s.c_char_p, bytes)
        self.assertEqual(s.c_char_p, b"abcdefg")

    def test_c_wchar_p(self):
        @press
        class S(EasyCastStructure):
            c_wchar_p: c_wchar_p

        s = S()

        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = False
        self.assertIsNone(s.c_wchar_p)

        # Test with c_wchar_p_as_intptr for invalid address.
        s.c_wchar_p = True
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, 1)

        s.c_wchar_p = 0
        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = 1234
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, 1234)

        s.c_wchar_p = -1
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, UIntPtr(-1).value)

        with self.assertRaises(TypeError):
            s.c_wchar_p = 0.14

        with self.assertRaises(TypeError):
            s.c_wchar_p = b"abcdefg"

        s.c_wchar_p = "abcdefg"
        self.assertIsInstance(s.c_wchar_p, str)
        self.assertEqual(s.c_wchar_p, "abcdefg")

        s.c_wchar_p = c_wchar_p("abcdefg")
        self.assertIsInstance(s.c_wchar_p, str)
        self.assertEqual(s.c_wchar_p, "abcdefg")

    def test_boolean(self):
        @press
        class S(EasyCastStructure):
            boolean: Boolean

        s = S()

        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = False
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = True
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = 0
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, False)

        s.boolean = 1234
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = -1
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = 0.14
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = b"abcdefg"
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

        s.boolean = "abcdefg"
        self.assertIsInstance(s.boolean, bool)
        self.assertEqual(s.boolean, True)

    def test_int32(self):
        @press
        class S(EasyCastStructure):
            int32: Int32

        s = S()

        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 0
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 1234
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 1234)

        s.int32 = -1
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, -1)

        with self.assertRaises(TypeError):
            s.int32 = 0.14

        with self.assertRaises(TypeError):
            s.int32 = b"abcdefg"

        with self.assertRaises(TypeError):
            s.int32 = "abcdefg"

        s.int32 = 0x100000000
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 0)

        s.int32 = 0x100000001
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, 1)

        s.int32 = 0x1FFFFFFFF
        self.assertIsInstance(s.int32, int)
        self.assertEqual(s.int32, -1)

    def test_uint32(self):
        @press
        class S(EasyCastStructure):
            uint32: UInt32

        s = S()

        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 0
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 1234
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 1234)

        s.uint32 = -1
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0xFFFFFFFF)

        with self.assertRaises(TypeError):
            s.uint32 = 0.14

        with self.assertRaises(TypeError):
            s.uint32 = b"abcdefg"

        with self.assertRaises(TypeError):
            s.uint32 = "abcdefg"

        s.uint32 = 0x100000000
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0)

        s.uint32 = 0x100000001
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 1)

        s.uint32 = 0x1FFFFFFFF
        self.assertIsInstance(s.uint32, int)
        self.assertEqual(s.uint32, 0xFFFFFFFF)

    def test_double(self):
        @press
        class S(EasyCastStructure):
            double: Double

        s = S()

        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0)

        s.double = 0
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0)

        s.double = 1234
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 1234)

        s.double = -1
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, -1)

        s.double = 0.14
        self.assertIsInstance(s.double, float)
        self.assertEqual(s.double, 0.14)

        with self.assertRaises(TypeError):
            s.double = b"abcdefg"

        with self.assertRaises(TypeError):
            s.double = "abcdefg"

    def test_char(self):
        @press
        class S(EasyCastStructure):
            char: Char

        s = S()

        self.assertIsInstance(s.char, str)
        self.assertEqual(s.char, "\x00")

        with self.assertRaises(TypeError):
            s.char = 0

        with self.assertRaises(TypeError):
            s.char = 1234

        with self.assertRaises(TypeError):
            s.char = -1

        with self.assertRaises(TypeError):
            s.char = 0.14

        with self.assertRaises(TypeError):
            s.char = b"abcdefg"

        with self.assertRaises(TypeError):
            s.char = "abcdefg"

        s.char = "a"
        self.assertIsInstance(s.char, str)
        self.assertEqual(s.char, "a")

        with self.assertRaises(TypeError):
            s.char = b"a"

    def test_int32_array(self):
        @press
        class S(EasyCastStructure):
            int32_array_3: Int32 * 3

        s = S()

        self.assertIsInstance(s.int32_array_3, Array)
        self.assertEqual(s.int32_array_3[0], 0)
        self.assertEqual(s.int32_array_3[1], 0)
        self.assertEqual(s.int32_array_3[2], 0)
        self.assertEqual(s.int32_array_3[:], [0, 0, 0])

        s.int32_array_3 = (3, 4, 5)
        self.assertIsInstance(s.int32_array_3, Array)
        self.assertEqual(s.int32_array_3[0], 3)
        self.assertEqual(s.int32_array_3[1], 4)
        self.assertEqual(s.int32_array_3[2], 5)
        self.assertEqual(s.int32_array_3[:], [3, 4, 5])

        with self.assertRaises(TypeError):
            s.int32_array_3 = [3, 4, 5]

        with self.assertRaises(RuntimeError):
            s.int32_array_3 = (3, 4, "5")

    def test_c_void_p_array(self):
        @press
        class S(EasyCastStructure):
            c_void_p_array_3: c_void_p * 3

        s = S()

        self.assertIsInstance(s.c_void_p_array_3, Array)
        self.assertIsNone(s.c_void_p_array_3[0])
        self.assertIsNone(s.c_void_p_array_3[1])
        self.assertIsNone(s.c_void_p_array_3[2])
        self.assertEqual(s.c_void_p_array_3[:], [None, None, None])

        s.c_void_p_array_3 = (3, 4, 5)
        self.assertEqual(s.c_void_p_array_3[0], 3)
        self.assertEqual(s.c_void_p_array_3[1], 4)
        self.assertEqual(s.c_void_p_array_3[2], 5)
        self.assertEqual(s.c_void_p_array_3[:], [3, 4, 5])

        with self.assertRaises(TypeError):
            s.c_void_p_array_3 = [3, 4, 5]

        with self.assertRaises(RuntimeError):
            s.c_void_p_array_3 = (3, 4, "5")

    def test_c_wchar_p_array(self):
        @press
        class S(EasyCastStructure):
            c_wchar_p_array_3: c_wchar_p * 3

        s = S()

        self.assertIsInstance(s.c_wchar_p_array_3, Array)
        self.assertIsNone(s.c_wchar_p_array_3[0])
        self.assertIsNone(s.c_wchar_p_array_3[1])
        self.assertIsNone(s.c_wchar_p_array_3[2])
        self.assertEqual(s.c_wchar_p_array_3[:], [None, None, None])

        # Access to invalid address indirectly.
        s.c_wchar_p_array_3 = (3, 4, 5)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[0], 3)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[1], 4)
        self.assertEqual(cast(s.c_wchar_p_array_3, POINTER(c_void_p))[2], 5)

        s.c_wchar_p_array_3 = ("3", "4", "5")
        self.assertEqual(s.c_wchar_p_array_3[0], "3")
        self.assertEqual(s.c_wchar_p_array_3[1], "4")
        self.assertEqual(s.c_wchar_p_array_3[2], "5")
        self.assertEqual(s.c_wchar_p_array_3[:], ["3", "4", "5"])

    def test_function_c_void_p(self):
        @functype
        def f(x: c_void_p) -> py_object:
            return x

        x = f(0)
        self.assertIsNone(x)

        x = f(1)
        self.assertIsInstance(x, int)
        self.assertEqual(x, 1)

        x = f("a")
        self.assertIsInstance(x, int)
        # x is meory address already freed.

        @functype
        def g(x: UIntPtr) -> c_void_p:
            return x

        x = g(0)
        self.assertIsNone(x)

        x = g(1)
        self.assertIsInstance(x, int)
        self.assertEqual(x, 1)

        # @functype
        # def h() -> c_void_p:
        #     return c_void_p()
        #
        # with self.assertRaises(TypeError):
        #     h()
        # TypeError: cannot be converted to pointer

    def test_function_c_char_p(self):
        @functype
        def f(x: c_char_p) -> py_object:
            return x

        s = c_char_p(b"abcdefg")
        i = cast(s, c_void_p).value

        x = f(0)
        self.assertIsNone(x)

        x = f(s)
        self.assertIsInstance(x, bytes)
        self.assertEqual(x, s.value)

        x = f(i)
        self.assertIsInstance(x, bytes)
        self.assertEqual(x, s.value)

        x = f(b"abcdefg")
        self.assertIsInstance(x, bytes)
        self.assertEqual(x, b"abcdefg")

        @functype
        def g(x: UIntPtr) -> c_char_p:
            return x

        x = g(0)
        self.assertIsNone(x)

        x = g(i)
        self.assertIsInstance(x, bytes)
        self.assertEqual(x, s.value)

        x = g(i, _as_intptr=True)
        self.assertIsInstance(x, int)
        self.assertEqual(x, i)

        # can not catch exception
        # @functype
        # def h() -> c_char_p:
        #     return c_char_p()
        #
        # with self.assertRaises(TypeError):
        #     h()
        # TypeError: bytes or integer address expected instead of c_char_p instance

    def test_function_c_wchar_p(self):
        @functype
        def f(x: c_wchar_p) -> py_object:
            return x

        s = c_wchar_p("abcdefg")
        i = cast(s, c_void_p).value

        x = f(0)
        self.assertIsNone(x)

        x = f(s)
        self.assertIsInstance(x, str)
        self.assertEqual(x, s.value)

        x = f(i)
        self.assertIsInstance(x, str)
        self.assertEqual(x, s.value)

        x = f("abcdefg")
        self.assertIsInstance(x, str)
        self.assertEqual(x, "abcdefg")

        @functype
        def g(x: UIntPtr) -> c_wchar_p:
            return x

        x = g(0)
        self.assertIsNone(x)

        x = g(i)
        self.assertIsInstance(x, str)
        self.assertEqual(x, s.value)

        x = g(i, _as_intptr=True)
        self.assertIsInstance(x, int)
        self.assertEqual(x, i)

        # can not catch exception
        # @functype
        # def h() -> c_wchar_p:
        #     return c_wchar_p()
        #
        # with self.assertRaises(TypeError):
        #     h()
        # TypeError: unicode string or integer address expected instead of c_wchar_p instance

    def test_function_self_not_annotated(self):
        class ComClassImpl(Structure):
            _fields_ = [("vtable", POINTER(c_void_p))]

            def __init__(self):
                self.vtable = (c_void_p * 1)()
                self.vtable[0] = cast(self.f, c_void_p)

            @WINFUNCTYPE(UInt32, c_void_p, UInt32)
            def f(this, x):
                return x

        class ComClassPtr(c_void_p):
            @commethod(0)
            def f(self, x: UInt32) -> UInt32:
                ...

        instance = cast(pointer(ComClassImpl()), ComClassPtr)

        x = instance.f(42)
        self.assertIsInstance(x, int)
        self.assertEqual(x, 42)

    def test_structure_tuple_unpack(self):
        @press
        class S(EasyCastStructure):
            a: Int32
            b: c_char_p
            c: c_wchar_p
            d: c_void_p

        @press
        class T(EasyCastStructure):
            e: Int32
            f: S
            g: Int32
            h: Int32 * 3

        @press
        class U(EasyCastStructure):
            i: T

        u = U()
        u.i = (1, (2, 3, 4, 5), 6, (7, 8, 9))
        self.assertEqual(u.i.e, 1)
        self.assertEqual(u.i.f.a, 2)
        self.assertEqual(u.i.f.b_as_intptr, 3)
        self.assertEqual(u.i.f.c_as_intptr, 4)
        self.assertEqual(u.i.f.d, 5)
        self.assertEqual(u.i.g, 6)
        self.assertEqual(u.i.h[0], 7)
        self.assertEqual(u.i.h[1], 8)
        self.assertEqual(u.i.h[2], 9)
        self.assertEqual(u.i.h[:], [7, 8, 9])

        # MEMO: not work
        # @functype
        # def f(u: U) -> py_object:
        #     return u
        # u = f((1, (2, 3, 4, 5), 6, (7, 8, 9)))
        # ctypes.ArgumentError: argument 1: TypeError: expected U instance instead of tuple


if __name__ == "__main__":
    unittest.main()
