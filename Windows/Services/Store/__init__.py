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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Services.Store
import Windows.System
import Windows.Web.Http
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fbd7946d-f040-4cb3-9a-39-29-bc-ec-db-e2-2d')
    @winrt_commethod(6)
    def get_StorePackageLicense(self) -> Windows.Services.Store.StorePackageLicense: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    StorePackageLicense = property(get_StorePackageLicense, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreAppLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f389f9de-73c0-45ce-9b-ab-b2-fe-3e-5e-af-d3')
    @winrt_commethod(6)
    def get_SkuStoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExpirationDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AddOnLicenses(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreLicense]: ...
    @winrt_commethod(12)
    def get_TrialTimeRemaining(self) -> Windows.Foundation.TimeSpan: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b4666e91-4443-40b3-99-3f-28-90-44-35-bd-c6')
    @winrt_commethod(6)
    def get_IsDiscLicense(self) -> Boolean: ...
    IsDiscLicense = property(get_IsDiscLicense, None)
class IStoreAvailability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fa060325-0ffd-4493-ad-43-f1-f9-91-8f-69-fa')
    @winrt_commethod(6)
    def get_StoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EndDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Price(self) -> Windows.Services.Store.StorePrice: ...
    @winrt_commethod(9)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def RequestPurchaseAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(11)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    StoreId = property(get_StoreId, None)
    EndDate = property(get_EndDate, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class IStoreCanAcquireLicenseResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3a693db3-0088-482f-86-d5-bd-46-52-26-63-ad')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_LicensableSku(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Services.Store.StoreCanLicenseStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LicensableSku = property(get_LicensableSku, None)
    Status = property(get_Status, None)
class IStoreCollectionData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8aa4c3b3-5bb3-441a-2a-b4-4d-ab-73-d5-ce-67')
    @winrt_commethod(6)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CampaignId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DeveloperOfferId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AcquiredDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_StartDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_EndDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_TrialTimeRemaining(self) -> Windows.Foundation.TimeSpan: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ea5dab72-6a00-4052-be-5b-bf-da-b4-43-33-52')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Store.StoreConsumableStatus: ...
    @winrt_commethod(7)
    def get_TrackingId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_BalanceRemaining(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    TrackingId = property(get_TrackingId, None)
    BalanceRemaining = property(get_BalanceRemaining, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ac98b6be-f4fd-4912-ba-bd-50-35-e5-e8-bc-ab')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def add_OfflineLicensesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreContext, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_OfflineLicensesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def GetCustomerPurchaseIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def GetCustomerCollectionsIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def GetAppLicenseAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreAppLicense]: ...
    @winrt_commethod(12)
    def GetStoreProductForCurrentAppAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductResult]: ...
    @winrt_commethod(13)
    def GetStoreProductsAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(14)
    def GetAssociatedStoreProductsAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(15)
    def GetAssociatedStoreProductsWithPagingAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_commethod(16)
    def GetUserCollectionAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(17)
    def GetUserCollectionWithPagingAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_commethod(18)
    def ReportConsumableFulfillmentAsync(self, productStoreId: WinRT_String, quantity: UInt32, trackingId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_commethod(19)
    def GetConsumableBalanceRemainingAsync(self, productStoreId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_commethod(20)
    def AcquireStoreLicenseForOptionalPackageAsync(self, optionalPackage: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreAcquireLicenseResult]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storeId: WinRT_String, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(23)
    def GetAppAndOptionalStorePackageUpdatesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StorePackageUpdate]]: ...
    @winrt_commethod(24)
    def RequestDownloadStorePackageUpdatesAsync(self, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(25)
    def RequestDownloadAndInstallStorePackageUpdatesAsync(self, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(26)
    def RequestDownloadAndInstallStorePackagesAsync(self, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    User = property(get_User, None)
class IStoreContext2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('18bc54da-7bd9-452c-91-16-3b-bd-06-ff-c6-3a')
    @winrt_commethod(6)
    def FindStoreProductForPackageAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductResult]: ...
class IStoreContext3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e26226ca-1a01-4730-85-a6-ec-c8-96-e4-ae-38')
    @winrt_commethod(6)
    def get_CanSilentlyDownloadStorePackageUpdates(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySilentDownloadStorePackageUpdatesAsync(self, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(8)
    def TrySilentDownloadAndInstallStorePackageUpdatesAsync(self, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(9)
    def CanAcquireStoreLicenseForOptionalPackageAsync(self, optionalPackage: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_commethod(10)
    def CanAcquireStoreLicenseAsync(self, productStoreId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_commethod(11)
    def GetStoreProductsWithOptionsAsync(self, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: Windows.Foundation.Collections.IIterable[WinRT_String], storeProductOptions: Windows.Services.Store.StoreProductOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_commethod(12)
    def GetAssociatedStoreQueueItemsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_commethod(13)
    def GetStoreQueueItemsAsync(self, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_commethod(14)
    def RequestDownloadAndInstallStorePackagesWithInstallOptionsAsync(self, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String], storePackageInstallOptions: Windows.Services.Store.StorePackageInstallOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(15)
    def DownloadAndInstallStorePackagesAsync(self, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_commethod(16)
    def RequestUninstallStorePackageAsync(self, package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(17)
    def RequestUninstallStorePackageByStoreIdAsync(self, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(18)
    def UninstallStorePackageAsync(self, package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_commethod(19)
    def UninstallStorePackageByStoreIdAsync(self, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    CanSilentlyDownloadStorePackageUpdates = property(get_CanSilentlyDownloadStorePackageUpdates, None)
class IStoreContext4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('af9c6f69-bea1-4bf4-8e-74-ae-03-e2-06-c6-b0')
    @winrt_commethod(6)
    def RequestRateAndReviewAppAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreRateAndReviewResult]: ...
    @winrt_commethod(7)
    def SetInstallOrderForAssociatedStoreQueueItemsAsync(self, items: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StoreQueueItem]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
class IStoreContextStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9c06ee5f-15c0-4e72-93-30-d6-19-1c-eb-d1-9c')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Services.Store.StoreContext: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.Services.Store.StoreContext: ...
class IStoreImage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('081fd248-adb4-4b64-a9-93-78-47-89-92-6e-d5')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('26dc9579-4c4f-4f30-bc-89-64-9f-60-e3-60-55')
    @winrt_commethod(6)
    def get_SkuStoreId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> Windows.Foundation.DateTime: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1d3d630c-0ccd-44dd-8c-59-80-81-0a-72-99-73')
    @winrt_commethod(6)
    def get_AllowForcedAppRestart(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowForcedAppRestart(self, value: Boolean) -> Void: ...
    AllowForcedAppRestart = property(get_AllowForcedAppRestart, put_AllowForcedAppRestart)
class IStorePackageLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0c465714-14e1-4973-bd-14-f7-77-24-27-1e-99')
    @winrt_commethod(6)
    def add_LicenseLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StorePackageLicense, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LicenseLost(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(9)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(10)
    def ReleaseLicense(self) -> Void: ...
    Package = property(get_Package, None)
    IsValid = property(get_IsValid, None)
class IStorePackageUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('140fa150-3cbf-4a35-b9-1f-48-27-1c-31-b0-72')
    @winrt_commethod(6)
    def get_Package(self) -> Windows.ApplicationModel.Package: ...
    @winrt_commethod(7)
    def get_Mandatory(self) -> Boolean: ...
    Package = property(get_Package, None)
    Mandatory = property(get_Mandatory, None)
class IStorePackageUpdateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e79142ed-61f9-4893-b4-fe-cf-19-16-03-af-7b')
    @winrt_commethod(6)
    def get_OverallState(self) -> Windows.Services.Store.StorePackageUpdateState: ...
    @winrt_commethod(7)
    def get_StorePackageUpdateStatuses(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StorePackageUpdateStatus]: ...
    OverallState = property(get_OverallState, None)
    StorePackageUpdateStatuses = property(get_StorePackageUpdateStatuses, None)
class IStorePackageUpdateResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('071d012e-bc62-4f2e-87-ea-99-d8-01-ae-af-98')
    @winrt_commethod(6)
    def get_StoreQueueItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]: ...
    StoreQueueItems = property(get_StoreQueueItems, None)
class IStorePrice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('55ba94c4-15f1-407c-8f-06-00-63-80-f4-df-0b')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SaleEndDate(self) -> Windows.Foundation.DateTime: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('320e2c52-d760-450a-a4-2b-67-d1-e9-01-ac-90')
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
    def get_Keywords(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Images(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreImage]: ...
    @winrt_commethod(14)
    def get_Videos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreVideo]: ...
    @winrt_commethod(15)
    def get_Skus(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreSku]: ...
    @winrt_commethod(16)
    def get_IsInUserCollection(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_Price(self) -> Windows.Services.Store.StorePrice: ...
    @winrt_commethod(18)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_LinkUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(20)
    def GetIsAnySkuInstalledAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5b34a0f9-a113-4811-83-26-16-19-9c-92-7f-31')
    @winrt_commethod(6)
    def get_ActionFilters(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ActionFilters = property(get_ActionFilters, None)
class IStoreProductPagedQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c92718c5-4dd5-4869-a4-62-ec-c6-87-2e-43-c5')
    @winrt_commethod(6)
    def get_Products(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreProduct]: ...
    @winrt_commethod(7)
    def get_HasMoreResults(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def GetNextAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    Products = property(get_Products, None)
    HasMoreResults = property(get_HasMoreResults, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreProductQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d805e6c5-d456-4ff6-80-49-90-76-d5-16-5f-73')
    @winrt_commethod(6)
    def get_Products(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreProduct]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Products = property(get_Products, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreProductResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b7674f73-3c87-4ee1-82-01-f4-28-35-9b-d3-af')
    @winrt_commethod(6)
    def get_Product(self) -> Windows.Services.Store.StoreProduct: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Product = property(get_Product, None)
    ExtendedError = property(get_ExtendedError, None)
class IStorePurchaseProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('836278f3-ff87-4364-a5-b4-fd-21-53-eb-e4-3b')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a768f59e-fefd-489f-9a-17-22-a5-93-e6-8b-9d')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String) -> Windows.Services.Store.StorePurchaseProperties: ...
class IStorePurchaseResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('add28552-f96a-463d-a7-bb-c2-0b-4f-ca-69-52')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Store.StorePurchaseStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreQueueItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('56d5c32b-f830-4293-91-88-ca-d2-dc-de-73-57')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_InstallKind(self) -> Windows.Services.Store.StoreQueueItemKind: ...
    @winrt_commethod(9)
    def GetCurrentStatus(self) -> Windows.Services.Store.StoreQueueItemStatus: ...
    @winrt_commethod(10)
    def add_Completed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreQueueItem, Windows.Services.Store.StoreQueueItemCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Completed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreQueueItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProductId = property(get_ProductId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    InstallKind = property(get_InstallKind, None)
class IStoreQueueItem2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('69491ca8-1ad4-447c-ad-8c-a9-50-35-f6-4d-82')
    @winrt_commethod(6)
    def CancelInstallAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def PauseInstallAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ResumeInstallAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IStoreQueueItemCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1247df6c-b44a-439b-bb-07-1d-30-03-d0-05-c2')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Store.StoreQueueItemStatus: ...
    Status = property(get_Status, None)
class IStoreQueueItemStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9bd6796f-9cc3-4ec3-b2-ef-7b-e4-33-b3-01-74')
    @winrt_commethod(6)
    def get_PackageInstallState(self) -> Windows.Services.Store.StoreQueueItemState: ...
    @winrt_commethod(7)
    def get_PackageInstallExtendedState(self) -> Windows.Services.Store.StoreQueueItemExtendedState: ...
    @winrt_commethod(8)
    def get_UpdateStatus(self) -> Windows.Services.Store.StorePackageUpdateStatus: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    PackageInstallState = property(get_PackageInstallState, None)
    PackageInstallExtendedState = property(get_PackageInstallExtendedState, None)
    UpdateStatus = property(get_UpdateStatus, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreRateAndReviewResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9d209d56-a6b5-4121-9b-61-ee-6d-0f-bd-bd-bb')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_WasUpdated(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Status(self) -> Windows.Services.Store.StoreRateAndReviewStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    WasUpdated = property(get_WasUpdated, None)
    Status = property(get_Status, None)
class IStoreRequestHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6ce5e5f9-a0c9-4b2c-96-a6-a1-71-c6-30-03-8d')
    @winrt_commethod(6)
    def SendRequestAsync(self, context: Windows.Services.Store.StoreContext, requestKind: UInt32, parametersAsJson: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreSendRequestResult]: ...
class IStoreSendRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c73abe60-8272-4502-8a-69-6e-75-15-3a-42-99')
    @winrt_commethod(6)
    def get_Response(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Response = property(get_Response, None)
    ExtendedError = property(get_ExtendedError, None)
class IStoreSendRequestResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2901296f-c0b0-49d0-8e-8d-aa-94-0a-f9-c1-0b')
    @winrt_commethod(6)
    def get_HttpStatusCode(self) -> Windows.Web.Http.HttpStatusCode: ...
    HttpStatusCode = property(get_HttpStatusCode, None)
class IStoreSku(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('397e6f55-4440-4f03-86-3c-91-f3-fe-c8-3d-79')
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
    def get_Images(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreImage]: ...
    @winrt_commethod(13)
    def get_Videos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreVideo]: ...
    @winrt_commethod(14)
    def get_Availabilities(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreAvailability]: ...
    @winrt_commethod(15)
    def get_Price(self) -> Windows.Services.Store.StorePrice: ...
    @winrt_commethod(16)
    def get_ExtendedJsonData(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_IsInUserCollection(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_BundledSkus(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(19)
    def get_CollectionData(self) -> Windows.Services.Store.StoreCollectionData: ...
    @winrt_commethod(20)
    def GetIsInstalledAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def RequestPurchaseAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(22)
    def RequestPurchaseWithPurchasePropertiesAsync(self, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_commethod(23)
    def get_IsSubscription(self) -> Boolean: ...
    @winrt_commethod(24)
    def get_SubscriptionInfo(self) -> Windows.Services.Store.StoreSubscriptionInfo: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4189776a-0559-43ac-a9-c6-3a-b0-01-1f-b8-eb')
    @winrt_commethod(6)
    def get_BillingPeriod(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_BillingPeriodUnit(self) -> Windows.Services.Store.StoreDurationUnit: ...
    @winrt_commethod(8)
    def get_HasTrialPeriod(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_TrialPeriod(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_TrialPeriodUnit(self) -> Windows.Services.Store.StoreDurationUnit: ...
    BillingPeriod = property(get_BillingPeriod, None)
    BillingPeriodUnit = property(get_BillingPeriodUnit, None)
    HasTrialPeriod = property(get_HasTrialPeriod, None)
    TrialPeriod = property(get_TrialPeriod, None)
    TrialPeriodUnit = property(get_TrialPeriodUnit, None)
class IStoreUninstallStorePackageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9fca39fd-126f-4cda-b8-01-13-46-b8-d0-a2-60')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Services.Store.StoreUninstallStorePackageStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IStoreVideo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f26cb184-6f5e-4dc2-88-6c-3c-63-08-3c-2f-94')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_VideoPurposeTag(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PreviewImage(self) -> Windows.Services.Store.StoreImage: ...
    Uri = property(get_Uri, None)
    VideoPurposeTag = property(get_VideoPurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
    PreviewImage = property(get_PreviewImage, None)
class StoreAcquireLicenseResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreAcquireLicenseResult'
    @winrt_mixinmethod
    def get_StorePackageLicense(self: Windows.Services.Store.IStoreAcquireLicenseResult) -> Windows.Services.Store.StorePackageLicense: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreAcquireLicenseResult) -> Windows.Foundation.HResult: ...
    StorePackageLicense = property(get_StorePackageLicense, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreAppLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreAppLicense'
    @winrt_mixinmethod
    def get_SkuStoreId(self: Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTrial(self: Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.Services.Store.IStoreAppLicense) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AddOnLicenses(self: Windows.Services.Store.IStoreAppLicense) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreLicense]: ...
    @winrt_mixinmethod
    def get_TrialTimeRemaining(self: Windows.Services.Store.IStoreAppLicense) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsTrialOwnedByThisUser(self: Windows.Services.Store.IStoreAppLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_TrialUniqueId(self: Windows.Services.Store.IStoreAppLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsDiscLicense(self: Windows.Services.Store.IStoreAppLicense2) -> Boolean: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreAvailability'
    @winrt_mixinmethod
    def get_StoreId(self: Windows.Services.Store.IStoreAvailability) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EndDate(self: Windows.Services.Store.IStoreAvailability) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Price(self: Windows.Services.Store.IStoreAvailability) -> Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreAvailability) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: Windows.Services.Store.IStoreAvailability) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: Windows.Services.Store.IStoreAvailability, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    StoreId = property(get_StoreId, None)
    EndDate = property(get_EndDate, None)
    Price = property(get_Price, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class StoreCanAcquireLicenseResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreCanAcquireLicenseResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreCanAcquireLicenseResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_LicensableSku(self: Windows.Services.Store.IStoreCanAcquireLicenseResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStoreCanAcquireLicenseResult) -> Windows.Services.Store.StoreCanLicenseStatus: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreCollectionData'
    @winrt_mixinmethod
    def get_IsTrial(self: Windows.Services.Store.IStoreCollectionData) -> Boolean: ...
    @winrt_mixinmethod
    def get_CampaignId(self: Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeveloperOfferId(self: Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AcquiredDate(self: Windows.Services.Store.IStoreCollectionData) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_StartDate(self: Windows.Services.Store.IStoreCollectionData) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndDate(self: Windows.Services.Store.IStoreCollectionData) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_TrialTimeRemaining(self: Windows.Services.Store.IStoreCollectionData) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreCollectionData) -> WinRT_String: ...
    IsTrial = property(get_IsTrial, None)
    CampaignId = property(get_CampaignId, None)
    DeveloperOfferId = property(get_DeveloperOfferId, None)
    AcquiredDate = property(get_AcquiredDate, None)
    StartDate = property(get_StartDate, None)
    EndDate = property(get_EndDate, None)
    TrialTimeRemaining = property(get_TrialTimeRemaining, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
class StoreConsumableResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreConsumableResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStoreConsumableResult) -> Windows.Services.Store.StoreConsumableStatus: ...
    @winrt_mixinmethod
    def get_TrackingId(self: Windows.Services.Store.IStoreConsumableResult) -> Guid: ...
    @winrt_mixinmethod
    def get_BalanceRemaining(self: Windows.Services.Store.IStoreConsumableResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreConsumableResult) -> Windows.Foundation.HResult: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreContext'
    @winrt_mixinmethod
    def get_User(self: Windows.Services.Store.IStoreContext) -> Windows.System.User: ...
    @winrt_mixinmethod
    def add_OfflineLicensesChanged(self: Windows.Services.Store.IStoreContext, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreContext, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OfflineLicensesChanged(self: Windows.Services.Store.IStoreContext, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCustomerPurchaseIdAsync(self: Windows.Services.Store.IStoreContext, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetCustomerCollectionsIdAsync(self: Windows.Services.Store.IStoreContext, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetAppLicenseAsync(self: Windows.Services.Store.IStoreContext) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreAppLicense]: ...
    @winrt_mixinmethod
    def GetStoreProductForCurrentAppAsync(self: Windows.Services.Store.IStoreContext) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductResult]: ...
    @winrt_mixinmethod
    def GetStoreProductsAsync(self: Windows.Services.Store.IStoreContext, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreProductsAsync(self: Windows.Services.Store.IStoreContext, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreProductsWithPagingAsync(self: Windows.Services.Store.IStoreContext, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_mixinmethod
    def GetUserCollectionAsync(self: Windows.Services.Store.IStoreContext, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetUserCollectionWithPagingAsync(self: Windows.Services.Store.IStoreContext, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], maxItemsToRetrievePerPage: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    @winrt_mixinmethod
    def ReportConsumableFulfillmentAsync(self: Windows.Services.Store.IStoreContext, productStoreId: WinRT_String, quantity: UInt32, trackingId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_mixinmethod
    def GetConsumableBalanceRemainingAsync(self: Windows.Services.Store.IStoreContext, productStoreId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreConsumableResult]: ...
    @winrt_mixinmethod
    def AcquireStoreLicenseForOptionalPackageAsync(self: Windows.Services.Store.IStoreContext, optionalPackage: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: Windows.Services.Store.IStoreContext, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: Windows.Services.Store.IStoreContext, storeId: WinRT_String, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def GetAppAndOptionalStorePackageUpdatesAsync(self: Windows.Services.Store.IStoreContext) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StorePackageUpdate]]: ...
    @winrt_mixinmethod
    def RequestDownloadStorePackageUpdatesAsync(self: Windows.Services.Store.IStoreContext, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackageUpdatesAsync(self: Windows.Services.Store.IStoreContext, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackagesAsync(self: Windows.Services.Store.IStoreContext, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def FindStoreProductForPackageAsync(self: Windows.Services.Store.IStoreContext2, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductResult]: ...
    @winrt_mixinmethod
    def get_CanSilentlyDownloadStorePackageUpdates(self: Windows.Services.Store.IStoreContext3) -> Boolean: ...
    @winrt_mixinmethod
    def TrySilentDownloadStorePackageUpdatesAsync(self: Windows.Services.Store.IStoreContext3, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def TrySilentDownloadAndInstallStorePackageUpdatesAsync(self: Windows.Services.Store.IStoreContext3, storePackageUpdates: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StorePackageUpdate]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def CanAcquireStoreLicenseForOptionalPackageAsync(self: Windows.Services.Store.IStoreContext3, optionalPackage: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def CanAcquireStoreLicenseAsync(self: Windows.Services.Store.IStoreContext3, productStoreId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreCanAcquireLicenseResult]: ...
    @winrt_mixinmethod
    def GetStoreProductsWithOptionsAsync(self: Windows.Services.Store.IStoreContext3, productKinds: Windows.Foundation.Collections.IIterable[WinRT_String], storeIds: Windows.Foundation.Collections.IIterable[WinRT_String], storeProductOptions: Windows.Services.Store.StoreProductOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductQueryResult]: ...
    @winrt_mixinmethod
    def GetAssociatedStoreQueueItemsAsync(self: Windows.Services.Store.IStoreContext3) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_mixinmethod
    def GetStoreQueueItemsAsync(self: Windows.Services.Store.IStoreContext3, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_mixinmethod
    def RequestDownloadAndInstallStorePackagesWithInstallOptionsAsync(self: Windows.Services.Store.IStoreContext3, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String], storePackageInstallOptions: Windows.Services.Store.StorePackageInstallOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def DownloadAndInstallStorePackagesAsync(self: Windows.Services.Store.IStoreContext3, storeIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Services.Store.StorePackageUpdateResult, Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def RequestUninstallStorePackageAsync(self: Windows.Services.Store.IStoreContext3, package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def RequestUninstallStorePackageByStoreIdAsync(self: Windows.Services.Store.IStoreContext3, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def UninstallStorePackageAsync(self: Windows.Services.Store.IStoreContext3, package: Windows.ApplicationModel.Package) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def UninstallStorePackageByStoreIdAsync(self: Windows.Services.Store.IStoreContext3, storeId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreUninstallStorePackageResult]: ...
    @winrt_mixinmethod
    def RequestRateAndReviewAppAsync(self: Windows.Services.Store.IStoreContext4) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreRateAndReviewResult]: ...
    @winrt_mixinmethod
    def SetInstallOrderForAssociatedStoreQueueItemsAsync(self: Windows.Services.Store.IStoreContext4, items: Windows.Foundation.Collections.IIterable[Windows.Services.Store.StoreQueueItem]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Services.Store.IStoreContextStatics) -> Windows.Services.Store.StoreContext: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.Services.Store.IStoreContextStatics, user: Windows.System.User) -> Windows.Services.Store.StoreContext: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreImage'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Services.Store.IStoreImage) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ImagePurposeTag(self: Windows.Services.Store.IStoreImage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Services.Store.IStoreImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Services.Store.IStoreImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Caption(self: Windows.Services.Store.IStoreImage) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    ImagePurposeTag = property(get_ImagePurposeTag, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Caption = property(get_Caption, None)
class StoreLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreLicense'
    @winrt_mixinmethod
    def get_SkuStoreId(self: Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.Services.Store.IStoreLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.Services.Store.IStoreLicense) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InAppOfferToken(self: Windows.Services.Store.IStoreLicense) -> WinRT_String: ...
    SkuStoreId = property(get_SkuStoreId, None)
    IsActive = property(get_IsActive, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ExtendedJsonData = property(get_ExtendedJsonData, None)
    InAppOfferToken = property(get_InAppOfferToken, None)
class StorePackageInstallOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePackageInstallOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Services.Store.StorePackageInstallOptions: ...
    @winrt_mixinmethod
    def get_AllowForcedAppRestart(self: Windows.Services.Store.IStorePackageInstallOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowForcedAppRestart(self: Windows.Services.Store.IStorePackageInstallOptions, value: Boolean) -> Void: ...
    AllowForcedAppRestart = property(get_AllowForcedAppRestart, put_AllowForcedAppRestart)
class StorePackageLicense(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePackageLicense'
    @winrt_mixinmethod
    def add_LicenseLost(self: Windows.Services.Store.IStorePackageLicense, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StorePackageLicense, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseLost(self: Windows.Services.Store.IStorePackageLicense, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Package(self: Windows.Services.Store.IStorePackageLicense) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_IsValid(self: Windows.Services.Store.IStorePackageLicense) -> Boolean: ...
    @winrt_mixinmethod
    def ReleaseLicense(self: Windows.Services.Store.IStorePackageLicense) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Package = property(get_Package, None)
    IsValid = property(get_IsValid, None)
class StorePackageUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePackageUpdate'
    @winrt_mixinmethod
    def get_Package(self: Windows.Services.Store.IStorePackageUpdate) -> Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_Mandatory(self: Windows.Services.Store.IStorePackageUpdate) -> Boolean: ...
    Package = property(get_Package, None)
    Mandatory = property(get_Mandatory, None)
class StorePackageUpdateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePackageUpdateResult'
    @winrt_mixinmethod
    def get_OverallState(self: Windows.Services.Store.IStorePackageUpdateResult) -> Windows.Services.Store.StorePackageUpdateState: ...
    @winrt_mixinmethod
    def get_StorePackageUpdateStatuses(self: Windows.Services.Store.IStorePackageUpdateResult) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StorePackageUpdateStatus]: ...
    @winrt_mixinmethod
    def get_StoreQueueItems(self: Windows.Services.Store.IStorePackageUpdateResult2) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreQueueItem]: ...
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
    PackageUpdateState: Windows.Services.Store.StorePackageUpdateState
class StorePrice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePrice'
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: Windows.Services.Store.IStorePrice) -> Boolean: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: Windows.Services.Store.IStorePrice) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedRecurrencePrice(self: Windows.Services.Store.IStorePrice) -> WinRT_String: ...
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    FormattedPrice = property(get_FormattedPrice, None)
    IsOnSale = property(get_IsOnSale, None)
    SaleEndDate = property(get_SaleEndDate, None)
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedRecurrencePrice = property(get_FormattedRecurrencePrice, None)
class StoreProduct(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreProduct'
    @winrt_mixinmethod
    def get_StoreId(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductKind(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasDigitalDownload(self: Windows.Services.Store.IStoreProduct) -> Boolean: ...
    @winrt_mixinmethod
    def get_Keywords(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Images(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreImage]: ...
    @winrt_mixinmethod
    def get_Videos(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreVideo]: ...
    @winrt_mixinmethod
    def get_Skus(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreSku]: ...
    @winrt_mixinmethod
    def get_IsInUserCollection(self: Windows.Services.Store.IStoreProduct) -> Boolean: ...
    @winrt_mixinmethod
    def get_Price(self: Windows.Services.Store.IStoreProduct) -> Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LinkUri(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetIsAnySkuInstalledAsync(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: Windows.Services.Store.IStoreProduct) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: Windows.Services.Store.IStoreProduct, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def get_InAppOfferToken(self: Windows.Services.Store.IStoreProduct) -> WinRT_String: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreProductOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Services.Store.StoreProductOptions: ...
    @winrt_mixinmethod
    def get_ActionFilters(self: Windows.Services.Store.IStoreProductOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ActionFilters = property(get_ActionFilters, None)
class StoreProductPagedQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreProductPagedQueryResult'
    @winrt_mixinmethod
    def get_Products(self: Windows.Services.Store.IStoreProductPagedQueryResult) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreProduct]: ...
    @winrt_mixinmethod
    def get_HasMoreResults(self: Windows.Services.Store.IStoreProductPagedQueryResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreProductPagedQueryResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def GetNextAsync(self: Windows.Services.Store.IStoreProductPagedQueryResult) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreProductPagedQueryResult]: ...
    Products = property(get_Products, None)
    HasMoreResults = property(get_HasMoreResults, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreProductQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreProductQueryResult'
    @winrt_mixinmethod
    def get_Products(self: Windows.Services.Store.IStoreProductQueryResult) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.Store.StoreProduct]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreProductQueryResult) -> Windows.Foundation.HResult: ...
    Products = property(get_Products, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreProductResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreProductResult'
    @winrt_mixinmethod
    def get_Product(self: Windows.Services.Store.IStoreProductResult) -> Windows.Services.Store.StoreProduct: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreProductResult) -> Windows.Foundation.HResult: ...
    Product = property(get_Product, None)
    ExtendedError = property(get_ExtendedError, None)
class StorePurchaseProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePurchaseProperties'
    @winrt_factorymethod
    def Create(cls: Windows.Services.Store.IStorePurchasePropertiesFactory, name: WinRT_String) -> Windows.Services.Store.StorePurchaseProperties: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Services.Store.StorePurchaseProperties: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Services.Store.IStorePurchaseProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Services.Store.IStorePurchaseProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStorePurchaseProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExtendedJsonData(self: Windows.Services.Store.IStorePurchaseProperties, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    ExtendedJsonData = property(get_ExtendedJsonData, put_ExtendedJsonData)
class StorePurchaseResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StorePurchaseResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStorePurchaseResult) -> Windows.Services.Store.StorePurchaseStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStorePurchaseResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
StorePurchaseStatus = Int32
StorePurchaseStatus_Succeeded: StorePurchaseStatus = 0
StorePurchaseStatus_AlreadyPurchased: StorePurchaseStatus = 1
StorePurchaseStatus_NotPurchased: StorePurchaseStatus = 2
StorePurchaseStatus_NetworkError: StorePurchaseStatus = 3
StorePurchaseStatus_ServerError: StorePurchaseStatus = 4
class StoreQueueItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreQueueItem'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.Services.Store.IStoreQueueItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.Services.Store.IStoreQueueItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstallKind(self: Windows.Services.Store.IStoreQueueItem) -> Windows.Services.Store.StoreQueueItemKind: ...
    @winrt_mixinmethod
    def GetCurrentStatus(self: Windows.Services.Store.IStoreQueueItem) -> Windows.Services.Store.StoreQueueItemStatus: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.Services.Store.IStoreQueueItem, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreQueueItem, Windows.Services.Store.StoreQueueItemCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.Services.Store.IStoreQueueItem, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Services.Store.IStoreQueueItem, handler: Windows.Foundation.TypedEventHandler[Windows.Services.Store.StoreQueueItem, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Services.Store.IStoreQueueItem, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CancelInstallAsync(self: Windows.Services.Store.IStoreQueueItem2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def PauseInstallAsync(self: Windows.Services.Store.IStoreQueueItem2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResumeInstallAsync(self: Windows.Services.Store.IStoreQueueItem2) -> Windows.Foundation.IAsyncAction: ...
    ProductId = property(get_ProductId, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    InstallKind = property(get_InstallKind, None)
class StoreQueueItemCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreQueueItemCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStoreQueueItemCompletedEventArgs) -> Windows.Services.Store.StoreQueueItemStatus: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreQueueItemStatus'
    @winrt_mixinmethod
    def get_PackageInstallState(self: Windows.Services.Store.IStoreQueueItemStatus) -> Windows.Services.Store.StoreQueueItemState: ...
    @winrt_mixinmethod
    def get_PackageInstallExtendedState(self: Windows.Services.Store.IStoreQueueItemStatus) -> Windows.Services.Store.StoreQueueItemExtendedState: ...
    @winrt_mixinmethod
    def get_UpdateStatus(self: Windows.Services.Store.IStoreQueueItemStatus) -> Windows.Services.Store.StorePackageUpdateStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreQueueItemStatus) -> Windows.Foundation.HResult: ...
    PackageInstallState = property(get_PackageInstallState, None)
    PackageInstallExtendedState = property(get_PackageInstallExtendedState, None)
    UpdateStatus = property(get_UpdateStatus, None)
    ExtendedError = property(get_ExtendedError, None)
class StoreRateAndReviewResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreRateAndReviewResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreRateAndReviewResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreRateAndReviewResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WasUpdated(self: Windows.Services.Store.IStoreRateAndReviewResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStoreRateAndReviewResult) -> Windows.Services.Store.StoreRateAndReviewStatus: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreRequestHelper'
    @winrt_classmethod
    def SendRequestAsync(cls: Windows.Services.Store.IStoreRequestHelperStatics, context: Windows.Services.Store.StoreContext, requestKind: UInt32, parametersAsJson: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StoreSendRequestResult]: ...
class StoreSendRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreSendRequestResult'
    @winrt_mixinmethod
    def get_Response(self: Windows.Services.Store.IStoreSendRequestResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreSendRequestResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_HttpStatusCode(self: Windows.Services.Store.IStoreSendRequestResult2) -> Windows.Web.Http.HttpStatusCode: ...
    Response = property(get_Response, None)
    ExtendedError = property(get_ExtendedError, None)
    HttpStatusCode = property(get_HttpStatusCode, None)
class StoreSku(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreSku'
    @winrt_mixinmethod
    def get_StoreId(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsTrial(self: Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_CustomDeveloperData(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Images(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreImage]: ...
    @winrt_mixinmethod
    def get_Videos(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreVideo]: ...
    @winrt_mixinmethod
    def get_Availabilities(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Store.StoreAvailability]: ...
    @winrt_mixinmethod
    def get_Price(self: Windows.Services.Store.IStoreSku) -> Windows.Services.Store.StorePrice: ...
    @winrt_mixinmethod
    def get_ExtendedJsonData(self: Windows.Services.Store.IStoreSku) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsInUserCollection(self: Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_BundledSkus(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_CollectionData(self: Windows.Services.Store.IStoreSku) -> Windows.Services.Store.StoreCollectionData: ...
    @winrt_mixinmethod
    def GetIsInstalledAsync(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPurchaseAsync(self: Windows.Services.Store.IStoreSku) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def RequestPurchaseWithPurchasePropertiesAsync(self: Windows.Services.Store.IStoreSku, storePurchaseProperties: Windows.Services.Store.StorePurchaseProperties) -> Windows.Foundation.IAsyncOperation[Windows.Services.Store.StorePurchaseResult]: ...
    @winrt_mixinmethod
    def get_IsSubscription(self: Windows.Services.Store.IStoreSku) -> Boolean: ...
    @winrt_mixinmethod
    def get_SubscriptionInfo(self: Windows.Services.Store.IStoreSku) -> Windows.Services.Store.StoreSubscriptionInfo: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreSubscriptionInfo'
    @winrt_mixinmethod
    def get_BillingPeriod(self: Windows.Services.Store.IStoreSubscriptionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_BillingPeriodUnit(self: Windows.Services.Store.IStoreSubscriptionInfo) -> Windows.Services.Store.StoreDurationUnit: ...
    @winrt_mixinmethod
    def get_HasTrialPeriod(self: Windows.Services.Store.IStoreSubscriptionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_TrialPeriod(self: Windows.Services.Store.IStoreSubscriptionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_TrialPeriodUnit(self: Windows.Services.Store.IStoreSubscriptionInfo) -> Windows.Services.Store.StoreDurationUnit: ...
    BillingPeriod = property(get_BillingPeriod, None)
    BillingPeriodUnit = property(get_BillingPeriodUnit, None)
    HasTrialPeriod = property(get_HasTrialPeriod, None)
    TrialPeriod = property(get_TrialPeriod, None)
    TrialPeriodUnit = property(get_TrialPeriodUnit, None)
class StoreUninstallStorePackageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreUninstallStorePackageResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Services.Store.IStoreUninstallStorePackageResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Store.IStoreUninstallStorePackageResult) -> Windows.Services.Store.StoreUninstallStorePackageStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
StoreUninstallStorePackageStatus = Int32
StoreUninstallStorePackageStatus_Succeeded: StoreUninstallStorePackageStatus = 0
StoreUninstallStorePackageStatus_CanceledByUser: StoreUninstallStorePackageStatus = 1
StoreUninstallStorePackageStatus_NetworkError: StoreUninstallStorePackageStatus = 2
StoreUninstallStorePackageStatus_UninstallNotApplicable: StoreUninstallStorePackageStatus = 3
StoreUninstallStorePackageStatus_Error: StoreUninstallStorePackageStatus = 4
class StoreVideo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Store.StoreVideo'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Services.Store.IStoreVideo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_VideoPurposeTag(self: Windows.Services.Store.IStoreVideo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Services.Store.IStoreVideo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Services.Store.IStoreVideo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Caption(self: Windows.Services.Store.IStoreVideo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PreviewImage(self: Windows.Services.Store.IStoreVideo) -> Windows.Services.Store.StoreImage: ...
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
