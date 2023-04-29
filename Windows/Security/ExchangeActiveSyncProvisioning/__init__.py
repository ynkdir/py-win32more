from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Security.ExchangeActiveSyncProvisioning
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class EasClientDeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.ExchangeActiveSyncProvisioning.EasClientDeviceInformation: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> Guid: ...
    @winrt_mixinmethod
    def get_OperatingSystem(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemManufacturer(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemProductName(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemSku(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHardwareVersion(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemFirmwareVersion(self: Windows.Security.ExchangeActiveSyncProvisioning.IEasClientDeviceInformation2) -> WinRT_String: ...
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
class IEasClientDeviceInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('54dfd981-1968-4ca3-b9-58-e5-95-d1-65-05-eb')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_OperatingSystem(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SystemManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SystemProductName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SystemSku(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
class IEasClientDeviceInformation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ffb35923-bb26-4d6a-81-bc-16-5a-ee-0a-d7-54')
    @winrt_commethod(6)
    def get_SystemHardwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SystemFirmwareVersion(self) -> WinRT_String: ...
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
make_head(_module, 'EasClientDeviceInformation')
make_head(_module, 'IEasClientDeviceInformation')
make_head(_module, 'IEasClientDeviceInformation2')
