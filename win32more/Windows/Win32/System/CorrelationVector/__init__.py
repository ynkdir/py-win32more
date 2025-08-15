from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.CorrelationVector
RTL_CORRELATION_VECTOR_STRING_LENGTH: UInt32 = 129
RTL_CORRELATION_VECTOR_V1_PREFIX_LENGTH: UInt32 = 16
RTL_CORRELATION_VECTOR_V1_LENGTH: UInt32 = 64
RTL_CORRELATION_VECTOR_V2_PREFIX_LENGTH: UInt32 = 22
RTL_CORRELATION_VECTOR_V2_LENGTH: UInt32 = 128
@winfunctype('ntdll.dll')
def RtlInitializeCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR), Version: Int32, Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlIncrementCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlExtendCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlValidateCorrelationVector(Vector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR)) -> UInt32: ...
class CORRELATION_VECTOR(Structure):
    Version: win32more.Windows.Win32.Foundation.CHAR
    Vector: win32more.Windows.Win32.Foundation.CHAR * 129


make_ready(__name__)
