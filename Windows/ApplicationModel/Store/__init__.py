from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Store
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
class CurrentApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.CurrentApp'
    @winrt_classmethod
    def GetCustomerPurchaseIdAsync(cls: Windows.ApplicationModel.Store.ICurrentApp2Statics, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetCustomerCollectionsIdAsync(cls: Windows.ApplicationModel.Store.ICurrentApp2Statics, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetAppPurchaseCampaignIdAsync(cls: Windows.ApplicationModel.Store.ICurrentAppWithCampaignId) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationByProductIdsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, productIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def LoadListingInformationByKeywordsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, keywords: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def ReportProductFulfillment(cls: Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, productId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def ReportConsumableFulfillmentAsync(cls: Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String, transactionId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithResultsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithDisplayPropertiesAsync(cls: Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String, offerId: WinRT_String, displayProperties: Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def GetUnfulfilledConsumablesAsync(cls: Windows.ApplicationModel.Store.ICurrentAppWithConsumables) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
    @winrt_classmethod
    def get_LicenseInformation(cls: Windows.ApplicationModel.Store.ICurrentApp) -> Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_classmethod
    def get_LinkUri(cls: Windows.ApplicationModel.Store.ICurrentApp) -> Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AppId(cls: Windows.ApplicationModel.Store.ICurrentApp) -> Guid: ...
    @winrt_classmethod
    def RequestAppPurchaseAsync(cls: Windows.ApplicationModel.Store.ICurrentApp, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestProductPurchaseAsync(cls: Windows.ApplicationModel.Store.ICurrentApp, productId: WinRT_String, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationAsync(cls: Windows.ApplicationModel.Store.ICurrentApp) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def GetAppReceiptAsync(cls: Windows.ApplicationModel.Store.ICurrentApp) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetProductReceiptAsync(cls: Windows.ApplicationModel.Store.ICurrentApp, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
    AppId = property(get_AppId, None)
class CurrentAppSimulator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.CurrentAppSimulator'
    @winrt_classmethod
    def GetAppPurchaseCampaignIdAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorWithCampaignId) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationByProductIdsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorStaticsWithFiltering, productIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def LoadListingInformationByKeywordsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorStaticsWithFiltering, keywords: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def ReportConsumableFulfillmentAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String, transactionId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithResultsAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithDisplayPropertiesAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String, offerId: WinRT_String, displayProperties: Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def GetUnfulfilledConsumablesAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
    @winrt_classmethod
    def get_LicenseInformation(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_classmethod
    def get_LinkUri(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AppId(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Guid: ...
    @winrt_classmethod
    def RequestAppPurchaseAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestProductPurchaseAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator, productId: WinRT_String, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def GetAppReceiptAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetProductReceiptAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReloadSimulatorAsync(cls: Windows.ApplicationModel.Store.ICurrentAppSimulator, simulatorSettingsFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
    AppId = property(get_AppId, None)
FulfillmentResult = Int32
FulfillmentResult_Succeeded: FulfillmentResult = 0
FulfillmentResult_NothingToFulfill: FulfillmentResult = 1
FulfillmentResult_PurchasePending: FulfillmentResult = 2
FulfillmentResult_PurchaseReverted: FulfillmentResult = 3
FulfillmentResult_ServerError: FulfillmentResult = 4
class ICurrentApp(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d52dc065-da3f-4685-99-5e-9b-48-2e-b5-e6-03')
    @winrt_commethod(6)
    def get_LicenseInformation(self) -> Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_commethod(7)
    def get_LinkUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(9)
    def RequestAppPurchaseAsync(self, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def RequestProductPurchaseAsync(self, productId: WinRT_String, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def LoadListingInformationAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(12)
    def GetAppReceiptAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetProductReceiptAsync(self, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
    AppId = property(get_AppId, None)
class ICurrentApp2Statics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df4e6e2d-3171-4ad3-86-14-2c-61-24-43-73-cb')
    @winrt_commethod(6)
    def GetCustomerPurchaseIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetCustomerCollectionsIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppSimulator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f17f9db1-74cd-4787-97-87-19-86-6e-9a-55-59')
    @winrt_commethod(6)
    def get_LicenseInformation(self) -> Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_commethod(7)
    def get_LinkUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(9)
    def RequestAppPurchaseAsync(self, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def RequestProductPurchaseAsync(self, productId: WinRT_String, includeReceipt: Boolean) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def LoadListingInformationAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(12)
    def GetAppReceiptAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetProductReceiptAsync(self, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def ReloadSimulatorAsync(self, simulatorSettingsFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
    AppId = property(get_AppId, None)
class ICurrentAppSimulatorStaticsWithFiltering(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('617e70e2-f86f-4b54-96-66-dd-e2-85-09-2c-68')
    @winrt_commethod(6)
    def LoadListingInformationByProductIdsAsync(self, productIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(7)
    def LoadListingInformationByKeywordsAsync(self, keywords: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
class ICurrentAppSimulatorWithCampaignId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('84678a43-df00-4672-a4-3f-b2-5b-14-41-cf-cf')
    @winrt_commethod(6)
    def GetAppPurchaseCampaignIdAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppSimulatorWithConsumables(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e51f0ab-20e7-4412-9b-85-59-bb-78-38-86-67')
    @winrt_commethod(6)
    def ReportConsumableFulfillmentAsync(self, productId: WinRT_String, transactionId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_commethod(7)
    def RequestProductPurchaseWithResultsAsync(self, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(8)
    def RequestProductPurchaseWithDisplayPropertiesAsync(self, productId: WinRT_String, offerId: WinRT_String, displayProperties: Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(9)
    def GetUnfulfilledConsumablesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
class ICurrentAppStaticsWithFiltering(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d36d6542-9085-438e-97-ba-a2-5c-97-6b-e2-fd')
    @winrt_commethod(6)
    def LoadListingInformationByProductIdsAsync(self, productIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(7)
    def LoadListingInformationByKeywordsAsync(self, keywords: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(8)
    def ReportProductFulfillment(self, productId: WinRT_String) -> Void: ...
class ICurrentAppWithCampaignId(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('312f4cd0-36c1-44a6-b3-2b-43-2d-60-8e-4d-d6')
    @winrt_commethod(6)
    def GetAppPurchaseCampaignIdAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppWithConsumables(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('844e0071-9e4f-4f79-99-5a-5f-91-17-2e-6c-ef')
    @winrt_commethod(6)
    def ReportConsumableFulfillmentAsync(self, productId: WinRT_String, transactionId: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_commethod(7)
    def RequestProductPurchaseWithResultsAsync(self, productId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(8)
    def RequestProductPurchaseWithDisplayPropertiesAsync(self, productId: WinRT_String, offerId: WinRT_String, displayProperties: Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(9)
    def GetUnfulfilledConsumablesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
class ILicenseInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8eb7dc30-f170-4ed5-8e-21-15-16-da-3f-d3-67')
    @winrt_commethod(6)
    def get_ProductLicenses(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.ProductLicense]: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExpirationDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def add_LicenseChanged(self, handler: Windows.ApplicationModel.Store.LicenseChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LicenseChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProductLicenses = property(get_ProductLicenses, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ExpirationDate = property(get_ExpirationDate, None)
class IListingInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('588b4abf-bc74-4383-b7-8c-99-60-63-23-de-ce')
    @winrt_commethod(6)
    def get_CurrentMarket(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ProductListings(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.ProductListing]: ...
    @winrt_commethod(9)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AgeRating(self) -> UInt32: ...
    CurrentMarket = property(get_CurrentMarket, None)
    Description = property(get_Description, None)
    ProductListings = property(get_ProductListings, None)
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
    AgeRating = property(get_AgeRating, None)
class IListingInformation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0fd2c1d-b30e-4384-84-ea-72-fe-fa-82-22-3e')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SaleEndDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CurrencyCode(self) -> WinRT_String: ...
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    SaleEndDate = property(get_SaleEndDate, None)
    IsOnSale = property(get_IsOnSale, None)
    CurrencyCode = property(get_CurrencyCode, None)
class IProductLicense(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('363308c7-2bcf-4c0e-8f-2f-e8-08-aa-a8-f9-9d')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> Windows.Foundation.DateTime: ...
    ProductId = property(get_ProductId, None)
    IsActive = property(get_IsActive, None)
    ExpirationDate = property(get_ExpirationDate, None)
class IProductLicenseWithFulfillment(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc535c8a-f667-40f3-ba-3c-04-5a-63-ab-b3-ac')
    @winrt_commethod(6)
    def get_IsConsumable(self) -> Boolean: ...
    IsConsumable = property(get_IsConsumable, None)
class IProductListing(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('45a7d6ad-c750-4d9c-94-7c-b0-0d-cb-f9-e9-c2')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
class IProductListing2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f89e290f-73fe-494d-a9-39-08-a9-b2-49-5a-be')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SaleEndDate(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CurrencyCode(self) -> WinRT_String: ...
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    SaleEndDate = property(get_SaleEndDate, None)
    IsOnSale = property(get_IsOnSale, None)
    CurrencyCode = property(get_CurrencyCode, None)
class IProductListingWithConsumables(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb9e9790-8f6b-481f-93-a7-5c-3a-63-06-81-49')
    @winrt_commethod(6)
    def get_ProductType(self) -> Windows.ApplicationModel.Store.ProductType: ...
    ProductType = property(get_ProductType, None)
class IProductListingWithMetadata(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('124da567-23f8-423e-95-32-18-99-43-c4-0a-ce')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Keywords(self) -> Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ProductType(self) -> Windows.ApplicationModel.Store.ProductType: ...
    @winrt_commethod(9)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ImageUri(self) -> Windows.Foundation.Uri: ...
    Description = property(get_Description, None)
    Keywords = property(get_Keywords, None)
    ProductType = property(get_ProductType, None)
    Tag = property(get_Tag, None)
    ImageUri = property(get_ImageUri, None)
class IProductPurchaseDisplayProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d70b7420-bc92-401b-a8-09-c9-b2-e5-db-bd-af')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Image(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_Image(self, value: Windows.Foundation.Uri) -> Void: ...
    Name = property(get_Name, put_Name)
    Description = property(get_Description, put_Description)
    Image = property(get_Image, put_Image)
class IProductPurchaseDisplayPropertiesFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f491df4-32d6-4b40-b4-74-b8-30-38-a4-d9-cf')
    @winrt_commethod(6)
    def CreateProductPurchaseDisplayProperties(self, name: WinRT_String) -> Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
class IPurchaseResults(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ed50b37e-8656-4f65-b8-c8-ac-7e-0c-b1-a1-c2')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.Store.ProductPurchaseStatus: ...
    @winrt_commethod(7)
    def get_TransactionId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ReceiptXml(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_OfferId(self) -> WinRT_String: ...
    Status = property(get_Status, None)
    TransactionId = property(get_TransactionId, None)
    ReceiptXml = property(get_ReceiptXml, None)
    OfferId = property(get_OfferId, None)
class IUnfulfilledConsumable(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2df7fbbb-1cdd-4cb8-a0-14-7b-9c-f8-98-69-27')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TransactionId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_OfferId(self) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    TransactionId = property(get_TransactionId, None)
    OfferId = property(get_OfferId, None)
class LicenseChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d4a50255-1369-4c36-83-2f-6f-2d-88-e3-65-9b')
    ClassId = 'Windows.ApplicationModel.Store.LicenseChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class LicenseInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.LicenseInformation'
    @winrt_mixinmethod
    def get_ProductLicenses(self: Windows.ApplicationModel.Store.ILicenseInformation) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.ProductLicense]: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.ApplicationModel.Store.ILicenseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTrial(self: Windows.ApplicationModel.Store.ILicenseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.ApplicationModel.Store.ILicenseInformation) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def add_LicenseChanged(self: Windows.ApplicationModel.Store.ILicenseInformation, handler: Windows.ApplicationModel.Store.LicenseChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseChanged(self: Windows.ApplicationModel.Store.ILicenseInformation, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProductLicenses = property(get_ProductLicenses, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ExpirationDate = property(get_ExpirationDate, None)
class ListingInformation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.ListingInformation'
    @winrt_mixinmethod
    def get_CurrentMarket(self: Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductListings(self: Windows.ApplicationModel.Store.IListingInformation) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.ProductListing]: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AgeRating(self: Windows.ApplicationModel.Store.IListingInformation) -> UInt32: ...
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: Windows.ApplicationModel.Store.IListingInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: Windows.ApplicationModel.Store.IListingInformation2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: Windows.ApplicationModel.Store.IListingInformation2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: Windows.ApplicationModel.Store.IListingInformation2) -> WinRT_String: ...
    CurrentMarket = property(get_CurrentMarket, None)
    Description = property(get_Description, None)
    ProductListings = property(get_ProductListings, None)
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
    AgeRating = property(get_AgeRating, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    SaleEndDate = property(get_SaleEndDate, None)
    IsOnSale = property(get_IsOnSale, None)
    CurrencyCode = property(get_CurrencyCode, None)
class ProductLicense(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.ProductLicense'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.Store.IProductLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.ApplicationModel.Store.IProductLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.ApplicationModel.Store.IProductLicense) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsConsumable(self: Windows.ApplicationModel.Store.IProductLicenseWithFulfillment) -> Boolean: ...
    ProductId = property(get_ProductId, None)
    IsActive = property(get_IsActive, None)
    ExpirationDate = property(get_ExpirationDate, None)
    IsConsumable = property(get_IsConsumable, None)
class ProductListing(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.ProductListing'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.Store.IProductListingWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Keywords(self: Windows.ApplicationModel.Store.IProductListingWithMetadata) -> Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ProductType(self: Windows.ApplicationModel.Store.IProductListingWithMetadata) -> Windows.ApplicationModel.Store.ProductType: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.ApplicationModel.Store.IProductListingWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ImageUri(self: Windows.ApplicationModel.Store.IProductListingWithMetadata) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: Windows.ApplicationModel.Store.IProductListing2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: Windows.ApplicationModel.Store.IProductListing2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: Windows.ApplicationModel.Store.IProductListing2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: Windows.ApplicationModel.Store.IProductListing2) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Keywords = property(get_Keywords, None)
    ProductType = property(get_ProductType, None)
    Tag = property(get_Tag, None)
    ImageUri = property(get_ImageUri, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    SaleEndDate = property(get_SaleEndDate, None)
    IsOnSale = property(get_IsOnSale, None)
    CurrencyCode = property(get_CurrencyCode, None)
class ProductPurchaseDisplayProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties'
    @winrt_factorymethod
    def CreateProductPurchaseDisplayProperties(cls: Windows.ApplicationModel.Store.IProductPurchaseDisplayPropertiesFactory, name: WinRT_String) -> Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Image(self: Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: Windows.Foundation.Uri) -> Void: ...
    Name = property(get_Name, put_Name)
    Description = property(get_Description, put_Description)
    Image = property(get_Image, put_Image)
ProductPurchaseStatus = Int32
ProductPurchaseStatus_Succeeded: ProductPurchaseStatus = 0
ProductPurchaseStatus_AlreadyPurchased: ProductPurchaseStatus = 1
ProductPurchaseStatus_NotFulfilled: ProductPurchaseStatus = 2
ProductPurchaseStatus_NotPurchased: ProductPurchaseStatus = 3
ProductType = Int32
ProductType_Unknown: ProductType = 0
ProductType_Durable: ProductType = 1
ProductType_Consumable: ProductType = 2
class PurchaseResults(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.PurchaseResults'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Store.IPurchaseResults) -> Windows.ApplicationModel.Store.ProductPurchaseStatus: ...
    @winrt_mixinmethod
    def get_TransactionId(self: Windows.ApplicationModel.Store.IPurchaseResults) -> Guid: ...
    @winrt_mixinmethod
    def get_ReceiptXml(self: Windows.ApplicationModel.Store.IPurchaseResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OfferId(self: Windows.ApplicationModel.Store.IPurchaseResults) -> WinRT_String: ...
    Status = property(get_Status, None)
    TransactionId = property(get_TransactionId, None)
    ReceiptXml = property(get_ReceiptXml, None)
    OfferId = property(get_OfferId, None)
class UnfulfilledConsumable(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.UnfulfilledConsumable'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransactionId(self: Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> Guid: ...
    @winrt_mixinmethod
    def get_OfferId(self: Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    TransactionId = property(get_TransactionId, None)
    OfferId = property(get_OfferId, None)
make_head(_module, 'CurrentApp')
make_head(_module, 'CurrentAppSimulator')
make_head(_module, 'ICurrentApp')
make_head(_module, 'ICurrentApp2Statics')
make_head(_module, 'ICurrentAppSimulator')
make_head(_module, 'ICurrentAppSimulatorStaticsWithFiltering')
make_head(_module, 'ICurrentAppSimulatorWithCampaignId')
make_head(_module, 'ICurrentAppSimulatorWithConsumables')
make_head(_module, 'ICurrentAppStaticsWithFiltering')
make_head(_module, 'ICurrentAppWithCampaignId')
make_head(_module, 'ICurrentAppWithConsumables')
make_head(_module, 'ILicenseInformation')
make_head(_module, 'IListingInformation')
make_head(_module, 'IListingInformation2')
make_head(_module, 'IProductLicense')
make_head(_module, 'IProductLicenseWithFulfillment')
make_head(_module, 'IProductListing')
make_head(_module, 'IProductListing2')
make_head(_module, 'IProductListingWithConsumables')
make_head(_module, 'IProductListingWithMetadata')
make_head(_module, 'IProductPurchaseDisplayProperties')
make_head(_module, 'IProductPurchaseDisplayPropertiesFactory')
make_head(_module, 'IPurchaseResults')
make_head(_module, 'IUnfulfilledConsumable')
make_head(_module, 'LicenseChangedEventHandler')
make_head(_module, 'LicenseInformation')
make_head(_module, 'ListingInformation')
make_head(_module, 'ProductLicense')
make_head(_module, 'ProductListing')
make_head(_module, 'ProductPurchaseDisplayProperties')
make_head(_module, 'PurchaseResults')
make_head(_module, 'UnfulfilledConsumable')
