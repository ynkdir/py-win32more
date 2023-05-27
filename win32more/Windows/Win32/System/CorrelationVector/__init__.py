from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.CorrelationVector
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
def RtlInitializeCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head), Version: Int32, Guid: POINTER(Guid)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlIncrementCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlExtendCorrelationVector(CorrelationVector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlValidateCorrelationVector(Vector: POINTER(win32more.Windows.Win32.System.CorrelationVector.CORRELATION_VECTOR_head)) -> UInt32: ...
class CORRELATION_VECTOR(EasyCastStructure):
    Version: win32more.Windows.Win32.Foundation.CHAR
    Vector: win32more.Windows.Win32.Foundation.CHAR * 129
make_head(_module, 'CORRELATION_VECTOR')
