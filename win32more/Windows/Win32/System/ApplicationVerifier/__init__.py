from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.ApplicationVerifier
class AVRF_BACKTRACE_INFORMATION(EasyCastStructure):
    Depth: UInt32
    Index: UInt32
    ReturnAddresses: UInt64 * 32
@winfunctype_pointer
def AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK(HandleOperation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_HANDLE_OPERATION), EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HANDLE_OPERATION(EasyCastStructure):
    Handle: UInt64
    ProcessId: UInt32
    ThreadId: UInt32
    OperationType: UInt32
    Spare0: UInt32
    BackTraceInformation: win32more.Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION
@winfunctype_pointer
def AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK(HeapAllocation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_HEAP_ALLOCATION), EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HEAP_ALLOCATION(EasyCastStructure):
    HeapHandle: UInt64
    UserAllocation: UInt64
    UserAllocationSize: UInt64
    Allocation: UInt64
    AllocationSize: UInt64
    UserAllocationState: UInt32
    HeapState: UInt32
    HeapContext: UInt64
    BackTraceInformation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION)
@winfunctype_pointer
def AVRF_RESOURCE_ENUMERATE_CALLBACK(ResourceDescription: VoidPtr, EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
AVRF_MAX_TRACES: UInt32 = 32
@winfunctype('verifier.dll')
def VerifierEnumerateResource(Process: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS, ResourceType: UInt32, ResourceCallback: win32more.Windows.Win32.System.ApplicationVerifier.AVRF_RESOURCE_ENUMERATE_CALLBACK, EnumerationContext: VoidPtr) -> UInt32: ...
VERIFIER_ENUM_RESOURCE_FLAGS = UInt32
AVRF_ENUM_RESOURCES_FLAGS_DONT_RESOLVE_TRACES: win32more.Windows.Win32.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS = 2
AVRF_ENUM_RESOURCES_FLAGS_SUSPEND: win32more.Windows.Win32.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS = 1
eAvrfResourceTypes = Int32
eAvrfResourceTypes_AvrfResourceHeapAllocation: win32more.Windows.Win32.System.ApplicationVerifier.eAvrfResourceTypes = 0
eAvrfResourceTypes_AvrfResourceHandleTrace: win32more.Windows.Win32.System.ApplicationVerifier.eAvrfResourceTypes = 1
eAvrfResourceTypes_AvrfResourceMax: win32more.Windows.Win32.System.ApplicationVerifier.eAvrfResourceTypes = 2
eHANDLE_TRACE_OPERATIONS = Int32
eHANDLE_TRACE_OPERATIONS_OperationDbUnused: win32more.Windows.Win32.System.ApplicationVerifier.eHANDLE_TRACE_OPERATIONS = 0
eHANDLE_TRACE_OPERATIONS_OperationDbOPEN: win32more.Windows.Win32.System.ApplicationVerifier.eHANDLE_TRACE_OPERATIONS = 1
eHANDLE_TRACE_OPERATIONS_OperationDbCLOSE: win32more.Windows.Win32.System.ApplicationVerifier.eHANDLE_TRACE_OPERATIONS = 2
eHANDLE_TRACE_OPERATIONS_OperationDbBADREF: win32more.Windows.Win32.System.ApplicationVerifier.eHANDLE_TRACE_OPERATIONS = 3
eHeapAllocationState = Int32
eHeapAllocationState_HeapFullPageHeap: win32more.Windows.Win32.System.ApplicationVerifier.eHeapAllocationState = 1073741824
eHeapAllocationState_HeapMetadata: win32more.Windows.Win32.System.ApplicationVerifier.eHeapAllocationState = -2147483648
eHeapAllocationState_HeapStateMask: win32more.Windows.Win32.System.ApplicationVerifier.eHeapAllocationState = -65536
eHeapEnumerationLevel = Int32
eHeapEnumerationLevel_HeapEnumerationEverything: win32more.Windows.Win32.System.ApplicationVerifier.eHeapEnumerationLevel = 0
eHeapEnumerationLevel_HeapEnumerationStop: win32more.Windows.Win32.System.ApplicationVerifier.eHeapEnumerationLevel = -1
eUserAllocationState = Int32
eUserAllocationState_AllocationStateUnknown: win32more.Windows.Win32.System.ApplicationVerifier.eUserAllocationState = 0
eUserAllocationState_AllocationStateBusy: win32more.Windows.Win32.System.ApplicationVerifier.eUserAllocationState = 1
eUserAllocationState_AllocationStateFree: win32more.Windows.Win32.System.ApplicationVerifier.eUserAllocationState = 2


make_ready(__name__)
