from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Payments
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class IPaymentAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentAddress'
    _iid_ = Guid('{5f2264e9-6f3a-4166-a018-0a0b06bb32b5}')
    @winrt_commethod(6)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Country(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AddressLines(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def put_AddressLines(self, value: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
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
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    AddressLines = property(get_AddressLines, put_AddressLines)
    City = property(get_City, put_City)
    Country = property(get_Country, put_Country)
    DependentLocality = property(get_DependentLocality, put_DependentLocality)
    LanguageCode = property(get_LanguageCode, put_LanguageCode)
    Organization = property(get_Organization, put_Organization)
    PhoneNumber = property(get_PhoneNumber, put_PhoneNumber)
    PostalCode = property(get_PostalCode, put_PostalCode)
    Properties = property(get_Properties, None)
    Recipient = property(get_Recipient, put_Recipient)
    Region = property(get_Region, put_Region)
    SortingCode = property(get_SortingCode, put_SortingCode)
class IPaymentCanMakePaymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResult'
    _iid_ = Guid('{7696fe55-d5d3-4d3d-b345-45591759c510}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus: ...
    Status = property(get_Status, None)
class IPaymentCanMakePaymentResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResultFactory'
    _iid_ = Guid('{bbdcaa3e-7d49-4f69-aa53-2a0f8164b7c9}')
    @winrt_commethod(6)
    def Create(self, value: win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus) -> win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult: ...
class IPaymentCurrencyAmount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentCurrencyAmount'
    _iid_ = Guid('{e3a3e9e0-b41f-4987-bdcb-071331f2daa4}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentCurrencyAmountFactory'
    _iid_ = Guid('{3257d338-140c-4575-8535-f773178c09a7}')
    @winrt_commethod(6)
    def Create(self, value: WinRT_String, currency: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(7)
    def CreateWithCurrencySystem(self, value: WinRT_String, currency: WinRT_String, currencySystem: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
class IPaymentDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentDetails'
    _iid_ = Guid('{53bb2d7d-e0eb-4053-8eae-ce7c48e02945}')
    @winrt_commethod(6)
    def get_Total(self) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_commethod(7)
    def put_Total(self, value: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]: ...
    @winrt_commethod(9)
    def put_DisplayItems(self, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> Void: ...
    @winrt_commethod(10)
    def get_ShippingOptions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentShippingOption]: ...
    @winrt_commethod(11)
    def put_ShippingOptions(self, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentShippingOption]) -> Void: ...
    @winrt_commethod(12)
    def get_Modifiers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier]: ...
    @winrt_commethod(13)
    def put_Modifiers(self, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier]) -> Void: ...
    DisplayItems = property(get_DisplayItems, put_DisplayItems)
    Modifiers = property(get_Modifiers, put_Modifiers)
    ShippingOptions = property(get_ShippingOptions, put_ShippingOptions)
    Total = property(get_Total, put_Total)
class IPaymentDetailsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentDetailsFactory'
    _iid_ = Guid('{cfe8afee-c0ea-4ca1-8bc7-6de67b1f3763}')
    @winrt_commethod(6)
    def Create(self, total: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(7)
    def CreateWithDisplayItems(self, total: win32more.Windows.ApplicationModel.Payments.PaymentItem, displayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
class IPaymentDetailsModifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentDetailsModifier'
    _iid_ = Guid('{be1c7d65-4323-41d7-b305-dfcb765f69de}')
    @winrt_commethod(6)
    def get_JsonData(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedMethodIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Total(self) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_commethod(9)
    def get_AdditionalDisplayItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]: ...
    AdditionalDisplayItems = property(get_AdditionalDisplayItems, None)
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    Total = property(get_Total, None)
class IPaymentDetailsModifierFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory'
    _iid_ = Guid('{79005286-54de-429c-9e4f-5dce6e10ebce}')
    @winrt_commethod(6)
    def Create(self, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_commethod(7)
    def CreateWithAdditionalDisplayItems(self, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_commethod(8)
    def CreateWithAdditionalDisplayItemsAndJsonData(self, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem], jsonData: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
class IPaymentItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentItem'
    _iid_ = Guid('{685ac88b-79b2-4b76-9e03-a876223dfe72}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Amount(self) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(9)
    def put_Amount(self, value: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_commethod(10)
    def get_Pending(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Pending(self, value: Boolean) -> Void: ...
    Amount = property(get_Amount, put_Amount)
    Label = property(get_Label, put_Label)
    Pending = property(get_Pending, put_Pending)
class IPaymentItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentItemFactory'
    _iid_ = Guid('{c6ab7ad8-2503-4d1d-a778-02b2e5927b2c}')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
class IPaymentMediator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMediator'
    _iid_ = Guid('{fb0ee829-ec0c-449a-83da-7ae3073365a2}')
    @winrt_commethod(6)
    def GetSupportedMethodIdsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(7)
    def SubmitPaymentRequestAsync(self, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_commethod(8)
    def SubmitPaymentRequestWithChangeHandlerAsync(self, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest, changeHandler: win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
class IPaymentMediator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMediator2'
    _iid_ = Guid('{ceef98f1-e407-4128-8e73-d93d5f822786}')
    @winrt_commethod(6)
    def CanMakePaymentAsync(self, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult]: ...
class IPaymentMerchantInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMerchantInfo'
    _iid_ = Guid('{63445050-0e94-4ed6-aacb-e6012bd327a7}')
    @winrt_commethod(6)
    def get_PackageFullName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    PackageFullName = property(get_PackageFullName, None)
    Uri = property(get_Uri, None)
class IPaymentMerchantInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMerchantInfoFactory'
    _iid_ = Guid('{9e89ced3-ccb7-4167-a8ec-e10ae96dbcd1}')
    @winrt_commethod(6)
    def Create(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
class IPaymentMethodData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMethodData'
    _iid_ = Guid('{d1d3caf4-de98-4129-b1b7-c3ad86237bf4}')
    @winrt_commethod(6)
    def get_SupportedMethodIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_JsonData(self) -> WinRT_String: ...
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
class IPaymentMethodDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentMethodDataFactory'
    _iid_ = Guid('{8addd27f-9baa-4a82-8342-a8210992a36b}')
    @winrt_commethod(6)
    def Create(self, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_commethod(7)
    def CreateWithJsonData(self, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], jsonData: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentMethodData: ...
class IPaymentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentOptions'
    _iid_ = Guid('{aaa30854-1f2b-4365-8251-01b58915a5bc}')
    @winrt_commethod(6)
    def get_RequestPayerEmail(self) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(7)
    def put_RequestPayerEmail(self, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(8)
    def get_RequestPayerName(self) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(9)
    def put_RequestPayerName(self, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(10)
    def get_RequestPayerPhoneNumber(self) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_commethod(11)
    def put_RequestPayerPhoneNumber(self, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_commethod(12)
    def get_RequestShipping(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_RequestShipping(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ShippingType(self) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingType: ...
    @winrt_commethod(15)
    def put_ShippingType(self, value: win32more.Windows.ApplicationModel.Payments.PaymentShippingType) -> Void: ...
    RequestPayerEmail = property(get_RequestPayerEmail, put_RequestPayerEmail)
    RequestPayerName = property(get_RequestPayerName, put_RequestPayerName)
    RequestPayerPhoneNumber = property(get_RequestPayerPhoneNumber, put_RequestPayerPhoneNumber)
    RequestShipping = property(get_RequestShipping, put_RequestShipping)
    ShippingType = property(get_ShippingType, put_ShippingType)
class IPaymentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequest'
    _iid_ = Guid('{b74942e1-ed7b-47eb-bc08-78cc5d6896b6}')
    @winrt_commethod(6)
    def get_MerchantInfo(self) -> win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_commethod(7)
    def get_Details(self) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(8)
    def get_MethodData(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentMethodData]: ...
    @winrt_commethod(9)
    def get_Options(self) -> win32more.Windows.ApplicationModel.Payments.PaymentOptions: ...
    Details = property(get_Details, None)
    MerchantInfo = property(get_MerchantInfo, None)
    MethodData = property(get_MethodData, None)
    Options = property(get_Options, None)
class IPaymentRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequest2'
    _iid_ = Guid('{b63ccfb5-5998-493e-a04c-67048a50f141}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IPaymentRequestChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs'
    _iid_ = Guid('{c6145e44-cd8b-4be4-b555-27c99194c0c5}')
    @winrt_commethod(6)
    def get_ChangeKind(self) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangeKind: ...
    @winrt_commethod(7)
    def get_ShippingAddress(self) -> win32more.Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_commethod(8)
    def get_SelectedShippingOption(self) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(9)
    def Acknowledge(self, changeResult: win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult) -> Void: ...
    ChangeKind = property(get_ChangeKind, None)
    SelectedShippingOption = property(get_SelectedShippingOption, None)
    ShippingAddress = property(get_ShippingAddress, None)
class IPaymentRequestChangedResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestChangedResult'
    _iid_ = Guid('{df699e5c-16c4-47ad-9401-8440ec0757db}')
    @winrt_commethod(6)
    def get_ChangeAcceptedByMerchant(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ChangeAcceptedByMerchant(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_UpdatedPaymentDetails(self) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_commethod(11)
    def put_UpdatedPaymentDetails(self, value: win32more.Windows.ApplicationModel.Payments.PaymentDetails) -> Void: ...
    ChangeAcceptedByMerchant = property(get_ChangeAcceptedByMerchant, put_ChangeAcceptedByMerchant)
    Message = property(get_Message, put_Message)
    UpdatedPaymentDetails = property(get_UpdatedPaymentDetails, put_UpdatedPaymentDetails)
class IPaymentRequestChangedResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestChangedResultFactory'
    _iid_ = Guid('{08740f56-1d33-4431-814b-67ea24bf21db}')
    @winrt_commethod(6)
    def Create(self, changeAcceptedByMerchant: Boolean) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_commethod(7)
    def CreateWithPaymentDetails(self, changeAcceptedByMerchant: Boolean, updatedPaymentDetails: win32more.Windows.ApplicationModel.Payments.PaymentDetails) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
class IPaymentRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestFactory'
    _iid_ = Guid('{3e8a79dc-6b74-42d3-b103-f0de35fb1848}')
    @winrt_commethod(6)
    def Create(self, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData]) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(7)
    def CreateWithMerchantInfo(self, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(8)
    def CreateWithMerchantInfoAndOptions(self, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: win32more.Windows.ApplicationModel.Payments.PaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
class IPaymentRequestFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestFactory2'
    _iid_ = Guid('{e6ce1325-a506-4372-b7ef-1a031d5662d1}')
    @winrt_commethod(6)
    def CreateWithMerchantInfoOptionsAndId(self, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: win32more.Windows.ApplicationModel.Payments.PaymentOptions, id: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
class IPaymentRequestSubmitResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult'
    _iid_ = Guid('{7b9c3912-30f2-4e90-b249-8ce7d78ffe56}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestStatus: ...
    @winrt_commethod(7)
    def get_Response(self) -> win32more.Windows.ApplicationModel.Payments.PaymentResponse: ...
    Response = property(get_Response, None)
    Status = property(get_Status, None)
class IPaymentResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentResponse'
    _iid_ = Guid('{e1389457-8bd2-4888-9fa8-97985545108e}')
    @winrt_commethod(6)
    def get_PaymentToken(self) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_commethod(7)
    def get_ShippingOption(self) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(8)
    def get_ShippingAddress(self) -> win32more.Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_commethod(9)
    def get_PayerEmail(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_PayerName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PayerPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def CompleteAsync(self, status: win32more.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    PayerEmail = property(get_PayerEmail, None)
    PayerName = property(get_PayerName, None)
    PayerPhoneNumber = property(get_PayerPhoneNumber, None)
    PaymentToken = property(get_PaymentToken, None)
    ShippingAddress = property(get_ShippingAddress, None)
    ShippingOption = property(get_ShippingOption, None)
class IPaymentShippingOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentShippingOption'
    _iid_ = Guid('{13372ada-9753-4574-8966-93145a76c7f9}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Amount(self) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_commethod(9)
    def put_Amount(self, value: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    Amount = property(get_Amount, put_Amount)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Label = property(get_Label, put_Label)
    Tag = property(get_Tag, put_Tag)
class IPaymentShippingOptionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory'
    _iid_ = Guid('{5de5f917-b2d7-446b-9d73-6123fbca3bc6}')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(7)
    def CreateWithSelected(self, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_commethod(8)
    def CreateWithSelectedAndTag(self, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean, tag: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
class IPaymentToken(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentToken'
    _iid_ = Guid('{bbcac013-ccd0-41f2-b2a1-0a2e4b5dce25}')
    @winrt_commethod(6)
    def get_PaymentMethodId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_JsonDetails(self) -> WinRT_String: ...
    JsonDetails = property(get_JsonDetails, None)
    PaymentMethodId = property(get_PaymentMethodId, None)
class IPaymentTokenFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.IPaymentTokenFactory'
    _iid_ = Guid('{988cd7aa-4753-4904-8373-dd7b08b995c1}')
    @winrt_commethod(6)
    def Create(self, paymentMethodId: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_commethod(7)
    def CreateWithJsonDetails(self, paymentMethodId: WinRT_String, jsonDetails: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
class PaymentAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentAddress
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentAddress'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentAddress.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Country(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AddressLines(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def put_AddressLines(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_City(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_City(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DependentLocality(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DependentLocality(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PostalCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PostalCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SortingCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SortingCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LanguageCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LanguageCode(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Organization(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Organization(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Recipient(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Recipient(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PhoneNumber(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.ApplicationModel.Payments.IPaymentAddress) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    AddressLines = property(get_AddressLines, put_AddressLines)
    City = property(get_City, put_City)
    Country = property(get_Country, put_Country)
    DependentLocality = property(get_DependentLocality, put_DependentLocality)
    LanguageCode = property(get_LanguageCode, put_LanguageCode)
    Organization = property(get_Organization, put_Organization)
    PhoneNumber = property(get_PhoneNumber, put_PhoneNumber)
    PostalCode = property(get_PostalCode, put_PostalCode)
    Properties = property(get_Properties, None)
    Recipient = property(get_Recipient, put_Recipient)
    Region = property(get_Region, put_Region)
    SortingCode = property(get_SortingCode, put_SortingCode)
class PaymentCanMakePaymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResult
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResultFactory, value: win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus) -> win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Payments.IPaymentCanMakePaymentResult) -> win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResultStatus: ...
    Status = property(get_Status, None)
class PaymentCanMakePaymentResultStatus(Enum, Int32):
    Unknown = 0
    Yes = 1
    No = 2
    NotAllowed = 3
    UserNotSignedIn = 4
    SpecifiedPaymentMethodIdsNotSupported = 5
    NoQualifyingCardOnFile = 6
class PaymentCurrencyAmount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentCurrencyAmount'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount.CreateWithCurrencySystem(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmountFactory, value: WinRT_String, currency: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_factorymethod
    def CreateWithCurrencySystem(cls: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmountFactory, value: WinRT_String, currency: WinRT_String, currencySystem: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def get_Currency(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Currency(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CurrencySystem(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CurrencySystem(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.ApplicationModel.Payments.IPaymentCurrencyAmount, value: WinRT_String) -> Void: ...
    Currency = property(get_Currency, put_Currency)
    CurrencySystem = property(get_CurrencySystem, put_CurrencySystem)
    Value = property(get_Value, put_Value)
class PaymentDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentDetails
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentDetails'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetails.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetails.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetails.CreateWithDisplayItems(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsFactory, total: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_factorymethod
    def CreateWithDisplayItems(cls: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsFactory, total: win32more.Windows.ApplicationModel.Payments.PaymentItem, displayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def get_Total(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def put_Total(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails, value: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayItems(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]: ...
    @winrt_mixinmethod
    def put_DisplayItems(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> Void: ...
    @winrt_mixinmethod
    def get_ShippingOptions(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentShippingOption]: ...
    @winrt_mixinmethod
    def put_ShippingOptions(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentShippingOption]) -> Void: ...
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier]: ...
    @winrt_mixinmethod
    def put_Modifiers(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetails, value: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier]) -> Void: ...
    DisplayItems = property(get_DisplayItems, put_DisplayItems)
    Modifiers = property(get_Modifiers, put_Modifiers)
    ShippingOptions = property(get_ShippingOptions, put_ShippingOptions)
    Total = property(get_Total, put_Total)
class PaymentDetailsModifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifier
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentDetailsModifier'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier.CreateWithAdditionalDisplayItems(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier.CreateWithAdditionalDisplayItemsAndJsonData(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_factorymethod
    def CreateWithAdditionalDisplayItems(cls: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem]) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_factorymethod
    def CreateWithAdditionalDisplayItemsAndJsonData(cls: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifierFactory, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], total: win32more.Windows.ApplicationModel.Payments.PaymentItem, additionalDisplayItems: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentItem], jsonData: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentDetailsModifier: ...
    @winrt_mixinmethod
    def get_JsonData(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedMethodIds(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Total(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def get_AdditionalDisplayItems(self: win32more.Windows.ApplicationModel.Payments.IPaymentDetailsModifier) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentItem]: ...
    AdditionalDisplayItems = property(get_AdditionalDisplayItems, None)
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
    Total = property(get_Total, None)
class PaymentItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentItem
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentItem.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentItemFactory, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> win32more.Windows.ApplicationModel.Payments.PaymentItem: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Amount(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def put_Amount(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem, value: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_mixinmethod
    def get_Pending(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_Pending(self: win32more.Windows.ApplicationModel.Payments.IPaymentItem, value: Boolean) -> Void: ...
    Amount = property(get_Amount, put_Amount)
    Label = property(get_Label, put_Label)
    Pending = property(get_Pending, put_Pending)
class PaymentMediator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentMediator
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMediator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentMediator.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Payments.PaymentMediator: ...
    @winrt_mixinmethod
    def GetSupportedMethodIdsAsync(self: win32more.Windows.ApplicationModel.Payments.IPaymentMediator) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def SubmitPaymentRequestAsync(self: win32more.Windows.ApplicationModel.Payments.IPaymentMediator, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_mixinmethod
    def SubmitPaymentRequestWithChangeHandlerAsync(self: win32more.Windows.ApplicationModel.Payments.IPaymentMediator, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest, changeHandler: win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedHandler) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestSubmitResult]: ...
    @winrt_mixinmethod
    def CanMakePaymentAsync(self: win32more.Windows.ApplicationModel.Payments.IPaymentMediator2, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult]: ...
class PaymentMerchantInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentMerchantInfo
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMerchantInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentMerchantInfoFactory, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_mixinmethod
    def get_PackageFullName(self: win32more.Windows.ApplicationModel.Payments.IPaymentMerchantInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Payments.IPaymentMerchantInfo) -> win32more.Windows.Foundation.Uri: ...
    PackageFullName = property(get_PackageFullName, None)
    Uri = property(get_Uri, None)
class PaymentMethodData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentMethodData
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentMethodData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentMethodData.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentMethodData.CreateWithJsonData(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentMethodDataFactory, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_factorymethod
    def CreateWithJsonData(cls: win32more.Windows.ApplicationModel.Payments.IPaymentMethodDataFactory, supportedMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], jsonData: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentMethodData: ...
    @winrt_mixinmethod
    def get_SupportedMethodIds(self: win32more.Windows.ApplicationModel.Payments.IPaymentMethodData) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_JsonData(self: win32more.Windows.ApplicationModel.Payments.IPaymentMethodData) -> WinRT_String: ...
    JsonData = property(get_JsonData, None)
    SupportedMethodIds = property(get_SupportedMethodIds, None)
class PaymentOptionPresence(Enum, Int32):
    None_ = 0
    Optional = 1
    Required = 2
class PaymentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentOptions
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Payments.PaymentOptions: ...
    @winrt_mixinmethod
    def get_RequestPayerEmail(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerEmail(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestPayerName(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerName(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestPayerPhoneNumber(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence: ...
    @winrt_mixinmethod
    def put_RequestPayerPhoneNumber(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions, value: win32more.Windows.ApplicationModel.Payments.PaymentOptionPresence) -> Void: ...
    @winrt_mixinmethod
    def get_RequestShipping(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequestShipping(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShippingType(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingType: ...
    @winrt_mixinmethod
    def put_ShippingType(self: win32more.Windows.ApplicationModel.Payments.IPaymentOptions, value: win32more.Windows.ApplicationModel.Payments.PaymentShippingType) -> Void: ...
    RequestPayerEmail = property(get_RequestPayerEmail, put_RequestPayerEmail)
    RequestPayerName = property(get_RequestPayerName, put_RequestPayerName)
    RequestPayerPhoneNumber = property(get_RequestPayerPhoneNumber, put_RequestPayerPhoneNumber)
    RequestShipping = property(get_RequestShipping, put_RequestShipping)
    ShippingType = property(get_ShippingType, put_ShippingType)
class PaymentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentRequest
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequest.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequest.CreateWithMerchantInfo(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequest.CreateWithMerchantInfoAndOptions(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequest.CreateWithMerchantInfoOptionsAndId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData]) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def CreateWithMerchantInfo(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def CreateWithMerchantInfoAndOptions(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestFactory, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: win32more.Windows.ApplicationModel.Payments.PaymentOptions) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_factorymethod
    def CreateWithMerchantInfoOptionsAndId(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestFactory2, details: win32more.Windows.ApplicationModel.Payments.PaymentDetails, methodData: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.Payments.PaymentMethodData], merchantInfo: win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo, options: win32more.Windows.ApplicationModel.Payments.PaymentOptions, id: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def get_MerchantInfo(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequest) -> win32more.Windows.ApplicationModel.Payments.PaymentMerchantInfo: ...
    @winrt_mixinmethod
    def get_Details(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequest) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def get_MethodData(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Payments.PaymentMethodData]: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequest) -> win32more.Windows.ApplicationModel.Payments.PaymentOptions: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequest2) -> WinRT_String: ...
    Details = property(get_Details, None)
    Id = property(get_Id, None)
    MerchantInfo = property(get_MerchantInfo, None)
    MethodData = property(get_MethodData, None)
    Options = property(get_Options, None)
class PaymentRequestChangeKind(Enum, Int32):
    ShippingOption = 0
    ShippingAddress = 1
class PaymentRequestChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestChangedArgs'
    @winrt_mixinmethod
    def get_ChangeKind(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangeKind: ...
    @winrt_mixinmethod
    def get_ShippingAddress(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> win32more.Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_SelectedShippingOption(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def Acknowledge(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedArgs, changeResult: win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult) -> Void: ...
    ChangeKind = property(get_ChangeKind, None)
    SelectedShippingOption = property(get_SelectedShippingOption, None)
    ShippingAddress = property(get_ShippingAddress, None)
class PaymentRequestChangedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5078b9e1-f398-4f2c-a27e-94d371cf6c7d}')
    @winrt_commethod(3)
    def Invoke(self, paymentRequest: win32more.Windows.ApplicationModel.Payments.PaymentRequest, args: win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedArgs) -> Void: ...
class PaymentRequestChangedResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestChangedResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult.CreateWithPaymentDetails(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResultFactory, changeAcceptedByMerchant: Boolean) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_factorymethod
    def CreateWithPaymentDetails(cls: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResultFactory, changeAcceptedByMerchant: Boolean, updatedPaymentDetails: win32more.Windows.ApplicationModel.Payments.PaymentDetails) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult: ...
    @winrt_mixinmethod
    def get_ChangeAcceptedByMerchant(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> Boolean: ...
    @winrt_mixinmethod
    def put_ChangeAcceptedByMerchant(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UpdatedPaymentDetails(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult) -> win32more.Windows.ApplicationModel.Payments.PaymentDetails: ...
    @winrt_mixinmethod
    def put_UpdatedPaymentDetails(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestChangedResult, value: win32more.Windows.ApplicationModel.Payments.PaymentDetails) -> Void: ...
    ChangeAcceptedByMerchant = property(get_ChangeAcceptedByMerchant, put_ChangeAcceptedByMerchant)
    Message = property(get_Message, put_Message)
    UpdatedPaymentDetails = property(get_UpdatedPaymentDetails, put_UpdatedPaymentDetails)
class PaymentRequestCompletionStatus(Enum, Int32):
    Succeeded = 0
    Failed = 1
    Unknown = 2
class PaymentRequestStatus(Enum, Int32):
    Succeeded = 0
    Failed = 1
    Canceled = 2
class PaymentRequestSubmitResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentRequestSubmitResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestStatus: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.ApplicationModel.Payments.IPaymentRequestSubmitResult) -> win32more.Windows.ApplicationModel.Payments.PaymentResponse: ...
    Response = property(get_Response, None)
    Status = property(get_Status, None)
class PaymentResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentResponse
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentResponse'
    @winrt_mixinmethod
    def get_PaymentToken(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_mixinmethod
    def get_ShippingOption(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def get_ShippingAddress(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> win32more.Windows.ApplicationModel.Payments.PaymentAddress: ...
    @winrt_mixinmethod
    def get_PayerEmail(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PayerName(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PayerPhoneNumber(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def CompleteAsync(self: win32more.Windows.ApplicationModel.Payments.IPaymentResponse, status: win32more.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    PayerEmail = property(get_PayerEmail, None)
    PayerName = property(get_PayerName, None)
    PayerPhoneNumber = property(get_PayerPhoneNumber, None)
    PaymentToken = property(get_PaymentToken, None)
    ShippingAddress = property(get_ShippingAddress, None)
    ShippingOption = property(get_ShippingOption, None)
class PaymentShippingOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentShippingOption'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentShippingOption.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentShippingOption.CreateWithSelected(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentShippingOption.CreateWithSelectedAndTag(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_factorymethod
    def CreateWithSelected(cls: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_factorymethod
    def CreateWithSelectedAndTag(cls: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOptionFactory, label: WinRT_String, amount: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount, selected: Boolean, tag: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentShippingOption: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Amount(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption) -> win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount: ...
    @winrt_mixinmethod
    def put_Amount(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption, value: win32more.Windows.ApplicationModel.Payments.PaymentCurrencyAmount) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: win32more.Windows.ApplicationModel.Payments.IPaymentShippingOption, value: Boolean) -> Void: ...
    Amount = property(get_Amount, put_Amount)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Label = property(get_Label, put_Label)
    Tag = property(get_Tag, put_Tag)
class PaymentShippingType(Enum, Int32):
    Shipping = 0
    Delivery = 1
    Pickup = 2
class PaymentToken(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.IPaymentToken
    _classid_ = 'Windows.ApplicationModel.Payments.PaymentToken'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentToken.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Payments.PaymentToken.CreateWithJsonDetails(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Payments.IPaymentTokenFactory, paymentMethodId: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_factorymethod
    def CreateWithJsonDetails(cls: win32more.Windows.ApplicationModel.Payments.IPaymentTokenFactory, paymentMethodId: WinRT_String, jsonDetails: WinRT_String) -> win32more.Windows.ApplicationModel.Payments.PaymentToken: ...
    @winrt_mixinmethod
    def get_PaymentMethodId(self: win32more.Windows.ApplicationModel.Payments.IPaymentToken) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_JsonDetails(self: win32more.Windows.ApplicationModel.Payments.IPaymentToken) -> WinRT_String: ...
    JsonDetails = property(get_JsonDetails, None)
    PaymentMethodId = property(get_PaymentMethodId, None)


make_ready(__name__)
