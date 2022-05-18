from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization.UI
import win32more.Security.DirectoryServices
import win32more.UI.Controls

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
DSSI_READ_ONLY = 1
DSSI_NO_ACCESS_CHECK = 2
DSSI_NO_EDIT_SACL = 4
DSSI_NO_EDIT_OWNER = 8
DSSI_IS_ROOT = 16
DSSI_NO_FILTER = 32
DSSI_NO_READONLY_MESSAGE = 64
def _define_PFNREADOBJECTSECURITY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),win32more.Foundation.LPARAM, use_last_error=False)
def _define_PFNWRITEOBJECTSECURITY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.LPARAM, use_last_error=False)
def _define_PFNDSCREATEISECINFO():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PFNDSCREATEISECINFOEX():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PFNDSCREATESECPAGE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.Controls.HPROPSHEETPAGE),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PFNDSEDITSECURITY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)
def _define_DSCreateISecurityInfoObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)(("DSCreateISecurityInfoObject", windll["DSSEC"]), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'ppSI'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSCreateISecurityInfoObjectEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)(("DSCreateISecurityInfoObjectEx", windll["DSSEC"]), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'pwszServer'),(1, 'pwszUserName'),(1, 'pwszPassword'),(1, 'dwFlags'),(1, 'ppSI'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSCreateSecurityPage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.Controls.HPROPSHEETPAGE),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)(("DSCreateSecurityPage", windll["DSSEC"]), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'phPage'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSEditSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM, use_last_error=False)(("DSEditSecurity", windll["DSSEC"]), ((1, 'hwndOwner'),(1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'pwszCaption'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DSSI_READ_ONLY",
    "DSSI_NO_ACCESS_CHECK",
    "DSSI_NO_EDIT_SACL",
    "DSSI_NO_EDIT_OWNER",
    "DSSI_IS_ROOT",
    "DSSI_NO_FILTER",
    "DSSI_NO_READONLY_MESSAGE",
    "PFNREADOBJECTSECURITY",
    "PFNWRITEOBJECTSECURITY",
    "PFNDSCREATEISECINFO",
    "PFNDSCREATEISECINFOEX",
    "PFNDSCREATESECPAGE",
    "PFNDSEDITSECURITY",
    "DSCreateISecurityInfoObject",
    "DSCreateISecurityInfoObjectEx",
    "DSCreateSecurityPage",
    "DSEditSecurity",
]
