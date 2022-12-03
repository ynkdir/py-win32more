from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.CorrelationVector
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
RTL_CORRELATION_VECTOR_STRING_LENGTH = 129
RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH = 16
RTL_CORRELATION_VECTOR_V1_LENGTH = 64
RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH = 22
RTL_CORRELATION_VECTOR_V2_LENGTH = 128
def _define_RtlInitializeCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head),Int32,POINTER(Guid))(('RtlInitializeCorrelationVector', windll['ntdll.dll']), ((1, 'CorrelationVector'),(1, 'Version'),(1, 'Guid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlIncrementCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head))(('RtlIncrementCorrelationVector', windll['ntdll.dll']), ((1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlExtendCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head))(('RtlExtendCorrelationVector', windll['ntdll.dll']), ((1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlValidateCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head))(('RtlValidateCorrelationVector', windll['ntdll.dll']), ((1, 'Vector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CORRELATION_VECTOR_head():
    class CORRELATION_VECTOR(Structure):
        pass
    return CORRELATION_VECTOR
def _define_CORRELATION_VECTOR():
    CORRELATION_VECTOR = win32more.System.CorrelationVector.CORRELATION_VECTOR_head
    CORRELATION_VECTOR._fields_ = [
        ('Version', win32more.Foundation.CHAR),
        ('Vector', win32more.Foundation.CHAR * 129),
    ]
    return CORRELATION_VECTOR
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
