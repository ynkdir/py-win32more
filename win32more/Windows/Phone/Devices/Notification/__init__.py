from __future__ import annotations
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Phone.Devices.Notification
class IVibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Notification.IVibrationDevice'
    _iid_ = Guid('{1b4a6595-cfcd-4e08-92fb-c1906d04498c}')
    @winrt_commethod(6)
    def Vibrate(self, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def Cancel(self) -> Void: ...
class IVibrationDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Notification.IVibrationDeviceStatics'
    _iid_ = Guid('{332fd2f1-1c69-4c91-949e-4bb67a85bdc7}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Phone.Devices.Notification.VibrationDevice: ...
class VibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Devices.Notification.IVibrationDevice
    _classid_ = 'Windows.Phone.Devices.Notification.VibrationDevice'
    @winrt_mixinmethod
    def Vibrate(self: win32more.Windows.Phone.Devices.Notification.IVibrationDevice, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Phone.Devices.Notification.IVibrationDevice) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Phone.Devices.Notification.IVibrationDeviceStatics) -> win32more.Windows.Phone.Devices.Notification.VibrationDevice: ...


make_ready(__name__)
