from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
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
def RegisterWaitUntilOOBECompleted(OOBECompletedCallback: Windows.Win32.System.SetupAndMigration.OOBE_COMPLETED_CALLBACK, CallbackContext: c_void_p, WaitHandle: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitUntilOOBECompleted(WaitHandle: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def OOBE_COMPLETED_CALLBACK(CallbackContext: c_void_p) -> Void: ...
make_head(_module, 'OOBE_COMPLETED_CALLBACK')
