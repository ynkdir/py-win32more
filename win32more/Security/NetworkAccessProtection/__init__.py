from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.NetworkAccessProtection
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
maxSoHAttributeCount = 100
maxSoHAttributeSize = 4000
minNetworkSoHSize = 12
maxNetworkSoHSize = 4000
maxStringLength = 1024
maxSystemHealthEntityCount = 20
maxEnforcerCount = 20
maxPrivateDataSize = 200
maxConnectionCountPerEnforcer = 20
freshSoHRequest = 1
shaFixup = 1
failureCategoryCount = 5
ComponentTypeEnforcementClientSoH = 1
ComponentTypeEnforcementClientRp = 2
percentageNotSupported = 101
def _define_CorrelationId_head():
    class CorrelationId(Structure):
        pass
    return CorrelationId
def _define_CorrelationId():
    CorrelationId = win32more.Security.NetworkAccessProtection.CorrelationId_head
    CorrelationId._fields_ = [
        ('connId', Guid),
        ('timeStamp', win32more.Foundation.FILETIME),
    ]
    return CorrelationId
def _define_CountedString_head():
    class CountedString(Structure):
        pass
    return CountedString
def _define_CountedString():
    CountedString = win32more.Security.NetworkAccessProtection.CountedString_head
    CountedString._fields_ = [
        ('length', UInt16),
        ('string', win32more.Foundation.PWSTR),
    ]
    return CountedString
ExtendedIsolationState = Int32
ExtendedIsolationState_extendedIsolationStateNoData = 0
ExtendedIsolationState_extendedIsolationStateTransition = 1
ExtendedIsolationState_extendedIsolationStateInfected = 2
ExtendedIsolationState_extendedIsolationStateUnknown = 3
FailureCategory = Int32
FailureCategory_failureCategoryNone = 0
FailureCategory_failureCategoryOther = 1
FailureCategory_failureCategoryClientComponent = 2
FailureCategory_failureCategoryClientCommunication = 3
FailureCategory_failureCategoryServerComponent = 4
FailureCategory_failureCategoryServerCommunication = 5
def _define_FailureCategoryMapping_head():
    class FailureCategoryMapping(Structure):
        pass
    return FailureCategoryMapping
def _define_FailureCategoryMapping():
    FailureCategoryMapping = win32more.Security.NetworkAccessProtection.FailureCategoryMapping_head
    FailureCategoryMapping._fields_ = [
        ('mappingCompliance', win32more.Foundation.BOOL * 5),
    ]
    return FailureCategoryMapping
def _define_FixupInfo_head():
    class FixupInfo(Structure):
        pass
    return FixupInfo
def _define_FixupInfo():
    FixupInfo = win32more.Security.NetworkAccessProtection.FixupInfo_head
    FixupInfo._fields_ = [
        ('state', win32more.Security.NetworkAccessProtection.FixupState),
        ('percentage', Byte),
        ('resultCodes', win32more.Security.NetworkAccessProtection.ResultCodes),
        ('fixupMsgId', UInt32),
    ]
    return FixupInfo
FixupState = Int32
FixupState_fixupStateSuccess = 0
FixupState_fixupStateInProgress = 1
FixupState_fixupStateCouldNotUpdate = 2
def _define_Ipv4Address_head():
    class Ipv4Address(Structure):
        pass
    return Ipv4Address
def _define_Ipv4Address():
    Ipv4Address = win32more.Security.NetworkAccessProtection.Ipv4Address_head
    Ipv4Address._fields_ = [
        ('addr', Byte * 4),
    ]
    return Ipv4Address
def _define_Ipv6Address_head():
    class Ipv6Address(Structure):
        pass
    return Ipv6Address
def _define_Ipv6Address():
    Ipv6Address = win32more.Security.NetworkAccessProtection.Ipv6Address_head
    Ipv6Address._fields_ = [
        ('addr', Byte * 16),
    ]
    return Ipv6Address
def _define_IsolationInfo_head():
    class IsolationInfo(Structure):
        pass
    return IsolationInfo
def _define_IsolationInfo():
    IsolationInfo = win32more.Security.NetworkAccessProtection.IsolationInfo_head
    IsolationInfo._fields_ = [
        ('isolationState', win32more.Security.NetworkAccessProtection.IsolationState),
        ('probEndTime', win32more.Foundation.FILETIME),
        ('failureUrl', win32more.Security.NetworkAccessProtection.CountedString),
    ]
    return IsolationInfo
def _define_IsolationInfoEx_head():
    class IsolationInfoEx(Structure):
        pass
    return IsolationInfoEx
