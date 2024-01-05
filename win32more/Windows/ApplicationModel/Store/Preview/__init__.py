from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Store.Preview
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Web.Core
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI.Xaml
import win32more.Windows.Win32.System.WinRT
DeliveryOptimizationDownloadMode = Int32
DeliveryOptimizationDownloadMode_Simple: DeliveryOptimizationDownloadMode = 0
DeliveryOptimizationDownloadMode_HttpOnly: DeliveryOptimizationDownloadMode = 1
DeliveryOptimizationDownloadMode_Lan: DeliveryOptimizationDownloadMode = 2
DeliveryOptimizationDownloadMode_Group: DeliveryOptimizationDownloadMode = 3
DeliveryOptimizationDownloadMode_Internet: DeliveryOptimizationDownloadMode = 4
DeliveryOptimizationDownloadMode_Bypass: DeliveryOptimizationDownloadMode = 5
DeliveryOptimizationDownloadModeSource = Int32
DeliveryOptimizationDownloadModeSource_Default: DeliveryOptimizationDownloadModeSource = 0
DeliveryOptimizationDownloadModeSource_Policy: DeliveryOptimizationDownloadModeSource = 1
class DeliveryOptimizationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings
    _classid_ = 'Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings'
    @winrt_mixinmethod
    def get_DownloadMode(self: win32more.Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadMode: ...
    @winrt_mixinmethod
    def get_DownloadModeSource(self: win32more.Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadModeSource: ...
    @winrt_classmethod
    def GetCurrentSettings(cls: win32more.Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettingsStatics) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings: ...
    DownloadMode = property(get_DownloadMode, None)
    DownloadModeSource = property(get_DownloadModeSource, None)
class IDeliveryOptimizationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings'
    _iid_ = Guid('{1810fda0-e853-565e-b874-7a8a7b9a0e0f}')
    @winrt_commethod(6)
    def get_DownloadMode(self) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadMode: ...
    @winrt_commethod(7)
    def get_DownloadModeSource(self) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadModeSource: ...
    DownloadMode = property(get_DownloadMode, None)
    DownloadModeSource = property(get_DownloadModeSource, None)
class IDeliveryOptimizationSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettingsStatics'
    _iid_ = Guid('{5c817caf-aed5-5999-b4c9-8c60898bc4f3}')
    @winrt_commethod(6)
    def GetCurrentSettings(self) -> win32more.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings: ...
class IStoreConfigurationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics'
    _iid_ = Guid('{728f7fc0-8628-42ec-84a2-07780eb44d8b}')
    @winrt_commethod(6)
    def SetSystemConfiguration(self, catalogHardwareManufacturerId: WinRT_String, catalogStoreContentModifierId: WinRT_String, systemConfigurationExpiration: win32more.Windows.Foundation.DateTime, catalogHardwareDescriptor: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def SetMobileOperatorConfiguration(self, mobileOperatorId: WinRT_String, appDownloadLimitInMegabytes: UInt32, updateDownloadLimitInMegabytes: UInt32) -> Void: ...
    @winrt_commethod(8)
    def SetStoreWebAccountId(self, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def IsStoreWebAccountId(self, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_commethod(10)
    def get_HardwareManufacturerInfo(self) -> win32more.Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo: ...
    @winrt_commethod(11)
    def FilterUnsupportedSystemFeaturesAsync(self, systemFeatures: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Store.Preview.StoreSystemFeature]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StoreSystemFeature]]: ...
    HardwareManufacturerInfo = property(get_HardwareManufacturerInfo, None)
class IStoreConfigurationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2'
    _iid_ = Guid('{657c4595-c8b7-4fe9-9f4c-4d71027d347e}')
    @winrt_commethod(6)
    def get_PurchasePromptingPolicy(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_PurchasePromptingPolicy(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    PurchasePromptingPolicy = property(get_PurchasePromptingPolicy, put_PurchasePromptingPolicy)
class IStoreConfigurationStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3'
    _iid_ = Guid('{6d45f57c-f144-4cb5-9d3f-4eb05e30b6d3}')
    @winrt_commethod(6)
    def HasStoreWebAccount(self) -> Boolean: ...
    @winrt_commethod(7)
    def HasStoreWebAccountForUser(self, user: win32more.Windows.System.User) -> Boolean: ...
    @winrt_commethod(8)
    def GetStoreLogDataAsync(self, options: win32more.Windows.ApplicationModel.Store.Preview.StoreLogOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_commethod(9)
    def SetStoreWebAccountIdForUser(self, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def IsStoreWebAccountIdForUser(self, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def GetPurchasePromptingPolicyForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(12)
    def SetPurchasePromptingPolicyForUser(self, user: win32more.Windows.System.User, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
class IStoreConfigurationStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4'
    _iid_ = Guid('{20ff56d2-4ee3-4cf0-9b12-552c03310f75}')
    @winrt_commethod(6)
    def GetStoreWebAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetStoreWebAccountIdForUser(self, user: win32more.Windows.System.User) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetEnterpriseStoreWebAccountId(self, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def SetEnterpriseStoreWebAccountIdForUser(self, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetEnterpriseStoreWebAccountId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetEnterpriseStoreWebAccountIdForUser(self, user: win32more.Windows.System.User) -> WinRT_String: ...
    @winrt_commethod(12)
    def ShouldRestrictToEnterpriseStoreOnly(self) -> Boolean: ...
    @winrt_commethod(13)
    def ShouldRestrictToEnterpriseStoreOnlyForUser(self, user: win32more.Windows.System.User) -> Boolean: ...
class IStoreConfigurationStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5'
    _iid_ = Guid('{f7613191-8fa9-49db-822b-0160e7e4e5c5}')
    @winrt_commethod(6)
    def IsPinToDesktopSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsPinToTaskbarSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsPinToStartSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def PinToDesktop(self, appPackageFamilyName: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def PinToDesktopForUser(self, user: win32more.Windows.System.User, appPackageFamilyName: WinRT_String) -> Void: ...
class IStoreHardwareManufacturerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo'
    _iid_ = Guid('{f292dc08-c654-43ac-a21f-34801c9d3388}')
    @winrt_commethod(6)
    def get_HardwareManufacturerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_StoreContentModifierId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ModelName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ManufacturerName(self) -> WinRT_String: ...
    HardwareManufacturerId = property(get_HardwareManufacturerId, None)
    StoreContentModifierId = property(get_StoreContentModifierId, None)
    ModelName = property(get_ModelName, None)
    ManufacturerName = property(get_ManufacturerName, None)
class IStorePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreview'
    _iid_ = Guid('{8a157241-840e-49a9-bc01-5d5b01fbc8e9}')
    @winrt_commethod(6)
    def RequestProductPurchaseByProductIdAndSkuIdAsync(self, productId: WinRT_String, skuId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults]: ...
    @winrt_commethod(7)
    def LoadAddOnProductInfosAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo]]: ...
class IStorePreviewProductInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo'
    _iid_ = Guid('{1937dbb3-6c01-4c9d-85cd-5babaac2b351}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProductType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SkuInfoList(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo]: ...
    ProductId = property(get_ProductId, None)
    ProductType = property(get_ProductType, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    SkuInfoList = property(get_SkuInfoList, None)
class IStorePreviewPurchaseResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults'
    _iid_ = Guid('{b0daaed1-d6c5-4e53-a043-fba0d8e61231}')
    @winrt_commethod(6)
    def get_ProductPurchaseStatus(self) -> win32more.Windows.ApplicationModel.Store.Preview.StorePreviewProductPurchaseStatus: ...
    ProductPurchaseStatus = property(get_ProductPurchaseStatus, None)
class IStorePreviewSkuInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo'
    _iid_ = Guid('{81fd76e2-0b26-48d9-98ce-27461c669d6c}')
    @winrt_commethod(6)
    def get_ProductId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SkuId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SkuType(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_CustomDeveloperData(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_CurrencyCode(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_FormattedListPrice(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_ExtendedData(self) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    SkuId = property(get_SkuId, None)
    SkuType = property(get_SkuType, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    CustomDeveloperData = property(get_CustomDeveloperData, None)
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedListPrice = property(get_FormattedListPrice, None)
    ExtendedData = property(get_ExtendedData, None)
class IWebAuthenticationCoreManagerHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper'
    _iid_ = Guid('{06a50525-e715-4123-9276-9d6f865ba55f}')
    @winrt_commethod(6)
    def RequestTokenWithUIElementHostingAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, uiElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(7)
    def RequestTokenWithUIElementHostingAndWebAccountAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount, uiElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
class _StoreConfiguration_Meta_(ComPtr.__class__):
    pass
class StoreConfiguration(ComPtr, metaclass=_StoreConfiguration_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StoreConfiguration'
    @winrt_classmethod
    def IsPinToDesktopSupported(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def IsPinToTaskbarSupported(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def IsPinToStartSupported(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def PinToDesktop(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5, appPackageFamilyName: WinRT_String) -> Void: ...
    @winrt_classmethod
    def PinToDesktopForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5, user: win32more.Windows.System.User, appPackageFamilyName: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetStoreWebAccountId(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetStoreWebAccountIdForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: win32more.Windows.System.User) -> WinRT_String: ...
    @winrt_classmethod
    def SetEnterpriseStoreWebAccountId(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetEnterpriseStoreWebAccountIdForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetEnterpriseStoreWebAccountId(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetEnterpriseStoreWebAccountIdForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: win32more.Windows.System.User) -> WinRT_String: ...
    @winrt_classmethod
    def ShouldRestrictToEnterpriseStoreOnly(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> Boolean: ...
    @winrt_classmethod
    def ShouldRestrictToEnterpriseStoreOnlyForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: win32more.Windows.System.User) -> Boolean: ...
    @winrt_classmethod
    def HasStoreWebAccount(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3) -> Boolean: ...
    @winrt_classmethod
    def HasStoreWebAccountForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: win32more.Windows.System.User) -> Boolean: ...
    @winrt_classmethod
    def GetStoreLogDataAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, options: win32more.Windows.ApplicationModel.Store.Preview.StoreLogOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_classmethod
    def SetStoreWebAccountIdForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsStoreWebAccountIdForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: win32more.Windows.System.User, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def GetPurchasePromptingPolicyForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_classmethod
    def SetPurchasePromptingPolicyForUser(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: win32more.Windows.System.User, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_classmethod
    def get_PurchasePromptingPolicy(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_classmethod
    def put_PurchasePromptingPolicy(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_classmethod
    def SetSystemConfiguration(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, catalogHardwareManufacturerId: WinRT_String, catalogStoreContentModifierId: WinRT_String, systemConfigurationExpiration: win32more.Windows.Foundation.DateTime, catalogHardwareDescriptor: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetMobileOperatorConfiguration(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, mobileOperatorId: WinRT_String, appDownloadLimitInMegabytes: UInt32, updateDownloadLimitInMegabytes: UInt32) -> Void: ...
    @winrt_classmethod
    def SetStoreWebAccountId(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsStoreWebAccountId(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def get_HardwareManufacturerInfo(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics) -> win32more.Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo: ...
    @winrt_classmethod
    def FilterUnsupportedSystemFeaturesAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, systemFeatures: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Store.Preview.StoreSystemFeature]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StoreSystemFeature]]: ...
    _StoreConfiguration_Meta_.PurchasePromptingPolicy = property(get_PurchasePromptingPolicy.__wrapped__, put_PurchasePromptingPolicy.__wrapped__)
    _StoreConfiguration_Meta_.HardwareManufacturerInfo = property(get_HardwareManufacturerInfo.__wrapped__, None)
class StoreHardwareManufacturerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo'
    @winrt_mixinmethod
    def get_HardwareManufacturerId(self: win32more.Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StoreContentModifierId(self: win32more.Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelName(self: win32more.Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ManufacturerName(self: win32more.Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    HardwareManufacturerId = property(get_HardwareManufacturerId, None)
    StoreContentModifierId = property(get_StoreContentModifierId, None)
    ModelName = property(get_ModelName, None)
    ManufacturerName = property(get_ManufacturerName, None)
StoreLogOptions = UInt32
StoreLogOptions_None: StoreLogOptions = 0
StoreLogOptions_TryElevate: StoreLogOptions = 1
class StorePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreview'
    @winrt_classmethod
    def RequestProductPurchaseByProductIdAndSkuIdAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IStorePreview, productId: WinRT_String, skuId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults]: ...
    @winrt_classmethod
    def LoadAddOnProductInfosAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IStorePreview) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo]]: ...
class StorePreviewProductInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductType(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuInfoList(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo]: ...
    ProductId = property(get_ProductId, None)
    ProductType = property(get_ProductType, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    SkuInfoList = property(get_SkuInfoList, None)
StorePreviewProductPurchaseStatus = Int32
StorePreviewProductPurchaseStatus_Succeeded: StorePreviewProductPurchaseStatus = 0
StorePreviewProductPurchaseStatus_AlreadyPurchased: StorePreviewProductPurchaseStatus = 1
StorePreviewProductPurchaseStatus_NotFulfilled: StorePreviewProductPurchaseStatus = 2
StorePreviewProductPurchaseStatus_NotPurchased: StorePreviewProductPurchaseStatus = 3
class StorePreviewPurchaseResults(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults'
    @winrt_mixinmethod
    def get_ProductPurchaseStatus(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults) -> win32more.Windows.ApplicationModel.Store.Preview.StorePreviewProductPurchaseStatus: ...
    ProductPurchaseStatus = property(get_ProductPurchaseStatus, None)
class StorePreviewSkuInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo'
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuId(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuType(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CustomDeveloperData(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedListPrice(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExtendedData(self: win32more.Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    ProductId = property(get_ProductId, None)
    SkuId = property(get_SkuId, None)
    SkuType = property(get_SkuType, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    CustomDeveloperData = property(get_CustomDeveloperData, None)
    CurrencyCode = property(get_CurrencyCode, None)
    FormattedListPrice = property(get_FormattedListPrice, None)
    ExtendedData = property(get_ExtendedData, None)
StoreSystemFeature = Int32
StoreSystemFeature_ArchitectureX86: StoreSystemFeature = 0
StoreSystemFeature_ArchitectureX64: StoreSystemFeature = 1
StoreSystemFeature_ArchitectureArm: StoreSystemFeature = 2
StoreSystemFeature_DirectX9: StoreSystemFeature = 3
StoreSystemFeature_DirectX10: StoreSystemFeature = 4
StoreSystemFeature_DirectX11: StoreSystemFeature = 5
StoreSystemFeature_D3D12HardwareFL11: StoreSystemFeature = 6
StoreSystemFeature_D3D12HardwareFL12: StoreSystemFeature = 7
StoreSystemFeature_Memory300MB: StoreSystemFeature = 8
StoreSystemFeature_Memory750MB: StoreSystemFeature = 9
StoreSystemFeature_Memory1GB: StoreSystemFeature = 10
StoreSystemFeature_Memory2GB: StoreSystemFeature = 11
StoreSystemFeature_CameraFront: StoreSystemFeature = 12
StoreSystemFeature_CameraRear: StoreSystemFeature = 13
StoreSystemFeature_Gyroscope: StoreSystemFeature = 14
StoreSystemFeature_Hover: StoreSystemFeature = 15
StoreSystemFeature_Magnetometer: StoreSystemFeature = 16
StoreSystemFeature_Nfc: StoreSystemFeature = 17
StoreSystemFeature_Resolution720P: StoreSystemFeature = 18
StoreSystemFeature_ResolutionWvga: StoreSystemFeature = 19
StoreSystemFeature_ResolutionWvgaOr720P: StoreSystemFeature = 20
StoreSystemFeature_ResolutionWxga: StoreSystemFeature = 21
StoreSystemFeature_ResolutionWvgaOrWxga: StoreSystemFeature = 22
StoreSystemFeature_ResolutionWxgaOr720P: StoreSystemFeature = 23
StoreSystemFeature_Memory4GB: StoreSystemFeature = 24
StoreSystemFeature_Memory6GB: StoreSystemFeature = 25
StoreSystemFeature_Memory8GB: StoreSystemFeature = 26
StoreSystemFeature_Memory12GB: StoreSystemFeature = 27
StoreSystemFeature_Memory16GB: StoreSystemFeature = 28
StoreSystemFeature_Memory20GB: StoreSystemFeature = 29
StoreSystemFeature_VideoMemory2GB: StoreSystemFeature = 30
StoreSystemFeature_VideoMemory4GB: StoreSystemFeature = 31
StoreSystemFeature_VideoMemory6GB: StoreSystemFeature = 32
StoreSystemFeature_VideoMemory1GB: StoreSystemFeature = 33
StoreSystemFeature_ArchitectureArm64: StoreSystemFeature = 34
class WebAuthenticationCoreManagerHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.WebAuthenticationCoreManagerHelper'
    @winrt_classmethod
    def RequestTokenWithUIElementHostingAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, uiElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenWithUIElementHostingAndWebAccountAsync(cls: win32more.Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount, uiElement: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...


make_ready(__name__)
