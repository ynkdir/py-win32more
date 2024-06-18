from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.EventCollector
EC_VARIANT_TYPE_MASK: UInt32 = 127
EC_VARIANT_TYPE_ARRAY: UInt32 = 128
EC_READ_ACCESS: UInt32 = 1
EC_WRITE_ACCESS: UInt32 = 2
EC_OPEN_ALWAYS: UInt32 = 0
EC_CREATE_NEW: UInt32 = 1
EC_OPEN_EXISTING: UInt32 = 2
@winfunctype('WecApi.dll')
def EcOpenSubscriptionEnum(Flags: UInt32) -> IntPtr: ...
@winfunctype('WecApi.dll')
def EcEnumNextSubscription(SubscriptionEnum: IntPtr, SubscriptionNameBufferSize: UInt32, SubscriptionNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, SubscriptionNameBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcOpenSubscription(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, AccessMask: UInt32, Flags: UInt32) -> IntPtr: ...
@winfunctype('WecApi.dll')
def EcSetSubscriptionProperty(Subscription: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetSubscriptionProperty(Subscription: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcSaveSubscription(Subscription: IntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcDeleteSubscription(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetObjectArraySize(ObjectArray: IntPtr, ObjectArraySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcSetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, ArrayIndex: UInt32, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, ArrayIndex: UInt32, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcInsertObjectArrayElement(ObjectArray: IntPtr, ArrayIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcRemoveObjectArrayElement(ObjectArray: IntPtr, ArrayIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetSubscriptionRunTimeStatus(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, StatusInfoId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID, EventSourceName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, StatusValueBufferSize: UInt32, StatusValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT), StatusValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcRetrySubscription(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, EventSourceName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcClose(Object: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
EC_SUBSCRIPTION_CONFIGURATION_MODE = Int32
EcConfigurationModeNormal: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONFIGURATION_MODE = 0
EcConfigurationModeCustom: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONFIGURATION_MODE = 1
EcConfigurationModeMinLatency: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONFIGURATION_MODE = 2
EcConfigurationModeMinBandwidth: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONFIGURATION_MODE = 3
EC_SUBSCRIPTION_CONTENT_FORMAT = Int32
EcContentFormatEvents: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONTENT_FORMAT = 1
EcContentFormatRenderedText: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CONTENT_FORMAT = 2
EC_SUBSCRIPTION_CREDENTIALS_TYPE = Int32
EcSubscriptionCredDefault: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CREDENTIALS_TYPE = 0
EcSubscriptionCredNegotiate: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CREDENTIALS_TYPE = 1
EcSubscriptionCredDigest: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CREDENTIALS_TYPE = 2
EcSubscriptionCredBasic: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CREDENTIALS_TYPE = 3
EcSubscriptionCredLocalMachine: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_CREDENTIALS_TYPE = 4
EC_SUBSCRIPTION_DELIVERY_MODE = Int32
EcDeliveryModePull: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_DELIVERY_MODE = 1
EcDeliveryModePush: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_DELIVERY_MODE = 2
EC_SUBSCRIPTION_PROPERTY_ID = Int32
EcSubscriptionEnabled: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 0
EcSubscriptionEventSources: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 1
EcSubscriptionEventSourceAddress: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 2
EcSubscriptionEventSourceEnabled: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 3
EcSubscriptionEventSourceUserName: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 4
EcSubscriptionEventSourcePassword: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 5
EcSubscriptionDescription: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 6
EcSubscriptionURI: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 7
EcSubscriptionConfigurationMode: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 8
EcSubscriptionExpires: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 9
EcSubscriptionQuery: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 10
EcSubscriptionTransportName: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 11
EcSubscriptionTransportPort: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 12
EcSubscriptionDeliveryMode: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 13
EcSubscriptionDeliveryMaxItems: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 14
EcSubscriptionDeliveryMaxLatencyTime: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 15
EcSubscriptionHeartbeatInterval: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 16
EcSubscriptionLocale: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 17
EcSubscriptionContentFormat: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 18
EcSubscriptionLogFile: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 19
EcSubscriptionPublisherName: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 20
EcSubscriptionCredentialsType: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 21
EcSubscriptionCommonUserName: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 22
EcSubscriptionCommonPassword: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 23
EcSubscriptionHostName: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 24
EcSubscriptionReadExistingEvents: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 25
EcSubscriptionDialect: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 26
EcSubscriptionType: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 27
EcSubscriptionAllowedIssuerCAs: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 28
EcSubscriptionAllowedSubjects: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 29
EcSubscriptionDeniedSubjects: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 30
EcSubscriptionAllowedSourceDomainComputers: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 31
EcSubscriptionPropertyIdEND: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID = 32
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = Int32
EcRuntimeStatusActiveStatusDisabled: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 1
EcRuntimeStatusActiveStatusActive: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 2
EcRuntimeStatusActiveStatusInactive: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 3
EcRuntimeStatusActiveStatusTrying: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 4
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = Int32
EcSubscriptionRunTimeStatusActive: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 0
EcSubscriptionRunTimeStatusLastError: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 1
EcSubscriptionRunTimeStatusLastErrorMessage: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 2
EcSubscriptionRunTimeStatusLastErrorTime: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 3
EcSubscriptionRunTimeStatusNextRetryTime: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 4
EcSubscriptionRunTimeStatusEventSources: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 5
EcSubscriptionRunTimeStatusLastHeartbeatTime: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 6
EcSubscriptionRunTimeStatusInfoIdEND: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 7
EC_SUBSCRIPTION_TYPE = Int32
EcSubscriptionTypeSourceInitiated: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_TYPE = 0
EcSubscriptionTypeCollectorInitiated: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_TYPE = 1
class EC_VARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    Count: UInt32
    Type: UInt32
    class _Anonymous_e__Union(Union):
        BooleanVal: win32more.Windows.Win32.Foundation.BOOL
        UInt32Val: UInt32
        DateTimeVal: UInt64
        StringVal: win32more.Windows.Win32.Foundation.PWSTR
        BinaryVal: POINTER(Byte)
        BooleanArr: POINTER(win32more.Windows.Win32.Foundation.BOOL)
        Int32Arr: POINTER(Int32)
        StringArr: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        PropertyHandleVal: IntPtr
EC_VARIANT_TYPE = Int32
EcVarTypeNull: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 0
EcVarTypeBoolean: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 1
EcVarTypeUInt32: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 2
EcVarTypeDateTime: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 3
EcVarTypeString: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 4
EcVarObjectArrayPropertyHandle: win32more.Windows.Win32.System.EventCollector.EC_VARIANT_TYPE = 5


make_ready(__name__)
