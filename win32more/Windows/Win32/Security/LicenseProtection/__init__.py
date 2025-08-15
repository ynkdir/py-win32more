from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.LicenseProtection
@winfunctype('licenseprotection.dll')
def RegisterLicenseKeyWithExpiration(licenseKey: win32more.Windows.Win32.Foundation.PWSTR, validityInDays: UInt32, status: POINTER(win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('licenseprotection.dll')
def ValidateLicenseKeyProtection(licenseKey: win32more.Windows.Win32.Foundation.PWSTR, notValidBefore: POINTER(win32more.Windows.Win32.Foundation.FILETIME), notValidAfter: POINTER(win32more.Windows.Win32.Foundation.FILETIME), status: POINTER(win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LicenseProtectionStatus = Int32
Success: win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus = 0
LicenseKeyNotFound: win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus = 1
LicenseKeyUnprotected: win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus = 2
LicenseKeyCorrupted: win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus = 3
LicenseKeyAlreadyExists: win32more.Windows.Win32.Security.LicenseProtection.LicenseProtectionStatus = 4


make_ready(__name__)
