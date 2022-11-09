from win32more.base import *
import win32more.Foundation
import win32more.System.EventCollector

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
EC_VARIANT_TYPE_MASK = 127
EC_VARIANT_TYPE_ARRAY = 128
EC_READ_ACCESS = 1
EC_WRITE_ACCESS = 2
EC_OPEN_ALWAYS = 0
EC_CREATE_NEW = 1
EC_OPEN_EXISTING = 2
EC_SUBSCRIPTION_PROPERTY_ID = Int32
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEnabled = 0
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSources = 1
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceAddress = 2
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceEnabled = 3
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceUserName = 4
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourcePassword = 5
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDescription = 6
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionURI = 7
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionConfigurationMode = 8
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionExpires = 9
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionQuery = 10
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportName = 11
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportPort = 12
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMode = 13
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxItems = 14
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxLatencyTime = 15
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHeartbeatInterval = 16
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLocale = 17
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionContentFormat = 18
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLogFile = 19
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPublisherName = 20
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCredentialsType = 21
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonUserName = 22
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonPassword = 23
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHostName = 24
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionReadExistingEvents = 25
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDialect = 26
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionType = 27
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedIssuerCAs = 28
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSubjects = 29
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeniedSubjects = 30
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSourceDomainComputers = 31
EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPropertyIdEND = 32
EC_SUBSCRIPTION_CREDENTIALS_TYPE = Int32
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDefault = 0
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredNegotiate = 1
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDigest = 2
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredBasic = 3
EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredLocalMachine = 4
EC_SUBSCRIPTION_TYPE = Int32
EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeSourceInitiated = 0
EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeCollectorInitiated = 1
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = Int32
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusActive = 0
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastError = 1
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorMessage = 2
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorTime = 3
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusNextRetryTime = 4
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusEventSources = 5
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastHeartbeatTime = 6
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusInfoIdEND = 7
EC_VARIANT_TYPE = Int32
EC_VARIANT_TYPE_EcVarTypeNull = 0
EC_VARIANT_TYPE_EcVarTypeBoolean = 1
EC_VARIANT_TYPE_EcVarTypeUInt32 = 2
EC_VARIANT_TYPE_EcVarTypeDateTime = 3
EC_VARIANT_TYPE_EcVarTypeString = 4
EC_VARIANT_TYPE_EcVarObjectArrayPropertyHandle = 5
def _define_EC_VARIANT_head():
    class EC_VARIANT(Structure):
        pass
    return EC_VARIANT
def _define_EC_VARIANT():
    EC_VARIANT = win32more.System.EventCollector.EC_VARIANT_head
    class EC_VARIANT__Anonymous_e__Union(Union):
        pass
    EC_VARIANT__Anonymous_e__Union._fields_ = [
        ("BooleanVal", win32more.Foundation.BOOL),
        ("UInt32Val", UInt32),
        ("DateTimeVal", UInt64),
        ("StringVal", win32more.Foundation.PWSTR),
        ("BinaryVal", c_char_p_no),
        ("BooleanArr", POINTER(win32more.Foundation.BOOL)),
        ("Int32Arr", POINTER(Int32)),
        ("StringArr", POINTER(win32more.Foundation.PWSTR)),
        ("PropertyHandleVal", IntPtr),
    ]
    EC_VARIANT._anonymous_ = [
        'Anonymous',
    ]
    EC_VARIANT._fields_ = [
        ("Anonymous", EC_VARIANT__Anonymous_e__Union),
        ("Count", UInt32),
        ("Type", UInt32),
    ]
    return EC_VARIANT
