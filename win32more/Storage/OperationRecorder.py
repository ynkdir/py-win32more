from win32more import *
import win32more.Storage.OperationRecorder
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Storage.OperationRecorder, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Storage.OperationRecorder, name)
def __dir__():
    return __all__
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD = 1
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD = 1
def _define_OPERATION_START_PARAMETERS_head():
    class OPERATION_START_PARAMETERS(Structure):
        pass
    return OPERATION_START_PARAMETERS
def _define_OPERATION_START_PARAMETERS():
    OPERATION_START_PARAMETERS = win32more.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head
    OPERATION_START_PARAMETERS._fields_ = [
        ("Version", UInt32),
        ("OperationId", UInt32),
        ("Flags", win32more.Storage.OperationRecorder.OPERATION_START_FLAGS),
    ]
    return OPERATION_START_PARAMETERS
def _define_OPERATION_END_PARAMETERS_head():
    class OPERATION_END_PARAMETERS(Structure):
        pass
    return OPERATION_END_PARAMETERS
def _define_OPERATION_END_PARAMETERS():
    OPERATION_END_PARAMETERS = win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head
    OPERATION_END_PARAMETERS._fields_ = [
        ("Version", UInt32),
        ("OperationId", UInt32),
        ("Flags", win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS),
    ]
    return OPERATION_END_PARAMETERS
def _define_OperationStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head), use_last_error=False)(("OperationStart", windll["ADVAPI32"]), ((1, 'OperationStartParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OperationEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head), use_last_error=False)(("OperationEnd", windll["ADVAPI32"]), ((1, 'OperationEndParams'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "OPERATION_START_FLAGS",
    "OPERATION_START_TRACE_CURRENT_THREAD",
    "OPERATION_END_PARAMETERS_FLAGS",
    "OPERATION_END_DISCARD",
    "OPERATION_START_PARAMETERS",
    "OPERATION_END_PARAMETERS",
    "OperationStart",
    "OperationEnd",
]
