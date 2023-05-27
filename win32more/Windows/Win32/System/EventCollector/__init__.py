from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.EventCollector
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def EcSetSubscriptionProperty(Subscription: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetSubscriptionProperty(Subscription: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcSaveSubscription(Subscription: IntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcDeleteSubscription(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetObjectArraySize(ObjectArray: IntPtr, ObjectArraySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcSetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, ArrayIndex: UInt32, Flags: UInt32, PropertyValue: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetObjectArrayProperty(ObjectArray: IntPtr, PropertyId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID, ArrayIndex: UInt32, Flags: UInt32, PropertyValueBufferSize: UInt32, PropertyValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT_head), PropertyValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcInsertObjectArrayElement(ObjectArray: IntPtr, ArrayIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcRemoveObjectArrayElement(ObjectArray: IntPtr, ArrayIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcGetSubscriptionRunTimeStatus(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, StatusInfoId: win32more.Windows.Win32.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID, EventSourceName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, StatusValueBufferSize: UInt32, StatusValueBuffer: POINTER(win32more.Windows.Win32.System.EventCollector.EC_VARIANT_head), StatusValueBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcRetrySubscription(SubscriptionName: win32more.Windows.Win32.Foundation.PWSTR, EventSourceName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WecApi.dll')
def EcClose(Object: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
EC_SUBSCRIPTION_CONFIGURATION_MODE = Int32
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeNormal: EC_SUBSCRIPTION_CONFIGURATION_MODE = 0
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeCustom: EC_SUBSCRIPTION_CONFIGURATION_MODE = 1
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinLatency: EC_SUBSCRIPTION_CONFIGURATION_MODE = 2
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinBandwidth: EC_SUBSCRIPTION_CONFIGURATION_MODE = 3
EC_SUBSCRIPTION_CONTENT_FORMAT = Int32
EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatEvents: EC_SUBSCRIPTION_CONTENT_FORMAT = 1
EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatRenderedText: EC_SUBSCRIPTION_CONTENT_FORMAT = 2
EC_SUBSCRIPTION_CREDENTIALS_TYPE = Int32
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDefault: EC_SUBSCRIPTION_CREDENTIALS_TYPE = 0
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredNegotiate: EC_SUBSCRIPTION_CREDENTIALS_TYPE = 1
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDigest: EC_SUBSCRIPTION_CREDENTIALS_TYPE = 2
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredBasic: EC_SUBSCRIPTION_CREDENTIALS_TYPE = 3
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredLocalMachine: EC_SUBSCRIPTION_CREDENTIALS_TYPE = 4
EC_SUBSCRIPTION_DELIVERY_MODE = Int32
EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePull: EC_SUBSCRIPTION_DELIVERY_MODE = 1
EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePush: EC_SUBSCRIPTION_DELIVERY_MODE = 2
EC_SUBSCRIPTION_PROPERTY_ID = Int32
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEnabled: EC_SUBSCRIPTION_PROPERTY_ID = 0
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSources: EC_SUBSCRIPTION_PROPERTY_ID = 1
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceAddress: EC_SUBSCRIPTION_PROPERTY_ID = 2
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceEnabled: EC_SUBSCRIPTION_PROPERTY_ID = 3
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceUserName: EC_SUBSCRIPTION_PROPERTY_ID = 4
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourcePassword: EC_SUBSCRIPTION_PROPERTY_ID = 5
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDescription: EC_SUBSCRIPTION_PROPERTY_ID = 6
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionURI: EC_SUBSCRIPTION_PROPERTY_ID = 7
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionConfigurationMode: EC_SUBSCRIPTION_PROPERTY_ID = 8
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionExpires: EC_SUBSCRIPTION_PROPERTY_ID = 9
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionQuery: EC_SUBSCRIPTION_PROPERTY_ID = 10
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportName: EC_SUBSCRIPTION_PROPERTY_ID = 11
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportPort: EC_SUBSCRIPTION_PROPERTY_ID = 12
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMode: EC_SUBSCRIPTION_PROPERTY_ID = 13
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxItems: EC_SUBSCRIPTION_PROPERTY_ID = 14
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxLatencyTime: EC_SUBSCRIPTION_PROPERTY_ID = 15
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHeartbeatInterval: EC_SUBSCRIPTION_PROPERTY_ID = 16
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLocale: EC_SUBSCRIPTION_PROPERTY_ID = 17
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionContentFormat: EC_SUBSCRIPTION_PROPERTY_ID = 18
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLogFile: EC_SUBSCRIPTION_PROPERTY_ID = 19
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPublisherName: EC_SUBSCRIPTION_PROPERTY_ID = 20
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCredentialsType: EC_SUBSCRIPTION_PROPERTY_ID = 21
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonUserName: EC_SUBSCRIPTION_PROPERTY_ID = 22
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonPassword: EC_SUBSCRIPTION_PROPERTY_ID = 23
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHostName: EC_SUBSCRIPTION_PROPERTY_ID = 24
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionReadExistingEvents: EC_SUBSCRIPTION_PROPERTY_ID = 25
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDialect: EC_SUBSCRIPTION_PROPERTY_ID = 26
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionType: EC_SUBSCRIPTION_PROPERTY_ID = 27
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedIssuerCAs: EC_SUBSCRIPTION_PROPERTY_ID = 28
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSubjects: EC_SUBSCRIPTION_PROPERTY_ID = 29
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeniedSubjects: EC_SUBSCRIPTION_PROPERTY_ID = 30
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSourceDomainComputers: EC_SUBSCRIPTION_PROPERTY_ID = 31
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPropertyIdEND: EC_SUBSCRIPTION_PROPERTY_ID = 32
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = Int32
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusDisabled: EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 1
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusActive: EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 2
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusInactive: EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 3
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusTrying: EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = 4
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = Int32
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusActive: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 0
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastError: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 1
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorMessage: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 2
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorTime: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 3
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusNextRetryTime: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 4
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusEventSources: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 5
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastHeartbeatTime: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 6
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusInfoIdEND: EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = 7
EC_SUBSCRIPTION_TYPE = Int32
EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeSourceInitiated: EC_SUBSCRIPTION_TYPE = 0
EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeCollectorInitiated: EC_SUBSCRIPTION_TYPE = 1
class EC_VARIANT(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    Count: UInt32
    Type: UInt32
    class _Anonymous_e__Union(EasyCastUnion):
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
EC_VARIANT_TYPE_EcVarTypeNull: EC_VARIANT_TYPE = 0
EC_VARIANT_TYPE_EcVarTypeBoolean: EC_VARIANT_TYPE = 1
EC_VARIANT_TYPE_EcVarTypeUInt32: EC_VARIANT_TYPE = 2
EC_VARIANT_TYPE_EcVarTypeDateTime: EC_VARIANT_TYPE = 3
EC_VARIANT_TYPE_EcVarTypeString: EC_VARIANT_TYPE = 4
EC_VARIANT_TYPE_EcVarObjectArrayPropertyHandle: EC_VARIANT_TYPE = 5
make_head(_module, 'EC_VARIANT')
