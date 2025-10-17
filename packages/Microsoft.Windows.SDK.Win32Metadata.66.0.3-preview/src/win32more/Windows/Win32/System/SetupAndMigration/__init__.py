from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.SetupAndMigration
@winfunctype('KERNEL32.dll')
def OOBEComplete(isOOBEComplete: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterWaitUntilOOBECompleted(OOBECompletedCallback: win32more.Windows.Win32.System.SetupAndMigration.OOBE_COMPLETED_CALLBACK, CallbackContext: VoidPtr, WaitHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnregisterWaitUntilOOBECompleted(WaitHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def OOBE_COMPLETED_CALLBACK(CallbackContext: VoidPtr) -> Void: ...


make_ready(__name__)
