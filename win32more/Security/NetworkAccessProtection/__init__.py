from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.NetworkAccessProtection
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
maxSoHAttributeCount: UInt32 = 100
maxSoHAttributeSize: UInt32 = 4000
minNetworkSoHSize: UInt32 = 12
maxNetworkSoHSize: UInt32 = 4000
maxStringLength: UInt32 = 1024
maxSystemHealthEntityCount: UInt32 = 20
maxEnforcerCount: UInt32 = 20
maxPrivateDataSize: UInt32 = 200
maxConnectionCountPerEnforcer: UInt32 = 20
freshSoHRequest: UInt32 = 1
shaFixup: UInt32 = 1
failureCategoryCount: UInt32 = 5
ComponentTypeEnforcementClientSoH: UInt32 = 1
ComponentTypeEnforcementClientRp: UInt32 = 2
percentageNotSupported: UInt32 = 101
class CorrelationId(Structure):
    connId: Guid
    timeStamp: win32more.Foundation.FILETIME
class CountedString(Structure):
    length: UInt16
    string: win32more.Foundation.PWSTR
ExtendedIsolationState = Int32
ExtendedIsolationState_extendedIsolationStateNoData: ExtendedIsolationState = 0
ExtendedIsolationState_extendedIsolationStateTransition: ExtendedIsolationState = 1
ExtendedIsolationState_extendedIsolationStateInfected: ExtendedIsolationState = 2
ExtendedIsolationState_extendedIsolationStateUnknown: ExtendedIsolationState = 3
FailureCategory = Int32
FailureCategory_failureCategoryNone: FailureCategory = 0
FailureCategory_failureCategoryOther: FailureCategory = 1
FailureCategory_failureCategoryClientComponent: FailureCategory = 2
FailureCategory_failureCategoryClientCommunication: FailureCategory = 3
FailureCategory_failureCategoryServerComponent: FailureCategory = 4
FailureCategory_failureCategoryServerCommunication: FailureCategory = 5
class FailureCategoryMapping(Structure):
    mappingCompliance: win32more.Foundation.BOOL * 5
class FixupInfo(Structure):
    state: win32more.Security.NetworkAccessProtection.FixupState
    percentage: Byte
    resultCodes: win32more.Security.NetworkAccessProtection.ResultCodes
    fixupMsgId: UInt32
FixupState = Int32
FixupState_fixupStateSuccess: FixupState = 0
FixupState_fixupStateInProgress: FixupState = 1
FixupState_fixupStateCouldNotUpdate: FixupState = 2
class Ipv4Address(Structure):
    addr: Byte * 4
class Ipv6Address(Structure):
    addr: Byte * 16
class IsolationInfo(Structure):
    isolationState: win32more.Security.NetworkAccessProtection.IsolationState
    probEndTime: win32more.Foundation.FILETIME
    failureUrl: win32more.Security.NetworkAccessProtection.CountedString
class IsolationInfoEx(Structure):
    isolationState: win32more.Security.NetworkAccessProtection.IsolationState
    extendedIsolationState: win32more.Security.NetworkAccessProtection.ExtendedIsolationState
    probEndTime: win32more.Foundation.FILETIME
    failureUrl: win32more.Security.NetworkAccessProtection.CountedString
IsolationState = Int32
IsolationState_isolationStateNotRestricted: IsolationState = 1
IsolationState_isolationStateInProbation: IsolationState = 2
IsolationState_isolationStateRestrictedAccess: IsolationState = 3
class NapComponentRegistrationInfo(Structure):
    id: UInt32
    friendlyName: win32more.Security.NetworkAccessProtection.CountedString
    description: win32more.Security.NetworkAccessProtection.CountedString
    version: win32more.Security.NetworkAccessProtection.CountedString
    vendorName: win32more.Security.NetworkAccessProtection.CountedString
    infoClsid: Guid
    configClsid: Guid
    registrationDate: win32more.Foundation.FILETIME
    componentType: UInt32
NapNotifyType = Int32
NapNotifyType_napNotifyTypeUnknown: NapNotifyType = 0
NapNotifyType_napNotifyTypeServiceState: NapNotifyType = 1
NapNotifyType_napNotifyTypeQuarState: NapNotifyType = 2
NapTracingLevel = Int32
NapTracingLevel_tracingLevelUndefined: NapTracingLevel = 0
NapTracingLevel_tracingLevelBasic: NapTracingLevel = 1
NapTracingLevel_tracingLevelAdvanced: NapTracingLevel = 2
NapTracingLevel_tracingLevelDebug: NapTracingLevel = 3
class NetworkSoH(Structure):
    size: UInt16
    data: c_char_p_no
