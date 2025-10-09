from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.OperationRecorder
@winfunctype('ADVAPI32.dll')
def OperationStart(OperationStartParams: POINTER(win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_START_PARAMETERS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def OperationEnd(OperationEndParams: POINTER(win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class OPERATION_END_PARAMETERS(Structure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS
OPERATION_END_PARAMETERS_FLAGS = UInt32
OPERATION_END_DISCARD: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_END_PARAMETERS_FLAGS = 1
OPERATION_START_FLAGS = UInt32
OPERATION_START_TRACE_CURRENT_THREAD: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_START_FLAGS = 1
class OPERATION_START_PARAMETERS(Structure):
    Version: UInt32
    OperationId: UInt32
    Flags: win32more.Windows.Win32.Storage.OperationRecorder.OPERATION_START_FLAGS


make_ready(__name__)
