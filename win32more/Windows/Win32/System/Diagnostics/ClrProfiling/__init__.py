from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Diagnostics.ClrProfiling
import win32more.Windows.Win32.System.WinRT.Metadata
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CorDB_CONTROL_Profiling: String = 'Cor_Enable_Profiling'
CorDB_CONTROL_ProfilingL: String = 'Cor_Enable_Profiling'
class COR_DEBUG_IL_TO_NATIVE_MAP(EasyCastStructure):
    ilOffset: UInt32
    nativeStartOffset: UInt32
    nativeEndOffset: UInt32
class COR_IL_MAP(EasyCastStructure):
    oldOffset: UInt32
    newOffset: UInt32
    fAccurate: win32more.Windows.Win32.Foundation.BOOL
class COR_PRF_ASSEMBLY_REFERENCE_INFO(EasyCastStructure):
    pbPublicKeyOrToken: VoidPtr
    cbPublicKeyOrToken: UInt32
    szName: win32more.Windows.Win32.Foundation.PWSTR
    pMetaData: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.ASSEMBLYMETADATA_head)
    pbHashValue: VoidPtr
    cbHashValue: UInt32
    dwAssemblyRefFlags: UInt32
COR_PRF_CLAUSE_TYPE = Int32
COR_PRF_CLAUSE_NONE: COR_PRF_CLAUSE_TYPE = 0
COR_PRF_CLAUSE_FILTER: COR_PRF_CLAUSE_TYPE = 1
COR_PRF_CLAUSE_CATCH: COR_PRF_CLAUSE_TYPE = 2
COR_PRF_CLAUSE_FINALLY: COR_PRF_CLAUSE_TYPE = 3
COR_PRF_CODEGEN_FLAGS = Int32
COR_PRF_CODEGEN_DISABLE_INLINING: COR_PRF_CODEGEN_FLAGS = 1
COR_PRF_CODEGEN_DISABLE_ALL_OPTIMIZATIONS: COR_PRF_CODEGEN_FLAGS = 2
class COR_PRF_CODE_INFO(EasyCastStructure):
    startAddress: UIntPtr
    size: UIntPtr
class COR_PRF_EX_CLAUSE_INFO(EasyCastStructure):
    clauseType: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_CLAUSE_TYPE
    programCounter: UIntPtr
    framePointer: UIntPtr
    shadowStackPointer: UIntPtr
COR_PRF_FINALIZER_FLAGS = Int32
COR_PRF_FINALIZER_CRITICAL: COR_PRF_FINALIZER_FLAGS = 1
class COR_PRF_FUNCTION(EasyCastStructure):
    functionId: UIntPtr
    reJitId: UIntPtr
class COR_PRF_FUNCTION_ARGUMENT_INFO(EasyCastStructure):
    numRanges: UInt32
    totalArgumentSize: UInt32
    ranges: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_ARGUMENT_RANGE * 1
class COR_PRF_FUNCTION_ARGUMENT_RANGE(EasyCastStructure):
    startAddress: UIntPtr
    length: UInt32
COR_PRF_GC_GENERATION = Int32
COR_PRF_GC_GEN_0: COR_PRF_GC_GENERATION = 0
COR_PRF_GC_GEN_1: COR_PRF_GC_GENERATION = 1
COR_PRF_GC_GEN_2: COR_PRF_GC_GENERATION = 2
COR_PRF_GC_LARGE_OBJECT_HEAP: COR_PRF_GC_GENERATION = 3
class COR_PRF_GC_GENERATION_RANGE(EasyCastStructure):
    generation: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_GENERATION
    rangeStart: UIntPtr
    rangeLength: UIntPtr
    rangeLengthReserved: UIntPtr
COR_PRF_GC_REASON = Int32
COR_PRF_GC_INDUCED: COR_PRF_GC_REASON = 1
COR_PRF_GC_OTHER: COR_PRF_GC_REASON = 0
COR_PRF_GC_ROOT_FLAGS = Int32
COR_PRF_GC_ROOT_PINNING: COR_PRF_GC_ROOT_FLAGS = 1
COR_PRF_GC_ROOT_WEAKREF: COR_PRF_GC_ROOT_FLAGS = 2
COR_PRF_GC_ROOT_INTERIOR: COR_PRF_GC_ROOT_FLAGS = 4
COR_PRF_GC_ROOT_REFCOUNTED: COR_PRF_GC_ROOT_FLAGS = 8
COR_PRF_GC_ROOT_KIND = Int32
COR_PRF_GC_ROOT_STACK: COR_PRF_GC_ROOT_KIND = 1
COR_PRF_GC_ROOT_FINALIZER: COR_PRF_GC_ROOT_KIND = 2
COR_PRF_GC_ROOT_HANDLE: COR_PRF_GC_ROOT_KIND = 3
COR_PRF_GC_ROOT_OTHER: COR_PRF_GC_ROOT_KIND = 0
COR_PRF_HIGH_MONITOR = Int32
COR_PRF_HIGH_MONITOR_NONE: COR_PRF_HIGH_MONITOR = 0
COR_PRF_HIGH_ADD_ASSEMBLY_REFERENCES: COR_PRF_HIGH_MONITOR = 1
COR_PRF_HIGH_IN_MEMORY_SYMBOLS_UPDATED: COR_PRF_HIGH_MONITOR = 2
COR_PRF_HIGH_MONITOR_DYNAMIC_FUNCTION_UNLOADS: COR_PRF_HIGH_MONITOR = 4
COR_PRF_HIGH_REQUIRE_PROFILE_IMAGE: COR_PRF_HIGH_MONITOR = 0
COR_PRF_HIGH_ALLOWABLE_AFTER_ATTACH: COR_PRF_HIGH_MONITOR = 6
COR_PRF_HIGH_MONITOR_IMMUTABLE: COR_PRF_HIGH_MONITOR = 0
COR_PRF_JIT_CACHE = Int32
COR_PRF_CACHED_FUNCTION_FOUND: COR_PRF_JIT_CACHE = 0
COR_PRF_CACHED_FUNCTION_NOT_FOUND: COR_PRF_JIT_CACHE = 1
class COR_PRF_METHOD(EasyCastStructure):
    moduleId: UIntPtr
    methodId: UInt32
