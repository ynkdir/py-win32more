from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.ApplicationVerifier
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
AVRF_MAX_TRACES = 32
def _define_VerifierEnumerateResource():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS,win32more.System.ApplicationVerifier.eAvrfResourceTypes,win32more.System.ApplicationVerifier.AVRF_RESOURCE_ENUMERATE_CALLBACK,c_void_p)(('VerifierEnumerateResource', windll['verifier.dll']), ((1, 'Process'),(1, 'Flags'),(1, 'ResourceType'),(1, 'ResourceCallback'),(1, 'EnumerationContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AVRF_BACKTRACE_INFORMATION_head():
    class AVRF_BACKTRACE_INFORMATION(Structure):
        pass
    return AVRF_BACKTRACE_INFORMATION
def _define_AVRF_BACKTRACE_INFORMATION():
    AVRF_BACKTRACE_INFORMATION = win32more.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION_head
    AVRF_BACKTRACE_INFORMATION._fields_ = [
        ('Depth', UInt32),
        ('Index', UInt32),
        ('ReturnAddresses', UInt64 * 32),
    ]
    return AVRF_BACKTRACE_INFORMATION
def _define_AVRF_HANDLE_OPERATION_head():
    class AVRF_HANDLE_OPERATION(Structure):
        pass
    return AVRF_HANDLE_OPERATION
def _define_AVRF_HANDLE_OPERATION():
    AVRF_HANDLE_OPERATION = win32more.System.ApplicationVerifier.AVRF_HANDLE_OPERATION_head
    AVRF_HANDLE_OPERATION._fields_ = [
        ('Handle', UInt64),
        ('ProcessId', UInt32),
        ('ThreadId', UInt32),
        ('OperationType', UInt32),
        ('Spare0', UInt32),
        ('BackTraceInformation', win32more.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION),
    ]
    return AVRF_HANDLE_OPERATION
def _define_AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK():
    return WINFUNCTYPE(UInt32,POINTER(win32more.System.ApplicationVerifier.AVRF_HANDLE_OPERATION_head),c_void_p,POINTER(UInt32))
def _define_AVRF_HEAP_ALLOCATION_head():
    class AVRF_HEAP_ALLOCATION(Structure):
        pass
    return AVRF_HEAP_ALLOCATION
def _define_AVRF_HEAP_ALLOCATION():
    AVRF_HEAP_ALLOCATION = win32more.System.ApplicationVerifier.AVRF_HEAP_ALLOCATION_head
    AVRF_HEAP_ALLOCATION._fields_ = [
        ('HeapHandle', UInt64),
        ('UserAllocation', UInt64),
        ('UserAllocationSize', UInt64),
        ('Allocation', UInt64),
        ('AllocationSize', UInt64),
        ('UserAllocationState', UInt32),
        ('HeapState', UInt32),
        ('HeapContext', UInt64),
        ('BackTraceInformation', POINTER(win32more.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION_head)),
    ]
    return AVRF_HEAP_ALLOCATION
def _define_AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK():
    return WINFUNCTYPE(UInt32,POINTER(win32more.System.ApplicationVerifier.AVRF_HEAP_ALLOCATION_head),c_void_p,POINTER(UInt32))
def _define_AVRF_RESOURCE_ENUMERATE_CALLBACK():
    return WINFUNCTYPE(UInt32,c_void_p,c_void_p,POINTER(UInt32))
eAvrfResourceTypes = Int32
eAvrfResourceTypes_AvrfResourceHeapAllocation = 0
eAvrfResourceTypes_AvrfResourceHandleTrace = 1
eAvrfResourceTypes_AvrfResourceMax = 2
eHANDLE_TRACE_OPERATIONS = Int32
eHANDLE_TRACE_OPERATIONS_OperationDbUnused = 0
eHANDLE_TRACE_OPERATIONS_OperationDbOPEN = 1
eHANDLE_TRACE_OPERATIONS_OperationDbCLOSE = 2
eHANDLE_TRACE_OPERATIONS_OperationDbBADREF = 3
eHeapAllocationState = Int32
eHeapAllocationState_HeapFullPageHeap = 1073741824
eHeapAllocationState_HeapMetadata = -2147483648
eHeapAllocationState_HeapStateMask = -65536
eHeapEnumerationLevel = Int32
eHeapEnumerationLevel_HeapEnumerationEverything = 0
eHeapEnumerationLevel_HeapEnumerationStop = -1
eUserAllocationState = Int32
eUserAllocationState_AllocationStateUnknown = 0
eUserAllocationState_AllocationStateBusy = 1
eUserAllocationState_AllocationStateFree = 2
VERIFIER_ENUM_RESOURCE_FLAGS = UInt32
AVRF_ENUM_RESOURCES_FLAGS_DONT_RESOLVE_TRACES = 2
AVRF_ENUM_RESOURCES_FLAGS_SUSPEND = 1
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
