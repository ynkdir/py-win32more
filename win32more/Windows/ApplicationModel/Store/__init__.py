from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Store
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class _CurrentApp_Meta_(ComPtr.__class__):
    pass
class CurrentApp(ComPtr, metaclass=_CurrentApp_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.CurrentApp'
    @winrt_classmethod
    def GetCustomerPurchaseIdAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp2Statics, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetCustomerCollectionsIdAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp2Statics, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetAppPurchaseCampaignIdAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppWithCampaignId) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationByProductIdsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, productIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def LoadListingInformationByKeywordsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, keywords: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def ReportProductFulfillment(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering, productId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def ReportConsumableFulfillmentAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String, transactionId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithResultsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithDisplayPropertiesAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppWithConsumables, productId: WinRT_String, offerId: WinRT_String, displayProperties: win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def GetUnfulfilledConsumablesAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppWithConsumables) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
    @winrt_classmethod
    def get_LicenseInformation(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp) -> win32more.Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_classmethod
    def get_LinkUri(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AppId(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp) -> Guid: ...
    @winrt_classmethod
    def RequestAppPurchaseAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestProductPurchaseAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp, productId: WinRT_String, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def GetAppReceiptAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetProductReceiptAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentApp, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    _CurrentApp_Meta_.AppId = property(get_AppId, None)
    _CurrentApp_Meta_.LicenseInformation = property(get_LicenseInformation, None)
    _CurrentApp_Meta_.LinkUri = property(get_LinkUri, None)
class _CurrentAppSimulator_Meta_(ComPtr.__class__):
    pass
class CurrentAppSimulator(ComPtr, metaclass=_CurrentAppSimulator_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.CurrentAppSimulator'
    @winrt_classmethod
    def GetAppPurchaseCampaignIdAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorWithCampaignId) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationByProductIdsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorStaticsWithFiltering, productIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def LoadListingInformationByKeywordsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorStaticsWithFiltering, keywords: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def ReportConsumableFulfillmentAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String, transactionId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithResultsAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def RequestProductPurchaseWithDisplayPropertiesAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables, productId: WinRT_String, offerId: WinRT_String, displayProperties: win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_classmethod
    def GetUnfulfilledConsumablesAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
    @winrt_classmethod
    def get_LicenseInformation(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator) -> win32more.Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_classmethod
    def get_LinkUri(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def get_AppId(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator) -> Guid: ...
    @winrt_classmethod
    def RequestAppPurchaseAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestProductPurchaseAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator, productId: WinRT_String, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def LoadListingInformationAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_classmethod
    def GetAppReceiptAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetProductReceiptAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReloadSimulatorAsync(cls: win32more.Windows.ApplicationModel.Store.ICurrentAppSimulator, simulatorSettingsFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    _CurrentAppSimulator_Meta_.AppId = property(get_AppId, None)
    _CurrentAppSimulator_Meta_.LicenseInformation = property(get_LicenseInformation, None)
    _CurrentAppSimulator_Meta_.LinkUri = property(get_LinkUri, None)
class FulfillmentResult(Enum, Int32):
    Succeeded = 0
    NothingToFulfill = 1
    PurchasePending = 2
    PurchaseReverted = 3
    ServerError = 4
class ICurrentApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentApp'
    _iid_ = Guid('{d52dc065-da3f-4685-995e-9b482eb5e603}')
    @winrt_commethod(6)
    def get_LicenseInformation(self) -> win32more.Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_commethod(7)
    def get_LinkUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(9)
    def RequestAppPurchaseAsync(self, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def RequestProductPurchaseAsync(self, productId: WinRT_String, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def LoadListingInformationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(12)
    def GetAppReceiptAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetProductReceiptAsync(self, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    AppId = property(get_AppId, None)
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
class ICurrentApp2Statics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentApp2Statics'
    _iid_ = Guid('{df4e6e2d-3171-4ad3-8614-2c61244373cb}')
    @winrt_commethod(6)
    def GetCustomerPurchaseIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def GetCustomerCollectionsIdAsync(self, serviceTicket: WinRT_String, publisherUserId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppSimulator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppSimulator'
    _iid_ = Guid('{f17f9db1-74cd-4787-9787-19866e9a5559}')
    @winrt_commethod(6)
    def get_LicenseInformation(self) -> win32more.Windows.ApplicationModel.Store.LicenseInformation: ...
    @winrt_commethod(7)
    def get_LinkUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_AppId(self) -> Guid: ...
    @winrt_commethod(9)
    def RequestAppPurchaseAsync(self, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def RequestProductPurchaseAsync(self, productId: WinRT_String, includeReceipt: Boolean) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def LoadListingInformationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(12)
    def GetAppReceiptAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetProductReceiptAsync(self, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def ReloadSimulatorAsync(self, simulatorSettingsFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppId = property(get_AppId, None)
    LicenseInformation = property(get_LicenseInformation, None)
    LinkUri = property(get_LinkUri, None)
class ICurrentAppSimulatorStaticsWithFiltering(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppSimulatorStaticsWithFiltering'
    _iid_ = Guid('{617e70e2-f86f-4b54-9666-dde285092c68}')
    @winrt_commethod(6)
    def LoadListingInformationByProductIdsAsync(self, productIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(7)
    def LoadListingInformationByKeywordsAsync(self, keywords: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
class ICurrentAppSimulatorWithCampaignId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppSimulatorWithCampaignId'
    _iid_ = Guid('{84678a43-df00-4672-a43f-b25b1441cfcf}')
    @winrt_commethod(6)
    def GetAppPurchaseCampaignIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppSimulatorWithConsumables(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppSimulatorWithConsumables'
    _iid_ = Guid('{4e51f0ab-20e7-4412-9b85-59bb78388667}')
    @winrt_commethod(6)
    def ReportConsumableFulfillmentAsync(self, productId: WinRT_String, transactionId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_commethod(7)
    def RequestProductPurchaseWithResultsAsync(self, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(8)
    def RequestProductPurchaseWithDisplayPropertiesAsync(self, productId: WinRT_String, offerId: WinRT_String, displayProperties: win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(9)
    def GetUnfulfilledConsumablesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
class ICurrentAppStaticsWithFiltering(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppStaticsWithFiltering'
    _iid_ = Guid('{d36d6542-9085-438e-97ba-a25c976be2fd}')
    @winrt_commethod(6)
    def LoadListingInformationByProductIdsAsync(self, productIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(7)
    def LoadListingInformationByKeywordsAsync(self, keywords: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.ListingInformation]: ...
    @winrt_commethod(8)
    def ReportProductFulfillment(self, productId: WinRT_String) -> Void: ...
class ICurrentAppWithCampaignId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppWithCampaignId'
    _iid_ = Guid('{312f4cd0-36c1-44a6-b32b-432d608e4dd6}')
    @winrt_commethod(6)
    def GetAppPurchaseCampaignIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ICurrentAppWithConsumables(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ICurrentAppWithConsumables'
    _iid_ = Guid('{844e0071-9e4f-4f79-995a-5f91172e6cef}')
    @winrt_commethod(6)
    def ReportConsumableFulfillmentAsync(self, productId: WinRT_String, transactionId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.FulfillmentResult]: ...
    @winrt_commethod(7)
    def RequestProductPurchaseWithResultsAsync(self, productId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(8)
    def RequestProductPurchaseWithDisplayPropertiesAsync(self, productId: WinRT_String, offerId: WinRT_String, displayProperties: win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.PurchaseResults]: ...
    @winrt_commethod(9)
    def GetUnfulfilledConsumablesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.UnfulfilledConsumable]]: ...
class ILicenseInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.ILicenseInformation'
    _iid_ = Guid('{8eb7dc30-f170-4ed5-8e21-1516da3fd367}')
    @winrt_commethod(6)
    def get_ProductLicenses(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.ProductLicense]: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsTrial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def add_LicenseChanged(self, handler: win32more.Windows.ApplicationModel.Store.LicenseChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LicenseChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExpirationDate = property(get_ExpirationDate, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ProductLicenses = property(get_ProductLicenses, None)
    LicenseChanged = event()
class IListingInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IListingInformation'
    _iid_ = Guid('{588b4abf-bc74-4383-b78c-99606323dece}')
    @winrt_commethod(6)
    def get_CurrentMarket(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ProductListings(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.ProductListing]: ...
    @winrt_commethod(9)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AgeRating(self) -> UInt32: ...
    AgeRating = property(get_AgeRating, None)
    CurrentMarket = property(get_CurrentMarket, None)
    Description = property(get_Description, None)
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
    ProductListings = property(get_ProductListings, None)
class IListingInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IListingInformation2'
    _iid_ = Guid('{c0fd2c1d-b30e-4384-84ea-72fefa82223e}')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SaleEndDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CurrencyCode(self) -> WinRT_String: ...
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    IsOnSale = property(get_IsOnSale, None)
    SaleEndDate = property(get_SaleEndDate, None)
class IProductLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductLicense'
    _iid_ = Guid('{363308c7-2bcf-4c0e-8f2f-e808aaa8f99d}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.DateTime: ...
    ExpirationDate = property(get_ExpirationDate, None)
    IsActive = property(get_IsActive, None)
    ProductId = property(get_ProductId, None)
class IProductLicenseWithFulfillment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductLicenseWithFulfillment'
    _iid_ = Guid('{fc535c8a-f667-40f3-ba3c-045a63abb3ac}')
    @winrt_commethod(6)
    def get_IsConsumable(self) -> Boolean: ...
    IsConsumable = property(get_IsConsumable, None)
class IProductListing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductListing'
    _iid_ = Guid('{45a7d6ad-c750-4d9c-947c-b00dcbf9e9c2}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FormattedPrice(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    FormattedPrice = property(get_FormattedPrice, None)
    Name = property(get_Name, None)
    ProductId = property(get_ProductId, None)
class IProductListing2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductListing2'
    _iid_ = Guid('{f89e290f-73fe-494d-a939-08a9b2495abe}')
    @winrt_commethod(6)
    def get_FormattedBasePrice(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SaleEndDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_IsOnSale(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CurrencyCode(self) -> WinRT_String: ...
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    IsOnSale = property(get_IsOnSale, None)
    SaleEndDate = property(get_SaleEndDate, None)
class IProductListingWithConsumables(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductListingWithConsumables'
    _iid_ = Guid('{eb9e9790-8f6b-481f-93a7-5c3a63068149}')
    @winrt_commethod(6)
    def get_ProductType(self) -> win32more.Windows.ApplicationModel.Store.ProductType: ...
    ProductType = property(get_ProductType, None)
class IProductListingWithMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductListingWithMetadata'
    _iid_ = Guid('{124da567-23f8-423e-9532-189943c40ace}')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Keywords(self) -> win32more.Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ProductType(self) -> win32more.Windows.ApplicationModel.Store.ProductType: ...
    @winrt_commethod(9)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ImageUri(self) -> win32more.Windows.Foundation.Uri: ...
    Description = property(get_Description, None)
    ImageUri = property(get_ImageUri, None)
    Keywords = property(get_Keywords, None)
    ProductType = property(get_ProductType, None)
    Tag = property(get_Tag, None)
class IProductPurchaseDisplayProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties'
    _iid_ = Guid('{d70b7420-bc92-401b-a809-c9b2e5dbbdaf}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Image(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_Image(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Description = property(get_Description, put_Description)
    Image = property(get_Image, put_Image)
    Name = property(get_Name, put_Name)
class IProductPurchaseDisplayPropertiesFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IProductPurchaseDisplayPropertiesFactory'
    _iid_ = Guid('{6f491df4-32d6-4b40-b474-b83038a4d9cf}')
    @winrt_commethod(6)
    def CreateProductPurchaseDisplayProperties(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
class IPurchaseResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IPurchaseResults'
    _iid_ = Guid('{ed50b37e-8656-4f65-b8c8-ac7e0cb1a1c2}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Store.ProductPurchaseStatus: ...
    @winrt_commethod(7)
    def get_TransactionId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_ReceiptXml(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_OfferId(self) -> WinRT_String: ...
    OfferId = property(get_OfferId, None)
    ReceiptXml = property(get_ReceiptXml, None)
    Status = property(get_Status, None)
    TransactionId = property(get_TransactionId, None)
class IUnfulfilledConsumable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.IUnfulfilledConsumable'
    _iid_ = Guid('{2df7fbbb-1cdd-4cb8-a014-7b9cf8986927}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TransactionId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_OfferId(self) -> WinRT_String: ...
    OfferId = property(get_OfferId, None)
    ProductId = property(get_ProductId, None)
    TransactionId = property(get_TransactionId, None)
class LicenseChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d4a50255-1369-4c36-832f-6f2d88e3659b}')
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class LicenseInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.ILicenseInformation
    _classid_ = 'Windows.ApplicationModel.Store.LicenseInformation'
    @winrt_mixinmethod
    def get_ProductLicenses(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.ProductLicense]: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTrial(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def add_LicenseChanged(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation, handler: win32more.Windows.ApplicationModel.Store.LicenseChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LicenseChanged(self: win32more.Windows.ApplicationModel.Store.ILicenseInformation, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExpirationDate = property(get_ExpirationDate, None)
    IsActive = property(get_IsActive, None)
    IsTrial = property(get_IsTrial, None)
    ProductLicenses = property(get_ProductLicenses, None)
    LicenseChanged = event()
class ListingInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IListingInformation
    _classid_ = 'Windows.ApplicationModel.Store.ListingInformation'
    @winrt_mixinmethod
    def get_CurrentMarket(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductListings(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.ProductListing]: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AgeRating(self: win32more.Windows.ApplicationModel.Store.IListingInformation) -> UInt32: ...
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: win32more.Windows.ApplicationModel.Store.IListingInformation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: win32more.Windows.ApplicationModel.Store.IListingInformation2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: win32more.Windows.ApplicationModel.Store.IListingInformation2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: win32more.Windows.ApplicationModel.Store.IListingInformation2) -> WinRT_String: ...
    AgeRating = property(get_AgeRating, None)
    CurrencyCode = property(get_CurrencyCode, None)
    CurrentMarket = property(get_CurrentMarket, None)
    Description = property(get_Description, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    FormattedPrice = property(get_FormattedPrice, None)
    IsOnSale = property(get_IsOnSale, None)
    Name = property(get_Name, None)
    ProductListings = property(get_ProductListings, None)
    SaleEndDate = property(get_SaleEndDate, None)
class ProductLicense(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IProductLicense
    _classid_ = 'Windows.ApplicationModel.Store.ProductLicense'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.Store.IProductLicense) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.ApplicationModel.Store.IProductLicense) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.ApplicationModel.Store.IProductLicense) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsConsumable(self: win32more.Windows.ApplicationModel.Store.IProductLicenseWithFulfillment) -> Boolean: ...
    ExpirationDate = property(get_ExpirationDate, None)
    IsActive = property(get_IsActive, None)
    IsConsumable = property(get_IsConsumable, None)
    ProductId = property(get_ProductId, None)
class ProductListing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IProductListing
    _classid_ = 'Windows.ApplicationModel.Store.ProductListing'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedPrice(self: win32more.Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Store.IProductListing) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Store.IProductListingWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Keywords(self: win32more.Windows.ApplicationModel.Store.IProductListingWithMetadata) -> win32more.Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ProductType(self: win32more.Windows.ApplicationModel.Store.IProductListingWithMetadata) -> win32more.Windows.ApplicationModel.Store.ProductType: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.ApplicationModel.Store.IProductListingWithMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ImageUri(self: win32more.Windows.ApplicationModel.Store.IProductListingWithMetadata) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_FormattedBasePrice(self: win32more.Windows.ApplicationModel.Store.IProductListing2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SaleEndDate(self: win32more.Windows.ApplicationModel.Store.IProductListing2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsOnSale(self: win32more.Windows.ApplicationModel.Store.IProductListing2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: win32more.Windows.ApplicationModel.Store.IProductListing2) -> WinRT_String: ...
    CurrencyCode = property(get_CurrencyCode, None)
    Description = property(get_Description, None)
    FormattedBasePrice = property(get_FormattedBasePrice, None)
    FormattedPrice = property(get_FormattedPrice, None)
    ImageUri = property(get_ImageUri, None)
    IsOnSale = property(get_IsOnSale, None)
    Keywords = property(get_Keywords, None)
    Name = property(get_Name, None)
    ProductId = property(get_ProductId, None)
    ProductType = property(get_ProductType, None)
    SaleEndDate = property(get_SaleEndDate, None)
    Tag = property(get_Tag, None)
class ProductPurchaseDisplayProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties
    _classid_ = 'Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties.CreateProductPurchaseDisplayProperties(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
    @winrt_factorymethod
    def CreateProductPurchaseDisplayProperties(cls: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayPropertiesFactory, name: WinRT_String) -> win32more.Windows.ApplicationModel.Store.ProductPurchaseDisplayProperties: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.ApplicationModel.Store.IProductPurchaseDisplayProperties, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Description = property(get_Description, put_Description)
    Image = property(get_Image, put_Image)
    Name = property(get_Name, put_Name)
class ProductPurchaseStatus(Enum, Int32):
    Succeeded = 0
    AlreadyPurchased = 1
    NotFulfilled = 2
    NotPurchased = 3
class ProductType(Enum, Int32):
    Unknown = 0
    Durable = 1
    Consumable = 2
class PurchaseResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IPurchaseResults
    _classid_ = 'Windows.ApplicationModel.Store.PurchaseResults'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Store.IPurchaseResults) -> win32more.Windows.ApplicationModel.Store.ProductPurchaseStatus: ...
    @winrt_mixinmethod
    def get_TransactionId(self: win32more.Windows.ApplicationModel.Store.IPurchaseResults) -> Guid: ...
    @winrt_mixinmethod
    def get_ReceiptXml(self: win32more.Windows.ApplicationModel.Store.IPurchaseResults) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OfferId(self: win32more.Windows.ApplicationModel.Store.IPurchaseResults) -> WinRT_String: ...
    OfferId = property(get_OfferId, None)
    ReceiptXml = property(get_ReceiptXml, None)
    Status = property(get_Status, None)
    TransactionId = property(get_TransactionId, None)
class UnfulfilledConsumable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.IUnfulfilledConsumable
    _classid_ = 'Windows.ApplicationModel.Store.UnfulfilledConsumable'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransactionId(self: win32more.Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> Guid: ...
    @winrt_mixinmethod
    def get_OfferId(self: win32more.Windows.ApplicationModel.Store.IUnfulfilledConsumable) -> WinRT_String: ...
    OfferId = property(get_OfferId, None)
    ProductId = property(get_ProductId, None)
    TransactionId = property(get_TransactionId, None)


make_ready(__name__)
