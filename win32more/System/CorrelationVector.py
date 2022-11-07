from win32more.base import *
import win32more.Foundation
import win32more.System.CorrelationVector

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
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
def _define_CORRELATION_VECTOR_head():
    class CORRELATION_VECTOR(Structure):
        pass
    return CORRELATION_VECTOR
def _define_CORRELATION_VECTOR():
    CORRELATION_VECTOR = win32more.System.CorrelationVector.CORRELATION_VECTOR_head
    CORRELATION_VECTOR._fields_ = [
        ("Version", win32more.Foundation.CHAR),
        ("Vector", win32more.Foundation.CHAR * 129),
    ]
    return CORRELATION_VECTOR
def _define_RtlInitializeCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head),Int32,POINTER(Guid), use_last_error=False)(("RtlInitializeCorrelationVector", windll["ntdll"]), ((1, 'CorrelationVector'),(1, 'Version'),(1, 'Guid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlIncrementCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), use_last_error=False)(("RtlIncrementCorrelationVector", windll["ntdll"]), ((1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlExtendCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), use_last_error=False)(("RtlExtendCorrelationVector", windll["ntdll"]), ((1, 'CorrelationVector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlValidateCorrelationVector():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.CorrelationVector.CORRELATION_VECTOR_head), use_last_error=False)(("RtlValidateCorrelationVector", windll["ntdll"]), ((1, 'Vector'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "RTL_CORRELATION_VECTOR_STRING_LENGTH",
    "RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH",
    "RTL_CORRELATION_VECTOR_V1_LENGTH",
    "RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH",
    "RTL_CORRELATION_VECTOR_V2_LENGTH",
    "CORRELATION_VECTOR",
    "RtlInitializeCorrelationVector",
    "RtlIncrementCorrelationVector",
    "RtlExtendCorrelationVector",
    "RtlValidateCorrelationVector",
]
