import unittest


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
