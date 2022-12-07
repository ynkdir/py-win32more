from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.OperationRecorder
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
@winfunctype('ADVAPI32.dll')
def OperationStart(OperationStartParams: POINTER(win32more.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OperationEnd(OperationEndParams: POINTER(win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head)) -> win32more.Foundation.BOOL: ...
class OPERATION_END_PARAMETERS(Structure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD: OPERATION_END_PARAMETERS_FLAGS = 1
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD: OPERATION_START_FLAGS = 1
class OPERATION_START_PARAMETERS(Structure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Storage.OperationRecorder.OPERATION_START_FLAGS
make_head(_module, 'OPERATION_END_PARAMETERS')
make_head(_module, 'OPERATION_START_PARAMETERS')
__all__ = [
    "OPERATION_END_DISCARD",
    "OPERATION_END_PARAMETERS",
    "OPERATION_END_PARAMETERS_FLAGS",
    "OPERATION_START_FLAGS",
    "OPERATION_START_PARAMETERS",
    "OPERATION_START_TRACE_CURRENT_THREAD",
    "OperationEnd",
    "OperationStart",
]
