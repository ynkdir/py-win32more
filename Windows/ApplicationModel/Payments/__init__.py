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
import Windows.ApplicationModel.Payments
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPaymentAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5f2264e9-6f3a-4166-a0-18-0a-0b-06-bb-32-b5')
    @winrt_commethod(6)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Country(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AddressLines(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def put_AddressLines(self, value: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(10)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Region(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_City(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_City(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_DependentLocality(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_DependentLocality(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_PostalCode(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_PostalCode(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_SortingCode(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_SortingCode(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_LanguageCode(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_LanguageCode(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_Organization(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def put_Organization(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(24)
    def get_Recipient(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def put_Recipient(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(26)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def put_PhoneNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(28)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    Country = property(get_Country, put_Country)
    AddressLines = property(get_AddressLines, put_AddressLines)
    Region = property(get_Region, put_Region)
    City = property(get_City, put_City)
    DependentLocality = property(get_DependentLocality, put_DependentLocality)
    PostalCode = property(get_PostalCode, put_PostalCode)
    SortingCode = property(get_SortingCode, put_SortingCode)
    LanguageCode = property(get_LanguageCode, put_LanguageCode)
    Organization = property(get_Organization, put_Organization)
    Recipient = property(get_Recipient, put_Recipient)
    PhoneNumber = property(get_PhoneNumber, put_PhoneNumber)
    Properties = property(get_Properties, None)
class IPaymentCanMakePaymentResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7696fe55-d5d3-4d3d-b3-45-45-59-17-59-c5-10')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus: ...
    Status = property(get_Status, None)
class IPaymentCanMakePaymentResultFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bbdcaa3e-7d49-4f69-aa-53-2a-0f-81-64-b7-c9')
    @winrt_commethod(6)
    def Create(self, value: Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus) -> Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult: ...
class IPaymentCurrencyAmount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e3a3e9e0-b41f-4987-bd-cb-07-13-31-f2-da-a4')
    @winrt_commethod(6)
    def get_Currency(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Currency(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CurrencySystem(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_CurrencySystem(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Value(self, value: WinRT_String) -> Void: ...
    Currency = property(get_Currency, put_Currency)
    CurrencySystem = property(get_CurrencySystem, put_CurrencySystem)
    Value = property(get_Value, put_Value)
class IPaymentCurrencyAmountFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3257d338-140c-4575-85-35-f7-73-17-8c-09-a7')
    @winrt_commethod(6)
    def Create(self, value: WinRT_String, currency: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(7)
    def CreateWithCurrencySystem(self, value: WinRT_String, currency: WinRT_String, currencySystem: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
class IPaymentDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('53bb2d7d-e0eb-4053-8e-ae-ce-7c-48-e0-29-45')
    @winrt_commethod(6)
    def get_Total(self) -> Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_commethod(7)
    def put_Total(self, value: Windows.ApplicationModel.Payments.PaymentItem) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]: ...
    @winrt_commethod(9)
    def put_DisplayItems(self, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]) -> Void: ...
    @winrt_commethod(10)
    def get_ShippingOptions(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentShippingOption]: ...
    @winrt_commethod(11)
    def put_ShippingOptions(self, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentShippingOption]) -> Void: ...
    @winrt_commethod(12)
    def get_Modifiers(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentDetailsModifier]: ...
    @winrt_commethod(13)
    def put_Modifiers(self, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentDetailsModifier]) -> Void: ...
    Total = property(get_Total, put_Total)
    DisplayItems = property(get_DisplayItems, put_DisplayItems)
    ShippingOptions = property(get_ShippingOptions, put_ShippingOptions)
    Modifiers = property(get_Modifiers, put_Modifiers)
class IPaymentDetailsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cfe8afee-c0ea-4ca1-8b-c7-6d-e6-7b-1f-37-63')
    @winrt_commethod(6)
    def Create(self, total: Windows.ApplicationModel.Payments.PaymentItem) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(7)
    def CreateWithDisplayItems(self, total: Windows.ApplicationModel.Payments.PaymentItem, displayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem]) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
class IPaymentDetailsModifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('be1c7d65-4323-41d7-b3-05-df-cb-76-5f-69-de')
    @winrt_commethod(6)
    def get_JsonData(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedMethodIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Total(self) -> Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_commethod(9)
    def get_AdditionalDisplayItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]: ...
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    Total = property(get_Total, None)
    AdditionalDisplayItems = property(get_AdditionalDisplayItems, None)
class IPaymentDetailsModifierFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('79005286-54de-429c-9e-4f-5d-ce-6e-10-eb-ce')
    @winrt_commethod(6)
    def Create(self, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_commethod(7)
    def CreateWithAdditionalDisplayItems(self, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem]) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_commethod(8)
    def CreateWithAdditionalDisplayItemsAndJsonData(self, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem], jsonData: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
class IPaymentItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('685ac88b-79b2-4b76-9e-03-a8-76-22-3d-fe-72')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Amount(self) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(9)
    def put_Amount(self, value: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_commethod(10)
    def get_Pending(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Pending(self, value: Boolean) -> Void: ...
    Label = property(get_Label, put_Label)
    Amount = property(get_Amount, put_Amount)
    Pending = property(get_Pending, put_Pending)
class IPaymentItemFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c6ab7ad8-2503-4d1d-a7-78-02-b2-e5-92-7b-2c')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Windows.ApplicationModel.Payments.PaymentItem: ...
class IPaymentMediator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb0ee829-ec0c-449a-83-da-7a-e3-07-33-65-a2')
    @winrt_commethod(6)
    def GetSupportedMethodIdsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def SubmitPaymentRequestAsync(self, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_commethod(8)
    def SubmitPaymentRequestWithChangeHandlerAsync(self, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest, changeHandler: Windows.ApplicationModel.Payments.PaymentRequestChangedHandler) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
class IPaymentMediator2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ceef98f1-e407-4128-8e-73-d9-3d-5f-82-27-86')
    @winrt_commethod(6)
    def CanMakePaymentAsync(self, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult]: ...
class IPaymentMerchantInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('63445050-0e94-4ed6-aa-cb-e6-01-2b-d3-27-a7')
    @winrt_commethod(6)
    def get_PackageFullName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    PackageFullName = property(get_PackageFullName, None)
    Uri = property(get_Uri, None)
class IPaymentMerchantInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e89ced3-ccb7-4167-a8-ec-e1-0a-e9-6d-bc-d1')
    @winrt_commethod(6)
    def Create(self, uri: Windows.Foundation.Uri) -> Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
class IPaymentMethodData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d1d3caf4-de98-4129-b1-b7-c3-ad-86-23-7b-f4')
    @winrt_commethod(6)
    def get_SupportedMethodIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_JsonData(self) -> WinRT_String: ...
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    JsonData = property(get_JsonData, None)
class IPaymentMethodDataFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8addd27f-9baa-4a82-83-42-a8-21-09-92-a3-6b')
    @winrt_commethod(6)
    def Create(self, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_commethod(7)
    def CreateWithJsonData(self, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], jsonData: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentMethodData: ...
class IPaymentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aaa30854-1f2b-4365-82-51-01-b5-89-15-a5-bc')
    @winrt_commethod(6)
    def get_RequestPayerEmail(self) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(7)
    def put_RequestPayerEmail(self, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(8)
    def get_RequestPayerName(self) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(9)
    def put_RequestPayerName(self, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(10)
    def get_RequestPayerPhoneNumber(self) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(11)
    def put_RequestPayerPhoneNumber(self, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(12)
    def get_RequestShipping(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_RequestShipping(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ShippingType(self) -> Windows.ApplicationModel.Payments.PaymentShippingType: ...
    @winrt_commethod(15)
    def put_ShippingType(self, value: Windows.ApplicationModel.Payments.PaymentShippingType) -> Void: ...
    RequestPayerEmail = property(get_RequestPayerEmail, put_RequestPayerEmail)
    RequestPayerName = property(get_RequestPayerName, put_RequestPayerName)
    RequestPayerPhoneNumber = property(get_RequestPayerPhoneNumber, put_RequestPayerPhoneNumber)
    RequestShipping = property(get_RequestShipping, put_RequestShipping)
    ShippingType = property(get_ShippingType, put_ShippingType)
class IPaymentRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b74942e1-ed7b-47eb-bc-08-78-cc-5d-68-96-b6')
    @winrt_commethod(6)
    def get_MerchantInfo(self) -> Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_commethod(7)
    def get_Details(self) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(8)
    def get_MethodData(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentMethodData]: ...
    @winrt_commethod(9)
    def get_Options(self) -> Windows.ApplicationModel.Payments.PaymentOptions: ...
    MerchantInfo = property(get_MerchantInfo, None)
    Details = property(get_Details, None)
    MethodData = property(get_MethodData, None)
    Options = property(get_Options, None)
class IPaymentRequest2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b63ccfb5-5998-493e-a0-4c-67-04-8a-50-f1-41')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IPaymentRequestChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c6145e44-cd8b-4be4-b5-55-27-c9-91-94-c0-c5')
    @winrt_commethod(6)
    def get_ChangeKind(self) -> Windows.ApplicationModel.Payments.PaymentRequestChangeKind: ...
    @winrt_commethod(7)
    def get_ShippingAddress(self) -> Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_commethod(8)
    def get_SelectedShippingOption(self) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(9)
    def Acknowledge(self, changeResult: Windows.ApplicationModel.Payments.PaymentRequestChangedResult) -> Void: ...
    ChangeKind = property(get_ChangeKind, None)
    ShippingAddress = property(get_ShippingAddress, None)
    SelectedShippingOption = property(get_SelectedShippingOption, None)
class IPaymentRequestChangedResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('df699e5c-16c4-47ad-94-01-84-40-ec-07-57-db')
    @winrt_commethod(6)
    def get_ChangeAcceptedByMerchant(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ChangeAcceptedByMerchant(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_UpdatedPaymentDetails(self) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(11)
    def put_UpdatedPaymentDetails(self, value: Windows.ApplicationModel.Payments.PaymentDetails) -> Void: ...
    ChangeAcceptedByMerchant = property(get_ChangeAcceptedByMerchant, put_ChangeAcceptedByMerchant)
    Message = property(get_Message, put_Message)
    UpdatedPaymentDetails = property(get_UpdatedPaymentDetails, put_UpdatedPaymentDetails)
class IPaymentRequestChangedResultFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('08740f56-1d33-4431-81-4b-67-ea-24-bf-21-db')
    @winrt_commethod(6)
    def Create(self, changeAcceptedByMerchant: Boolean) -> Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_commethod(7)
    def CreateWithPaymentDetails(self, changeAcceptedByMerchant: Boolean, updatedPaymentDetails: Windows.ApplicationModel.Payments.PaymentDetails) -> Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
class IPaymentRequestFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3e8a79dc-6b74-42d3-b1-03-f0-de-35-fb-18-48')
    @winrt_commethod(6)
    def Create(self, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData]) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(7)
    def CreateWithMerchantInfo(self, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(8)
    def CreateWithMerchantInfoAndOptions(self, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: Windows.ApplicationModel.Payments.PaymentOptions) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
class IPaymentRequestFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e6ce1325-a506-4372-b7-ef-1a-03-1d-56-62-d1')
    @winrt_commethod(6)
    def CreateWithMerchantInfoOptionsAndId(self, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: Windows.ApplicationModel.Payments.PaymentOptions, id: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
class IPaymentRequestSubmitResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7b9c3912-30f2-4e90-b2-49-8c-e7-d7-8f-fe-56')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.Payments.PaymentRequestStatus: ...
    @winrt_commethod(7)
    def get_Response(self) -> Windows.ApplicationModel.Payments.PaymentResponse: ...
    Status = property(get_Status, None)
    Response = property(get_Response, None)
class IPaymentResponse(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e1389457-8bd2-4888-9f-a8-97-98-55-45-10-8e')
    @winrt_commethod(6)
    def get_PaymentToken(self) -> Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_commethod(7)
    def get_ShippingOption(self) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(8)
    def get_ShippingAddress(self) -> Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_commethod(9)
    def get_PayerEmail(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_PayerName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PayerPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def CompleteAsync(self, status: Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus) -> Windows.Foundation.IAsyncAction: ...
    PaymentToken = property(get_PaymentToken, None)
    ShippingOption = property(get_ShippingOption, None)
    ShippingAddress = property(get_ShippingAddress, None)
    PayerEmail = property(get_PayerEmail, None)
    PayerName = property(get_PayerName, None)
    PayerPhoneNumber = property(get_PayerPhoneNumber, None)
class IPaymentShippingOption(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('13372ada-9753-4574-89-66-93-14-5a-76-c7-f9')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Amount(self) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(9)
    def put_Amount(self, value: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    Label = property(get_Label, put_Label)
    Amount = property(get_Amount, put_Amount)
    Tag = property(get_Tag, put_Tag)
    IsSelected = property(get_IsSelected, put_IsSelected)
class IPaymentShippingOptionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5de5f917-b2d7-446b-9d-73-61-23-fb-ca-3b-c6')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(7)
    def CreateWithSelected(self, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(8)
    def CreateWithSelectedAndTag(self, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean, tag: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
class IPaymentToken(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bbcac013-ccd0-41f2-b2-a1-0a-2e-4b-5d-ce-25')
    @winrt_commethod(6)
    def get_PaymentMethodId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_JsonDetails(self) -> WinRT_String: ...
    PaymentMethodId = property(get_PaymentMethodId, None)
    JsonDetails = property(get_JsonDetails, None)
class IPaymentTokenFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('988cd7aa-4753-4904-83-73-dd-7b-08-b9-95-c1')
    @winrt_commethod(6)
    def Create(self, paymentMethodId: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_commethod(7)
    def CreateWithJsonDetails(self, paymentMethodId: WinRT_String, jsonDetails: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentToken: ...
class PaymentAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentAddress'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_Country(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Country(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AddressLines(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_AddressLines(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_Region(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_City(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_City(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DependentLocality(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DependentLocality(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PostalCode(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PostalCode(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SortingCode(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SortingCode(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LanguageCode(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LanguageCode(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Organization(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Organization(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Recipient(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Recipient(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PhoneNumber(self: Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.ApplicationModel.Payments.IPaymentAddress) -> Windows.Foundation.Collections.ValueSet: ...
    Country = property(get_Country, put_Country)
    AddressLines = property(get_AddressLines, put_AddressLines)
    Region = property(get_Region, put_Region)
    City = property(get_City, put_City)
    DependentLocality = property(get_DependentLocality, put_DependentLocality)
    PostalCode = property(get_PostalCode, put_PostalCode)
    SortingCode = property(get_SortingCode, put_SortingCode)
    LanguageCode = property(get_LanguageCode, put_LanguageCode)
    Organization = property(get_Organization, put_Organization)
    Recipient = property(get_Recipient, put_Recipient)
    PhoneNumber = property(get_PhoneNumber, put_PhoneNumber)
    Properties = property(get_Properties, None)
class PaymentCanMakePaymentResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResultFactory, value: Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus) -> Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResult) -> Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus: ...
    Status = property(get_Status, None)
PaymentCanMakePaymentResultStatus = Int32
PaymentCanMakePaymentResultStatus_Unknown: PaymentCanMakePaymentResultStatus = 0
PaymentCanMakePaymentResultStatus_Yes: PaymentCanMakePaymentResultStatus = 1
PaymentCanMakePaymentResultStatus_No: PaymentCanMakePaymentResultStatus = 2
PaymentCanMakePaymentResultStatus_NotAllowed: PaymentCanMakePaymentResultStatus = 3
PaymentCanMakePaymentResultStatus_UserNotSignedIn: PaymentCanMakePaymentResultStatus = 4
PaymentCanMakePaymentResultStatus_SpecifiedPaymentMethodIdsNotSupported: PaymentCanMakePaymentResultStatus = 5
PaymentCanMakePaymentResultStatus_NoQualifyingCardOnFile: PaymentCanMakePaymentResultStatus = 6
class PaymentCurrencyAmount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentCurrencyAmount'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentCurrencyAmountFactory, value: WinRT_String, currency: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_factorymethod
    def CreateWithCurrencySystem(cls: Windows.ApplicationModel.Payments.IPaymentCurrencyAmountFactory, value: WinRT_String, currency: WinRT_String, currencySystem: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def get_Currency(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Currency(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CurrencySystem(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CurrencySystem(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    Currency = property(get_Currency, put_Currency)
    CurrencySystem = property(get_CurrencySystem, put_CurrencySystem)
    Value = property(get_Value, put_Value)
class PaymentDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentDetails'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentDetailsFactory, total: Windows.ApplicationModel.Payments.PaymentItem) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_factorymethod
    def CreateWithDisplayItems(cls: Windows.ApplicationModel.Payments.IPaymentDetailsFactory, total: Windows.ApplicationModel.Payments.PaymentItem, displayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem]) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def get_Total(self: Windows.ApplicationModel.Payments.IPaymentDetails) -> Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def put_Total(self: Windows.ApplicationModel.Payments.IPaymentDetails, value: Windows.ApplicationModel.Payments.PaymentItem) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayItems(self: Windows.ApplicationModel.Payments.IPaymentDetails) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]: ...
    @winrt_mixinmethod
    def put_DisplayItems(self: Windows.ApplicationModel.Payments.IPaymentDetails, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]) -> Void: ...
    @winrt_mixinmethod
    def get_ShippingOptions(self: Windows.ApplicationModel.Payments.IPaymentDetails) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentShippingOption]: ...
    @winrt_mixinmethod
    def put_ShippingOptions(self: Windows.ApplicationModel.Payments.IPaymentDetails, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentShippingOption]) -> Void: ...
    @winrt_mixinmethod
    def get_Modifiers(self: Windows.ApplicationModel.Payments.IPaymentDetails) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentDetailsModifier]: ...
    @winrt_mixinmethod
    def put_Modifiers(self: Windows.ApplicationModel.Payments.IPaymentDetails, value: Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentDetailsModifier]) -> Void: ...
    Total = property(get_Total, put_Total)
    DisplayItems = property(get_DisplayItems, put_DisplayItems)
    ShippingOptions = property(get_ShippingOptions, put_ShippingOptions)
    Modifiers = property(get_Modifiers, put_Modifiers)
class PaymentDetailsModifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentDetailsModifier'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_factorymethod
    def CreateWithAdditionalDisplayItems(cls: Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem]) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_factorymethod
    def CreateWithAdditionalDisplayItemsAndJsonData(cls: Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], total: Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentItem], jsonData: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_mixinmethod
    def get_JsonData(self: Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedMethodIds(self: Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Total(self: Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def get_AdditionalDisplayItems(self: Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentItem]: ...
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    Total = property(get_Total, None)
    AdditionalDisplayItems = property(get_AdditionalDisplayItems, None)
class PaymentItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentItem'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentItemFactory, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.ApplicationModel.Payments.IPaymentItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.ApplicationModel.Payments.IPaymentItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Amount(self: Windows.ApplicationModel.Payments.IPaymentItem) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def put_Amount(self: Windows.ApplicationModel.Payments.IPaymentItem, value: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_mixinmethod
    def get_Pending(self: Windows.ApplicationModel.Payments.IPaymentItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_Pending(self: Windows.ApplicationModel.Payments.IPaymentItem, value: Boolean) -> Void: ...
    Label = property(get_Label, put_Label)
    Amount = property(get_Amount, put_Amount)
    Pending = property(get_Pending, put_Pending)
class PaymentMediator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMediator'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Payments.PaymentMediator: ...
    @winrt_mixinmethod
    def GetSupportedMethodIdsAsync(self: Windows.ApplicationModel.Payments.IPaymentMediator) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def SubmitPaymentRequestAsync(self: Windows.ApplicationModel.Payments.IPaymentMediator, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_mixinmethod
    def SubmitPaymentRequestWithChangeHandlerAsync(self: Windows.ApplicationModel.Payments.IPaymentMediator, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest, changeHandler: Windows.ApplicationModel.Payments.PaymentRequestChangedHandler) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_mixinmethod
    def CanMakePaymentAsync(self: Windows.ApplicationModel.Payments.IPaymentMediator2, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult]: ...
class PaymentMerchantInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMerchantInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentMerchantInfoFactory, uri: Windows.Foundation.Uri) -> Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_mixinmethod
    def get_PackageFullName(self: Windows.ApplicationModel.Payments.IPaymentMerchantInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Payments.IPaymentMerchantInfo) -> Windows.Foundation.Uri: ...
    PackageFullName = property(get_PackageFullName, None)
    Uri = property(get_Uri, None)
class PaymentMethodData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMethodData'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentMethodDataFactory, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_factorymethod
    def CreateWithJsonData(cls: Windows.ApplicationModel.Payments.IPaymentMethodDataFactory, supportedMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String], jsonData: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_mixinmethod
    def get_SupportedMethodIds(self: Windows.ApplicationModel.Payments.IPaymentMethodData) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_JsonData(self: Windows.ApplicationModel.Payments.IPaymentMethodData) -> WinRT_String: ...
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    JsonData = property(get_JsonData, None)
PaymentOptionPresence = Int32
PaymentOptionPresence_None: PaymentOptionPresence = 0
PaymentOptionPresence_Optional: PaymentOptionPresence = 1
PaymentOptionPresence_Required: PaymentOptionPresence = 2
class PaymentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Payments.PaymentOptions: ...
    @winrt_mixinmethod
    def get_RequestPayerEmail(self: Windows.ApplicationModel.Payments.IPaymentOptions) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerEmail(self: Windows.ApplicationModel.Payments.IPaymentOptions, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestPayerName(self: Windows.ApplicationModel.Payments.IPaymentOptions) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerName(self: Windows.ApplicationModel.Payments.IPaymentOptions, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestPayerPhoneNumber(self: Windows.ApplicationModel.Payments.IPaymentOptions) -> Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerPhoneNumber(self: Windows.ApplicationModel.Payments.IPaymentOptions, value: Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestShipping(self: Windows.ApplicationModel.Payments.IPaymentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequestShipping(self: Windows.ApplicationModel.Payments.IPaymentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShippingType(self: Windows.ApplicationModel.Payments.IPaymentOptions) -> Windows.ApplicationModel.Payments.PaymentShippingType: ...
    @winrt_mixinmethod
    def put_ShippingType(self: Windows.ApplicationModel.Payments.IPaymentOptions, value: Windows.ApplicationModel.Payments.PaymentShippingType) -> Void: ...
    RequestPayerEmail = property(get_RequestPayerEmail, put_RequestPayerEmail)
    RequestPayerName = property(get_RequestPayerName, put_RequestPayerName)
    RequestPayerPhoneNumber = property(get_RequestPayerPhoneNumber, put_RequestPayerPhoneNumber)
    RequestShipping = property(get_RequestShipping, put_RequestShipping)
    ShippingType = property(get_ShippingType, put_ShippingType)
class PaymentRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequest'
    @winrt_factorymethod
    def CreateWithMerchantInfoOptionsAndId(cls: Windows.ApplicationModel.Payments.IPaymentRequestFactory2, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: Windows.ApplicationModel.Payments.PaymentOptions, id: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData]) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def CreateWithMerchantInfo(cls: Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def CreateWithMerchantInfoAndOptions(cls: Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: Windows.ApplicationModel.Payments.PaymentDetails, methodData: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: Windows.ApplicationModel.Payments.PaymentOptions) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def get_MerchantInfo(self: Windows.ApplicationModel.Payments.IPaymentRequest) -> Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_mixinmethod
    def get_Details(self: Windows.ApplicationModel.Payments.IPaymentRequest) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def get_MethodData(self: Windows.ApplicationModel.Payments.IPaymentRequest) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Payments.PaymentMethodData]: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.ApplicationModel.Payments.IPaymentRequest) -> Windows.ApplicationModel.Payments.PaymentOptions: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Payments.IPaymentRequest2) -> WinRT_String: ...
    MerchantInfo = property(get_MerchantInfo, None)
    Details = property(get_Details, None)
    MethodData = property(get_MethodData, None)
    Options = property(get_Options, None)
    Id = property(get_Id, None)
PaymentRequestChangeKind = Int32
PaymentRequestChangeKind_ShippingOption: PaymentRequestChangeKind = 0
PaymentRequestChangeKind_ShippingAddress: PaymentRequestChangeKind = 1
class PaymentRequestChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestChangedArgs'
    @winrt_mixinmethod
    def get_ChangeKind(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> Windows.ApplicationModel.Payments.PaymentRequestChangeKind: ...
    @winrt_mixinmethod
    def get_ShippingAddress(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_SelectedShippingOption(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def Acknowledge(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs, changeResult: Windows.ApplicationModel.Payments.PaymentRequestChangedResult) -> Void: ...
    ChangeKind = property(get_ChangeKind, None)
    ShippingAddress = property(get_ShippingAddress, None)
    SelectedShippingOption = property(get_SelectedShippingOption, None)
class PaymentRequestChangedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('5078b9e1-f398-4f2c-a2-7e-94-d3-71-cf-6c-7d')
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestChangedHandler'
    @winrt_commethod(3)
    def Invoke(self, paymentRequest: Windows.ApplicationModel.Payments.PaymentRequest, args: Windows.ApplicationModel.Payments.PaymentRequestChangedArgs) -> Void: ...
class PaymentRequestChangedResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestChangedResult'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentRequestChangedResultFactory, changeAcceptedByMerchant: Boolean) -> Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_factorymethod
    def CreateWithPaymentDetails(cls: Windows.ApplicationModel.Payments.IPaymentRequestChangedResultFactory, changeAcceptedByMerchant: Boolean, updatedPaymentDetails: Windows.ApplicationModel.Payments.PaymentDetails) -> Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_mixinmethod
    def get_ChangeAcceptedByMerchant(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> Boolean: ...
    @winrt_mixinmethod
    def put_ChangeAcceptedByMerchant(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UpdatedPaymentDetails(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def put_UpdatedPaymentDetails(self: Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: Windows.ApplicationModel.Payments.PaymentDetails) -> Void: ...
    ChangeAcceptedByMerchant = property(get_ChangeAcceptedByMerchant, put_ChangeAcceptedByMerchant)
    Message = property(get_Message, put_Message)
    UpdatedPaymentDetails = property(get_UpdatedPaymentDetails, put_UpdatedPaymentDetails)
PaymentRequestCompletionStatus = Int32
PaymentRequestCompletionStatus_Succeeded: PaymentRequestCompletionStatus = 0
PaymentRequestCompletionStatus_Failed: PaymentRequestCompletionStatus = 1
PaymentRequestCompletionStatus_Unknown: PaymentRequestCompletionStatus = 2
PaymentRequestStatus = Int32
PaymentRequestStatus_Succeeded: PaymentRequestStatus = 0
PaymentRequestStatus_Failed: PaymentRequestStatus = 1
PaymentRequestStatus_Canceled: PaymentRequestStatus = 2
class PaymentRequestSubmitResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestSubmitResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult) -> Windows.ApplicationModel.Payments.PaymentRequestStatus: ...
    @winrt_mixinmethod
    def get_Response(self: Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult) -> Windows.ApplicationModel.Payments.PaymentResponse: ...
    Status = property(get_Status, None)
    Response = property(get_Response, None)
class PaymentResponse(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentResponse'
    @winrt_mixinmethod
    def get_PaymentToken(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_mixinmethod
    def get_ShippingOption(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def get_ShippingAddress(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_PayerEmail(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PayerName(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PayerPhoneNumber(self: Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def CompleteAsync(self: Windows.ApplicationModel.Payments.IPaymentResponse, status: Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus) -> Windows.Foundation.IAsyncAction: ...
    PaymentToken = property(get_PaymentToken, None)
    ShippingOption = property(get_ShippingOption, None)
    ShippingAddress = property(get_ShippingAddress, None)
    PayerEmail = property(get_PayerEmail, None)
    PayerName = property(get_PayerName, None)
    PayerPhoneNumber = property(get_PayerPhoneNumber, None)
class PaymentShippingOption(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentShippingOption'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_factorymethod
    def CreateWithSelected(cls: Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_factorymethod
    def CreateWithSelectedAndTag(cls: Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean, tag: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.ApplicationModel.Payments.IPaymentShippingOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.ApplicationModel.Payments.IPaymentShippingOption, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Amount(self: Windows.ApplicationModel.Payments.IPaymentShippingOption) -> Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def put_Amount(self: Windows.ApplicationModel.Payments.IPaymentShippingOption, value: Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.ApplicationModel.Payments.IPaymentShippingOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.ApplicationModel.Payments.IPaymentShippingOption, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.ApplicationModel.Payments.IPaymentShippingOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: Windows.ApplicationModel.Payments.IPaymentShippingOption, value: Boolean) -> Void: ...
    Label = property(get_Label, put_Label)
    Amount = property(get_Amount, put_Amount)
    Tag = property(get_Tag, put_Tag)
    IsSelected = property(get_IsSelected, put_IsSelected)
PaymentShippingType = Int32
PaymentShippingType_Shipping: PaymentShippingType = 0
PaymentShippingType_Delivery: PaymentShippingType = 1
PaymentShippingType_Pickup: PaymentShippingType = 2
class PaymentToken(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentToken'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Payments.IPaymentTokenFactory, paymentMethodId: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_factorymethod
    def CreateWithJsonDetails(cls: Windows.ApplicationModel.Payments.IPaymentTokenFactory, paymentMethodId: WinRT_String, jsonDetails: WinRT_String) -> Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_mixinmethod
    def get_PaymentMethodId(self: Windows.ApplicationModel.Payments.IPaymentToken) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_JsonDetails(self: Windows.ApplicationModel.Payments.IPaymentToken) -> WinRT_String: ...
    PaymentMethodId = property(get_PaymentMethodId, None)
    JsonDetails = property(get_JsonDetails, None)
make_head(_module, 'IPaymentAddress')
make_head(_module, 'IPaymentCanMakePaymentResult')
make_head(_module, 'IPaymentCanMakePaymentResultFactory')
make_head(_module, 'IPaymentCurrencyAmount')
make_head(_module, 'IPaymentCurrencyAmountFactory')
make_head(_module, 'IPaymentDetails')
make_head(_module, 'IPaymentDetailsFactory')
make_head(_module, 'IPaymentDetailsModifier')
make_head(_module, 'IPaymentDetailsModifierFactory')
make_head(_module, 'IPaymentItem')
make_head(_module, 'IPaymentItemFactory')
make_head(_module, 'IPaymentMediator')
make_head(_module, 'IPaymentMediator2')
make_head(_module, 'IPaymentMerchantInfo')
make_head(_module, 'IPaymentMerchantInfoFactory')
make_head(_module, 'IPaymentMethodData')
make_head(_module, 'IPaymentMethodDataFactory')
make_head(_module, 'IPaymentOptions')
make_head(_module, 'IPaymentRequest')
make_head(_module, 'IPaymentRequest2')
make_head(_module, 'IPaymentRequestChangedArgs')
make_head(_module, 'IPaymentRequestChangedResult')
make_head(_module, 'IPaymentRequestChangedResultFactory')
make_head(_module, 'IPaymentRequestFactory')
make_head(_module, 'IPaymentRequestFactory2')
make_head(_module, 'IPaymentRequestSubmitResult')
make_head(_module, 'IPaymentResponse')
make_head(_module, 'IPaymentShippingOption')
make_head(_module, 'IPaymentShippingOptionFactory')
make_head(_module, 'IPaymentToken')
make_head(_module, 'IPaymentTokenFactory')
make_head(_module, 'PaymentAddress')
make_head(_module, 'PaymentCanMakePaymentResult')
make_head(_module, 'PaymentCurrencyAmount')
make_head(_module, 'PaymentDetails')
make_head(_module, 'PaymentDetailsModifier')
make_head(_module, 'PaymentItem')
make_head(_module, 'PaymentMediator')
make_head(_module, 'PaymentMerchantInfo')
make_head(_module, 'PaymentMethodData')
make_head(_module, 'PaymentOptions')
make_head(_module, 'PaymentRequest')
make_head(_module, 'PaymentRequestChangedArgs')
make_head(_module, 'PaymentRequestChangedHandler')
make_head(_module, 'PaymentRequestChangedResult')
make_head(_module, 'PaymentRequestSubmitResult')
make_head(_module, 'PaymentResponse')
make_head(_module, 'PaymentShippingOption')
make_head(_module, 'PaymentToken')
