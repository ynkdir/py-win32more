import unittest

from win32more.Windows.Win32.UI.Shell import wnsprintfW

from win32more import Char


class TestVaArgs(unittest.TestCase):
    def test_vaargs(self):
        buf = (Char * 1024)()
        r = wnsprintfW(buf, len(buf), "hello %s %d %x", "world", 42, 0x1234)
        self.assertEqual(len(buf.value), r)
        self.assertEqual(buf.value, "hello world 42 1234")


if __name__ == "__main__":
    unittest.main()
