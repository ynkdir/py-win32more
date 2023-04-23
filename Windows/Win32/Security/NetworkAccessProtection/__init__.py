from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Security.NetworkAccessProtection
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
class CorrelationId(EasyCastStructure):
    connId: Guid
    timeStamp: Windows.Win32.Foundation.FILETIME
class CountedString(EasyCastStructure):
    length: UInt16
    string: Windows.Win32.Foundation.PWSTR
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
class FailureCategoryMapping(EasyCastStructure):
    mappingCompliance: Windows.Win32.Foundation.BOOL * 5
class FixupInfo(EasyCastStructure):
    state: Windows.Win32.Security.NetworkAccessProtection.FixupState
    percentage: Byte
    resultCodes: Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    fixupMsgId: UInt32
FixupState = Int32
FixupState_fixupStateSuccess: FixupState = 0
FixupState_fixupStateInProgress: FixupState = 1
FixupState_fixupStateCouldNotUpdate: FixupState = 2
class Ipv4Address(EasyCastStructure):
    addr: Byte * 4
class Ipv6Address(EasyCastStructure):
    addr: Byte * 16
class IsolationInfo(EasyCastStructure):
    isolationState: Windows.Win32.Security.NetworkAccessProtection.IsolationState
    probEndTime: Windows.Win32.Foundation.FILETIME
    failureUrl: Windows.Win32.Security.NetworkAccessProtection.CountedString
class IsolationInfoEx(EasyCastStructure):
    isolationState: Windows.Win32.Security.NetworkAccessProtection.IsolationState
    extendedIsolationState: Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState
    probEndTime: Windows.Win32.Foundation.FILETIME
    failureUrl: Windows.Win32.Security.NetworkAccessProtection.CountedString
IsolationState = Int32
IsolationState_isolationStateNotRestricted: IsolationState = 1
IsolationState_isolationStateInProbation: IsolationState = 2
IsolationState_isolationStateRestrictedAccess: IsolationState = 3
class NapComponentRegistrationInfo(EasyCastStructure):
    id: UInt32
    friendlyName: Windows.Win32.Security.NetworkAccessProtection.CountedString
    description: Windows.Win32.Security.NetworkAccessProtection.CountedString
    version: Windows.Win32.Security.NetworkAccessProtection.CountedString
    vendorName: Windows.Win32.Security.NetworkAccessProtection.CountedString
    infoClsid: Guid
    configClsid: Guid
    registrationDate: Windows.Win32.Foundation.FILETIME
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
class NetworkSoH(EasyCastStructure):
    size: UInt16
    data: POINTER(Byte)
class PrivateData(EasyCastStructure):
    size: UInt16
    data: POINTER(Byte)
RemoteConfigurationType = Int32
RemoteConfigurationType_remoteConfigTypeMachine: RemoteConfigurationType = 1
RemoteConfigurationType_remoteConfigTypeConfigBlob: RemoteConfigurationType = 2
class ResultCodes(EasyCastStructure):
    count: UInt16
    results: POINTER(Windows.Win32.Foundation.HRESULT)
class SoH(EasyCastStructure):
    count: UInt16
    attributes: POINTER(Windows.Win32.Security.NetworkAccessProtection.SoHAttribute_head)
class SoHAttribute(EasyCastStructure):
    type: UInt16
    size: UInt16
    value: POINTER(Byte)
class SystemHealthAgentState(EasyCastStructure):
    id: UInt32
    shaResultCodes: Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    failureCategory: Windows.Win32.Security.NetworkAccessProtection.FailureCategory
    fixupInfo: Windows.Win32.Security.NetworkAccessProtection.FixupInfo
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
