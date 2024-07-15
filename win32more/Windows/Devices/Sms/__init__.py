from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Sms
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class CellularClass(Enum, Int32):
    None_ = 0
    Gsm = 1
    Cdma = 2
class DeleteSmsMessageOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.DeleteSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncAction, handler: win32more.Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncAction) -> win32more.Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class DeleteSmsMessagesOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.DeleteSmsMessagesOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncAction, handler: win32more.Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncAction) -> win32more.Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class GetSmsDeviceOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]
    _classid_ = 'Windows.Devices.Sms.GetSmsDeviceOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice], handler: win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Devices.Sms.SmsDevice]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]) -> win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Devices.Sms.SmsDevice]: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]) -> win32more.Windows.Devices.Sms.SmsDevice: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class GetSmsMessageOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage]
    _classid_ = 'Windows.Devices.Sms.GetSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage], handler: win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Devices.Sms.ISmsMessage]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage]) -> win32more.Windows.Foundation.AsyncOperationCompletedHandler[win32more.Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage]) -> win32more.Windows.Devices.Sms.ISmsMessage: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class GetSmsMessagesOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]
    _classid_ = 'Windows.Devices.Sms.GetSmsMessagesOperation'
    @winrt_mixinmethod
    def put_Progress(self: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32], handler: win32more.Windows.Foundation.AsyncOperationProgressHandler[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]) -> win32more.Windows.Foundation.AsyncOperationProgressHandler[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32], handler: win32more.Windows.Foundation.AsyncOperationWithProgressCompletedHandler[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]) -> win32more.Windows.Foundation.AsyncOperationWithProgressCompletedHandler[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Progress = property(get_Progress, put_Progress)
    Status = property(get_Status, None)
class ISmsAppMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsAppMessage'
    _iid_ = Guid('{e8bb8494-d3a0-4a0a-86d7-291033a8cf54}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_CallbackNumber(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CallbackNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IsDeliveryNotificationEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDeliveryNotificationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_RetryAttemptCount(self) -> Int32: ...
    @winrt_commethod(17)
    def put_RetryAttemptCount(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_Encoding(self) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(19)
    def put_Encoding(self, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(20)
    def get_PortNumber(self) -> Int32: ...
    @winrt_commethod(21)
    def put_PortNumber(self, value: Int32) -> Void: ...
    @winrt_commethod(22)
    def get_TeleserviceId(self) -> Int32: ...
    @winrt_commethod(23)
    def put_TeleserviceId(self, value: Int32) -> Void: ...
    @winrt_commethod(24)
    def get_ProtocolId(self) -> Int32: ...
    @winrt_commethod(25)
    def put_ProtocolId(self, value: Int32) -> Void: ...
    @winrt_commethod(26)
    def get_BinaryBody(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(27)
    def put_BinaryBody(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, None)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    PortNumber = property(get_PortNumber, put_PortNumber)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class ISmsBinaryMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsBinaryMessage'
    _iid_ = Guid('{5bf4e813-3b53-4c6e-b61a-d86a63755650}')
    @winrt_commethod(6)
    def get_Format(self) -> win32more.Windows.Devices.Sms.SmsDataFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: win32more.Windows.Devices.Sms.SmsDataFormat) -> Void: ...
    @winrt_commethod(8)
    def GetData(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(9)
    def SetData(self, value: PassArray[Byte]) -> Void: ...
    Format = property(get_Format, put_Format)
class ISmsBroadcastMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsBroadcastMessage'
    _iid_ = Guid('{75aebbf1-e4b7-4874-a09c-2956e592f957}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Channel(self) -> Int32: ...
    @winrt_commethod(10)
    def get_GeographicalScope(self) -> win32more.Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_commethod(11)
    def get_MessageCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_UpdateNumber(self) -> Int32: ...
    @winrt_commethod(13)
    def get_BroadcastType(self) -> win32more.Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_commethod(14)
    def get_IsEmergencyAlert(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsUserPopupRequested(self) -> Boolean: ...
    Body = property(get_Body, None)
    BroadcastType = property(get_BroadcastType, None)
    Channel = property(get_Channel, None)
    GeographicalScope = property(get_GeographicalScope, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
    MessageCode = property(get_MessageCode, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    UpdateNumber = property(get_UpdateNumber, None)
class ISmsDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDevice'
    _iid_ = Guid('{091791ed-872b-4eec-9c72-ab11627b34ec}')
    @winrt_commethod(6)
    def SendMessageAsync(self, message: win32more.Windows.Devices.Sms.ISmsMessage) -> win32more.Windows.Devices.Sms.SendSmsMessageOperation: ...
    @winrt_commethod(7)
    def CalculateLength(self, message: win32more.Windows.Devices.Sms.SmsTextMessage) -> win32more.Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_commethod(8)
    def get_AccountPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(10)
    def get_MessageStore(self) -> win32more.Windows.Devices.Sms.SmsDeviceMessageStore: ...
    @winrt_commethod(11)
    def get_DeviceStatus(self) -> win32more.Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_commethod(12)
    def add_SmsMessageReceived(self, eventHandler: win32more.Windows.Devices.Sms.SmsMessageReceivedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SmsMessageReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SmsDeviceStatusChanged(self, eventHandler: win32more.Windows.Devices.Sms.SmsDeviceStatusChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SmsDeviceStatusChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
    MessageStore = property(get_MessageStore, None)
    SmsMessageReceived = event()
    SmsDeviceStatusChanged = event()
class ISmsDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDevice2'
    _iid_ = Guid('{bd8a5c13-e522-46cb-b8d5-9ead30fb6c47}')
    @winrt_commethod(6)
    def get_SmscAddress(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SmscAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ParentDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AccountPhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(12)
    def get_DeviceStatus(self) -> win32more.Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_commethod(13)
    def CalculateLength(self, message: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_commethod(14)
    def SendMessageAndGetResultAsync(self, message: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_commethod(15)
    def add_DeviceStatusChanged(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sms.SmsDevice2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DeviceStatusChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    DeviceStatus = property(get_DeviceStatus, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceStatusChanged = event()
class ISmsDevice2Statics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDevice2Statics'
    _iid_ = Guid('{65c78325-1031-491e-8fb6-ef9991afe363}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(8)
    def GetDefault(self) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(9)
    def FromParentId(self, parentDeviceId: WinRT_String) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
class ISmsDeviceMessageStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDeviceMessageStore'
    _iid_ = Guid('{9889f253-f188-4427-8d54-ce0c2423c5c1}')
    @winrt_commethod(6)
    def DeleteMessageAsync(self, messageId: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def DeleteMessagesAsync(self, messageFilter: win32more.Windows.Devices.Sms.SmsMessageFilter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetMessageAsync(self, messageId: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_commethod(9)
    def GetMessagesAsync(self, messageFilter: win32more.Windows.Devices.Sms.SmsMessageFilter) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_commethod(10)
    def get_MaxMessages(self) -> UInt32: ...
    MaxMessages = property(get_MaxMessages, None)
class ISmsDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDeviceStatics'
    _iid_ = Guid('{f88d07ea-d815-4dd1-a234-4520ce4604a4}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
class ISmsDeviceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsDeviceStatics2'
    _iid_ = Guid('{2ca11c87-0873-4caf-8a7d-bd471e8586d1}')
    @winrt_commethod(6)
    def FromNetworkAccountIdAsync(self, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
class ISmsFilterRule(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsFilterRule'
    _iid_ = Guid('{40e32fae-b049-4fbc-afe9-e2a610eff55c}')
    @winrt_commethod(6)
    def get_MessageType(self) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_ImsiPrefixes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_DeviceIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_SenderNumbers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_TextMessagePrefixes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PortNumbers(self) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(12)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(13)
    def put_CellularClass(self, value: win32more.Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_commethod(14)
    def get_ProtocolIds(self) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(15)
    def get_TeleserviceIds(self) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(16)
    def get_WapApplicationIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(17)
    def get_WapContentTypes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(18)
    def get_BroadcastTypes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_commethod(19)
    def get_BroadcastChannels(self) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    BroadcastChannels = property(get_BroadcastChannels, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    DeviceIds = property(get_DeviceIds, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    MessageType = property(get_MessageType, None)
    PortNumbers = property(get_PortNumbers, None)
    ProtocolIds = property(get_ProtocolIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
class ISmsFilterRuleFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsFilterRuleFactory'
    _iid_ = Guid('{00c36508-6296-4f29-9aad-8920ceba3ce8}')
    @winrt_commethod(6)
    def CreateFilterRule(self, messageType: win32more.Windows.Devices.Sms.SmsMessageType) -> win32more.Windows.Devices.Sms.SmsFilterRule: ...
class ISmsFilterRules(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsFilterRules'
    _iid_ = Guid('{4e47eafb-79cd-4881-9894-55a4135b23fa}')
    @winrt_commethod(6)
    def get_ActionType(self) -> win32more.Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_commethod(7)
    def get_Rules(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
class ISmsFilterRulesFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsFilterRulesFactory'
    _iid_ = Guid('{a09924ed-6e2e-4530-9fde-465d02eed00e}')
    @winrt_commethod(6)
    def CreateFilterRules(self, actionType: win32more.Windows.Devices.Sms.SmsFilterActionType) -> win32more.Windows.Devices.Sms.SmsFilterRules: ...
class ISmsMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessage'
    _iid_ = Guid('{ed3c5e28-6984-4b07-811d-8d5906ed3cea}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MessageClass(self) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
class ISmsMessageBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessageBase'
    _iid_ = Guid('{2cf0fe30-fe50-4fc6-aa88-4ccfe27a29ea}')
    @winrt_commethod(6)
    def get_MessageType(self) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_MessageClass(self) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_commethod(10)
    def get_SimIccId(self) -> WinRT_String: ...
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    MessageClass = property(get_MessageClass, None)
    MessageType = property(get_MessageType, None)
    SimIccId = property(get_SimIccId, None)
class ISmsMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessageReceivedEventArgs'
    _iid_ = Guid('{08e80a98-b8e5-41c1-a3d8-d3abfae22675}')
    @winrt_commethod(6)
    def get_TextMessage(self) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_commethod(7)
    def get_BinaryMessage(self) -> win32more.Windows.Devices.Sms.SmsBinaryMessage: ...
    BinaryMessage = property(get_BinaryMessage, None)
    TextMessage = property(get_TextMessage, None)
class ISmsMessageReceivedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails'
    _iid_ = Guid('{2bcfcbd4-2657-4128-ad5f-e3877132bdb1}')
    @winrt_commethod(6)
    def get_MessageType(self) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_TextMessage(self) -> win32more.Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_commethod(8)
    def get_WapMessage(self) -> win32more.Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_commethod(9)
    def get_AppMessage(self) -> win32more.Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_commethod(10)
    def get_BroadcastMessage(self) -> win32more.Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_commethod(11)
    def get_VoicemailMessage(self) -> win32more.Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_commethod(12)
    def get_StatusMessage(self) -> win32more.Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_commethod(13)
    def Drop(self) -> Void: ...
    @winrt_commethod(14)
    def Accept(self) -> Void: ...
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    MessageType = property(get_MessageType, None)
    StatusMessage = property(get_StatusMessage, None)
    TextMessage = property(get_TextMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    WapMessage = property(get_WapMessage, None)
class ISmsMessageRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessageRegistration'
    _iid_ = Guid('{1720503e-f34f-446b-83b3-0ff19923b409}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sms.SmsMessageRegistration, win32more.Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
    MessageReceived = event()
class ISmsMessageRegistrationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsMessageRegistrationStatics'
    _iid_ = Guid('{63a05464-2898-4778-a03c-6f994907d63a}')
    @winrt_commethod(6)
    def get_AllRegistrations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_commethod(7)
    def Register(self, id: WinRT_String, filterRules: win32more.Windows.Devices.Sms.SmsFilterRules) -> win32more.Windows.Devices.Sms.SmsMessageRegistration: ...
    AllRegistrations = property(get_AllRegistrations, None)
class ISmsReceivedEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsReceivedEventDetails'
    _iid_ = Guid('{5bb50f15-e46d-4c82-847d-5a0304c1d53d}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MessageIndex(self) -> UInt32: ...
    DeviceId = property(get_DeviceId, None)
    MessageIndex = property(get_MessageIndex, None)
class ISmsReceivedEventDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsReceivedEventDetails2'
    _iid_ = Guid('{40e05c86-a7b4-4771-9ae7-0b5ffb12c03a}')
    @winrt_commethod(6)
    def get_MessageClass(self) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_commethod(7)
    def get_BinaryMessage(self) -> win32more.Windows.Devices.Sms.SmsBinaryMessage: ...
    BinaryMessage = property(get_BinaryMessage, None)
    MessageClass = property(get_MessageClass, None)
class ISmsSendMessageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsSendMessageResult'
    _iid_ = Guid('{db139af2-78c9-4feb-9622-452328088d62}')
    @winrt_commethod(6)
    def get_IsSuccessful(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MessageReferenceNumbers(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_ModemErrorCode(self) -> win32more.Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_commethod(10)
    def get_IsErrorTransient(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_NetworkCauseCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_TransportFailureCause(self) -> Int32: ...
    CellularClass = property(get_CellularClass, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class ISmsStatusMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsStatusMessage'
    _iid_ = Guid('{e6d28342-b70b-4677-9379-c9783fdff8f4}')
    @winrt_commethod(6)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Status(self) -> Int32: ...
    @winrt_commethod(10)
    def get_MessageReferenceNumber(self) -> Int32: ...
    @winrt_commethod(11)
    def get_ServiceCenterTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_DischargeTime(self) -> win32more.Windows.Foundation.DateTime: ...
    Body = property(get_Body, None)
    DischargeTime = property(get_DischargeTime, None)
    From = property(get_From, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    Status = property(get_Status, None)
    To = property(get_To, None)
class ISmsTextMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsTextMessage'
    _iid_ = Guid('{d61c904c-a495-487f-9a6f-971548c5bc9f}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PartReferenceId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_PartNumber(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PartCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_From(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Encoding(self) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(17)
    def put_Encoding(self, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(18)
    def ToBinaryMessages(self, format: win32more.Windows.Devices.Sms.SmsDataFormat) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsBinaryMessage]: ...
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, put_From)
    PartCount = property(get_PartCount, None)
    PartNumber = property(get_PartNumber, None)
    PartReferenceId = property(get_PartReferenceId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class ISmsTextMessage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsTextMessage2'
    _iid_ = Guid('{22a0d893-4555-4755-b5a1-e7fd84955f8d}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_To(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Body(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Encoding(self) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(13)
    def put_Encoding(self, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_commethod(14)
    def get_CallbackNumber(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_CallbackNumber(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_IsDeliveryNotificationEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsDeliveryNotificationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_RetryAttemptCount(self) -> Int32: ...
    @winrt_commethod(19)
    def put_RetryAttemptCount(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_TeleserviceId(self) -> Int32: ...
    @winrt_commethod(21)
    def get_ProtocolId(self) -> Int32: ...
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, None)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    ProtocolId = property(get_ProtocolId, None)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class ISmsTextMessageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsTextMessageStatics'
    _iid_ = Guid('{7f68c5ed-3ccc-47a3-8c55-380d3b010892}')
    @winrt_commethod(6)
    def FromBinaryMessage(self, binaryMessage: win32more.Windows.Devices.Sms.SmsBinaryMessage) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_commethod(7)
    def FromBinaryData(self, format: win32more.Windows.Devices.Sms.SmsDataFormat, value: PassArray[Byte]) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
class ISmsVoicemailMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsVoicemailMessage'
    _iid_ = Guid('{271aa0a6-95b1-44ff-bcb8-b8fdd7e08bc3}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MessageCount(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    Body = property(get_Body, None)
    MessageCount = property(get_MessageCount, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
class ISmsWapMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sms.ISmsWapMessage'
    _iid_ = Guid('{cd937743-7a55-4d3b-9021-f22e022d09c5}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ApplicationId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_BinaryBody(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ApplicationId = property(get_ApplicationId, None)
    BinaryBody = property(get_BinaryBody, None)
    ContentType = property(get_ContentType, None)
    From = property(get_From, None)
    Headers = property(get_Headers, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
LegacySmsApiContract: UInt32 = 65536
class SendSmsMessageOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[AwaitableProtocol]
    default_interface: win32more.Windows.Foundation.IAsyncAction
    _classid_ = 'Windows.Devices.Sms.SendSmsMessageOperation'
    @winrt_mixinmethod
    def put_Completed(self: win32more.Windows.Foundation.IAsyncAction, handler: win32more.Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Completed(self: win32more.Windows.Foundation.IAsyncAction) -> win32more.Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_mixinmethod
    def GetResults(self: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Foundation.IAsyncInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Foundation.IAsyncInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IAsyncInfo) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    ErrorCode = property(get_ErrorCode, None)
    Id = property(get_Id, None)
    Status = property(get_Status, None)
class SmsAppMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsAppMessage
    _classid_ = 'Windows.Devices.Sms.SmsAppMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsAppMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_PortNumber(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_PortNumber(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_TeleserviceId(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_ProtocolId(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: win32more.Windows.Devices.Sms.ISmsAppMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_BinaryBody(self: win32more.Windows.Devices.Sms.ISmsAppMessage, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, None)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    MessageClass = property(get_MessageClass, None)
    MessageType = property(get_MessageType, None)
    PortNumber = property(get_PortNumber, put_PortNumber)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    SimIccId = property(get_SimIccId, None)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class SmsBinaryMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsBinaryMessage
    _classid_ = 'Windows.Devices.Sms.SmsBinaryMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsBinaryMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Sms.SmsBinaryMessage: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Devices.Sms.ISmsBinaryMessage) -> win32more.Windows.Devices.Sms.SmsDataFormat: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Windows.Devices.Sms.ISmsBinaryMessage, value: win32more.Windows.Devices.Sms.SmsDataFormat) -> Void: ...
    @winrt_mixinmethod
    def GetData(self: win32more.Windows.Devices.Sms.ISmsBinaryMessage) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def SetData(self: win32more.Windows.Devices.Sms.ISmsBinaryMessage, value: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Sms.ISmsMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessage) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    Format = property(get_Format, put_Format)
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
class SmsBroadcastMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsBroadcastMessage
    _classid_ = 'Windows.Devices.Sms.SmsBroadcastMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Channel(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_GeographicalScope(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> win32more.Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_mixinmethod
    def get_MessageCode(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_UpdateNumber(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_BroadcastType(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> win32more.Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_mixinmethod
    def get_IsEmergencyAlert(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserPopupRequested(self: win32more.Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Body = property(get_Body, None)
    BroadcastType = property(get_BroadcastType, None)
    CellularClass = property(get_CellularClass, None)
    Channel = property(get_Channel, None)
    DeviceId = property(get_DeviceId, None)
    GeographicalScope = property(get_GeographicalScope, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
    MessageClass = property(get_MessageClass, None)
    MessageCode = property(get_MessageCode, None)
    MessageType = property(get_MessageType, None)
    SimIccId = property(get_SimIccId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    UpdateNumber = property(get_UpdateNumber, None)
class SmsBroadcastType(Enum, Int32):
    Other = 0
    CmasPresidential = 1
    CmasExtreme = 2
    CmasSevere = 3
    CmasAmber = 4
    CmasTest = 5
    EUAlert1 = 6
    EUAlert2 = 7
    EUAlert3 = 8
    EUAlertAmber = 9
    EUAlertInfo = 10
    EtwsEarthquake = 11
    EtwsTsunami = 12
    EtwsTsunamiAndEarthquake = 13
    LatAlertLocal = 14
class SmsDataFormat(Enum, Int32):
    Unknown = 0
    CdmaSubmit = 1
    GsmSubmit = 2
    CdmaDeliver = 3
    GsmDeliver = 4
class SmsDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsDevice
    _classid_ = 'Windows.Devices.Sms.SmsDevice'
    @winrt_mixinmethod
    def SendMessageAsync(self: win32more.Windows.Devices.Sms.ISmsDevice, message: win32more.Windows.Devices.Sms.ISmsMessage) -> win32more.Windows.Devices.Sms.SendSmsMessageOperation: ...
    @winrt_mixinmethod
    def CalculateLength(self: win32more.Windows.Devices.Sms.ISmsDevice, message: win32more.Windows.Devices.Sms.SmsTextMessage) -> win32more.Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_mixinmethod
    def get_AccountPhoneNumber(self: win32more.Windows.Devices.Sms.ISmsDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsDevice) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageStore(self: win32more.Windows.Devices.Sms.ISmsDevice) -> win32more.Windows.Devices.Sms.SmsDeviceMessageStore: ...
    @winrt_mixinmethod
    def get_DeviceStatus(self: win32more.Windows.Devices.Sms.ISmsDevice) -> win32more.Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_mixinmethod
    def add_SmsMessageReceived(self: win32more.Windows.Devices.Sms.ISmsDevice, eventHandler: win32more.Windows.Devices.Sms.SmsMessageReceivedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SmsMessageReceived(self: win32more.Windows.Devices.Sms.ISmsDevice, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SmsDeviceStatusChanged(self: win32more.Windows.Devices.Sms.ISmsDevice, eventHandler: win32more.Windows.Devices.Sms.SmsDeviceStatusChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SmsDeviceStatusChanged(self: win32more.Windows.Devices.Sms.ISmsDevice, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FromNetworkAccountIdAsync(cls: win32more.Windows.Devices.Sms.ISmsDeviceStatics2, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Sms.ISmsDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Sms.ISmsDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Sms.ISmsDeviceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsDevice]: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
    MessageStore = property(get_MessageStore, None)
    SmsMessageReceived = event()
    SmsDeviceStatusChanged = event()
class SmsDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsDevice2
    _classid_ = 'Windows.Devices.Sms.SmsDevice2'
    @winrt_mixinmethod
    def get_SmscAddress(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SmscAddress(self: win32more.Windows.Devices.Sms.ISmsDevice2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentDeviceId(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccountPhoneNumber(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_DeviceStatus(self: win32more.Windows.Devices.Sms.ISmsDevice2) -> win32more.Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_mixinmethod
    def CalculateLength(self: win32more.Windows.Devices.Sms.ISmsDevice2, message: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_mixinmethod
    def SendMessageAndGetResultAsync(self: win32more.Windows.Devices.Sms.ISmsDevice2, message: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_mixinmethod
    def add_DeviceStatusChanged(self: win32more.Windows.Devices.Sms.ISmsDevice2, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sms.SmsDevice2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceStatusChanged(self: win32more.Windows.Devices.Sms.ISmsDevice2, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Sms.ISmsDevice2Statics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Devices.Sms.ISmsDevice2Statics, deviceId: WinRT_String) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Devices.Sms.ISmsDevice2Statics) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def FromParentId(cls: win32more.Windows.Devices.Sms.ISmsDevice2Statics, parentDeviceId: WinRT_String) -> win32more.Windows.Devices.Sms.SmsDevice2: ...
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    DeviceStatus = property(get_DeviceStatus, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceStatusChanged = event()
class SmsDeviceMessageStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore
    _classid_ = 'Windows.Devices.Sms.SmsDeviceMessageStore'
    @winrt_mixinmethod
    def DeleteMessageAsync(self: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore, messageId: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteMessagesAsync(self: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore, messageFilter: win32more.Windows.Devices.Sms.SmsMessageFilter) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMessageAsync(self: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore, messageId: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sms.ISmsMessage]: ...
    @winrt_mixinmethod
    def GetMessagesAsync(self: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore, messageFilter: win32more.Windows.Devices.Sms.SmsMessageFilter) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsMessage], Int32]: ...
    @winrt_mixinmethod
    def get_MaxMessages(self: win32more.Windows.Devices.Sms.ISmsDeviceMessageStore) -> UInt32: ...
    MaxMessages = property(get_MaxMessages, None)
class SmsDeviceStatus(Enum, Int32):
    Off = 0
    Ready = 1
    SimNotInserted = 2
    BadSim = 3
    DeviceFailure = 4
    SubscriptionNotActivated = 5
    DeviceLocked = 6
    DeviceBlocked = 7
class SmsDeviceStatusChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{982b1162-3dd7-4618-af89-0c272d5d06d8}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Devices.Sms.SmsDevice) -> Void: ...
class SmsEncodedLength(Structure):
    SegmentCount: UInt32
    CharacterCountLastSegment: UInt32
    CharactersPerSegment: UInt32
    ByteCountLastSegment: UInt32
    BytesPerSegment: UInt32
class SmsEncoding(Enum, Int32):
    Unknown = 0
    Optimal = 1
    SevenBitAscii = 2
    Unicode = 3
    GsmSevenBit = 4
    EightBit = 5
    Latin = 6
    Korean = 7
    IA5 = 8
    ShiftJis = 9
    LatinHebrew = 10
class SmsFilterActionType(Enum, Int32):
    AcceptImmediately = 0
    Drop = 1
    Peek = 2
    Accept = 3
class SmsFilterRule(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsFilterRule
    _classid_ = 'Windows.Devices.Sms.SmsFilterRule'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsFilterRule.CreateFilterRule(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFilterRule(cls: win32more.Windows.Devices.Sms.ISmsFilterRuleFactory, messageType: win32more.Windows.Devices.Sms.SmsMessageType) -> win32more.Windows.Devices.Sms.SmsFilterRule: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_ImsiPrefixes(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeviceIds(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SenderNumbers(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TextMessagePrefixes(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PortNumbers(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def put_CellularClass(self: win32more.Windows.Devices.Sms.ISmsFilterRule, value: win32more.Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolIds(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_TeleserviceIds(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_WapApplicationIds(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_WapContentTypes(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_BroadcastTypes(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_mixinmethod
    def get_BroadcastChannels(self: win32more.Windows.Devices.Sms.ISmsFilterRule) -> win32more.Windows.Foundation.Collections.IVector[Int32]: ...
    BroadcastChannels = property(get_BroadcastChannels, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    DeviceIds = property(get_DeviceIds, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    MessageType = property(get_MessageType, None)
    PortNumbers = property(get_PortNumbers, None)
    ProtocolIds = property(get_ProtocolIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
class SmsFilterRules(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsFilterRules
    _classid_ = 'Windows.Devices.Sms.SmsFilterRules'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsFilterRules.CreateFilterRules(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFilterRules(cls: win32more.Windows.Devices.Sms.ISmsFilterRulesFactory, actionType: win32more.Windows.Devices.Sms.SmsFilterActionType) -> win32more.Windows.Devices.Sms.SmsFilterRules: ...
    @winrt_mixinmethod
    def get_ActionType(self: win32more.Windows.Devices.Sms.ISmsFilterRules) -> win32more.Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_mixinmethod
    def get_Rules(self: win32more.Windows.Devices.Sms.ISmsFilterRules) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
class SmsGeographicalScope(Enum, Int32):
    None_ = 0
    CellWithImmediateDisplay = 1
    LocationArea = 2
    Plmn = 3
    Cell = 4
class SmsMessageClass(Enum, Int32):
    None_ = 0
    Class0 = 1
    Class1 = 2
    Class2 = 3
    Class3 = 4
class SmsMessageFilter(Enum, Int32):
    All = 0
    Unread = 1
    Read = 2
    Sent = 3
    Draft = 4
class SmsMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsMessageReceivedEventArgs
    _classid_ = 'Windows.Devices.Sms.SmsMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_TextMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedEventArgs) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_mixinmethod
    def get_BinaryMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedEventArgs) -> win32more.Windows.Devices.Sms.SmsBinaryMessage: ...
    BinaryMessage = property(get_BinaryMessage, None)
    TextMessage = property(get_TextMessage, None)
class SmsMessageReceivedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b7ad409-ec2d-47ce-a253-732beeebcacd}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Devices.Sms.SmsDevice, e: win32more.Windows.Devices.Sms.SmsMessageReceivedEventArgs) -> Void: ...
class SmsMessageReceivedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails
    _classid_ = 'Windows.Devices.Sms.SmsMessageReceivedTriggerDetails'
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_TextMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_WapMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_mixinmethod
    def get_AppMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_BroadcastMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_mixinmethod
    def get_VoicemailMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_mixinmethod
    def get_StatusMessage(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> win32more.Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_mixinmethod
    def Drop(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    MessageType = property(get_MessageType, None)
    StatusMessage = property(get_StatusMessage, None)
    TextMessage = property(get_TextMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    WapMessage = property(get_WapMessage, None)
class _SmsMessageRegistration_Meta_(ComPtr.__class__):
    pass
class SmsMessageRegistration(ComPtr, metaclass=_SmsMessageRegistration_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsMessageRegistration
    _classid_ = 'Windows.Devices.Sms.SmsMessageRegistration'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Sms.ISmsMessageRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Windows.Devices.Sms.ISmsMessageRegistration) -> Void: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Devices.Sms.ISmsMessageRegistration, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sms.SmsMessageRegistration, win32more.Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Devices.Sms.ISmsMessageRegistration, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllRegistrations(cls: win32more.Windows.Devices.Sms.ISmsMessageRegistrationStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_classmethod
    def Register(cls: win32more.Windows.Devices.Sms.ISmsMessageRegistrationStatics, id: WinRT_String, filterRules: win32more.Windows.Devices.Sms.SmsFilterRules) -> win32more.Windows.Devices.Sms.SmsMessageRegistration: ...
    Id = property(get_Id, None)
    _SmsMessageRegistration_Meta_.AllRegistrations = property(get_AllRegistrations, None)
    MessageReceived = event()
class SmsMessageType(Enum, Int32):
    Binary = 0
    Text = 1
    Wap = 2
    App = 3
    Broadcast = 4
    Voicemail = 5
    Status = 6
class SmsModemErrorCode(Enum, Int32):
    Other = 0
    MessagingNetworkError = 1
    SmsOperationNotSupportedByDevice = 2
    SmsServiceNotSupportedByNetwork = 3
    DeviceFailure = 4
    MessageNotEncodedProperly = 5
    MessageTooLarge = 6
    DeviceNotReady = 7
    NetworkNotReady = 8
    InvalidSmscAddress = 9
    NetworkFailure = 10
    FixedDialingNumberRestricted = 11
class SmsReceivedEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsReceivedEventDetails
    _classid_ = 'Windows.Devices.Sms.SmsReceivedEventDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsReceivedEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageIndex(self: win32more.Windows.Devices.Sms.ISmsReceivedEventDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsReceivedEventDetails2) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_BinaryMessage(self: win32more.Windows.Devices.Sms.ISmsReceivedEventDetails2) -> win32more.Windows.Devices.Sms.SmsBinaryMessage: ...
    BinaryMessage = property(get_BinaryMessage, None)
    DeviceId = property(get_DeviceId, None)
    MessageClass = property(get_MessageClass, None)
    MessageIndex = property(get_MessageIndex, None)
class SmsSendMessageResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsSendMessageResult
    _classid_ = 'Windows.Devices.Sms.SmsSendMessageResult'
    @winrt_mixinmethod
    def get_IsSuccessful(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumbers(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_ModemErrorCode(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> win32more.Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_mixinmethod
    def get_IsErrorTransient(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_NetworkCauseCode(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    @winrt_mixinmethod
    def get_TransportFailureCause(self: win32more.Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    CellularClass = property(get_CellularClass, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class SmsStatusMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsStatusMessage
    _classid_ = 'Windows.Devices.Sms.SmsStatusMessage'
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumber(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_ServiceCenterTimestamp(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_DischargeTime(self: win32more.Windows.Devices.Sms.ISmsStatusMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Body = property(get_Body, None)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    DischargeTime = property(get_DischargeTime, None)
    From = property(get_From, None)
    MessageClass = property(get_MessageClass, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    MessageType = property(get_MessageType, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    SimIccId = property(get_SimIccId, None)
    Status = property(get_Status, None)
    To = property(get_To, None)
class SmsTextMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsTextMessage
    _classid_ = 'Windows.Devices.Sms.SmsTextMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsTextMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PartReferenceId(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_PartNumber(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_PartCount(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_From(self: win32more.Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: win32more.Windows.Devices.Sms.ISmsTextMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: win32more.Windows.Devices.Sms.ISmsTextMessage) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: win32more.Windows.Devices.Sms.ISmsTextMessage, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def ToBinaryMessages(self: win32more.Windows.Devices.Sms.ISmsTextMessage, format: win32more.Windows.Devices.Sms.SmsDataFormat) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sms.ISmsBinaryMessage]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Sms.ISmsMessage) -> UInt32: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessage) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_classmethod
    def FromBinaryMessage(cls: win32more.Windows.Devices.Sms.ISmsTextMessageStatics, binaryMessage: win32more.Windows.Devices.Sms.SmsBinaryMessage) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    @winrt_classmethod
    def FromBinaryData(cls: win32more.Windows.Devices.Sms.ISmsTextMessageStatics, format: win32more.Windows.Devices.Sms.SmsDataFormat, value: PassArray[Byte]) -> win32more.Windows.Devices.Sms.SmsTextMessage: ...
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, put_From)
    Id = property(get_Id, None)
    MessageClass = property(get_MessageClass, None)
    PartCount = property(get_PartCount, None)
    PartNumber = property(get_PartNumber, None)
    PartReferenceId = property(get_PartReferenceId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class SmsTextMessage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsTextMessage2
    _classid_ = 'Windows.Devices.Sms.SmsTextMessage2'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Sms.SmsTextMessage2.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> win32more.Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: win32more.Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: win32more.Windows.Devices.Sms.ISmsTextMessage2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: win32more.Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    Encoding = property(get_Encoding, put_Encoding)
    From = property(get_From, None)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    MessageClass = property(get_MessageClass, None)
    MessageType = property(get_MessageType, None)
    ProtocolId = property(get_ProtocolId, None)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    SimIccId = property(get_SimIccId, None)
    TeleserviceId = property(get_TeleserviceId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
class SmsVoicemailMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsVoicemailMessage
    _classid_ = 'Windows.Devices.Sms.SmsVoicemailMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsVoicemailMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageCount(self: win32more.Windows.Devices.Sms.ISmsVoicemailMessage) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Body = property(get_Body, None)
    CellularClass = property(get_CellularClass, None)
    DeviceId = property(get_DeviceId, None)
    MessageClass = property(get_MessageClass, None)
    MessageCount = property(get_MessageCount, None)
    MessageType = property(get_MessageType, None)
    SimIccId = property(get_SimIccId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
class SmsWapMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sms.ISmsWapMessage
    _classid_ = 'Windows.Devices.Sms.SmsWapMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Devices.Sms.ISmsWapMessage) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_MessageType(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> win32more.Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: win32more.Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    ApplicationId = property(get_ApplicationId, None)
    BinaryBody = property(get_BinaryBody, None)
    CellularClass = property(get_CellularClass, None)
    ContentType = property(get_ContentType, None)
    DeviceId = property(get_DeviceId, None)
    From = property(get_From, None)
    Headers = property(get_Headers, None)
    MessageClass = property(get_MessageClass, None)
    MessageType = property(get_MessageType, None)
    SimIccId = property(get_SimIccId, None)
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)


make_ready(__name__)
