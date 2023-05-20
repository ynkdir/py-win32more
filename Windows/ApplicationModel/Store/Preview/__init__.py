from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Store.Preview
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authentication.Web.Core
import Windows.Security.Credentials
import Windows.Storage.Streams
import Windows.System
import Windows.UI.Xaml
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings
    _classid_ = 'Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings'
    @winrt_mixinmethod
    def get_DownloadMode(self: Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadMode: ...
    @winrt_mixinmethod
    def get_DownloadModeSource(self: Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadModeSource: ...
    @winrt_classmethod
    def GetCurrentSettings(cls: Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettingsStatics) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings: ...
    DownloadMode = property(get_DownloadMode, None)
    DownloadModeSource = property(get_DownloadModeSource, None)
class IDeliveryOptimizationSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettings'
    _iid_ = Guid('{1810fda0-e853-565e-b874-7a8a7b9a0e0f}')
    @winrt_commethod(6)
    def get_DownloadMode(self) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadMode: ...
    @winrt_commethod(7)
    def get_DownloadModeSource(self) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadModeSource: ...
    DownloadMode = property(get_DownloadMode, None)
    DownloadModeSource = property(get_DownloadModeSource, None)
class IDeliveryOptimizationSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IDeliveryOptimizationSettingsStatics'
    _iid_ = Guid('{5c817caf-aed5-5999-b4c9-8c60898bc4f3}')
    @winrt_commethod(6)
    def GetCurrentSettings(self) -> Windows.ApplicationModel.Store.Preview.DeliveryOptimizationSettings: ...
class IStoreConfigurationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics'
    _iid_ = Guid('{728f7fc0-8628-42ec-84a2-07780eb44d8b}')
    @winrt_commethod(6)
    def SetSystemConfiguration(self, catalogHardwareManufacturerId: WinRT_String, catalogStoreContentModifierId: WinRT_String, systemConfigurationExpiration: Windows.Foundation.DateTime, catalogHardwareDescriptor: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def SetMobileOperatorConfiguration(self, mobileOperatorId: WinRT_String, appDownloadLimitInMegabytes: UInt32, updateDownloadLimitInMegabytes: UInt32) -> Void: ...
    @winrt_commethod(8)
    def SetStoreWebAccountId(self, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def IsStoreWebAccountId(self, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_commethod(10)
    def get_HardwareManufacturerInfo(self) -> Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo: ...
    @winrt_commethod(11)
    def FilterUnsupportedSystemFeaturesAsync(self, systemFeatures: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Store.Preview.StoreSystemFeature]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StoreSystemFeature]]: ...
    HardwareManufacturerInfo = property(get_HardwareManufacturerInfo, None)
class IStoreConfigurationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2'
    _iid_ = Guid('{657c4595-c8b7-4fe9-9f4c-4d71027d347e}')
    @winrt_commethod(6)
    def get_PurchasePromptingPolicy(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_PurchasePromptingPolicy(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    PurchasePromptingPolicy = property(get_PurchasePromptingPolicy, put_PurchasePromptingPolicy)
class IStoreConfigurationStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3'
    _iid_ = Guid('{6d45f57c-f144-4cb5-9d3f-4eb05e30b6d3}')
    @winrt_commethod(6)
    def HasStoreWebAccount(self) -> Boolean: ...
    @winrt_commethod(7)
    def HasStoreWebAccountForUser(self, user: Windows.System.User) -> Boolean: ...
    @winrt_commethod(8)
    def GetStoreLogDataAsync(self, options: Windows.ApplicationModel.Store.Preview.StoreLogOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_commethod(9)
    def SetStoreWebAccountIdForUser(self, user: Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def IsStoreWebAccountIdForUser(self, user: Windows.System.User, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def GetPurchasePromptingPolicyForUser(self, user: Windows.System.User) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(12)
    def SetPurchasePromptingPolicyForUser(self, user: Windows.System.User, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
class IStoreConfigurationStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4'
    _iid_ = Guid('{20ff56d2-4ee3-4cf0-9b12-552c03310f75}')
    @winrt_commethod(6)
    def GetStoreWebAccountId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetStoreWebAccountIdForUser(self, user: Windows.System.User) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetEnterpriseStoreWebAccountId(self, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def SetEnterpriseStoreWebAccountIdForUser(self, user: Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetEnterpriseStoreWebAccountId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetEnterpriseStoreWebAccountIdForUser(self, user: Windows.System.User) -> WinRT_String: ...
    @winrt_commethod(12)
    def ShouldRestrictToEnterpriseStoreOnly(self) -> Boolean: ...
    @winrt_commethod(13)
    def ShouldRestrictToEnterpriseStoreOnlyForUser(self, user: Windows.System.User) -> Boolean: ...
class IStoreConfigurationStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def PinToDesktopForUser(self, user: Windows.System.User, appPackageFamilyName: WinRT_String) -> Void: ...
class IStoreHardwareManufacturerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreview'
    _iid_ = Guid('{8a157241-840e-49a9-bc01-5d5b01fbc8e9}')
    @winrt_commethod(6)
    def RequestProductPurchaseByProductIdAndSkuIdAsync(self, productId: WinRT_String, skuId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults]: ...
    @winrt_commethod(7)
    def LoadAddOnProductInfosAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo]]: ...
class IStorePreviewProductInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_SkuInfoList(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo]: ...
    ProductId = property(get_ProductId, None)
    ProductType = property(get_ProductType, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    SkuInfoList = property(get_SkuInfoList, None)
class IStorePreviewPurchaseResults(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults'
    _iid_ = Guid('{b0daaed1-d6c5-4e53-a043-fba0d8e61231}')
    @winrt_commethod(6)
    def get_ProductPurchaseStatus(self) -> Windows.ApplicationModel.Store.Preview.StorePreviewProductPurchaseStatus: ...
    ProductPurchaseStatus = property(get_ProductPurchaseStatus, None)
class IStorePreviewSkuInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper'
    _iid_ = Guid('{06a50525-e715-4123-9276-9d6f865ba55f}')
    @winrt_commethod(6)
    def RequestTokenWithUIElementHostingAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, uiElement: Windows.UI.Xaml.UIElement) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(7)
    def RequestTokenWithUIElementHostingAndWebAccountAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount, uiElement: Windows.UI.Xaml.UIElement) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
class _StoreConfiguration_Meta_(ComPtr.__class__):
    pass
class StoreConfiguration(ComPtr, metaclass=_StoreConfiguration_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StoreConfiguration'
    @winrt_classmethod
    def IsPinToDesktopSupported(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def IsPinToTaskbarSupported(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def IsPinToStartSupported(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5) -> Boolean: ...
    @winrt_classmethod
    def PinToDesktop(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5, appPackageFamilyName: WinRT_String) -> Void: ...
    @winrt_classmethod
    def PinToDesktopForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics5, user: Windows.System.User, appPackageFamilyName: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetStoreWebAccountId(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetStoreWebAccountIdForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: Windows.System.User) -> WinRT_String: ...
    @winrt_classmethod
    def SetEnterpriseStoreWebAccountId(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetEnterpriseStoreWebAccountIdForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetEnterpriseStoreWebAccountId(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetEnterpriseStoreWebAccountIdForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: Windows.System.User) -> WinRT_String: ...
    @winrt_classmethod
    def ShouldRestrictToEnterpriseStoreOnly(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4) -> Boolean: ...
    @winrt_classmethod
    def ShouldRestrictToEnterpriseStoreOnlyForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics4, user: Windows.System.User) -> Boolean: ...
    @winrt_classmethod
    def HasStoreWebAccount(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3) -> Boolean: ...
    @winrt_classmethod
    def HasStoreWebAccountForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: Windows.System.User) -> Boolean: ...
    @winrt_classmethod
    def GetStoreLogDataAsync(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, options: Windows.ApplicationModel.Store.Preview.StoreLogOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_classmethod
    def SetStoreWebAccountIdForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: Windows.System.User, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsStoreWebAccountIdForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: Windows.System.User, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def GetPurchasePromptingPolicyForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: Windows.System.User) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_classmethod
    def SetPurchasePromptingPolicyForUser(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics3, user: Windows.System.User, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_classmethod
    def get_PurchasePromptingPolicy(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_classmethod
    def put_PurchasePromptingPolicy(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics2, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_classmethod
    def SetSystemConfiguration(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, catalogHardwareManufacturerId: WinRT_String, catalogStoreContentModifierId: WinRT_String, systemConfigurationExpiration: Windows.Foundation.DateTime, catalogHardwareDescriptor: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SetMobileOperatorConfiguration(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, mobileOperatorId: WinRT_String, appDownloadLimitInMegabytes: UInt32, updateDownloadLimitInMegabytes: UInt32) -> Void: ...
    @winrt_classmethod
    def SetStoreWebAccountId(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, webAccountId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsStoreWebAccountId(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, webAccountId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def get_HardwareManufacturerInfo(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics) -> Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo: ...
    @winrt_classmethod
    def FilterUnsupportedSystemFeaturesAsync(cls: Windows.ApplicationModel.Store.Preview.IStoreConfigurationStatics, systemFeatures: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Store.Preview.StoreSystemFeature]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StoreSystemFeature]]: ...
    _StoreConfiguration_Meta_.PurchasePromptingPolicy = property(get_PurchasePromptingPolicy.__wrapped__, put_PurchasePromptingPolicy.__wrapped__)
    _StoreConfiguration_Meta_.HardwareManufacturerInfo = property(get_HardwareManufacturerInfo.__wrapped__, None)
class StoreHardwareManufacturerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StoreHardwareManufacturerInfo'
    @winrt_mixinmethod
    def get_HardwareManufacturerId(self: Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StoreContentModifierId(self: Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelName(self: Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ManufacturerName(self: Windows.ApplicationModel.Store.Preview.IStoreHardwareManufacturerInfo) -> WinRT_String: ...
    HardwareManufacturerId = property(get_HardwareManufacturerId, None)
    StoreContentModifierId = property(get_StoreContentModifierId, None)
    ModelName = property(get_ModelName, None)
    ManufacturerName = property(get_ManufacturerName, None)
StoreLogOptions = UInt32
StoreLogOptions_None: StoreLogOptions = 0
StoreLogOptions_TryElevate: StoreLogOptions = 1
class StorePreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreview'
    @winrt_classmethod
    def RequestProductPurchaseByProductIdAndSkuIdAsync(cls: Windows.ApplicationModel.Store.Preview.IStorePreview, productId: WinRT_String, skuId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults]: ...
    @winrt_classmethod
    def LoadAddOnProductInfosAsync(cls: Windows.ApplicationModel.Store.Preview.IStorePreview) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo]]: ...
class StorePreviewProductInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewProductInfo'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProductType(self: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuInfoList(self: Windows.ApplicationModel.Store.Preview.IStorePreviewProductInfo) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewPurchaseResults'
    @winrt_mixinmethod
    def get_ProductPurchaseStatus(self: Windows.ApplicationModel.Store.Preview.IStorePreviewPurchaseResults) -> Windows.ApplicationModel.Store.Preview.StorePreviewProductPurchaseStatus: ...
    ProductPurchaseStatus = property(get_ProductPurchaseStatus, None)
class StorePreviewSkuInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo
    _classid_ = 'Windows.ApplicationModel.Store.Preview.StorePreviewSkuInfo'
    @winrt_mixinmethod
    def get_ProductId(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuId(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SkuType(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CustomDeveloperData(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrencyCode(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedListPrice(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExtendedData(self: Windows.ApplicationModel.Store.Preview.IStorePreviewSkuInfo) -> WinRT_String: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.Preview.WebAuthenticationCoreManagerHelper'
    @winrt_classmethod
    def RequestTokenWithUIElementHostingAsync(cls: Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, uiElement: Windows.UI.Xaml.UIElement) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenWithUIElementHostingAndWebAccountAsync(cls: Windows.ApplicationModel.Store.Preview.IWebAuthenticationCoreManagerHelper, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount, uiElement: Windows.UI.Xaml.UIElement) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
make_head(_module, 'DeliveryOptimizationSettings')
make_head(_module, 'IDeliveryOptimizationSettings')
make_head(_module, 'IDeliveryOptimizationSettingsStatics')
make_head(_module, 'IStoreConfigurationStatics')
make_head(_module, 'IStoreConfigurationStatics2')
make_head(_module, 'IStoreConfigurationStatics3')
make_head(_module, 'IStoreConfigurationStatics4')
make_head(_module, 'IStoreConfigurationStatics5')
make_head(_module, 'IStoreHardwareManufacturerInfo')
make_head(_module, 'IStorePreview')
make_head(_module, 'IStorePreviewProductInfo')
make_head(_module, 'IStorePreviewPurchaseResults')
make_head(_module, 'IStorePreviewSkuInfo')
make_head(_module, 'IWebAuthenticationCoreManagerHelper')
make_head(_module, 'StoreConfiguration')
make_head(_module, 'StoreHardwareManufacturerInfo')
make_head(_module, 'StorePreview')
make_head(_module, 'StorePreviewProductInfo')
make_head(_module, 'StorePreviewPurchaseResults')
make_head(_module, 'StorePreviewSkuInfo')
make_head(_module, 'WebAuthenticationCoreManagerHelper')
