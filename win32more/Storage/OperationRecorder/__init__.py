from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.OperationRecorder
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
def _define_OperationStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head))(('OperationStart', windll['ADVAPI32.dll']), ((1, 'OperationStartParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OperationEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head))(('OperationEnd', windll['ADVAPI32.dll']), ((1, 'OperationEndParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OPERATION_END_PARAMETERS_head():
    class OPERATION_END_PARAMETERS(Structure):
        pass
    return OPERATION_END_PARAMETERS
def _define_OPERATION_END_PARAMETERS():
    OPERATION_END_PARAMETERS = win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head
    OPERATION_END_PARAMETERS._fields_ = [
        ('Version', UInt32),
        ('OperationId', UInt32),
        ('Flags', win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS),
    ]
    return OPERATION_END_PARAMETERS
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD = 1
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD = 1
def _define_OPERATION_START_PARAMETERS_head():
    class OPERATION_START_PARAMETERS(Structure):
        pass
    return OPERATION_START_PARAMETERS
def _define_OPERATION_START_PARAMETERS():
    OPERATION_START_PARAMETERS = win32more.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head
    OPERATION_START_PARAMETERS._fields_ = [
        ('Version', UInt32),
        ('OperationId', UInt32),
        ('Flags', win32more.Storage.OperationRecorder.OPERATION_START_FLAGS),
    ]
    return OPERATION_START_PARAMETERS
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
