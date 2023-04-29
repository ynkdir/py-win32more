from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Storage.OperationRecorder
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('ADVAPI32.dll')
def OperationStart(OperationStartParams: POINTER(Windows.Win32.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OperationEnd(OperationEndParams: POINTER(Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head)) -> Windows.Win32.Foundation.BOOL: ...
class OPERATION_END_PARAMETERS(EasyCastStructure):
    Version: UInt32
    OperationId: UInt32
    Flags: Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD: OPERATION_END_PARAMETERS_FLAGS = 1
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD: OPERATION_START_FLAGS = 1
class OPERATION_START_PARAMETERS(EasyCastStructure):
    Version: UInt32
    OperationId: UInt32
    Flags: Windows.Win32.Storage.OperationRecorder.OPERATION_START_FLAGS
make_head(_module, 'OPERATION_END_PARAMETERS')
make_head(_module, 'OPERATION_START_PARAMETERS')
