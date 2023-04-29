from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security.LicenseProtection
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('licenseprotection.dll')
def RegisterLicenseKeyWithExpiration(licenseKey: Windows.Win32.Foundation.PWSTR, validityInDays: UInt32, status: POINTER(Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('licenseprotection.dll')
def ValidateLicenseKeyProtection(licenseKey: Windows.Win32.Foundation.PWSTR, notValidBefore: POINTER(Windows.Win32.Foundation.FILETIME_head), notValidAfter: POINTER(Windows.Win32.Foundation.FILETIME_head), status: POINTER(Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> Windows.Win32.Foundation.HRESULT: ...
LicenseProtectionStatus = Int32
LicenseProtectionStatus_Success: LicenseProtectionStatus = 0
LicenseProtectionStatus_LicenseKeyNotFound: LicenseProtectionStatus = 1
LicenseProtectionStatus_LicenseKeyUnprotected: LicenseProtectionStatus = 2
LicenseProtectionStatus_LicenseKeyCorrupted: LicenseProtectionStatus = 3
LicenseProtectionStatus_LicenseKeyAlreadyExists: LicenseProtectionStatus = 4
