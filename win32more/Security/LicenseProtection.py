from win32more import *
import win32more.Security.LicenseProtection
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Security.LicenseProtection, name, eval(f"_define_{name}()"))
    return getattr(win32more.Security.LicenseProtection, name)
LicenseProtectionStatus = Int32
LicenseProtectionStatus_Success = 0
LicenseProtectionStatus_LicenseKeyNotFound = 1
LicenseProtectionStatus_LicenseKeyUnprotected = 2
LicenseProtectionStatus_LicenseKeyCorrupted = 3
LicenseProtectionStatus_LicenseKeyAlreadyExists = 4
def _define_RegisterLicenseKeyWithExpiration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus), use_last_error=False)(("RegisterLicenseKeyWithExpiration", windll["licenseprotection"]), ((1, 'licenseKey'),(1, 'validityInDays'),(1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidateLicenseKeyProtection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus), use_last_error=False)(("ValidateLicenseKeyProtection", windll["licenseprotection"]), ((1, 'licenseKey'),(1, 'notValidBefore'),(1, 'notValidAfter'),(1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "LicenseProtectionStatus",
    "LicenseProtectionStatus_Success",
    "LicenseProtectionStatus_LicenseKeyNotFound",
    "LicenseProtectionStatus_LicenseKeyUnprotected",
    "LicenseProtectionStatus_LicenseKeyCorrupted",
    "LicenseProtectionStatus_LicenseKeyAlreadyExists",
    "RegisterLicenseKeyWithExpiration",
    "ValidateLicenseKeyProtection",
]
