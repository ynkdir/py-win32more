from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.NetworkAccessProtection
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
    timeStamp: win32more.Windows.Win32.Foundation.FILETIME
class CountedString(EasyCastStructure):
    length: UInt16
    string: win32more.Windows.Win32.Foundation.PWSTR
ExtendedIsolationState = Int32
ExtendedIsolationState_extendedIsolationStateNoData: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 0
ExtendedIsolationState_extendedIsolationStateTransition: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 1
ExtendedIsolationState_extendedIsolationStateInfected: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 2
ExtendedIsolationState_extendedIsolationStateUnknown: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 3
FailureCategory = Int32
FailureCategory_failureCategoryNone: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 0
FailureCategory_failureCategoryOther: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 1
FailureCategory_failureCategoryClientComponent: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 2
FailureCategory_failureCategoryClientCommunication: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 3
FailureCategory_failureCategoryServerComponent: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 4
FailureCategory_failureCategoryServerCommunication: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 5
class FailureCategoryMapping(EasyCastStructure):
    mappingCompliance: win32more.Windows.Win32.Foundation.BOOL * 5
class FixupInfo(EasyCastStructure):
    state: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState
    percentage: Byte
    resultCodes: win32more.Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    fixupMsgId: UInt32
FixupState = Int32
FixupState_fixupStateSuccess: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 0
FixupState_fixupStateInProgress: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 1
FixupState_fixupStateCouldNotUpdate: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 2
class Ipv4Address(EasyCastStructure):
    addr: Byte * 4
class Ipv6Address(EasyCastStructure):
    addr: Byte * 16
class IsolationInfo(EasyCastStructure):
    isolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState
    probEndTime: win32more.Windows.Win32.Foundation.FILETIME
    failureUrl: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
class IsolationInfoEx(EasyCastStructure):
    isolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState
    extendedIsolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState
    probEndTime: win32more.Windows.Win32.Foundation.FILETIME
    failureUrl: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
IsolationState = Int32
IsolationState_isolationStateNotRestricted: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 1
IsolationState_isolationStateInProbation: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 2
IsolationState_isolationStateRestrictedAccess: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 3
class NapComponentRegistrationInfo(EasyCastStructure):
    id: UInt32
    friendlyName: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
    description: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
    version: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
    vendorName: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
    infoClsid: Guid
    configClsid: Guid
    registrationDate: win32more.Windows.Win32.Foundation.FILETIME
    componentType: UInt32
NapNotifyType = Int32
NapNotifyType_napNotifyTypeUnknown: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 0
NapNotifyType_napNotifyTypeServiceState: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 1
NapNotifyType_napNotifyTypeQuarState: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 2
NapTracingLevel = Int32
NapTracingLevel_tracingLevelUndefined: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 0
NapTracingLevel_tracingLevelBasic: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 1
NapTracingLevel_tracingLevelAdvanced: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 2
NapTracingLevel_tracingLevelDebug: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 3
class NetworkSoH(EasyCastStructure):
    size: UInt16
    data: POINTER(Byte)
class PrivateData(EasyCastStructure):
    size: UInt16
    data: POINTER(Byte)
RemoteConfigurationType = Int32
RemoteConfigurationType_remoteConfigTypeMachine: win32more.Windows.Win32.Security.NetworkAccessProtection.RemoteConfigurationType = 1
RemoteConfigurationType_remoteConfigTypeConfigBlob: win32more.Windows.Win32.Security.NetworkAccessProtection.RemoteConfigurationType = 2
class ResultCodes(EasyCastStructure):
    count: UInt16
    results: POINTER(win32more.Windows.Win32.Foundation.HRESULT)
class SoH(EasyCastStructure):
    count: UInt16
    attributes: POINTER(win32more.Windows.Win32.Security.NetworkAccessProtection.SoHAttribute)
class SoHAttribute(EasyCastStructure):
    type: UInt16
    size: UInt16
    value: POINTER(Byte)
class SystemHealthAgentState(EasyCastStructure):
    id: UInt32
    shaResultCodes: win32more.Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    failureCategory: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory
    fixupInfo: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupInfo


make_ready(__name__)