EC_SUBSCRIPTION_CONFIGURATION_MODE = Int32
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeNormal = 0
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeCustom = 1
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinLatency = 2
EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinBandwidth = 3
EC_SUBSCRIPTION_DELIVERY_MODE = Int32
EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePull = 1
EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePush = 2
EC_SUBSCRIPTION_CONTENT_FORMAT = Int32
EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatEvents = 1
EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatRenderedText = 2
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS = Int32
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusDisabled = 1
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusActive = 2
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusInactive = 3
EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusTrying = 4
def _define_EcOpenSubscriptionEnum():
    try:
        return WINFUNCTYPE(IntPtr,UInt32, use_last_error=True)(("EcOpenSubscriptionEnum", windll["WecApi"]), ((1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcEnumNextSubscription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(("EcEnumNextSubscription", windll["WecApi"]), ((1, 'SubscriptionEnum'),(1, 'SubscriptionNameBufferSize'),(1, 'SubscriptionNameBuffer'),(1, 'SubscriptionNameBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcOpenSubscription():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=True)(("EcOpenSubscription", windll["WecApi"]), ((1, 'SubscriptionName'),(1, 'AccessMask'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcSetSubscriptionProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID,UInt32,POINTER(win32more.System.EventCollector.EC_VARIANT_head), use_last_error=False)(("EcSetSubscriptionProperty", windll["WecApi"]), ((1, 'Subscription'),(1, 'PropertyId'),(1, 'Flags'),(1, 'PropertyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcGetSubscriptionProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID,UInt32,UInt32,POINTER(win32more.System.EventCollector.EC_VARIANT_head),POINTER(UInt32), use_last_error=False)(("EcGetSubscriptionProperty", windll["WecApi"]), ((1, 'Subscription'),(1, 'PropertyId'),(1, 'Flags'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcSaveSubscription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32, use_last_error=False)(("EcSaveSubscription", windll["WecApi"]), ((1, 'Subscription'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcDeleteSubscription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("EcDeleteSubscription", windll["WecApi"]), ((1, 'SubscriptionName'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcGetObjectArraySize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(UInt32), use_last_error=False)(("EcGetObjectArraySize", windll["WecApi"]), ((1, 'ObjectArray'),(1, 'ObjectArraySize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcSetObjectArrayProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID,UInt32,UInt32,POINTER(win32more.System.EventCollector.EC_VARIANT_head), use_last_error=False)(("EcSetObjectArrayProperty", windll["WecApi"]), ((1, 'ObjectArray'),(1, 'PropertyId'),(1, 'ArrayIndex'),(1, 'Flags'),(1, 'PropertyValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcGetObjectArrayProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,win32more.System.EventCollector.EC_SUBSCRIPTION_PROPERTY_ID,UInt32,UInt32,UInt32,POINTER(win32more.System.EventCollector.EC_VARIANT_head),POINTER(UInt32), use_last_error=False)(("EcGetObjectArrayProperty", windll["WecApi"]), ((1, 'ObjectArray'),(1, 'PropertyId'),(1, 'ArrayIndex'),(1, 'Flags'),(1, 'PropertyValueBufferSize'),(1, 'PropertyValueBuffer'),(1, 'PropertyValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcInsertObjectArrayElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32, use_last_error=False)(("EcInsertObjectArrayElement", windll["WecApi"]), ((1, 'ObjectArray'),(1, 'ArrayIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcRemoveObjectArrayElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32, use_last_error=False)(("EcRemoveObjectArrayElement", windll["WecApi"]), ((1, 'ObjectArray'),(1, 'ArrayIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcGetSubscriptionRunTimeStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.System.EventCollector.EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.EventCollector.EC_VARIANT_head),POINTER(UInt32), use_last_error=False)(("EcGetSubscriptionRunTimeStatus", windll["WecApi"]), ((1, 'SubscriptionName'),(1, 'StatusInfoId'),(1, 'EventSourceName'),(1, 'Flags'),(1, 'StatusValueBufferSize'),(1, 'StatusValueBuffer'),(1, 'StatusValueBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcRetrySubscription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("EcRetrySubscription", windll["WecApi"]), ((1, 'SubscriptionName'),(1, 'EventSourceName'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EcClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("EcClose", windll["WecApi"]), ((1, 'Object'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "EC_VARIANT_TYPE_MASK",
    "EC_VARIANT_TYPE_ARRAY",
    "EC_READ_ACCESS",
    "EC_WRITE_ACCESS",
    "EC_OPEN_ALWAYS",
    "EC_CREATE_NEW",
    "EC_OPEN_EXISTING",
    "EC_SUBSCRIPTION_PROPERTY_ID",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEnabled",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSources",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceAddress",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceEnabled",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourceUserName",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionEventSourcePassword",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDescription",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionURI",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionConfigurationMode",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionExpires",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionQuery",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportName",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionTransportPort",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMode",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxItems",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeliveryMaxLatencyTime",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHeartbeatInterval",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLocale",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionContentFormat",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionLogFile",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPublisherName",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCredentialsType",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonUserName",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionCommonPassword",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionHostName",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionReadExistingEvents",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDialect",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionType",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedIssuerCAs",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSubjects",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionDeniedSubjects",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionAllowedSourceDomainComputers",
    "EC_SUBSCRIPTION_PROPERTY_ID_EcSubscriptionPropertyIdEND",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDefault",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredNegotiate",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredDigest",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredBasic",
    "EC_SUBSCRIPTION_CREDENTIALS_TYPE_EcSubscriptionCredLocalMachine",
    "EC_SUBSCRIPTION_TYPE",
    "EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeSourceInitiated",
    "EC_SUBSCRIPTION_TYPE_EcSubscriptionTypeCollectorInitiated",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusActive",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastError",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorMessage",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastErrorTime",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusNextRetryTime",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusEventSources",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusLastHeartbeatTime",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_EcSubscriptionRunTimeStatusInfoIdEND",
    "EC_VARIANT_TYPE",
    "EC_VARIANT_TYPE_EcVarTypeNull",
    "EC_VARIANT_TYPE_EcVarTypeBoolean",
    "EC_VARIANT_TYPE_EcVarTypeUInt32",
    "EC_VARIANT_TYPE_EcVarTypeDateTime",
    "EC_VARIANT_TYPE_EcVarTypeString",
    "EC_VARIANT_TYPE_EcVarObjectArrayPropertyHandle",
    "EC_VARIANT",
    "EC_SUBSCRIPTION_CONFIGURATION_MODE",
    "EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeNormal",
    "EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeCustom",
    "EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinLatency",
    "EC_SUBSCRIPTION_CONFIGURATION_MODE_EcConfigurationModeMinBandwidth",
    "EC_SUBSCRIPTION_DELIVERY_MODE",
    "EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePull",
    "EC_SUBSCRIPTION_DELIVERY_MODE_EcDeliveryModePush",
    "EC_SUBSCRIPTION_CONTENT_FORMAT",
    "EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatEvents",
    "EC_SUBSCRIPTION_CONTENT_FORMAT_EcContentFormatRenderedText",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusDisabled",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusActive",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusInactive",
    "EC_SUBSCRIPTION_RUNTIME_STATUS_ACTIVE_STATUS_EcRuntimeStatusActiveStatusTrying",
    "EcOpenSubscriptionEnum",
    "EcEnumNextSubscription",
    "EcOpenSubscription",
    "EcSetSubscriptionProperty",
    "EcGetSubscriptionProperty",
    "EcSaveSubscription",
    "EcDeleteSubscription",
    "EcGetObjectArraySize",
    "EcSetObjectArrayProperty",
    "EcGetObjectArrayProperty",
    "EcInsertObjectArrayElement",
    "EcRemoveObjectArrayElement",
    "EcGetSubscriptionRunTimeStatus",
    "EcRetrySubscription",
    "EcClose",
]
