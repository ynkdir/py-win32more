from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.PasswordManagement
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
def _define_MSChapSrvChangePassword():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN,POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head))(('MSChapSrvChangePassword', windll['ADVAPI32.dll']), ((1, 'ServerName'),(1, 'UserName'),(1, 'LmOldPresent'),(1, 'LmOldOwfPassword'),(1, 'LmNewOwfPassword'),(1, 'NtOldOwfPassword'),(1, 'NtNewOwfPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MSChapSrvChangePassword2():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head),POINTER(win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head),POINTER(win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head))(('MSChapSrvChangePassword2', windll['ADVAPI32.dll']), ((1, 'ServerName'),(1, 'UserName'),(1, 'NewPasswordEncryptedWithOldNt'),(1, 'OldNtOwfPasswordEncryptedWithNewNt'),(1, 'LmPresent'),(1, 'NewPasswordEncryptedWithOldLm'),(1, 'OldLmOwfPasswordEncryptedWithNewLmOrNt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CYPHER_BLOCK_head():
    class CYPHER_BLOCK(Structure):
        pass
    return CYPHER_BLOCK
def _define_CYPHER_BLOCK():
    CYPHER_BLOCK = win32more.System.PasswordManagement.CYPHER_BLOCK_head
    CYPHER_BLOCK._fields_ = [
        ('data', win32more.Foundation.CHAR * 8),
    ]
    return CYPHER_BLOCK
def _define_ENCRYPTED_LM_OWF_PASSWORD_head():
    class ENCRYPTED_LM_OWF_PASSWORD(Structure):
        pass
    return ENCRYPTED_LM_OWF_PASSWORD
def _define_ENCRYPTED_LM_OWF_PASSWORD():
    ENCRYPTED_LM_OWF_PASSWORD = win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head
    ENCRYPTED_LM_OWF_PASSWORD._fields_ = [
        ('data', win32more.System.PasswordManagement.CYPHER_BLOCK * 2),
    ]
    return ENCRYPTED_LM_OWF_PASSWORD
def _define_LM_OWF_PASSWORD_head():
    class LM_OWF_PASSWORD(Structure):
        pass
    return LM_OWF_PASSWORD
def _define_LM_OWF_PASSWORD():
    LM_OWF_PASSWORD = win32more.System.PasswordManagement.LM_OWF_PASSWORD_head
    LM_OWF_PASSWORD._fields_ = [
        ('data', win32more.System.PasswordManagement.CYPHER_BLOCK * 2),
    ]
    return LM_OWF_PASSWORD
def _define_SAMPR_ENCRYPTED_USER_PASSWORD_head():
    class SAMPR_ENCRYPTED_USER_PASSWORD(Structure):
        pass
    return SAMPR_ENCRYPTED_USER_PASSWORD
def _define_SAMPR_ENCRYPTED_USER_PASSWORD():
    SAMPR_ENCRYPTED_USER_PASSWORD = win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head
    SAMPR_ENCRYPTED_USER_PASSWORD._fields_ = [
        ('Buffer', Byte * 516),
    ]
    return SAMPR_ENCRYPTED_USER_PASSWORD
__all__ = [
    "CYPHER_BLOCK",
    "ENCRYPTED_LM_OWF_PASSWORD",
    "LM_OWF_PASSWORD",
    "MSChapSrvChangePassword",
    "MSChapSrvChangePassword2",
    "SAMPR_ENCRYPTED_USER_PASSWORD",
]
