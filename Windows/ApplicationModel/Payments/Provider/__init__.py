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
import Windows.ApplicationModel.Payments.Provider
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
class IPaymentAppCanMakePaymentTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails'
    _iid_ = Guid('{0ce201f0-8b93-4eb6-8c46-2e4a6c6a26f6}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_commethod(7)
    def ReportCanMakePaymentResult(self, value: Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult) -> Void: ...
    Request = property(get_Request, None)
class IPaymentAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppManager'
    _iid_ = Guid('{0e47aa53-8521-4969-a957-df2538a3a98f}')
    @winrt_commethod(6)
    def RegisterAsync(self, supportedPaymentMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def UnregisterAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IPaymentAppManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentAppManagerStatics'
    _iid_ = Guid('{a341ac28-fc89-4406-b4d9-34e7fe79dfb6}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.ApplicationModel.Payments.Provider.PaymentAppManager: ...
    Current = property(get_Current, None)
class IPaymentTransaction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransaction'
    _iid_ = Guid('{62581da0-26a5-4e9b-a6eb-66606cf001d3}')
    @winrt_commethod(6)
    def get_PaymentRequest(self) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
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
    def UpdateShippingAddressAsync(self, shippingAddress: Windows.ApplicationModel.Payments.PaymentAddress) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_commethod(14)
    def UpdateSelectedShippingOptionAsync(self, selectedShippingOption: Windows.ApplicationModel.Payments.PaymentShippingOption) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_commethod(15)
    def AcceptAsync(self, paymentToken: Windows.ApplicationModel.Payments.PaymentToken) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult]: ...
    @winrt_commethod(16)
    def Reject(self) -> Void: ...
    PaymentRequest = property(get_PaymentRequest, None)
    PayerEmail = property(get_PayerEmail, put_PayerEmail)
    PayerName = property(get_PayerName, put_PayerName)
    PayerPhoneNumber = property(get_PayerPhoneNumber, put_PayerPhoneNumber)
class IPaymentTransactionAcceptResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult'
    _iid_ = Guid('{060e3276-d30c-4817-95a2-df7ae9273b56}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus: ...
    Status = property(get_Status, None)
class IPaymentTransactionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.IPaymentTransactionStatics'
    _iid_ = Guid('{8d639750-ee0a-4df5-9b1e-1c0f9ec59881}')
    @winrt_commethod(6)
    def FromIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.Provider.PaymentTransaction]: ...
class PaymentAppCanMakePaymentTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentAppCanMakePaymentTriggerDetails'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def ReportCanMakePaymentResult(self: Windows.ApplicationModel.Payments.Provider.IPaymentAppCanMakePaymentTriggerDetails, value: Windows.ApplicationModel.Payments.PaymentCanMakePaymentResult) -> Void: ...
    Request = property(get_Request, None)
class PaymentAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Payments.Provider.IPaymentAppManager
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentAppManager'
    @winrt_mixinmethod
    def RegisterAsync(self: Windows.ApplicationModel.Payments.Provider.IPaymentAppManager, supportedPaymentMethodIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnregisterAsync(self: Windows.ApplicationModel.Payments.Provider.IPaymentAppManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_Current(cls: Windows.ApplicationModel.Payments.Provider.IPaymentAppManagerStatics) -> Windows.ApplicationModel.Payments.Provider.PaymentAppManager: ...
    Current = property(get_Current, None)
class PaymentTransaction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentTransaction'
    @winrt_mixinmethod
    def get_PaymentRequest(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> Windows.ApplicationModel.Payments.PaymentRequest: ...
    @winrt_mixinmethod
    def get_PayerEmail(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerEmail(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PayerName(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerName(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PayerPhoneNumber(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PayerPhoneNumber(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def UpdateShippingAddressAsync(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, shippingAddress: Windows.ApplicationModel.Payments.PaymentAddress) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_mixinmethod
    def UpdateSelectedShippingOptionAsync(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, selectedShippingOption: Windows.ApplicationModel.Payments.PaymentShippingOption) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.PaymentRequestChangedResult]: ...
    @winrt_mixinmethod
    def AcceptAsync(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction, paymentToken: Windows.ApplicationModel.Payments.PaymentToken) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult]: ...
    @winrt_mixinmethod
    def Reject(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransaction) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.ApplicationModel.Payments.Provider.IPaymentTransactionStatics, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Payments.Provider.PaymentTransaction]: ...
    PaymentRequest = property(get_PaymentRequest, None)
    PayerEmail = property(get_PayerEmail, put_PayerEmail)
    PayerName = property(get_PayerName, put_PayerName)
    PayerPhoneNumber = property(get_PayerPhoneNumber, put_PayerPhoneNumber)
class PaymentTransactionAcceptResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult
    _classid_ = 'Windows.ApplicationModel.Payments.Provider.PaymentTransactionAcceptResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.Payments.Provider.IPaymentTransactionAcceptResult) -> Windows.ApplicationModel.Payments.PaymentRequestCompletionStatus: ...
    Status = property(get_Status, None)
make_head(_module, 'IPaymentAppCanMakePaymentTriggerDetails')
make_head(_module, 'IPaymentAppManager')
make_head(_module, 'IPaymentAppManagerStatics')
make_head(_module, 'IPaymentTransaction')
make_head(_module, 'IPaymentTransactionAcceptResult')
make_head(_module, 'IPaymentTransactionStatics')
make_head(_module, 'PaymentAppCanMakePaymentTriggerDetails')
make_head(_module, 'PaymentAppManager')
make_head(_module, 'PaymentTransaction')
make_head(_module, 'PaymentTransactionAcceptResult')
