from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.System.Profile.SystemManufacturers
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IOemSupportInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d2eae55-87ef-4266-86-d0-c4-af-be-b2-9b-b9')
    @winrt_commethod(6)
    def get_SupportLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_SupportAppLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_SupportProvider(self) -> WinRT_String: ...
    SupportLink = property(get_SupportLink, None)
    SupportAppLink = property(get_SupportAppLink, None)
    SupportProvider = property(get_SupportProvider, None)
class ISmbiosInformationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('080cca7c-637c-48c4-b7-28-f9-27-38-12-db-8e')
    @winrt_commethod(6)
    def get_SerialNumber(self) -> WinRT_String: ...
    SerialNumber = property(get_SerialNumber, None)
class ISystemSupportDeviceInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05880b99-8247-441b-a9-96-a1-78-4b-ab-79-a8')
    @winrt_commethod(6)
    def get_OperatingSystem(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SystemManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SystemProductName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SystemSku(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SystemHardwareVersion(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SystemFirmwareVersion(self) -> WinRT_String: ...
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
class ISystemSupportInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef750974-c422-45d7-a4-4d-5c-1c-00-43-a2-b3')
    @winrt_commethod(6)
    def get_LocalSystemEdition(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OemSupportInfo(self) -> Windows.System.Profile.SystemManufacturers.OemSupportInfo: ...
    LocalSystemEdition = property(get_LocalSystemEdition, None)
    OemSupportInfo = property(get_OemSupportInfo, None)
class ISystemSupportInfoStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33f349a4-3fa1-4986-aa-4b-05-74-20-45-5e-6d')
    @winrt_commethod(6)
    def get_LocalDeviceInfo(self) -> Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo: ...
    LocalDeviceInfo = property(get_LocalDeviceInfo, None)
class OemSupportInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemManufacturers.OemSupportInfo'
    @winrt_mixinmethod
    def get_SupportLink(self: Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportAppLink(self: Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportProvider(self: Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> WinRT_String: ...
    SupportLink = property(get_SupportLink, None)
    SupportAppLink = property(get_SupportAppLink, None)
    SupportProvider = property(get_SupportProvider, None)
class SmbiosInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemManufacturers.SmbiosInformation'
    @winrt_classmethod
    def get_SerialNumber(cls: Windows.System.Profile.SystemManufacturers.ISmbiosInformationStatics) -> WinRT_String: ...
    SerialNumber = property(get_SerialNumber, None)
SystemManufacturersContract: UInt32 = 196608
class SystemSupportDeviceInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo'
    @winrt_mixinmethod
    def get_OperatingSystem(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemManufacturer(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemProductName(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemSku(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHardwareVersion(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemFirmwareVersion(self: Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    OperatingSystem = property(get_OperatingSystem, None)
    FriendlyName = property(get_FriendlyName, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
class SystemSupportInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Profile.SystemManufacturers.SystemSupportInfo'
    @winrt_classmethod
    def get_LocalDeviceInfo(cls: Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics2) -> Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo: ...
    @winrt_classmethod
    def get_LocalSystemEdition(cls: Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_OemSupportInfo(cls: Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics) -> Windows.System.Profile.SystemManufacturers.OemSupportInfo: ...
    LocalDeviceInfo = property(get_LocalDeviceInfo, None)
    LocalSystemEdition = property(get_LocalSystemEdition, None)
    OemSupportInfo = property(get_OemSupportInfo, None)
make_head(_module, 'IOemSupportInfo')
make_head(_module, 'ISmbiosInformationStatics')
make_head(_module, 'ISystemSupportDeviceInfo')
make_head(_module, 'ISystemSupportInfoStatics')
make_head(_module, 'ISystemSupportInfoStatics2')
make_head(_module, 'OemSupportInfo')
make_head(_module, 'SmbiosInformation')
make_head(_module, 'SystemSupportDeviceInfo')
make_head(_module, 'SystemSupportInfo')
