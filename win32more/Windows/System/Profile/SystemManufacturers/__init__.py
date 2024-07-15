from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.System.Profile.SystemManufacturers
import win32more.Windows.Win32.System.WinRT
class IOemSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.IOemSupportInfo'
    _iid_ = Guid('{8d2eae55-87ef-4266-86d0-c4afbeb29bb9}')
    @winrt_commethod(6)
    def get_SupportLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_SupportAppLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_SupportProvider(self) -> WinRT_String: ...
    SupportAppLink = property(get_SupportAppLink, None)
    SupportLink = property(get_SupportLink, None)
    SupportProvider = property(get_SupportProvider, None)
class ISmbiosInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.ISmbiosInformationStatics'
    _iid_ = Guid('{080cca7c-637c-48c4-b728-f9273812db8e}')
    @winrt_commethod(6)
    def get_SerialNumber(self) -> WinRT_String: ...
    SerialNumber = property(get_SerialNumber, None)
class ISystemSupportDeviceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo'
    _iid_ = Guid('{05880b99-8247-441b-a996-a1784bab79a8}')
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
    FriendlyName = property(get_FriendlyName, None)
    OperatingSystem = property(get_OperatingSystem, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
class ISystemSupportInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics'
    _iid_ = Guid('{ef750974-c422-45d7-a44d-5c1c0043a2b3}')
    @winrt_commethod(6)
    def get_LocalSystemEdition(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OemSupportInfo(self) -> win32more.Windows.System.Profile.SystemManufacturers.OemSupportInfo: ...
    LocalSystemEdition = property(get_LocalSystemEdition, None)
    OemSupportInfo = property(get_OemSupportInfo, None)
class ISystemSupportInfoStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics2'
    _iid_ = Guid('{33f349a4-3fa1-4986-aa4b-057420455e6d}')
    @winrt_commethod(6)
    def get_LocalDeviceInfo(self) -> win32more.Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo: ...
    LocalDeviceInfo = property(get_LocalDeviceInfo, None)
class OemSupportInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.SystemManufacturers.IOemSupportInfo
    _classid_ = 'Windows.System.Profile.SystemManufacturers.OemSupportInfo'
    @winrt_mixinmethod
    def get_SupportLink(self: win32more.Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportAppLink(self: win32more.Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportProvider(self: win32more.Windows.System.Profile.SystemManufacturers.IOemSupportInfo) -> WinRT_String: ...
    SupportAppLink = property(get_SupportAppLink, None)
    SupportLink = property(get_SupportLink, None)
    SupportProvider = property(get_SupportProvider, None)
class _SmbiosInformation_Meta_(ComPtr.__class__):
    pass
class SmbiosInformation(ComPtr, metaclass=_SmbiosInformation_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.SmbiosInformation'
    @winrt_classmethod
    def get_SerialNumber(cls: win32more.Windows.System.Profile.SystemManufacturers.ISmbiosInformationStatics) -> WinRT_String: ...
    _SmbiosInformation_Meta_.SerialNumber = property(get_SerialNumber, None)
SystemManufacturersContract: UInt32 = 196608
class SystemSupportDeviceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo
    _classid_ = 'Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo'
    @winrt_mixinmethod
    def get_OperatingSystem(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemManufacturer(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemProductName(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemSku(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHardwareVersion(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemFirmwareVersion(self: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportDeviceInfo) -> WinRT_String: ...
    FriendlyName = property(get_FriendlyName, None)
    OperatingSystem = property(get_OperatingSystem, None)
    SystemFirmwareVersion = property(get_SystemFirmwareVersion, None)
    SystemHardwareVersion = property(get_SystemHardwareVersion, None)
    SystemManufacturer = property(get_SystemManufacturer, None)
    SystemProductName = property(get_SystemProductName, None)
    SystemSku = property(get_SystemSku, None)
class _SystemSupportInfo_Meta_(ComPtr.__class__):
    pass
class SystemSupportInfo(ComPtr, metaclass=_SystemSupportInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Profile.SystemManufacturers.SystemSupportInfo'
    @winrt_classmethod
    def get_LocalDeviceInfo(cls: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics2) -> win32more.Windows.System.Profile.SystemManufacturers.SystemSupportDeviceInfo: ...
    @winrt_classmethod
    def get_LocalSystemEdition(cls: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_OemSupportInfo(cls: win32more.Windows.System.Profile.SystemManufacturers.ISystemSupportInfoStatics) -> win32more.Windows.System.Profile.SystemManufacturers.OemSupportInfo: ...
    _SystemSupportInfo_Meta_.LocalDeviceInfo = property(get_LocalDeviceInfo, None)
    _SystemSupportInfo_Meta_.LocalSystemEdition = property(get_LocalSystemEdition, None)
    _SystemSupportInfo_Meta_.OemSupportInfo = property(get_OemSupportInfo, None)


make_ready(__name__)
