from win32more import *
import win32more.NetworkManagement.WebDav
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.NetworkManagement.WebDav, name, globals()[f"_define_{name}"]())
    return getattr(win32more.NetworkManagement.WebDav, name)
def __dir__():
    return __all__
DAV_AUTHN_SCHEME_BASIC = 1
DAV_AUTHN_SCHEME_NTLM = 2
DAV_AUTHN_SCHEME_PASSPORT = 4
DAV_AUTHN_SCHEME_DIGEST = 8
DAV_AUTHN_SCHEME_NEGOTIATE = 16
DAV_AUTHN_SCHEME_CERT = 65536
DAV_AUTHN_SCHEME_FBA = 1048576
def _define_DAV_CALLBACK_AUTH_BLOB_head():
    class DAV_CALLBACK_AUTH_BLOB(Structure):
        pass
    return DAV_CALLBACK_AUTH_BLOB
def _define_DAV_CALLBACK_AUTH_BLOB():
    DAV_CALLBACK_AUTH_BLOB = win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_BLOB_head
    DAV_CALLBACK_AUTH_BLOB._fields_ = [
        ("pBuffer", c_void_p),
        ("ulSize", UInt32),
        ("ulType", UInt32),
    ]
    return DAV_CALLBACK_AUTH_BLOB
def _define_DAV_CALLBACK_AUTH_UNP_head():
    class DAV_CALLBACK_AUTH_UNP(Structure):
        pass
    return DAV_CALLBACK_AUTH_UNP
def _define_DAV_CALLBACK_AUTH_UNP():
    DAV_CALLBACK_AUTH_UNP = win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_UNP_head
    DAV_CALLBACK_AUTH_UNP._fields_ = [
        ("pszUserName", win32more.Foundation.PWSTR),
        ("ulUserNameLength", UInt32),
        ("pszPassword", win32more.Foundation.PWSTR),
        ("ulPasswordLength", UInt32),
    ]
    return DAV_CALLBACK_AUTH_UNP
def _define_DAV_CALLBACK_CRED_head():
    class DAV_CALLBACK_CRED(Structure):
        pass
    return DAV_CALLBACK_CRED
def _define_DAV_CALLBACK_CRED():
    DAV_CALLBACK_CRED = win32more.NetworkManagement.WebDav.DAV_CALLBACK_CRED_head
    DAV_CALLBACK_CRED._fields_ = [
        ("AuthBlob", win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_BLOB),
        ("UNPBlob", win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_UNP),
        ("bAuthBlobValid", win32more.Foundation.BOOL),
        ("bSave", win32more.Foundation.BOOL),
    ]
    return DAV_CALLBACK_CRED
AUTHNEXTSTEP = Int32
AUTHNEXTSTEP_DefaultBehavior = 0
AUTHNEXTSTEP_RetryRequest = 1
AUTHNEXTSTEP_CancelRequest = 2
def _define_PFNDAVAUTHCALLBACK_FREECRED():
    return CFUNCTYPE(UInt32,c_void_p, use_last_error=False)
def _define_PFNDAVAUTHCALLBACK():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.NetworkManagement.WebDav.DAV_CALLBACK_CRED_head),POINTER(win32more.NetworkManagement.WebDav.AUTHNEXTSTEP),POINTER(win32more.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK_FREECRED), use_last_error=False)
def _define_DavAddConnection():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32, use_last_error=False)(("DavAddConnection", windll["NETAPI32"]), ((1, 'ConnectionHandle'),(1, 'RemoteName'),(1, 'UserName'),(1, 'Password'),(1, 'ClientCert'),(1, 'CertSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavDeleteConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("DavDeleteConnection", windll["NETAPI32"]), ((1, 'ConnectionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavGetUNCFromHTTPPath():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("DavGetUNCFromHTTPPath", windll["NETAPI32"]), ((1, 'Url'),(1, 'UncPath'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavGetHTTPFromUNCPath():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("DavGetHTTPFromUNCPath", windll["NETAPI32"]), ((1, 'UncPath'),(1, 'Url'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavGetTheLockOwnerOfTheFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("DavGetTheLockOwnerOfTheFile", windll["davclnt"]), ((1, 'FileName'),(1, 'LockOwnerName'),(1, 'LockOwnerNameLengthInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavGetExtendedError():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)(("DavGetExtendedError", windll["NETAPI32"]), ((1, 'hFile'),(1, 'ExtError'),(1, 'ExtErrorString'),(1, 'cChSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavFlushFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("DavFlushFile", windll["NETAPI32"]), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavInvalidateCache():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("DavInvalidateCache", windll["davclnt"]), ((1, 'URLName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavCancelConnectionsToServer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("DavCancelConnectionsToServer", windll["davclnt"]), ((1, 'lpName'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavRegisterAuthCallback():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK,UInt32, use_last_error=False)(("DavRegisterAuthCallback", windll["davclnt"]), ((1, 'CallBack'),(1, 'Version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DavUnregisterAuthCallback():
    try:
        return WINFUNCTYPE(Void,UInt32, use_last_error=False)(("DavUnregisterAuthCallback", windll["davclnt"]), ((1, 'hCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DAV_AUTHN_SCHEME_BASIC",
    "DAV_AUTHN_SCHEME_NTLM",
    "DAV_AUTHN_SCHEME_PASSPORT",
    "DAV_AUTHN_SCHEME_DIGEST",
    "DAV_AUTHN_SCHEME_NEGOTIATE",
    "DAV_AUTHN_SCHEME_CERT",
    "DAV_AUTHN_SCHEME_FBA",
    "DAV_CALLBACK_AUTH_BLOB",
    "DAV_CALLBACK_AUTH_UNP",
    "DAV_CALLBACK_CRED",
    "AUTHNEXTSTEP",
    "AUTHNEXTSTEP_DefaultBehavior",
    "AUTHNEXTSTEP_RetryRequest",
    "AUTHNEXTSTEP_CancelRequest",
    "PFNDAVAUTHCALLBACK_FREECRED",
    "PFNDAVAUTHCALLBACK",
    "DavAddConnection",
    "DavDeleteConnection",
    "DavGetUNCFromHTTPPath",
    "DavGetHTTPFromUNCPath",
    "DavGetTheLockOwnerOfTheFile",
    "DavGetExtendedError",
    "DavFlushFile",
    "DavInvalidateCache",
    "DavCancelConnectionsToServer",
    "DavRegisterAuthCallback",
    "DavUnregisterAuthCallback",
]
