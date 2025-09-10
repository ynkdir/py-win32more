from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Background
import win32more.Windows.Foundation
class DeviceServicingDetails(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Background.IDeviceServicingDetails
    _classid_ = 'Windows.Devices.Background.DeviceServicingDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpectedDuration(self: win32more.Windows.Devices.Background.IDeviceServicingDetails) -> win32more.Windows.Foundation.TimeSpan: ...
    Arguments = property(get_Arguments, None)
    DeviceId = property(get_DeviceId, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class DeviceUseDetails(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Background.IDeviceUseDetails
    _classid_ = 'Windows.Devices.Background.DeviceUseDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
    DeviceId = property(get_DeviceId, None)
class IDeviceServicingDetails(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Background.IDeviceServicingDetails'
    _iid_ = Guid('{4aabee29-2344-4ac4-8527-4a8ef6905645}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpectedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Arguments = property(get_Arguments, None)
    DeviceId = property(get_DeviceId, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class IDeviceUseDetails(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Background.IDeviceUseDetails'
    _iid_ = Guid('{7d565141-557e-4154-b994-e4f7a11fb323}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
    DeviceId = property(get_DeviceId, None)


make_ready(__name__)
