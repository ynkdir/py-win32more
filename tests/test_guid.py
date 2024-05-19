import unittest

from win32more import Guid


class TestGuid(unittest.TestCase):
    def test_guid_eq(self):
        a = Guid("{00000000-0000-0000-c000-000000000046}")
        b = Guid("{00000000-0000-0000-c000-000000000046}")
        c = Guid("{af86e2e0-b12d-4c6a-9c5a-d7aa65101e90}")
        self.assertTrue(a == b)
        self.assertFalse(a != b)
        self.assertFalse(a == c)
        self.assertTrue(a != c)


if __name__ == "__main__":
    unittest.main()