class PrivateData(Structure):
    size: UInt16
    data: c_char_p_no
RemoteConfigurationType = Int32
RemoteConfigurationType_remoteConfigTypeMachine: RemoteConfigurationType = 1
RemoteConfigurationType_remoteConfigTypeConfigBlob: RemoteConfigurationType = 2
class ResultCodes(Structure):
    count: UInt16
    results: POINTER(win32more.Foundation.HRESULT)
class SoH(Structure):
    count: UInt16
    attributes: POINTER(win32more.Security.NetworkAccessProtection.SoHAttribute_head)
class SoHAttribute(Structure):
    type: UInt16
    size: UInt16
    value: c_char_p_no
class SystemHealthAgentState(Structure):
    id: UInt32
    shaResultCodes: win32more.Security.NetworkAccessProtection.ResultCodes
    failureCategory: win32more.Security.NetworkAccessProtection.FailureCategory
    fixupInfo: win32more.Security.NetworkAccessProtection.FixupInfo
make_head(_module, 'CorrelationId')
make_head(_module, 'CountedString')
make_head(_module, 'FailureCategoryMapping')
make_head(_module, 'FixupInfo')
make_head(_module, 'Ipv4Address')
make_head(_module, 'Ipv6Address')
make_head(_module, 'IsolationInfo')
make_head(_module, 'IsolationInfoEx')
make_head(_module, 'NapComponentRegistrationInfo')
make_head(_module, 'NetworkSoH')
make_head(_module, 'PrivateData')
make_head(_module, 'ResultCodes')
make_head(_module, 'SoH')
make_head(_module, 'SoHAttribute')
make_head(_module, 'SystemHealthAgentState')
__all__ = [
    "ComponentTypeEnforcementClientRp",
    "ComponentTypeEnforcementClientSoH",
    "CorrelationId",
    "CountedString",
    "ExtendedIsolationState",
    "ExtendedIsolationState_extendedIsolationStateInfected",
    "ExtendedIsolationState_extendedIsolationStateNoData",
    "ExtendedIsolationState_extendedIsolationStateTransition",
    "ExtendedIsolationState_extendedIsolationStateUnknown",
    "FailureCategory",
    "FailureCategoryMapping",
    "FailureCategory_failureCategoryClientCommunication",
    "FailureCategory_failureCategoryClientComponent",
    "FailureCategory_failureCategoryNone",
    "FailureCategory_failureCategoryOther",
    "FailureCategory_failureCategoryServerCommunication",
    "FailureCategory_failureCategoryServerComponent",
    "FixupInfo",
    "FixupState",
    "FixupState_fixupStateCouldNotUpdate",
    "FixupState_fixupStateInProgress",
    "FixupState_fixupStateSuccess",
    "Ipv4Address",
    "Ipv6Address",
    "IsolationInfo",
    "IsolationInfoEx",
    "IsolationState",
    "IsolationState_isolationStateInProbation",
    "IsolationState_isolationStateNotRestricted",
    "IsolationState_isolationStateRestrictedAccess",
    "NapComponentRegistrationInfo",
    "NapNotifyType",
    "NapNotifyType_napNotifyTypeQuarState",
    "NapNotifyType_napNotifyTypeServiceState",
    "NapNotifyType_napNotifyTypeUnknown",
    "NapTracingLevel",
    "NapTracingLevel_tracingLevelAdvanced",
    "NapTracingLevel_tracingLevelBasic",
    "NapTracingLevel_tracingLevelDebug",
    "NapTracingLevel_tracingLevelUndefined",
    "NetworkSoH",
    "PrivateData",
    "RemoteConfigurationType",
    "RemoteConfigurationType_remoteConfigTypeConfigBlob",
    "RemoteConfigurationType_remoteConfigTypeMachine",
    "ResultCodes",
    "SoH",
    "SoHAttribute",
    "SystemHealthAgentState",
    "failureCategoryCount",
    "freshSoHRequest",
    "maxConnectionCountPerEnforcer",
    "maxEnforcerCount",
    "maxNetworkSoHSize",
    "maxPrivateDataSize",
    "maxSoHAttributeCount",
    "maxSoHAttributeSize",
    "maxStringLength",
    "maxSystemHealthEntityCount",
    "minNetworkSoHSize",
    "percentageNotSupported",
    "shaFixup",
]
_arch_optional = [
]
