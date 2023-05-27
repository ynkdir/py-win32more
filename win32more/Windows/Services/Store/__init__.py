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
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Store
import win32more.Windows.System
import win32more.Windows.Web.Http
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IStoreAcquireLicenseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreAcquireLicenseResult'
    _iid_ = Guid('{fbd7946d-f040-4cb3-9a39-29bcecdbe22d}')
    @winrt_commethod(6)
    def get_StorePackageLicense(self) -> win32more.Windows.Services.Store.StorePackageLicense: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    StorePackageLicense = property(get_StorePackageLicense, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreAppLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreAppLicense'
    _iid_ = Guid('{f389f9de-73c0-45ce-9bab-b2fe3e5eafd3}')
    @winrt_commethod(6)
    def get_SkuStoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AddOnLicenses(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreLicense]: ...
    @winrt_commethod(12)
    def get_TrialTimeRemaining(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_IsTrialOwnedByThisUser(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_TrialUniqueId(self) -> WinRT_String: ...
    SkuStoreId = property(get_SkuStoreId, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    AddOnLicenses = property(get_AddOnLicenses, None)
    TrialTimeRemaining = property(get_TrialTimeRemaining, None)
    IsTrialOwnedByThisUser = property(get_IsTrialOwnedByThisUser, None)
    TrialUniqueId = property(get_TrialUniqueId, None)
class IStoreAppLicense2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreAppLicense2'
    _iid_ = Guid('{b4666e91-4443-40b3-993f-28904435bdc6}')
    @winrt_commethod(6)
    def get_IsDiscLicense(self) -> Boolean: ...
    IsDiscLicense = property(get_IsDiscLicense, None)
class IStoreAvailability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreAvailability'
    _iid_ = Guid('{fa060325-0ffd-4493-ad43-f1f9918f69fa}')
    @winrt_commethod(6)
    def get_StoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EndDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Price(self) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_commethod(9)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def RequestPurchaseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(11)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    StoreId = property(get_StoreId, None)
    EndDate = property(get_EndDate, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class IStoreCanAcquireLicenseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreCanAcquireLicenseResult'
    _iid_ = Guid('{3a693db3-0088-482f-86d5-bd46522663ad}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_LicensableSku(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Services.Store.StoreCanLicenseStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LicensableSku = property(get_LicensableSku, None)
    Status = property(get_Status, None)
class IStoreCollectionData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreCollectionData'
    _iid_ = Guid('{8aa4c3b3-5bb3-441a-2ab4-4dab73d5ce67}')
    @winrt_commethod(6)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CampaignId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DeveloperOfferId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AcquiredDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_StartDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_EndDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_TrialTimeRemaining(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    IsTrial = property(get_IsTrial, None)
    CampaignId = property(get_CampaignId, None)
    DeveloperOfferId = property(get_DeveloperOfferId, None)
    AcquiredDate = property(get_AcquiredDate, None)
    StartDate = property(get_StartDate, None)
    EndDate = property(get_EndDate, None)
    TrialTimeRemaining = property(get_TrialTimeRemaining, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class IStoreConsumableResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreConsumableResult'
    _iid_ = Guid('{ea5dab72-6a00-4052-be5b-bfdab4433352}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Store.StoreConsumableStatus: ...
    @winrt_commethod(7)
    def get_TrackingId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_BalanceRemaining(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    TrackingId = property(get_TrackingId, None)
    BalanceRemaining = property(get_BalanceRemaining, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreContext'
    _iid_ = Guid('{ac98b6be-f4fd-4912-babd-5035e5e8bcab}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def add_OfflineLicensesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreContext, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_OfflineLicensesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def GetCustomerPurchaseIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def GetCustomerCollectionsIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def GetAppLicenseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreAppLicense]: ...
    @winrt_commethod(12)
    def GetStoreProductForCurrentAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductResult]: ...
    @winrt_commethod(13)
    def GetStoreProductsAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(14)
    def GetAssociatedStoreProductsAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(15)
    def GetAssociatedStoreProductsWithPagingAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_commethod(16)
    def GetUserCollectionAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(17)
    def GetUserCollectionWithPagingAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_commethod(18)
    def ReportConsumableFulfillmentAsync(self, productStoreId: WinRT_String, quantity: UInt32, trackingId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_commethod(19)
    def GetConsumableBalanceRemainingAsync(self, productStoreId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_commethod(20)
    def AcquireStoreLicenseForOptionalPackageAsync(self, optionalPackage: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreAcquireLicenseResult]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storeId: WinRT_String, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(23)
    def GetAppAndOptionalStorePackageUpdatesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StorePackageUpdate]]: ...
    @winrt_commethod(24)
    def RequestDownloadStorePackageUpdatesAsync(self, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(25)
    def RequestDownloadAndInstallStorePackageUpdatesAsync(self, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(26)
    def RequestDownloadAndInstallStorePackagesAsync(self, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    User = property(get_User, None)
class IStoreContext2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreContext2'
    _iid_ = Guid('{18bc54da-7bd9-452c-9116-3bbd06ffc63a}')
    @winrt_commethod(6)
    def FindStoreProductForPackageAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductResult]: ...
class IStoreContext3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreContext3'
    _iid_ = Guid('{e26226ca-1a01-4730-85a6-ecc896e4ae38}')
    @winrt_commethod(6)
    def get_CanSilentlyDownloadStorePackageUpdates(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySilentDownloadStorePackageUpdatesAsync(self, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(8)
    def TrySilentDownloadAndInstallStorePackageUpdatesAsync(self, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(9)
    def CanAcquireStoreLicenseForOptionalPackageAsync(self, optionalPackage: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_commethod(10)
    def CanAcquireStoreLicenseAsync(self, productStoreId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_commethod(11)
    def GetStoreProductsWithOptionsAsync(self, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeProductOptions: win32more.Windows.Services.Store.StoreProductOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(12)
    def GetAssociatedStoreQueueItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_commethod(13)
    def GetStoreQueueItemsAsync(self, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_commethod(14)
    def RequestDownloadAndInstallStorePackagesWithInstallOptionsAsync(self, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storePackageInstallOptions: win32more.Windows.Services.Store.StorePackageInstallOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(15)
    def DownloadAndInstallStorePackagesAsync(self, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(16)
    def RequestUninstallStorePackageAsync(self, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(17)
    def RequestUninstallStorePackageByStoreIdAsync(self, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(18)
    def UninstallStorePackageAsync(self, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(19)
    def UninstallStorePackageByStoreIdAsync(self, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    CanSilentlyDownloadStorePackageUpdates = property(get_CanSilentlyDownloadStorePackageUpdates, None)
class IStoreContext4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreContext4'
    _iid_ = Guid('{af9c6f69-bea1-4bf4-8e74-ae03e206c6b0}')
    @winrt_commethod(6)
    def RequestRateAndReviewAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreRateAndReviewResult]: ...
    @winrt_commethod(7)
    def SetInstallOrderForAssociatedStoreQueueItemsAsync(self, items: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StoreQueueItem]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
class IStoreContextStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreContextStatics'
    _iid_ = Guid('{9c06ee5f-15c0-4e72-9330-d6191cebd19c}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Services.Store.StoreContext: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Services.Store.StoreContext: ...
class IStoreImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreImage'
    _iid_ = Guid('{081fd248-adb4-4b64-a993-784789926ed5}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_ImagePurposeTag(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Caption(self) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    ImagePurposeTag = property(get_ImagePurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
class IStoreLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreLicense'
    _iid_ = Guid('{26dc9579-4c4f-4f30-bc89-649f60e36055}')
    @winrt_commethod(6)
    def get_SkuStoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_InAppOfferToken(self) -> WinRT_String: ...
    SkuStoreId = property(get_SkuStoreId, None)
    IsActive = property(get_IsActive, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    InAppOfferToken = property(get_InAppOfferToken, None)
class IStorePackageInstallOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePackageInstallOptions'
    _iid_ = Guid('{1d3d630c-0ccd-44dd-8c59-80810a729973}')
    @winrt_commethod(6)
    def get_AllowForcedAppRestart(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowForcedAppRestart(self, value: Boolean) -> Void: ...
    AllowForcedAppRestart = property(get_AllowForcedAppRestart, put_AllowForcedAppRestart)
class IStorePackageLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePackageLicense'
    _iid_ = Guid('{0c465714-14e1-4973-bd14-f77724271e99}')
    @winrt_commethod(6)
    def add_LicenseLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StorePackageLicense, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LicenseLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(9)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(10)
    def ReleaseLicense(self) -> Void: ...
    Package = property(get_Package, None)
    IsValid = property(get_IsValid, None)
class IStorePackageUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePackageUpdate'
    _iid_ = Guid('{140fa150-3cbf-4a35-b91f-48271c31b072}')
    @winrt_commethod(6)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_Mandatory(self) -> Boolean: ...
    Package = property(get_Package, None)
    Mandatory = property(get_Mandatory, None)
class IStorePackageUpdateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePackageUpdateResult'
    _iid_ = Guid('{e79142ed-61f9-4893-b4fe-cf191603af7b}')
    @winrt_commethod(6)
    def get_OverallState(self) -> win32more.Windows.Services.Store.StorePackageUpdateState: ...
    @winrt_commethod(7)
    def get_StorePackageUpdateStatuses(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    OverallState = property(get_OverallState, None)
    StorePackageUpdateStatuses = property(get_StorePackageUpdateStatuses, None)
class IStorePackageUpdateResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePackageUpdateResult2'
    _iid_ = Guid('{071d012e-bc62-4f2e-87ea-99d801aeaf98}')
    @winrt_commethod(6)
    def get_StoreQueueItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]: ...
    StoreQueueItems = property(get_StoreQueueItems, None)
class IStorePrice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePrice'
    _iid_ = Guid('{55ba94c4-15f1-407c-8f06-006380f4df0b}')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SaleEndDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_CurrencyCode(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_FormattedRecurrencePrice(self) -> WinRT_String: ...
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    FormattedPrice = property(get_FormattedPrice, None)
    IsOnSale = property(get_IsOnSale, None)
    SaleEndDate = property(get_SaleEndDate, None)
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedRecurrencePrice = property(get_FormattedRecurrencePrice, None)
class IStoreProduct(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreProduct'
    _iid_ = Guid('{320e2c52-d760-450a-a42b-67d1e901ac90}')
    @winrt_commethod(6)
    def get_StoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ProductKind(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_HasDigitalDownload(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_Keywords(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Images(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreImage]: ...
    @winrt_commethod(14)
    def get_Videos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreVideo]: ...
    @winrt_commethod(15)
    def get_Skus(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreSku]: ...
    @winrt_commethod(16)
    def get_IsInUserCollection(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_Price(self) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_commethod(18)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_LinkUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(20)
    def GetIsAnySkuInstalledAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(23)
    def get_InAppOfferToken(self) -> WinRT_String: ...
    StoreId = property(get_StoreId, None)
    Language = property(get_Language, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    ProductKind = property(get_ProductKind, None)
    HasDigitalDownload = property(get_HasDigitalDownload, None)
    Keywords = property(get_Keywords, None)
    Images = property(get_Images, None)
    Videos = property(get_Videos, None)
    Skus = property(get_Skus, None)
    IsInUserCollection = property(get_IsInUserCollection, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    LinkUri = property(get_LinkUri, None)
    InAppOfferToken = property(get_InAppOfferToken, None)
class IStoreProductOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreProductOptions'
    _iid_ = Guid('{5b34a0f9-a113-4811-8326-16199c927f31}')
    @winrt_commethod(6)
    def get_ActionFilters(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ActionFilters = property(get_ActionFilters, None)
class IStoreProductPagedQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreProductPagedQueryResult'
    _iid_ = Guid('{c92718c5-4dd5-4869-a462-ecc6872e43c5}')
    @winrt_commethod(6)
    def get_Products(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreProduct]: ...
    @winrt_commethod(7)
    def get_HasMoreResults(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def GetNextAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    Products = property(get_Products, None)
    HasMoreResults = property(get_HasMoreResults, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreProductQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreProductQueryResult'
    _iid_ = Guid('{d805e6c5-d456-4ff6-8049-9076d5165f73}')
    @winrt_commethod(6)
    def get_Products(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreProduct]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Products = property(get_Products, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreProductResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreProductResult'
    _iid_ = Guid('{b7674f73-3c87-4ee1-8201-f428359bd3af}')
    @winrt_commethod(6)
    def get_Product(self) -> win32more.Windows.Services.Store.StoreProduct: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Product = property(get_Product, None)
    ExtendedError = property(get_ExtendedError, None)
class IStorePurchaseProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePurchaseProperties'
    _iid_ = Guid('{836278f3-ff87-4364-a5b4-fd2153ebe43b}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ExtendedJsonData(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    ExtendedJsonData = property(get_ExtendedJsonData, put_ExtendedJsonData)
class IStorePurchasePropertiesFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePurchasePropertiesFactory'
    _iid_ = Guid('{a768f59e-fefd-489f-9a17-22a593e68b9d}')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String) -> win32more.Windows.Services.Store.StorePurchaseProperties: ...
class IStorePurchaseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStorePurchaseResult'
    _iid_ = Guid('{add28552-f96a-463d-a7bb-c20b4fca6952}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Store.StorePurchaseStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreQueueItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreQueueItem'
    _iid_ = Guid('{56d5c32b-f830-4293-9188-cad2dcde7357}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_InstallKind(self) -> win32more.Windows.Services.Store.StoreQueueItemKind: ...
    @winrt_commethod(9)
    def GetCurrentStatus(self) -> win32more.Windows.Services.Store.StoreQueueItemStatus: ...
    @winrt_commethod(10)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreQueueItem, win32more.Windows.Services.Store.StoreQueueItemCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreQueueItem, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProductId = property(get_ProductId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    InstallKind = property(get_InstallKind, None)
class IStoreQueueItem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreQueueItem2'
    _iid_ = Guid('{69491ca8-1ad4-447c-ad8c-a95035f64d82}')
    @winrt_commethod(6)
    def CancelInstallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def PauseInstallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ResumeInstallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IStoreQueueItemCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreQueueItemCompletedEventArgs'
    _iid_ = Guid('{1247df6c-b44a-439b-bb07-1d3003d005c2}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Store.StoreQueueItemStatus: ...
    Status = property(get_Status, None)
class IStoreQueueItemStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreQueueItemStatus'
    _iid_ = Guid('{9bd6796f-9cc3-4ec3-b2ef-7be433b30174}')
    @winrt_commethod(6)
    def get_PackageInstallState(self) -> win32more.Windows.Services.Store.StoreQueueItemState: ...
    @winrt_commethod(7)
    def get_PackageInstallExtendedState(self) -> win32more.Windows.Services.Store.StoreQueueItemExtendedState: ...
    @winrt_commethod(8)
    def get_UpdateStatus(self) -> win32more.Windows.Services.Store.StorePackageUpdateStatus: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    PackageInstallState = property(get_PackageInstallState, None)
    PackageInstallExtendedState = property(get_PackageInstallExtendedState, None)
    UpdateStatus = property(get_UpdateStatus, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreRateAndReviewResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreRateAndReviewResult'
    _iid_ = Guid('{9d209d56-a6b5-4121-9b61-ee6d0fbdbdbb}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_WasUpdated(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Status(self) -> win32more.Windows.Services.Store.StoreRateAndReviewStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    WasUpdated = property(get_WasUpdated, None)
    Status = property(get_Status, None)
class IStoreRequestHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreRequestHelperStatics'
    _iid_ = Guid('{6ce5e5f9-a0c9-4b2c-96a6-a171c630038d}')
    @winrt_commethod(6)
    def SendRequestAsync(self, context: win32more.Windows.Services.Store.StoreContext, requestKind: UInt32, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreSendRequestResult]: ...
class IStoreSendRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreSendRequestResult'
    _iid_ = Guid('{c73abe60-8272-4502-8a69-6e75153a4299}')
    @winrt_commethod(6)
    def get_Response(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Response = property(get_Response, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreSendRequestResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreSendRequestResult2'
    _iid_ = Guid('{2901296f-c0b0-49d0-8e8d-aa940af9c10b}')
    @winrt_commethod(6)
    def get_HttpStatusCode(self) -> win32more.Windows.Web.Http.HttpStatusCode: ...
    HttpStatusCode = property(get_HttpStatusCode, None)
class IStoreSku(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreSku'
    _iid_ = Guid('{397e6f55-4440-4f03-863c-91f3fec83d79}')
    @winrt_commethod(6)
    def get_StoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_CustomDeveloperData(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Images(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreImage]: ...
    @winrt_commethod(13)
    def get_Videos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreVideo]: ...
    @winrt_commethod(14)
    def get_Availabilities(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreAvailability]: ...
    @winrt_commethod(15)
    def get_Price(self) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_commethod(16)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_IsInUserCollection(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_BundledSkus(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(19)
    def get_CollectionData(self) -> win32more.Windows.Services.Store.StoreCollectionData: ...
    @winrt_commethod(20)
    def GetIsInstalledAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(23)
    def get_IsSubscription(self) -> Boolean: ...
    @winrt_commethod(24)
    def get_SubscriptionInfo(self) -> win32more.Windows.Services.Store.StoreSubscriptionInfo: ...
    StoreId = property(get_StoreId, None)
    Language = property(get_Language, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    IsTrial = property(get_IsTrial, None)
    CustomDeveloperData = property(get_CustomDeveloperData, None)
    Images = property(get_Images, None)
    Videos = property(get_Videos, None)
    Availabilities = property(get_Availabilities, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    IsInUserCollection = property(get_IsInUserCollection, None)
    BundledSkus = property(get_BundledSkus, None)
    CollectionData = property(get_CollectionData, None)
    IsSubscription = property(get_IsSubscription, None)
    SubscriptionInfo = property(get_SubscriptionInfo, None)
class IStoreSubscriptionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreSubscriptionInfo'
    _iid_ = Guid('{4189776a-0559-43ac-a9c6-3ab0011fb8eb}')
    @winrt_commethod(6)
    def get_BillingPeriod(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_BillingPeriodUnit(self) -> win32more.Windows.Services.Store.StoreDurationUnit: ...
    @winrt_commethod(8)
    def get_HasTrialPeriod(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_TrialPeriod(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_TrialPeriodUnit(self) -> win32more.Windows.Services.Store.StoreDurationUnit: ...
    BillingPeriod = property(get_BillingPeriod, None)
    BillingPeriodUnit = property(get_BillingPeriodUnit, None)
    HasTrialPeriod = property(get_HasTrialPeriod, None)
    TrialPeriod = property(get_TrialPeriod, None)
    TrialPeriodUnit = property(get_TrialPeriodUnit, None)
class IStoreUninstallStorePackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreUninstallStorePackageResult'
    _iid_ = Guid('{9fca39fd-126f-4cda-b801-1346b8d0a260}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Services.Store.StoreUninstallStorePackageStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IStoreVideo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.IStoreVideo'
    _iid_ = Guid('{f26cb184-6f5e-4dc2-886c-3c63083c2f94}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_VideoPurposeTag(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PreviewImage(self) -> win32more.Windows.Services.Store.StoreImage: ...
    Uri = property(get_Uri, None)
    VideoPurposeTag = property(get_VideoPurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
    PreviewImage = property(get_PreviewImage, None)
class StoreAcquireLicenseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreAcquireLicenseResult
    _classid_ = 'Windows.Services.Store.StoreAcquireLicenseResult'
    @winrt_mixinmethod
    def get_StorePackageLicense(self: win32more.Windows.Services.Store.IStoreAcquireLicenseResult) -> win32more.Windows.Services.Store.StorePackageLicense: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreAcquireLicenseResult) -> win32more.Windows.Foundation.HResult: ...
    StorePackageLicense = property(get_StorePackageLicense, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreAppLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreAppLicense
    _classid_ = 'Windows.Services.Store.StoreAppLicense'
    @winrt_mixinmethod
    def get_SkuStoreId(self: win32more.Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTrial(self: win32more.Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.Services.Store.IStoreAppLicense) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AddOnLicenses(self: win32more.Windows.Services.Store.IStoreAppLicense) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreLicense]: ...
    @winrt_mixinmethod
    def get_TrialTimeRemaining(self: win32more.Windows.Services.Store.IStoreAppLicense) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsTrialOwnedByThisUser(self: win32more.Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_TrialUniqueId(self: win32more.Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsDiscLicense(self: win32more.Windows.Services.Store.IStoreAppLicense2) -> Boolean: ...
    SkuStoreId = property(get_SkuStoreId, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    AddOnLicenses = property(get_AddOnLicenses, None)
    TrialTimeRemaining = property(get_TrialTimeRemaining, None)
    IsTrialOwnedByThisUser = property(get_IsTrialOwnedByThisUser, None)
    TrialUniqueId = property(get_TrialUniqueId, None)
    IsDiscLicense = property(get_IsDiscLicense, None)
class StoreAvailability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreAvailability
    _classid_ = 'Windows.Services.Store.StoreAvailability'
    @winrt_mixinmethod
    def get_StoreId(self: win32more.Windows.Services.Store.IStoreAvailability) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EndDate(self: win32more.Windows.Services.Store.IStoreAvailability) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Price(self: win32more.Windows.Services.Store.IStoreAvailability) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreAvailability) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: win32more.Windows.Services.Store.IStoreAvailability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: win32more.Windows.Services.Store.IStoreAvailability, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    StoreId = property(get_StoreId, None)
    EndDate = property(get_EndDate, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class StoreCanAcquireLicenseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreCanAcquireLicenseResult
    _classid_ = 'Windows.Services.Store.StoreCanAcquireLicenseResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreCanAcquireLicenseResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_LicensableSku(self: win32more.Windows.Services.Store.IStoreCanAcquireLicenseResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStoreCanAcquireLicenseResult) -> win32more.Windows.Services.Store.StoreCanLicenseStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LicensableSku = property(get_LicensableSku, None)
    Status = property(get_Status, None)
StoreCanLicenseStatus = Int32
StoreCanLicenseStatus_NotLicensableToUser: StoreCanLicenseStatus = 0
StoreCanLicenseStatus_Licensable: StoreCanLicenseStatus = 1
StoreCanLicenseStatus_LicenseActionNotApplicableToProduct: StoreCanLicenseStatus = 2
StoreCanLicenseStatus_NetworkError: StoreCanLicenseStatus = 3
StoreCanLicenseStatus_ServerError: StoreCanLicenseStatus = 4
class StoreCollectionData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreCollectionData
    _classid_ = 'Windows.Services.Store.StoreCollectionData'
    @winrt_mixinmethod
    def get_IsTrial(self: win32more.Windows.Services.Store.IStoreCollectionData) -> Boolean: ...
    @winrt_mixinmethod
    def get_CampaignId(self: win32more.Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeveloperOfferId(self: win32more.Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AcquiredDate(self: win32more.Windows.Services.Store.IStoreCollectionData) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_StartDate(self: win32more.Windows.Services.Store.IStoreCollectionData) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndDate(self: win32more.Windows.Services.Store.IStoreCollectionData) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_TrialTimeRemaining(self: win32more.Windows.Services.Store.IStoreCollectionData) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    IsTrial = property(get_IsTrial, None)
    CampaignId = property(get_CampaignId, None)
    DeveloperOfferId = property(get_DeveloperOfferId, None)
    AcquiredDate = property(get_AcquiredDate, None)
    StartDate = property(get_StartDate, None)
    EndDate = property(get_EndDate, None)
    TrialTimeRemaining = property(get_TrialTimeRemaining, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class StoreConsumableResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreConsumableResult
    _classid_ = 'Windows.Services.Store.StoreConsumableResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStoreConsumableResult) -> win32more.Windows.Services.Store.StoreConsumableStatus: ...
    @winrt_mixinmethod
    def get_TrackingId(self: win32more.Windows.Services.Store.IStoreConsumableResult) -> Guid: ...
    @winrt_mixinmethod
    def get_BalanceRemaining(self: win32more.Windows.Services.Store.IStoreConsumableResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreConsumableResult) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    TrackingId = property(get_TrackingId, None)
    BalanceRemaining = property(get_BalanceRemaining, None)
    ExtendedError = property(get_ExtendedError, None)
StoreConsumableStatus = Int32
StoreConsumableStatus_Succeeded: StoreConsumableStatus = 0
StoreConsumableStatus_InsufficentQuantity: StoreConsumableStatus = 1
StoreConsumableStatus_NetworkError: StoreConsumableStatus = 2
StoreConsumableStatus_ServerError: StoreConsumableStatus = 3
class StoreContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreContext
    _classid_ = 'Windows.Services.Store.StoreContext'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Services.Store.IStoreContext) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def add_OfflineLicensesChanged(self: win32more.Windows.Services.Store.IStoreContext, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreContext, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OfflineLicensesChanged(self: win32more.Windows.Services.Store.IStoreContext, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCustomerPurchaseIdAsync(self: win32more.Windows.Services.Store.IStoreContext, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetCustomerCollectionsIdAsync(self: win32more.Windows.Services.Store.IStoreContext, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAppLicenseAsync(self: win32more.Windows.Services.Store.IStoreContext) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreAppLicense]: ...
    @winrt_mixinmethod
    def GetStoreProductForCurrentAppAsync(self: win32more.Windows.Services.Store.IStoreContext) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductResult]: ...
    @winrt_mixinmethod
    def GetStoreProductsAsync(self: win32more.Windows.Services.Store.IStoreContext, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreProductsAsync(self: win32more.Windows.Services.Store.IStoreContext, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreProductsWithPagingAsync(self: win32more.Windows.Services.Store.IStoreContext, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_mixinmethod
    def GetUserCollectionAsync(self: win32more.Windows.Services.Store.IStoreContext, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetUserCollectionWithPagingAsync(self: win32more.Windows.Services.Store.IStoreContext, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_mixinmethod
    def ReportConsumableFulfillmentAsync(self: win32more.Windows.Services.Store.IStoreContext, productStoreId: WinRT_String, quantity: UInt32, trackingId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_mixinmethod
    def GetConsumableBalanceRemainingAsync(self: win32more.Windows.Services.Store.IStoreContext, productStoreId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_mixinmethod
    def AcquireStoreLicenseForOptionalPackageAsync(self: win32more.Windows.Services.Store.IStoreContext, optionalPackage: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: win32more.Windows.Services.Store.IStoreContext, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: win32more.Windows.Services.Store.IStoreContext, storeId: WinRT_String, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def GetAppAndOptionalStorePackageUpdatesAsync(self: win32more.Windows.Services.Store.IStoreContext) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StorePackageUpdate]]: ...
    @winrt_mixinmethod
    def RequestDownloadStorePackageUpdatesAsync(self: win32more.Windows.Services.Store.IStoreContext, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackageUpdatesAsync(self: win32more.Windows.Services.Store.IStoreContext, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackagesAsync(self: win32more.Windows.Services.Store.IStoreContext, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def FindStoreProductForPackageAsync(self: win32more.Windows.Services.Store.IStoreContext2, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductResult]: ...
    @winrt_mixinmethod
    def get_CanSilentlyDownloadStorePackageUpdates(self: win32more.Windows.Services.Store.IStoreContext3) -> Boolean: ...
    @winrt_mixinmethod
    def TrySilentDownloadStorePackageUpdatesAsync(self: win32more.Windows.Services.Store.IStoreContext3, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def TrySilentDownloadAndInstallStorePackageUpdatesAsync(self: win32more.Windows.Services.Store.IStoreContext3, storePackageUpdates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StorePackageUpdate]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def CanAcquireStoreLicenseForOptionalPackageAsync(self: win32more.Windows.Services.Store.IStoreContext3, optionalPackage: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def CanAcquireStoreLicenseAsync(self: win32more.Windows.Services.Store.IStoreContext3, productStoreId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def GetStoreProductsWithOptionsAsync(self: win32more.Windows.Services.Store.IStoreContext3, productKinds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storeProductOptions: win32more.Windows.Services.Store.StoreProductOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreQueueItemsAsync(self: win32more.Windows.Services.Store.IStoreContext3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_mixinmethod
    def GetStoreQueueItemsAsync(self: win32more.Windows.Services.Store.IStoreContext3, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackagesWithInstallOptionsAsync(self: win32more.Windows.Services.Store.IStoreContext3, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], storePackageInstallOptions: win32more.Windows.Services.Store.StorePackageInstallOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def DownloadAndInstallStorePackagesAsync(self: win32more.Windows.Services.Store.IStoreContext3, storeIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Services.Store.StorePackageUpdateResult, win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestUninstallStorePackageAsync(self: win32more.Windows.Services.Store.IStoreContext3, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def RequestUninstallStorePackageByStoreIdAsync(self: win32more.Windows.Services.Store.IStoreContext3, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def UninstallStorePackageAsync(self: win32more.Windows.Services.Store.IStoreContext3, package: win32more.Windows.ApplicationModel.Package) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def UninstallStorePackageByStoreIdAsync(self: win32more.Windows.Services.Store.IStoreContext3, storeId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def RequestRateAndReviewAppAsync(self: win32more.Windows.Services.Store.IStoreContext4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreRateAndReviewResult]: ...
    @winrt_mixinmethod
    def SetInstallOrderForAssociatedStoreQueueItemsAsync(self: win32more.Windows.Services.Store.IStoreContext4, items: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Store.StoreQueueItem]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Services.Store.IStoreContextStatics) -> win32more.Windows.Services.Store.StoreContext: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Services.Store.IStoreContextStatics, user: win32more.Windows.System.User) -> win32more.Windows.Services.Store.StoreContext: ...
    User = property(get_User, None)
    CanSilentlyDownloadStorePackageUpdates = property(get_CanSilentlyDownloadStorePackageUpdates, None)
StoreContract: UInt32 = 262144
StoreDurationUnit = Int32
StoreDurationUnit_Minute: StoreDurationUnit = 0
StoreDurationUnit_Hour: StoreDurationUnit = 1
StoreDurationUnit_Day: StoreDurationUnit = 2
StoreDurationUnit_Week: StoreDurationUnit = 3
StoreDurationUnit_Month: StoreDurationUnit = 4
StoreDurationUnit_Year: StoreDurationUnit = 5
class StoreImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreImage
    _classid_ = 'Windows.Services.Store.StoreImage'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Services.Store.IStoreImage) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ImagePurposeTag(self: win32more.Windows.Services.Store.IStoreImage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Services.Store.IStoreImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Services.Store.IStoreImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Caption(self: win32more.Windows.Services.Store.IStoreImage) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    ImagePurposeTag = property(get_ImagePurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
class StoreLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreLicense
    _classid_ = 'Windows.Services.Store.StoreLicense'
    @winrt_mixinmethod
    def get_SkuStoreId(self: win32more.Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.Services.Store.IStoreLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.Services.Store.IStoreLicense) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InAppOfferToken(self: win32more.Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    SkuStoreId = property(get_SkuStoreId, None)
    IsActive = property(get_IsActive, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    InAppOfferToken = property(get_InAppOfferToken, None)
class StorePackageInstallOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePackageInstallOptions
    _classid_ = 'Windows.Services.Store.StorePackageInstallOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Store.StorePackageInstallOptions: ...
    @winrt_mixinmethod
    def get_AllowForcedAppRestart(self: win32more.Windows.Services.Store.IStorePackageInstallOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowForcedAppRestart(self: win32more.Windows.Services.Store.IStorePackageInstallOptions, value: Boolean) -> Void: ...
    AllowForcedAppRestart = property(get_AllowForcedAppRestart, put_AllowForcedAppRestart)
class StorePackageLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePackageLicense
    _classid_ = 'Windows.Services.Store.StorePackageLicense'
    @winrt_mixinmethod
    def add_LicenseLost(self: win32more.Windows.Services.Store.IStorePackageLicense, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StorePackageLicense, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseLost(self: win32more.Windows.Services.Store.IStorePackageLicense, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.Services.Store.IStorePackageLicense) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_IsValid(self: win32more.Windows.Services.Store.IStorePackageLicense) -> Boolean: ...
    @winrt_mixinmethod
    def ReleaseLicense(self: win32more.Windows.Services.Store.IStorePackageLicense) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Package = property(get_Package, None)
    IsValid = property(get_IsValid, None)
class StorePackageUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePackageUpdate
    _classid_ = 'Windows.Services.Store.StorePackageUpdate'
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.Services.Store.IStorePackageUpdate) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Mandatory(self: win32more.Windows.Services.Store.IStorePackageUpdate) -> Boolean: ...
    Package = property(get_Package, None)
    Mandatory = property(get_Mandatory, None)
class StorePackageUpdateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePackageUpdateResult
    _classid_ = 'Windows.Services.Store.StorePackageUpdateResult'
    @winrt_mixinmethod
    def get_OverallState(self: win32more.Windows.Services.Store.IStorePackageUpdateResult) -> win32more.Windows.Services.Store.StorePackageUpdateState: ...
    @winrt_mixinmethod
    def get_StorePackageUpdateStatuses(self: win32more.Windows.Services.Store.IStorePackageUpdateResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def get_StoreQueueItems(self: win32more.Windows.Services.Store.IStorePackageUpdateResult2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreQueueItem]: ...
    OverallState = property(get_OverallState, None)
    StorePackageUpdateStatuses = property(get_StorePackageUpdateStatuses, None)
    StoreQueueItems = property(get_StoreQueueItems, None)
StorePackageUpdateState = Int32
StorePackageUpdateState_Pending: StorePackageUpdateState = 0
StorePackageUpdateState_Downloading: StorePackageUpdateState = 1
StorePackageUpdateState_Deploying: StorePackageUpdateState = 2
StorePackageUpdateState_Completed: StorePackageUpdateState = 3
StorePackageUpdateState_Canceled: StorePackageUpdateState = 4
StorePackageUpdateState_OtherError: StorePackageUpdateState = 5
StorePackageUpdateState_ErrorLowBattery: StorePackageUpdateState = 6
StorePackageUpdateState_ErrorWiFiRecommended: StorePackageUpdateState = 7
StorePackageUpdateState_ErrorWiFiRequired: StorePackageUpdateState = 8
class StorePackageUpdateStatus(EasyCastStructure):
    PackageFamilyName: WinRT_String
    PackageDownloadSizeInBytes: UInt64
    PackageBytesDownloaded: UInt64
    PackageDownloadProgress: Double
    TotalDownloadProgress: Double
    PackageUpdateState: win32more.Windows.Services.Store.StorePackageUpdateState
class StorePrice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePrice
    _classid_ = 'Windows.Services.Store.StorePrice'
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: win32more.Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: win32more.Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: win32more.Windows.Services.Store.IStorePrice) -> Boolean: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: win32more.Windows.Services.Store.IStorePrice) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: win32more.Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedRecurrencePrice(self: win32more.Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    FormattedPrice = property(get_FormattedPrice, None)
    IsOnSale = property(get_IsOnSale, None)
    SaleEndDate = property(get_SaleEndDate, None)
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedRecurrencePrice = property(get_FormattedRecurrencePrice, None)
class StoreProduct(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreProduct
    _classid_ = 'Windows.Services.Store.StoreProduct'
    @winrt_mixinmethod
    def get_StoreId(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductKind(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasDigitalDownload(self: win32more.Windows.Services.Store.IStoreProduct) -> Boolean: ...
    @winrt_mixinmethod
    def get_Keywords(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Images(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreImage]: ...
    @winrt_mixinmethod
    def get_Videos(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreVideo]: ...
    @winrt_mixinmethod
    def get_Skus(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreSku]: ...
    @winrt_mixinmethod
    def get_IsInUserCollection(self: win32more.Windows.Services.Store.IStoreProduct) -> Boolean: ...
    @winrt_mixinmethod
    def get_Price(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinkUri(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetIsAnySkuInstalledAsync(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: win32more.Windows.Services.Store.IStoreProduct) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: win32more.Windows.Services.Store.IStoreProduct, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def get_InAppOfferToken(self: win32more.Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    StoreId = property(get_StoreId, None)
    Language = property(get_Language, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    ProductKind = property(get_ProductKind, None)
    HasDigitalDownload = property(get_HasDigitalDownload, None)
    Keywords = property(get_Keywords, None)
    Images = property(get_Images, None)
    Videos = property(get_Videos, None)
    Skus = property(get_Skus, None)
    IsInUserCollection = property(get_IsInUserCollection, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    LinkUri = property(get_LinkUri, None)
    InAppOfferToken = property(get_InAppOfferToken, None)
class StoreProductOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreProductOptions
    _classid_ = 'Windows.Services.Store.StoreProductOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Store.StoreProductOptions: ...
    @winrt_mixinmethod
    def get_ActionFilters(self: win32more.Windows.Services.Store.IStoreProductOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ActionFilters = property(get_ActionFilters, None)
class StoreProductPagedQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreProductPagedQueryResult
    _classid_ = 'Windows.Services.Store.StoreProductPagedQueryResult'
    @winrt_mixinmethod
    def get_Products(self: win32more.Windows.Services.Store.IStoreProductPagedQueryResult) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreProduct]: ...
    @winrt_mixinmethod
    def get_HasMoreResults(self: win32more.Windows.Services.Store.IStoreProductPagedQueryResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreProductPagedQueryResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def GetNextAsync(self: win32more.Windows.Services.Store.IStoreProductPagedQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreProductPagedQueryResult]: ...
    Products = property(get_Products, None)
    HasMoreResults = property(get_HasMoreResults, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreProductQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreProductQueryResult
    _classid_ = 'Windows.Services.Store.StoreProductQueryResult'
    @winrt_mixinmethod
    def get_Products(self: win32more.Windows.Services.Store.IStoreProductQueryResult) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.Store.StoreProduct]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreProductQueryResult) -> win32more.Windows.Foundation.HResult: ...
    Products = property(get_Products, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreProductResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreProductResult
    _classid_ = 'Windows.Services.Store.StoreProductResult'
    @winrt_mixinmethod
    def get_Product(self: win32more.Windows.Services.Store.IStoreProductResult) -> win32more.Windows.Services.Store.StoreProduct: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreProductResult) -> win32more.Windows.Foundation.HResult: ...
    Product = property(get_Product, None)
    ExtendedError = property(get_ExtendedError, None)
class StorePurchaseProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePurchaseProperties
    _classid_ = 'Windows.Services.Store.StorePurchaseProperties'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Services.Store.IStorePurchasePropertiesFactory, name: WinRT_String) -> win32more.Windows.Services.Store.StorePurchaseProperties: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Store.StorePurchaseProperties: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Services.Store.IStorePurchaseProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Services.Store.IStorePurchaseProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStorePurchaseProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExtendedJsonData(self: win32more.Windows.Services.Store.IStorePurchaseProperties, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    ExtendedJsonData = property(get_ExtendedJsonData, put_ExtendedJsonData)
class StorePurchaseResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStorePurchaseResult
    _classid_ = 'Windows.Services.Store.StorePurchaseResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStorePurchaseResult) -> win32more.Windows.Services.Store.StorePurchaseStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStorePurchaseResult) -> win32more.Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
StorePurchaseStatus = Int32
StorePurchaseStatus_Succeeded: StorePurchaseStatus = 0
StorePurchaseStatus_AlreadyPurchased: StorePurchaseStatus = 1
StorePurchaseStatus_NotPurchased: StorePurchaseStatus = 2
StorePurchaseStatus_NetworkError: StorePurchaseStatus = 3
StorePurchaseStatus_ServerError: StorePurchaseStatus = 4
class StoreQueueItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreQueueItem
    _classid_ = 'Windows.Services.Store.StoreQueueItem'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.Services.Store.IStoreQueueItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.Services.Store.IStoreQueueItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstallKind(self: win32more.Windows.Services.Store.IStoreQueueItem) -> win32more.Windows.Services.Store.StoreQueueItemKind: ...
    @winrt_mixinmethod
    def GetCurrentStatus(self: win32more.Windows.Services.Store.IStoreQueueItem) -> win32more.Windows.Services.Store.StoreQueueItemStatus: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.Services.Store.IStoreQueueItem, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreQueueItem, win32more.Windows.Services.Store.StoreQueueItemCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.Services.Store.IStoreQueueItem, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Services.Store.IStoreQueueItem, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Store.StoreQueueItem, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Services.Store.IStoreQueueItem, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CancelInstallAsync(self: win32more.Windows.Services.Store.IStoreQueueItem2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseInstallAsync(self: win32more.Windows.Services.Store.IStoreQueueItem2) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeInstallAsync(self: win32more.Windows.Services.Store.IStoreQueueItem2) -> win32more.Windows.Foundation.IAsyncAction: ...
    ProductId = property(get_ProductId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    InstallKind = property(get_InstallKind, None)
class StoreQueueItemCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreQueueItemCompletedEventArgs
    _classid_ = 'Windows.Services.Store.StoreQueueItemCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStoreQueueItemCompletedEventArgs) -> win32more.Windows.Services.Store.StoreQueueItemStatus: ...
    Status = property(get_Status, None)
StoreQueueItemExtendedState = Int32
StoreQueueItemExtendedState_ActivePending: StoreQueueItemExtendedState = 0
StoreQueueItemExtendedState_ActiveStarting: StoreQueueItemExtendedState = 1
StoreQueueItemExtendedState_ActiveAcquiringLicense: StoreQueueItemExtendedState = 2
StoreQueueItemExtendedState_ActiveDownloading: StoreQueueItemExtendedState = 3
StoreQueueItemExtendedState_ActiveRestoringData: StoreQueueItemExtendedState = 4
StoreQueueItemExtendedState_ActiveInstalling: StoreQueueItemExtendedState = 5
StoreQueueItemExtendedState_Completed: StoreQueueItemExtendedState = 6
StoreQueueItemExtendedState_Canceled: StoreQueueItemExtendedState = 7
StoreQueueItemExtendedState_Paused: StoreQueueItemExtendedState = 8
StoreQueueItemExtendedState_Error: StoreQueueItemExtendedState = 9
StoreQueueItemExtendedState_PausedPackagesInUse: StoreQueueItemExtendedState = 10
StoreQueueItemExtendedState_PausedLowBattery: StoreQueueItemExtendedState = 11
StoreQueueItemExtendedState_PausedWiFiRecommended: StoreQueueItemExtendedState = 12
StoreQueueItemExtendedState_PausedWiFiRequired: StoreQueueItemExtendedState = 13
StoreQueueItemExtendedState_PausedReadyToInstall: StoreQueueItemExtendedState = 14
StoreQueueItemKind = Int32
StoreQueueItemKind_Install: StoreQueueItemKind = 0
StoreQueueItemKind_Update: StoreQueueItemKind = 1
StoreQueueItemKind_Repair: StoreQueueItemKind = 2
StoreQueueItemState = Int32
StoreQueueItemState_Active: StoreQueueItemState = 0
StoreQueueItemState_Completed: StoreQueueItemState = 1
StoreQueueItemState_Canceled: StoreQueueItemState = 2
StoreQueueItemState_Error: StoreQueueItemState = 3
StoreQueueItemState_Paused: StoreQueueItemState = 4
class StoreQueueItemStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreQueueItemStatus
    _classid_ = 'Windows.Services.Store.StoreQueueItemStatus'
    @winrt_mixinmethod
    def get_PackageInstallState(self: win32more.Windows.Services.Store.IStoreQueueItemStatus) -> win32more.Windows.Services.Store.StoreQueueItemState: ...
    @winrt_mixinmethod
    def get_PackageInstallExtendedState(self: win32more.Windows.Services.Store.IStoreQueueItemStatus) -> win32more.Windows.Services.Store.StoreQueueItemExtendedState: ...
    @winrt_mixinmethod
    def get_UpdateStatus(self: win32more.Windows.Services.Store.IStoreQueueItemStatus) -> win32more.Windows.Services.Store.StorePackageUpdateStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreQueueItemStatus) -> win32more.Windows.Foundation.HResult: ...
    PackageInstallState = property(get_PackageInstallState, None)
    PackageInstallExtendedState = property(get_PackageInstallExtendedState, None)
    UpdateStatus = property(get_UpdateStatus, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreRateAndReviewResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreRateAndReviewResult
    _classid_ = 'Windows.Services.Store.StoreRateAndReviewResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreRateAndReviewResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreRateAndReviewResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WasUpdated(self: win32more.Windows.Services.Store.IStoreRateAndReviewResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStoreRateAndReviewResult) -> win32more.Windows.Services.Store.StoreRateAndReviewStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    WasUpdated = property(get_WasUpdated, None)
    Status = property(get_Status, None)
StoreRateAndReviewStatus = Int32
StoreRateAndReviewStatus_Succeeded: StoreRateAndReviewStatus = 0
StoreRateAndReviewStatus_CanceledByUser: StoreRateAndReviewStatus = 1
StoreRateAndReviewStatus_NetworkError: StoreRateAndReviewStatus = 2
StoreRateAndReviewStatus_Error: StoreRateAndReviewStatus = 3
class StoreRequestHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Store.StoreRequestHelper'
    @winrt_classmethod
    def SendRequestAsync(cls: win32more.Windows.Services.Store.IStoreRequestHelperStatics, context: win32more.Windows.Services.Store.StoreContext, requestKind: UInt32, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StoreSendRequestResult]: ...
class StoreSendRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreSendRequestResult
    _classid_ = 'Windows.Services.Store.StoreSendRequestResult'
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.Services.Store.IStoreSendRequestResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreSendRequestResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_HttpStatusCode(self: win32more.Windows.Services.Store.IStoreSendRequestResult2) -> win32more.Windows.Web.Http.HttpStatusCode: ...
    Response = property(get_Response, None)
    ExtendedError = property(get_ExtendedError, None)
    HttpStatusCode = property(get_HttpStatusCode, None)
class StoreSku(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreSku
    _classid_ = 'Windows.Services.Store.StoreSku'
    @winrt_mixinmethod
    def get_StoreId(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsTrial(self: win32more.Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_CustomDeveloperData(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Images(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreImage]: ...
    @winrt_mixinmethod
    def get_Videos(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreVideo]: ...
    @winrt_mixinmethod
    def get_Availabilities(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Store.StoreAvailability]: ...
    @winrt_mixinmethod
    def get_Price(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: win32more.Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsInUserCollection(self: win32more.Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_BundledSkus(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_CollectionData(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Services.Store.StoreCollectionData: ...
    @winrt_mixinmethod
    def GetIsInstalledAsync(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: win32more.Windows.Services.Store.IStoreSku, storePurchaseProperties: win32more.Windows.Services.Store.StorePurchaseProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def get_IsSubscription(self: win32more.Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_SubscriptionInfo(self: win32more.Windows.Services.Store.IStoreSku) -> win32more.Windows.Services.Store.StoreSubscriptionInfo: ...
    StoreId = property(get_StoreId, None)
    Language = property(get_Language, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    IsTrial = property(get_IsTrial, None)
    CustomDeveloperData = property(get_CustomDeveloperData, None)
    Images = property(get_Images, None)
    Videos = property(get_Videos, None)
    Availabilities = property(get_Availabilities, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    IsInUserCollection = property(get_IsInUserCollection, None)
    BundledSkus = property(get_BundledSkus, None)
    CollectionData = property(get_CollectionData, None)
    IsSubscription = property(get_IsSubscription, None)
    SubscriptionInfo = property(get_SubscriptionInfo, None)
class StoreSubscriptionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreSubscriptionInfo
    _classid_ = 'Windows.Services.Store.StoreSubscriptionInfo'
    @winrt_mixinmethod
    def get_BillingPeriod(self: win32more.Windows.Services.Store.IStoreSubscriptionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_BillingPeriodUnit(self: win32more.Windows.Services.Store.IStoreSubscriptionInfo) -> win32more.Windows.Services.Store.StoreDurationUnit: ...
    @winrt_mixinmethod
    def get_HasTrialPeriod(self: win32more.Windows.Services.Store.IStoreSubscriptionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_TrialPeriod(self: win32more.Windows.Services.Store.IStoreSubscriptionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrialPeriodUnit(self: win32more.Windows.Services.Store.IStoreSubscriptionInfo) -> win32more.Windows.Services.Store.StoreDurationUnit: ...
    BillingPeriod = property(get_BillingPeriod, None)
    BillingPeriodUnit = property(get_BillingPeriodUnit, None)
    HasTrialPeriod = property(get_HasTrialPeriod, None)
    TrialPeriod = property(get_TrialPeriod, None)
    TrialPeriodUnit = property(get_TrialPeriodUnit, None)
class StoreUninstallStorePackageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreUninstallStorePackageResult
    _classid_ = 'Windows.Services.Store.StoreUninstallStorePackageResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Services.Store.IStoreUninstallStorePackageResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Store.IStoreUninstallStorePackageResult) -> win32more.Windows.Services.Store.StoreUninstallStorePackageStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
StoreUninstallStorePackageStatus = Int32
StoreUninstallStorePackageStatus_Succeeded: StoreUninstallStorePackageStatus = 0
StoreUninstallStorePackageStatus_CanceledByUser: StoreUninstallStorePackageStatus = 1
StoreUninstallStorePackageStatus_NetworkError: StoreUninstallStorePackageStatus = 2
StoreUninstallStorePackageStatus_UninstallNotApplicable: StoreUninstallStorePackageStatus = 3
StoreUninstallStorePackageStatus_Error: StoreUninstallStorePackageStatus = 4
class StoreVideo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Store.IStoreVideo
    _classid_ = 'Windows.Services.Store.StoreVideo'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Services.Store.IStoreVideo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_VideoPurposeTag(self: win32more.Windows.Services.Store.IStoreVideo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Services.Store.IStoreVideo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Services.Store.IStoreVideo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Caption(self: win32more.Windows.Services.Store.IStoreVideo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PreviewImage(self: win32more.Windows.Services.Store.IStoreVideo) -> win32more.Windows.Services.Store.StoreImage: ...
    Uri = property(get_Uri, None)
    VideoPurposeTag = property(get_VideoPurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
    PreviewImage = property(get_PreviewImage, None)
make_head(_module, 'IStoreAcquireLicenseResult')
make_head(_module, 'IStoreAppLicense')
make_head(_module, 'IStoreAppLicense2')
make_head(_module, 'IStoreAvailability')
make_head(_module, 'IStoreCanAcquireLicenseResult')
make_head(_module, 'IStoreCollectionData')
make_head(_module, 'IStoreConsumableResult')
make_head(_module, 'IStoreContext')
make_head(_module, 'IStoreContext2')
make_head(_module, 'IStoreContext3')
make_head(_module, 'IStoreContext4')
make_head(_module, 'IStoreContextStatics')
make_head(_module, 'IStoreImage')
make_head(_module, 'IStoreLicense')
make_head(_module, 'IStorePackageInstallOptions')
make_head(_module, 'IStorePackageLicense')
make_head(_module, 'IStorePackageUpdate')
make_head(_module, 'IStorePackageUpdateResult')
make_head(_module, 'IStorePackageUpdateResult2')
make_head(_module, 'IStorePrice')
make_head(_module, 'IStoreProduct')
make_head(_module, 'IStoreProductOptions')
make_head(_module, 'IStoreProductPagedQueryResult')
make_head(_module, 'IStoreProductQueryResult')
make_head(_module, 'IStoreProductResult')
make_head(_module, 'IStorePurchaseProperties')
make_head(_module, 'IStorePurchasePropertiesFactory')
make_head(_module, 'IStorePurchaseResult')
make_head(_module, 'IStoreQueueItem')
make_head(_module, 'IStoreQueueItem2')
make_head(_module, 'IStoreQueueItemCompletedEventArgs')
make_head(_module, 'IStoreQueueItemStatus')
make_head(_module, 'IStoreRateAndReviewResult')
make_head(_module, 'IStoreRequestHelperStatics')
make_head(_module, 'IStoreSendRequestResult')
make_head(_module, 'IStoreSendRequestResult2')
make_head(_module, 'IStoreSku')
make_head(_module, 'IStoreSubscriptionInfo')
make_head(_module, 'IStoreUninstallStorePackageResult')
make_head(_module, 'IStoreVideo')
make_head(_module, 'StoreAcquireLicenseResult')
make_head(_module, 'StoreAppLicense')
make_head(_module, 'StoreAvailability')
make_head(_module, 'StoreCanAcquireLicenseResult')
make_head(_module, 'StoreCollectionData')
make_head(_module, 'StoreConsumableResult')
make_head(_module, 'StoreContext')
make_head(_module, 'StoreImage')
make_head(_module, 'StoreLicense')
make_head(_module, 'StorePackageInstallOptions')
make_head(_module, 'StorePackageLicense')
make_head(_module, 'StorePackageUpdate')
make_head(_module, 'StorePackageUpdateResult')
make_head(_module, 'StorePackageUpdateStatus')
make_head(_module, 'StorePrice')
make_head(_module, 'StoreProduct')
make_head(_module, 'StoreProductOptions')
make_head(_module, 'StoreProductPagedQueryResult')
make_head(_module, 'StoreProductQueryResult')
make_head(_module, 'StoreProductResult')
make_head(_module, 'StorePurchaseProperties')
make_head(_module, 'StorePurchaseResult')
make_head(_module, 'StoreQueueItem')
make_head(_module, 'StoreQueueItemCompletedEventArgs')
make_head(_module, 'StoreQueueItemStatus')
make_head(_module, 'StoreRateAndReviewResult')
make_head(_module, 'StoreRequestHelper')
make_head(_module, 'StoreSendRequestResult')
make_head(_module, 'StoreSku')
make_head(_module, 'StoreSubscriptionInfo')
make_head(_module, 'StoreUninstallStorePackageResult')
make_head(_module, 'StoreVideo')