def _define_IsolationInfoEx():
    IsolationInfoEx = win32more.Security.NetworkAccessProtection.IsolationInfoEx_head
    IsolationInfoEx._fields_ = [
        ('isolationState', win32more.Security.NetworkAccessProtection.IsolationState),
        ('extendedIsolationState', win32more.Security.NetworkAccessProtection.ExtendedIsolationState),
        ('probEndTime', win32more.Foundation.FILETIME),
        ('failureUrl', win32more.Security.NetworkAccessProtection.CountedString),
    ]
    return IsolationInfoEx
IsolationState = Int32
IsolationState_isolationStateNotRestricted = 1
IsolationState_isolationStateInProbation = 2
IsolationState_isolationStateRestrictedAccess = 3
def _define_NapComponentRegistrationInfo_head():
    class NapComponentRegistrationInfo(Structure):
        pass
    return NapComponentRegistrationInfo
def _define_NapComponentRegistrationInfo():
    NapComponentRegistrationInfo = win32more.Security.NetworkAccessProtection.NapComponentRegistrationInfo_head
    NapComponentRegistrationInfo._fields_ = [
        ('id', UInt32),
        ('friendlyName', win32more.Security.NetworkAccessProtection.CountedString),
        ('description', win32more.Security.NetworkAccessProtection.CountedString),
        ('version', win32more.Security.NetworkAccessProtection.CountedString),
        ('vendorName', win32more.Security.NetworkAccessProtection.CountedString),
        ('infoClsid', Guid),
        ('configClsid', Guid),
        ('registrationDate', win32more.Foundation.FILETIME),
        ('componentType', UInt32),
    ]
    return NapComponentRegistrationInfo
NapNotifyType = Int32
NapNotifyType_napNotifyTypeUnknown = 0
NapNotifyType_napNotifyTypeServiceState = 1
NapNotifyType_napNotifyTypeQuarState = 2
NapTracingLevel = Int32
NapTracingLevel_tracingLevelUndefined = 0
NapTracingLevel_tracingLevelBasic = 1
NapTracingLevel_tracingLevelAdvanced = 2
NapTracingLevel_tracingLevelDebug = 3
def _define_NetworkSoH_head():
    class NetworkSoH(Structure):
        pass
    return NetworkSoH
def _define_NetworkSoH():
    NetworkSoH = win32more.Security.NetworkAccessProtection.NetworkSoH_head
    NetworkSoH._fields_ = [
        ('size', UInt16),
        ('data', c_char_p_no),
    ]
    return NetworkSoH
def _define_PrivateData_head():
    class PrivateData(Structure):
        pass
    return PrivateData
def _define_PrivateData():
    PrivateData = win32more.Security.NetworkAccessProtection.PrivateData_head
    PrivateData._fields_ = [
        ('size', UInt16),
        ('data', c_char_p_no),
    ]
    return PrivateData
RemoteConfigurationType = Int32
RemoteConfigurationType_remoteConfigTypeMachine = 1
RemoteConfigurationType_remoteConfigTypeConfigBlob = 2
def _define_ResultCodes_head():
    class ResultCodes(Structure):
        pass
    return ResultCodes
def _define_ResultCodes():
    ResultCodes = win32more.Security.NetworkAccessProtection.ResultCodes_head
    ResultCodes._fields_ = [
        ('count', UInt16),
        ('results', POINTER(win32more.Foundation.HRESULT)),
    ]
    return ResultCodes
def _define_SoH_head():
    class SoH(Structure):
        pass
    return SoH
def _define_SoH():
    SoH = win32more.Security.NetworkAccessProtection.SoH_head
    SoH._fields_ = [
        ('count', UInt16),
        ('attributes', POINTER(win32more.Security.NetworkAccessProtection.SoHAttribute_head)),
    ]
    return SoH
def _define_SoHAttribute_head():
    class SoHAttribute(Structure):
        pass
    return SoHAttribute
def _define_SoHAttribute():
    SoHAttribute = win32more.Security.NetworkAccessProtection.SoHAttribute_head
    SoHAttribute._fields_ = [
        ('type', UInt16),
        ('size', UInt16),
        ('value', c_char_p_no),
    ]
    return SoHAttribute
def _define_SystemHealthAgentState_head():
    class SystemHealthAgentState(Structure):
        pass
    return SystemHealthAgentState
def _define_SystemHealthAgentState():
    SystemHealthAgentState = win32more.Security.NetworkAccessProtection.SystemHealthAgentState_head
    SystemHealthAgentState._fields_ = [
        ('id', UInt32),
        ('shaResultCodes', win32more.Security.NetworkAccessProtection.ResultCodes),
        ('failureCategory', win32more.Security.NetworkAccessProtection.FailureCategory),
        ('fixupInfo', win32more.Security.NetworkAccessProtection.FixupInfo),
    ]
    return SystemHealthAgentState
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
