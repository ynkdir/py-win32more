from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.OperationRecorder
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
def OperationStart(OperationStartParams: POINTER(win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_START_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OperationEnd(OperationEndParams: POINTER(win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class OPERATION_END_PARAMETERS(EasyCastStructure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD: OPERATION_END_PARAMETERS_FLAGS = 1
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD: OPERATION_START_FLAGS = 1
class OPERATION_START_PARAMETERS(EasyCastStructure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_START_FLAGS
make_head(_module, 'OPERATION_END_PARAMETERS')
make_head(_module, 'OPERATION_START_PARAMETERS')
