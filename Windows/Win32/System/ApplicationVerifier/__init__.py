from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.ApplicationVerifier
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
class AVRF_BACKTRACE_INFORMATION(Structure):
    Depth: UInt32
    Index: UInt32
    ReturnAddresses: UInt64 * 32
@winfunctype_pointer
def AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK(HandleOperation: POINTER(Windows.Win32.System.ApplicationVerifier.AVRF_HANDLE_OPERATION_head), EnumerationContext: c_void_p, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HANDLE_OPERATION(Structure):
    Handle: UInt64
    ProcessId: UInt32
    ThreadId: UInt32
    OperationType: UInt32
    Spare0: UInt32
    BackTraceInformation: Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION
@winfunctype_pointer
def AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK(HeapAllocation: POINTER(Windows.Win32.System.ApplicationVerifier.AVRF_HEAP_ALLOCATION_head), EnumerationContext: c_void_p, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HEAP_ALLOCATION(Structure):
    HeapHandle: UInt64
    UserAllocation: UInt64
    UserAllocationSize: UInt64
    Allocation: UInt64
    AllocationSize: UInt64
    UserAllocationState: UInt32
    HeapState: UInt32
    HeapContext: UInt64
    BackTraceInformation: POINTER(Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION_head)
@winfunctype_pointer
def AVRF_RESOURCE_ENUMERATE_CALLBACK(ResourceDescription: c_void_p, EnumerationContext: c_void_p, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
AVRF_MAX_TRACES: UInt32 = 32
@winfunctype('verifier.dll')
def VerifierEnumerateResource(Process: Windows.Win32.Foundation.HANDLE, Flags: Windows.Win32.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS, ResourceType: Windows.Win32.System.ApplicationVerifier.eAvrfResourceTypes, ResourceCallback: Windows.Win32.System.ApplicationVerifier.AVRF_RESOURCE_ENUMERATE_CALLBACK, EnumerationContext: c_void_p) -> UInt32: ...
VERIFIER_ENUM_RESOURCE_FLAGS = UInt32
AVRF_ENUM_RESOURCES_FLAGS_DONT_RESOLVE_TRACES: VERIFIER_ENUM_RESOURCE_FLAGS = 2
AVRF_ENUM_RESOURCES_FLAGS_SUSPEND: VERIFIER_ENUM_RESOURCE_FLAGS = 1
eAvrfResourceTypes = Int32
eAvrfResourceTypes_AvrfResourceHeapAllocation: eAvrfResourceTypes = 0
eAvrfResourceTypes_AvrfResourceHandleTrace: eAvrfResourceTypes = 1
eAvrfResourceTypes_AvrfResourceMax: eAvrfResourceTypes = 2
eHANDLE_TRACE_OPERATIONS = Int32
eHANDLE_TRACE_OPERATIONS_OperationDbUnused: eHANDLE_TRACE_OPERATIONS = 0
eHANDLE_TRACE_OPERATIONS_OperationDbOPEN: eHANDLE_TRACE_OPERATIONS = 1
eHANDLE_TRACE_OPERATIONS_OperationDbCLOSE: eHANDLE_TRACE_OPERATIONS = 2
eHANDLE_TRACE_OPERATIONS_OperationDbBADREF: eHANDLE_TRACE_OPERATIONS = 3
eHeapAllocationState = Int32
eHeapAllocationState_HeapFullPageHeap: eHeapAllocationState = 1073741824
eHeapAllocationState_HeapMetadata: eHeapAllocationState = -2147483648
eHeapAllocationState_HeapStateMask: eHeapAllocationState = -65536
eHeapEnumerationLevel = Int32
eHeapEnumerationLevel_HeapEnumerationEverything: eHeapEnumerationLevel = 0
eHeapEnumerationLevel_HeapEnumerationStop: eHeapEnumerationLevel = -1
eUserAllocationState = Int32
eUserAllocationState_AllocationStateUnknown: eUserAllocationState = 0
eUserAllocationState_AllocationStateBusy: eUserAllocationState = 1
eUserAllocationState_AllocationStateFree: eUserAllocationState = 2
make_head(_module, 'AVRF_BACKTRACE_INFORMATION')
make_head(_module, 'AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK')
make_head(_module, 'AVRF_HANDLE_OPERATION')
make_head(_module, 'AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK')
make_head(_module, 'AVRF_HEAP_ALLOCATION')
make_head(_module, 'AVRF_RESOURCE_ENUMERATE_CALLBACK')
__all__ = [
    "AVRF_BACKTRACE_INFORMATION",
    "AVRF_ENUM_RESOURCES_FLAGS_DONT_RESOLVE_TRACES",
    "AVRF_ENUM_RESOURCES_FLAGS_SUSPEND",
    "AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK",
    "AVRF_HANDLE_OPERATION",
    "AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK",
    "AVRF_HEAP_ALLOCATION",
    "AVRF_MAX_TRACES",
    "AVRF_RESOURCE_ENUMERATE_CALLBACK",
    "VERIFIER_ENUM_RESOURCE_FLAGS",
    "VerifierEnumerateResource",
    "eAvrfResourceTypes",
    "eAvrfResourceTypes_AvrfResourceHandleTrace",
    "eAvrfResourceTypes_AvrfResourceHeapAllocation",
    "eAvrfResourceTypes_AvrfResourceMax",
    "eHANDLE_TRACE_OPERATIONS",
    "eHANDLE_TRACE_OPERATIONS_OperationDbBADREF",
    "eHANDLE_TRACE_OPERATIONS_OperationDbCLOSE",
    "eHANDLE_TRACE_OPERATIONS_OperationDbOPEN",
    "eHANDLE_TRACE_OPERATIONS_OperationDbUnused",
    "eHeapAllocationState",
    "eHeapAllocationState_HeapFullPageHeap",
    "eHeapAllocationState_HeapMetadata",
    "eHeapAllocationState_HeapStateMask",
    "eHeapEnumerationLevel",
    "eHeapEnumerationLevel_HeapEnumerationEverything",
    "eHeapEnumerationLevel_HeapEnumerationStop",
    "eUserAllocationState",
    "eUserAllocationState_AllocationStateBusy",
    "eUserAllocationState_AllocationStateFree",
    "eUserAllocationState_AllocationStateUnknown",
]
_arch_optional = [
]
