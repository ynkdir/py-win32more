from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Diagnostics.Debug
import win32more.System.Js

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
JS_SOURCE_CONTEXT_NONE = 18446744073709551615
JsRuntimeVersion = Int32
JsRuntimeVersion_JsRuntimeVersion10 = 0
JsRuntimeVersion_JsRuntimeVersion11 = 1
JsRuntimeVersion_JsRuntimeVersionEdge = -1
JsErrorCode = UInt32
JsErrorCode_JsNoError = 0
JsErrorCode_JsErrorCategoryUsage = 65536
JsErrorCode_JsErrorInvalidArgument = 65537
JsErrorCode_JsErrorNullArgument = 65538
JsErrorCode_JsErrorNoCurrentContext = 65539
JsErrorCode_JsErrorInExceptionState = 65540
JsErrorCode_JsErrorNotImplemented = 65541
JsErrorCode_JsErrorWrongThread = 65542
JsErrorCode_JsErrorRuntimeInUse = 65543
JsErrorCode_JsErrorBadSerializedScript = 65544
JsErrorCode_JsErrorInDisabledState = 65545
JsErrorCode_JsErrorCannotDisableExecution = 65546
JsErrorCode_JsErrorHeapEnumInProgress = 65547
JsErrorCode_JsErrorArgumentNotObject = 65548
JsErrorCode_JsErrorInProfileCallback = 65549
JsErrorCode_JsErrorInThreadServiceCallback = 65550
JsErrorCode_JsErrorCannotSerializeDebugScript = 65551
JsErrorCode_JsErrorAlreadyDebuggingContext = 65552
JsErrorCode_JsErrorAlreadyProfilingContext = 65553
JsErrorCode_JsErrorIdleNotEnabled = 65554
JsErrorCode_JsErrorCategoryEngine = 131072
JsErrorCode_JsErrorOutOfMemory = 131073
JsErrorCode_JsErrorCategoryScript = 196608
JsErrorCode_JsErrorScriptException = 196609
JsErrorCode_JsErrorScriptCompile = 196610
JsErrorCode_JsErrorScriptTerminated = 196611
JsErrorCode_JsErrorScriptEvalDisabled = 196612
JsErrorCode_JsErrorCategoryFatal = 262144
JsErrorCode_JsErrorFatal = 262145
JsRuntimeAttributes = Int32
JsRuntimeAttributes_JsRuntimeAttributeNone = 0
JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork = 1
JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt = 2
JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing = 4
JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration = 8
JsRuntimeAttributes_JsRuntimeAttributeDisableEval = 16
JsMemoryEventType = Int32
JsMemoryEventType_JsMemoryAllocate = 0
JsMemoryEventType_JsMemoryFree = 1
JsMemoryEventType_JsMemoryFailure = 2
def _define_JsMemoryAllocationCallback():
    return CFUNCTYPE(Boolean,c_void_p,win32more.System.Js.JsMemoryEventType,UIntPtr, use_last_error=False)
def _define_JsBeforeCollectCallback():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_JsBackgroundWorkItemCallback():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_JsThreadServiceCallback():
    return CFUNCTYPE(Boolean,win32more.System.Js.JsBackgroundWorkItemCallback,c_void_p, use_last_error=False)
JsValueType = Int32
JsValueType_JsUndefined = 0
JsValueType_JsNull = 1
JsValueType_JsNumber = 2
JsValueType_JsString = 3
JsValueType_JsBoolean = 4
JsValueType_JsObject = 5
JsValueType_JsFunction = 6
JsValueType_JsError = 7
JsValueType_JsArray = 8
def _define_JsFinalizeCallback():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_JsNativeFunction():
    return CFUNCTYPE(c_void_p,c_void_p,Boolean,POINTER(c_void_p),UInt16,c_void_p, use_last_error=False)
