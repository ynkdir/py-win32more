from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Time
wszW32TimeRegKeyTimeProviders: String = 'System\\CurrentControlSet\\Services\\W32Time\\TimeProviders'
wszW32TimeRegKeyPolicyTimeProviders: String = 'Software\\Policies\\Microsoft\\W32Time\\TimeProviders'
wszW32TimeRegValueEnabled: String = 'Enabled'
wszW32TimeRegValueDllName: String = 'DllName'
wszW32TimeRegValueInputProvider: String = 'InputProvider'
wszW32TimeRegValueMetaDataProvider: String = 'MetaDataProvider'
TSF_Hardware: UInt32 = 1
TSF_Authenticated: UInt32 = 2
TSF_IPv6: UInt32 = 4
TSF_SignatureAuthenticated: UInt32 = 8
TIME_ZONE_ID_INVALID: UInt32 = 4294967295
@winfunctype('KERNEL32.dll')
def SystemTimeToTzSpecificLocalTime(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION), lpUniversalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), lpLocalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TzSpecificLocalTimeToSystemTime(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION), lpLocalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), lpUniversalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FileTimeToSystemTime(lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SystemTimeToFileTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTimeZoneInformation(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetTimeZoneInformation(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDynamicTimeZoneInformation(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDynamicTimeZoneInformation(pTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTimeZoneInformationForYear(wYear: UInt16, pdtzi: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION), ptzi: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDynamicTimeZoneInformation(dwIndex: UInt32, lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetDynamicTimeZoneInformationEffectiveYears(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION), FirstYear: POINTER(UInt32), LastYear: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SystemTimeToTzSpecificLocalTimeEx(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION), lpUniversalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), lpLocalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TzSpecificLocalTimeToSystemTimeEx(lpTimeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION), lpLocalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), lpUniversalTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalFileTimeToLocalSystemTime(timeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION), localFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), localSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalSystemTimeToLocalFileTime(timeZoneInformation: POINTER(win32more.Windows.Win32.System.Time.TIME_ZONE_INFORMATION), localSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), localFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class DYNAMIC_TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: win32more.Windows.Win32.Foundation.SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DaylightBias: Int32
    TimeZoneKeyName: Char * 128
    DynamicDaylightTimeDisabled: win32more.Windows.Win32.Foundation.BOOLEAN
class TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: win32more.Windows.Win32.Foundation.SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: win32more.Windows.Win32.Foundation.SYSTEMTIME
    DaylightBias: Int32


make_ready(__name__)
