import unittest
from ctypes import WinError

from Windows import FAILED
from Windows.Foundation.Collections import StringMap
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)


class TestWinrtStringMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)

    @classmethod
    def tearDownClass(cls):
        RoUninitialize()

    def test_stringmap(self):
        m = StringMap.New()

        m.Insert("key1", "value1")
        self.assertEqual(m.Lookup("key1"), "value1")

        m.Insert("key2", "value2")
        self.assertEqual(m.Lookup("key2"), "value2")

        m.Release()


if __name__ == "__main__":
    main()
