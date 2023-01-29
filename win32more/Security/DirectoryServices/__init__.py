from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization.UI
import win32more.Security.DirectoryServices
import win32more.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
DSSI_READ_ONLY: UInt32 = 1
DSSI_NO_ACCESS_CHECK: UInt32 = 2
DSSI_NO_EDIT_SACL: UInt32 = 4
DSSI_NO_EDIT_OWNER: UInt32 = 8
DSSI_IS_ROOT: UInt32 = 16
DSSI_NO_FILTER: UInt32 = 32
DSSI_NO_READONLY_MESSAGE: UInt32 = 64
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObject(pwszObjectPath: win32more.Foundation.PWSTR, pwszObjectClass: win32more.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head), pfnReadSD: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObjectEx(pwszObjectPath: win32more.Foundation.PWSTR, pwszObjectClass: win32more.Foundation.PWSTR, pwszServer: win32more.Foundation.PWSTR, pwszUserName: win32more.Foundation.PWSTR, pwszPassword: win32more.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head), pfnReadSD: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateSecurityPage(pwszObjectPath: win32more.Foundation.PWSTR, pwszObjectClass: win32more.Foundation.PWSTR, dwFlags: UInt32, phPage: POINTER(win32more.UI.Controls.HPROPSHEETPAGE), pfnReadSD: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSEditSecurity(hwndOwner: win32more.Foundation.HWND, pwszObjectPath: win32more.Foundation.PWSTR, pwszObjectClass: win32more.Foundation.PWSTR, dwFlags: UInt32, pwszCaption: win32more.Foundation.PWSTR, pfnReadSD: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFO(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head), param4: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFOEX(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.PWSTR, param2: win32more.Foundation.PWSTR, param3: win32more.Foundation.PWSTR, param4: win32more.Foundation.PWSTR, param5: UInt32, param6: POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head), param7: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, param8: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param9: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATESECPAGE(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.PWSTR, param2: UInt32, param3: POINTER(win32more.UI.Controls.HPROPSHEETPAGE), param4: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSEDITSECURITY(param0: win32more.Foundation.HWND, param1: win32more.Foundation.PWSTR, param2: win32more.Foundation.PWSTR, param3: UInt32, param4: win32more.Foundation.PWSTR, param5: win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY, param6: win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param7: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNREADOBJECTSECURITY(param0: win32more.Foundation.PWSTR, param1: UInt32, param2: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), param3: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNWRITEOBJECTSECURITY(param0: win32more.Foundation.PWSTR, param1: UInt32, param2: win32more.Security.PSECURITY_DESCRIPTOR, param3: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'PFNDSCREATEISECINFO')
make_head(_module, 'PFNDSCREATEISECINFOEX')
make_head(_module, 'PFNDSCREATESECPAGE')
make_head(_module, 'PFNDSEDITSECURITY')
make_head(_module, 'PFNREADOBJECTSECURITY')
make_head(_module, 'PFNWRITEOBJECTSECURITY')
__all__ = [
    "DSCreateISecurityInfoObject",
    "DSCreateISecurityInfoObjectEx",
    "DSCreateSecurityPage",
    "DSEditSecurity",
    "DSSI_IS_ROOT",
    "DSSI_NO_ACCESS_CHECK",
    "DSSI_NO_EDIT_OWNER",
    "DSSI_NO_EDIT_SACL",
    "DSSI_NO_FILTER",
    "DSSI_NO_READONLY_MESSAGE",
    "DSSI_READ_ONLY",
    "PFNDSCREATEISECINFO",
    "PFNDSCREATEISECINFOEX",
    "PFNDSCREATESECPAGE",
    "PFNDSEDITSECURITY",
    "PFNREADOBJECTSECURITY",
    "PFNWRITEOBJECTSECURITY",
]
_arch_optional = [
]
