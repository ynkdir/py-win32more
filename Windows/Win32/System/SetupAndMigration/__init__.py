from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.SetupAndMigration
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('KERNEL32.dll')
def OOBEComplete(isOOBEComplete: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterWaitUntilOOBECompleted(OOBECompletedCallback: Windows.Win32.System.SetupAndMigration.OOBE_COMPLETED_CALLBACK, CallbackContext: VoidPtr, WaitHandle: POINTER(VoidPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitUntilOOBECompleted(WaitHandle: VoidPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def OOBE_COMPLETED_CALLBACK(CallbackContext: VoidPtr) -> Void: ...
make_head(_module, 'OOBE_COMPLETED_CALLBACK')