def _define_JsCreateRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Js.JsRuntimeAttributes,win32more.System.Js.JsRuntimeVersion,win32more.System.Js.JsThreadServiceCallback,POINTER(c_void_p), use_last_error=False)(("JsCreateRuntime", windll["chakra"]), ((1, 'attributes'),(1, 'runtimeVersion'),(1, 'threadService'),(1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCollectGarbage():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsCollectGarbage", windll["chakra"]), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDisposeRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsDisposeRuntime", windll["chakra"]), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntimeMemoryUsage():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UIntPtr), use_last_error=False)(("JsGetRuntimeMemoryUsage", windll["chakra"]), ((1, 'runtime'),(1, 'memoryUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntimeMemoryLimit():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UIntPtr), use_last_error=False)(("JsGetRuntimeMemoryLimit", windll["chakra"]), ((1, 'runtime'),(1, 'memoryLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeMemoryLimit():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,UIntPtr, use_last_error=False)(("JsSetRuntimeMemoryLimit", windll["chakra"]), ((1, 'runtime'),(1, 'memoryLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeMemoryAllocationCallback():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,win32more.System.Js.JsMemoryAllocationCallback, use_last_error=False)(("JsSetRuntimeMemoryAllocationCallback", windll["chakra"]), ((1, 'runtime'),(1, 'callbackState'),(1, 'allocationCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeBeforeCollectCallback():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,win32more.System.Js.JsBeforeCollectCallback, use_last_error=False)(("JsSetRuntimeBeforeCollectCallback", windll["chakra"]), ((1, 'runtime'),(1, 'callbackState'),(1, 'beforeCollectCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsAddRef():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UInt32), use_last_error=False)(("JsAddRef", windll["chakra"]), ((1, 'ref'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRelease():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UInt32), use_last_error=False)(("JsRelease", windll["chakra"]), ((1, 'ref'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,win32more.System.Diagnostics.Debug.IDebugApplication64_head,POINTER(c_void_p), use_last_error=False)(("JsCreateContext", windll["chakra"]), ((1, 'runtime'),(1, 'debugApplication'),(1, 'newContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetCurrentContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetCurrentContext", windll["chakra"]), ((1, 'currentContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetCurrentContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsSetCurrentContext", windll["chakra"]), ((1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetRuntime", windll["chakra"]), ((1, 'context'),(1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStartDebugging():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Diagnostics.Debug.IDebugApplication64_head, use_last_error=False)(("JsStartDebugging", windll["chakra"]), ((1, 'debugApplication'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIdle():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(UInt32), use_last_error=False)(("JsIdle", windll["chakra"]), ((1, 'nextIdleTick'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsParseScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("JsParseScript", windll["chakra"]), ((1, 'script'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRunScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("JsRunScript", windll["chakra"]), ((1, 'script'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSerializeScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("JsSerializeScript", windll["chakra"]), ((1, 'script'),(1, 'buffer'),(1, 'bufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsParseSerializedScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,c_char_p_no,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("JsParseSerializedScript", windll["chakra"]), ((1, 'script'),(1, 'buffer'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRunSerializedScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,c_char_p_no,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("JsRunSerializedScript", windll["chakra"]), ((1, 'script'),(1, 'buffer'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPropertyIdFromName():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("JsGetPropertyIdFromName", windll["chakra"]), ((1, 'name'),(1, 'propertyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPropertyNameFromId():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(POINTER(UInt16)), use_last_error=False)(("JsGetPropertyNameFromId", windll["chakra"]), ((1, 'propertyId'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetUndefinedValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetUndefinedValue", windll["chakra"]), ((1, 'undefinedValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetNullValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetNullValue", windll["chakra"]), ((1, 'nullValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetTrueValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetTrueValue", windll["chakra"]), ((1, 'trueValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetFalseValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetFalseValue", windll["chakra"]), ((1, 'falseValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsBoolToBoolean():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Byte,POINTER(c_void_p), use_last_error=False)(("JsBoolToBoolean", windll["chakra"]), ((1, 'value'),(1, 'booleanValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsBooleanToBool():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean), use_last_error=False)(("JsBooleanToBool", windll["chakra"]), ((1, 'value'),(1, 'boolValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToBoolean():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsConvertValueToBoolean", windll["chakra"]), ((1, 'value'),(1, 'booleanValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetValueType():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(win32more.System.Js.JsValueType), use_last_error=False)(("JsGetValueType", windll["chakra"]), ((1, 'value'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDoubleToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Double,POINTER(c_void_p), use_last_error=False)(("JsDoubleToNumber", windll["chakra"]), ((1, 'doubleValue'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIntToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Int32,POINTER(c_void_p), use_last_error=False)(("JsIntToNumber", windll["chakra"]), ((1, 'intValue'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsNumberToDouble():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Double), use_last_error=False)(("JsNumberToDouble", windll["chakra"]), ((1, 'value'),(1, 'doubleValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsConvertValueToNumber", windll["chakra"]), ((1, 'value'),(1, 'numberValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetStringLength():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Int32), use_last_error=False)(("JsGetStringLength", windll["chakra"]), ((1, 'stringValue'),(1, 'length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsPointerToString():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(Char),UIntPtr,POINTER(c_void_p), use_last_error=False)(("JsPointerToString", windll["chakra"]), ((1, 'stringValue'),(1, 'stringLength'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStringToPointer():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(POINTER(UInt16)),POINTER(UIntPtr), use_last_error=False)(("JsStringToPointer", windll["chakra"]), ((1, 'value'),(1, 'stringValue'),(1, 'stringLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToString():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsConvertValueToString", windll["chakra"]), ((1, 'value'),(1, 'stringValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsVariantToValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(win32more.System.Com.VARIANT_head),POINTER(c_void_p), use_last_error=False)(("JsVariantToValue", windll["chakra"]), ((1, 'variant'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsValueToVariant():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("JsValueToVariant", windll["chakra"]), ((1, 'object'),(1, 'variant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetGlobalObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetGlobalObject", windll["chakra"]), ((1, 'globalObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsCreateObject", windll["chakra"]), ((1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateExternalObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,win32more.System.Js.JsFinalizeCallback,POINTER(c_void_p), use_last_error=False)(("JsCreateExternalObject", windll["chakra"]), ((1, 'data'),(1, 'finalizeCallback'),(1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsConvertValueToObject", windll["chakra"]), ((1, 'value'),(1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPrototype():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetPrototype", windll["chakra"]), ((1, 'object'),(1, 'prototypeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetPrototype():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p, use_last_error=False)(("JsSetPrototype", windll["chakra"]), ((1, 'object'),(1, 'prototypeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetExtensionAllowed():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean), use_last_error=False)(("JsGetExtensionAllowed", windll["chakra"]), ((1, 'object'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsPreventExtension():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsPreventExtension", windll["chakra"]), ((1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetProperty", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetOwnPropertyDescriptor():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetOwnPropertyDescriptor", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'propertyDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetOwnPropertyNames():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetOwnPropertyNames", windll["chakra"]), ((1, 'object'),(1, 'propertyNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p,Byte, use_last_error=False)(("JsSetProperty", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'value'),(1, 'useStrictRules'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean), use_last_error=False)(("JsHasProperty", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'hasProperty'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDeleteProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,Byte,POINTER(c_void_p), use_last_error=False)(("JsDeleteProperty", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'useStrictRules'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDefineProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p,POINTER(Boolean), use_last_error=False)(("JsDefineProperty", windll["chakra"]), ((1, 'object'),(1, 'propertyId'),(1, 'propertyDescriptor'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean), use_last_error=False)(("JsHasIndexedProperty", windll["chakra"]), ((1, 'object'),(1, 'index'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetIndexedProperty", windll["chakra"]), ((1, 'object'),(1, 'index'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p, use_last_error=False)(("JsSetIndexedProperty", windll["chakra"]), ((1, 'object'),(1, 'index'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDeleteIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p, use_last_error=False)(("JsDeleteIndexedProperty", windll["chakra"]), ((1, 'object'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEquals():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean), use_last_error=False)(("JsEquals", windll["chakra"]), ((1, 'object1'),(1, 'object2'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStrictEquals():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean), use_last_error=False)(("JsStrictEquals", windll["chakra"]), ((1, 'object1'),(1, 'object2'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean), use_last_error=False)(("JsHasExternalData", windll["chakra"]), ((1, 'object'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsGetExternalData", windll["chakra"]), ((1, 'object'),(1, 'externalData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p, use_last_error=False)(("JsSetExternalData", windll["chakra"]), ((1, 'object'),(1, 'externalData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateArray():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,UInt32,POINTER(c_void_p), use_last_error=False)(("JsCreateArray", windll["chakra"]), ((1, 'length'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCallFunction():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p),UInt16,POINTER(c_void_p), use_last_error=False)(("JsCallFunction", windll["chakra"]), ((1, 'function'),(1, 'arguments'),(1, 'argumentCount'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConstructObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p),UInt16,POINTER(c_void_p), use_last_error=False)(("JsConstructObject", windll["chakra"]), ((1, 'function'),(1, 'arguments'),(1, 'argumentCount'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateFunction():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Js.JsNativeFunction,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateFunction", windll["chakra"]), ((1, 'nativeFunction'),(1, 'callbackState'),(1, 'function'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateRangeError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateRangeError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateReferenceError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateReferenceError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateSyntaxError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateSyntaxError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateTypeError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateTypeError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateURIError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p), use_last_error=False)(("JsCreateURIError", windll["chakra"]), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(Boolean), use_last_error=False)(("JsHasException", windll["chakra"]), ((1, 'hasException'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetAndClearException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p), use_last_error=False)(("JsGetAndClearException", windll["chakra"]), ((1, 'exception'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsSetException", windll["chakra"]), ((1, 'exception'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDisableRuntimeExecution():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsDisableRuntimeExecution", windll["chakra"]), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEnableRuntimeExecution():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p, use_last_error=False)(("JsEnableRuntimeExecution", windll["chakra"]), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIsRuntimeExecutionDisabled():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean), use_last_error=False)(("JsIsRuntimeExecutionDisabled", windll["chakra"]), ((1, 'runtime'),(1, 'isDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStartProfiling():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Diagnostics.Debug.IActiveScriptProfilerCallback_head,win32more.System.Diagnostics.Debug.PROFILER_EVENT_MASK,UInt32, use_last_error=False)(("JsStartProfiling", windll["chakra"]), ((1, 'callback'),(1, 'eventMask'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStopProfiling():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.HRESULT, use_last_error=False)(("JsStopProfiling", windll["chakra"]), ((1, 'reason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEnumerateHeap():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(win32more.System.Diagnostics.Debug.IActiveScriptProfilerHeapEnum_head), use_last_error=False)(("JsEnumerateHeap", windll["chakra"]), ((1, 'enumerator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIsEnumeratingHeap():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(Boolean), use_last_error=False)(("JsIsEnumeratingHeap", windll["chakra"]), ((1, 'isEnumeratingHeap'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "JS_SOURCE_CONTEXT_NONE",
    "JsRuntimeVersion",
    "JsRuntimeVersion_JsRuntimeVersion10",
    "JsRuntimeVersion_JsRuntimeVersion11",
    "JsRuntimeVersion_JsRuntimeVersionEdge",
    "JsErrorCode",
    "JsErrorCode_JsNoError",
    "JsErrorCode_JsErrorCategoryUsage",
    "JsErrorCode_JsErrorInvalidArgument",
    "JsErrorCode_JsErrorNullArgument",
    "JsErrorCode_JsErrorNoCurrentContext",
    "JsErrorCode_JsErrorInExceptionState",
    "JsErrorCode_JsErrorNotImplemented",
    "JsErrorCode_JsErrorWrongThread",
    "JsErrorCode_JsErrorRuntimeInUse",
    "JsErrorCode_JsErrorBadSerializedScript",
    "JsErrorCode_JsErrorInDisabledState",
    "JsErrorCode_JsErrorCannotDisableExecution",
    "JsErrorCode_JsErrorHeapEnumInProgress",
    "JsErrorCode_JsErrorArgumentNotObject",
    "JsErrorCode_JsErrorInProfileCallback",
    "JsErrorCode_JsErrorInThreadServiceCallback",
    "JsErrorCode_JsErrorCannotSerializeDebugScript",
    "JsErrorCode_JsErrorAlreadyDebuggingContext",
    "JsErrorCode_JsErrorAlreadyProfilingContext",
    "JsErrorCode_JsErrorIdleNotEnabled",
    "JsErrorCode_JsErrorCategoryEngine",
    "JsErrorCode_JsErrorOutOfMemory",
    "JsErrorCode_JsErrorCategoryScript",
    "JsErrorCode_JsErrorScriptException",
    "JsErrorCode_JsErrorScriptCompile",
    "JsErrorCode_JsErrorScriptTerminated",
    "JsErrorCode_JsErrorScriptEvalDisabled",
    "JsErrorCode_JsErrorCategoryFatal",
    "JsErrorCode_JsErrorFatal",
    "JsRuntimeAttributes",
    "JsRuntimeAttributes_JsRuntimeAttributeNone",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork",
    "JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt",
    "JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration",
    "JsRuntimeAttributes_JsRuntimeAttributeDisableEval",
    "JsMemoryEventType",
    "JsMemoryEventType_JsMemoryAllocate",
    "JsMemoryEventType_JsMemoryFree",
    "JsMemoryEventType_JsMemoryFailure",
    "JsMemoryAllocationCallback",
    "JsBeforeCollectCallback",
    "JsBackgroundWorkItemCallback",
    "JsThreadServiceCallback",
    "JsValueType",
    "JsValueType_JsUndefined",
    "JsValueType_JsNull",
    "JsValueType_JsNumber",
    "JsValueType_JsString",
    "JsValueType_JsBoolean",
    "JsValueType_JsObject",
    "JsValueType_JsFunction",
    "JsValueType_JsError",
    "JsValueType_JsArray",
    "JsFinalizeCallback",
    "JsNativeFunction",
    "JsCreateRuntime",
    "JsCollectGarbage",
    "JsDisposeRuntime",
    "JsGetRuntimeMemoryUsage",
    "JsGetRuntimeMemoryLimit",
    "JsSetRuntimeMemoryLimit",
    "JsSetRuntimeMemoryAllocationCallback",
    "JsSetRuntimeBeforeCollectCallback",
    "JsAddRef",
    "JsRelease",
    "JsCreateContext",
    "JsGetCurrentContext",
    "JsSetCurrentContext",
    "JsGetRuntime",
    "JsStartDebugging",
    "JsIdle",
    "JsParseScript",
    "JsRunScript",
    "JsSerializeScript",
    "JsParseSerializedScript",
    "JsRunSerializedScript",
    "JsGetPropertyIdFromName",
    "JsGetPropertyNameFromId",
    "JsGetUndefinedValue",
    "JsGetNullValue",
    "JsGetTrueValue",
    "JsGetFalseValue",
    "JsBoolToBoolean",
    "JsBooleanToBool",
    "JsConvertValueToBoolean",
    "JsGetValueType",
    "JsDoubleToNumber",
    "JsIntToNumber",
    "JsNumberToDouble",
    "JsConvertValueToNumber",
    "JsGetStringLength",
    "JsPointerToString",
    "JsStringToPointer",
    "JsConvertValueToString",
    "JsVariantToValue",
    "JsValueToVariant",
    "JsGetGlobalObject",
    "JsCreateObject",
    "JsCreateExternalObject",
    "JsConvertValueToObject",
    "JsGetPrototype",
    "JsSetPrototype",
    "JsGetExtensionAllowed",
    "JsPreventExtension",
    "JsGetProperty",
    "JsGetOwnPropertyDescriptor",
    "JsGetOwnPropertyNames",
    "JsSetProperty",
    "JsHasProperty",
    "JsDeleteProperty",
    "JsDefineProperty",
    "JsHasIndexedProperty",
    "JsGetIndexedProperty",
    "JsSetIndexedProperty",
    "JsDeleteIndexedProperty",
    "JsEquals",
    "JsStrictEquals",
    "JsHasExternalData",
    "JsGetExternalData",
    "JsSetExternalData",
    "JsCreateArray",
    "JsCallFunction",
    "JsConstructObject",
    "JsCreateFunction",
    "JsCreateError",
    "JsCreateRangeError",
    "JsCreateReferenceError",
    "JsCreateSyntaxError",
    "JsCreateTypeError",
    "JsCreateURIError",
    "JsHasException",
    "JsGetAndClearException",
    "JsSetException",
    "JsDisableRuntimeExecution",
    "JsEnableRuntimeExecution",
    "JsIsRuntimeExecutionDisabled",
    "JsStartProfiling",
    "JsStopProfiling",
    "JsEnumerateHeap",
    "JsIsEnumeratingHeap",
]
