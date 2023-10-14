from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.LicenseProtection
@winfunctype('licenseprotection.dll')
def RegisterLicenseKeyWithExpiration(licenseKey: win32more.Windows.Win32.Foundation.PWSTR, validityInDays: UInt32, status: POINTER(win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('licenseprotection.dll')
def ValidateLicenseKeyProtection(licenseKey: win32more.Windows.Win32.Foundation.PWSTR, notValidBefore: POINTER(win32more.Windows.Win32.Foundation.FILETIME), notValidAfter: POINTER(win32more.Windows.Win32.Foundation.FILETIME), status: POINTER(win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LicenseProtectionStatus = Int32
LicenseProtectionStatus_Success: LicenseProtectionStatus = 0
LicenseProtectionStatus_LicenseKeyNotFound: LicenseProtectionStatus = 1
LicenseProtectionStatus_LicenseKeyUnprotected: LicenseProtectionStatus = 2
LicenseProtectionStatus_LicenseKeyCorrupted: LicenseProtectionStatus = 3
LicenseProtectionStatus_LicenseKeyAlreadyExists: LicenseProtectionStatus = 4
make_ready(__name__)
