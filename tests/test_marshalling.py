import unittest
from ctypes import cast

from Windows import (
    EasyCastStructure,
    EasyCastUnion,
    c_char_p_no,
    c_void_p,
    c_wchar_p_no,
    press,
)
from Windows.Win32.UI.Shell import StrChrA, StrChrW


class TestMarshalling(unittest.TestCase):
    def test_c_void_p(self):
        @press
        class S(EasyCastStructure):
            c_void_p: c_void_p

        s = S()

        self.assertIsNone(s.c_void_p)

        s.c_void_p = 0
        self.assertIsNone(s.c_void_p)

        s.c_void_p = 1234
        self.assertIsInstance(s.c_void_p, int)
        self.assertEqual(s.c_void_p, 1234)

    def test_c_char_p(self):
        @press
        class S(EasyCastStructure):
            c_char_p: c_char_p_no

        s = S()

        self.assertIsNone(s.c_char_p)

        s.c_char_p = 0
        self.assertIsNone(s.c_char_p)

        s.c_char_p = b"abcdefg"
        self.assertIsInstance(s.c_char_p, bytes)
        self.assertEqual(s.c_char_p, b"abcdefg")

        s.c_char_p = 1234
        self.assertIsInstance(s.c_char_p_as_intptr, int)
        self.assertEqual(s.c_char_p_as_intptr, 1234)

    def test_c_wchar_p(self):
        @press
        class S(EasyCastStructure):
            c_wchar_p: c_wchar_p_no

        s = S()

        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = 0
        self.assertIsNone(s.c_wchar_p)

        s.c_wchar_p = "abcdefg"
        self.assertIsInstance(s.c_wchar_p, str)
        self.assertEqual(s.c_wchar_p, "abcdefg")

        s.c_wchar_p = 1234
        self.assertIsInstance(s.c_wchar_p_as_intptr, int)
        self.assertEqual(s.c_wchar_p_as_intptr, 1234)

    def test_function_return_char_p(self):
        s = c_char_p_no(b"abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrA(s, ord("x"))
        self.assertIsNone(p)

        p = StrChrA(s, ord("d"))
        self.assertEquals(p, b"defg")

        p = StrChrA(s, ord("d"), _as_intptr=True)
        self.assertEquals(p, i + 3)

    def test_function_return_wchar_p(self):
        s = c_wchar_p_no("abcdefg")
        i = cast(s, c_void_p).value

        p = StrChrW(s, "x")
        self.assertIsNone(p)

        p = StrChrW(s, "d")
        self.assertEquals(p, "defg")

        p = StrChrW(s, "d", _as_intptr=True)
        self.assertEquals(p, i + 6)


if __name__ == "__main__":
    unittest.main()
