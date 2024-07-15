from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.PackageExtensions
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class IPackageExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtension'
    _iid_ = Guid('{da70c957-7ead-5c3b-9cf0-cc43faf474b4}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(10)
    def GetExtensionProperties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(11)
    def GetExtensionPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_commethod(12)
    def GetPublicPath(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def GetPublicFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(14)
    def GetPublicFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Package = property(get_Package, None)
class IPackageExtensionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog'
    _iid_ = Guid('{0879dfe6-ac30-58b2-97f9-480b07e75bfa}')
    @winrt_commethod(6)
    def FindAll(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]]: ...
    @winrt_commethod(8)
    def RequestRemovePackageAsync(self, packageFullName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def add_PackageInstalled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageInstalledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PackageInstalled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_PackageUpdating(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_PackageUpdating(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_PackageUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PackageUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_PackageUninstalling(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_PackageUninstalling(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_PackageStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_PackageStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PackageInstalled = event()
    PackageUpdating = event()
    PackageUpdated = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
class IPackageExtensionCatalogStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalogStatics'
    _iid_ = Guid('{9588ece4-3183-5684-9e5f-27759733ddfe}')
    @winrt_commethod(6)
    def Open(self, packageExtensionName: WinRT_String) -> win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog: ...
class IPackageExtensionPackageInstalledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageInstalledEventArgs'
    _iid_ = Guid('{3c9b0067-083c-5fe3-bdfb-9feb156b4118}')
    @winrt_commethod(6)
    def get_PackageExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class IPackageExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageStatusChangedEventArgs'
    _iid_ = Guid('{b8fee20a-680d-5942-876c-5de12df1083c}')
    @winrt_commethod(6)
    def get_PackageExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class IPackageExtensionPackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUninstallingEventArgs'
    _iid_ = Guid('{3b8e9cb7-c539-554d-bb33-a84c0bfa3f50}')
    @winrt_commethod(6)
    def get_PackageExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class IPackageExtensionPackageUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatedEventArgs'
    _iid_ = Guid('{fdc31add-16a7-509d-8bc4-fde22e856d2d}')
    @winrt_commethod(6)
    def get_PackageExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(8)
    def get_Extensions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class IPackageExtensionPackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatingEventArgs'
    _iid_ = Guid('{27ae2ce1-a1d3-532e-8e7e-8b43782fce09}')
    @winrt_commethod(6)
    def get_PackageExtensionName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class PackageExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtension'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def GetExtensionProperties(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def GetExtensionPropertiesAsync(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_mixinmethod
    def GetPublicPath(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPublicFolder(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def GetPublicFolderAsync(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtension) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Package = property(get_Package, None)
class PackageExtensionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog'
    @winrt_mixinmethod
    def FindAll(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    @winrt_mixinmethod
    def FindAllAsync(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]]: ...
    @winrt_mixinmethod
    def RequestRemovePackageAsync(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, packageFullName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_PackageInstalled(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageInstalledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageInstalled(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdating(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdating(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUpdated(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUpdated(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageUninstalling(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUninstallingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageUninstalling(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PackageStatusChanged(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog, win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PackageStatusChanged(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def Open(cls: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionCatalogStatics, packageExtensionName: WinRT_String) -> win32more.Windows.ApplicationModel.PackageExtensions.PackageExtensionCatalog: ...
    PackageInstalled = event()
    PackageUpdating = event()
    PackageUpdated = event()
    PackageUninstalling = event()
    PackageStatusChanged = event()
class PackageExtensionPackageInstalledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageInstalledEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageInstalledEventArgs'
    @winrt_mixinmethod
    def get_PackageExtensionName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageInstalledEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageInstalledEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageInstalledEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class PackageExtensionPackageStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageStatusChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_PackageExtensionName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageStatusChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageStatusChangedEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class PackageExtensionPackageUninstallingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUninstallingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUninstallingEventArgs'
    @winrt_mixinmethod
    def get_PackageExtensionName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUninstallingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUninstallingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class PackageExtensionPackageUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatedEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatedEventArgs'
    @winrt_mixinmethod
    def get_PackageExtensionName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatedEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Extensions(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.PackageExtensions.PackageExtension]: ...
    Extensions = property(get_Extensions, None)
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)
class PackageExtensionPackageUpdatingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatingEventArgs
    _classid_ = 'Windows.ApplicationModel.PackageExtensions.PackageExtensionPackageUpdatingEventArgs'
    @winrt_mixinmethod
    def get_PackageExtensionName(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.ApplicationModel.PackageExtensions.IPackageExtensionPackageUpdatingEventArgs) -> win32more.Windows.ApplicationModel.Package: ...
    Package = property(get_Package, None)
    PackageExtensionName = property(get_PackageExtensionName, None)


make_ready(__name__)
