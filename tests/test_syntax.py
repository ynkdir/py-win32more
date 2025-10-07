import unittest
from ctypes import _CFuncPtr, sizeof


def commit(prototype):
    return prototype.__commit__()


class TestSyntax(unittest.TestCase):
    def test_pkey_lazyload(self):
        from win32more.Windows.Win32.Devices.FunctionDiscovery import PKEY_FunctionInstance
        from win32more.Windows.Win32.Foundation import PROPERTYKEY

        self.assertIsInstance(PKEY_FunctionInstance, PROPERTYKEY)

    def test_devpkey_lazyload(self):
        from win32more.Windows.Win32.Devices.Display import DEVPKEY_IndirectDisplay
        from win32more.Windows.Win32.Foundation import DEVPROPKEY

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

    def test_circular_referenct_function_pointer(self):
        # def pfn(x: POINTER(A)): ...
        # struct A:
        #   f: pfn
        from win32more.Windows.Win32.System.Com import LPEXCEPFINO_DEFERRED_FILLIN

        self.assertIsNotNone(LPEXCEPFINO_DEFERRED_FILLIN)

    def test_function_pointer(self):
        from win32more.Windows.Win32.Graphics.Gdi import FONTENUMPROCA

        self.assertTrue(issubclass(FONTENUMPROCA, _CFuncPtr))

    def test_function_pointer_referred_twice(self):
        from win32more.Windows.Win32.UI.WindowsAndMessaging import WNDCLASSA, WNDCLASSW

        self.assertNotEqual(sizeof(WNDCLASSA), 0)
        self.assertNotEqual(sizeof(WNDCLASSW), 0)

    @unittest.skip("mddbootstrap auto initialization causes error")
    def test_winrt_overload_select_statics_properly(self):
        from win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime import DeploymentManager

        self.assertEqual(
            set(func._prototype.__annotations__["cls"] for func in DeploymentManager.__dict__["Initialize"].funcs),
            {
                "win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics2",
                "win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics",
            },
        )

    def test_inline_function(self):
        from win32more.Windows.Win32.System.Threading import GetCurrentProcessToken

        self.assertEqual(GetCurrentProcessToken(), -4)

    def test_overload_method_is_wrapped_with_winrt_overload(self):
        from win32more.Windows.Storage.Pickers import FileOpenPicker

        from win32more.winrt import winrt_overload

        self.assertIsInstance(FileOpenPicker.__dict__["PickSingleFileAsync"], winrt_overload)

    def test_issue5_u_e__Union_is_not_defined(self):
        from win32more.Windows.Win32.System.Rpc import RPC_SECURITY_QOS_V3_W

        self.assertNotEqual(sizeof(RPC_SECURITY_QOS_V3_W._u_e__Union), 0)

    def test_type_error_when_struct_member_descriptor_is_not_cfield_type(self):
        # _ctypes/stgdict.c:MakeFields() raises TypeError for non _ctypes.CField type.
        from win32more.Windows.Win32.Foundation import DECIMAL

        self.assertNotEqual(sizeof(DECIMAL), 0)

    def test_unicode_alias(self):
        from win32more.Windows.Win32.UI.WindowsAndMessaging import MessageBox, MessageBoxW

        self.assertIs(MessageBox, MessageBoxW)

    def test_struct_member_of_generic_type(self):
        from typing import Generic

        from win32more.Windows.Foundation import IReference
        from win32more.Windows.Web.Http import HttpProgress

        from win32more import UInt64

        x = HttpProgress()
        self.assertIsInstance(x.TotalBytesToSend, Generic)
        self.assertIsInstance(x.TotalBytesToSend, IReference)
        self.assertEqual(x.TotalBytesToSend.__orig_class__.__args__, (UInt64,))

    def test_struct_bitfield(self):
        from win32more.Windows.Win32.Storage.Nvme import NVME_COMMAND_DWORD0

        from win32more import UInt32

        self.assertEqual(sizeof(NVME_COMMAND_DWORD0), sizeof(UInt32))

        x = NVME_COMMAND_DWORD0(OPC=1, FUSE=1, Reserved0=1, PSDT=1, CID=1)
        # self.assertEqual(x.AsUlong, 0b00000000000000011000010100000001)
        # since Win32Metadata v64.0.22 (10.0.26100.2161 SDK)
        self.assertEqual(x.AsUlong, 0b00000000000000010100010100000001)

    def test_struct_unnamed_bitfield_member(self):
        from win32more.Windows.Win32.Networking.WinSock import IPV6_HEADER

        x = IPV6_HEADER()
        x.VersionClassFlow = 0x12345678
        self.assertEqual(x.Version, 7)
        self.assertEqual(x.Anonymous1, 8)

    def test_flexible_array(self):
        from win32more._win32 import Byte, FlexibleArray, Structure

        @commit
        class S(Structure):
            arr: FlexibleArray[Byte]

        s = S.from_buffer(bytearray(b"\x01\x02\x03\x04"))

        self.assertEqual(s.arr[0], 1)
        self.assertEqual(s.arr[:4], [1, 2, 3, 4])

        with self.assertRaises(ValueError):
            # ValueError: slice stop is required
            s.arr[:]

        with self.assertRaises(IndexError):
            for x in s.arr:
                pass


if __name__ == "__main__":
    unittest.main()
