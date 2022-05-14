from win32more import *
import win32more.System.PasswordManagement
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.PasswordManagement, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.PasswordManagement, name)
def _define_CYPHER_BLOCK_head():
    class CYPHER_BLOCK(Structure):
        pass
    return CYPHER_BLOCK
def _define_CYPHER_BLOCK():
    CYPHER_BLOCK = win32more.System.PasswordManagement.CYPHER_BLOCK_head
    CYPHER_BLOCK._fields_ = [
        ("data", win32more.Foundation.CHAR * 8),
    ]
    return CYPHER_BLOCK
def _define_LM_OWF_PASSWORD_head():
    class LM_OWF_PASSWORD(Structure):
        pass
    return LM_OWF_PASSWORD
def _define_LM_OWF_PASSWORD():
    LM_OWF_PASSWORD = win32more.System.PasswordManagement.LM_OWF_PASSWORD_head
    LM_OWF_PASSWORD._fields_ = [
        ("data", win32more.System.PasswordManagement.CYPHER_BLOCK * 2),
    ]
    return LM_OWF_PASSWORD
def _define_SAMPR_ENCRYPTED_USER_PASSWORD_head():
    class SAMPR_ENCRYPTED_USER_PASSWORD(Structure):
        pass
    return SAMPR_ENCRYPTED_USER_PASSWORD
def _define_SAMPR_ENCRYPTED_USER_PASSWORD():
    SAMPR_ENCRYPTED_USER_PASSWORD = win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head
    SAMPR_ENCRYPTED_USER_PASSWORD._fields_ = [
        ("Buffer", Byte * 516),
    ]
    return SAMPR_ENCRYPTED_USER_PASSWORD
def _define_ENCRYPTED_LM_OWF_PASSWORD_head():
    class ENCRYPTED_LM_OWF_PASSWORD(Structure):
        pass
    return ENCRYPTED_LM_OWF_PASSWORD
def _define_ENCRYPTED_LM_OWF_PASSWORD():
    ENCRYPTED_LM_OWF_PASSWORD = win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head
    ENCRYPTED_LM_OWF_PASSWORD._fields_ = [
        ("data", win32more.System.PasswordManagement.CYPHER_BLOCK * 2),
    ]
    return ENCRYPTED_LM_OWF_PASSWORD
def _define_MSChapSrvChangePassword():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN,POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head),POINTER(win32more.System.PasswordManagement.LM_OWF_PASSWORD_head), use_last_error=False)(("MSChapSrvChangePassword", windll["ADVAPI32"]), ((1, 'ServerName'),(1, 'UserName'),(1, 'LmOldPresent'),(1, 'LmOldOwfPassword'),(1, 'LmNewOwfPassword'),(1, 'NtOldOwfPassword'),(1, 'NtNewOwfPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MSChapSrvChangePassword2():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head),POINTER(win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head),POINTER(win32more.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head), use_last_error=False)(("MSChapSrvChangePassword2", windll["ADVAPI32"]), ((1, 'ServerName'),(1, 'UserName'),(1, 'NewPasswordEncryptedWithOldNt'),(1, 'OldNtOwfPasswordEncryptedWithNewNt'),(1, 'LmPresent'),(1, 'NewPasswordEncryptedWithOldLm'),(1, 'OldLmOwfPasswordEncryptedWithNewLmOrNt'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CYPHER_BLOCK",
    "LM_OWF_PASSWORD",
    "SAMPR_ENCRYPTED_USER_PASSWORD",
    "ENCRYPTED_LM_OWF_PASSWORD",
    "MSChapSrvChangePassword",
    "MSChapSrvChangePassword2",
]
