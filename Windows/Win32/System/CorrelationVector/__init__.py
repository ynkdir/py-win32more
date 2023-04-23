from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.CorrelationVector
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
RTL_CORRELATION_VECTOR_STRING_LENGTH: UInt32 = 129
RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH: UInt32 = 16
RTL_CORRELATION_VECTOR_V1_LENGTH: UInt32 = 64
RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH: UInt32 = 22
RTL_CORRELATION_VECTOR_V2_LENGTH: UInt32 = 128
@winfunctype('ntdll.dll')
def RtlInitializeCorrelationVector(CorrelationVector: POINTER(Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head), Version: Int32, Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlIncrementCorrelationVector(CorrelationVector: POINTER(Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlExtendCorrelationVector(CorrelationVector: POINTER(Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlValidateCorrelationVector(Vector: POINTER(Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
class CORRELATION_VECTOR(EasyCastStructure):
    Version: Windows.Win32.Foundation.CHAR
    Vector: Windows.Win32.Foundation.CHAR * 129
make_head(_module, 'CORRELATION_VECTOR')
