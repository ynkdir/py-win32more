import unittest
from ctypes import _CFuncPtr, sizeof


class TestSyntax(unittest.TestCase):
    def test_pkey_lazyload(self):
        from win32more.Windows.Win32.Devices.FunctionDiscovery import PKEY_FunctionInstance
        from win32more.Windows.Win32.UI.Shell.PropertiesSystem import PROPERTYKEY

        self.assertIsInstance(PKEY_FunctionInstance, PROPERTYKEY)

    def test_devpkey_lazyload(self):
        from win32more.Windows.Win32.Devices.Display import DEVPKEY_IndirectDisplay
        from win32more.Windows.Win32.Devices.Properties import DEVPROPKEY

        self.assertIsInstance(DEVPKEY_IndirectDisplay, DEVPROPKEY)

    def test_sid_lazyload(self):
        from win32more.Windows.Win32.Security import SECURITY_NULL_SID_AUTHORITY, SID_IDENTIFIER_AUTHORITY

        self.assertIsInstance(SECURITY_NULL_SID_AUTHORITY, SID_IDENTIFIER_AUTHORITY)

    def test_just_import(self):
        from win32more.Windows.Win32.Foundation import POINT

        self.assertEqual(sizeof(POINT), 8)

    def test_array(self):
        from win32more.Windows.Win32.Foundation import POINT

        point_array = (POINT * 1)()
        point_array[0].x = 123
        self.assertEqual(point_array[0].x, 123)

    def test_circular_referenct_pointer(self):
        # struct A:
        #   a: POINTER(A)
        from win32more.Windows.Win32.System.Kernel import SLIST_ENTRY

        self.assertNotEqual(sizeof(SLIST_ENTRY), 0)

    def test_circular_reference_pointer_direct(self):
        # struct A:
        #  b: POINTER(B)
        # struct B:
        #  a: A
        from win32more.Windows.Win32.Devices.WebServicesOnDevices import WSDXML_NODE

        self.assertNotEqual(sizeof(WSDXML_NODE), 0)

    def test_function_pointer(self):
        from win32more.Windows.Win32.Graphics.Gdi import FONTENUMPROCA

        self.assertTrue(issubclass(FONTENUMPROCA, _CFuncPtr))

    def test_function_pointer_referred_twice(self):
        from win32more.Windows.Win32.UI.WindowsAndMessaging import WNDCLASSA, WNDCLASSW

        self.assertNotEqual(sizeof(WNDCLASSA), 0)
        self.assertNotEqual(sizeof(WNDCLASSW), 0)


if __name__ == "__main__":
    unittest.main()
