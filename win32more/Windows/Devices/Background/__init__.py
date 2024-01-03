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
import win32more.Windows.Devices.Background
import win32more.Windows.Foundation
class DeviceServicingDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Background.IDeviceServicingDetails
    _classid_ = 'Windows.Devices.Background.DeviceServicingDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpectedDuration(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> win32more.Windows.Foundation.TimeSpan: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class DeviceUseDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Background.IDeviceUseDetails
    _classid_ = 'Windows.Devices.Background.DeviceUseDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
class IDeviceServicingDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Background.IDeviceServicingDetails'
    _iid_ = Guid('{4aabee29-2344-4ac4-8527-4a8ef6905645}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpectedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class IDeviceUseDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Background.IDeviceUseDetails'
    _iid_ = Guid('{7d565141-557e-4154-b994-e4f7a11fb323}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)


make_ready(__name__)
