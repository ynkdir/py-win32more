from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.LicenseProtection
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
def _define_RegisterLicenseKeyWithExpiration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus))(('RegisterLicenseKeyWithExpiration', windll['licenseprotection.dll']), ((1, 'licenseKey'),(1, 'validityInDays'),(1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidateLicenseKeyProtection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus))(('ValidateLicenseKeyProtection', windll['licenseprotection.dll']), ((1, 'licenseKey'),(1, 'notValidBefore'),(1, 'notValidAfter'),(1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
LicenseProtectionStatus = Int32
LicenseProtectionStatus_Success = 0
LicenseProtectionStatus_LicenseKeyNotFound = 1
LicenseProtectionStatus_LicenseKeyUnprotected = 2
LicenseProtectionStatus_LicenseKeyCorrupted = 3
LicenseProtectionStatus_LicenseKeyAlreadyExists = 4
__all__ = [
    "LicenseProtectionStatus",
    "LicenseProtectionStatus_LicenseKeyAlreadyExists",
    "LicenseProtectionStatus_LicenseKeyCorrupted",
    "LicenseProtectionStatus_LicenseKeyNotFound",
    "LicenseProtectionStatus_LicenseKeyUnprotected",
    "LicenseProtectionStatus_Success",
    "RegisterLicenseKeyWithExpiration",
    "ValidateLicenseKeyProtection",
]
