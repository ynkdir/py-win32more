from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.AppExtensions
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class AppExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtension'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_AppInfo(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def GetExtensionPropertiesAsync(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_mixinmethod
    def GetPublicFolderAsync(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension2) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetExtensionProperties(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension3) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def GetPublicPath(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension3) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPublicFolder(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtension3) -> win32more.Windows.Storage.StorageFolder: ...
    AppInfo = property(get_AppInfo, None)
    AppUserModelId = property(get_AppUserModelId, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Package = property(get_Package, None)
class AppExtensionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionCatalog'
    @winrt_mixinmethod
    def FindAllAsync(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]]: ...
    @winrt_mixinmethod
    def RequestRemovePackageAsync(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, packageFullName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_PackageInstalled(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageInstalled(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdating(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdating(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdated(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdated(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUninstalling(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUninstalling(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageStatusChanged(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStatusChanged(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindAll(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    @winrt_classmethod
    def Open(cls: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionCatalogStatics, appExtensionName: WinRT_String) -> win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog: ...
    PackageInstalled = event()
    PackageUpdating = event()
    PackageUpdated = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
class AppExtensionPackageInstalledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
class AppExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class AppExtensionPackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class AppExtensionPackageUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
class AppExtensionPackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs
    _classid_ = 'Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs'
    @winrt_mixinmethod
    def get_AppExtensionName(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtension'
    _iid_ = Guid('{8450902c-15ed-4faf-93ea-2237bbf8cbd6}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(10)
    def get_AppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(11)
    def GetExtensionPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_commethod(12)
    def GetPublicFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    AppInfo = property(get_AppInfo, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Package = property(get_Package, None)
class IAppExtension2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtension2'
    _iid_ = Guid('{ab3b15f0-14f9-4b9f-9419-a349a242ef38}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IAppExtension3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtension3'
    _iid_ = Guid('{5923c101-aa38-4009-84d9-5b54a0df30ae}')
    @winrt_commethod(6)
    def GetExtensionProperties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(7)
    def GetPublicPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetPublicFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
class IAppExtensionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog'
    _iid_ = Guid('{97872032-8426-4ad1-9084-92e88c2da200}')
    @winrt_commethod(6)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]]: ...
    @winrt_commethod(7)
    def RequestRemovePackageAsync(self, packageFullName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def add_PackageInstalled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageInstalledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PackageInstalled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PackageUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PackageUpdating(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PackageUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PackageUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PackageUninstalling(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PackageUninstalling(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PackageStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog, win32more.Windows.ApplicationModel.AppExtensions.AppExtensionPackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PackageStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PackageInstalled = event()
    PackageUpdating = event()
    PackageUpdated = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
class IAppExtensionCatalog2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionCatalog2'
    _iid_ = Guid('{50056eba-58b6-4147-b5a5-8feca6dfb49d}')
    @winrt_commethod(6)
    def FindAll(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
class IAppExtensionCatalogStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionCatalogStatics'
    _iid_ = Guid('{3c36668a-5f18-4f0b-9ce5-cab61d196f11}')
    @winrt_commethod(6)
    def Open(self, appExtensionName: WinRT_String) -> win32more.Windows.ApplicationModel.AppExtensions.AppExtensionCatalog: ...
class IAppExtensionPackageInstalledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionPackageInstalledEventArgs'
    _iid_ = Guid('{39e59234-3351-4a8d-9745-e7d3dd45bc48}')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
class IAppExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionPackageStatusChangedEventArgs'
    _iid_ = Guid('{1ce17433-1153-44fd-87b1-8ae1050303df}')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtensionPackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUninstallingEventArgs'
    _iid_ = Guid('{60f160c5-171e-40ff-ae98-ab2c20dd4d75}')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)
class IAppExtensionPackageUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatedEventArgs'
    _iid_ = Guid('{3a83c43f-797e-44b5-ba24-a4c8b5a543d7}')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppExtensions.AppExtension]: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
class IAppExtensionPackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.AppExtensions.IAppExtensionPackageUpdatingEventArgs'
    _iid_ = Guid('{7ed59329-1a65-4800-a700-b321009e306a}')
    @winrt_commethod(6)
    def get_AppExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    AppExtensionName = property(get_AppExtensionName, None)
    Package = property(get_Package, None)


make_ready(__name__)
