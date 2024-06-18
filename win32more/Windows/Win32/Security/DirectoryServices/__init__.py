from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Authorization.UI
import win32more.Windows.Win32.Security.DirectoryServices
import win32more.Windows.Win32.UI.Controls
DSSI_READ_ONLY: UInt32 = 1
DSSI_NO_ACCESS_CHECK: UInt32 = 2
DSSI_NO_EDIT_SACL: UInt32 = 4
DSSI_NO_EDIT_OWNER: UInt32 = 8
DSSI_IS_ROOT: UInt32 = 16
DSSI_NO_FILTER: UInt32 = 32
DSSI_NO_READONLY_MESSAGE: UInt32 = 64
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObject(pwszObjectPath: win32more.Windows.Win32.Foundation.PWSTR, pwszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation), pfnReadSD: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObjectEx(pwszObjectPath: win32more.Windows.Win32.Foundation.PWSTR, pwszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, pwszServer: win32more.Windows.Win32.Foundation.PWSTR, pwszUserName: win32more.Windows.Win32.Foundation.PWSTR, pwszPassword: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation), pfnReadSD: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateSecurityPage(pwszObjectPath: win32more.Windows.Win32.Foundation.PWSTR, pwszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, phPage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE), pfnReadSD: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSEditSecurity(hwndOwner: win32more.Windows.Win32.Foundation.HWND, pwszObjectPath: win32more.Windows.Win32.Foundation.PWSTR, pwszObjectClass: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pwszCaption: win32more.Windows.Win32.Foundation.PWSTR, pfnReadSD: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFO(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation), param4: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFOEX(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: win32more.Windows.Win32.Foundation.PWSTR, param4: win32more.Windows.Win32.Foundation.PWSTR, param5: UInt32, param6: POINTER(win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation), param7: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param8: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param9: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATESECPAGE(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE), param4: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSEDITSECURITY(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: UInt32, param4: win32more.Windows.Win32.Foundation.PWSTR, param5: win32more.Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param6: win32more.Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param7: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNREADOBJECTSECURITY(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), param3: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNWRITEOBJECTSECURITY(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, param3: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
