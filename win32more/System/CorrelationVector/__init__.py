from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.CorrelationVector
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
RTL_CORRELATION_VECTOR_STRING_LENGTH: UInt32 = 129
RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH: UInt32 = 16
RTL_CORRELATION_VECTOR_V1_LENGTH: UInt32 = 64
RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH: UInt32 = 22
RTL_CORRELATION_VECTOR_V2_LENGTH: UInt32 = 128
@winfunctype('ntdll.dll')
def RtlInitializeCorrelationVector(CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), Version: Int32, Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlIncrementCorrelationVector(CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlExtendCorrelationVector(CorrelationVector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlValidateCorrelationVector(Vector: POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
class CORRELATION_VECTOR(Structure):
    Version: win32more.Foundation.CHAR
    Vector: win32more.Foundation.CHAR * 129
make_head(_module, 'CORRELATION_VECTOR')
__all__ = [
    "CORRELATION_VECTOR",
    "RTL_CORRELATION_VECTOR_STRING_LENGTH",
    "RTL_CORRELATION_VECTOR_V1_LENGTH",
    "RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH",
    "RTL_CORRELATION_VECTOR_V2_LENGTH",
    "RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH",
    "RtlExtendCorrelationVector",
    "RtlIncrementCorrelationVector",
    "RtlInitializeCorrelationVector",
    "RtlValidateCorrelationVector",
]
