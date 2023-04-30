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
import Windows.ApplicationModel
import Windows.ApplicationModel.AppExtensions
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtension'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_AppInfo(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def GetExtensionPropertiesAsync(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_mixinmethod
    def GetPublicFolderAsync(self: Windows.ApplicationModel.AppExtensions.IAppExtension) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.ApplicationModel.AppExtensions.IAppExtension2) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Package = property(get_Package, None)
    AppInfo = property(get_AppInfo, None)
    AppUserModelId = property(get_AppUserModelId, None)
class AppExtensionCatalog(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionCatalog'
    @winrt_mixinmethod
    def FindAllAsync(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]]: ...
    @winrt_mixinmethod
    def RequestRemovePackageAsync(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, packageFullName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_PackageInstalled(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageInstalled(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdating(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdating(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdated(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdated(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUninstalling(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUninstalling(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageStatusChanged(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStatusChanged(self: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def Open(cls: Windows.ApplicationModel.AppExtensions.IAppExtensionCatalogStatics, appExtensionName: WinRT_String) -> Windows.ApplicationModel.AppExtensions.AppExtensionCatalog: ...
class AppExtensionPackageInstalledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
    Extensions = property(get_Extensions, None)
class AppExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class AppExtensionPackageUninstallingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class AppExtensionPackageUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
    Extensions = property(get_Extensions, None)
class AppExtensionPackageUpdatingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtension(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8450902c-15ed-4faf-93-ea-22-37-bb-f8-cb-d6')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(10)
    def get_AppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(11)
    def GetExtensionPropertiesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_commethod(12)
    def GetPublicFolderAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Package = property(get_Package, None)
    AppInfo = property(get_AppInfo, None)
class IAppExtension2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab3b15f0-14f9-4b9f-94-19-a3-49-a2-42-ef-38')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IAppExtensionCatalog(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('97872032-8426-4ad1-90-84-92-e8-8c-2d-a2-00')
    @winrt_commethod(6)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]]: ...
    @winrt_commethod(7)
    def RequestRemovePackageAsync(self, packageFullName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def add_PackageInstalled(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PackageInstalled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PackageUpdating(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PackageUpdating(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PackageUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PackageUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PackageUninstalling(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PackageUninstalling(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PackageStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PackageStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IAppExtensionCatalogStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3c36668a-5f18-4f0b-9c-e5-ca-b6-1d-19-6f-11')
    @winrt_commethod(6)
    def Open(self, appExtensionName: WinRT_String) -> Windows.ApplicationModel.AppExtensions.AppExtensionCatalog: ...
class IAppExtensionPackageInstalledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('39e59234-3351-4a8d-97-45-e7-d3-dd-45-bc-48')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
    Extensions = property(get_Extensions, None)
class IAppExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1ce17433-1153-44fd-87-b1-8a-e1-05-03-03-df')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtensionPackageUninstallingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('60f160c5-171e-40ff-ae-98-ab-2c-20-dd-4d-75')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtensionPackageUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3a83c43f-797e-44b5-ba-24-a4-c8-b5-a5-43-d7')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
    Extensions = property(get_Extensions, None)
class IAppExtensionPackageUpdatingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7ed59329-1a65-4800-a7-00-b3-21-00-9e-30-6a')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
make_head(_module, 'AppExtension')
make_head(_module, 'AppExtensionCatalog')
make_head(_module, 'AppExtensionPackageInstalledEventArgs')
make_head(_module, 'AppExtensionPackageStatusChangedEventArgs')
make_head(_module, 'AppExtensionPackageUninstallingEventArgs')
make_head(_module, 'AppExtensionPackageUpdatedEventArgs')
make_head(_module, 'AppExtensionPackageUpdatingEventArgs')
make_head(_module, 'IAppExtension')
make_head(_module, 'IAppExtension2')
make_head(_module, 'IAppExtensionCatalog')
make_head(_module, 'IAppExtensionCatalogStatics')
make_head(_module, 'IAppExtensionPackageInstalledEventArgs')
make_head(_module, 'IAppExtensionPackageStatusChangedEventArgs')
make_head(_module, 'IAppExtensionPackageUninstallingEventArgs')
make_head(_module, 'IAppExtensionPackageUpdatedEventArgs')
make_head(_module, 'IAppExtensionPackageUpdatingEventArgs')
