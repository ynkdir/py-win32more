from __future__ import annotations

import unittest

from ctypes import CFUNCTYPE
from Windows import ForeignFunction
import Windows.Win32.Foundation


def functype(prototype):
    def factory(name, types, params):
        return CFUNCTYPE(*types)(prototype)

    return ForeignFunction(prototype, factory)


class TestHresult(unittest.TestCase):
    def test_hresult(self):
        @functype
        def f(x: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT:
            return x

        self.assertEqual(
            f(Windows.Win32.Foundation.S_OK), Windows.Win32.Foundation.S_OK
        )

        with self.assertRaises(OSError):
            f(Windows.Win32.Foundation.E_FAIL)


if __name__ == "__main__":
    unittest.main()
