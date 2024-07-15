from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Payments
import win32more.Windows.ApplicationModel.Payments.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IPaymentAppCanMakePaymentTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails'
    _iid_ = Guid('{0ce201f0-8b93-4eb6-8c46-2e4a6c6a26f6}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(7)
    def ReportCanMakePaymentResult(self, value: win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult) -> Void: ...
    Request = property(get_Request, None)
class IPaymentAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppManager'
    _iid_ = Guid('{0e47aa53-8521-4969-a957-df2538a3a98f}')
    @winrt_commethod(6)
    def RegisterAsync(self, supportedPaymentMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def UnregisterAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPaymentAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppManagerStatics'
    _iid_ = Guid('{a341ac28-fc89-4406-b4d9-34e7fe79dfb6}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.ApplicationModel.Payments.Provider.PaymentAppManager: ...
    Current = property(get_Current, None)
class IPaymentTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransaction'
    _iid_ = Guid('{62581da0-26a5-4e9b-a6eb-66606cf001d3}')
    @winrt_commethod(6)
    def get_PaymentRequest(self) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(7)
    def get_PayerEmail(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_PayerEmail(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_PayerName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_PayerName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_PayerPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_PayerPhoneNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def UpdateShippingAddressAsync(self, shippingAddress: win32more.Windows.ApplicationModel.Payments.PaymentAddress) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_commethod(14)
    def UpdateSelectedShippingOptionAsync(self, selectedShippingOption: win32more.Windows.ApplicationModel.Payments.PaymentShippingOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_commethod(15)
    def AcceptAsync(self, paymentToken: win32more.Windows.ApplicationModel.Payments.PaymentToken) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult]: ...
    @winrt_commethod(16)
    def Reject(self) -> Void: ...
    PayerEmail = property(get_PayerEmail, put_PayerEmail)
    PayerName = property(get_PayerName, put_PayerName)
    PayerPhoneNumber = property(get_PayerPhoneNumber, put_PayerPhoneNumber)
    PaymentRequest = property(get_PaymentRequest, None)
class IPaymentTransactionAcceptResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult'
    _iid_ = Guid('{060e3276-d30c-4817-95a2-df7ae9273b56}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus: ...
    Status = property(get_Status, None)
class IPaymentTransactionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransactionStatics'
    _iid_ = Guid('{8d639750-ee0a-4df5-9b1e-1c0f9ec59881}')
    @winrt_commethod(6)
    def FromIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.Provider.PaymentTransaction]: ...
class PaymentAppCanMakePaymentTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentAppCanMakePaymentTriggerDetails'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def ReportCanMakePaymentResult(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails, value: win32more.Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult) -> Void: ...
    Request = property(get_Request, None)
class _PaymentAppManager_Meta_(ComPtr.__class__):
    pass
class PaymentAppManager(ComPtr, metaclass=_PaymentAppManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppManager
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentAppManager'
    @winrt_mixinmethod
    def RegisterAsync(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppManager, supportedPaymentMethodIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnregisterAsync(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentAppManagerStatics) -> win32more.Windows.ApplicationModel.Payments.Provider.PaymentAppManager: ...
    _PaymentAppManager_Meta_.Current = property(get_Current, None)
class PaymentTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentTransaction'
    @winrt_mixinmethod
    def get_PaymentRequest(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> win32more.Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def get_PayerEmail(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerEmail(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PayerName(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerName(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PayerPhoneNumber(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerPhoneNumber(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def UpdateShippingAddressAsync(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, shippingAddress: win32more.Windows.ApplicationModel.Payments.PaymentAddress) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_mixinmethod
    def UpdateSelectedShippingOptionAsync(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, selectedShippingOption: win32more.Windows.ApplicationModel.Payments.PaymentShippingOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_mixinmethod
    def AcceptAsync(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, paymentToken: win32more.Windows.ApplicationModel.Payments.PaymentToken) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult]: ...
    @winrt_mixinmethod
    def Reject(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransactionStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Payments.Provider.PaymentTransaction]: ...
    PayerEmail = property(get_PayerEmail, put_PayerEmail)
    PayerName = property(get_PayerName, put_PayerName)
    PayerPhoneNumber = property(get_PayerPhoneNumber, put_PayerPhoneNumber)
    PaymentRequest = property(get_PaymentRequest, None)
class PaymentTransactionAcceptResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult) -> win32more.Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus: ...
    Status = property(get_Status, None)


make_ready(__name__)
