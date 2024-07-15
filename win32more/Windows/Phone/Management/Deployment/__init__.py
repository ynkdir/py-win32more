from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management.Deployment
import win32more.Windows.Phone.Management.Deployment
import win32more.Windows.Win32.System.WinRT
class Enterprise(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Management.Deployment.IEnterprise
    _classid_ = 'Windows.Phone.Management.Deployment.Enterprise'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WorkplaceId(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> Int32: ...
    @winrt_mixinmethod
    def get_EnrollmentValidFrom(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EnrollmentValidTo(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Phone.Management.Deployment.IEnterprise) -> win32more.Windows.Phone.Management.Deployment.EnterpriseStatus: ...
    EnrollmentValidFrom = property(get_EnrollmentValidFrom, None)
    EnrollmentValidTo = property(get_EnrollmentValidTo, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    Status = property(get_Status, None)
    WorkplaceId = property(get_WorkplaceId, None)
class _EnterpriseEnrollmentManager_Meta_(ComPtr.__class__):
    pass
class EnterpriseEnrollmentManager(ComPtr, metaclass=_EnterpriseEnrollmentManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.EnterpriseEnrollmentManager'
    @winrt_classmethod
    def get_EnrolledEnterprises(cls: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Management.Deployment.Enterprise]: ...
    @winrt_classmethod
    def get_CurrentEnterprise(cls: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> win32more.Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_classmethod
    def ValidateEnterprisesAsync(cls: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RequestEnrollmentAsync(cls: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enrollmentToken: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult]: ...
    @winrt_classmethod
    def RequestUnenrollmentAsync(cls: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager, enterprise: win32more.Windows.Phone.Management.Deployment.Enterprise) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    _EnterpriseEnrollmentManager_Meta_.CurrentEnterprise = property(get_CurrentEnterprise, None)
    _EnterpriseEnrollmentManager_Meta_.EnrolledEnterprises = property(get_EnrolledEnterprises, None)
class EnterpriseEnrollmentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult
    _classid_ = 'Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult'
    @winrt_mixinmethod
    def get_EnrolledEnterprise(self: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> win32more.Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult) -> win32more.Windows.Phone.Management.Deployment.EnterpriseEnrollmentStatus: ...
    EnrolledEnterprise = property(get_EnrolledEnterprise, None)
    Status = property(get_Status, None)
class EnterpriseEnrollmentStatus(Enum, Int32):
    Success = 0
    CancelledByUser = 1
    UnknownFailure = 2
class EnterpriseStatus(Enum, Int32):
    Enrolled = 0
    Disabled = 1
    Revoked = 2
    Expired = 3
class IEnterprise(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterprise'
    _iid_ = Guid('{96592f8d-856c-4426-a947-b06307718078}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_WorkplaceId(self) -> Int32: ...
    @winrt_commethod(9)
    def get_EnrollmentValidFrom(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_EnrollmentValidTo(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Status(self) -> win32more.Windows.Phone.Management.Deployment.EnterpriseStatus: ...
    EnrollmentValidFrom = property(get_EnrollmentValidFrom, None)
    EnrollmentValidTo = property(get_EnrollmentValidTo, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    Status = property(get_Status, None)
    WorkplaceId = property(get_WorkplaceId, None)
class IEnterpriseEnrollmentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterpriseEnrollmentManager'
    _iid_ = Guid('{20f9f390-2c69-41d8-88e6-e4b3884026cb}')
    @winrt_commethod(6)
    def get_EnrolledEnterprises(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Management.Deployment.Enterprise]: ...
    @winrt_commethod(7)
    def get_CurrentEnterprise(self) -> win32more.Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_commethod(8)
    def ValidateEnterprisesAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RequestEnrollmentAsync(self, enrollmentToken: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.Management.Deployment.EnterpriseEnrollmentResult]: ...
    @winrt_commethod(10)
    def RequestUnenrollmentAsync(self, enterprise: win32more.Windows.Phone.Management.Deployment.Enterprise) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    CurrentEnterprise = property(get_CurrentEnterprise, None)
    EnrolledEnterprises = property(get_EnrolledEnterprises, None)
class IEnterpriseEnrollmentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IEnterpriseEnrollmentResult'
    _iid_ = Guid('{9ff71ce6-90db-4342-b326-1729aa91301c}')
    @winrt_commethod(6)
    def get_EnrolledEnterprise(self) -> win32more.Windows.Phone.Management.Deployment.Enterprise: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Phone.Management.Deployment.EnterpriseEnrollmentStatus: ...
    EnrolledEnterprise = property(get_EnrolledEnterprise, None)
    Status = property(get_Status, None)
class IInstallationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IInstallationManagerStatics'
    _iid_ = Guid('{929aa738-8d49-42ac-80c9-b4ad793c43f2}')
    @winrt_commethod(6)
    def AddPackageAsync(self, title: WinRT_String, sourceLocation: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(7)
    def AddPackagePreloadedAsync(self, title: WinRT_String, sourceLocation: win32more.Windows.Foundation.Uri, instanceId: WinRT_String, offerId: WinRT_String, license: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(8)
    def GetPendingPackageInstalls(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]]: ...
    @winrt_commethod(9)
    def FindPackagesForCurrentPublisher(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_commethod(10)
    def FindPackages(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
class IInstallationManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IInstallationManagerStatics2'
    _iid_ = Guid('{7c6c2cbd-fa4a-4c8e-ab97-d959452f19e5}')
    @winrt_commethod(6)
    def RemovePackageAsync(self, packageFullName: WinRT_String, removalOptions: win32more.Windows.Management.Deployment.RemovalOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(7)
    def RegisterPackageAsync(self, manifestUri: win32more.Windows.Foundation.Uri, dependencyPackageUris: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], deploymentOptions: win32more.Windows.Management.Deployment.DeploymentOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_commethod(8)
    def FindPackagesByNamePublisher(self, packageName: WinRT_String, packagePublisher: WinRT_String) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
class IPackageInstallResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IPackageInstallResult'
    _iid_ = Guid('{33e8eed5-0f7e-4473-967c-7d6e1c0e7de1}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_InstallState(self) -> win32more.Windows.Management.Deployment.PackageInstallState: ...
    InstallState = property(get_InstallState, None)
    ProductId = property(get_ProductId, None)
class IPackageInstallResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.IPackageInstallResult2'
    _iid_ = Guid('{7149d909-3ff9-41ed-a717-2bc65ffc61d2}')
    @winrt_commethod(6)
    def get_ErrorText(self) -> WinRT_String: ...
    ErrorText = property(get_ErrorText, None)
class InstallationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Management.Deployment.InstallationManager'
    @winrt_classmethod
    def RemovePackageAsync(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageFullName: WinRT_String, removalOptions: win32more.Windows.Management.Deployment.RemovalOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def RegisterPackageAsync(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics2, manifestUri: win32more.Windows.Foundation.Uri, dependencyPackageUris: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], deploymentOptions: win32more.Windows.Management.Deployment.DeploymentOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def FindPackagesByNamePublisher(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics2, packageName: WinRT_String, packagePublisher: WinRT_String) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_classmethod
    def AddPackageAsync(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def AddPackagePreloadedAsync(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics, title: WinRT_String, sourceLocation: win32more.Windows.Foundation.Uri, instanceId: WinRT_String, offerId: WinRT_String, license: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]: ...
    @winrt_classmethod
    def GetPendingPackageInstalls(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Phone.Management.Deployment.PackageInstallResult, UInt32]]: ...
    @winrt_classmethod
    def FindPackagesForCurrentPublisher(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
    @winrt_classmethod
    def FindPackages(cls: win32more.Windows.Phone.Management.Deployment.IInstallationManagerStatics) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Package]: ...
class PackageInstallResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Management.Deployment.IPackageInstallResult
    _classid_ = 'Windows.Phone.Management.Deployment.PackageInstallResult'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.Phone.Management.Deployment.IPackageInstallResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstallState(self: win32more.Windows.Phone.Management.Deployment.IPackageInstallResult) -> win32more.Windows.Management.Deployment.PackageInstallState: ...
    @winrt_mixinmethod
    def get_ErrorText(self: win32more.Windows.Phone.Management.Deployment.IPackageInstallResult2) -> WinRT_String: ...
    ErrorText = property(get_ErrorText, None)
    InstallState = property(get_InstallState, None)
    ProductId = property(get_ProductId, None)


make_ready(__name__)
