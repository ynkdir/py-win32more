from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.Sms
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CellularClass = Int32
CellularClass_None: CellularClass = 0
CellularClass_Gsm: CellularClass = 1
CellularClass_Cdma: CellularClass = 2
class ISmsAppMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e8bb8494-d3a0-4a0a-86-d7-29-10-33-a8-cf-54')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
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
    def get_Encoding(self) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(19)
    def put_Encoding(self, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
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
    def get_BinaryBody(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(27)
    def put_BinaryBody(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    Encoding = property(get_Encoding, put_Encoding)
    PortNumber = property(get_PortNumber, put_PortNumber)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
class ISmsBroadcastMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75aebbf1-e4b7-4874-a0-9c-29-56-e5-92-f9-57')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Channel(self) -> Int32: ...
    @winrt_commethod(10)
    def get_GeographicalScope(self) -> Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_commethod(11)
    def get_MessageCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_UpdateNumber(self) -> Int32: ...
    @winrt_commethod(13)
    def get_BroadcastType(self) -> Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_commethod(14)
    def get_IsEmergencyAlert(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsUserPopupRequested(self) -> Boolean: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    Channel = property(get_Channel, None)
    GeographicalScope = property(get_GeographicalScope, None)
    MessageCode = property(get_MessageCode, None)
    UpdateNumber = property(get_UpdateNumber, None)
    BroadcastType = property(get_BroadcastType, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
class ISmsDevice2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bd8a5c13-e522-46cb-b8-d5-9e-ad-30-fb-6c-47')
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
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(12)
    def get_DeviceStatus(self) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_commethod(13)
    def CalculateLength(self, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_commethod(14)
    def SendMessageAndGetResultAsync(self, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_commethod(15)
    def add_DeviceStatusChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsDevice2, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DeviceStatusChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceId = property(get_DeviceId, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
class ISmsDevice2Statics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('65c78325-1031-491e-8f-b6-ef-99-91-af-e3-63')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, deviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(8)
    def GetDefault(self) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_commethod(9)
    def FromParentId(self, parentDeviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
class ISmsFilterRule(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40e32fae-b049-4fbc-af-e9-e2-a6-10-ef-f5-5c')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_ImsiPrefixes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_DeviceIds(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_SenderNumbers(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_TextMessagePrefixes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_PortNumbers(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(12)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(13)
    def put_CellularClass(self, value: Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_commethod(14)
    def get_ProtocolIds(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(15)
    def get_TeleserviceIds(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_commethod(16)
    def get_WapApplicationIds(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(17)
    def get_WapContentTypes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(18)
    def get_BroadcastTypes(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_commethod(19)
    def get_BroadcastChannels(self) -> Windows.Foundation.Collections.IVector[Int32]: ...
    MessageType = property(get_MessageType, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    DeviceIds = property(get_DeviceIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    PortNumbers = property(get_PortNumbers, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    ProtocolIds = property(get_ProtocolIds, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    BroadcastChannels = property(get_BroadcastChannels, None)
class ISmsFilterRuleFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00c36508-6296-4f29-9a-ad-89-20-ce-ba-3c-e8')
    @winrt_commethod(6)
    def CreateFilterRule(self, messageType: Windows.Devices.Sms.SmsMessageType) -> Windows.Devices.Sms.SmsFilterRule: ...
class ISmsFilterRules(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e47eafb-79cd-4881-98-94-55-a4-13-5b-23-fa')
    @winrt_commethod(6)
    def get_ActionType(self) -> Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_commethod(7)
    def get_Rules(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
class ISmsFilterRulesFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a09924ed-6e2e-4530-9f-de-46-5d-02-ee-d0-0e')
    @winrt_commethod(6)
    def CreateFilterRules(self, actionType: Windows.Devices.Sms.SmsFilterActionType) -> Windows.Devices.Sms.SmsFilterRules: ...
class ISmsMessageBase(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2cf0fe30-fe50-4fc6-aa-88-4c-cf-e2-7a-29-ea')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_MessageClass(self) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_commethod(10)
    def get_SimIccId(self) -> WinRT_String: ...
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class ISmsMessageReceivedTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2bcfcbd4-2657-4128-ad-5f-e3-87-71-32-bd-b1')
    @winrt_commethod(6)
    def get_MessageType(self) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_commethod(7)
    def get_TextMessage(self) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_commethod(8)
    def get_WapMessage(self) -> Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_commethod(9)
    def get_AppMessage(self) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_commethod(10)
    def get_BroadcastMessage(self) -> Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_commethod(11)
    def get_VoicemailMessage(self) -> Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_commethod(12)
    def get_StatusMessage(self) -> Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_commethod(13)
    def Drop(self) -> Void: ...
    @winrt_commethod(14)
    def Accept(self) -> Void: ...
    MessageType = property(get_MessageType, None)
    TextMessage = property(get_TextMessage, None)
    WapMessage = property(get_WapMessage, None)
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    StatusMessage = property(get_StatusMessage, None)
class ISmsMessageRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1720503e-f34f-446b-83-b3-0f-f1-99-23-b4-09')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def add_MessageReceived(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsMessageRegistration, Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MessageReceived(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
class ISmsMessageRegistrationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63a05464-2898-4778-a0-3c-6f-99-49-07-d6-3a')
    @winrt_commethod(6)
    def get_AllRegistrations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_commethod(7)
    def Register(self, id: WinRT_String, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.Devices.Sms.SmsMessageRegistration: ...
    AllRegistrations = property(get_AllRegistrations, None)
class ISmsSendMessageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db139af2-78c9-4feb-96-22-45-23-28-08-8d-62')
    @winrt_commethod(6)
    def get_IsSuccessful(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MessageReferenceNumbers(self) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_commethod(8)
    def get_CellularClass(self) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_commethod(9)
    def get_ModemErrorCode(self) -> Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_commethod(10)
    def get_IsErrorTransient(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_NetworkCauseCode(self) -> Int32: ...
    @winrt_commethod(12)
    def get_TransportFailureCause(self) -> Int32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    CellularClass = property(get_CellularClass, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class ISmsStatusMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e6d28342-b70b-4677-93-79-c9-78-3f-df-f8-f4')
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
    def get_ServiceCenterTimestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(12)
    def get_DischargeTime(self) -> Windows.Foundation.DateTime: ...
    To = property(get_To, None)
    From = property(get_From, None)
    Body = property(get_Body, None)
    Status = property(get_Status, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    DischargeTime = property(get_DischargeTime, None)
class ISmsTextMessage2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22a0d893-4555-4755-b5-a1-e7-fd-84-95-5f-8d')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
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
    def get_Encoding(self) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_commethod(13)
    def put_Encoding(self, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
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
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, None)
    ProtocolId = property(get_ProtocolId, None)
class ISmsVoicemailMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('271aa0a6-95b1-44ff-bc-b8-b8-fd-d7-e0-8b-c3')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MessageCount(self) -> Windows.Foundation.IReference[Int32]: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    MessageCount = property(get_MessageCount, None)
class ISmsWapMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd937743-7a55-4d3b-90-21-f2-2e-02-2d-09-c5')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_To(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_From(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ApplicationId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_BinaryBody(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Headers(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    From = property(get_From, None)
    ApplicationId = property(get_ApplicationId, None)
    ContentType = property(get_ContentType, None)
    BinaryBody = property(get_BinaryBody, None)
    Headers = property(get_Headers, None)
class SmsAppMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsAppMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: Windows.Devices.Sms.ISmsAppMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: Windows.Devices.Sms.ISmsAppMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsAppMessage) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsAppMessage, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: Windows.Devices.Sms.ISmsAppMessage, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_PortNumber(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_PortNumber(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_TeleserviceId(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: Windows.Devices.Sms.ISmsAppMessage) -> Int32: ...
    @winrt_mixinmethod
    def put_ProtocolId(self: Windows.Devices.Sms.ISmsAppMessage, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: Windows.Devices.Sms.ISmsAppMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_BinaryBody(self: Windows.Devices.Sms.ISmsAppMessage, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    Encoding = property(get_Encoding, put_Encoding)
    PortNumber = property(get_PortNumber, put_PortNumber)
    TeleserviceId = property(get_TeleserviceId, put_TeleserviceId)
    ProtocolId = property(get_ProtocolId, put_ProtocolId)
    BinaryBody = property(get_BinaryBody, put_BinaryBody)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsBroadcastMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsBroadcastMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Channel(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_GeographicalScope(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Devices.Sms.SmsGeographicalScope: ...
    @winrt_mixinmethod
    def get_MessageCode(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_UpdateNumber(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_BroadcastType(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Windows.Devices.Sms.SmsBroadcastType: ...
    @winrt_mixinmethod
    def get_IsEmergencyAlert(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserPopupRequested(self: Windows.Devices.Sms.ISmsBroadcastMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    Channel = property(get_Channel, None)
    GeographicalScope = property(get_GeographicalScope, None)
    MessageCode = property(get_MessageCode, None)
    UpdateNumber = property(get_UpdateNumber, None)
    BroadcastType = property(get_BroadcastType, None)
    IsEmergencyAlert = property(get_IsEmergencyAlert, None)
    IsUserPopupRequested = property(get_IsUserPopupRequested, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
SmsBroadcastType = Int32
SmsBroadcastType_Other: SmsBroadcastType = 0
SmsBroadcastType_CmasPresidential: SmsBroadcastType = 1
SmsBroadcastType_CmasExtreme: SmsBroadcastType = 2
SmsBroadcastType_CmasSevere: SmsBroadcastType = 3
SmsBroadcastType_CmasAmber: SmsBroadcastType = 4
SmsBroadcastType_CmasTest: SmsBroadcastType = 5
SmsBroadcastType_EUAlert1: SmsBroadcastType = 6
SmsBroadcastType_EUAlert2: SmsBroadcastType = 7
SmsBroadcastType_EUAlert3: SmsBroadcastType = 8
SmsBroadcastType_EUAlertAmber: SmsBroadcastType = 9
SmsBroadcastType_EUAlertInfo: SmsBroadcastType = 10
SmsBroadcastType_EtwsEarthquake: SmsBroadcastType = 11
SmsBroadcastType_EtwsTsunami: SmsBroadcastType = 12
SmsBroadcastType_EtwsTsunamiAndEarthquake: SmsBroadcastType = 13
SmsBroadcastType_LatAlertLocal: SmsBroadcastType = 14
SmsDataFormat = Int32
SmsDataFormat_Unknown: SmsDataFormat = 0
SmsDataFormat_CdmaSubmit: SmsDataFormat = 1
SmsDataFormat_GsmSubmit: SmsDataFormat = 2
SmsDataFormat_CdmaDeliver: SmsDataFormat = 3
SmsDataFormat_GsmDeliver: SmsDataFormat = 4
class SmsDevice2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsDevice2'
    @winrt_mixinmethod
    def get_SmscAddress(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SmscAddress(self: Windows.Devices.Sms.ISmsDevice2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentDeviceId(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccountPhoneNumber(self: Windows.Devices.Sms.ISmsDevice2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsDevice2) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_DeviceStatus(self: Windows.Devices.Sms.ISmsDevice2) -> Windows.Devices.Sms.SmsDeviceStatus: ...
    @winrt_mixinmethod
    def CalculateLength(self: Windows.Devices.Sms.ISmsDevice2, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsEncodedLength: ...
    @winrt_mixinmethod
    def SendMessageAndGetResultAsync(self: Windows.Devices.Sms.ISmsDevice2, message: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sms.SmsSendMessageResult]: ...
    @winrt_mixinmethod
    def add_DeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsDevice2, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeviceStatusChanged(self: Windows.Devices.Sms.ISmsDevice2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sms.ISmsDevice2Statics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: Windows.Devices.Sms.ISmsDevice2Statics, deviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sms.ISmsDevice2Statics) -> Windows.Devices.Sms.SmsDevice2: ...
    @winrt_classmethod
    def FromParentId(cls: Windows.Devices.Sms.ISmsDevice2Statics, parentDeviceId: WinRT_String) -> Windows.Devices.Sms.SmsDevice2: ...
    SmscAddress = property(get_SmscAddress, put_SmscAddress)
    DeviceId = property(get_DeviceId, None)
    ParentDeviceId = property(get_ParentDeviceId, None)
    AccountPhoneNumber = property(get_AccountPhoneNumber, None)
    CellularClass = property(get_CellularClass, None)
    DeviceStatus = property(get_DeviceStatus, None)
SmsDeviceStatus = Int32
SmsDeviceStatus_Off: SmsDeviceStatus = 0
SmsDeviceStatus_Ready: SmsDeviceStatus = 1
SmsDeviceStatus_SimNotInserted: SmsDeviceStatus = 2
SmsDeviceStatus_BadSim: SmsDeviceStatus = 3
SmsDeviceStatus_DeviceFailure: SmsDeviceStatus = 4
SmsDeviceStatus_SubscriptionNotActivated: SmsDeviceStatus = 5
SmsDeviceStatus_DeviceLocked: SmsDeviceStatus = 6
SmsDeviceStatus_DeviceBlocked: SmsDeviceStatus = 7
class SmsEncodedLength(EasyCastStructure):
    SegmentCount: UInt32
    CharacterCountLastSegment: UInt32
    CharactersPerSegment: UInt32
    ByteCountLastSegment: UInt32
    BytesPerSegment: UInt32
SmsEncoding = Int32
SmsEncoding_Unknown: SmsEncoding = 0
SmsEncoding_Optimal: SmsEncoding = 1
SmsEncoding_SevenBitAscii: SmsEncoding = 2
SmsEncoding_Unicode: SmsEncoding = 3
SmsEncoding_GsmSevenBit: SmsEncoding = 4
SmsEncoding_EightBit: SmsEncoding = 5
SmsEncoding_Latin: SmsEncoding = 6
SmsEncoding_Korean: SmsEncoding = 7
SmsEncoding_IA5: SmsEncoding = 8
SmsEncoding_ShiftJis: SmsEncoding = 9
SmsEncoding_LatinHebrew: SmsEncoding = 10
SmsFilterActionType = Int32
SmsFilterActionType_AcceptImmediately: SmsFilterActionType = 0
SmsFilterActionType_Drop: SmsFilterActionType = 1
SmsFilterActionType_Peek: SmsFilterActionType = 2
SmsFilterActionType_Accept: SmsFilterActionType = 3
class SmsFilterRule(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsFilterRule'
    @winrt_factorymethod
    def CreateFilterRule(cls: Windows.Devices.Sms.ISmsFilterRuleFactory, messageType: Windows.Devices.Sms.SmsMessageType) -> Windows.Devices.Sms.SmsFilterRule: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_ImsiPrefixes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeviceIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SenderNumbers(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TextMessagePrefixes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PortNumbers(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def put_CellularClass(self: Windows.Devices.Sms.ISmsFilterRule, value: Windows.Devices.Sms.CellularClass) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_TeleserviceIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    @winrt_mixinmethod
    def get_WapApplicationIds(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_WapContentTypes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_BroadcastTypes(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsBroadcastType]: ...
    @winrt_mixinmethod
    def get_BroadcastChannels(self: Windows.Devices.Sms.ISmsFilterRule) -> Windows.Foundation.Collections.IVector[Int32]: ...
    MessageType = property(get_MessageType, None)
    ImsiPrefixes = property(get_ImsiPrefixes, None)
    DeviceIds = property(get_DeviceIds, None)
    SenderNumbers = property(get_SenderNumbers, None)
    TextMessagePrefixes = property(get_TextMessagePrefixes, None)
    PortNumbers = property(get_PortNumbers, None)
    CellularClass = property(get_CellularClass, put_CellularClass)
    ProtocolIds = property(get_ProtocolIds, None)
    TeleserviceIds = property(get_TeleserviceIds, None)
    WapApplicationIds = property(get_WapApplicationIds, None)
    WapContentTypes = property(get_WapContentTypes, None)
    BroadcastTypes = property(get_BroadcastTypes, None)
    BroadcastChannels = property(get_BroadcastChannels, None)
class SmsFilterRules(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsFilterRules'
    @winrt_factorymethod
    def CreateFilterRules(cls: Windows.Devices.Sms.ISmsFilterRulesFactory, actionType: Windows.Devices.Sms.SmsFilterActionType) -> Windows.Devices.Sms.SmsFilterRules: ...
    @winrt_mixinmethod
    def get_ActionType(self: Windows.Devices.Sms.ISmsFilterRules) -> Windows.Devices.Sms.SmsFilterActionType: ...
    @winrt_mixinmethod
    def get_Rules(self: Windows.Devices.Sms.ISmsFilterRules) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sms.SmsFilterRule]: ...
    ActionType = property(get_ActionType, None)
    Rules = property(get_Rules, None)
SmsGeographicalScope = Int32
SmsGeographicalScope_None: SmsGeographicalScope = 0
SmsGeographicalScope_CellWithImmediateDisplay: SmsGeographicalScope = 1
SmsGeographicalScope_LocationArea: SmsGeographicalScope = 2
SmsGeographicalScope_Plmn: SmsGeographicalScope = 3
SmsGeographicalScope_Cell: SmsGeographicalScope = 4
SmsMessageClass = Int32
SmsMessageClass_None: SmsMessageClass = 0
SmsMessageClass_Class0: SmsMessageClass = 1
SmsMessageClass_Class1: SmsMessageClass = 2
SmsMessageClass_Class2: SmsMessageClass = 3
SmsMessageClass_Class3: SmsMessageClass = 4
class SmsMessageReceivedTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsMessageReceivedTriggerDetails'
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_TextMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_WapMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsWapMessage: ...
    @winrt_mixinmethod
    def get_AppMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsAppMessage: ...
    @winrt_mixinmethod
    def get_BroadcastMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsBroadcastMessage: ...
    @winrt_mixinmethod
    def get_VoicemailMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsVoicemailMessage: ...
    @winrt_mixinmethod
    def get_StatusMessage(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Windows.Devices.Sms.SmsStatusMessage: ...
    @winrt_mixinmethod
    def Drop(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    @winrt_mixinmethod
    def Accept(self: Windows.Devices.Sms.ISmsMessageReceivedTriggerDetails) -> Void: ...
    MessageType = property(get_MessageType, None)
    TextMessage = property(get_TextMessage, None)
    WapMessage = property(get_WapMessage, None)
    AppMessage = property(get_AppMessage, None)
    BroadcastMessage = property(get_BroadcastMessage, None)
    VoicemailMessage = property(get_VoicemailMessage, None)
    StatusMessage = property(get_StatusMessage, None)
class SmsMessageRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsMessageRegistration'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Sms.ISmsMessageRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def Unregister(self: Windows.Devices.Sms.ISmsMessageRegistration) -> Void: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: Windows.Devices.Sms.ISmsMessageRegistration, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sms.SmsMessageRegistration, Windows.Devices.Sms.SmsMessageReceivedTriggerDetails]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: Windows.Devices.Sms.ISmsMessageRegistration, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_AllRegistrations(cls: Windows.Devices.Sms.ISmsMessageRegistrationStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sms.SmsMessageRegistration]: ...
    @winrt_classmethod
    def Register(cls: Windows.Devices.Sms.ISmsMessageRegistrationStatics, id: WinRT_String, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.Devices.Sms.SmsMessageRegistration: ...
    Id = property(get_Id, None)
    AllRegistrations = property(get_AllRegistrations, None)
SmsMessageType = Int32
SmsMessageType_Binary: SmsMessageType = 0
SmsMessageType_Text: SmsMessageType = 1
SmsMessageType_Wap: SmsMessageType = 2
SmsMessageType_App: SmsMessageType = 3
SmsMessageType_Broadcast: SmsMessageType = 4
SmsMessageType_Voicemail: SmsMessageType = 5
SmsMessageType_Status: SmsMessageType = 6
SmsModemErrorCode = Int32
SmsModemErrorCode_Other: SmsModemErrorCode = 0
SmsModemErrorCode_MessagingNetworkError: SmsModemErrorCode = 1
SmsModemErrorCode_SmsOperationNotSupportedByDevice: SmsModemErrorCode = 2
SmsModemErrorCode_SmsServiceNotSupportedByNetwork: SmsModemErrorCode = 3
SmsModemErrorCode_DeviceFailure: SmsModemErrorCode = 4
SmsModemErrorCode_MessageNotEncodedProperly: SmsModemErrorCode = 5
SmsModemErrorCode_MessageTooLarge: SmsModemErrorCode = 6
SmsModemErrorCode_DeviceNotReady: SmsModemErrorCode = 7
SmsModemErrorCode_NetworkNotReady: SmsModemErrorCode = 8
SmsModemErrorCode_InvalidSmscAddress: SmsModemErrorCode = 9
SmsModemErrorCode_NetworkFailure: SmsModemErrorCode = 10
SmsModemErrorCode_FixedDialingNumberRestricted: SmsModemErrorCode = 11
class SmsSendMessageResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsSendMessageResult'
    @winrt_mixinmethod
    def get_IsSuccessful(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumbers(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_ModemErrorCode(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Windows.Devices.Sms.SmsModemErrorCode: ...
    @winrt_mixinmethod
    def get_IsErrorTransient(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_NetworkCauseCode(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    @winrt_mixinmethod
    def get_TransportFailureCause(self: Windows.Devices.Sms.ISmsSendMessageResult) -> Int32: ...
    IsSuccessful = property(get_IsSuccessful, None)
    MessageReferenceNumbers = property(get_MessageReferenceNumbers, None)
    CellularClass = property(get_CellularClass, None)
    ModemErrorCode = property(get_ModemErrorCode, None)
    IsErrorTransient = property(get_IsErrorTransient, None)
    NetworkCauseCode = property(get_NetworkCauseCode, None)
    TransportFailureCause = property(get_TransportFailureCause, None)
class SmsStatusMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsStatusMessage'
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsStatusMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageReferenceNumber(self: Windows.Devices.Sms.ISmsStatusMessage) -> Int32: ...
    @winrt_mixinmethod
    def get_ServiceCenterTimestamp(self: Windows.Devices.Sms.ISmsStatusMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_DischargeTime(self: Windows.Devices.Sms.ISmsStatusMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    To = property(get_To, None)
    From = property(get_From, None)
    Body = property(get_Body, None)
    Status = property(get_Status, None)
    MessageReferenceNumber = property(get_MessageReferenceNumber, None)
    ServiceCenterTimestamp = property(get_ServiceCenterTimestamp, None)
    DischargeTime = property(get_DischargeTime, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsTextMessage2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsTextMessage2'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Sms.SmsTextMessage2: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsTextMessage2) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_To(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Body(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Encoding(self: Windows.Devices.Sms.ISmsTextMessage2) -> Windows.Devices.Sms.SmsEncoding: ...
    @winrt_mixinmethod
    def put_Encoding(self: Windows.Devices.Sms.ISmsTextMessage2, value: Windows.Devices.Sms.SmsEncoding) -> Void: ...
    @winrt_mixinmethod
    def get_CallbackNumber(self: Windows.Devices.Sms.ISmsTextMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CallbackNumber(self: Windows.Devices.Sms.ISmsTextMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsTextMessage2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDeliveryNotificationEnabled(self: Windows.Devices.Sms.ISmsTextMessage2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RetryAttemptCount(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def put_RetryAttemptCount(self: Windows.Devices.Sms.ISmsTextMessage2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TeleserviceId(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_ProtocolId(self: Windows.Devices.Sms.ISmsTextMessage2) -> Int32: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, put_To)
    From = property(get_From, None)
    Body = property(get_Body, put_Body)
    Encoding = property(get_Encoding, put_Encoding)
    CallbackNumber = property(get_CallbackNumber, put_CallbackNumber)
    IsDeliveryNotificationEnabled = property(get_IsDeliveryNotificationEnabled, put_IsDeliveryNotificationEnabled)
    RetryAttemptCount = property(get_RetryAttemptCount, put_RetryAttemptCount)
    TeleserviceId = property(get_TeleserviceId, None)
    ProtocolId = property(get_ProtocolId, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsVoicemailMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsVoicemailMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Body(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageCount(self: Windows.Devices.Sms.ISmsVoicemailMessage) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    Body = property(get_Body, None)
    MessageCount = property(get_MessageCount, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
class SmsWapMessage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sms.SmsWapMessage'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_To(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_From(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationId(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Devices.Sms.ISmsWapMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BinaryBody(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Devices.Sms.ISmsWapMessage) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_MessageType(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageType: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CellularClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.CellularClass: ...
    @winrt_mixinmethod
    def get_MessageClass(self: Windows.Devices.Sms.ISmsMessageBase) -> Windows.Devices.Sms.SmsMessageClass: ...
    @winrt_mixinmethod
    def get_SimIccId(self: Windows.Devices.Sms.ISmsMessageBase) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    To = property(get_To, None)
    From = property(get_From, None)
    ApplicationId = property(get_ApplicationId, None)
    ContentType = property(get_ContentType, None)
    BinaryBody = property(get_BinaryBody, None)
    Headers = property(get_Headers, None)
    MessageType = property(get_MessageType, None)
    DeviceId = property(get_DeviceId, None)
    CellularClass = property(get_CellularClass, None)
    MessageClass = property(get_MessageClass, None)
    SimIccId = property(get_SimIccId, None)
make_head(_module, 'ISmsAppMessage')
make_head(_module, 'ISmsBroadcastMessage')
make_head(_module, 'ISmsDevice2')
make_head(_module, 'ISmsDevice2Statics')
make_head(_module, 'ISmsFilterRule')
make_head(_module, 'ISmsFilterRuleFactory')
make_head(_module, 'ISmsFilterRules')
make_head(_module, 'ISmsFilterRulesFactory')
make_head(_module, 'ISmsMessageBase')
make_head(_module, 'ISmsMessageReceivedTriggerDetails')
make_head(_module, 'ISmsMessageRegistration')
make_head(_module, 'ISmsMessageRegistrationStatics')
make_head(_module, 'ISmsSendMessageResult')
make_head(_module, 'ISmsStatusMessage')
make_head(_module, 'ISmsTextMessage2')
make_head(_module, 'ISmsVoicemailMessage')
make_head(_module, 'ISmsWapMessage')
make_head(_module, 'SmsAppMessage')
make_head(_module, 'SmsBroadcastMessage')
make_head(_module, 'SmsDevice2')
make_head(_module, 'SmsEncodedLength')
make_head(_module, 'SmsFilterRule')
make_head(_module, 'SmsFilterRules')
make_head(_module, 'SmsMessageReceivedTriggerDetails')
make_head(_module, 'SmsMessageRegistration')
make_head(_module, 'SmsSendMessageResult')
make_head(_module, 'SmsStatusMessage')
make_head(_module, 'SmsTextMessage2')
make_head(_module, 'SmsVoicemailMessage')
make_head(_module, 'SmsWapMessage')
