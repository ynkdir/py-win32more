from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Portable
import win32more.Windows.Storage
class IServiceDeviceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Portable.IServiceDeviceStatics'
    _iid_ = Guid('{a88214e1-59c7-4a20-aba6-9f6707937230}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, serviceType: win32more.Windows.Devices.Portable.ServiceDeviceType) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromServiceId(self, serviceId: Guid) -> WinRT_String: ...
class IStorageDeviceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Portable.IStorageDeviceStatics'
    _iid_ = Guid('{5ece44ee-1b23-4dd2-8652-bc164f003128}')
    @winrt_commethod(6)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
PortableDeviceContract: UInt32 = 65536
class ServiceDevice(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Portable.ServiceDevice'
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Portable.IServiceDeviceStatics, serviceType: win32more.Windows.Devices.Portable.ServiceDeviceType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromServiceId(cls: win32more.Windows.Devices.Portable.IServiceDeviceStatics, serviceId: Guid) -> WinRT_String: ...
class ServiceDeviceType(Enum, Int32):
    CalendarService = 0
    ContactsService = 1
    DeviceStatusService = 2
    NotesService = 3
    RingtonesService = 4
    SmsService = 5
    TasksService = 6
class StorageDevice(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Portable.StorageDevice'
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Devices.Portable.IStorageDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Portable.IStorageDeviceStatics) -> WinRT_String: ...


make_ready(__name__)