COR_PRF_MISC = Int32
PROFILER_PARENT_UNKNOWN: COR_PRF_MISC = -3
PROFILER_GLOBAL_CLASS: COR_PRF_MISC = -2
PROFILER_GLOBAL_MODULE: COR_PRF_MISC = -1
COR_PRF_MODULE_FLAGS = Int32
COR_PRF_MODULE_DISK: COR_PRF_MODULE_FLAGS = 1
COR_PRF_MODULE_NGEN: COR_PRF_MODULE_FLAGS = 2
COR_PRF_MODULE_DYNAMIC: COR_PRF_MODULE_FLAGS = 4
COR_PRF_MODULE_COLLECTIBLE: COR_PRF_MODULE_FLAGS = 8
COR_PRF_MODULE_RESOURCE: COR_PRF_MODULE_FLAGS = 16
COR_PRF_MODULE_FLAT_LAYOUT: COR_PRF_MODULE_FLAGS = 32
COR_PRF_MODULE_WINDOWS_RUNTIME: COR_PRF_MODULE_FLAGS = 64
COR_PRF_MONITOR = Int32
COR_PRF_MONITOR_NONE: COR_PRF_MONITOR = 0
COR_PRF_MONITOR_FUNCTION_UNLOADS: COR_PRF_MONITOR = 1
COR_PRF_MONITOR_CLASS_LOADS: COR_PRF_MONITOR = 2
COR_PRF_MONITOR_MODULE_LOADS: COR_PRF_MONITOR = 4
COR_PRF_MONITOR_ASSEMBLY_LOADS: COR_PRF_MONITOR = 8
COR_PRF_MONITOR_APPDOMAIN_LOADS: COR_PRF_MONITOR = 16
COR_PRF_MONITOR_JIT_COMPILATION: COR_PRF_MONITOR = 32
COR_PRF_MONITOR_EXCEPTIONS: COR_PRF_MONITOR = 64
COR_PRF_MONITOR_GC: COR_PRF_MONITOR = 128
COR_PRF_MONITOR_OBJECT_ALLOCATED: COR_PRF_MONITOR = 256
COR_PRF_MONITOR_THREADS: COR_PRF_MONITOR = 512
COR_PRF_MONITOR_REMOTING: COR_PRF_MONITOR = 1024
COR_PRF_MONITOR_CODE_TRANSITIONS: COR_PRF_MONITOR = 2048
COR_PRF_MONITOR_ENTERLEAVE: COR_PRF_MONITOR = 4096
COR_PRF_MONITOR_CCW: COR_PRF_MONITOR = 8192
COR_PRF_MONITOR_REMOTING_COOKIE: COR_PRF_MONITOR = 17408
COR_PRF_MONITOR_REMOTING_ASYNC: COR_PRF_MONITOR = 33792
COR_PRF_MONITOR_SUSPENDS: COR_PRF_MONITOR = 65536
COR_PRF_MONITOR_CACHE_SEARCHES: COR_PRF_MONITOR = 131072
COR_PRF_ENABLE_REJIT: COR_PRF_MONITOR = 262144
COR_PRF_ENABLE_INPROC_DEBUGGING: COR_PRF_MONITOR = 524288
COR_PRF_ENABLE_JIT_MAPS: COR_PRF_MONITOR = 1048576
COR_PRF_DISABLE_INLINING: COR_PRF_MONITOR = 2097152
COR_PRF_DISABLE_OPTIMIZATIONS: COR_PRF_MONITOR = 4194304
COR_PRF_ENABLE_OBJECT_ALLOCATED: COR_PRF_MONITOR = 8388608
COR_PRF_MONITOR_CLR_EXCEPTIONS: COR_PRF_MONITOR = 16777216
COR_PRF_MONITOR_ALL: COR_PRF_MONITOR = 17301503
COR_PRF_ENABLE_FUNCTION_ARGS: COR_PRF_MONITOR = 33554432
COR_PRF_ENABLE_FUNCTION_RETVAL: COR_PRF_MONITOR = 67108864
COR_PRF_ENABLE_FRAME_INFO: COR_PRF_MONITOR = 134217728
COR_PRF_ENABLE_STACK_SNAPSHOT: COR_PRF_MONITOR = 268435456
COR_PRF_USE_PROFILE_IMAGES: COR_PRF_MONITOR = 536870912
COR_PRF_DISABLE_TRANSPARENCY_CHECKS_UNDER_FULL_TRUST: COR_PRF_MONITOR = 1073741824
COR_PRF_DISABLE_ALL_NGEN_IMAGES: COR_PRF_MONITOR = -2147483648
COR_PRF_ALL: COR_PRF_MONITOR = -1879048193
COR_PRF_REQUIRE_PROFILE_IMAGE: COR_PRF_MONITOR = 536877056
COR_PRF_ALLOWABLE_AFTER_ATTACH: COR_PRF_MONITOR = 268501758
COR_PRF_MONITOR_IMMUTABLE: COR_PRF_MONITOR = -285422592
COR_PRF_RUNTIME_TYPE = Int32
COR_PRF_DESKTOP_CLR: COR_PRF_RUNTIME_TYPE = 1
COR_PRF_CORE_CLR: COR_PRF_RUNTIME_TYPE = 2
COR_PRF_SNAPSHOT_INFO = Int32
COR_PRF_SNAPSHOT_DEFAULT: COR_PRF_SNAPSHOT_INFO = 0
COR_PRF_SNAPSHOT_REGISTER_CONTEXT: COR_PRF_SNAPSHOT_INFO = 1
COR_PRF_SNAPSHOT_X86_OPTIMIZED: COR_PRF_SNAPSHOT_INFO = 2
COR_PRF_STATIC_TYPE = Int32
COR_PRF_FIELD_NOT_A_STATIC: COR_PRF_STATIC_TYPE = 0
COR_PRF_FIELD_APP_DOMAIN_STATIC: COR_PRF_STATIC_TYPE = 1
COR_PRF_FIELD_THREAD_STATIC: COR_PRF_STATIC_TYPE = 2
COR_PRF_FIELD_CONTEXT_STATIC: COR_PRF_STATIC_TYPE = 4
COR_PRF_FIELD_RVA_STATIC: COR_PRF_STATIC_TYPE = 8
COR_PRF_SUSPEND_REASON = Int32
COR_PRF_SUSPEND_OTHER: COR_PRF_SUSPEND_REASON = 0
COR_PRF_SUSPEND_FOR_GC: COR_PRF_SUSPEND_REASON = 1
COR_PRF_SUSPEND_FOR_APPDOMAIN_SHUTDOWN: COR_PRF_SUSPEND_REASON = 2
COR_PRF_SUSPEND_FOR_CODE_PITCHING: COR_PRF_SUSPEND_REASON = 3
COR_PRF_SUSPEND_FOR_SHUTDOWN: COR_PRF_SUSPEND_REASON = 4
COR_PRF_SUSPEND_FOR_INPROC_DEBUGGER: COR_PRF_SUSPEND_REASON = 6
COR_PRF_SUSPEND_FOR_GC_PREP: COR_PRF_SUSPEND_REASON = 7
COR_PRF_SUSPEND_FOR_REJIT: COR_PRF_SUSPEND_REASON = 8
COR_PRF_TRANSITION_REASON = Int32
COR_PRF_TRANSITION_CALL: COR_PRF_TRANSITION_REASON = 0
COR_PRF_TRANSITION_RETURN: COR_PRF_TRANSITION_REASON = 1
CorDebugIlToNativeMappingTypes = Int32
NO_MAPPING: CorDebugIlToNativeMappingTypes = -1
PROLOG: CorDebugIlToNativeMappingTypes = -2
EPILOG: CorDebugIlToNativeMappingTypes = -3
@winfunctype_pointer
def FunctionEnter(funcID: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionEnter2(funcId: UIntPtr, clientData: UIntPtr, func: UIntPtr, argumentInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_ARGUMENT_INFO_head)) -> Void: ...
@winfunctype_pointer
def FunctionEnter3(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID) -> Void: ...
@winfunctype_pointer
def FunctionEnter3WithInfo(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID, eltInfo: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionIDMapper(funcId: UIntPtr, pbHookFunction: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UIntPtr: ...
@winfunctype_pointer
def FunctionIDMapper2(funcId: UIntPtr, clientData: VoidPtr, pbHookFunction: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UIntPtr: ...
class FunctionIDOrClientID(EasyCastUnion):
    functionID: UIntPtr
    clientID: UIntPtr
@winfunctype_pointer
def FunctionLeave(funcID: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionLeave2(funcId: UIntPtr, clientData: UIntPtr, func: UIntPtr, retvalRange: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_ARGUMENT_RANGE_head)) -> Void: ...
@winfunctype_pointer
def FunctionLeave3(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID) -> Void: ...
@winfunctype_pointer
def FunctionLeave3WithInfo(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID, eltInfo: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionTailcall(funcID: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionTailcall2(funcId: UIntPtr, clientData: UIntPtr, func: UIntPtr) -> Void: ...
@winfunctype_pointer
def FunctionTailcall3(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID) -> Void: ...
@winfunctype_pointer
def FunctionTailcall3WithInfo(functionIDOrClientID: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDOrClientID, eltInfo: UIntPtr) -> Void: ...
class ICorProfilerAssemblyReferenceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a78c24-2eef-4f65-b45f-dd1d8038bf3c}')
    @commethod(3)
    def AddAssemblyReference(self, pAssemblyRefInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_ASSEMBLY_REFERENCE_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{176fbed1-a55c-4796-98ca-a9da0ef883e7}')
    @commethod(3)
    def Initialize(self, pICorProfilerInfoUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppDomainCreationStarted(self, appDomainId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AppDomainCreationFinished(self, appDomainId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AppDomainShutdownStarted(self, appDomainId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AppDomainShutdownFinished(self, appDomainId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AssemblyLoadStarted(self, assemblyId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AssemblyLoadFinished(self, assemblyId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AssemblyUnloadStarted(self, assemblyId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AssemblyUnloadFinished(self, assemblyId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ModuleLoadStarted(self, moduleId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ModuleLoadFinished(self, moduleId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ModuleUnloadStarted(self, moduleId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ModuleUnloadFinished(self, moduleId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ModuleAttachedToAssembly(self, moduleId: UIntPtr, AssemblyId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ClassLoadStarted(self, classId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ClassLoadFinished(self, classId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ClassUnloadStarted(self, classId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ClassUnloadFinished(self, classId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FunctionUnloadStarted(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def JITCompilationStarted(self, functionId: UIntPtr, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def JITCompilationFinished(self, functionId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def JITCachedFunctionSearchStarted(self, functionId: UIntPtr, pbUseCachedFunction: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def JITCachedFunctionSearchFinished(self, functionId: UIntPtr, result: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_JIT_CACHE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def JITFunctionPitched(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def JITInlining(self, callerId: UIntPtr, calleeId: UIntPtr, pfShouldInline: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ThreadCreated(self, threadId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def ThreadDestroyed(self, threadId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ThreadAssignedToOSThread(self, managedThreadId: UIntPtr, osThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def RemotingClientInvocationStarted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemotingClientSendingMessage(self, pCookie: POINTER(Guid), fIsAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def RemotingClientReceivingReply(self, pCookie: POINTER(Guid), fIsAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def RemotingClientInvocationFinished(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def RemotingServerReceivingMessage(self, pCookie: POINTER(Guid), fIsAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemotingServerInvocationStarted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RemotingServerInvocationReturned(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def RemotingServerSendingReply(self, pCookie: POINTER(Guid), fIsAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def UnmanagedToManagedTransition(self, functionId: UIntPtr, reason: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_TRANSITION_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def ManagedToUnmanagedTransition(self, functionId: UIntPtr, reason: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_TRANSITION_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def RuntimeSuspendStarted(self, suspendReason: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_SUSPEND_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def RuntimeSuspendFinished(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def RuntimeSuspendAborted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RuntimeResumeStarted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RuntimeResumeFinished(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def RuntimeThreadSuspended(self, threadId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def RuntimeThreadResumed(self, threadId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def MovedReferences(self, cMovedObjectIDRanges: UInt32, oldObjectIDRangeStart: POINTER(UIntPtr), newObjectIDRangeStart: POINTER(UIntPtr), cObjectIDRangeLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def ObjectAllocated(self, objectId: UIntPtr, classId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def ObjectsAllocatedByClass(self, cClassCount: UInt32, classIds: POINTER(UIntPtr), cObjects: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def ObjectReferences(self, objectId: UIntPtr, classId: UIntPtr, cObjectRefs: UInt32, objectRefIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def RootReferences(self, cRootRefs: UInt32, rootRefIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def ExceptionThrown(self, thrownObjectId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def ExceptionSearchFunctionEnter(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ExceptionSearchFunctionLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def ExceptionSearchFilterEnter(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def ExceptionSearchFilterLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def ExceptionSearchCatcherFound(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def ExceptionOSHandlerEnter(self, __unused: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def ExceptionOSHandlerLeave(self, __unused: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def ExceptionUnwindFunctionEnter(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def ExceptionUnwindFunctionLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def ExceptionUnwindFinallyEnter(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def ExceptionUnwindFinallyLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def ExceptionCatcherEnter(self, functionId: UIntPtr, objectId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def ExceptionCatcherLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def COMClassicVTableCreated(self, wrappedClassId: UIntPtr, implementedIID: POINTER(Guid), pVTable: VoidPtr, cSlots: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def COMClassicVTableDestroyed(self, wrappedClassId: UIntPtr, implementedIID: POINTER(Guid), pVTable: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def ExceptionCLRCatcherFound(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def ExceptionCLRCatcherExecute(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback2(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback
    _iid_ = Guid('{8a8cc829-ccf2-49fe-bbae-0f022228071a}')
    @commethod(72)
    def ThreadNameChanged(self, threadId: UIntPtr, cchName: UInt32, name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def GarbageCollectionStarted(self, cGenerations: Int32, generationCollected: POINTER(win32more.Windows.Win32.Foundation.BOOL), reason: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def SurvivingReferences(self, cSurvivingObjectIDRanges: UInt32, objectIDRangeStart: POINTER(UIntPtr), cObjectIDRangeLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def GarbageCollectionFinished(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def FinalizeableObjectQueued(self, finalizerFlags: UInt32, objectID: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def RootReferences2(self, cRootRefs: UInt32, rootRefIds: POINTER(UIntPtr), rootKinds: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_ROOT_KIND), rootFlags: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_ROOT_FLAGS), rootIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def HandleCreated(self, handleId: UIntPtr, initialObjectId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def HandleDestroyed(self, handleId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback3(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback2
    _iid_ = Guid('{4fd2ed52-7731-4b8d-9469-03d2cc3086c5}')
    @commethod(80)
    def InitializeForAttach(self, pCorProfilerInfoUnk: win32more.Windows.Win32.System.Com.IUnknown_head, pvClientData: VoidPtr, cbClientData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def ProfilerAttachComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def ProfilerDetachSucceeded(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback4(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback3
    _iid_ = Guid('{7b63b2e3-107d-4d48-b2f6-f61e229470d2}')
    @commethod(83)
    def ReJITCompilationStarted(self, functionId: UIntPtr, rejitId: UIntPtr, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetReJITParameters(self, moduleId: UIntPtr, methodId: UInt32, pFunctionControl: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerFunctionControl_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def ReJITCompilationFinished(self, functionId: UIntPtr, rejitId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def ReJITError(self, moduleId: UIntPtr, methodId: UInt32, functionId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def MovedReferences2(self, cMovedObjectIDRanges: UInt32, oldObjectIDRangeStart: POINTER(UIntPtr), newObjectIDRangeStart: POINTER(UIntPtr), cObjectIDRangeLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def SurvivingReferences2(self, cSurvivingObjectIDRanges: UInt32, objectIDRangeStart: POINTER(UIntPtr), cObjectIDRangeLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback5(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback4
    _iid_ = Guid('{8dfba405-8c9f-45f8-bffa-83b14cef78b5}')
    @commethod(89)
    def ConditionalWeakTableElementReferences(self, cRootRefs: UInt32, keyRefIds: POINTER(UIntPtr), valueRefIds: POINTER(UIntPtr), rootIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback6(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback5
    _iid_ = Guid('{fc13df4b-4448-4f4f-950c-ba8d19d00c36}')
    @commethod(90)
    def GetAssemblyReferences(self, wszAssemblyPath: win32more.Windows.Win32.Foundation.PWSTR, pAsmRefProvider: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerAssemblyReferenceProvider_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback7(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback6
    _iid_ = Guid('{f76a2dba-1d52-4539-866c-2aa518f9efc3}')
    @commethod(91)
    def ModuleInMemorySymbolsUpdated(self, moduleId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback8(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback7
    _iid_ = Guid('{5bed9b15-c079-4d47-bfe2-215a140c07e0}')
    @commethod(92)
    def DynamicMethodJITCompilationStarted(self, functionId: UIntPtr, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL, pILHeader: POINTER(Byte), cbILHeader: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def DynamicMethodJITCompilationFinished(self, functionId: UIntPtr, hrStatus: win32more.Windows.Win32.Foundation.HRESULT, fIsSafeToBlock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerCallback9(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerCallback8
    _iid_ = Guid('{27583ec3-c8f5-482f-8052-194b8ce4705a}')
    @commethod(94)
    def DynamicMethodUnloaded(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerFunctionControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0963021-e1ea-4732-8581-e01b0bd3c0c6}')
    @commethod(3)
    def SetCodegenFlags(self, flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetILFunctionBody(self, cbNewILMethodHeader: UInt32, pbNewILMethodHeader: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetILInstrumentedCodeMap(self, cILMapEntries: UInt32, rgILMapEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_IL_MAP_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerFunctionEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff71301a-b994-429d-a10b-b345a65280ef}')
    @commethod(3)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerFunctionEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Next(self, celt: UInt32, ids: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28b5557d-3f3f-48b4-90b2-5f9eea2f6c48}')
    @commethod(3)
    def GetClassFromObject(self, objectId: UIntPtr, pClassId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClassFromToken(self, moduleId: UIntPtr, typeDef: UInt32, pClassId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCodeInfo(self, functionId: UIntPtr, pStart: POINTER(POINTER(Byte)), pcSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEventMask(self, pdwEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFunctionFromIP(self, ip: POINTER(Byte), pFunctionId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFunctionFromToken(self, moduleId: UIntPtr, token: UInt32, pFunctionId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetHandleFromThread(self, threadId: UIntPtr, phThread: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetObjectSize(self, objectId: UIntPtr, pcSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsArrayClass(self, classId: UIntPtr, pBaseElemType: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.CorElementType), pBaseClassId: POINTER(UIntPtr), pcRank: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetThreadInfo(self, threadId: UIntPtr, pdwWin32ThreadId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentThreadID(self, pThreadId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetClassIDInfo(self, classId: UIntPtr, pModuleId: POINTER(UIntPtr), pTypeDefToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFunctionInfo(self, functionId: UIntPtr, pClassId: POINTER(UIntPtr), pModuleId: POINTER(UIntPtr), pToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEventMask(self, dwEvents: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetEnterLeaveFunctionHooks(self, pFuncEnter: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionEnter), pFuncLeave: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionLeave), pFuncTailcall: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionTailcall)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetFunctionIDMapper(self, pFunc: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDMapper)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetTokenAndMetaDataFromFunction(self, functionId: UIntPtr, riid: POINTER(Guid), ppImport: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head), pToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetModuleInfo(self, moduleId: UIntPtr, ppBaseLoadAddress: POINTER(POINTER(Byte)), cchName: UInt32, pcchName: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, pAssemblyId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetModuleMetaData(self, moduleId: UIntPtr, dwOpenFlags: UInt32, riid: POINTER(Guid), ppOut: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetILFunctionBody(self, moduleId: UIntPtr, methodId: UInt32, ppMethodHeader: POINTER(POINTER(Byte)), pcbMethodSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetILFunctionBodyAllocator(self, moduleId: UIntPtr, ppMalloc: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.IMethodMalloc_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetILFunctionBody(self, moduleId: UIntPtr, methodid: UInt32, pbNewILMethodHeader: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetAppDomainInfo(self, appDomainId: UIntPtr, cchName: UInt32, pcchName: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, pProcessId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetAssemblyInfo(self, assemblyId: UIntPtr, cchName: UInt32, pcchName: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, pAppDomainId: POINTER(UIntPtr), pModuleId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetFunctionReJIT(self, functionId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def ForceGC(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetILInstrumentedCodeMap(self, functionId: UIntPtr, fStartJit: win32more.Windows.Win32.Foundation.BOOL, cILMapEntries: UInt32, rgILMapEntries: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_IL_MAP_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetInprocInspectionInterface(self, ppicd: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetInprocInspectionIThisThread(self, ppicd: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetThreadContext(self, threadId: UIntPtr, pContextId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def BeginInprocDebugging(self, fThisThreadOnly: win32more.Windows.Win32.Foundation.BOOL, pdwProfilerContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def EndInprocDebugging(self, dwProfilerContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetILToNativeMapping(self, functionId: UIntPtr, cMap: UInt32, pcMap: POINTER(UInt32), map: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_DEBUG_IL_TO_NATIVE_MAP_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo
    _iid_ = Guid('{cc0935cd-a518-487d-b0bb-a93214e65478}')
    @commethod(36)
    def DoStackSnapshot(self, thread: UIntPtr, callback: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.StackSnapshotCallback), infoFlags: UInt32, clientData: VoidPtr, context: POINTER(Byte), contextSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetEnterLeaveFunctionHooks2(self, pFuncEnter: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionEnter2), pFuncLeave: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionLeave2), pFuncTailcall: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionTailcall2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetFunctionInfo2(self, funcId: UIntPtr, frameInfo: UIntPtr, pClassId: POINTER(UIntPtr), pModuleId: POINTER(UIntPtr), pToken: POINTER(UInt32), cTypeArgs: UInt32, pcTypeArgs: POINTER(UInt32), typeArgs: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetStringLayout(self, pBufferLengthOffset: POINTER(UInt32), pStringLengthOffset: POINTER(UInt32), pBufferOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetClassLayout(self, classID: UIntPtr, rFieldOffset: POINTER(win32more.Windows.Win32.System.WinRT.Metadata.COR_FIELD_OFFSET_head), cFieldOffset: UInt32, pcFieldOffset: POINTER(UInt32), pulClassSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetClassIDInfo2(self, classId: UIntPtr, pModuleId: POINTER(UIntPtr), pTypeDefToken: POINTER(UInt32), pParentClassId: POINTER(UIntPtr), cNumTypeArgs: UInt32, pcNumTypeArgs: POINTER(UInt32), typeArgs: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetCodeInfo2(self, functionID: UIntPtr, cCodeInfos: UInt32, pcCodeInfos: POINTER(UInt32), codeInfos: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_CODE_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetClassFromTokenAndTypeArgs(self, moduleID: UIntPtr, typeDef: UInt32, cTypeArgs: UInt32, typeArgs: POINTER(UIntPtr), pClassID: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetFunctionFromTokenAndTypeArgs(self, moduleID: UIntPtr, funcDef: UInt32, classId: UIntPtr, cTypeArgs: UInt32, typeArgs: POINTER(UIntPtr), pFunctionID: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def EnumModuleFrozenObjects(self, moduleID: UIntPtr, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerObjectEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetArrayObjectInfo(self, objectId: UIntPtr, cDimensions: UInt32, pDimensionSizes: POINTER(UInt32), pDimensionLowerBounds: POINTER(Int32), ppData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetBoxClassLayout(self, classId: UIntPtr, pBufferOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetThreadAppDomain(self, threadId: UIntPtr, pAppDomainId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetRVAStaticAddress(self, classId: UIntPtr, fieldToken: UInt32, ppAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetAppDomainStaticAddress(self, classId: UIntPtr, fieldToken: UInt32, appDomainId: UIntPtr, ppAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetThreadStaticAddress(self, classId: UIntPtr, fieldToken: UInt32, threadId: UIntPtr, ppAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetContextStaticAddress(self, classId: UIntPtr, fieldToken: UInt32, contextId: UIntPtr, ppAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetStaticFieldInfo(self, classId: UIntPtr, fieldToken: UInt32, pFieldInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_STATIC_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetGenerationBounds(self, cObjectRanges: UInt32, pcObjectRanges: POINTER(UInt32), ranges: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_GENERATION_RANGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetObjectGeneration(self, objectId: UIntPtr, range: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_GC_GENERATION_RANGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetNotifiedExceptionClauseInfo(self, pinfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_EX_CLAUSE_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo2
    _iid_ = Guid('{b555ed4f-452a-4e54-8b39-b5360bad32a0}')
    @commethod(57)
    def EnumJITedFunctions(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerFunctionEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def RequestProfilerDetach(self, dwExpectedCompletionMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetFunctionIDMapper2(self, pFunc: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionIDMapper2), clientData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetStringLayout2(self, pStringLengthOffset: POINTER(UInt32), pBufferOffset: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def SetEnterLeaveFunctionHooks3(self, pFuncEnter3: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionEnter3), pFuncLeave3: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionLeave3), pFuncTailcall3: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionTailcall3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def SetEnterLeaveFunctionHooks3WithInfo(self, pFuncEnter3WithInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionEnter3WithInfo), pFuncLeave3WithInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionLeave3WithInfo), pFuncTailcall3WithInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.FunctionTailcall3WithInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetFunctionEnter3Info(self, functionId: UIntPtr, eltInfo: UIntPtr, pFrameInfo: POINTER(UIntPtr), pcbArgumentInfo: POINTER(UInt32), pArgumentInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_ARGUMENT_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetFunctionLeave3Info(self, functionId: UIntPtr, eltInfo: UIntPtr, pFrameInfo: POINTER(UIntPtr), pRetvalRange: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_FUNCTION_ARGUMENT_RANGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def GetFunctionTailcall3Info(self, functionId: UIntPtr, eltInfo: UIntPtr, pFrameInfo: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def EnumModules(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerModuleEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetRuntimeInformation(self, pClrInstanceId: POINTER(UInt16), pRuntimeType: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_RUNTIME_TYPE), pMajorVersion: POINTER(UInt16), pMinorVersion: POINTER(UInt16), pBuildNumber: POINTER(UInt16), pQFEVersion: POINTER(UInt16), cchVersionString: UInt32, pcchVersionString: POINTER(UInt32), szVersionString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def GetThreadStaticAddress2(self, classId: UIntPtr, fieldToken: UInt32, appDomainId: UIntPtr, threadId: UIntPtr, ppAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetAppDomainsContainingModule(self, moduleId: UIntPtr, cAppDomainIds: UInt32, pcAppDomainIds: POINTER(UInt32), appDomainIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetModuleInfo2(self, moduleId: UIntPtr, ppBaseLoadAddress: POINTER(POINTER(Byte)), cchName: UInt32, pcchName: POINTER(UInt32), szName: win32more.Windows.Win32.Foundation.PWSTR, pAssemblyId: POINTER(UIntPtr), pdwModuleFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo4(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo3
    _iid_ = Guid('{0d8fdcaa-6257-47bf-b1bf-94dac88466ee}')
    @commethod(71)
    def EnumThreads(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerThreadEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def InitializeCurrentThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def RequestReJIT(self, cFunctions: UInt32, moduleIds: POINTER(UIntPtr), methodIds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def RequestRevert(self, cFunctions: UInt32, moduleIds: POINTER(UIntPtr), methodIds: POINTER(UInt32), status: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def GetCodeInfo3(self, functionID: UIntPtr, reJitId: UIntPtr, cCodeInfos: UInt32, pcCodeInfos: POINTER(UInt32), codeInfos: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_CODE_INFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def GetFunctionFromIP2(self, ip: POINTER(Byte), pFunctionId: POINTER(UIntPtr), pReJitId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetReJITIDs(self, functionId: UIntPtr, cReJitIds: UInt32, pcReJitIds: POINTER(UInt32), reJitIds: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def GetILToNativeMapping2(self, functionId: UIntPtr, reJitId: UIntPtr, cMap: UInt32, pcMap: POINTER(UInt32), map: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_DEBUG_IL_TO_NATIVE_MAP_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def EnumJITedFunctions2(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerFunctionEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def GetObjectSize2(self, objectId: UIntPtr, pcSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo5(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo4
    _iid_ = Guid('{07602928-ce38-4b83-81e7-74adaf781214}')
    @commethod(81)
    def GetEventMask2(self, pdwEventsLow: POINTER(UInt32), pdwEventsHigh: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def SetEventMask2(self, dwEventsLow: UInt32, dwEventsHigh: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo6(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo5
    _iid_ = Guid('{f30a070d-bffb-46a7-b1d8-8781ef7b698a}')
    @commethod(83)
    def EnumNgenModuleMethodsInliningThisMethod(self, inlinersModuleId: UIntPtr, inlineeModuleId: UIntPtr, inlineeMethodId: UInt32, incompleteData: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerMethodEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo7(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo6
    _iid_ = Guid('{9aeecc0d-63e0-4187-8c00-e312f503f663}')
    @commethod(84)
    def ApplyMetaData(self, moduleId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def GetInMemorySymbolsLength(self, moduleId: UIntPtr, pCountSymbolBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def ReadInMemorySymbols(self, moduleId: UIntPtr, symbolsReadOffset: UInt32, pSymbolBytes: POINTER(Byte), countSymbolBytes: UInt32, pCountSymbolBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerInfo8(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerInfo7
    _iid_ = Guid('{c5ac80a6-782e-4716-8044-39598c60cfbf}')
    @commethod(87)
    def IsFunctionDynamic(self, functionId: UIntPtr, isDynamic: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def GetFunctionFromIP3(self, ip: POINTER(Byte), functionId: POINTER(UIntPtr), pReJitId: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def GetDynamicFunctionInfo(self, functionId: UIntPtr, moduleId: POINTER(UIntPtr), ppvSig: POINTER(POINTER(Byte)), pbSig: POINTER(UInt32), cchName: UInt32, pcchName: POINTER(UInt32), wszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerMethodEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fccee788-0088-454b-a811-c99f298d1942}')
    @commethod(3)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerMethodEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Next(self, celt: UInt32, elements: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.COR_PRF_METHOD_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerModuleEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b0266d75-2081-4493-af7f-028ba34db891}')
    @commethod(3)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerModuleEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Next(self, celt: UInt32, ids: POINTER(UIntPtr), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerObjectEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c6269bd-2d13-4321-ae12-6686365fd6af}')
    @commethod(3)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerObjectEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Next(self, celt: UInt32, objects: POINTER(UIntPtr), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorProfilerThreadEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{571194f7-25ed-419f-aa8b-7016b3159701}')
    @commethod(3)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.ClrProfiling.ICorProfilerThreadEnum_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Next(self, celt: UInt32, ids: POINTER(UIntPtr), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMethodMalloc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0efb28b-6ee2-4d7b-b983-a75ef7beedb8}')
    @commethod(3)
    def Alloc(self, cb: UInt32) -> VoidPtr: ...
@winfunctype_pointer
def StackSnapshotCallback(funcId: UIntPtr, ip: UIntPtr, frameInfo: UIntPtr, contextSize: UInt32, context: POINTER(Byte), clientData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'COR_DEBUG_IL_TO_NATIVE_MAP')
make_head(_module, 'COR_IL_MAP')
make_head(_module, 'COR_PRF_ASSEMBLY_REFERENCE_INFO')
make_head(_module, 'COR_PRF_CODE_INFO')
make_head(_module, 'COR_PRF_EX_CLAUSE_INFO')
make_head(_module, 'COR_PRF_FUNCTION')
make_head(_module, 'COR_PRF_FUNCTION_ARGUMENT_INFO')
make_head(_module, 'COR_PRF_FUNCTION_ARGUMENT_RANGE')
make_head(_module, 'COR_PRF_GC_GENERATION_RANGE')
make_head(_module, 'COR_PRF_METHOD')
make_head(_module, 'FunctionEnter')
make_head(_module, 'FunctionEnter2')
make_head(_module, 'FunctionEnter3')
make_head(_module, 'FunctionEnter3WithInfo')
make_head(_module, 'FunctionIDMapper')
make_head(_module, 'FunctionIDMapper2')
make_head(_module, 'FunctionIDOrClientID')
make_head(_module, 'FunctionLeave')
make_head(_module, 'FunctionLeave2')
make_head(_module, 'FunctionLeave3')
make_head(_module, 'FunctionLeave3WithInfo')
make_head(_module, 'FunctionTailcall')
make_head(_module, 'FunctionTailcall2')
make_head(_module, 'FunctionTailcall3')
make_head(_module, 'FunctionTailcall3WithInfo')
make_head(_module, 'ICorProfilerAssemblyReferenceProvider')
make_head(_module, 'ICorProfilerCallback')
make_head(_module, 'ICorProfilerCallback2')
make_head(_module, 'ICorProfilerCallback3')
make_head(_module, 'ICorProfilerCallback4')
make_head(_module, 'ICorProfilerCallback5')
make_head(_module, 'ICorProfilerCallback6')
make_head(_module, 'ICorProfilerCallback7')
make_head(_module, 'ICorProfilerCallback8')
make_head(_module, 'ICorProfilerCallback9')
make_head(_module, 'ICorProfilerFunctionControl')
make_head(_module, 'ICorProfilerFunctionEnum')
make_head(_module, 'ICorProfilerInfo')
make_head(_module, 'ICorProfilerInfo2')
make_head(_module, 'ICorProfilerInfo3')
make_head(_module, 'ICorProfilerInfo4')
make_head(_module, 'ICorProfilerInfo5')
make_head(_module, 'ICorProfilerInfo6')
make_head(_module, 'ICorProfilerInfo7')
make_head(_module, 'ICorProfilerInfo8')
make_head(_module, 'ICorProfilerMethodEnum')
make_head(_module, 'ICorProfilerModuleEnum')
make_head(_module, 'ICorProfilerObjectEnum')
make_head(_module, 'ICorProfilerThreadEnum')
make_head(_module, 'IMethodMalloc')
make_head(_module, 'StackSnapshotCallback')
