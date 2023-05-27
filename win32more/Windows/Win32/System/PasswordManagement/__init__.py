from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.PasswordManagement
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
def MSChapSrvChangePassword(ServerName: win32more.Windows.Win32.Foundation.PWSTR, UserName: win32more.Windows.Win32.Foundation.PWSTR, LmOldPresent: win32more.Windows.Win32.Foundation.BOOLEAN, LmOldOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), LmNewOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), NtOldOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), NtNewOwfPassword: POINTER(win32more.Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def MSChapSrvChangePassword2(ServerName: win32more.Windows.Win32.Foundation.PWSTR, UserName: win32more.Windows.Win32.Foundation.PWSTR, NewPasswordEncryptedWithOldNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head), OldNtOwfPasswordEncryptedWithNewNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head), LmPresent: win32more.Windows.Win32.Foundation.BOOLEAN, NewPasswordEncryptedWithOldLm: POINTER(win32more.Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head), OldLmOwfPasswordEncryptedWithNewLmOrNt: POINTER(win32more.Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head)) -> UInt32: ...
class CYPHER_BLOCK(EasyCastStructure):
    data: win32more.Windows.Win32.Foundation.CHAR * 8
class ENCRYPTED_LM_OWF_PASSWORD(EasyCastStructure):
    data: win32more.Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class LM_OWF_PASSWORD(EasyCastStructure):
    data: win32more.Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class SAMPR_ENCRYPTED_USER_PASSWORD(EasyCastStructure):
    Buffer: Byte * 516
make_head(_module, 'CYPHER_BLOCK')
make_head(_module, 'ENCRYPTED_LM_OWF_PASSWORD')
make_head(_module, 'LM_OWF_PASSWORD')
make_head(_module, 'SAMPR_ENCRYPTED_USER_PASSWORD')
