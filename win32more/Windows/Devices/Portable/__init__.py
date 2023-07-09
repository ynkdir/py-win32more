from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Portable
import win32more.Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IServiceDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Portable.IServiceDeviceStatics'
    _iid_ = Guid('{a88214e1-59c7-4a20-aba6-9f6707937230}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, serviceType: win32more.Windows.Devices.Portable.ServiceDeviceType) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromServiceId(self, serviceId: Guid) -> WinRT_String: ...
class IStorageDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Portable.IStorageDeviceStatics'
    _iid_ = Guid('{5ece44ee-1b23-4dd2-8652-bc164f003128}')
    @winrt_commethod(6)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
PortableDeviceContract: UInt32 = 65536
class ServiceDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Portable.ServiceDevice'
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Portable.IServiceDeviceStatics, serviceType: win32more.Windows.Devices.Portable.ServiceDeviceType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromServiceId(cls: win32more.Windows.Devices.Portable.IServiceDeviceStatics, serviceId: Guid) -> WinRT_String: ...
ServiceDeviceType = Int32
ServiceDeviceType_CalendarService: ServiceDeviceType = 0
ServiceDeviceType_ContactsService: ServiceDeviceType = 1
ServiceDeviceType_DeviceStatusService: ServiceDeviceType = 2
ServiceDeviceType_NotesService: ServiceDeviceType = 3
ServiceDeviceType_RingtonesService: ServiceDeviceType = 4
ServiceDeviceType_SmsService: ServiceDeviceType = 5
ServiceDeviceType_TasksService: ServiceDeviceType = 6
class StorageDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Portable.StorageDevice'
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Devices.Portable.IStorageDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Portable.IStorageDeviceStatics) -> WinRT_String: ...
make_head(_module, 'IServiceDeviceStatics')
make_head(_module, 'IStorageDeviceStatics')
make_head(_module, 'ServiceDevice')
make_head(_module, 'StorageDevice')
