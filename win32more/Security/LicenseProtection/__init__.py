from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.LicenseProtection
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('licenseprotection.dll')
def RegisterLicenseKeyWithExpiration(licenseKey: win32more.Foundation.PWSTR, validityInDays: UInt32, status: POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Foundation.HRESULT: ...
@winfunctype('licenseprotection.dll')
def ValidateLicenseKeyProtection(licenseKey: win32more.Foundation.PWSTR, notValidBefore: POINTER(win32more.Foundation.FILETIME_head), notValidAfter: POINTER(win32more.Foundation.FILETIME_head), status: POINTER(win32more.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Foundation.HRESULT: ...
LicenseProtectionStatus = Int32
LicenseProtectionStatus_Success: LicenseProtectionStatus = 0
LicenseProtectionStatus_LicenseKeyNotFound: LicenseProtectionStatus = 1
LicenseProtectionStatus_LicenseKeyUnprotected: LicenseProtectionStatus = 2
LicenseProtectionStatus_LicenseKeyCorrupted: LicenseProtectionStatus = 3
LicenseProtectionStatus_LicenseKeyAlreadyExists: LicenseProtectionStatus = 4
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
