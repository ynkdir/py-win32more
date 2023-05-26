from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.Authorization.UI
import Windows.Win32.Security.DirectoryServices
import Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DSSI_READ_ONLY: UInt32 = 1
DSSI_NO_ACCESS_CHECK: UInt32 = 2
DSSI_NO_EDIT_SACL: UInt32 = 4
DSSI_NO_EDIT_OWNER: UInt32 = 8
DSSI_IS_ROOT: UInt32 = 16
DSSI_NO_FILTER: UInt32 = 32
DSSI_NO_READONLY_MESSAGE: UInt32 = 64
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObject(pwszObjectPath: Windows.Win32.Foundation.PWSTR, pwszObjectClass: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(Windows.Win32.Security.Authorization.UI.ISecurityInformation_head), pfnReadSD: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateISecurityInfoObjectEx(pwszObjectPath: Windows.Win32.Foundation.PWSTR, pwszObjectClass: Windows.Win32.Foundation.PWSTR, pwszServer: Windows.Win32.Foundation.PWSTR, pwszUserName: Windows.Win32.Foundation.PWSTR, pwszPassword: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppSI: POINTER(Windows.Win32.Security.Authorization.UI.ISecurityInformation_head), pfnReadSD: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSCreateSecurityPage(pwszObjectPath: Windows.Win32.Foundation.PWSTR, pwszObjectClass: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, phPage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE), pfnReadSD: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DSSEC.dll')
def DSEditSecurity(hwndOwner: Windows.Win32.Foundation.HWND, pwszObjectPath: Windows.Win32.Foundation.PWSTR, pwszObjectClass: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pwszCaption: Windows.Win32.Foundation.PWSTR, pfnReadSD: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, pfnWriteSD: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, lpContext: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFO(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(Windows.Win32.Security.Authorization.UI.ISecurityInformation_head), param4: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATEISECINFOEX(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, param3: Windows.Win32.Foundation.PWSTR, param4: Windows.Win32.Foundation.PWSTR, param5: UInt32, param6: POINTER(Windows.Win32.Security.Authorization.UI.ISecurityInformation_head), param7: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param8: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param9: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSCREATESECPAGE(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE), param4: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param5: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param6: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNDSEDITSECURITY(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, param3: UInt32, param4: Windows.Win32.Foundation.PWSTR, param5: Windows.Win32.Security.DirectoryServices.PFNREADOBJECTSECURITY, param6: Windows.Win32.Security.DirectoryServices.PFNWRITEOBJECTSECURITY, param7: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNREADOBJECTSECURITY(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNWRITEOBJECTSECURITY(param0: Windows.Win32.Foundation.PWSTR, param1: UInt32, param2: Windows.Win32.Security.PSECURITY_DESCRIPTOR, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'PFNDSCREATEISECINFO')
make_head(_module, 'PFNDSCREATEISECINFOEX')
make_head(_module, 'PFNDSCREATESECPAGE')
make_head(_module, 'PFNDSEDITSECURITY')
make_head(_module, 'PFNREADOBJECTSECURITY')
make_head(_module, 'PFNWRITEOBJECTSECURITY')
