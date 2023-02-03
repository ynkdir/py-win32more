from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Diagnostics.Debug
import Windows.Win32.System.Js
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
JS_SOURCE_CONTEXT_NONE: UInt64 = 18446744073709551615
if ARCH in 'X64,ARM64':
    @winfunctype('chakra.dll')
    def JsCreateContext(runtime: c_void_p, debugApplication: Windows.Win32.System.Diagnostics.Debug.IDebugApplication64_head, newContext: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X64,ARM64':
    @winfunctype('chakra.dll')
    def JsStartDebugging(debugApplication: Windows.Win32.System.Diagnostics.Debug.IDebugApplication64_head) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateRuntime(attributes: Windows.Win32.System.Js.JsRuntimeAttributes, runtimeVersion: Windows.Win32.System.Js.JsRuntimeVersion, threadService: Windows.Win32.System.Js.JsThreadServiceCallback, runtime: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCollectGarbage(runtime: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDisposeRuntime(runtime: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntimeMemoryUsage(runtime: c_void_p, memoryUsage: POINTER(UIntPtr)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntimeMemoryLimit(runtime: c_void_p, memoryLimit: POINTER(UIntPtr)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeMemoryLimit(runtime: c_void_p, memoryLimit: UIntPtr) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeMemoryAllocationCallback(runtime: c_void_p, callbackState: c_void_p, allocationCallback: Windows.Win32.System.Js.JsMemoryAllocationCallback) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeBeforeCollectCallback(runtime: c_void_p, callbackState: c_void_p, beforeCollectCallback: Windows.Win32.System.Js.JsBeforeCollectCallback) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsAddRef(ref: c_void_p, count: POINTER(UInt32)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRelease(ref: c_void_p, count: POINTER(UInt32)) -> Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X86':
    @winfunctype('chakra.dll')
    def JsCreateContext(runtime: c_void_p, debugApplication: Windows.Win32.System.Diagnostics.Debug.IDebugApplication32_head, newContext: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetCurrentContext(currentContext: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetCurrentContext(context: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntime(context: c_void_p, runtime: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X86':
    @winfunctype('chakra.dll')
    def JsStartDebugging(debugApplication: Windows.Win32.System.Diagnostics.Debug.IDebugApplication32_head) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIdle(nextIdleTick: POINTER(UInt32)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsParseScript(script: Windows.Win32.Foundation.PWSTR, sourceContext: UIntPtr, sourceUrl: Windows.Win32.Foundation.PWSTR, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRunScript(script: Windows.Win32.Foundation.PWSTR, sourceContext: UIntPtr, sourceUrl: Windows.Win32.Foundation.PWSTR, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSerializeScript(script: Windows.Win32.Foundation.PWSTR, buffer: c_char_p_no, bufferSize: POINTER(UInt32)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsParseSerializedScript(script: Windows.Win32.Foundation.PWSTR, buffer: c_char_p_no, sourceContext: UIntPtr, sourceUrl: Windows.Win32.Foundation.PWSTR, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRunSerializedScript(script: Windows.Win32.Foundation.PWSTR, buffer: c_char_p_no, sourceContext: UIntPtr, sourceUrl: Windows.Win32.Foundation.PWSTR, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPropertyIdFromName(name: Windows.Win32.Foundation.PWSTR, propertyId: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPropertyNameFromId(propertyId: c_void_p, name: POINTER(POINTER(UInt16))) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetUndefinedValue(undefinedValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetNullValue(nullValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetTrueValue(trueValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetFalseValue(falseValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsBoolToBoolean(value: Byte, booleanValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsBooleanToBool(value: c_void_p, boolValue: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToBoolean(value: c_void_p, booleanValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetValueType(value: c_void_p, type: POINTER(Windows.Win32.System.Js.JsValueType)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDoubleToNumber(doubleValue: Double, value: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIntToNumber(intValue: Int32, value: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsNumberToDouble(value: c_void_p, doubleValue: POINTER(Double)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToNumber(value: c_void_p, numberValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetStringLength(stringValue: c_void_p, length: POINTER(Int32)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsPointerToString(stringValue: Windows.Win32.Foundation.PWSTR, stringLength: UIntPtr, value: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStringToPointer(value: c_void_p, stringValue: POINTER(POINTER(UInt16)), stringLength: POINTER(UIntPtr)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToString(value: c_void_p, stringValue: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsVariantToValue(variant: POINTER(Windows.Win32.System.Com.VARIANT_head), value: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsValueToVariant(object: c_void_p, variant: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetGlobalObject(globalObject: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateObject(object: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateExternalObject(data: c_void_p, finalizeCallback: Windows.Win32.System.Js.JsFinalizeCallback, object: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToObject(value: c_void_p, object: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPrototype(object: c_void_p, prototypeObject: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetPrototype(object: c_void_p, prototypeObject: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetExtensionAllowed(object: c_void_p, value: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsPreventExtension(object: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetProperty(object: c_void_p, propertyId: c_void_p, value: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetOwnPropertyDescriptor(object: c_void_p, propertyId: c_void_p, propertyDescriptor: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetOwnPropertyNames(object: c_void_p, propertyNames: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetProperty(object: c_void_p, propertyId: c_void_p, value: c_void_p, useStrictRules: Byte) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasProperty(object: c_void_p, propertyId: c_void_p, hasProperty: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDeleteProperty(object: c_void_p, propertyId: c_void_p, useStrictRules: Byte, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDefineProperty(object: c_void_p, propertyId: c_void_p, propertyDescriptor: c_void_p, result: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasIndexedProperty(object: c_void_p, index: c_void_p, result: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetIndexedProperty(object: c_void_p, index: c_void_p, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetIndexedProperty(object: c_void_p, index: c_void_p, value: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDeleteIndexedProperty(object: c_void_p, index: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEquals(object1: c_void_p, object2: c_void_p, result: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStrictEquals(object1: c_void_p, object2: c_void_p, result: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasExternalData(object: c_void_p, value: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetExternalData(object: c_void_p, externalData: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetExternalData(object: c_void_p, externalData: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateArray(length: UInt32, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCallFunction(function: c_void_p, arguments: POINTER(c_void_p), argumentCount: UInt16, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConstructObject(function: c_void_p, arguments: POINTER(c_void_p), argumentCount: UInt16, result: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateFunction(nativeFunction: Windows.Win32.System.Js.JsNativeFunction, callbackState: c_void_p, function: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateRangeError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateReferenceError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateSyntaxError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateTypeError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateURIError(message: c_void_p, error: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasException(hasException: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetAndClearException(exception: POINTER(c_void_p)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetException(exception: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDisableRuntimeExecution(runtime: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEnableRuntimeExecution(runtime: c_void_p) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIsRuntimeExecutionDisabled(runtime: c_void_p, isDisabled: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStartProfiling(callback: Windows.Win32.System.Diagnostics.Debug.IActiveScriptProfilerCallback_head, eventMask: Windows.Win32.System.Diagnostics.Debug.PROFILER_EVENT_MASK, context: UInt32) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStopProfiling(reason: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEnumerateHeap(enumerator: POINTER(Windows.Win32.System.Diagnostics.Debug.IActiveScriptProfilerHeapEnum_head)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIsEnumeratingHeap(isEnumeratingHeap: POINTER(Boolean)) -> Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype_pointer
def JsBackgroundWorkItemCallback(callbackState: c_void_p) -> Void: ...
@winfunctype_pointer
def JsBeforeCollectCallback(callbackState: c_void_p) -> Void: ...
JsErrorCode = UInt32
JsErrorCode_JsNoError: JsErrorCode = 0
JsErrorCode_JsErrorCategoryUsage: JsErrorCode = 65536
JsErrorCode_JsErrorInvalidArgument: JsErrorCode = 65537
JsErrorCode_JsErrorNullArgument: JsErrorCode = 65538
JsErrorCode_JsErrorNoCurrentContext: JsErrorCode = 65539
JsErrorCode_JsErrorInExceptionState: JsErrorCode = 65540
JsErrorCode_JsErrorNotImplemented: JsErrorCode = 65541
JsErrorCode_JsErrorWrongThread: JsErrorCode = 65542
JsErrorCode_JsErrorRuntimeInUse: JsErrorCode = 65543
JsErrorCode_JsErrorBadSerializedScript: JsErrorCode = 65544
JsErrorCode_JsErrorInDisabledState: JsErrorCode = 65545
JsErrorCode_JsErrorCannotDisableExecution: JsErrorCode = 65546
JsErrorCode_JsErrorHeapEnumInProgress: JsErrorCode = 65547
JsErrorCode_JsErrorArgumentNotObject: JsErrorCode = 65548
JsErrorCode_JsErrorInProfileCallback: JsErrorCode = 65549
JsErrorCode_JsErrorInThreadServiceCallback: JsErrorCode = 65550
JsErrorCode_JsErrorCannotSerializeDebugScript: JsErrorCode = 65551
JsErrorCode_JsErrorAlreadyDebuggingContext: JsErrorCode = 65552
JsErrorCode_JsErrorAlreadyProfilingContext: JsErrorCode = 65553
JsErrorCode_JsErrorIdleNotEnabled: JsErrorCode = 65554
JsErrorCode_JsErrorCategoryEngine: JsErrorCode = 131072
JsErrorCode_JsErrorOutOfMemory: JsErrorCode = 131073
JsErrorCode_JsErrorCategoryScript: JsErrorCode = 196608
JsErrorCode_JsErrorScriptException: JsErrorCode = 196609
JsErrorCode_JsErrorScriptCompile: JsErrorCode = 196610
JsErrorCode_JsErrorScriptTerminated: JsErrorCode = 196611
JsErrorCode_JsErrorScriptEvalDisabled: JsErrorCode = 196612
JsErrorCode_JsErrorCategoryFatal: JsErrorCode = 262144
JsErrorCode_JsErrorFatal: JsErrorCode = 262145
@winfunctype_pointer
def JsFinalizeCallback(data: c_void_p) -> Void: ...
@winfunctype_pointer
def JsMemoryAllocationCallback(callbackState: c_void_p, allocationEvent: Windows.Win32.System.Js.JsMemoryEventType, allocationSize: UIntPtr) -> Boolean: ...
JsMemoryEventType = Int32
JsMemoryEventType_JsMemoryAllocate: JsMemoryEventType = 0
JsMemoryEventType_JsMemoryFree: JsMemoryEventType = 1
JsMemoryEventType_JsMemoryFailure: JsMemoryEventType = 2
@winfunctype_pointer
def JsNativeFunction(callee: c_void_p, isConstructCall: Boolean, arguments: POINTER(c_void_p), argumentCount: UInt16, callbackState: c_void_p) -> c_void_p: ...
JsRuntimeAttributes = Int32
JsRuntimeAttributes_JsRuntimeAttributeNone: JsRuntimeAttributes = 0
JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork: JsRuntimeAttributes = 1
JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt: JsRuntimeAttributes = 2
JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing: JsRuntimeAttributes = 4
JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration: JsRuntimeAttributes = 8
JsRuntimeAttributes_JsRuntimeAttributeDisableEval: JsRuntimeAttributes = 16
JsRuntimeVersion = Int32
JsRuntimeVersion_JsRuntimeVersion10: JsRuntimeVersion = 0
JsRuntimeVersion_JsRuntimeVersion11: JsRuntimeVersion = 1
JsRuntimeVersion_JsRuntimeVersionEdge: JsRuntimeVersion = -1
@winfunctype_pointer
def JsThreadServiceCallback(callback: Windows.Win32.System.Js.JsBackgroundWorkItemCallback, callbackState: c_void_p) -> Boolean: ...
JsValueType = Int32
JsValueType_JsUndefined: JsValueType = 0
JsValueType_JsNull: JsValueType = 1
JsValueType_JsNumber: JsValueType = 2
JsValueType_JsString: JsValueType = 3
JsValueType_JsBoolean: JsValueType = 4
JsValueType_JsObject: JsValueType = 5
JsValueType_JsFunction: JsValueType = 6
JsValueType_JsError: JsValueType = 7
JsValueType_JsArray: JsValueType = 8
make_head(_module, 'JsBackgroundWorkItemCallback')
make_head(_module, 'JsBeforeCollectCallback')
make_head(_module, 'JsFinalizeCallback')
make_head(_module, 'JsMemoryAllocationCallback')
make_head(_module, 'JsNativeFunction')
make_head(_module, 'JsThreadServiceCallback')
__all__ = [
    "JS_SOURCE_CONTEXT_NONE",
    "JsAddRef",
    "JsBackgroundWorkItemCallback",
    "JsBeforeCollectCallback",
    "JsBoolToBoolean",
    "JsBooleanToBool",
    "JsCallFunction",
    "JsCollectGarbage",
    "JsConstructObject",
    "JsConvertValueToBoolean",
    "JsConvertValueToNumber",
    "JsConvertValueToObject",
    "JsConvertValueToString",
    "JsCreateArray",
    "JsCreateContext",
    "JsCreateError",
    "JsCreateExternalObject",
    "JsCreateFunction",
    "JsCreateObject",
    "JsCreateRangeError",
    "JsCreateReferenceError",
    "JsCreateRuntime",
    "JsCreateSyntaxError",
    "JsCreateTypeError",
    "JsCreateURIError",
    "JsDefineProperty",
    "JsDeleteIndexedProperty",
    "JsDeleteProperty",
    "JsDisableRuntimeExecution",
    "JsDisposeRuntime",
    "JsDoubleToNumber",
    "JsEnableRuntimeExecution",
    "JsEnumerateHeap",
    "JsEquals",
    "JsErrorCode",
    "JsErrorCode_JsErrorAlreadyDebuggingContext",
    "JsErrorCode_JsErrorAlreadyProfilingContext",
    "JsErrorCode_JsErrorArgumentNotObject",
    "JsErrorCode_JsErrorBadSerializedScript",
    "JsErrorCode_JsErrorCannotDisableExecution",
    "JsErrorCode_JsErrorCannotSerializeDebugScript",
    "JsErrorCode_JsErrorCategoryEngine",
    "JsErrorCode_JsErrorCategoryFatal",
    "JsErrorCode_JsErrorCategoryScript",
    "JsErrorCode_JsErrorCategoryUsage",
    "JsErrorCode_JsErrorFatal",
    "JsErrorCode_JsErrorHeapEnumInProgress",
    "JsErrorCode_JsErrorIdleNotEnabled",
    "JsErrorCode_JsErrorInDisabledState",
    "JsErrorCode_JsErrorInExceptionState",
    "JsErrorCode_JsErrorInProfileCallback",
    "JsErrorCode_JsErrorInThreadServiceCallback",
    "JsErrorCode_JsErrorInvalidArgument",
    "JsErrorCode_JsErrorNoCurrentContext",
    "JsErrorCode_JsErrorNotImplemented",
    "JsErrorCode_JsErrorNullArgument",
    "JsErrorCode_JsErrorOutOfMemory",
    "JsErrorCode_JsErrorRuntimeInUse",
    "JsErrorCode_JsErrorScriptCompile",
    "JsErrorCode_JsErrorScriptEvalDisabled",
    "JsErrorCode_JsErrorScriptException",
    "JsErrorCode_JsErrorScriptTerminated",
    "JsErrorCode_JsErrorWrongThread",
    "JsErrorCode_JsNoError",
    "JsFinalizeCallback",
    "JsGetAndClearException",
    "JsGetCurrentContext",
    "JsGetExtensionAllowed",
    "JsGetExternalData",
    "JsGetFalseValue",
    "JsGetGlobalObject",
    "JsGetIndexedProperty",
    "JsGetNullValue",
    "JsGetOwnPropertyDescriptor",
    "JsGetOwnPropertyNames",
    "JsGetProperty",
    "JsGetPropertyIdFromName",
    "JsGetPropertyNameFromId",
    "JsGetPrototype",
    "JsGetRuntime",
    "JsGetRuntimeMemoryLimit",
    "JsGetRuntimeMemoryUsage",
    "JsGetStringLength",
    "JsGetTrueValue",
    "JsGetUndefinedValue",
    "JsGetValueType",
    "JsHasException",
    "JsHasExternalData",
    "JsHasIndexedProperty",
    "JsHasProperty",
    "JsIdle",
    "JsIntToNumber",
    "JsIsEnumeratingHeap",
    "JsIsRuntimeExecutionDisabled",
    "JsMemoryAllocationCallback",
    "JsMemoryEventType",
    "JsMemoryEventType_JsMemoryAllocate",
    "JsMemoryEventType_JsMemoryFailure",
    "JsMemoryEventType_JsMemoryFree",
    "JsNativeFunction",
    "JsNumberToDouble",
    "JsParseScript",
    "JsParseSerializedScript",
    "JsPointerToString",
    "JsPreventExtension",
    "JsRelease",
    "JsRunScript",
    "JsRunSerializedScript",
    "JsRuntimeAttributes",
    "JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableEval",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration",
    "JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing",
    "JsRuntimeAttributes_JsRuntimeAttributeNone",
    "JsRuntimeVersion",
    "JsRuntimeVersion_JsRuntimeVersion10",
    "JsRuntimeVersion_JsRuntimeVersion11",
    "JsRuntimeVersion_JsRuntimeVersionEdge",
    "JsSerializeScript",
    "JsSetCurrentContext",
    "JsSetException",
    "JsSetExternalData",
    "JsSetIndexedProperty",
    "JsSetProperty",
    "JsSetPrototype",
    "JsSetRuntimeBeforeCollectCallback",
    "JsSetRuntimeMemoryAllocationCallback",
    "JsSetRuntimeMemoryLimit",
    "JsStartDebugging",
    "JsStartProfiling",
    "JsStopProfiling",
    "JsStrictEquals",
    "JsStringToPointer",
    "JsThreadServiceCallback",
    "JsValueToVariant",
    "JsValueType",
    "JsValueType_JsArray",
    "JsValueType_JsBoolean",
    "JsValueType_JsError",
    "JsValueType_JsFunction",
    "JsValueType_JsNull",
    "JsValueType_JsNumber",
    "JsValueType_JsObject",
    "JsValueType_JsString",
    "JsValueType_JsUndefined",
    "JsVariantToValue",
]
_arch_optional = [
]
