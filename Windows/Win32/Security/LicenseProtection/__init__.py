from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
