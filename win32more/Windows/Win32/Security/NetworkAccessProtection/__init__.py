from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
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
class CorrelationId(Structure):
    connId: Guid
    timeStamp: win32more.Windows.Win32.Foundation.FILETIME
class CountedString(Structure):
    length: UInt16
    string: win32more.Windows.Win32.Foundation.PWSTR
ExtendedIsolationState = Int32
extendedIsolationStateNoData: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 0
extendedIsolationStateTransition: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 1
extendedIsolationStateInfected: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 2
extendedIsolationStateUnknown: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState = 3
FailureCategory = Int32
failureCategoryNone: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 0
failureCategoryOther: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 1
failureCategoryClientComponent: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 2
failureCategoryClientCommunication: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 3
failureCategoryServerComponent: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 4
failureCategoryServerCommunication: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory = 5
class FailureCategoryMapping(Structure):
    mappingCompliance: win32more.Windows.Win32.Foundation.BOOL * 5
class FixupInfo(Structure):
    state: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState
    percentage: Byte
    resultCodes: win32more.Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    fixupMsgId: UInt32
FixupState = Int32
fixupStateSuccess: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 0
fixupStateInProgress: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 1
fixupStateCouldNotUpdate: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupState = 2
class Ipv4Address(Structure):
    addr: Byte * 4
class Ipv6Address(Structure):
    addr: Byte * 16
class IsolationInfo(Structure):
    isolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState
    probEndTime: win32more.Windows.Win32.Foundation.FILETIME
    failureUrl: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
class IsolationInfoEx(Structure):
    isolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState
    extendedIsolationState: win32more.Windows.Win32.Security.NetworkAccessProtection.ExtendedIsolationState
    probEndTime: win32more.Windows.Win32.Foundation.FILETIME
    failureUrl: win32more.Windows.Win32.Security.NetworkAccessProtection.CountedString
IsolationState = Int32
isolationStateNotRestricted: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 1
isolationStateInProbation: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 2
isolationStateRestrictedAccess: win32more.Windows.Win32.Security.NetworkAccessProtection.IsolationState = 3
class NapComponentRegistrationInfo(Structure):
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
napNotifyTypeUnknown: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 0
napNotifyTypeServiceState: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 1
napNotifyTypeQuarState: win32more.Windows.Win32.Security.NetworkAccessProtection.NapNotifyType = 2
NapTracingLevel = Int32
tracingLevelUndefined: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 0
tracingLevelBasic: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 1
tracingLevelAdvanced: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 2
tracingLevelDebug: win32more.Windows.Win32.Security.NetworkAccessProtection.NapTracingLevel = 3
class NetworkSoH(Structure):
    size: UInt16
    data: POINTER(Byte)
class PrivateData(Structure):
    size: UInt16
    data: POINTER(Byte)
RemoteConfigurationType = Int32
remoteConfigTypeMachine: win32more.Windows.Win32.Security.NetworkAccessProtection.RemoteConfigurationType = 1
remoteConfigTypeConfigBlob: win32more.Windows.Win32.Security.NetworkAccessProtection.RemoteConfigurationType = 2
class ResultCodes(Structure):
    count: UInt16
    results: POINTER(win32more.Windows.Win32.Foundation.HRESULT)
class SoH(Structure):
    count: UInt16
    attributes: POINTER(win32more.Windows.Win32.Security.NetworkAccessProtection.SoHAttribute)
class SoHAttribute(Structure):
    type: UInt16
    size: UInt16
    value: POINTER(Byte)
class SystemHealthAgentState(Structure):
    id: UInt32
    shaResultCodes: win32more.Windows.Win32.Security.NetworkAccessProtection.ResultCodes
    failureCategory: win32more.Windows.Win32.Security.NetworkAccessProtection.FailureCategory
    fixupInfo: win32more.Windows.Win32.Security.NetworkAccessProtection.FixupInfo


make_ready(__name__)
