from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Diagnostics.Debug
import win32more.System.Js
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
JS_SOURCE_CONTEXT_NONE = 18446744073709551615
def _define_JsCreateContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,win32more.System.Diagnostics.Debug.IDebugApplication64_head,POINTER(c_void_p))(('JsCreateContext', windll['chakra.dll']), ((1, 'runtime'),(1, 'debugApplication'),(1, 'newContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStartDebugging():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Diagnostics.Debug.IDebugApplication64_head)(('JsStartDebugging', windll['chakra.dll']), ((1, 'debugApplication'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Js.JsRuntimeAttributes,win32more.System.Js.JsRuntimeVersion,win32more.System.Js.JsThreadServiceCallback,POINTER(c_void_p))(('JsCreateRuntime', windll['chakra.dll']), ((1, 'attributes'),(1, 'runtimeVersion'),(1, 'threadService'),(1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCollectGarbage():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsCollectGarbage', windll['chakra.dll']), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDisposeRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsDisposeRuntime', windll['chakra.dll']), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntimeMemoryUsage():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UIntPtr))(('JsGetRuntimeMemoryUsage', windll['chakra.dll']), ((1, 'runtime'),(1, 'memoryUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntimeMemoryLimit():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UIntPtr))(('JsGetRuntimeMemoryLimit', windll['chakra.dll']), ((1, 'runtime'),(1, 'memoryLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeMemoryLimit():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,UIntPtr)(('JsSetRuntimeMemoryLimit', windll['chakra.dll']), ((1, 'runtime'),(1, 'memoryLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeMemoryAllocationCallback():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,win32more.System.Js.JsMemoryAllocationCallback)(('JsSetRuntimeMemoryAllocationCallback', windll['chakra.dll']), ((1, 'runtime'),(1, 'callbackState'),(1, 'allocationCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetRuntimeBeforeCollectCallback():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,win32more.System.Js.JsBeforeCollectCallback)(('JsSetRuntimeBeforeCollectCallback', windll['chakra.dll']), ((1, 'runtime'),(1, 'callbackState'),(1, 'beforeCollectCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsAddRef():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UInt32))(('JsAddRef', windll['chakra.dll']), ((1, 'ref'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRelease():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(UInt32))(('JsRelease', windll['chakra.dll']), ((1, 'ref'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetCurrentContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetCurrentContext', windll['chakra.dll']), ((1, 'currentContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetCurrentContext():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsSetCurrentContext', windll['chakra.dll']), ((1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetRuntime():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsGetRuntime', windll['chakra.dll']), ((1, 'context'),(1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIdle():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(UInt32))(('JsIdle', windll['chakra.dll']), ((1, 'nextIdleTick'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsParseScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p))(('JsParseScript', windll['chakra.dll']), ((1, 'script'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRunScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p))(('JsRunScript', windll['chakra.dll']), ((1, 'script'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSerializeScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32))(('JsSerializeScript', windll['chakra.dll']), ((1, 'script'),(1, 'buffer'),(1, 'bufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsParseSerializedScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,c_char_p_no,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p))(('JsParseSerializedScript', windll['chakra.dll']), ((1, 'script'),(1, 'buffer'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsRunSerializedScript():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,c_char_p_no,UIntPtr,win32more.Foundation.PWSTR,POINTER(c_void_p))(('JsRunSerializedScript', windll['chakra.dll']), ((1, 'script'),(1, 'buffer'),(1, 'sourceContext'),(1, 'sourceUrl'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPropertyIdFromName():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,POINTER(c_void_p))(('JsGetPropertyIdFromName', windll['chakra.dll']), ((1, 'name'),(1, 'propertyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPropertyNameFromId():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(POINTER(UInt16)))(('JsGetPropertyNameFromId', windll['chakra.dll']), ((1, 'propertyId'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetUndefinedValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetUndefinedValue', windll['chakra.dll']), ((1, 'undefinedValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetNullValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetNullValue', windll['chakra.dll']), ((1, 'nullValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetTrueValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetTrueValue', windll['chakra.dll']), ((1, 'trueValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetFalseValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetFalseValue', windll['chakra.dll']), ((1, 'falseValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsBoolToBoolean():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Byte,POINTER(c_void_p))(('JsBoolToBoolean', windll['chakra.dll']), ((1, 'value'),(1, 'booleanValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsBooleanToBool():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean))(('JsBooleanToBool', windll['chakra.dll']), ((1, 'value'),(1, 'boolValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToBoolean():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsConvertValueToBoolean', windll['chakra.dll']), ((1, 'value'),(1, 'booleanValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetValueType():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(win32more.System.Js.JsValueType))(('JsGetValueType', windll['chakra.dll']), ((1, 'value'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDoubleToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Double,POINTER(c_void_p))(('JsDoubleToNumber', windll['chakra.dll']), ((1, 'doubleValue'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIntToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,Int32,POINTER(c_void_p))(('JsIntToNumber', windll['chakra.dll']), ((1, 'intValue'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsNumberToDouble():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Double))(('JsNumberToDouble', windll['chakra.dll']), ((1, 'value'),(1, 'doubleValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToNumber():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsConvertValueToNumber', windll['chakra.dll']), ((1, 'value'),(1, 'numberValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetStringLength():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Int32))(('JsGetStringLength', windll['chakra.dll']), ((1, 'stringValue'),(1, 'length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsPointerToString():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.PWSTR,UIntPtr,POINTER(c_void_p))(('JsPointerToString', windll['chakra.dll']), ((1, 'stringValue'),(1, 'stringLength'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStringToPointer():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(POINTER(UInt16)),POINTER(UIntPtr))(('JsStringToPointer', windll['chakra.dll']), ((1, 'value'),(1, 'stringValue'),(1, 'stringLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToString():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsConvertValueToString', windll['chakra.dll']), ((1, 'value'),(1, 'stringValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsVariantToValue():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(win32more.System.Com.VARIANT_head),POINTER(c_void_p))(('JsVariantToValue', windll['chakra.dll']), ((1, 'variant'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsValueToVariant():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(win32more.System.Com.VARIANT_head))(('JsValueToVariant', windll['chakra.dll']), ((1, 'object'),(1, 'variant'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetGlobalObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetGlobalObject', windll['chakra.dll']), ((1, 'globalObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsCreateObject', windll['chakra.dll']), ((1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateExternalObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,win32more.System.Js.JsFinalizeCallback,POINTER(c_void_p))(('JsCreateExternalObject', windll['chakra.dll']), ((1, 'data'),(1, 'finalizeCallback'),(1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConvertValueToObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsConvertValueToObject', windll['chakra.dll']), ((1, 'value'),(1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetPrototype():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsGetPrototype', windll['chakra.dll']), ((1, 'object'),(1, 'prototypeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetPrototype():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p)(('JsSetPrototype', windll['chakra.dll']), ((1, 'object'),(1, 'prototypeObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetExtensionAllowed():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean))(('JsGetExtensionAllowed', windll['chakra.dll']), ((1, 'object'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsPreventExtension():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsPreventExtension', windll['chakra.dll']), ((1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p))(('JsGetProperty', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetOwnPropertyDescriptor():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p))(('JsGetOwnPropertyDescriptor', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'propertyDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetOwnPropertyNames():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsGetOwnPropertyNames', windll['chakra.dll']), ((1, 'object'),(1, 'propertyNames'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p,Byte)(('JsSetProperty', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'value'),(1, 'useStrictRules'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean))(('JsHasProperty', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'hasProperty'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDeleteProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,Byte,POINTER(c_void_p))(('JsDeleteProperty', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'useStrictRules'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDefineProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p,POINTER(Boolean))(('JsDefineProperty', windll['chakra.dll']), ((1, 'object'),(1, 'propertyId'),(1, 'propertyDescriptor'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean))(('JsHasIndexedProperty', windll['chakra.dll']), ((1, 'object'),(1, 'index'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(c_void_p))(('JsGetIndexedProperty', windll['chakra.dll']), ((1, 'object'),(1, 'index'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,c_void_p)(('JsSetIndexedProperty', windll['chakra.dll']), ((1, 'object'),(1, 'index'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDeleteIndexedProperty():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p)(('JsDeleteIndexedProperty', windll['chakra.dll']), ((1, 'object'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEquals():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean))(('JsEquals', windll['chakra.dll']), ((1, 'object1'),(1, 'object2'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStrictEquals():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p,POINTER(Boolean))(('JsStrictEquals', windll['chakra.dll']), ((1, 'object1'),(1, 'object2'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean))(('JsHasExternalData', windll['chakra.dll']), ((1, 'object'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsGetExternalData', windll['chakra.dll']), ((1, 'object'),(1, 'externalData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetExternalData():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,c_void_p)(('JsSetExternalData', windll['chakra.dll']), ((1, 'object'),(1, 'externalData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateArray():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,UInt32,POINTER(c_void_p))(('JsCreateArray', windll['chakra.dll']), ((1, 'length'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCallFunction():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p),UInt16,POINTER(c_void_p))(('JsCallFunction', windll['chakra.dll']), ((1, 'function'),(1, 'arguments'),(1, 'argumentCount'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsConstructObject():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p),UInt16,POINTER(c_void_p))(('JsConstructObject', windll['chakra.dll']), ((1, 'function'),(1, 'arguments'),(1, 'argumentCount'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateFunction():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Js.JsNativeFunction,c_void_p,POINTER(c_void_p))(('JsCreateFunction', windll['chakra.dll']), ((1, 'nativeFunction'),(1, 'callbackState'),(1, 'function'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateRangeError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateRangeError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateReferenceError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateReferenceError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateSyntaxError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateSyntaxError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateTypeError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateTypeError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsCreateURIError():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(c_void_p))(('JsCreateURIError', windll['chakra.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsHasException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(Boolean))(('JsHasException', windll['chakra.dll']), ((1, 'hasException'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsGetAndClearException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(c_void_p))(('JsGetAndClearException', windll['chakra.dll']), ((1, 'exception'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsSetException():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsSetException', windll['chakra.dll']), ((1, 'exception'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsDisableRuntimeExecution():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsDisableRuntimeExecution', windll['chakra.dll']), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEnableRuntimeExecution():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p)(('JsEnableRuntimeExecution', windll['chakra.dll']), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIsRuntimeExecutionDisabled():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,c_void_p,POINTER(Boolean))(('JsIsRuntimeExecutionDisabled', windll['chakra.dll']), ((1, 'runtime'),(1, 'isDisabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStartProfiling():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.System.Diagnostics.Debug.IActiveScriptProfilerCallback_head,win32more.System.Diagnostics.Debug.PROFILER_EVENT_MASK,UInt32)(('JsStartProfiling', windll['chakra.dll']), ((1, 'callback'),(1, 'eventMask'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsStopProfiling():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,win32more.Foundation.HRESULT)(('JsStopProfiling', windll['chakra.dll']), ((1, 'reason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsEnumerateHeap():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(win32more.System.Diagnostics.Debug.IActiveScriptProfilerHeapEnum_head))(('JsEnumerateHeap', windll['chakra.dll']), ((1, 'enumerator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsIsEnumeratingHeap():
    try:
        return WINFUNCTYPE(win32more.System.Js.JsErrorCode,POINTER(Boolean))(('JsIsEnumeratingHeap', windll['chakra.dll']), ((1, 'isEnumeratingHeap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JsBackgroundWorkItemCallback():
    return WINFUNCTYPE(Void,c_void_p)
def _define_JsBeforeCollectCallback():
    return WINFUNCTYPE(Void,c_void_p)
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
def _define_JsFinalizeCallback():
    return WINFUNCTYPE(Void,c_void_p)
def _define_JsMemoryAllocationCallback():
    return WINFUNCTYPE(Boolean,c_void_p,win32more.System.Js.JsMemoryEventType,UIntPtr)
JsMemoryEventType = Int32
JsMemoryEventType_JsMemoryAllocate = 0
JsMemoryEventType_JsMemoryFree = 1
JsMemoryEventType_JsMemoryFailure = 2
def _define_JsNativeFunction():
    return WINFUNCTYPE(c_void_p,c_void_p,Boolean,POINTER(c_void_p),UInt16,c_void_p)
JsRuntimeAttributes = Int32
JsRuntimeAttributes_JsRuntimeAttributeNone = 0
JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork = 1
JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt = 2
JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing = 4
JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration = 8
JsRuntimeAttributes_JsRuntimeAttributeDisableEval = 16
JsRuntimeVersion = Int32
JsRuntimeVersion_JsRuntimeVersion10 = 0
JsRuntimeVersion_JsRuntimeVersion11 = 1
JsRuntimeVersion_JsRuntimeVersionEdge = -1
def _define_JsThreadServiceCallback():
    return WINFUNCTYPE(Boolean,win32more.System.Js.JsBackgroundWorkItemCallback,c_void_p)
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
